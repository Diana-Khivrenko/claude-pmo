# Sub-task (one platform)

What a developer builds and QA tests on one platform. It must be complete for that platform: the developer should not need to read the sibling sub-tasks.

Section guidance:

- **Link block**, as on the Feature: **Design** first (the developer looks for screens first), then **Use cases** with the Reference sections or string keys, then **Builds on** when it applies. For a backend sub-task the Design line is left out.
- **Specification:** numbered parts, one per screen, state or behaviour, each a short list of bullets. Describe what the person sees and can do, every state the use case names (empty, loading where it matters, error, the alternative paths), who sees what, and what happens after each action. Quote UI strings exactly from the Reference in double quotes. For backend, describe the behaviour the platform must guarantee (who may do what, what is returned, what is refused and how), not the implementation.
- **Acceptance Criteria:** checkable statements, one observable outcome each. Always include:
  - the platform sizes or breakpoints from the design match it (front end),
  - "Every string matches <Reference page>, and no button carries a name" (front end),
  - the accessibility criterion at the profile's level, unless the area is excluded: contrast, keyboard order, names and states read by a screen reader, focus when something opens and closes, announcements for toasts and errors, behaviour at enlarged text (the 200% text size belongs to app tickets when the design draws it for the phone only). Name the real elements of this screen, never a generic line: see the accessibility skill, `references/ticket-criteria.md`.

Do not add a separate Required changes section here: the specification already is the list of changes for this platform.

Output skeleton:

```
**Design:** [<design key>](<url>)
**Use cases:** [<page>, Use case <n>](<url>#<anchor>), strings on [<page>. Reference](<url>), <sections or keys>
**Builds on:** [<key>](<url>) (<what it gave>)

**Specification:**

1. <Screen, state or behaviour>

* ...

2. <Next one>

* ...

### Acceptance Criteria

* ...
```

Example: `references/examples.md`, Sub-task.
