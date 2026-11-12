---
name: build-check
argument-hint: <ticket key, or merge request link>
description: "Check what was built against what was asked: read the merge request for a Jira ticket, go through every acceptance criterion, check every UI string against the Reference page, try the scenarios on staging in Chrome, and point out what the merge request adds beyond the ticket. Read-only, the report stays in the chat. Anyone on the project can run it. Use when someone asks whether a ticket is done, to check or review a merge request or pull request against its ticket, before Code review or before testing, or asks what a build actually does."
---

# Build check

A merge request can pass code review and still not do what the ticket asked: a criterion forgotten, a string reworded, a state left out, or something extra nobody decided. This skill compares the build with the ticket and the specs behind it, so the gaps are found before QA spends a day on them.

**It is read-only, always.** It never comments in GitLab or GitHub, never changes a ticket, never creates a bug and never moves a status. The report stays in the chat, and the person who ran it decides what to do with it. Anyone on the project can run it: a developer before Code review, QA before testing, the manager at any time.

## 1. Gather

1. **The project profile** (pmo-setup skill): the code host and repositories, where UI strings live, the staging URL, the platforms, the product languages, spelling of in-product copy.
2. **The ticket**, in full: description, acceptance criteria, design links, parent Feature, linked tickets, and comments that changed the requirement.
3. **The specs behind it**: the use case it links to, and the Reference entries for every string the screen shows. When the ticket and the use case disagree, note it in the report.
4. **The merge request**: from the ticket's development links, or by searching the code host for the ticket key in merge request titles and branch names. Read the description, the full diff and the pipeline status. When several merge requests carry the key (one per platform, or a fix-up), read them all and say which is which.

**When anything is missing**, no merge request found, two that both look current, no staging URL, no use case link, ask in the chat before checking what you can and calling it complete.

## 2. Check

### Acceptance criteria against the code

Go through the criteria one by one, and for each give a verdict with the evidence:

- **Done**: where in the diff it happens (file and line, linked on the code host).
- **Partly**: what is there and what is missing.
- **Not found**: nothing in the diff does it. Not found in the diff is not proof it is missing, it may already exist in the code, so search the repository before saying so, and say where you looked.
- **Cannot tell from code**: behaviour only visible at runtime (an animation, focus order, a push arriving). Check it on staging.

Read the use case's alternative paths too: errors, empty states, limits, roles. A criterion list rarely names all of them, and they are where builds most often fall short.

### Strings against the Reference

Find every UI string the merge request adds or changes, in the code and in the translation files, and compare with the Reference:

- the English text, word for word: capitals, final full stop, placeholders, the in-product spelling the profile names,
- the key exists in every product language file the profile names, and no language file carries an English placeholder or an empty value,
- no button carries a person's, team's or group's name,
- strings the Reference does not have.

### The build on staging

Open staging in Chrome and walk the use case scenarios for this ticket: the basic path, then each alternative path the screen can reach. Use the account the person is already signed in with, or ask them to sign in. Never type a password. Check the states the code cannot show: what is announced, where focus goes, how it looks at enlarged text and in both themes when the ticket asks for it.

Do nothing on staging that reaches other people (sending a request, a message, an invite to a real address) without asking first. Say which build you checked (the version or commit staging shows, when it shows one), because staging may not carry the merge request yet.

### What the merge request adds

List everything the diff does that the ticket and the use case do not ask for: a new control, a new state, a changed rule, a new string, a changed default. Technical work that changes no behaviour (refactoring, tests, logging) is not listed.

## 3. Report

In the chat, in the language the person wrote in, short and in this order:

1. **Verdict in one line**: matches the ticket, or the number of gaps.
2. **Acceptance criteria**: a table, criterion, verdict, evidence.
3. **Strings**: each difference with its Reference key, the Reference text, the text in the build, and where.
4. **On staging**: what was checked and what did not behave as the use case says, with the steps.
5. **Beyond the ticket**: what the merge request adds.

Every finding has its source: the criterion or use case sentence quoted, the file and line linked. No finding without both sides.

Then say what each kind of finding usually leads to, and leave the choice to the person:

- a criterion not met, or a string that differs from the Reference: back to the developer, or a Bug Sub-Task (jira-ticket skill) when the ticket is already in Ready for QA or later,
- something built that the specs do not describe: it needs a decision first (new-requirement skill), it is not fixed or accepted silently,
- the specs themselves look outdated: the manager runs spec-sync.
