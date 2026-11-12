# Bug Sub-Task

A defect found in testing, or behaviour that contradicts the use case or the Reference. Filed first of all as a Bug Sub-Task under the Feature whose behaviour it breaks, linked "relates to" the platform sub-task it breaks. When no Feature fits, a standalone Bug is fine (see Hierarchy in SKILL.md). One defect per ticket: two defects are fixed and verified separately.

Title: tag first, then `<Module>: <what is wrong> <where> <when>`. Concise, understandable without opening the ticket, never "does not work" or "issue" without saying what.

Section guidance:

- **Preconditions**, numbered: the concrete state needed, not "a user exists". Which account, which role, what data (a team with one coach, a chat with ten shared cards), which environment and build, which feature flag.
- **Steps to reproduce**, numbered: one action per step, by a named actor ("as the guest", "as user A on web"), executable without reading code.
- **Actual result:** what happens, factually. The exact wrong text, the wrong state, the measured value. A screenshot or recording when there is one.
- **Expected result:** what should happen instead, **quoted from the source**: the use case sentence or the Reference string, linked. When no written requirement covers it, say so in one line and state what the expectation is based on (the same screen elsewhere, the behaviour before a change).
- **Accessibility bugs:** Preconditions name the assistive technology and setting (VoiceOver on iOS, TalkBack, keyboard only on web, largest text size, dark theme), and the Expected result names the WCAG criterion by number and name.
- **Cause**, only when it was found: where in the code the defect happens and why, in two or three sentences, with the file linked on the code host (plain path as the link text, no backticks inside the link). Never the fix, never a long technical write-up: the developer starts from the cause, the solution is theirs. The bug-cause skill finds it.

Not in a bug: dates, build numbers in prose (they go in Preconditions as the environment), severity essays, local file paths, QA status lines, acceptance criteria lists (the Expected result is the criterion).

Output skeleton:

```
### Preconditions

1. ...

### Steps to reproduce

1. ...

### Actual result

...

### Expected result

...

### Cause

...
```

Example: `references/examples.md`, Bug.
