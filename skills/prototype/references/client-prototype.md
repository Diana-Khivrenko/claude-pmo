# The client prototype

A page the client opens from one link, on a laptop, and taps through like the real app. It explains itself, so nobody has to present it in a meeting.

## Page layout

Two columns on a desktop, stacked on a narrow screen:

- **The phone:** a device frame at the app size from the profile (for example 390 wide), with the status bar (9:41, signal, wifi, battery), the real app header and bottom navigation, and the home indicator. Everything inside is clickable and changes state like the real app: navigation, sheets, toasts, counters, ticks.
- **The side panel:**
  - an eyebrow line in small capitals: `PRODUCT · MODULE · CLICKABLE PROTOTYPE`,
  - a plain title saying what the client will try ("Getting a new team started", "Try every booking scenario on the phone"),
  - one or two sentences on what the feature does, from the person's side,
  - **How to try it:** one line ("Pick a scenario, then follow the steps on the phone"),
  - **the persona:** "You are Sam Carter. Alex Kim is a teammate with a match on Fri, Nov 20." with invented names,
  - **the scenarios** (see below),
  - at the bottom, the fixed date: "Today in the prototype: Tue, Nov 10", and **Restart scenario**.

When the feature is web only or differs a lot on web, use a browser frame instead of the phone, or offer both with a switch.

## Scenarios

Five to ten scenarios, numbered, each a card or a chip:

- **A title** in the person's words ("Book a training slot", "The match was cancelled"),
- **one line** on what it shows,
- **Try this:** numbered steps, each one action on the phone, naming the button exactly as the phone shows it,
- **What to look for:** two or three bullets on what should happen and what to notice,
- **Start** (or "Try it on the phone"): loads the scenario's own starting state into the phone, so scenarios can be run in any order. The running scenario is marked.

Cover the main journey first, then the alternative paths the client cares about: the empty state, the first visit, a limit, an error the person can recover from, what other people see.

For flows built from choices (a form with options), scenarios can be **presets** shown as chips: each loads a ready example into the phone, and the side panel explains, for the screen on the phone, what each choice does and "What will happen" in one plain sentence.

## Writing for the client

- Plain, warm, short. No internal words: not "use case", "state", "frame", "API", "backend", "ticket".
- Explain why, not how: "so nobody books the same court twice".
- Never put an open question or an undecided option into the prototype. If something is not decided, leave it out and tell the manager.

## Build

- One self-contained HTML page: CSS and JavaScript inline, images and the logo as embedded files, nothing loaded from elsewhere except fonts the design system allows. The client must be able to open it anywhere.
- Keep the app state in one JavaScript object per scenario (the starting state), and render the phone from that state, so Start resets cleanly and every scenario is reproducible.
- The persona, the people and the fixed date are defined once and used everywhere.

## Before sending

Run every scenario in a headless browser from Start to the last step, click each step, take a screenshot at the end, and compare with "What to look for". Fix every scenario that does not end where it says. Then publish and give the manager the link, with one line per scenario on what it shows.
