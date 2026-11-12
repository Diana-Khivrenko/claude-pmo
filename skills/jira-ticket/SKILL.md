---
name: jira-ticket
argument-hint: <feature, sub-task, bug or design, if known> <use case link, ticket key or raw material>
description: "Write, create and update Jira tickets the Snotor way: a Feature per use case, one sub-task per platform, a design ticket that blocks them, and bugs with preconditions, steps, actual, expected and the cause. Covers titles with platform tags, the parent, links, flag, assignee and QA Assignee, the status a ticket is created in, when a ticket goes back to To Do, and when a comment is allowed. Use whenever someone asks for a ticket, a story, a bug report, sub-tasks, dev tickets from a use case, design tickets, rewriting or updating a ticket, or moving designs into tickets, even if they do not say Jira."
---

# Jira tickets

A ticket is what a developer starts from and what QA tests against. It has to be complete enough that nobody comes back to ask what was meant, and short enough to read in a minute. Every rule below exists because breaking it once cost the team time: read the why, it tells you what to do in the cases the rule does not name.

Before anything else, read:

1. **The project profile** (see the pmo-setup skill, and until a profile exists, ask for the values listed in "What the profile gives you" and offer to write them down). Never guess a project key, a tag, a developer or a QA person.
2. **The source.** The use case and the Reference page for a Feature, sub-task or design ticket. For a bug, the use case or Reference text that defines the expected behaviour. When a design exists, open the actual frames in Figma before writing, never work from a designer's comment alone.
3. **The template for the ticket type** in `templates/`, and the matching example in `references/examples.md`.

**When anything is missing**, a module owner, a QA person, a page, a key, a tag or a decision, ask the manager in the chat, every time, and carry on once they answer. Never guess, and never leave a placeholder or a question in Jira or Confluence instead of asking. If the answer is a lasting setting, offer to add it to the project profile.

## New behaviour goes through the gate first

Before drafting, check that the request is covered by the use case and the Reference. A request that adds or changes behaviour the specs do not describe, including one written as a bug ("it should also…"), is not a ticket yet: run the new-requirement skill, which confirms it, gets it decided, interviews, designs if needed and updates Confluence, and only then comes back here. A bug report that also asks for something new is split: the bug here, the new part through new-requirement.

## Drafting first, creating only on request

The default deliverable is the draft: title, description and the fields (parent, links, flag, assignee, QA Assignee, status), shown in the chat.

- Create in Jira only when the person says so in plain words ("create them", "put them in Jira"). "Write the tickets" means drafts.
- When creating, do everything in one pass: the ticket, the parent, the "is blocked by" link, the flag, the assignee, the QA Assignee, the status. Then report the keys as links. A half-created ticket (no link, no flag) is worse than none, because it looks finished.
- Two read-only checks run before a draft is final, each one narrow search: the **parent** (propose the best match, name the runner-up when the choice is not obvious, ask when nothing fits) and **duplicates** (search the two or three most distinctive words of the title, and if a likely duplicate exists, stop and show it).

## What a ticket never contains

- **Invented scope.** Only what the use case, the Reference and the design say. A gap is not filled with a plausible requirement: it becomes a question to the person in the chat. An invented requirement breaks the spec and confuses the board, which is worse than a gap left open.
- **Open questions.** No "TBD", no "to confirm", no question in the description or in a comment. A ticket with a question in it cannot be started. Ask in the chat, decide, then write the answer in.
- **Technical decisions.** No "Technical notes" or implementation design, the architect owns those. A bug's Cause section says where and why the defect happens, it never prescribes the fix.
- **Names on buttons.** No person, team, group or other proper name in a button label, in the title, the specification or the acceptance criteria ("Leave", "Remove from the team", never "Leave Riverside FC"). Names may appear in titles and body text of the product, never on a button. Every user-facing ticket carries the criterion "No button carries a name".
- **Dates and provenance.** No "decided on 12 November", no "as agreed with the client". State what is true. Jira already records who and when.
- **Rules cited by number.** Not "per rule 4", state what the rule requires.
- **Design sources in the wrong place.** Design links belong in dev and design tickets (the Design line), never in Confluence use cases.

