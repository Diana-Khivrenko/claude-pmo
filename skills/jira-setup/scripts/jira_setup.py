#!/usr/bin/env python3
"""Snotor Jira standard: audit, plan and apply the parts of a Jira project
setup that the Jira REST API supports.

Covers: project style, issue types, the project's issue type scheme, the
QA Assignee field with its context and screens, the Blocks link type, the
Flagged field, statuses per issue type, and board filters plus boards.
Workflow transitions, board columns, quick filters, Slack and Marketplace
apps are done in the browser (see references/chrome-steps.md).

Standard library only, so it runs on any machine with Python 3.8+.

Usage:
  python3 jira_setup.py audit --config jira-setup.json --env /path/jira.env
  python3 jira_setup.py plan  --config jira-setup.json --env /path/jira.env
  python3 jira_setup.py apply --config jira-setup.json --env /path/jira.env [--allow-shared]

The env file holds two lines the person writes themselves:
  JIRA_EMAIL=name@company.com
  JIRA_API_TOKEN=...
The token is never printed.
"""

import argparse
import base64
import json
import sys
import urllib.error
import urllib.parse
import urllib.request

STANDARD_TYPES = [
    # name, hierarchy level, description used only when the type is created
    ("Epic", 1, None),
    ("Feature", 0, "One use case of the product. The parent of one sub-task per platform."),
    ("Task", 0, "Product work that is not a use case."),
    ("Technical task", 0, "Infrastructure, security, CI or tech debt work."),
    ("Sub-task", -1, "One platform's part of a Feature."),
    ("Technical Sub-task", -1, "Technical work under a Technical task. Needs no QA."),
    ("Bug Sub-Task", -1, "A defect found in testing, under the Feature it breaks."),
]
STANDARD_STATUSES = [
    "Backlog", "To Do", "Blocked (Comment required)", "Failed QA", "In Progress",
    "Code review", "Ready for deploy", "Ready for QA", "Testing (QA)", "Done",
]
# Same step under another name: mapped to the standard name when aligning a project
STATUS_ALIASES = {"Review": "Code review", "Testing": "Testing (QA)"}
QA_FIELD_NAME = "QA Assignee"
QA_FIELD_TYPE = "com.atlassian.jira.plugin.system.customfieldtypes:userpicker"
QA_FIELD_SEARCHER = "com.atlassian.jira.plugin.system.customfieldtypes:userpickergroupsearcher"
QA_ISSUE_TYPES = ["Sub-task", "Bug Sub-Task"]


class Jira:
    def __init__(self, site, email, token):
        self.base = "https://" + site.replace("https://", "").rstrip("/")
        raw = (email + ":" + token).encode()
        self.auth = "Basic " + base64.b64encode(raw).decode()

    def call(self, method, path, body=None, params=None):
        url = self.base + path
        if params:
            url += "?" + urllib.parse.urlencode(params, doseq=True)
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", self.auth)
        req.add_header("Accept", "application/json")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                text = resp.read().decode()
                return json.loads(text) if text else None
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:500]
            raise SystemExit(f"Jira {method} {path} failed with {e.code}: {detail}")

    def paged(self, path, params=None, key="values"):
        params = dict(params or {})
        start, out = 0, []
        while True:
            params["startAt"] = start
            page = self.call("GET", path, params=params)
            items = page.get(key, [])
            out.extend(items)
            if page.get("isLast", True) or not items:
                return out
            start += len(items)


def load_env(path):
    env = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("JIRA_EMAIL", "JIRA_API_TOKEN"):
        if not env.get(k):
            raise SystemExit(f"{k} is missing in the env file")
    return env


