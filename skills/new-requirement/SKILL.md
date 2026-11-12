---
name: new-requirement
argument-hint: <the request, the message or the ticket it comes from>
description: "The gate for anything new, in any project: when someone asks for a ticket, a story or a bug report that is really a new feature or a change of behaviour the specs do not describe, confirm it should be built and who decided it, then run it through the full process (interview, optional design, Confluence, then tickets) so no requirement reaches Jira without a use case behind it. Use whenever a request adds or changes behaviour, when a bug report asks for something the use case does not say, when someone outside product management asks for a new feature or improvement, or when a ticket would have no use case to point to."
---

# New requirement

A ticket is the last step, never the first. When a requirement goes straight into Jira, the use case and the Reference fall behind, QA tests against pages that no longer describe the product, and nobody can tell later where the rule came from or who agreed to it. This skill stops that: anything new is confirmed, decided, written into Confluence, and only then turned into tickets.

## 1. Is it new?

Read the project profile (pmo-setup skill), then the use case and the Reference of the module the request touches. Sort the request into one of three:

| What it is | How to tell | What happens |
|---|---|---|
| **A bug** | The product does something the use case or the Reference says it should not, or does not do what they say. You can quote the sentence. | A bug through the jira-ticket skill. This skill stops here. |
| **A gap** | The specs are silent on a case that the existing feature clearly has to handle (an error, an empty state, a limit), and nothing new is added for the user. | Ask the manager how it should behave, then the spec-change skill, then the bug or ticket. |
| **A new requirement** | It adds something (a screen, a control, an option, a rule, a notification), or asks for behaviour different from what the specs say, even when it is written as a bug ("it should also…", "it would be better if…", "users expect…"). | Continue with this skill. |

Say in the chat which of the three it is and why, quoting the use case sentence or saying that no sentence covers it. When it is not clear, ask the manager.

## 2. Confirm before any work

Who asks matters, and every project has its own people who can decide. Take them from the profile's row **Who decides new requirements**, by name and role, never from another project or from habit. When the profile does not say, ask the manager who decides on this project and offer to add it to the profile. When the person asking is not one of them, or you cannot tell who is asking, ask:

1. **Are you sure this has to be built?** In plain words, what changes for the user, and what happens if it is not built.
2. **Who decided it?** Which of the people who decide on this project, in a meeting, in a message, in a client request. A link or a quote when there is one.
3. **Is it for this release?** Or something to keep for later.

Then:

- **Decided by someone the profile names**: carry on with step 3.
- **Not decided yet**: do not open a page or a ticket. Offer a short message to the person who decides, as the profile names them, in the house style (message skill) that says what is asked, by whom and why, and ends with an open question. Stop until the decision comes back.
- **For later**: offer to note it in the module's Postponed page or the backlog the profile names, written as a request, never as a requirement.

When one of the people who decide runs this skill, step 2 is a single question: "This is new, shall I run it through the full process?"

## 3. The full process, in order

Each step uses its own skill and its own rules. Do not skip ahead, and report in the chat after each step before starting the next.

1. **Interview** (interview skill): rounds of closed questions until every decision is made: who, when, what they see, what happens after, the limits, the errors, the roles, what notifies whom. Nothing is written anywhere until the interview is done.
2. **Design**, optional. Ask whether this needs design: a new screen, state or control usually does, a rule or a limit behind existing UI often does not. If it does, the prototype skill for a canvas or a client prototype when the manager wants one, and a design ticket in the design project (jira-ticket skill, design template) once the use case exists. Areas the profile marks as "no design ticket" skip this.
3. **Confluence**: the use case page (use-case-page skill) for new behaviour, the Reference page (reference-page skill) for every new string. When the request changes something that already exists, the spec-change skill instead, so every page that says the old thing is updated.
4. **Tickets** (jira-ticket skill): the Feature and the platform sub-tasks, written from the updated use case and Reference and linked to them, blocked by the design ticket and flagged when there is one. Drafts first, created on the manager's word.

Between steps 3 and 4, the **spec-reviewer** agent reviews the new or changed pages (and the **privacy-review** agent when personal data is involved), and blocking findings are settled with the manager before any ticket is written. After step 4, the **verifier** agent checks that pages and tickets say the same thing and follow the rules.

At the end, report in the chat: the decision and who made it, the pages changed, the design ticket, the tickets created, each as a link. If the request came from a person outside product management, offer a short reply telling them where it landed.

## What never happens

- No ticket for new behaviour without a use case behind it.
- No requirement written into Confluence or Jira that nobody with the right to decide has confirmed.
- No new behaviour slipped into a bug ticket. If a bug report also asks for something new, split it: the bug as a bug, the new part through this skill.
- No open question, no "requested by" history and no decision log on the pages. The use case describes the product as it will be, the decision trail stays in the chat and the messages.
