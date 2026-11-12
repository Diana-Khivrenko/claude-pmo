# Example: Pebble, Authentication, Use case 1

An invented page for an invented product, Pebble, an app for local sports clubs, written in the house format and shortened. It shows the shape, not content to reuse.

What to notice:

- The intro says what lives here and links to where everything else lives, including what is postponed.
- The role sits in the info panel, the three path headings are underlined h3, User Stories is a plain h3.
- Basic Path is prose in the order things happen, with "should", strings quoted exactly, and the web and tablet differences in their own paragraph.
- Alternative Path is one "If" per case, including the privacy case (identical behaviour for known and unknown addresses), the failure to send, wrong code, too many tries, expiry, rate limit and going back.
- Every Acceptance Criteria bullet is something QA can check.
- No frame ids, no Figma links, no design tickets, no questions, no dates.

```html
<p>Signing up and signing in live on this page, as one flow. There is one way into Pebble, a code sent to an email address, and it is the same whether the person already has an account or not.</p>
<p>The profile lives on <a href="…/Profile">Profile</a>. Every string lives once on <a href="…/Authentication.+Reference">Authentication. Reference</a>. Sign-in with other providers is out of the current scope and lives on <a href="…/Authentication.+Postponed">Authentication. Postponed</a>.</p>
[Table of Contents macro]

<h1>Use case 1. Sign in or sign up with an email code</h1>
<div data-type="panel-info"><p>Role - User</p></div>

<h3><u>Preconditions</u></h3>
<ul><li><p>The user should be able to reach the inbox of the email address they enter</p></li></ul>

<h3><u>Basic Path</u></h3>
<p>When the user opens Pebble, they should be presented with the Continue screen. It shows the Pebble logo, the heading “Welcome to Pebble”, the line “Everything your club needs, in one place”, a single “Email” field, a “Continue” button, the language switcher, and the footer with the legal links and the help link. There should be no password field anywhere in the product.</p>
<p>On web and on the tablet the same card sits centred on the page. The language switcher moves onto the page, top right and outside the card, and the help link sits inside the card under “Continue”.</p>
<p>Signing up and signing in should be the same flow, on the same screen, with the same steps. The user should not have to know in advance whether they already have an account, and Pebble should not ask.</p>
<p>When the user enters an email address and taps “Continue”, Pebble should send a 6-digit code to that email address and open the Enter the code screen. While the code is being sent the Email field and “Continue” should be disabled, so the same address cannot be submitted twice.</p>
<p>A correct code should confirm the email address and prove that it belongs to the user, so there should be no separate confirmation email and no unconfirmed state anywhere in the product.</p>
<p>After a correct code the two cases diverge, and only there. An email address that already has an account should be signed straight in and land on Home. An email address with no account should be taken to the Last step screen, see Use case 2.</p>

<h3><u>Alternative Path</u></h3>
<p>The Continue screen should behave identically for an email address that has an account and one that does not, so it cannot be used to find out who is on Pebble. Both send a code, with identical screens, identical strings and indistinguishable response times.</p>
<p>If the email address is not a valid email format, “Continue” should stay disabled.</p>
<p>If the code could not be sent at all, the Enter the code screen should still open, with its six boxes empty, the line “The code was not sent. Pebble could not be reached” and the action “Send a code again”.</p>
<p>If the code is wrong, the screen should show “That code is not right. Check it and try again.” and let the user try again.</p>
<p>After five wrong attempts the code should be retired, and the screen should show “Too many tries. We can send you a new code.” A retired code should stop working even if the correct one is entered afterwards.</p>
<p>If the code has expired, the screen should show “This code has expired. We can send you a new one.” with a one-tap resend.</p>
<p>Resending should be rate limited to one code per email address per 60 seconds, with the remaining time shown on the action.</p>

<h3>User Stories</h3>
<ol><li><p>As a user, I want one way in that works whether I have an account or not, so that I never have to know which door is mine.</p></li></ol>
<p><strong>Acceptance Criteria</strong></p>
<ul>
<li><p>The Continue screen holds one Email field, a “Continue” button and the language switcher, and no password field</p></li>
<li><p>Signing up and signing in run the same steps, and the flows diverge only after a correct code</p></li>
<li><p>An email address that has an account and one that does not produce identical screens, identical strings and indistinguishable response times</p></li>
<li><p>“Continue” stays disabled until the email address is a valid email format</p></li>
</ul>
<ol start="2"><li><p>As a user, I want a code in my inbox instead of a password, so that there is nothing to invent or remember.</p></li></ol>
<p><strong>Acceptance Criteria</strong></p>
<ul>
<li><p>Tapping “Continue” sends a 6-digit code to the address and opens the Enter the code screen</p></li>
<li><p>After five wrong attempts the code is retired, the screen shows “Too many tries. We can send you a new code.”, and a new code can be requested from the same screen</p></li>
<li><p>Codes are rate limited to one per email address per 60 seconds</p></li>
</ul>
```
