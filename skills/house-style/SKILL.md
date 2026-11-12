---
name: house-style
description: "The Snotor house writing style for everything that goes into Confluence, Jira or a design: punctuation, spelling, quoting UI strings, names on buttons, what never goes into a page or a ticket, and tone. Use whenever you write or edit a use case, a Reference page, a ticket, a comment, UI copy or any other text that lands in the team's tools, and whenever another snotor-pmo skill says to follow the house style."
---

# House style

Everything the team reads is written the same way, so the reader spends their attention on what the text says, not on how it is written. These rules apply to every page, ticket, comment and string. The other snotor-pmo skills point here instead of repeating them.

## Punctuation

- **No long dashes.** Never the em dash or the en dash, anywhere. Use a comma, a colon, brackets, or two sentences. A hyphen only inside words (sign-in, 6-digit).
- **No semicolons.** A comma, or a new sentence.
- **Typographic quotes** around UI strings in prose: “Continue”. In Jira Markdown, plain double quotes are fine.
- Numbers from 1 000 up are written with a space as the thousands separator when the project's copy rules say so ("4 000").

## Spelling

- **In-product copy** (buttons, labels, messages, emails, every string a user sees) uses the spelling the project profile names, for example American English ("organize", "color").
- **Prose** in specs, Reference explanations and tickets may use the team's own spelling, for example British English. The two never mix inside a quoted string: a string is quoted exactly as it ships.
- A shipped string spelled differently from its Reference entry is a bug.

## UI strings

- Quote every string exactly as it stands on the Reference page, character for character, including capitals and the final full stop or its absence.
- Placeholders are written as the Reference writes them, `{email}` or `[name]`, never filled with an example value inside a quoted string.
- **No names on buttons.** No person, team, group or other proper name in a button label, ever: “Leave”, “Remove from the team”, “Make an admin”, never “Leave Riverside FC” or “Remove Sam”. A name may appear in a title, a body line or a row, where it is data, never on a button. Every confirmation names the thing by its kind: “the member”, “the team”.

## What never goes into a page or a ticket

- **Open questions**, "TBD", "to confirm", "decide later". Questions go to the manager in the chat, are decided there, and the answer is written in.
- **Design status notes**, such as "not drawn yet" or "what the design still has to draw". They stay in the chat.
- **Design sources in use cases and Reference pages**: no Figma links, canvases, design tickets, artboard or frame ids (W01, M05). Use cases describe behaviour and copy, not screens in a file. Design links belong in tickets only.
- **Technical decisions** in tickets, unless the architect wrote them. A bug's cause is a finding, not a decision.
- **Dates and provenance**: no "decided on 12 November", no "as agreed with the client". State what is true. The tools record who and when.
- **Rules cited by number** ("per rule 4"). State what the rule requires.
- **Real personal data** in examples or mockups. Use invented names.
- **Opinions about people.** No judgement, rating or characterisation of the client, a colleague or anyone else (how technical, how quick, how easy they are). Clients read the pages, the tickets and the comments.

## Tone

- Plain, specific and neutral. Say what the product does, from the person's side, in words a client can confirm.
- No metaphors, no drama, no filler, no marketing language.
- Comments in Jira are kind and neutral, with no thanks and no greetings, and explain the behaviour and its constraints fully enough that nobody has to open anything else.
- Messages to people (clients, the team) follow the message skill, which is warmer by design.

## Before you hand anything over

Search your own text for: a long dash, a semicolon, a name inside a quoted button label, a question mark outside a quoted string, a date, a Figma or frame reference in a use case or Reference page. Fix every hit.
