---
name: jira-setup
argument-hint: <setup or audit> <Jira project key or link>
description: "Set up a new Jira project to the Snotor standard, or audit an existing one against it: company-managed project, the Epic, Feature, sub-task hierarchy, the custom Feature issue type, the QA Assignee field on Sub-task and Bug Sub-Task, the workflow and statuses, the blocking rule, the Development and Infrastructure boards with their columns and quick filters, the three automation rules, the two Slack notifications, and the Markdown for Jira app. Use whenever someone asks to set up, configure, prepare or check Jira for a project, add the Feature type or QA Assignee, fix board columns, statuses or automation, compare a project with the standard, or asks why Claude's tickets look wrong in a project, even if they do not say 'setup'."
---

# Jira setup and audit

You configure a Jira project so that every other snotor-pmo skill (jira-ticket above all) works in it the same way it works everywhere else, or you check an existing project and report where it differs. The target is `references/standard.md` in this skill. Read it first, every time: it is the source of truth, and this file only says how to get a project there.

Two modes:

- **setup**: a new or nearly empty project. Interview, plan, apply, verify.
- **audit**: an existing project. Read only, report, offer fixes. Choose audit whenever the project already has tickets, even if the person said "set up".

## What you must never do

These changes hit a whole Jira site, often shared by other teams, and some cannot be undone.

- Never change anything before the person has seen the plan and said yes to it. A plan is a list of concrete changes, not "I'll configure Jira".
- Never delete an issue type, status, field, screen, scheme or board. Extras are reported as "outside the standard" and left alone.
- Never edit the site's default issue type scheme, a workflow, scheme or field context that other projects use, without naming those projects to the person and getting a yes for exactly that.
- Never ask for the API token in the chat, never print it, never write it into a file you create. The person puts it in the env file themselves.
- Never convert a team-managed project. Stop and say a Jira admin has to recreate it as company-managed.
- Never create tickets other than the epics from step 1, and only after a yes.
- Never comment on tickets during setup. Every comment reaches the team's Slack channel.

## Tools and who does what

The Jira connector (Atlassian Rovo) can read and write tickets but cannot change configuration. So the work is split three ways:

| Part | How | Why |
|---|---|---|
| Issue types, issue type scheme, QA Assignee field, its context and screens, board filters and boards | `scripts/jira_setup.py` against the Jira REST API, with a Jira admin's API token | The API does these reliably and the script is idempotent: running it twice changes nothing the second time. |
| Workflow transitions, board columns, quick filters, the three automation rules, the Markdown for Jira app | Claude in Chrome, the person's own browser, following `references/chrome-steps.md` | No usable public API, or the API is too fragile for this. |
| The two Slack notifications | The person, in Slack, with your step list | Claude does not configure apps or post in Slack. |
| Verification and audit of tickets-level facts | The Jira connector, read only | Quick, and needs no token. |

### Where the script runs

The script needs network access to the Jira site. Try in this order and say which one you use:

1. The person's computer through the device shell, if a folder is connected and the site is reachable from there. Copy the script and the config into that folder.
2. The person's own terminal: give them the exact command to run and ask them to paste the output back.

The cloud workspace usually cannot reach the company's Jira site, so do not count on it.

### The env file

Ask the person to create a file `jira.env` in a connected folder that is not a git repository, with two lines they type themselves:

```
JIRA_EMAIL=their.work@email
JIRA_API_TOKEN=token from id.atlassian.com, Security, API tokens
```

The account must be a Jira admin for setup. Audit works with any account that sees the project, though some checks (screens, schemes) then come back as errors: report them as "needs an admin to check", not as problems.

## Setup, step by step

### Step 1. Interview

Get these values. Take them from the project profile if one exists (see the pmo-setup skill), otherwise ask, a few at a time, in plain words. Never fill one in with a guess: an invented QA person or epic name ends up on every ticket. This holds through the whole setup: whenever a value is missing, ask the manager in the chat and carry on once they answer.

- Jira site and project key. Does the project exist yet? Company-managed?
- Platforms and their tags, for example `[BE]`, `[Web]`, `[App]`.
- Modules, one epic each. Plus the standing epic "Other development tasks".
- Who built or will build each module, per platform (becomes the default assignee rule in the profile).
- QA people and which modules each one owns.
- Kanban or Scrum.
- The team Slack channel.
- Is there a separate design project? Is there work that never gets a design ticket (an internal admin panel, for example)?
- Who owns the project's automation rules (usually the PM), and is the code host connected to Jira?

Write the answers down as the Jira part of the project profile and show it to the person before going further.

### Step 2. Plan

1. Fill `templates/jira-setup.example.json` with the site, key and board filters, save it as `jira-setup.json` next to the env file. Show the board JQL to the person, the defaults in the template split boards by issue type, which may not fit every project.
2. Run `python3 jira_setup.py plan --config jira-setup.json --env jira.env`. It only reads.
3. Show the table it prints. Explain every FIX row in one plain sentence, and every MANUAL row with who has to act. Add the browser steps and the Slack steps that apply.
4. Ask for a yes on the whole list, or on the parts the person picks.

### Step 3. Apply

1. Run the script with `apply`. Add `--allow-shared` only if the person agreed, in step 2, to change a scheme shared with the projects you named.
2. Do the browser steps from `references/chrome-steps.md`, one at a time, with a screenshot after each.
3. Give the person the Slack steps and wait for them to confirm the test comment arrived.
4. Offer the QA summary from CI (qa-summary skill), which posts each merged merge request's description on its ticket. It needs the code host, so it can also be done later.
5. Create the module epics and "Other development tasks" with the Jira connector, after showing the list. Epics are created in To Do, with no description beyond one line saying which module it is, and no comment.

### Step 4. Verify

1. Run the script with `audit`. Every row should now be OK, DONE or INFO. Anything else goes back to the person.
2. With the Jira connector, read the project's issue types and the fields of a Sub-task, a Bug Sub-Task and a Technical Sub-task. QA Assignee must be on the first two. On the third it may exist, and stays empty.
3. Look at each board in Chrome: columns in the standard order, quick filters present. Open the automation lists: the three standard rules are on, each with its owner.
4. Report in the chat: what was set up, what is still manual and who owns it. One short table, then two or three sentences.

## Audit, step by step

1. Read the project with the Jira connector: issue types, the fields of each sub-task type, the statuses (from the transitions of one open ticket), the link types.
2. If the person has an env file, run the script with `audit` for the parts the connector cannot see (schemes, screens, field contexts, boards).
3. Search the open Bug Sub-Tasks with no "relates to" link to a platform sub-task, and list them by key in the report. Never move or relink them in audit mode.
4. In Chrome, open the project's automation list and the global one, and compare the rules with section 11 of the standard. Look at the boards only if the person asks for a full audit.
5. Report in three groups, in this order:
   - **Breaks the skills**: missing Feature type, missing QA Assignee, missing Blocks link type, a missing status the skills move tickets to, team-managed project.
   - **Differs from the standard**: wrong columns, a missing quick filter, extra Slack triggers, a missing standard automation rule or one whose condition differs, Bug Sub-Tasks with no link to the sub-task they break.
   - **Outside the standard, left alone**: extra issue types or statuses.
6. Offer to fix the first two groups through setup steps 2 to 4. Change nothing in audit mode.

## Writing to the person

Plain, warm, short. Explain why a setting matters in one sentence ("every comment reaches the whole channel, so we keep notifications to two"), not how Jira works in general. Questions go in the chat, one decision at a time, never into Jira.
