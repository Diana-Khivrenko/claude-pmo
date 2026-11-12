---
name: qa-summary
argument-hint: <project or repository> <GitLab, GitHub or Bitbucket, if known>
description: "Set up the QA summary from CI: when a pull request or merge request merges, a CI job posts its description as a comment on the Jira ticket named in the branch or title, through a Jira automation webhook, with no Jira account or API token stored in CI. Covers the Jira flow, the webhook secret, the script, the CI job for GitLab, GitHub or Bitbucket, and the end-to-end check. Use when someone asks to connect a repository to Jira, to post merge or pull request summaries to tickets, to notify QA from the repo, or to set up the QA summary on a new project."
---

# QA summary from CI

When a merge lands, QA should not have to open the merge request to learn what changed and what to test. A CI job sends the merge request's description to a Jira automation webhook, and Jira adds it as one comment on the ticket named in the branch or the title. No Jira account or API token lives in CI, only the webhook's URL and secret.

```
merge → CI job finds the merged request and its ticket key → webhook → Jira flow adds the comment, unless that link is already there
```

## Before you start

1. **The project profile** (pmo-setup skill): the Jira site and project key, the code host and the repositories, the team Slack channel.
2. **Ask the person, in one round**, unless the profile already says:
   - Which repositories, and which code host (GitLab, GitHub, Bitbucket).
   - The target branch (usually `main`, or the default branch).
   - A flow for this project only, or one global flow for the whole site. **Propose the project flow**: it needs only project admin rights and cannot comment on other projects' tickets.
   - Who can add CI secrets in those repositories, and who reviews a change to the pipeline file.

**When anything is missing**, ask in the chat. Never guess a repository, a branch or a stage name.

Tell the person once, in plain words, what this adds: every merge posts one comment on its ticket, and the team's Slack channel shows comments (jira-setup standard, Slack notifications). That is intended, QA needs it, but it is one more message per merge.

## Secrets: the rules

The webhook URL and secret let anyone who has them add comments to every ticket the flow can reach.

- Never ask for them in the chat, never print them, never write them into a file, a commit, a ticket or a page.
- The person copies them from Jira straight into the code host's secret variables.
- If one leaks, Regenerate in the Incoming webhook step, and update the CI variable right after: the old secret stops working at once.

## 1. The Jira flow

Done in the person's Chrome (Claude in Chrome), by a project admin for a project flow or a Jira admin for a global one. Say what you are about to change, wait for a yes, take a screenshot after each step.

1. Project settings, Automation (or Settings, System, Global automation for a global flow). Create flow.
2. Trigger: **Incoming webhook**, set to take the work items from the request (the step then reads "Gather work items from request").
3. Condition **Compare two values** (the smart values condition):
   - First value: `{{issue.comments.body.join(" ")}}`
   - Condition: does not contain
   - Second value: `{{webhookData.mergeRequestUrl}}`

   This stops a re-run of the CI job from posting the same summary twice.
4. Action **Add comment to work item**, comment `{{webhookData.comment}}`.
5. Name it **QA summary from CI**, owner the PM of the project, turn it on.

Jira creates the webhook URL and the secret only once the flow is saved. They are in the side panel of the Incoming webhook step. Ask the person to open that panel and copy them into the CI variables themselves (step 3).

### Test the flow before touching CI

Give the person this command for their own terminal, with a real test ticket the person picks:

```bash
curl -X POST "$JIRA_AUTOMATION_URL" \
  -H "Content-Type: application/json" \
  -H "X-Automation-Webhook-Token: $JIRA_AUTOMATION_TOKEN" \
  -d '{"issues":["PROJ-123"],"mergeRequestUrl":"https://example.com/pr/1","comment":"Webhook test"}'
```

The comment appears within seconds. If not, the flow's Audit log says which step stopped and why. Delete the test comment afterwards only if the person asks.

## 2. The repository change

1. Add `scripts/post-qa-summary-to-jira.mjs` from this skill, unchanged.
2. Add the CI job for the platform from `references/ci-platforms.md`, merged into the existing pipeline file, never replacing it. Use a stage the pipeline already has.
3. Make the change on its own branch named with a ticket key, and open a merge request for the developers to review. Never push to the target branch. If no connector can write to the repository, give the person the two files ready to hand to a developer.

The script posts the description as it is, so the description is what QA reads. Offer, without insisting, a merge request template with a short QA section (what changed, how to test, what to watch), so descriptions are written for QA.

## 3. The secrets in CI

Give the person the steps for their platform from `references/ci-platforms.md`: `JIRA_AUTOMATION_URL`, `JIRA_AUTOMATION_TOKEN`, and on GitLab and Bitbucket an `SCM_TOKEN` that can only read merge requests. They add them themselves, masked and protected.

## 4. Check end to end

1. A branch named with a real ticket key, a merge request with a description, merged into the target branch.
2. The CI log ends with `Sent the QA summary for … to <KEY>`.
3. The ticket has one new comment starting "QA summary for", linking the merge request.
4. Re-run the job: the flow's Audit log shows a run stopped at the condition, and no second comment appears.

When something fails, use the table in `references/ci-platforms.md`. Report in the chat what was set up, in which repositories, and what is left for whom.

## Never

- Store or show the webhook URL, the secret or a source-control token anywhere but the code host's secret variables.
- Make the pipeline fail because the summary could not be posted.
- Create test tickets: test on a ticket the person picks.
- Change other automation rules on the way. They belong to the jira-setup skill.
