---
name: spec-change
argument-hint: <the decision, or the comment or message it comes from>
description: "Carry one product decision into every place it lives, in one go: the use case pages, the Reference pages, the canvas and the client prototype, the design tickets and the dev tickets, each handled by its own rules. Use whenever a decision changes or is added (client feedback, a designer's comment, a developer's finding, the manager's call), whenever someone asks to update the spec, the Reference, a string, a limit or a ticket, and whenever only one place is named but others say the same thing."
---

# Spec change

The use case, the Reference page, the prototype and the tickets must say the same thing at every moment, because each of them is someone's source of truth: the client reads the prototype, the designer the Reference, the developer the ticket, QA the use case. A decision changed in one place and not the others is how a feature gets built wrong.

**The standing rule:** when a decision is stated plainly, change it everywhere it applies, even if the request named only one place ("update the Reference" also means the use case and the tickets), without asking first. Ask only when the decision itself is unclear, or when it contradicts another decision.

## 1. Understand the decision exactly

- Restate it to yourself in one sentence: what was true, what is true now, for whom.
- If it comes from a **designer's comment**, open the actual Figma frames first and see what they drew. Never update from the comment text alone.
- If it comes from a **request** (the client's or anyone's), find the need behind it (interview skill), and check it against existing decisions.
- **When anything is unclear**, the exact new wording, the new limit, which roles it covers, ask the manager in the chat before changing anything.

## 2. Find every place it lives

Search, do not rely on memory. With the connectors:

- **Confluence:** the module's use case and Reference pages, and every other page that quotes the same rule or string (search by the string, the key and the main words). Shared strings often live on another module's Reference.
- **Design:** the canvas and the client prototype artifacts for this feature, and the design ticket in the design project.
- **Jira:** the Feature, its sub-tasks and bug sub-tasks, and any other ticket whose description quotes the old rule or string (search the text).
- **The project profile**, only if the decision is a working setting rather than product behaviour.

Write the list in the chat as a short impact map: each place, what changes there, and its status for tickets.

## 3. Change them, in this order

1. **Use case page** (use-case-page skill): change in place, no "Update" notes, no dates. Never renumber or rename a use case heading without fixing the ticket links to it.
2. **Reference page** (reference-page skill): change the entry, keep the key. A new string gets a new key.
3. **Canvas and client prototype** (prototype skill): redraw the affected frames and scenarios, then open them and check the result against the Figma screens and the Reference.
4. **Design ticket:** update it if the designer has not started, otherwise follow the same status rules as dev tickets in the design workflow. If the design must change, the dev tickets that depend on it get the "is blocked by" link and the flag again.
5. **Dev tickets** (jira-ticket skill), by status:

| Where the ticket is | What to do |
|---|---|
| To Do | Rewrite the description. No comment. |
| In Progress | Rewrite the description, leave it in In Progress, one comment saying what changed. |
| Code review | Rewrite the description, move it back to To Do, one comment. |
| Ready for deploy, Ready for QA, Testing (QA) | Do not edit. Create a new ticket for the change (same parent and platform, full description), link the two, and leave one comment for QA on the old ticket: what stays tested there, what moves to the new ticket. |
| Ready for QA, when the screen got a whole new design | Close the old ticket with one comment that testing is not needed because the new design is built in the new ticket. |
| Done | Leave it. The change is a new ticket. |

Comments follow the house style: kind, neutral, no thanks, explaining the behaviour and its constraints.

## 4. Check and report

- Re-read every changed place and make sure the wording, the numbers and the strings are identical everywhere.
- Then hand the decision and the impact map to the **verifier** agent, which checks every place live, searches for anything still saying the old thing, and checks the tickets against the rules. Fix what it finds before reporting.
- Report in the chat as a short table: place (linked), what changed, and for tickets what was done (rewritten, moved, new ticket, closed).
- Questions that came up during the change go into the chat, never into a page or a ticket.

## Never

- Leave the old and the new behaviour side by side anywhere.
- Change Figma files yourself: the designer owns them, the design ticket carries the change.
- Write "changed on", "previously", "as agreed with" on a page or in a ticket.
- Stop after the place that was named, when others say the same thing.