class Report:
    def __init__(self):
        self.rows = []  # (area, state, text)

    def ok(self, area, text):
        self.rows.append((area, "OK", text))

    def fix(self, area, text):
        self.rows.append((area, "FIX", text))

    def manual(self, area, text):
        self.rows.append((area, "MANUAL", text))

    def info(self, area, text):
        self.rows.append((area, "INFO", text))

    def done(self, area, text):
        self.rows.append((area, "DONE", text))

    def print(self, title):
        print(f"# {title}\n")
        print("| Area | State | Detail |\n|---|---|---|")
        for a, s, t in self.rows:
            print(f"| {a} | {s} | {t.replace('|', '/')} |")
        counts = {}
        for _, s, _ in self.rows:
            counts[s] = counts.get(s, 0) + 1
        print("\nTotals: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))


def run(mode, cfg, env, allow_shared):
    apply = mode == "apply"
    j = Jira(cfg["site"], env["JIRA_EMAIL"], env["JIRA_API_TOKEN"])
    r = Report()
    key = cfg["project_key"]

    # 1. Project
    project = j.call("GET", f"/rest/api/3/project/{key}")
    pid = project["id"]
    if project.get("style") != "classic":
        r.manual("Project", f"{key} is team-managed. Stop: a Jira admin has to recreate it as company-managed.")
        r.print(f"Jira {mode}: {key}")
        return 2
    r.ok("Project", f"{key} is company-managed")

    # 2. Issue types
    all_types = j.call("GET", "/rest/api/3/issuetype")
    site_types = [t for t in all_types if "scope" not in t]  # skip team-managed types
    by_name = {}
    for t in site_types:
        by_name.setdefault(t["name"].lower(), t)
    std_ids = {}
    for name, level, desc in STANDARD_TYPES:
        t = by_name.get(name.lower())
        if t and t.get("hierarchyLevel") == level:
            std_ids[name] = t["id"]
            r.ok("Issue types", f"{name} exists on the site (level {level})")
        elif t:
            r.manual("Issue types", f"{name} exists at level {t.get('hierarchyLevel')}, the standard needs {level}. A Jira admin decides how to fix it.")
        elif apply:
            created = j.call("POST", "/rest/api/3/issuetype",
                             {"name": name, "description": desc or "", "hierarchyLevel": level})
            std_ids[name] = created["id"]
            r.done("Issue types", f"Created {name} (level {level})")
        else:
            r.fix("Issue types", f"Create {name} at level {level}")

    # 3. Issue type scheme of the project
    mapping = j.call("GET", "/rest/api/3/issuetypescheme/project", params={"projectId": pid})
    scheme = mapping["values"][0]["issueTypeScheme"]
    scheme_types = [m["issueTypeId"] for m in j.paged(
        "/rest/api/3/issuetypescheme/mapping", {"issueTypeSchemeId": scheme["id"]})]
    missing = [n for n, i in std_ids.items() if i not in scheme_types]
    missing += [n for n, _, _ in STANDARD_TYPES if n not in std_ids]  # still to be created
    id_to_name = {t["id"]: t["name"] for t in all_types}
    extras = [id_to_name.get(i, i) for i in scheme_types if i not in std_ids.values()]

    if scheme.get("isDefault"):
        if not missing and not extras:
            r.ok("Type scheme", "Project uses the default scheme, and it matches the standard")
        else:
            in_use = []
            for i in scheme_types:
                if i in std_ids.values():
                    continue
                cnt = j.call("POST", "/rest/api/3/search/approximate-count",
                             {"jql": f'project = {key} AND issuetype = {i}'})
                if cnt.get("count", 0) > 0:
                    in_use.append(i)
            keep_names = [id_to_name.get(i, i) for i in in_use]
            text = (f"Project uses the shared default scheme. Create scheme '{key}: Snotor issue types' "
                    f"with the standard types" + (f" plus types already used by issues: {', '.join(keep_names)}" if keep_names else "")
                    + ", assigned to the project. The default scheme is never edited.")
            if apply and len(std_ids) == len(STANDARD_TYPES):
                new = j.call("POST", "/rest/api/3/issuetypescheme", {
                    "name": f"{key}: Snotor issue types",
                    "description": "Snotor Jira standard",
                    "issueTypeIds": list(std_ids.values()) + in_use,
                    "defaultIssueTypeId": std_ids["Feature"],
                })
                j.call("PUT", "/rest/api/3/issuetypescheme/project",
                       {"issueTypeSchemeId": new["issueTypeSchemeId"], "projectId": pid})
                r.done("Type scheme", text.replace("Create", "Created"))
            else:
                r.fix("Type scheme", text)
    else:
        users = j.call("GET", "/rest/api/3/issuetypescheme",
                       params={"id": scheme["id"], "expand": "projects"})
        projects = users["values"][0].get("projects", {}).get("values", []) if users.get("values") else []
        shared = [p["key"] for p in projects if p.get("key") != key]
        if missing:
            text = f"Add {', '.join(missing)} to scheme '{scheme['name']}'"
            if shared and not allow_shared:
                r.manual("Type scheme", text + f". The scheme is shared with {', '.join(shared)}: rerun with --allow-shared after the PM agrees.")
            elif apply and all(n in std_ids for n in missing):
                j.call("PUT", f"/rest/api/3/issuetypescheme/{scheme['id']}/issuetype",
                       {"issueTypeIds": [std_ids[n] for n in missing]})
                r.done("Type scheme", text.replace("Add", "Added"))
            else:
                r.fix("Type scheme", text)
        else:
            r.ok("Type scheme", f"'{scheme['name']}' has every standard type")
    if extras:
        r.info("Type scheme", f"Types outside the standard, left as they are: {', '.join(extras)}")

    # 4. QA Assignee field, context and screens
    fields = j.call("GET", "/rest/api/3/field")
    qa = next((f for f in fields if f.get("name") == QA_FIELD_NAME and f.get("custom")), None)
    if qa and qa.get("schema", {}).get("custom") != QA_FIELD_TYPE:
        r.manual("QA Assignee", f"A field named {QA_FIELD_NAME} exists but is not a single user picker ({qa['schema'].get('custom')}). A Jira admin decides.")
        qa = None
    elif qa:
        r.ok("QA Assignee", f"Field exists on the site ({qa['id']}), reused")
    elif apply:
        qa = j.call("POST", "/rest/api/3/field", {
            "name": QA_FIELD_NAME, "description": "The QA person who tests this ticket. Filled by hand.",
            "type": QA_FIELD_TYPE, "searcherKey": QA_FIELD_SEARCHER})
        r.done("QA Assignee", f"Created the field ({qa['id']})")
    else:
        r.fix("QA Assignee", "Create the single user picker field QA Assignee")

    qa_type_ids = [std_ids[n] for n in QA_ISSUE_TYPES if n in std_ids]
    if qa:
        fid = qa["id"]
        pm = j.paged(f"/rest/api/3/field/{fid}/context/projectmapping", {"projectId": pid})
        contexts = j.paged(f"/rest/api/3/field/{fid}/context")
        ctx_id = next((m["contextId"] for m in pm if m.get("projectId") == pid), None)
        if ctx_id:
            tm = j.paged(f"/rest/api/3/field/{fid}/context/issuetypemapping", {"contextId": ctx_id})
            any_type = any(m.get("isAnyIssueType") for m in tm)
            have = {m["issueTypeId"] for m in tm if not m.get("isAnyIssueType")}
            if any_type or set(qa_type_ids) <= have:
                r.ok("QA Assignee", "Project context covers Sub-task and Bug Sub-Task")
                broader = "all issue types" if any_type else ", ".join(
                    sorted(id_to_name.get(i, i) for i in have if i not in qa_type_ids))
                if broader:
                    r.info("QA Assignee", f"The field is also available on {broader}. Allowed, it is simply left empty there.")
            else:
                miss = [n for n in QA_ISSUE_TYPES if std_ids.get(n) not in have]
                r.manual("QA Assignee", f"Project context does not cover {', '.join(miss)}. Add them in the field's contexts (check first that the context is used only by this project).")
        else:
            text = f"Create a context '{key} QA Assignee' for project {key}, issue types Sub-task and Bug Sub-Task"
            if apply and len(qa_type_ids) == len(QA_ISSUE_TYPES):
                j.call("POST", f"/rest/api/3/field/{fid}/context", {
                    "name": f"{key} QA Assignee", "projectIds": [pid], "issueTypeIds": qa_type_ids})
                r.done("QA Assignee", text.replace("Create", "Created"))
            else:
                r.fix("QA Assignee", text)
        if any(c.get("isGlobalContext") for c in contexts):
            r.info("QA Assignee", "The field also has a global context. The project context above takes precedence in this project.")

        # Screens used by the QA issue types
        itss = j.call("GET", "/rest/api/3/issuetypescreenscheme/project", params={"projectId": pid})
        itss_id = itss["values"][0]["issueTypeScreenScheme"]["id"]
        maps = j.paged("/rest/api/3/issuetypescreenscheme/mapping", {"issueTypeScreenSchemeId": itss_id})
        default_ss = next((m["screenSchemeId"] for m in maps if m["issueTypeId"] == "default"), None)
        ss_ids = set()
        for tid in qa_type_ids:
            ss_ids.add(next((m["screenSchemeId"] for m in maps if m["issueTypeId"] == tid), default_ss))
        ss_ids.discard(None)
        screen_ids = set()
        if ss_ids:
            for ss in j.paged("/rest/api/3/screenscheme", {"id": sorted(ss_ids)}):
                screen_ids.update(str(v) for v in ss.get("screens", {}).values())
        for sid in sorted(screen_ids):
            tabs = j.call("GET", f"/rest/api/3/screens/{sid}/tabs")
            on_screen = False
            for tab in tabs:
                tf = j.call("GET", f"/rest/api/3/screens/{sid}/tabs/{tab['id']}/fields")
                if any(f["id"] == fid for f in tf):
                    on_screen = True
                    break
            if on_screen:
                r.ok("QA Assignee", f"On screen {sid}")
            elif apply and tabs:
                j.call("POST", f"/rest/api/3/screens/{sid}/tabs/{tabs[0]['id']}/fields", {"fieldId": fid})
                r.done("QA Assignee", f"Added to screen {sid}")
            else:
                r.fix("QA Assignee", f"Add to screen {sid}")

    # 5. Flagged field and Blocks link type
    if any(f.get("name") == "Flagged" for f in fields):
        r.ok("Flagged", "Flagged field exists")
    else:
        r.manual("Flagged", "No Flagged field. It comes with Jira Software; ask the site admin.")
    links = j.call("GET", "/rest/api/3/issueLinkType").get("issueLinkTypes", [])
    if any(l["name"] == "Blocks" and l["inward"] == "is blocked by" for l in links):
        r.ok("Links", "Blocks / is blocked by exists")
    else:
        r.manual("Links", "Link type Blocks (blocks / is blocked by) is missing. Add it in Jira settings, Issue linking.")

    # 6. Statuses per issue type (workflow itself is fixed in the browser)
    per_type = j.call("GET", f"/rest/api/3/project/{key}/statuses")
    status_sets = {}
    for entry in per_type:
        status_sets.setdefault(frozenset(s["name"] for s in entry.get("statuses", [])), []).append(entry["name"])
    if len(status_sets) > 1:
        groups = "; ".join(", ".join(sorted(v)) for v in status_sets.values())
        r.manual("Workflow", f"Issue types use {len(status_sets)} different workflows ({groups}). The standard is one workflow for all types (browser step).")
    for entry in per_type:
        if entry["name"] not in [n for n, _, _ in STANDARD_TYPES]:
            continue
        have = [s["name"] for s in entry.get("statuses", [])]
        miss = [s for s in STANDARD_STATUSES if s not in have]
        extra = [s for s in have if s not in STANDARD_STATUSES]
        if miss:
            r.manual("Workflow", f"{entry['name']}: missing statuses {', '.join(miss)} (browser step)")
        else:
            r.ok("Workflow", f"{entry['name']}: every standard status present")
        if extra:
            mapped = [f"{s} -> {STATUS_ALIASES[s]}" for s in extra if s in STATUS_ALIASES]
            other = [s for s in extra if s not in STATUS_ALIASES]
            if mapped:
                r.manual("Workflow", f"{entry['name']}: rename by mapping {', '.join(mapped)} (browser step)")
            if other:
                r.info("Workflow", f"{entry['name']}: statuses outside the standard, ask the PM before mapping: {', '.join(other)}")

    # 7. Boards (filters and boards; columns and quick filters are browser steps)
    boards = j.paged("/rest/agile/1.0/board", {"projectKeyOrId": key})
    board_names = {b["name"] for b in boards}
    for b in cfg.get("boards", []):
        if b["name"] in board_names:
            r.ok("Boards", f"Board '{b['name']}' exists (check columns and quick filters in the browser)")
            continue
        text = f"Create filter and {b.get('type', 'kanban')} board '{b['name']}': {b['jql']}"
        if apply:
            flt = j.call("POST", "/rest/api/3/filter", {
                "name": b["name"], "jql": b["jql"],
                "sharePermissions": [{"type": "project", "project": {"id": pid}}]})
            j.call("POST", "/rest/agile/1.0/board", {
                "name": b["name"], "type": b.get("type", "kanban"), "filterId": int(flt["id"]),
                "location": {"type": "project", "projectKeyOrId": key}})
            r.done("Boards", text.replace("Create", "Created"))
        else:
            r.fix("Boards", text)

    r.manual("Browser", "Workflow transitions, board columns, quick filters, Slack and Markdown for Jira: see chrome-steps.md")
    r.print(f"Jira {mode}: {key}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["audit", "plan", "apply"])
    ap.add_argument("--config", required=True)
    ap.add_argument("--env", required=True)
    ap.add_argument("--allow-shared", action="store_true",
                    help="allow adding issue types to a scheme other projects use")
    a = ap.parse_args()
    with open(a.config, encoding="utf-8") as f:
        cfg = json.load(f)
    sys.exit(run(a.mode, cfg, load_env(a.env), a.allow_shared))


if __name__ == "__main__":
    main()
