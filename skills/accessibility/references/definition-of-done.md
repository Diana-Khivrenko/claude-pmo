# Template: Accessibility Definition of Done

A generic template. Replace the values in square brackets with the project profile's: platforms, themes, languages, level. Keep the house style.

---

This Definition of Done applies to every front end and design task. A task is only done when the relevant items below are satisfied for the surfaces it touches.

## Scope

- Applies to [web and the mobile app], in [light and dark themes], and across [all product languages: …]
- Applies to every new or modified screen, component, dialog, bottom sheet, banner and widget
- Does not apply to [excepted areas, for example the internal admin panel]

## 1. Text alternatives for non-text content (WCAG 1.1.1 A)

**What to do:** every image, icon and control that conveys meaning exposes a text alternative, and purely decorative visuals are hidden from assistive technology.

**How:**

- Web: every image has a meaningful `alt`, following the project's conventions, for example: user avatars "[User name]'s profile picture", group or organisation logos "[Name] logo", content images "View photo" or "View video".
- Decorative images: empty `alt=""` on web, hidden from accessibility on the app.
- App: accessible labels on every interactive icon (settings, close, back, options, add, skip).
- Badges and status pills expose meaningful labels, never empty or duplicate ones.
- Remove redundant or empty labels that make the screen reader announce nothing or the same thing twice.

**Done when:** no meaningful image, icon or control is unlabelled, and no decorative element is announced.

## 2. Name, role and value of custom components (WCAG 4.1.2 A)

**What to do:** every custom control exposes what it is, its current state and its value.

**How:**

- Web: native elements first. Custom ones get the correct ARIA: `role="switch"` with `aria-checked`, `role="radio"` with `aria-checked`, `aria-expanded` on expandable parts, `aria-pressed` on toggled buttons, `aria-label` or `aria-labelledby` where there is no visible label.
- Never `aria-label` on a `div` without a valid role, never `aria-hidden` on something focusable, never an interactive element inside another.
- iOS: `accessibilityTraits` (button, link, selected) and a correct `accessibilityValue`.
- Android: the role through `AccessibilityNodeInfo` (Views) or `Modifier.semantics { role = … }` (Compose).
- Stateful components (toggles, radios, tabs, poll options) announce their state and update it on change.

**Done when:** a screen reader announces the role, state and value of every control on the surface.

## 3. Semantic structure and relationships (WCAG 1.3.1 A)

**What to do:** structure and relationships are programmatic, not only visual.

**How:**

- Correct heading hierarchy, lists and landmarks (`nav`, `main`, `header`, `region`).
- Form fields have associated labels.
- Related controls are grouped with the right grouping semantics.

**Done when:** the accessibility tree reflects the visual structure and grouping.

## 4. Keyboard and focus on web (WCAG 2.1.1 A, 2.1.2 A, 2.4.3 A, 2.4.7 AA)

**What to do:** everything works by keyboard, nothing traps focus, focus is always visible, and its order is logical.

**How:**

- Every interactive element is reachable and operable with Tab, Shift+Tab, Enter, Space and the arrow keys as appropriate.
- Dialogs and dropdowns keep focus inside while open and **return focus to the control that opened them** on close.
- A visible focus indicator on every focusable element.
- Focus order follows the visual reading order, and never stops on hidden or decorative elements.

**Done when:** the surface can be fully used by keyboard alone, with visible focus in a logical order.

## 5. Screen reader order and focus on the app (WCAG 2.4.3 A, 4.1.3 AA)

**What to do:** VoiceOver and TalkBack reach elements in a meaningful order and do not leak into background content.

**How:**

- iOS: `accessibilityElements` in the intended order. Android: `traversalBefore` and `traversalAfter`.
- When a sheet or dialog opens, focus moves into it, the background cannot be reached, and focus returns on close.

**Done when:** swipe navigation follows a sensible order and sheets contain focus.

## 6. Status messages (WCAG 4.1.3 AA)

**What to do:** toasts, errors, loading and empty states are announced without moving focus.

**How:**

- Web: `role="status"` or `aria-live="polite"` for confirmations, `role="alert"` or `aria-live="assertive"` for errors.
- iOS: an announcement notification. Android: `announceForAccessibility` or a live region.
- Validation errors are announced and associated with the field.

**Done when:** confirmations, errors, loading and empty states are announced without focus moving.

## 7. Page title and language on web (WCAG 2.4.2 A, 3.1.1 A, 3.1.2 AA)

- Every route sets a unique, descriptive, translated title, never a translation key.
- The page `lang` follows the active language and changes with it.

**Done when:** each page has a real title and a correct `lang`.

## 8. Contrast (WCAG 1.4.3 AA, 1.4.11 AA)

- Normal text at least 4.5:1, large text at least 3:1, controls and meaningful graphics at least 3:1.
- Checked in [both themes] on every platform.
- Colour is never the only way information is shown.

**Done when:** everything on the surface passes in [both themes].

## 9. Text size, zoom and reflow (WCAG 1.4.4 AA, 1.4.10 AA)

- Web: usable at 200% zoom with no lost content and no horizontal scrolling to read a line.
- App: follows the system text size (Dynamic Type, Android font scale), containers grow with the text, and buttons, pills, cards and sheets stay readable and usable at 200%.

**Done when:** nothing clips, overlaps or stops working at 200%.

## 10. Touch targets on the app

- At least 44 × 44 pt on iOS and 48 × 48 dp on Android, with at least 8 between adjacent targets.
- Every custom gesture (swipe, long press) has a tap alternative (WCAG 2.5.1).

## Verification checklist (per task)

- [ ] Automated scan with no new violations on the touched surface (axe or Lighthouse on web, Accessibility Scanner on Android)
- [ ] Keyboard-only pass on web: reach, operate, leave, visible focus, logical order
- [ ] Screen reader pass (VoiceOver, TalkBack): labels, roles, states, order, announcements
- [ ] Contrast checked in [both themes]
- [ ] 200% zoom on web and largest text size on the app checked
- [ ] Page title and `lang` checked on web
- [ ] Checked in [all product languages], including layout with the longest strings
- [ ] The criteria are in the ticket and confirmed by QA
