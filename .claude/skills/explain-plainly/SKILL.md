---
name: explain-plainly
description: >-
  Explain something for a non-technical reader, defining every jargon term in
  plain words as you go. Use this skill whenever the user asks for a "no-jargon
  version", to "explain in plain English / plainly / simply", "ELI5", "in simple
  terms", "what does this actually mean", "break it down for me", "dumb it down",
  "I'm not technical", or otherwise signals they're confused by technical content
  and want it demystified — even if they don't use those exact words. It applies
  to anything: a checklist/doc section, a settings screen, a concept, an error
  message, or a piece of code. Trigger it even when the user just pastes
  something technical and asks "what is this?" in a way that implies they want it
  made simple.
---

# Explain Plainly

The goal: make someone who is **not** technical genuinely understand. Success is the reader thinking "oh, *that's* all it is" — not nodding along to words they didn't follow. Assume they're smart but unfamiliar with the vocabulary, so the work is translation, not dumbing down.

## The recipe

Apply these every time. They're the difference between a real explanation and a wall of jargon.

1. **Define every jargon term inline, the moment it appears.** Put the plain meaning right after the term, usually in parentheses. Don't assume *any* technical word is known — "SMTP", "index", "cache", "DNS", "API", "boolean" all get a quick plain gloss. If you wouldn't say it to a friend over coffee without explaining, explain it.

2. **Short sentences. Plain words. Analogies.** Prefer everyday words over precise-but-opaque ones. A good analogy ("SMTP is like the postal service, but for email") does more than a paragraph of accuracy. Reach for one whenever a concept is abstract.

3. **Always answer "what do I actually do?"** People don't just want to understand — they want to know the concrete steps to take. Give the click-by-click or do-this-then-that actions. If something is automatic after setup, say so explicitly.

4. **Then answer "how does it run after?"** Explain what happens day-to-day once it's in place, so they have a working mental model, not just a definition.

5. **Finish with "how it all fits together."** A few sentences tying the pieces into one picture. This is what makes it *click* and stick.

## Calibrate to the reader

Watch for cues about how non-technical they are and adjust. Default to assuming little technical background — it's far better to over-explain a term than to lose them. If they clearly know a term, don't belabor it. Never be condescending; explaining a word is a courtesy, not a comment on their intelligence.

## Format

Use light structure that's easy to scan: a short plain-English summary up top ("big picture first"), then the pieces, then the "fits together" close. Headings and short bullets help; dense paragraphs don't. Keep it warm and conversational — you're a knowledgeable friend, not a manual.

When explaining a multi-item thing (like a checklist section with several steps), go item by item, and for each give: what it means, what to actually do, and why it matters.

## Example (shape, not a script)

> **Big picture:** this section just turns on the outside services your live site needs.
>
> **SMTP** stands for "Simple Mail Transfer Protocol" — the technical name for **the system that delivers email**, like the postal service but for messages. Your site needs it because, on its own, WordPress's emails often get treated as junk and never arrive…
>
> **What you actually do:** install the plugin → sign up with a sending service → paste the code it gives you → send a test.
>
> **How it runs after:** from then on it's automatic — whenever the site emails someone, it quietly hands the message to that service, which delivers it reliably.
>
> **How it fits together:** this is the "make email actually work" step; the next two are spam protection and a photo tool.

## What to avoid

- Don't leave any acronym or technical noun unglossed.
- Don't hedge into precision the reader can't use ("it depends on the MX records' TTL propagation") — give the useful version.
- Don't just define things; always include the *do this* and the *here's how it works* parts.
