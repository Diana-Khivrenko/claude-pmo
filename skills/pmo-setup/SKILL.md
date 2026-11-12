---
name: pmo-setup
argument-hint: <create, update or show> <project name, Jira key or Confluence space>
description: "Create, update or read the project profile: the one Confluence page per project that every snotor-pmo skill reads for the Jira keys, platform tags, who builds and tests each module, the Confluence space, the code host, spelling and accessibility rules. Use when a project starts using snotor-pmo, when someone asks to set up Claude for a project, when a developer, QA owner, epic, tag or key changes, when another skill cannot find a value it needs, or when someone asks who owns a module or where something lives."
---

# Project profile

Every snotor-pmo skill works the same way in every project because the project-specific values live in one place: a Confluence page called `<Project>. Project profile` in the project's space. The skills never carry those values themselves and never guess them. This skill creates that page, keeps it current, and tells the other skills where it is.

Why Confluence: the whole team can see and correct the page, it outlives any one person's chat, and a new PM gets the same answers as the old one. Why one page: a value written in two places drifts.

## How the skills find the profile

In this order, and stop at the first hit:

1. A line `Project profile: <link>` in the instructions of the Claude project the chat runs in.
2. A Confluence search for a page titled `<Project>. Project profile`, in the space named by the person or by the Jira project.
3. Ask the person. If no profile exists, offer to create one with this skill.

When a skill reads the profile and a value it needs is missing or empty, it asks the manager in the chat, every time, uses the answer for the task, and offers to add it to the profile. It never fills a gap with a guess, because a guessed developer or QA name ends up on every ticket. An empty cell in the profile is normal: it means "ask when it comes up".

On the page itself an unknown value is left empty. Never write "(?)", "TBD" or a question into the profile, open questions stay in the chat.

## What belongs in the profile, and what does not

The profile holds **working settings**: where things are, who does what, which conventions apply. It changes when the team or the setup changes.

It does not hold **product decisions** (those are use cases and Reference pages, where the whole team reads them), personal working preferences of one PM (those stay in that person's own Claude memory), open questions, or anything about people beyond their role and what they own. Never an opinion, a rating or a note on how someone works, decides or communicates, about the client or about the team: the client and the whole team read this page.

The template is `templates/project-profile.md`. Keep its section names and table columns, because the other skills look values up by them.

## Create

1. **Read before asking.** With the connectors, collect what already exists so the person only confirms:
   - Jira: the project key and type, the design project if there is one, the epics (one per module), and for each epic the assignees of recent sub-tasks per platform tag, as a suggestion for module owners.
   - Confluence: the space key, the home page, use case and Reference pages per module.
   - Code host: the repositories, if the connector is available.
2. **Interview for the rest**, a few questions at a time, in plain words: platforms and their tags, QA owner per module, areas that never get a design ticket, spelling for in-product copy, product languages, accessibility level and exceptions, the team Slack channel, who owns the automation rules, the client contacts and their role.
3. **Show the filled page in the chat.** Mark every value that came from a suggestion rather than from the person, and get a yes on those explicitly.
4. **Create the page** in the project's space, in the house format (no long dashes, commas instead of semicolons, tables as in the template). Title exactly `<Project>. Project profile`.
5. **Give the pointer line** for the Claude project instructions, ready to paste:

   ```
   Project profile: <link to the page>
   Use the snotor-pmo skills. Read the project profile before any Jira, Confluence or design work in this project.
   ```

   Claude cannot edit project instructions itself, so tell the person where to paste it: the project in the Claude sidebar, then Instructions.

## Update

When someone says a value changed (a new web developer for a module, a new QA owner, a new platform):

1. Read the page, change only the affected rows, keep everything else exactly as it is.
2. If the change affects work in flight (a new owner of a module with open tickets), say so in the chat and ask whether the open tickets should be reassigned. Do not reassign them without a yes.
3. The profile page is updated without asking first when the person stated the change plainly. It is a settings page, not a decision.

## Show

When asked who owns a module, where a page lives or what the tags are, answer from the profile with the link, not from memory of earlier chats. If the profile and what the person says disagree, the person is right: offer to update the page.

## Writing to the person

Plain and warm. When you ask for a value, say in a few words what it is used for ("the QA owner goes into QA Assignee on every sub-task of that module"), so the person sees why it matters.
