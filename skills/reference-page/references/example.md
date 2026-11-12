# Example: Pebble, Teams. Reference

An invented page for an invented product, Pebble, an app for local sports clubs, shortened to two sections. It shows the shape, not content to reuse.

What to notice:

- The intro maps each section to the use case that defines its behaviour.
- "How to read this page" explains the brackets, the placeholders and the order of the variants once, so the entries stay short.
- Keys go from general to specific and never change.
- Variants by kind of club are separated by " · " in a fixed order, with "…" for the repeated part.
- "Where it appears" carries the condition ("unavailable until a member is ticked"), the accessible name of icon controls, and who sees it. No frame ids, no Figma.
- Toasts come in singular and plural entries.

```html
<p>Every string of putting club members onto teams. Behavior lives on <a href="…/Teams">Teams</a>: Use case 1 for sections 1 and 2, Use case 2 for section 3, Use case 6 for section 5.</p>
<p><strong>How to read this page.</strong> Every string below is shared, so one entry serves web and the app. Square brackets mark a value the interface fills in. Where a string depends on the kind of club, the entry gives the three forms in the order Sports club, Rowing club, Something else. [team] marks the name of one team, [club] the name of the club and [first name] the first name of a member.</p>
[Table of Contents macro, first level only]

<h1>3. Add a player</h1>
<table><thead><tr><th><p>Key</p></th><th><p>Text</p></th><th><p>Where it appears</p></th></tr></thead><tbody>
<tr><td><p><code>players.add.title</code></p></td><td><p>Who joins [team]?</p></td><td><p>The title of the sheet, a dialog on web</p></td></tr>
<tr><td><p><code>players.add.lead</code></p></td><td><p>Choose from the members of [club]. The team’s coaches and the club’s admins see who is on the team. · … the crew’s coaches … · … the group’s leaders …</p></td><td><p>Beneath the title</p></td></tr>
<tr><td><p><code>players.add.confirm</code></p></td><td><p>Add to the team · Add to the crew · Add to the group</p></td><td><p>The primary action, unavailable until a member is ticked</p></td></tr>
<tr><td><p><code>players.add.notNow</code></p></td><td><p>Not now</p></td><td><p>The dismissal. On web the dialog also carries Close, an icon control with no visible label, which does the same</p></td></tr>
<tr><td><p><code>players.added.toast.one</code></p></td><td><p>[first name] joined [team]</p></td><td><p>The toast after adding one member</p></td></tr>
<tr><td><p><code>players.added.toast.many</code></p></td><td><p>[n] players joined [team]</p></td><td><p>The toast after adding more than one member</p></td></tr>
</tbody></table>

<h1>5. The team’s Members</h1>
<table><thead><tr><th><p>Key</p></th><th><p>Text</p></th><th><p>Where it appears</p></th></tr></thead><tbody>
<tr><td><p><code>team.members.add</code></p></td><td><p>Add a player</p></td><td><p>The action in the team’s Members, at the end of the row with the chips Players and Coaches, or alone in that row while the team has no players. Shown only to a coach of the team while a club member can still be added. It opens Add a player, section 3, with this team already chosen</p></td></tr>
<tr><td><p><code>team.members.since</code></p></td><td><p>On the team since [month] [year]</p></td><td><p>Beneath each player’s name in the list</p></td></tr>
</tbody></table>
```
