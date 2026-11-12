# <Project>. Project profile

Intro paragraph, one or two sentences: this page holds the working settings of the project that people and Claude read before Jira, Confluence or design work. Product behaviour lives in the use case and Reference pages, not here.

Table of Contents macro.

## Project

| Setting | Value |
|---|---|
| Product | <name>, <one line on what it is> |
| Client | <company>, contacts: <name> (<role>), ... |
| Jira site | <https://site.atlassian.net> |
| Development project | <KEY>, company-managed, <Kanban or Scrum> |
| Design project | <KEY>, new design tickets go to <status>, or "none" |
| Standing epic for work outside the modules | <KEY-n> Other development tasks |
| Confluence space | <KEY>, home page <link> |
| Code host | <GitHub or GitLab>, repositories <list>, file links as <https://host/org/<repo>/blob/HEAD/<path>> |
| Environments | stage <url>, production <url> |
| Team Slack channel | <#channel>, Jira notifications: comment added, Bug Sub-Task created |
| Automation rule owner | <name> |
| Design system | <link to the design system in Claude>, or <name of the style skill>, or <Figma library file>, and where the logo and icon files are |
| When an approved design and a use case disagree | <the design wins, or the use case wins> |

## Platforms

| Platform | Tag | Design sizes |
|---|---|---|
| Backend | [BE] | |
| Web | [Web] | 1440, tablet, mobile web |
| App | [App] | 390 |

## Modules

One row per module. The epic is the parent of every Feature in that module. The owners are the default assignees of new tickets.

| Module | Epic | Use cases | Reference | Backend | Web | App | QA owner | Design ticket |
|---|---|---|---|---|---|---|---|---|
| <Module> | <KEY-n> | <link> | <link> | <name> | <name> | <name> | <name or "QA assigns"> | yes |
| <Admin panel> | <KEY-n> | <link> | <link> | <name> | <name> | | <name> | no |

## Team

| Role | People |
|---|---|
| Product owner | <name> |
| Who decides new requirements | <names and roles of the people who can approve new behaviour on this project>, everyone else's requests go through the new-requirement skill |
| Design | <names> |
| Architect | <name> |
| QA | <names> |

## Copy and language

| Setting | Value |
|---|---|
| Spelling of in-product copy | <American English>, a UI string that differs from the Reference is a bug |
| Spelling of specs and tickets | <British or American English> |
| Product languages | <list>, source language <English> |
| Where UI strings live | <repository and path of the translation files, per platform> |
| Date and time format | <for example "Tue, Sep 29, 18:00"> |

## Accessibility

| Setting | Value |
|---|---|
| Level | <WCAG 2.1 AA>, part of every user-facing ticket |
| Exceptions | <for example the admin panel> |
| Themes | <light and dark, or light only> |
| Accessibility pages | <link to the Accessibility home page>, set up by the accessibility skill |

## Privacy

| Setting | Value |
|---|---|
| Markets | <countries and regions the product is offered in> |
| People under 18 | <can use the product, from which age, or not at all> |
| Privacy Policy and Terms | <links> |
| Data protection contact | <name and role, on the client's side> |

## Board health

| Setting | Value |
|---|---|
| Days before a ticket counts as stuck | In Progress 7, Code review 3, Ready for deploy 3, Ready for QA 5, Testing (QA) 5 |
