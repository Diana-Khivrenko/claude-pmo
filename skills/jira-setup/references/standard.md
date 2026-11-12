# The Snotor Jira standard

This is the target every project is set up to and audited against. It was taken from the first project run end to end with this workflow, and generalised. Values that differ per project are marked **(profile)** and come from the project profile, never from this file.

Why it is strict: Claude reads Jira through the API and follows these rules literally on every ticket. A setting that is "almost the same" in one project makes every skill behave differently there.

## 1. Project

- **Company-managed** (classic) software project. Team-managed projects hide part of their statuses and fields from the API, so Claude cannot read or audit them reliably. If the project is team-managed, stop and say so: it has to be recreated or migrated by a Jira admin, the skill does not convert it.
- Project key **(profile)**, for example `ABC`.
- One Jira site per organisation **(profile)**, for example `snotor.atlassian.net`.

## 2. Issue types and hierarchy

Three levels, never deeper: Epic, then a standard-level type, then a sub-task type.

| Issue type | Level | Used for |
|---|---|---|
| Epic | 1 | One module of the product (Chat, Posts, Payments). Plus one standing epic, "Other development tasks", for work that belongs to no module. |
| Feature | 0 | One use case. A short noun title ("Attachments gallery"). The parent of the platform sub-tasks. |
| Task | 0 | Product work that is not a use case. |
| Technical task | 0 | Infrastructure, security, CI, tech debt. |
| Sub-task | -1 | One per platform under a Feature, title starts with the platform tag. What a developer picks up and QA tests. |
| Technical Sub-task | -1 | Technical work under a Technical task. Needs no QA. |
| Bug Sub-Task | -1 | A defect found in testing, under the Feature whose behaviour it breaks, linked "relates to" the platform sub-task it breaks. The first choice for a bug, a standalone Bug only when no Feature fits. |

- Feature is a **custom** issue type at level 0 (the same level as Task). Description to set on it: "One use case of the product. The parent of one sub-task per platform."
- Other types a project already has (Story, Bug, and so on) are reported in the audit as "not in the standard", never deleted. Removing a type can break existing issues.
- Rules about how tickets are split (one sub-task per platform, no parent with a single child, a bug goes under the Feature it breaks) live in the jira-ticket skill, not in Jira configuration.

## 3. Fields

| Field | Type | On which issue types | Notes |
|---|---|---|---|
| QA Assignee | Custom, user picker (single user) | Sub-task, Bug Sub-Task | Must be available on these two. It may also exist on other types, it is simply left empty there: Technical Sub-tasks need no QA. Filled by hand at any status, one QA person per module **(profile)**. A site has one QA Assignee field, and every project reuses it through its own field context. |
| Flagged | Jira Software system field | All | Used to mark a dev ticket that waits for its design ticket. |
| Assignee | System | All | Every new dev ticket gets one: the developer who built that module **(profile)**. |

## 4. Link types

- **Blocks** (`blocks` / `is blocked by`) must exist.

