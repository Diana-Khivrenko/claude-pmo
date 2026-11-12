# Examples

Invented tickets for an invented product, Pebble, an app for local sports clubs. All four belong to one use case (Teams, Use case 6), so the Feature, its web sub-task and its design ticket can be read together. They show the shape, not content to reuse. The keys (PEB, DES) and links are placeholders.

## Feature

Title: `Teams: Add a player from the team's Members`
Parent: the Teams epic. Status: To Do. No assignee needed on a Feature.

```
**Use cases:** [Teams, Use case 6. Add a player from the team's Members](https://<site>/wiki/spaces/PEB/pages/<id>/Teams#Use-case-6), strings on [Teams. Reference](https://<site>/wiki/spaces/PEB/pages/<id>/Teams.+Reference), section 5 (team.members.add) and section 3
**Design:** [DES-41](https://<site>/browse/DES-41)
**Builds on:** [PEB-310](https://<site>/browse/PEB-310) (the team's Members) and the Add a player screen of Use case 2

A coach who opens a team first to look at it no longer has to go back to the club's settings to add a player. The team's Members carries Add a player for a coach of that team, at the end of the row with the Players and Coaches chips, or alone in that row while the team has no players. It opens the existing Add a player screen with this team already chosen, and adding returns to the team's Members with Players selected and the toast naming the player and the team.

The work is on the front end only: the platform already lists the club's members with whether each is on the team, and adds them, as Add a player from the club's settings does today.
```

Why it is good: the links come first, the prose says what changes for the coach in their words, the second paragraph tells the team where the work lands, and there is nothing a developer would build from (that is in the sub-tasks).

## Sub-task

Title: `[Web] Teams: Add a player from the team's Members`
Parent: the Feature above. Status: To Do. Assignee: the web developer of Teams. Linked "is blocked by" DES-41 and flagged until the design is delivered.

```
**Design:** [DES-41](https://<site>/browse/DES-41)
**Use cases:** [Teams, Use case 6](https://<site>/wiki/spaces/PEB/pages/<id>/Teams#Use-case-6), with Use case 2 for the Add a player page, strings on [Teams. Reference](https://<site>/wiki/spaces/PEB/pages/<id>/Teams.+Reference), section 5 (`team.members.add`) and section 3
**Builds on:** [PEB-310](https://<site>/browse/PEB-310) (the team's Members) and the Add a player page opened from the club's settings

**Specification:**

1. Add a player on the team's Members, web at 1440 and tablet

* The team's Members carries "Add a player", a Secondary Small button with a plus, at the end of the row with the chips "Players · [n]" and "Coaches · [n]", whichever chip is selected
* While the team has no players, Members has no chips, as PEB-310 defines, and "Add a player" stands alone in that row, above the coaches
* The button shows only to a coach of the team while at least one club member is not on it yet. It is gone once every club member is on the team, and shows again when a new member joins the club
* A player of the team and a club admin who does not coach this team do not see it

2. Add a player opened from the team

* "Add a player" opens the existing Add a player page with this team already chosen
* Everything else on the page is as when it is opened from the club's settings: the club's members in alphabetical order, a member already on the chosen team shown checked and not selectable, and "Add to the team" unavailable until a member is ticked
* The back control returns to the team's Members and adds nobody
* "Add to the team" adds every ticked member at once, returns to the team's Members with Players selected and shows the toast "[first name] joined [team]", or "[n] players joined [team]" for more than one
* If another coach adds the same member while the page is open, adding still succeeds and the member is on the team once

### Acceptance Criteria

* Add a player shows beside the Players and Coaches chips, and alone in that row while the team has no players
* It shows only to a coach of the team, and only while a club member can still be added
* It opens Add a player with this team chosen, and the back control returns to the team's Members
* Adding returns to the team's Members with Players selected and shows the toast naming the player and the team, or the number of players
* Web at 1440 and tablet match the design of DES-41
* Every string matches Teams. Reference, and no button carries a name
* Accessibility: contrast meets WCAG 2.1 AA, Add a player is a real button reached by keyboard in visual order after the chips, focus moves to the Add a player page when it opens and returns to the Add a player button after back, the toast is announced, and the row holds at 200% zoom
```

Why it is good: the design comes first, every state and every person who does or does not see the button is named, strings are quoted exactly, the race with another coach is covered, and accessibility is concrete for this screen rather than a generic line.

## Design ticket

Title: `[Design] Teams - Add a player from the team Members (Web and App)`
Project: the design project, no parent. Status: the profile's status for new design tickets. Assignee: the designer. Blocks the web and app sub-tasks.

```
A coach who opens a team first to look at it has to go back to the club's settings to add a player. The team Members gets its own Add a player action, which opens the existing Add a player screen with this team already chosen.

**Use cases:** [Teams](https://<site>/wiki/spaces/PEB/pages/<id>/Teams), Use case 6. **Strings:** [Teams. Reference](https://<site>/wiki/spaces/PEB/pages/<id>/Teams.+Reference), team.members.add and section 3

**Sketch:** [Add a player from the team Members](<canvas link>), frames W1 to W4 and A1 to A4.

**Platforms:** drawn in the app at 390 and on web at 1440, tablet and mobile web, the same functionality on both.

### Required changes

* **Team Members, Players selected:** Add a player, a Secondary Small button with a plus, at the end of the row with the Players and Coaches chips
* **Team Members, no players yet:** no chips, Add a player alone in that row, above the coaches
* **Add a player opened from the team:** the existing Add a player screen with this team already chosen. Back on web and the close control in the app return to the team Members
* **Back on Members after adding:** Players selected, the new player in the list, and the toast [first name] joined [team]

### Acceptance Criteria

* The four states above are drawn in the app at 390 and on web at 1440, tablet and mobile web
* Every string matches Teams. Reference
* No button carries a name
```

## Bug

An invented report written to the standard, to show the shape with a Cause.

Title: `[Web] Chat: The conversation jumps back down while scrolling up past shared cards that have not loaded yet`
Parent: the ticket whose change introduced it. Status: To Do. Assignee: the web developer of Chat. QA Assignee: the Chat QA owner.

```
### Preconditions

1. Two accounts, user R and user A, with a one to one chat between them
2. User R has shared 10 or more match results and training sessions into that chat
3. Web, staging build

### Steps to reproduce

1. As user A on web, open the chat by its address and wait until it settles at the last message
2. Scroll up with the mouse wheel past cards that have not been on screen yet

### Actual result

After each scroll up, the history moves back down by itself in 1 to 4 steps within about a quarter of a second, by 56 to 282 px in total for a 500 px wheel step. Each jump comes right after a shared card grows from its placeholder height to its loaded height. The content under the cursor moves.

### Expected result

Scrolling up moves the history only by the wheel distance, and a card that loads above or inside the view does not shift the messages being read. No written requirement covers scroll stability: the expectation is the behaviour of the same history in a chat where the cards do not change height, which gives no correction at all.

### Cause

Chat history is virtualized, so a row mounts only when it scrolls into view, and a shared card first renders as a placeholder about 148 px high. When the card loads it grows by 24 to 56 px, and because the history is anchored to the end, the list virtualizer answers each growth with a programmatic scroll back down ([src/chat/HistoryList.tsx](<code host link>)). The app is not affected.
```

Why it is good: preconditions name the data needed, steps have an actor, the actual result is measured, the expected result says honestly what it is based on, and the cause points the developer to the mechanism without prescribing the fix.
