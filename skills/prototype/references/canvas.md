# The canvas (for the team)

The canvas is the designer's starting point and the developers' first look at the feature. It shows every state the use case describes, on every platform, with the logic written under each frame.

## Layout

- One canvas per use case page area, with a small frame budget: about 12 frames per canvas. A plan of 30 or more frames in one run loses its tail. Split by flow instead ("Create", "Read and reply", "Manage") and build them one after the other.
- Frames side by side in the order a person meets them, the app row and the web row separated:
  - app frames named `A1`, `A2`, …, at the app size from the profile (for example 390 wide),
  - web frames named `W1`, `W2`, …, at the web size (for example 1440 wide), plus tablet and mobile web when the profile lists them and the layout differs.
- Above the frames, a short header: the module, the use case numbers covered, and the source of the visual language.

## Under every frame, a note

Two to four short lines in a muted style:

- what state this is and how the person got here,
- what each action on the frame does and where it leads (frame id),
- the rule that decides what is shown (who sees it, the limit, the condition).

The notes are for designers and developers. They never go into the use case page, and frame ids never appear in Confluence.

## What a canvas must make clear

These are the three depths a single card spec lacks, and without them the output is not ready for development:

1. **State matrix:** every state of every screen, including empty, loading where visible, error, limits reached, and the variants by role.
2. **Flow and navigation:** where each action leads, what Back and Close do, what happens after success (toast, landing screen).
3. **Layout and responsive rules:** what moves, wraps or collapses between app and web, and at enlarged text when the design draws it.

## Reuse

Draw the new screens on top of what exists: copy the real header, navigation and cards of the neighbouring screens from the design system or the Figma file, so only the new parts are new.

## Hand-off

The canvas link goes into the design ticket as the Sketch line, with the frame ids it covers and where in the Figma file the designer should place the new frames (jira-ticket skill, design template).
