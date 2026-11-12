# Design ticket

For the designer. Lives in the design project from the profile, has no parent, and blocks the dev sub-tasks that need it.

Section guidance:

- **Opening**, one or two sentences, no heading: the problem for the person using the product and what the design adds.
- **Use cases** and **Strings**: links to the use case and the Reference page, with the sections or keys. The designer draws the exact strings from the Reference, never invents copy.
- **Sketch**, when there is one: a link to the prototype or canvas and which frames it covers, and where in the Figma file the new frames belong.
- **Platforms:** which platforms and sizes are drawn (for example the app at 390 and web at 1440, tablet and mobile web), and whether the functionality is the same on all of them.
- **Required changes:** one bullet per screen or state, bold name then what it shows. Every state the use case names, including empty and error states.
- **Acceptance Criteria:** all listed states drawn at all listed sizes, every string matches the Reference, no button carries a name.

Output skeleton:

```
<The problem and what the design adds.>

**Use cases:** [<page>](<url>), Use case <n>. **Strings:** [<page>. Reference](<url>), <sections or keys>

**Sketch:** [<name>](<url>), frames <...>. It is drawn on <page> of the <name> Figma file.

**Platforms:** <platforms and sizes>, <same functionality or the differences>.

### Required changes

* **<Screen or state>:** ...

### Acceptance Criteria

* The states above are drawn <platforms and sizes>
* Every string matches <page>. Reference
* No button carries a name
```

Example: `references/examples.md`, Design ticket.
