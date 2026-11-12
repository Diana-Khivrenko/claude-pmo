---
name: reference-page
argument-hint: <module> <the strings to add or change, or the use case they come from>
description: "Write and update the Reference page of a module in Confluence: every string the module shows, once, with its key, its exact text and where it appears, in the Snotor table format. Use whenever someone asks for copy, strings, texts, labels, error messages, toasts, empty states or translations keys for a feature, asks to add or change a string, to check UI copy against the design or the build, or whenever a use case gains or changes a string, even if they do not say Reference."
---

# Reference pages

The Reference page holds every string a module shows, written once, so the designer, both front ends, QA and the translators all use the same words. The use case page describes behaviour and quotes strings, the Reference page owns them. A string that is not on the Reference page does not exist yet.

Before writing, read:

1. **The project profile** (pmo-setup skill): spelling of in-product copy, product languages, the Confluence space.
2. **The house style** (house-style skill), in particular UI strings and names on buttons.
3. **The use case page** of the module: every string the Basic and Alternative Paths quote must be here, and every entry here must be used by a use case.
4. **The existing Reference page** and the Reference pages of neighbouring modules, so a string that already exists elsewhere is reused by pointing to it, not copied.
5. **The design**, when it exists: open the actual frames and compare the strings on them with this page. A difference is either a design bug or a decision, and the manager decides which.

**When anything is missing or unclear**, the exact wording, a plural, a form for a variant, where a string appears, ask the manager in the chat, every time. Never invent a string and never leave a placeholder text or a question on the page.

## Page structure

The skeleton is `templates/reference.html`. The example is `references/example.md` (an invented product, Teams. Reference).

1. **Title:** `<Module>. Reference`.
2. **Intro**, one paragraph, no heading: "Every string of <what>." Then "Behaviour lives on <use case page>", with which use case covers which section ("Use case 1 for sections 1 and 2, Use case 4 for sections 4 to 6").
3. **How to read this page**, a paragraph starting with that phrase in bold: that one entry serves web and the app unless it says otherwise, what square brackets mean, the placeholder legend ([group], [first name], [n]), and how variants are written.
4. **Table of Contents macro**, first level only.
5. **One h1 per area or screen,** numbered: `1. The team card`, `2. Add a player`. In the order a person meets them.
6. Under each, **one table** with three columns: **Key**, **Text**, **Where it appears**.
7. Short paragraphs under a table only for what applies to the whole section, and links to where a shared string lives.

## Writing an entry

- **Key:** lowercase, dot-separated, from general to specific, in code format: `players.add.title`, `team.members.add`. Stable: a key never changes once a ticket or the code uses it. A new meaning gets a new key.
- **Text:** the exact string, in the spelling the profile names for in-product copy, with its final full stop or without it, exactly as it ships. No quotes around it.
  - Values the interface fills in are in square brackets: `[first name] is in [group]`.
  - **Variants** (by kind of account or club, by role, by count) are separated by ` · ` in a fixed order that the How to read paragraph names. Repeated parts may be shortened with "…" after the first full form.
  - **Plurals:** give every form: "[n] years, and “1 year” in the singular".
  - **Icon controls** with no visible text are entries too, with their accessible name: "Close, an icon control with no visible label".
  - A string reused from another key says so: "The text of `team.members.since`".
- **Where it appears:** the place on the screen in plain words (title, beneath the title, the primary action, the toast after…), the condition when it shows ("while the team has no players", "unavailable until a member is ticked"), who sees it, and the accessible name when it differs from the text. Never a frame id, a Figma link or a design ticket.
- Examples of filled values use invented names ("as in “Emma · Under 12s”"), never real people.

## Rules every string follows

- **No names on buttons.** A button names the action alone. A name may sit in a title, a line or a row as data.
- Confirmations name the thing by its kind ("the member", "the team"), not by its name.
- One string, one key, one place. If another module's Reference already holds it, link to that entry.
- Errors say what happened and what the person can do next, in the product's voice. The generic error is the project's standard one (for example "Something went wrong. Please try again" with "Try again").

## Changing an existing page

1. Read the page as it is.
2. Change only the affected entries, in place. Keep keys stable. A removed string is deleted from the table, not struck through.
3. **Change everything together.** The use case page that quotes the string, the design, and every ticket that quotes it change with it (spec-change skill), even if the manager named only the Reference page. Tickets already in Ready for deploy, Ready for QA or Testing (QA) are not edited, the change becomes a new linked ticket (jira-ticket skill).
4. Report in the chat which keys were added, changed or removed, and what else changed with them.

## Writing to Confluence

- Use the Confluence HTML from the template: the toc extension with maxLevel 1, numbered h1 sections, three-column tables with the key in `<code>`.
- After writing, open the page and check that every table has the three columns, keys render as code, and no long dash or semicolon slipped into the prose (a dash inside a quoted name such as a double-barrelled surname is data and stays).
