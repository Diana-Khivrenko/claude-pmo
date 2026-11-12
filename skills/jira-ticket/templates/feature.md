# Feature

One Feature per use case. It is the parent of the platform sub-tasks and the place a reader goes to understand why the work exists. It carries no acceptance criteria: those live in the sub-tasks, where they are tested.

Section guidance:

- **Link block** first, one line each, bold label then links:
  - **Use cases:** the use case, linked with its heading anchor, plus the Reference page and the sections or string keys that matter.
  - **Design:** the design ticket, or the Figma link once the design is delivered. Leave the line out for work with no design ticket.
  - **Builds on:** earlier tickets this work extends, each with a few words saying what it gave. Leave out when nothing applies.
- **The why and the what**, at most two short paragraphs, at most 120 words, no heading above them. The first says what changes for the person using the product, in their terms. The second, when needed, says where the work lands (front end only, backend only) and what already exists that it relies on.

Output skeleton:

```
**Use cases:** [<page>, Use case <n>. <name>](<url>#<anchor>), strings on [<page>. Reference](<url>), <sections or keys>
**Design:** [<design key>](<url>)
**Builds on:** [<key>](<url>) (<what it gave>)

<What changes for the person, in plain words.>

<Where the work lands and what it relies on, when needed.>
```

Example: `references/examples.md`, Feature.
