---
name: design-style
argument-hint: <a website link, screenshots, or a Figma file> <a name for the style>
description: "Build a reusable style skill for a project from a reference: a website the client likes, screenshots, or the project's Figma library, so every later canvas and prototype draws in that visual language. Studies the reference closely, writes the design rules, exact tokens, component recipes and a preview page, checks the result against the reference, and proposes the skill for saving. Use when a project has no design system in Claude, when someone says make it look like this site, build a style from this link, capture our Figma components, or when the prototype skill had to read Figma by hand more than once."
---

# Building a style skill

A prototype is only as convincing as its visual language. When a project has no design system in Claude, this skill turns a reference into a style skill that Claude follows on every later canvas and prototype, so screens stop being re-invented each time. A whole style skill can be built this way from a single website link.

## Sources

- **A website or screenshots:** open the pages in Chrome, take screenshots at desktop and phone width, and read the CSS of the elements that define the look (backgrounds, cards, buttons, inputs, type, spacing, shadows, blur, motion).
- **A Figma file or library:** read the variables (colours, type, spacing, radii), the components and their variants, and three or four finished screens with the Figma connector. The Figma values are the truth: copy them, do not approximate.
- **Both:** Figma for tokens and components, the site for atmosphere and imagery.

Ask the manager which reference is the source when there are several, and whether the logo and icons come as files (they are never generated).

## What to capture

Study the reference before writing anything. Look at the same element in several places and note what is constant:

1. **The feeling** in one or two sentences, and what would break it.
2. **Rules**, numbered, the ten or so decisions that make the style recognisable: the background, the surfaces, the radii, how many dark elements per view, where the accent colour is allowed, how loud the type is, density, dividers, imagery, motion. Each rule says why and what the most common mistake is.
3. **Exact blocks** for anything that is hard to get right by description (a layered background, a glass surface), as copy-ready HTML and CSS, tuned for the app size.
4. **Tokens** as CSS custom properties and as JSON: colours with roles, type scale, spacing, radii, shadows, blur, easing and durations.
5. **Components:** app bar, bottom navigation, buttons (primary, secondary, small, icon), inputs, chips, cards, list rows, sheets and dialogs, toasts, empty states, each with its exact styles and states.
6. **A preview page** that shows the tokens and every component on the style's own background.

## Skill layout

```
<style-name>/
  SKILL.md              the feeling, the rules, the exact blocks, when to use it
  references/tokens.css
  references/tokens.json
  references/components.md
  preview.html
```

The description says when to use it in the words people use ("in our app style", "like the client's site", the product name), so it loads on its own.

## Check before handing over

1. Render `preview.html` and two sample screens (a list and a form, at the app size) in a headless browser.
2. Put the screenshots next to the reference screenshots and compare: background, surfaces, radii, type, spacing, the accent, the primary button. Fix every difference you can name, then compare again.
3. Show the manager the side-by-side screenshots.

## Saving

Propose the style skill for saving with the skill proposal tool. Add its name to the project profile, design system row, so the prototype skill finds it. If the style should be shared with the whole organisation, it can be added to the snotor-pmo repository as its own skill folder.
