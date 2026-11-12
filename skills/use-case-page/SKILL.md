---
name: use-case-page
argument-hint: <module or page> <the idea, the decision, or the use case to change>
description: "Write and update Confluence use case pages in the Snotor house format: one page per module, intro and Table of Contents, numbered use cases with the role in an info panel, underlined Preconditions, Basic Path and Alternative Path, User Stories with Acceptance Criteria, note panels for asides. Use whenever someone asks for a spec, a use case, a page in Confluence, to describe how a feature behaves, to add or change behaviour on an existing page, or to write up a decision about the product, even if they do not say use case."
---

# Use case pages

The use case page is where the product's behaviour lives. Designers draw from it, developers build from it, QA tests against it, the client reads it, and the tickets link to it. So it has to say exactly what happens, for every person and every case, in words the client can confirm, and nothing else.

Each module has two pages: the use case page (behaviour, this skill) and the Reference page (every string, the reference-page skill). A use case quotes strings, the Reference page owns them.

Before writing, read:

1. **The project profile** (pmo-setup skill): the Confluence space, the module's existing pages, the spelling rules.
2. **The house style** (house-style skill). Every rule there applies here.
3. **What already exists:** the module's use case page and Reference page, and the pages the new behaviour touches. A new rule that contradicts an existing page is a decision for the manager, not something to resolve by editing quietly.
4. **The design**, when one exists for this behaviour: open the actual frames in Figma, never work from a designer's comment alone. Where an approved design and the page disagree, show the difference to the manager in the chat. Which one wins is a project setting in the profile (for example: the approved design wins and the page is realigned to it). If the profile does not say, ask.

**When anything is missing or unclear**, an edge case, a limit, who may do what, what happens on failure, ask the manager in the chat, every time, before writing. Never fill a gap with a plausible behaviour, and never leave a question, a "TBD" or a design note on the page.

## The questions to settle before writing

Work through them with the manager, a few at a time, until each has an answer. A use case is finished when nobody downstream would need to ask any of these:

- Who does this: which role, and who sees the result. Who must not be able to.
- Where it starts and where the person lands after each action, on every platform.
- Every state: empty, first time, many items, loading where it is visible, error, offline when it matters.
- Limits: lengths, counts, sizes, formats, rate limits, time windows.
- What happens on failure, and what is kept or lost.
- What changes for other people (notifications, counts, what they see).
- What differs between the app and web, if anything.
- What is out of scope, so nobody builds it.

## Page structure

The skeleton is `templates/use-case.html`, in Confluence HTML. The example is `references/example.md` (an invented product, Authentication, Use case 1).

1. **Intro**, one or two short paragraphs, no heading: what lives on this page in one sentence, then where the neighbouring things live, as links (the Reference page, related modules, what is postponed).
2. **Table of Contents macro.**
3. **One h1 per use case:** `Use case <n>. <What the person does>`, a verb phrase ("Sign in or sign up with an email code", "Add a player from the team's Members").
4. Under it, an **info panel** with the role: `Role - User`, `Role - Admin`.
5. **Preconditions**, an h3 with the text underlined: bullets, each a state that must be true, in "should" form.
6. **Basic Path**, underlined h3: prose paragraphs in order of what happens. "When the user taps “Continue”, <Product> should send…". Platform differences get their own paragraph ("On web and on the tablet…"). An h4 for a sub-topic that needs its own heading, a table for fields with rules.
7. **Alternative Path**, underlined h3: one paragraph per case, each starting with "If". Every error, every refusal, every edge case the questions above turned up.
8. **User Stories**, a plain h3: a numbered list, one story per item, "As a <role>, I want <outcome>, so that <reason>". After each story a bold **Acceptance Criteria** line and bullets in the present tense, each one checkable by QA ("“Continue” stays disabled until the email address is a valid email format").
9. **Asides** that apply to the whole page (where data comes from, a shared rule) go in a **note panel**, under their own h1 when they are long (for example "Locations", "Email copy").

## Writing rules for use cases

- Describe **behaviour and copy**, never screens in a file: no frame ids, no "see artboard W3", no Figma or design ticket links. Name screens by what they are ("the Enter the code screen").
- Quote every string exactly as the Reference page has it, in typographic quotes. A string that does not exist yet is added to the Reference page in the same change.
- "Should" in Preconditions, Basic Path and Alternative Path. Present tense in Acceptance Criteria.
- Every rule is said once. If another page already defines it, link to it ("as Use case 4 of [Teams] defines") instead of restating it.
- Out of scope is stated plainly when someone would otherwise build it ("Sign-in with other providers is out of the current scope and lives on [Authentication. Postponed]").

## Changing an existing page

1. Read the page as it is now.
2. Change only what the decision changes, in place, so the page always reads as the current truth. No "Update:" paragraphs, no struck-through text, no dates.
3. **Never renumber or rename existing use cases** without updating every ticket that links to them: tickets link to the heading anchor, and a renamed heading breaks those links silently. A new use case is added with the next free number.
4. **Change everything together.** The same decision updates the Reference page, the design ticket or canvas, and the tickets (spec-change skill), even when the manager named only this page. Say in the chat what else you changed.

## Writing to Confluence

- When the manager asked for the page to be written or updated, write it directly once every question is settled. Show the outline first only for a new module page.
- Use the Confluence HTML format from the template: the toc extension, `panel-info`, `panel-note`, `<h3><u>…</u></h3>`.
- Before a new or heavily changed page goes to design or development, ask the **spec-reviewer** agent to review it together with the Reference page, and the **privacy-review** agent too when the behaviour touches personal data (profiles, messages, photos, location, minors, search, sharing, invites, deletion). Bring their blocking findings to the manager in the chat.
- After writing, open the page and check it: TOC renders, every use case has its panel, headings are in the right level, no long dash or semicolon slipped in.
- Report in the chat: which page, which use cases were added or changed, and what else changed with it. Questions that came up go into the chat, never onto the page.
