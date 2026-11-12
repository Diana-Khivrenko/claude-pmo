---
name: bug-cause
argument-hint: <bug ticket key, or the bug report text>
description: "Find where in the code a reported bug happens and why, and write it as the Cause section of the bug ticket: two or three sentences with the file linked, never the fix. Reads the ticket, the specs and the code, checks recent changes that may have introduced it, and says how sure it is. Read-only until the person says yes. Anyone on the project can run it. Use when someone asks why a bug happens, what causes it, where it comes from, which change broke it, or asks to fill in the Cause of a bug ticket."
---

# Bug cause

A bug with its cause found is fixed in an hour, one without it can take a day of searching. This skill reads the code the way a developer would to find where and why the defect happens, so the ticket points straight at it. The solution stays with the developer: the skill never proposes the fix, because the person who owns the code knows its constraints better.

Anyone on the project can run it: QA while filing, the manager while triaging, a developer picking the ticket up.

## 1. Gather

1. **The project profile** (pmo-setup skill): the code host, the repositories per platform, where UI strings live, the code host URL pattern for linking files.
2. **The bug**: the ticket or the report, its steps, actual and expected result, platform, environment and build.
3. **The specs**: the use case sentence or Reference string the expected result rests on. If there is none, say so first (step 4 below), because then it may not be a bug at all.
4. **The code**: the repository of the platform the tag names ([BE], [Web], [App]), read through the code host connector or a local clone the person has.

**When anything is missing**, which repository, which platform, steps that cannot be followed, ask in the chat.

## 2. Find it

Work from the symptom to the line, and keep the trail so it can be shown:

1. **Where the screen lives.** Find the screen, component or endpoint from the strings on it (search the Reference key or the visible text in the translation files and the code), the route, or the API call it makes.
2. **Follow the steps through the code.** For each step of the report, find what runs: the handler, the state change, the request, the server logic, the query. Stop where the code does something different from the expected result.
3. **Check both sides.** A wrong screen can come from the client or from the data the server sends. Look at the response the client relies on before blaming either side, and say which side it is.
4. **When it started.** Look at the history of the lines involved: the recent merge requests and commits that touched them, and the ticket keys in their titles. A bug that appeared after a change is usually caused by it, and that ticket is the natural parent of the bug (jira-ticket skill).
5. **Reproduce, when it helps.** On staging in Chrome, with the account the person is signed in with, never typing a password, and doing nothing that reaches other people without asking. Confirm the steps produce the actual result, and note the build.

## 3. Say how sure you are

Every cause carries one of three labels, said plainly:

- **Confirmed**: traced in the code and reproduced, or traced to a line whose effect is certain.
- **Likely**: traced to a place in the code that explains the symptom, not reproduced.
- **Not found**: what was checked and ruled out, and where to look next.

Only a confirmed or likely cause goes into a ticket, and a likely one says "likely" in its first sentence. A guess never does.

## 4. When it is not a bug

Sometimes the code does exactly what the use case says, or the use case is silent on the case. Then the defect is in the spec or the request, not in the code. Say so with the sentence quoted, and point to the right path: a gap or a new requirement goes through the new-requirement skill, an outdated spec to the manager for spec-sync. Do not write a Cause for it.

## 5. Write the Cause

The Cause section of the bug template (jira-ticket skill): where the defect happens and why, in two or three plain sentences a QA person can follow, with the file linked on the code host (plain path as the link text, no backticks inside the link) and the line or function named. When a change introduced it, name that merge request or ticket, linked.

Never in the Cause: the fix, code snippets, a long technical write-up, a refactoring suggestion, blame on a person.

Example: the Cause of the Bug in `jira-ticket/references/examples.md`. It names the mechanism (virtualized history, the placeholder height, the anchoring to the end), the code that does it, and the platform that is not affected, in three sentences, with no fix.

## 6. Report, and write only on a yes

In the chat, in the language the person wrote in: the cause with its label, the trail (the steps mapped to the files that run them, linked), the change that introduced it if found, and the Cause text ready to paste.

Write it into the ticket only when the person says so, and by the status rules of the jira-ticket skill: in To Do, add the Cause to the description with no comment. In any later status, do not edit the description, offer one comment to the developer instead, kind and neutral, carrying the cause. A new bug being filed gets the Cause as part of its description (jira-ticket skill).

Nothing else is ever written: no comment in GitLab or GitHub, no branch, no change to the code.
