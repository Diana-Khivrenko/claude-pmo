---
name: spec-sync
argument-hint: <module, or "all"> <optional: the report that started it>
description: "Bring a module's use case and Reference pages back in line with its approved Figma design: open every frame of the module, compare every string and every state with the Reference and the use cases, list what drifted, ask the manager which side is right for each difference, and update the pages and tickets on a yes. One module at a time. Use when QA, a developer or a designer reports that the Reference or a use case is outdated or does not match the design, when someone asks to sync, refresh or audit the specs against Figma, or before a module goes to development or regression."
---

# Spec sync

Designs move on in Figma, a string is shortened, a state is added, a flow is redrawn after a review, and the use case and the Reference stay behind. Then QA tests against one text, the developer builds from another, and reports like "the Reference does not match the design" keep coming. This skill sweeps one module at a time, finds every drift, and lets the manager decide each one, so the specs become the truth again.

This is the module-wide sweep. The design-check skill checks one new design ticket before it reaches development. The difference between the build and the specs is a bug (jira-ticket skill), not a spec sync.

## Before you start

Read the **project profile** (pmo-setup skill): the module table (use case pages, Reference page, design ticket), the design project, the spelling of in-product copy, and **which source wins when an approved design and a use case disagree**.

Then gather, for the one module:

1. **The use case pages and the Reference page** of the module, in full. Also the Reference pages of other modules that this module's screens use (shared strings).
2. **The design.** The design tickets of the module in the design project, and the Figma links in them and in the dev tickets. The approved design is the one whose design ticket is Done or whose links are in the dev tickets. Open every frame through the Figma connector (follow its own instructions for sessions): read the text layers for the exact strings, and take a screenshot of each frame to see states, roles and flows.
3. **The report**, if one started this: the exact message, who sent it, what screen it means.

Read the whole file, every page except drafts: the main platforms, and also enlarged text, mobile web and tablet when the file has them. With the Figma connector, a read-only script that returns the visible text of every frame, section by section, is the fastest way to see every string, and screenshots of the sections show the states and the grouping. Note which sections are older and which were added by later design tickets (the section names and the tickets they mention usually say so), because they often disagree with each other.

**When anything is missing or unclear**, ask the manager in the chat before comparing: no Figma link for the module, two files or pages that both look current, frames marked as drafts or explorations, a frame you cannot open. Never compare against a frame that may not be the approved design.

## One module at a time

Run one module per pass. With "all", list the modules from the profile first, then do them one by one: report on a module, settle it with the manager, update it, and only then move to the next. A sweep over the whole product in one report is too long to decide well.

When a report started the sweep, check the reported screen first and settle it, then offer to sweep the rest of the module.

## What to compare

| Check | What it means |
|---|---|
| Copy | Every string in the frames against its Reference entry: wording, capitals, final full stop, placeholders, the in-product spelling the profile names. |
| Missing from the Reference | A string in the frames that no Reference entry carries: a new title, hint, error, toast, empty state, button. |
| Gone from the design | A Reference entry that no frame shows any more. It may be removed from the design, or only not drawn (an error, a limit). Never assume which. |
| Where it appears | The Where it appears column still matches where the string sits and when it shows. |
| Behaviour | What the frames show against the use cases: the states, who sees what (each role), where each action leads, what is disabled, the limits, the order of steps. |
| New in the design | A screen, state, control or rule the design has and no use case describes. |
| Names on buttons | A frame with a person's, team's or group's name on a button is a design error, never copied into the Reference. |

Platforms: compare every platform and size the design has. A string that differs between web and app is either two Reference variants or a design inconsistency, ask which.

## Report and decide

In the chat, per module, grouped and numbered so the manager can answer by number:

1. **Copy differs:** the key, the Reference text, the frame text, the frame (name and link with its node id).
2. **Missing from the Reference.**
3. **In the Reference, not in the design.**
4. **Behaviour differs from the use case:** the use case sentence quoted, what the frames show.
5. **New in the design.**

6. **The pages break the house rules:** design-status notes ("What the design still has to settle", "not drawn", **new** markers), design sources in the pages (design ticket keys, Figma links, artboard or frame numbers, "Screens - artboards" lines), and notes that are no longer true.

For each, propose a direction, and ask closed questions where it is not mechanical: "1 to 6, take the design text, yes?", "8: the error is not drawn, keep it in the Reference?". **Which side is newer decides, not only the profile's rule.** The profile's rule (for example: the approved design wins) holds when the frame is as new as the decision. When the spec carries a decision made after the frame was drawn (a later design ticket redrew the same thing, the manager decided it later, testers' feedback changed it), the spec wins and the frame goes to the designer. Older sections of a file often lag behind the newer ones: compare them with each other too, and when two sections draw the same string differently, the newer section is the design.

A design that looks like a mistake (a name on a button, spelling that differs from the profile's, a typo, a state that contradicts another decision) is never taken over: it goes in a separate list for the designer.

Open the report with one or two sentences on where the drift is concentrated (for example "the newer sections match, the original main set lags"), so the manager sees the shape before the list.

Never write the findings, open questions or "not drawn" notes into Confluence or Jira. They stay in the chat.

## Update on a yes

Carry every decided difference through the spec-change skill, so each lands everywhere it lives:

1. **Reference page:** change the text, keep the key. A new string gets a new key in the right section. A removed string is deleted only on the manager's yes.
2. **Use case page:** rewrite the steps, states and alternative paths in place, in the house format. No "updated" notes, no dates, no frame ids, no Figma links.
3. **House-rule cleanup**, on the manager's yes: remove design-status sections and notes, **new** markers, design ticket keys, Figma links and artboard references from both pages. A note that records a real product decision ("the body names no person, because not every product language can build a pronoun from a name") stays, rewritten as the rule without the design history.
4. **Tickets**, by the status rules of the jira-ticket skill. To Do: rewrite with no comment. In Progress: rewrite, one comment. Code review: rewrite, back to To Do, one comment. Ready for deploy, Ready for QA, Testing (QA): never edited, a new linked ticket for the change and a comment for QA on the old one.
5. **Canvas and client prototype**, if the module has them (prototype skill).

Never edit Figma. Design errors go to the designer only when the manager says so, as Figma comments on the frames or one comment on the design ticket, kind and neutral, no thanks.

If the sweep was started by a report, tell the manager what to answer the reporter, and offer a reply in the message skill's style. Do not reply in Jira or Slack on your own.

## Finish

Report in the chat for the module: what was changed on which page, which tickets were updated or created, what went to the designer, what was left as is and why. Then ask whether to move to the next module.