## Writing rules

The house-style skill applies in full. The points below are the ones tickets break most often.

- **Every key and every document is a link.** `[PEB-310](https://<site>/browse/PEB-310)`, `[Teams, Use case 6](<page url>#<anchor>)`. A bare key or "see the spec" makes the reader go searching. The title is the exception: Jira's summary is plain text.
- **UI copy is quoted exactly** from the Reference page, in the spelling the profile names for in-product copy. Ticket prose may follow the team's own spelling.
- **House punctuation:** no long dashes anywhere, a comma where a semicolon would go, Markdown for Jira (`##`, `###`, `**bold**`, lists, backticks for code names).
- **Neutral, factual tone.** Say what the product does and should do. No metaphors, no drama.
- **Accessibility** is part of done on every ticket with a user-facing surface, at the level the profile names (for example WCAG 2.1 AA), unless the profile lists an exception (for example an internal admin panel). It is an acceptance criterion in the same ticket, never a separate ticket, written concretely for the screen as the accessibility skill describes.

## Titles

| Type | Pattern | Example |
|---|---|---|
| Feature | `<Module>: <use case name>`, no tag | `Teams: Add a player from the team's Members` |
| Sub-task | `<tag> <the Feature's title>` | `[Web] Teams: Add a player from the team's Members` |
| Bug Sub-Task | `<tag> <Module>: <what is wrong> <where> <when>` | `[App] Teams: The last-coach hint under Leave team is cut off in the team menu` |
| Design ticket | `[Design] <Module> - <what> (<platforms>)` | `[Design] Teams - Add a player from the team Members (Web and App)` |

Platform tags come from the profile, always first, one per platform: for example `[BE]`, `[Web]`, `[App]`. A bug that affects two platforms the same way carries both tags, `[Web][App]`. The tag follows where the fix lands, not who found it.

## Hierarchy and splitting

- **Epic** per module, created once (jira-epics skill). Work that belongs to no module goes under the standing epic "Other development tasks".
- **Feature** per use case. Holds the why and the links, no acceptance criteria.
- **One sub-task per platform** under the Feature, each with its own specification and acceptance criteria. This is what a developer picks up and QA tests.
- **Bug Sub-Task** under the Feature whose behaviour it breaks, **linked "relates to" the platform sub-task it breaks** (the [Web] sub-task for a web defect, both platform sub-tasks for a [Web][App] bug). The parent shows which use case is broken, the link shows which piece of work QA tested and the developer reopens. A bug that repeats or follows from another open bug is also linked "relates to" that bug.
  - Bug Sub-Task is the first choice. A bug filed outside its Feature is invisible on the Feature, does not hold the Feature back from Ready for QA (the automation counts its sub-tasks), and is easy to miss when that use case is tested.
  - Find the Feature first: search the project for the module and the use case the behaviour belongs to, and open the Feature to check its sub-tasks. If there are several candidates, ask the manager in the chat which one.
  - When no Feature fits (the area was built before Features were used, the defect spans several modules, or it has no product behaviour behind it, like a CI runner or an alert rule), a standalone Bug or Technical task is fine, under the module's epic or "Other development tasks". It is still linked "relates to" the tickets it concerns, when there are any.
- **Technical task / Technical Sub-task** for infrastructure, security, CI and tech debt.
- Never a parent with a single child. Two small pieces go as siblings under the existing Feature. Split only along a real seam (a platform, a separately shippable piece, two outcomes a user would notice separately), never to make a ticket shorter. State the seam in one sentence when you split.

## Design tickets and the blocking rule

- A design ticket goes to the design project from the profile, with no parent, in the status the profile names for new design tickets (for example Selected for Development, where a design workflow has no To Do).
- Every dev sub-task that needs that design is linked **"is blocked by"** the design ticket **and flagged**, at the moment it is created. The link says what it waits for, the flag shows the wait on the board.
- The same rule holds for any other dependency: a ticket waiting on another ticket gets the link and the flag, and normally stays in To Do. The Blocked status is rarely used.
- Work the profile lists as "no design ticket" (for example an internal admin panel) gets no design ticket, no link and no flag.
- **When the design arrives:** put the design links in the Design line of each dev ticket, remove the flag, keep the link. Comment only if the ticket is past To Do (see Comments).

