---
name: interview
argument-hint: <the idea in two or three sentences, a client message, or a link to a ticket>
description: "Interview the manager about a new idea, a client request or a change, round by round, until every decision a designer, developer or QA would need is made, then hand the decisions to the use case, Reference, prototype and ticket skills. Use when someone brings an idea, a feature request, a client message, a Slack thread or a vague ticket and wants a spec, or says interview me, ask me questions, help me think it through, what am I missing, before any use case is written."
---

# Interview

The interview is where a feature gets cheap: every question answered here is a question the designer, the developers and QA will not ask later, and a change made here costs one chat instead of a redesign. The deliverable is not a document. It is a list of decisions the manager has made, ready for the use-case-page and reference-page skills.

## Before the first question

1. Read the **project profile** (pmo-setup skill) and find the module the idea belongs to. If it belongs to none, that is the first question.
2. Read **what already exists**: the module's use case and Reference pages, the neighbouring modules the idea touches (notifications, search, the admin panel, counts on other screens), and open tickets on the same subject. Use the connectors, do not ask the manager for what you can read.
3. Read the **design** if one exists, the actual frames.
4. Write down for yourself what is already decided by those pages. Never ask a question the pages answer: state the answer and move on ("Members already loads page by page, so the new list does too").

## How to ask

- **Rounds of three to five questions,** grouped by theme, most consequential first. Wait for the answers before the next round, because answers change what is worth asking.
- **Closed questions with a proposal.** Offer two to four concrete options, with the one you would pick first and why in a few words. Use the question tool when the session has one. An open question only when there is no sensible default.
- **Say why each question matters** in a few plain words ("this decides whether QA tests one list or two").
- **Skip the obvious.** A question whose answer would not change the design, the build or the tests is not asked.
- **Surface conflicts.** When the idea contradicts an existing page, show both and ask which wins. Never resolve it silently.
- **Keep a running list** of decisions in the chat after each round, short, so the manager sees what is settled.
- Warm and plain, in the manager's language, never a wall of questions.

## What to cover

Work through these until each is either decided or explicitly out of scope. Not every idea needs every theme.

| Theme | The questions behind it |
|---|---|
| Who | Which role does it, who sees the result, who must not. Admins, guests, people outside the group. |
| Where | Where it starts on each platform, where the person lands after each action, what Back does. |
| What exactly | The fields, the choices, what is required, the order of steps. |
| States | Empty, first time, one item, many items, loading where it is visible, error, offline when it matters. |
| Limits | Lengths, counts, file sizes and formats, rate limits, time windows, what happens at the limit. |
| Failure | What the person sees, what is kept, what is lost, how they retry. |
| Other people | Notifications and push, counts and badges, what changes on other screens, what others are told. |
| Privacy | Who can find out what, what must not leak through a count, an error or a search. |
| Change and removal | Editing, deleting, undoing, what happens to existing data and to content created before. |
| Platforms | What differs between the app and web, what is app only. |
| Neighbours | Search, the admin panel, analytics, the calendar or any module that shows the same thing. |
| Copy | The key strings, which the reference-page skill will turn into entries. No names on buttons. |
| Out of scope | What will not be built now, so nobody builds it. |

## When to stop

The interview is finished when a designer could draw every state, a developer could build it, and QA could write the tests without asking anything. Then:

1. Give the **decision summary** in the chat: what the feature does, the decisions by theme, what is out of scope, and which existing pages change.
2. Ask whether to go on, and with what: the use case and the Reference page (use-case-page and reference-page skills), a prototype for the client (prototype skill), then the tickets (jira-ticket skill).

Never write an open question into Confluence or Jira to "decide later". If something cannot be decided now (it waits for the client, for example), say so in the summary and keep it out of the pages until it is decided.

## When the idea names a solution

An idea often arrives as a solution ("can we have X like in Y"), whoever brings it. Find the need behind it first, so the answer fits the product as it is, and check it against existing decisions before designing anything. If the idea reverses an earlier decision, say so plainly, so the decision is made with the full picture.
