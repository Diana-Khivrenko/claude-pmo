# Browser steps

What the Jira REST API cannot do well, done in the person's Chrome with Claude in Chrome, on the account of a Jira admin. Before each step: say what you are about to change, wait for a yes, then do it. After each step: take a screenshot and compare it with the standard.

Jira's admin screens change from time to time. If a page does not look like the step describes, stop, describe what you see, and ask. Do not click around looking for it.

## 1. Workflow

The project ends up with one workflow for every issue type (section 5 of `standard.md`).

1. Project settings, Workflows. If the issue types use more than one workflow, take the one Sub-task uses as the base. If it is shared with other projects, make a copy for this project instead of editing it.
2. Add every missing status from section 5 of `standard.md`, with the category given there. Reuse an existing status of the same name, never create a second "To Do".
3. Make every status reachable from any status: on each status, tick "Allow all statuses to transition to this one" (the wording in the new editor). The result is global transitions only.
4. Do not add conditions or validators. "Only developers move to Ready for QA" is a team rule, not a workflow condition.
5. In the project's workflow scheme, assign this workflow to all issue types.
6. Publish. Jira asks how to map statuses of existing issues: use the mapping table in section 5 of `standard.md` (Review to Code review, Testing to Testing (QA)). Show the full mapping to the person and wait for a yes before confirming.

If the workflow is shared with other projects (the editor says so), stop and ask. Changing it changes them too.

## 2. Board columns

For each board the script created or found: Board, Board settings, Columns.

1. One column per status, in the order of section 5. On Kanban, Backlog stays in the Kanban backlog, not a column.
2. Each status in its own column. Nothing left in "Unmapped statuses" except Backlog, and Blocked (Comment required) if the PM chose not to have a column for it (it is optional).

## 3. Quick filters

Development board, Board settings, Quick filters. Add from the project profile:

- one per platform tag, named after the tag (`Web`), query `summary ~ "\\[Web\\]"`,
- one per QA person, named after the person, query `"QA Assignee" = <accountId>`, with the account id looked up with the Jira connector, never guess it,
- "Flagged", query `Flagged is not EMPTY`.

## 4. Slack

Done by a person in Slack, because the Jira Cloud app is configured inside Slack and Claude does not post or configure apps there.

Give the person these steps:

1. In the team channel from the profile, add the Jira Cloud app if it is not there yet.
2. Open the app's notification setup for the channel (in recent versions, `/jira notify`, or, if the command differs, use the app's channel settings).
3. Pick the project. Turn on exactly two triggers:
   - Comment added (all issue types),
   - Issue created, with the filter issue type = Bug Sub-Task.
4. Turn everything else off: transitions, assignments, edits.

Then ask the person to post a test comment on any ticket and confirm it reached the channel.

## 5. Markdown for Jira

Jira settings, Apps, Explore more apps, search "Markdown for Jira", install. Needs a site admin. If the person is not one, say who has to do it and move on.

## 6. Design project (only when the profile has one)

In the design project's workflow, check that new issues land in the status the profile names for new design tickets. Report differences, do not rebuild the design workflow without asking.

## 7. Automation

Space settings, Automation, for the two project rules. Jira settings, System, Global automation, for the global one. Build each rule exactly as in section 11 of `standard.md`. The names matter, because the audit finds the rules by name.

1. List the existing rules in both places. A rule with the standard name but a different trigger, condition or action is shown to the person with the difference, and fixed only after a yes.
2. For each missing project rule: Create flow, the trigger "Work item transitioned" with the To status, a branch "For: Parent", inside it the JQL condition (and for the second rule the "If sub-tasks match" condition), then "Transition the work item to". Owner: the PM. Turn it on.
3. "Move to in progress": only if the site has no rule with that name. Check first in Development tools that the code host is connected.
4. Test each project rule once on a real Feature the person picks: move one sub-task and check the Feature in the rule's Audit log. Never create test tickets for this.
