---
name: message
argument-hint: <who it is for, the channel, and what to say, in any language>
description: "Write English messages in the Snotor house style: warm, friendly and easy to follow, never short and dry. Each point explains the why in plain words, acknowledges the other person's view, and ends with a gentle open question where a decision is needed. Turns notes in any language into English for Slack, email or a Jira comment, adapted to the reader (client, designer, developer, QA). Drafts only, never sent without a yes. Use whenever someone asks to write, reply to, translate, soften or rewrite a message, a question for the client, an update, a reply to a designer or developer, or says how do I say this in English."
---

# Message

A message is how a decision gets made, a misunderstanding gets cleared, or a person feels heard. A dry message ("Not possible, see spec") gets a dry answer or none. A warm one that explains why gets a real answer. So every message, in every project, is written so the reader understands what is asked, why it matters, and that their view counts.

## Before writing

Work out, from what the person gave you, or ask in one line when it is not clear:

- **Who reads it**: their role (client, founder, designer, developer, QA), and how technical they are. A reader who does not work with code gets the product in plain words, never endpoints, statuses or field names.
- **Where it goes**: Slack, email, a Jira comment, a Figma comment. It sets the length and the shape.
- **What it must achieve**: a decision, an answer, an update, an apology, a no.
- **The facts**: read the ticket, the use case or the thread it answers, when one is named. Never state a rule, a date or a number you have not checked. When something is missing, ask in the chat, never put a placeholder or a guess into the draft.

Notes can come in any language, or several mixed in one message. Write the meaning in natural English, not a word-for-word translation, and keep the names of things exactly as the product and the specs call them.

## The style

**Warm and friendly.** Start with a short, human opening that fits the person and the moment ("Hi Anna, thanks for flagging this", "Hope your week is going well"). Never stiff ("Please be informed"), never gushing.

**Explain the why in plain words.** Every point says what it is and why it matters, in a sentence or two the reader can follow without opening anything. Name the effect on real people: "a member opening the link on their phone would land on a page they cannot use".

**Acknowledge their view.** Before disagreeing or asking for a change, show you understood what they want and why it makes sense ("I can see why showing everyone at once feels simpler"). Then give the other side.

**End with a gentle, open question** where a decision is needed: "What do you think?", "Would that work for you?", "Is there anything I am missing?". Never a closed ultimatum ("Please confirm by Friday").

**Easy to read.** Short paragraphs. Several points get a short introduction ("A few things we'd love your thoughts on:") and then one numbered paragraph each. Options for a decision are named plainly, with what each one means for the user, and a recommendation when there is one.

**Never short and dry.** A one-line answer is fine only when the reader asked a one-line question.

## Per channel

- **Slack**: a greeting, the points, the question. No headings. Bold only for the one thing they must not miss.
- **Email**: a clear subject, a greeting, the points, the question, a friendly sign-off.
- **Jira comment**: the exception. Kind and neutral, no greeting, no thanks. It explains the behaviour of the system and its constraints in enough detail that the developer or QA needs nothing else (jira-ticket skill, Comments). No open question: questions are settled in the chat before anything is written into Jira.
- **Figma comment**: one point per comment, attached to the frame it is about, kind and specific.

## Writing rules

The house-style skill applies to every message: no long dashes, no semicolons, no names on buttons when a button is quoted. Quote UI strings exactly as the Reference has them. British or American spelling for the prose, whichever the person writes in, but UI strings stay as the Reference spells them.

Never in a message: blame, sarcasm, internal gossip, another client's or project's details, anything confidential the reader should not see.

## Deliver

Show the draft in the chat, ready to copy. When the situation has two honest approaches (hold firm or offer an alternative, ask now or decide and inform), show both, each labelled with what it aims for, and let the person choose.

Never send a message, post a comment or reply in a thread yourself unless the person says so in plain words, and then only the exact text they approved.

## Example

Notes from the manager, here in Ukrainian (any language works the same way): "клієнт хоче щоб за посиланням люди одразу потрапляли в команду без підтвердження тренера, але тоді будь-хто з посиланням побачить розклад і контакти команди, спитати чи він впевнений, можна запропонувати щоб тренер підтверджував тільки тих, хто ще не в клубі".

(In English: the client wants people who open the link to join the team straight away, without the coach's approval, but then anyone with the link would see the team's schedule and contacts. Ask whether he is sure, and suggest the coach approves only people who are not in the club yet.)

Draft for a client, in Slack (the product, Pebble, and the name are invented):

> Hi Tom, hope you're doing well!
>
> I've been thinking about your idea of letting people join a team straight from the invite link, without the coach approving them. I can see why it appeals, it makes joining feel instant and saves the coach a lot of tapping.
>
> The one thing that worries me a little is who else might get in. Links get forwarded, and anyone who has it would see the team's training times, places and the members' contact details straight away. For a club, that could feel unsafe.
>
> One middle way could be to keep it instant for people who are already members of the club, and ask the coach to approve only someone new to the club. Joining stays quick for most people, and the team keeps its peace of mind.
>
> What do you think? Would that work for you, or is there a case I'm missing?
