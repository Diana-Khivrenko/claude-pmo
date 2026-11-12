# snotor-pmo

Skills for product owners and project managers at Snotor: how we set up Jira, write tickets, write Confluence use case and Reference pages, build prototypes, check designs and write to clients and the team. One standard for every project, and project specifics (Jira key, platforms, people) live in each project's profile, never in the skills.

## Skills

| Skill | Status | What it does |
|---|---|---|
| `pmo-setup` | 0.1, draft | Creates and keeps the project profile, the Confluence page every skill reads for keys, tags, owners and conventions |
| `message` | 0.1, draft | Writes warm, clear English messages for Slack, email, Jira and Figma from notes in any language, drafts only |
| `house-style` | 0.1, draft | The writing rules for every page, ticket, comment and string: punctuation, spelling, UI strings, what never goes in |
| `new-requirement` | 0.1, draft | The gate for anything new: confirms it should be built and that the project's decision makers agreed, then runs interview, optional design, Confluence and only then tickets |
| `interview` | 0.1, draft | Interviews the manager about an idea or a client request until every decision is made, before any use case is written |
| `use-case-page` | 0.1, draft | Writes and updates Confluence use case pages in the house format |
| `reference-page` | 0.1, draft | Writes and updates the Reference page of a module: every string once, with its key and where it appears |
| `prototype` | 0.1, draft | Draws the canvas for the team and the clickable prototype for the client from the use case and Reference |
| `design-style` | 0.1, draft | Builds a reusable style skill from a reference site, screenshots or a Figma library |
| `spec-change` | 0.1, draft | Carries one decision into the use case, Reference, prototype, design ticket and dev tickets, each by its own rules |
| `accessibility` | 0.1, draft | Sets up the accessibility standard, Definition of Done and testing guide in Confluence, and writes concrete accessibility criteria into every user-facing ticket |
| `spec-sync` | 0.1, draft | Sweeps one module at a time against its approved Figma design and brings the use cases, Reference and tickets back in line, on the manager's yes |
| `build-check` | 0.1, draft | Checks a merge request and staging against its ticket, the use case and the Reference, read-only, for anyone on the project |
| `bug-cause` | 0.1, draft | Finds where in the code a bug happens and why, with how sure it is, and writes the Cause section without the fix |
| `design-check` | 0.1, draft | Checks every Figma frame against the use case and Reference, then carries the approved design into the dev tickets |
| `jira-epics` | 0.1, draft | Agrees the module and standing epics with the manager, creates them with links to the specs, and checks that tickets sit under the right epic |
| `jira-setup` | 0.1, draft | Sets up a Jira project to the Snotor standard, or audits an existing one |
| `qa-summary` | 0.1, draft | Connects a repository to Jira: on merge, CI posts the merge request's description as a comment on its ticket through an automation webhook, for GitLab, GitHub or Bitbucket |
| `jira-ticket` | 0.1, draft | Writes, creates and updates Features, platform sub-tasks, design tickets and bugs to the Snotor standard |

## Agents

| Agent | What it does |
|---|---|
| `spec-reviewer` | Reviews a use case and Reference page with fresh eyes before design or development: gaps, contradictions, untestable lines, mismatches, house format and style. Read-only |
| `privacy-review` | Reviews a spec for personal data: who sees what, leaks through counts, search and errors, minors, deletion, retention, third parties. Driven by the profile's markets, never a legal verdict. Read-only |
| `board-health` | On request, a check of a project's board: tickets with no use case, flags with no blocking link, missing people, bugs with no link, stuck tickets, new behaviour outside the process. Report in the chat only. Read-only |
| `verifier` | After any change, checks live that it landed everywhere, finds places still saying the old thing, and checks tickets and pages against the rules. Read-only |

The skills call them at the right moment (spec-change, new-requirement, use-case-page), and you can also ask for them directly.

## One rule for every skill

When a skill does not find something it needs (an owner, a page, a key, a decision), it asks the manager in the chat, every time. It never guesses and never writes a placeholder or a question into Jira or Confluence.

## Install

Claude Code:

```
/plugin marketplace add Diana-Khivrenko/claude-pmo
/plugin install snotor-pmo@snotor-pmo
```

Cowork: ask the organisation admin to add the plugin from this repository to the organisation's plugin catalog.

## Contributing

Change a skill in a branch and open a pull request. Every rule in a skill says why it exists, so a reviewer can tell a rule from a habit. Bump `version` in `.claude-plugin/plugin.json` when a change is merged.
