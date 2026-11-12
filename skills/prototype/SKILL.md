---
name: prototype
argument-hint: <canvas or client prototype> <module and use cases>
description: "Draw a feature from its use case and Reference page in the project's own visual language, as a design canvas for the team (every state, web and app, a note under each frame) and as a clickable prototype the client taps through on a phone (scenarios on the side, each with steps and what to look for). Use whenever someone asks for screens, a sketch, a mockup, a canvas, a design for the designer to start from, a prototype, something to show or send the client, or to try a flow before the design is drawn."
---

# Prototypes

A prototype exists so the client can see and shape a feature while changes are still easy, and so the designer and the developers start from decisions that are already made. It is drawn from the use case and the Reference page, in the project's own visual language, and it never decides anything on its own.

There are two deliverables, built in that order:

1. **The canvas**, for the team: every state of the use case, web and app, each frame with a short note on its logic. Its link goes into the design ticket as the Sketch. See `references/canvas.md`.
2. **The client prototype**, a separate page the client taps through on a phone, with scenarios and plain explanations beside it. One link to send. See `references/client-prototype.md`.

Build the canvas first unless the manager asks only for the client prototype: it is where the states are worked out.

## Before drawing

1. **The project profile** (pmo-setup skill): the platforms and their sizes, and the **design system** row.
2. **The use case and the Reference page.** Every screen, state and string comes from them. Strings are copied exactly from the Reference.
3. **Existing designs** of the neighbouring screens in Figma, opened, so the new screens fit what is already built.
4. **When anything is missing**, a state the use case does not describe, a string the Reference does not have, a decision, ask the manager in the chat. Never draw an invented behaviour: whatever a prototype shows is read as decided, and would end up built. If the gap is a spec gap, it goes back through the interview and use-case-page skills.

## The visual language: where it comes from

Use exactly one source, in this order, and say in the chat which one you used:

1. **The project's design system in Claude**, when the profile links one (a design system artifact or a Design System type). Use its tokens and components as they are.
2. **A style skill for the project**, when the profile names one (built with the design-style skill from a reference site or a Figma file). Load it and follow its rules.
3. **The Figma library**, when there is neither: read the components, variables and a few finished screens with the Figma connector, and draw from what you read. If this happens more than once on a project, propose building a style skill with the design-style skill, so the next prototype does not start from zero.

Never mix sources, never invent a palette, and never fall back to a generic look. Never generate a logo, a wordmark or an icon set: use the files the project supplies, and ask for them if they are missing.

## Rules for everything drawn

- **Copy:** exactly from the Reference, in the in-product spelling. No names on buttons (house-style skill).
- **People and data:** invented names that fit the product's market, one consistent persona per prototype. Never real people, never real personal data.
- **Dates:** one fixed "today" for the whole prototype, so relative dates ("Today", "Tomorrow", overdue) behave the same for everyone.
- **States:** every state the use case names, including empty, error and limits, in the order a person meets them.
- **Platforms and sizes** from the profile (for example app 390, web 1440, tablet and mobile web).

## After building, always

1. Open the page, take screenshots and look at them. On the client prototype, run every scenario from Start to its end, clicking each step, and fix anything that breaks or reads wrong.
2. Compare with the Figma screens the work builds on: spacing, components, colours, copy. Fix the differences before reporting.
3. Check every visible string against the Reference.
4. Publish as an artifact (the person can share the link with designers or the client), and report in the chat what the page covers and anything you could not draw because it is not decided yet.

## When the client answers

Client comments on the prototype are input for the interview skill. A change the client asks for goes through the use case and the Reference first (spec-change skill), then into the canvas and the prototype, so all four say the same thing before any ticket is written.