**The blocking rule, for every project, no exceptions:** when a ticket cannot move until another ticket is done, link them right away. The blocked ticket "is blocked by" the ticket that blocks it (a design ticket, a backend sub-task, another team's ticket), and the blocked ticket gets the **flag**.

- The link says *what* it waits for, so anybody opening either ticket sees the dependency, and the blocker shows which tickets are waiting on it. A flag without a link only says "something is wrong" and sends people asking.
- The flag makes the wait visible on the board without moving the ticket out of its column.
- When the blocker is done, the flag comes off. The link stays, as the history of why the ticket waited.
- A blocked ticket normally stays in its status (usually To Do) with the flag and the link. The Blocked (Comment required) status is rarely used, see section 5.

## 5. Workflow and statuses

**One workflow, shared by every issue type** of the development project, Epic included. One set of status names means the skills, the boards and the people never have to remember which type moves through which statuses. Every transition is **global** (any status can move to any status), so nobody is stuck waiting for a transition to be added.

| Order | Status | Category | Rule that goes with it |
|---|---|---|---|
| 1 | Backlog | To Do | Exists, but nothing is created here. Nobody reads the backlog. |
| 2 | To Do | To Do | Every new ticket starts here, with an assignee. A ticket in Code review whose requirements change comes back here (in In Progress it stays where it is, with one comment). A ticket in Ready for deploy, Ready for QA or Testing (QA) is never edited: the change becomes a new linked ticket. A blocked ticket usually stays here, flagged and linked (section 4). |
| 3 | Blocked (Comment required) | To Do | Rarely used: the flag and the "is blocked by" link are the normal way. Whoever does move a ticket here writes a comment saying what blocks it. A board column for it is optional. |
| 4 | Failed QA | To Do | Testing found a defect. Each defect gets its own Bug Sub-Task under the Feature. Goes back to the developer. |
| 5 | In Progress | In Progress | A developer is working on it. |
| 6 | Code review | In Progress | Merge request open. |
| 7 | Ready for deploy | In Progress | Code review passed, waiting for the deploy to the environment QA tests on. |
| 8 | Ready for QA | In Progress | Deployed for testing. **Only developers** move tickets here. A convention, not a workflow condition. |
| 9 | Testing (QA) | In Progress | QA tests the Basic Path and every Alternative Path of the use case. |
| 10 | Done | Done | |

Status names are matched exactly, including the brackets in "Testing (QA)" and "Blocked (Comment required)", because skills move tickets by name.

Aligning an existing project: a project that runs several workflows is moved to this one through its workflow scheme. Statuses that are the same step under another name are mapped, never kept side by side:

| Existing status | Maps to |
|---|---|
| Review | Code review |
| Testing | Testing (QA) |

Any other status outside the standard is shown to the PM before mapping, never mapped by guess.

## 6. Boards

One audience per board, so nobody scrolls past tickets that are not for them.

| Board | Audience | Filter (default, confirm with the PM) |
|---|---|---|
| `<KEY> Development` | Developers, QA, the client | `project = <KEY> AND issuetype not in (Epic, "Technical task", "Technical Sub-task") ORDER BY Rank ASC` |
| `<KEY> Infrastructure` | DevOps, architect | `project = <KEY> AND issuetype in ("Technical task", "Technical Sub-task") ORDER BY Rank ASC` |
| Design board | Designers, PO | Only when the project has a separate design project **(profile)**. See section 8. |

- Columns: one per status in the order of section 5. Backlog is not a column on a Kanban board. A column for Blocked (Comment required) is optional, many teams leave it out because blocked tickets stay in To Do with the flag.
- Quick filters on the Development board:
  - one per platform tag **(profile)**: `summary ~ "\\[Web\\]"` and so on,
  - one per QA person **(profile)**: `"QA Assignee" = <accountId>`,
  - "Flagged": `Flagged is not EMPTY`.
- Board type, Kanban or Scrum **(profile)**. Ask, do not assume.

## 7. Slack notifications

Exactly two, into the team channel **(profile)**, through the Jira Cloud app for Slack:

1. **Comment added**: every comment means a person needs an answer.
2. **Issue created, type Bug Sub-Task**: QA found something.

Nothing else (no status changes, edits or assignments), or the channel is noise within a day. This is also why the skills never comment on a ticket in To Do or on a newly created ticket.

## 8. Design project (optional)

When the organisation keeps design tickets in a separate project **(profile)**:

- No epics. Design tickets have no parent.
- Titles start with `[Design]`. One ticket covers web and app.
- New design tickets go to the status the profile names **(profile)**, for example Selected for Development when the design workflow has no To Do.
- Some kinds of work get no design ticket at all **(profile)**, for example an internal admin panel.

## 9. Apps

- **Markdown for Jira** from the Atlassian Marketplace, so that what Claude writes renders correctly.

## 10. Content created once

- One epic per module **(profile)**, created from the module list.
- The standing epic "Other development tasks".

## 11. Automation

Three rules, plus one optional. They keep a Feature's status in step with its sub-tasks and move a ticket to In Progress when work on it starts, so nobody has to move parents by hand. Everything else stays manual on purpose: every automated move is a move nobody decided, and Slack shows comments from rules like any other.

| Rule | Where | Trigger | Condition | Action |
|---|---|---|---|---|
| Feature to In Progress when a sub-task starts | Project | Work item transitioned to **In Progress** | Branch "For: Parent": the parent matches `issuetype = Feature AND status = "To Do"` | Transition the parent to **In Progress** |
| Feature to Ready for QA when every sub-task is ready | Project | Work item transitioned to **Ready for QA** | Branch "For: Parent": the parent matches `issuetype = Feature AND status != "Ready for QA"`, and its sub-tasks match `status in ("Ready for QA", "Testing (QA)", "Done")` | Transition the parent to **Ready for QA** |
| Move to in progress | Global (once per Jira site) | Branch created | Status equals **To Do** | Transition the work item to **In Progress** |

- The second rule leaves **Ready for deploy** out of its sub-task condition on purpose. Ready for deploy comes before Ready for QA, so a sub-task there is not deployed for testing yet, and the Feature must not reach Ready for QA ahead of it.
- Bug Sub-Tasks count as sub-tasks in that condition: a Feature with an open bug does not move to Ready for QA.
- "Move to in progress" needs the code host (GitHub or GitLab) connected to Jira in Development tools, otherwise the Branch created trigger never fires. It is a global rule, so a site that already has it does not get a second copy.
- The rule owner gets the email when a rule fails, so the owner is the PM of the project for the project rules **(profile)** and a Jira admin for the global one.
- One optional fourth rule, per project: **QA summary from CI**, an Incoming webhook flow that adds the merged merge request's description as a comment on its ticket. It is set up with the qa-summary skill, together with the CI job that calls it.
- Other rules found on the site are reported in the audit as outside the standard and left alone.