## Fields and statuses

- **Status at creation:** To Do in the development project, never Backlog.
- **Assignee:** always. The developer who built that module on that platform, from the profile. If the profile does not say, ask, never leave it empty.
- **QA Assignee:** on Sub-task and Bug Sub-Task, set to the module's QA owner when the profile names one. Otherwise leave it for QA to fill. Never on a Technical Sub-task.
- **Never move a ticket to Ready for QA.** Only developers do that.
- **Requirements change, by where the ticket is:**
  - **To Do:** rewrite the description, no comment.
  - **In Progress:** rewrite the description, leave the ticket in In Progress, one comment. The developer is working on it right now, so the comment tells them what changed.
  - **Code review:** rewrite the description, move the ticket back to To Do, one comment. The work is considered finished, and nobody revisits a ticket in review for new requirements, so a silent rewrite would never be read.
  - **Ready for deploy, Ready for QA or Testing (QA):** never edit it. What it describes has been built and is being shipped or tested against that text, so changing it would make QA test against requirements the code was never written for. Create a new ticket for the change (same parent, same platform, written in full in the template, not as a diff), link the two with "relates to", and leave one comment on the old ticket for QA: which behaviour stays tested here and which moves to the new ticket, with the new key linked.
- **A screen that gets a new design:** the old dev tickets for that screen waiting in Ready for QA are closed (Done) with one comment saying testing is not needed because the new design is built in [the new ticket], rather than being sent back to To Do.

## Comments

Every comment reaches the whole team's Slack channel. So:

- **Never comment on a ticket in To Do**, including one you just created or just rewrote. Nobody has opened it yet, the description is what gets read.
- **One comment per change** on a ticket somebody has already started (a ticket in In Progress, one sent back to To Do from Code review, or a ticket in Ready for deploy, Ready for QA or Testing (QA) that gets the QA comment about a new ticket): what changed and why it matters for the work. A correction to your own change edits that same comment, never a new one.
- **Tone:** kind and neutral, no thanks, no greetings. Explain the behaviour of the system and its constraints in enough detail that the developer does not need to open anything else to understand the change.
- No comments just to pass on a link or to say a design is ready.

## Updating existing tickets

1. Read the ticket, its status, its parent and its links first.
2. If the ticket is in Ready for deploy, Ready for QA or Testing (QA), stop editing it: create the new linked ticket and the QA comment as described above.
3. Otherwise rewrite the description in the current template, keeping everything still true. Do not append "Update:" paragraphs, the description always reads as the current truth.
4. Apply the status and comment rules above according to where the ticket is.
5. When the change comes from a spec decision, the use case page, the Reference page and the design ticket change with it (the spec-change skill), even if the person named only the ticket.

## What the profile gives you

Jira site URL, development project key, design project key and its new-ticket status, platform tags, the epic for each module, developers per module and platform, QA owner per module, accessibility level and exceptions, areas with no design ticket, spelling for in-product copy, Confluence space, code host URL pattern for linking files in a bug's Cause.

## Before you hand over a draft

Check every draft against this list and fix what fails:

- Title follows the pattern, tag first for sub-tasks and bugs.
- Parent set and correct. A bug is a Bug Sub-Task under its Feature, linked "relates to" the platform sub-task it breaks, unless no Feature fits.
- Every key and page is a link.
- Nothing invented, no open question, no technical decision, no date.
- No button carries a name, UI strings match the Reference exactly.
- Accessibility criterion present on every user-facing sub-task (unless the profile excludes the area).
- Blocking link and flag on every dev ticket waiting for a design, unless the area needs no design ticket.
- Assignee set, QA Assignee set when the profile names one, status To Do.
- No edit to a ticket in Ready for deploy, Ready for QA or Testing (QA): a new linked ticket instead.
- No long dashes, no semicolons.
