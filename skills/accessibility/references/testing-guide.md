# Template: Accessibility testing guide

A generic template. Replace the values in square brackets with the profile's. Drop the platform sections the project does not have. Keep the house style (no long dashes in the tables either).

---

Web, iOS and Android. The QA reference for accessibility testing. All tests target WCAG 2.1 level [AA], Apple's Human Interface Guidelines for accessibility and Android accessibility practice.

**In scope:** every new feature before merge, a full regression on each release candidate, and the critical flows: sign-in, main navigation, reading content, forms and error states.

**Out of scope:** AAA criteria (best effort) and third-party embedded widgets.

## 1. Severity

Use these levels when filing accessibility bugs, and name the WCAG criterion and the platform in the ticket.

| Severity | Meaning | Fix by |
|---|---|---|
| Critical | Blocks access completely for people with disabilities | Before release |
| High | Seriously impairs use, a workaround exists | Next release |
| Medium | Friction or confusion, a partial failure | Planned |
| Low | Minor deviation or best-practice improvement | Backlog |

## 2. Tools

Automated tools first, then manual screen reader and motor testing. Automated tools find roughly a third of real issues.

| Tool | Platform | What it checks |
|---|---|---|
| axe DevTools | Web | Automated WCAG audit of a page |
| Lighthouse | Web | Accessibility score, contrast, labels |
| NVDA with Chrome | Web, Windows | Keyboard, ARIA, live regions |
| VoiceOver with Safari | Web, Mac | Screen reader on web |
| VoiceOver | iOS | Swipe navigation, rotor, custom actions |
| Switch Control | iOS | The whole app without touch |
| Display and Text Size | iOS | Dynamic Type, Bold Text, Reduce Motion |
| TalkBack | Android | Explore by touch, linear navigation |
| Accessibility Scanner | Android | Touch target size, labels |
| Switch Access | Android | Sequential and directional scanning |
| Colour Contrast Analyser | All | Manual contrast of brand colours |

Always test VoiceOver and TalkBack on a physical device: simulators do not reproduce them faithfully.

## 3. Web checklist

Screen readers: NVDA with Chrome, VoiceOver with Safari. Keyboard only in Chrome, Firefox, Safari and Edge.

**Perceivable:** images have descriptive `alt` or empty `alt` when decorative (1.1.1), video has captions (1.2.2), colour is not the only signal (1.4.1), text contrast 4.5:1 and large text 3:1 (1.4.3), controls and graphics 3:1 (1.4.11), reflow without horizontal scroll at 400% (1.4.10), text spacing overrides do not break layout (1.4.12), nothing flashes more than three times a second (2.3.1).

**Operable:** everything reachable by Tab (2.1.1), no keyboard trap (2.1.2), visible focus (2.4.7), a working skip link (2.4.1), a descriptive page title (2.4.2), logical focus order (2.4.3), clear link purpose (2.4.4), session timeouts warn and allow extension (2.2.1), moving content can be paused (2.2.2).

**Understandable:** page `lang` set (3.1.1), language changes marked (3.1.2), errors name the field and the problem (3.3.1), required fields labelled before submitting (3.3.2), suggestions given where possible (3.3.3), consistent navigation (3.2.3), no change of context on focus (3.2.1).

**Robust:** every input has a label and custom components have correct roles and states (4.1.2), dynamic changes announced through live regions (4.1.3), dialogs keep and return focus (2.4.3), axe reports no critical or serious violations, Lighthouse score at least 90.

## 4. iOS checklist

VoiceOver: every element has a meaningful label, decorative images are hidden, grouped elements read as one where appropriate, reading order matches the visual order, custom controls have the right traits, tab bars announce the name, position ("2 of 5") and badge, alerts and sheets take focus when shown, the rotor offers headings, links and form controls.

Dynamic Type and display: text scales up to the largest accessibility size, layout does not break or truncate, Bold Text, Reduce Motion, Increase Contrast, Smart Invert and Dark Mode are respected.

Touch and motor: targets at least 44 × 44 pt with 8 pt between them, custom gestures have a tap alternative (2.5.1), Switch Control and AssistiveTouch can complete every critical flow.

Forms: fields announce their label, the keyboard matches the field (email, phone), the return key fits (Next, Done), inline errors are announced, pickers work with VoiceOver.

## 5. Android checklist

TalkBack: every interactive element has a content description or text, decorative images have an empty one, reading order is logical, custom views expose correct node info, tabs and bottom navigation announce name and position, dialogs and bottom sheets take focus, live regions announce changes, headings are marked.

Font and display: text scales to 200% (sp units), nothing clips at the largest size, the largest display size does not break layout, high contrast text and removed animations are respected.

Touch and motor: targets at least 48 × 48 dp with 8 dp between them, custom gestures have a tap alternative, Switch Access reaches every screen.

Forms: fields have a label or hint read by TalkBack, the input type matches the field, errors are announced without moving focus, Accessibility Scanner reports no critical issue, spinners and date pickers work with TalkBack.

## 6. Critical flows, every platform, with a screen reader before each release

Register, sign in (including the error state), move between the main tabs, read a feed item, complete and submit a form, sign out, change a setting, error and empty states, loading states.

## 7. Bug template

```
Title: [Platform] <what is wrong, where, when>

Preconditions:
1. [VoiceOver on iOS / TalkBack on Android / keyboard only on web / largest text size / dark theme]
2. [Account and data needed]

Steps to reproduce:
1. Go to [screen]
2. [Action]

Actual result: [what happens]
Expected result: [what should happen], WCAG [number and name]
```

## 8. Release sign-off

A release is blocked while any of these is true: a Critical accessibility bug is open, a High bug is open in a critical flow, axe reports a critical or serious violation on a key web page, Lighthouse is under 90 on a key web page, Accessibility Scanner reports a critical item on a key Android screen, the VoiceOver or TalkBack end-to-end flows are not signed off, keyboard-only navigation fails on web. Medium bugs must be triaged and planned.
