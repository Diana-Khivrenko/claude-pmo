---
name: jira-epics
argument-hint: <create or audit> <project key>
description: "Fill a Jira project with epics: agree the list of module epics and standing epics with the manager, create them with a short description and links to the use case and Reference pages, record their keys in the project profile, and audit whether existing Features and tasks sit under the right epic. Use when a project needs epics, when someone asks to set up or fill the backlog structure, add a module, or check that tickets are under the right epics."
---

# Jira epics

An epic is the home of one module. Every Feature, task and bug of that module lives under it, so the board can be read by module and nothing floats without a home. This skill creates the epics and keeps tickets under the right ones. The tickets inside the epics are the jira-ticket skill's job.

Before anything, read the **project profile** (pmo-setup skill): the Jira site and development project key, the Confluence space, and the module table. **When anything is missing**, ask the manager in the chat.

## 1. Agree the list in the chat

The list of epics is decided with the manager, never guessed from documents alone.

1. Read what already exists: the epics in the project (with their status and how many tickets each has), and the module pages in the project's Confluence space, if there are any.
2. Propose the list in the chat as a table: epic name, what it holds in one line, the Confluence pages it would link to, and whether it already exists.
   - **Module epics**, one per module of the product (for example Authentication, Profile, Chat, Calendar).
   - **Standing epics**, proposed every time and decided by the manager for each project. The usual set: Foundation & Project Setup, DevOps, Security, Tech debt, Other development tasks, and Admin panel when the product has one.
3. Ask closed questions where the split is not obvious: one epic or two, does this belong to a module or to Other development tasks.
4. Create nothing until the manager says yes to the list.

Rules for the list:

- One epic per module, never per platform, release or sprint. Platforms are split in sub-tasks, time in sprints or versions.
- The name is the module name, short and in the words the product uses, no tags, no project name ("Chat", not "[App] <Product> Chat module").
- Never a second epic for something an existing epic already covers. If the existing one has a different name, propose renaming or keep it.

## 2. Create

For each agreed epic that does not exist yet:

- **Summary:** the module name.
- **Status:** To Do.
- **Description**, in the house style:
  - one or two sentences on what the module covers, in the product's words, from the use cases or from what the manager said. Nothing invented, no scope the manager did not confirm.
  - **Use cases:** links to the module's use case pages, when they exist.
  - **Reference:** link to the module's Reference page, when it exists.
  - Standing epics get only the sentence on what goes there (for Other development tasks: work and bugs that belong to no module).
- No comments, no assignee unless the manager names one.

Then open the epics list and check them. Write each new key into the profile's module table (Epic column) and the standing epic for work outside the modules. Report the keys in the chat.

When a use case or Reference page appears later for a module whose epic has no link to it, add the link to the epic's description. An epic description is updated freely at any status, it is a map, not a requirement QA tests against.

## 3. Audit

When asked to check the structure, or right after creating epics on a project that already has tickets:

1. Find the open tickets with no epic: Features, Tasks, Technical tasks and standalone Bugs whose parent is empty. Sub-tasks are not checked, their parent is a Feature.
2. Find the open tickets likely under the wrong epic: a Feature or task whose title starts with a module name (`Teams: …`, `[BE] Chat: …`) that differs from its epic's name.
3. Find epics with no open and no done tickets, and two epics that look like the same module.
4. Show the result in the chat as tables, with the suggested epic for each ticket and why (its title, its use case link). Ambiguous ones are listed as questions.
5. Move nothing without the manager's yes. On a yes, change only the parent, never the description and never the status, and leave no comments (a parent change needs none, and every comment notifies the team). Report what was moved, ticket by ticket.
6. Empty or duplicate epics are reported, never deleted or merged without the manager's explicit yes.
