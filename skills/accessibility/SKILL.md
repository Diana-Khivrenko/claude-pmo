---
name: accessibility
argument-hint: <set up, ticket, audit> <project, module or ticket keys>
description: "Make accessibility part of a project: set up the accessibility pages in Confluence (the standard, the Definition of Done for design and front end, the QA testing guide), write concrete accessibility acceptance criteria into every user-facing ticket, audit open tickets that lack them, and file accessibility bugs with the WCAG criterion. Use whenever someone mentions accessibility, a11y, WCAG, screen readers, VoiceOver, TalkBack, keyboard navigation, contrast or text size, sets up a new project, or asks why tickets have no accessibility criteria."
---

# Accessibility

Accessibility is part of done on every screen, never a separate project later. The first project run with this plugin worked this way: one standard for the whole product, a Definition of Done every design and front end task is measured against, a testing guide for QA, and concrete criteria in every user-facing ticket. This skill brings the same to any project.

Before anything, read the **project profile** (pmo-setup skill): the accessibility level, the exceptions (for example an internal admin panel), the platforms, the themes and the product languages. **When anything is missing**, the level, whether there is a dark theme, which areas are excepted, ask the manager in the chat.

## 1. Set up the pages (once per project)

Check first whether the project already has them (search the space for "Accessibility" and "WCAG"). If it does, compare them with the templates here and offer to fill the gaps, never overwrite.

Otherwise create three pages in the project's space, in the house style, adapted to the profile (platforms, themes, languages, level):

1. **Accessibility**, the home page: the standard in one bold sentence ("<Project> follows WCAG 2.1, levels A and AA, across the whole product"), where it applies (platforms, themes, languages), and links to the two working pages, with one line on who uses each.
2. **Accessibility Definition of Done**, from `references/definition-of-done.md`: what every design and front end task must satisfy, by criterion, with what to do, how on each platform, and when it is done, plus the per-task verification checklist.
3. **Accessibility testing guide**, from `references/testing-guide.md`: severity levels, tools, the checklists for web, iOS and Android, the cross-platform critical flows, the bug template and the release sign-off criteria.

Show the outline to the manager before creating, then create, open each page and check it. Add the link of the home page to the profile's Accessibility row.

## 2. Accessibility in every user-facing ticket

Every sub-task with a user-facing surface (web or app front end, and the design ticket) carries an accessibility criterion in its Acceptance Criteria, unless the area is excepted in the profile. Backend and technical sub-tasks do not.

The criterion is **concrete for this screen**, never a generic line. Write it from the Definition of Done, naming the real elements, as described in `references/ticket-criteria.md`. For example: "Accessibility: contrast meets WCAG 2.1 AA, Add a player is a real button reached by keyboard in visual order after the chips, focus moves to the Add a player page when it opens and returns to the Add a player button after back, the toast is announced, and the row holds at 200% zoom".

The jira-ticket skill applies this when writing tickets. The design-check skill checks the design for contrast, touch targets, focus states and enlarged text.

## 3. Audit open tickets

When asked to bring existing tickets up to the standard:

1. Find the open user-facing sub-tasks of the project (or the module) whose description has no accessibility criterion.
2. Show the list in the chat, grouped by status, and get the manager's yes before changing anything. This can be many tickets, and each change may notify people.
3. Add the concrete criterion by the status rules of the jira-ticket skill: To Do, rewrite with no comment. In Progress, rewrite with one comment. Code review, rewrite, back to To Do, one comment. Ready for deploy, Ready for QA, Testing (QA), do not edit: one new linked ticket carrying the accessibility work for that screen, with a comment for QA on the old one.
4. Report what was changed, ticket by ticket.

## 4. Accessibility bugs

Bugs follow the bug template of the jira-ticket skill, with two additions:

- **Preconditions** name the assistive technology and setting (VoiceOver on iOS, TalkBack, keyboard only on web, largest text size, dark theme).
- **Expected result** names the WCAG criterion it breaks, by number and name ("WCAG 4.1.3 Status Messages: the toast is announced without moving focus").

## 5. In specs and strings

- The use case describes what is announced when it matters (a toast, an error, a loading state) and where focus goes when a sheet or page opens and closes.
- The Reference page has an entry for every icon control with no visible text, carrying its accessible name, and the accessible name of any control whose spoken name differs from its text (reference-page skill).
