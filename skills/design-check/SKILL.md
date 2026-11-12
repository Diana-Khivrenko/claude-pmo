---
name: design-check
argument-hint: <design ticket key or Figma link>
description: "Check a finished design against the use case and the Reference page: open every Figma frame, and list what is missing, what reads differently from the Reference, what contradicts the spec and what the design adds that the spec does not have, each with the frame and the sentence it comes from. Then, on the manager's yes, carry the approved design into the dev tickets. Use when a designer says a design is ready, when someone asks to review, check or compare a design, a Figma file or frames, or before design links go into dev tickets."
---

# Design check

When the designer is done, every frame is compared with the use case and the Reference before anything reaches development. A missing state or a wrong string is cheap to fix in Figma and expensive once it is built.

## Before checking

1. **The project profile** (pmo-setup skill): platforms and sizes, spelling of in-product copy, accessibility level, which source wins when the design and the use case disagree.
2. **The design ticket**: which use cases and frames it covers, the platforms it promises.
3. **The use case and the Reference page** the ticket links to.
4. **The frames themselves**, every one, through the Figma connector (follow its own instructions for sessions). Read the text layers for the exact strings and take a screenshot of each frame to see layout and states. Never check from the designer's message or a summary.

**When anything is missing**, a frame you cannot open, a link to the wrong file, frames for only one platform, ask the manager in the chat instead of checking what you can and calling it done.

## What to compare

| Check | What it means |
|---|---|
| Coverage | Every state the use case describes is drawn, on every platform and size the ticket promises: empty, first time, error, limits, the variants by role, what happens after each action. |
| Copy | Every visible string matches the Reference exactly: wording, capitals, final full stop, spelling of in-product copy. A string that is not in the Reference is either a design invention or a Reference gap. |
| Names on buttons | No button carries a person's, team's or group's name. |
| Behaviour | What the frames show (who sees what, where an action leads, what is disabled) agrees with the use case. |
| Additions | Anything the design shows that the spec does not have: a new control, a new state, a new rule. |
| Design system | Components come from the project's design system or Figma library, not detached copies with different values. |
| Accessibility | At the profile's level: contrast of text and controls, touch targets, a visible focus state on web, enlarged text where the design draws it. |
| Data | Example names and photos are invented, never real people. |

## Report

In the chat, grouped, most important first:

1. **Missing:** states or platforms not drawn.
2. **Copy differs from the Reference.**
3. **Contradicts the use case.**
4. **The design adds something the spec does not have.** These are decisions for the manager, not errors. If the profile says the design wins and the manager agrees, the use case and the Reference are realigned through the spec-change skill.
5. **Design system and accessibility.**

Each finding: the frame (name and link with its node id), what is wrong in one sentence, and the sentence or Reference key it comes from, quoted. No finding without its source. If everything checks out, say so plainly.

Do not post the findings to Figma or to Jira on your own. Ask the manager whether to send them to the designer, and how: Figma comments on the frames, or one comment on the design ticket (house style, kind and neutral, no thanks).

## When the design checks out

On the manager's yes, carry it into development (jira-ticket skill):

1. Put the Figma links into the Design line of each dev ticket.
2. Remove the flag, keep the "is blocked by" link.
3. Comment only on dev tickets that are past To Do. A ticket in To Do gets no comment.
4. Move the design ticket to Done.
5. Report in the chat which tickets were updated.
