# Writing the accessibility criterion of a ticket

One bullet in the Acceptance Criteria, starting with "Accessibility:", listing only what applies to this screen, with the real names of its elements. A generic line ("meets WCAG 2.1 AA") gives QA nothing to test and is not acceptable.

## How to build it

Go through the Definition of Done and keep each item that the screen actually has:

| The screen has | Write |
|---|---|
| Text and controls | "contrast meets WCAG 2.1 AA in both themes" |
| An icon control with no visible text | "<control> has the accessible name “<name from the Reference>”" |
| Images or avatars | "avatars read “[User name]'s profile picture”, decorative images are not announced" |
| A custom control (switch, radio, chip, tab, poll option) | "<control> announces its role and its selected or checked state, and the change" |
| Web, anything interactive | "<controls> are reached by keyboard in visual order, with visible focus" |
| A sheet, dialog or new page opening | "focus moves into <it> when it opens and returns to <trigger> when it closes, the background is not reachable while it is open" |
| A toast, error, loading or empty state | "<toast or error> is announced without moving focus" |
| A form | "every field has its label, errors are announced and tied to the field" |
| A new web route | "the page title is “<title>” and `lang` follows the language" |
| Text that can grow | "<row or card> holds at 200% zoom on web" or "at the largest text size on the app" |
| Touch targets on the app | "<controls> are at least 44 × 44 pt on iOS and 48 × 48 dp on Android" |
| A gesture (swipe, long press) | "<action> is also reachable without the gesture, through <alternative>" |

Platform-specific items go only into the ticket of that platform: keyboard and page title into the web sub-task, touch targets and system text size into the app sub-task. When the design draws enlarged text for the phone only, the 200% criterion belongs to the app ticket.

## Example

From the invented web sub-task in `jira-ticket/references/examples.md` (Add a player from the team's Members):

> Accessibility: contrast meets WCAG 2.1 AA, Add a player is a real button reached by keyboard in visual order after the chips, focus moves to the Add a player page when it opens and returns to the Add a player button after back, the toast is announced, and the row holds at 200% zoom

It names the button, its place in the keyboard order, where focus goes in both directions, the toast, and the one layout that could break. QA can test every clause.
