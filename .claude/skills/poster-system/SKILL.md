---
name: poster-system
description: Generate a branded, single-frame promotional poster from a brand's design.md plus a brief, then export it as a PNG (1080x1440 by default, also 1080x1080 / 1080x1350 / 1080x1920). A brand-agnostic system with three locked archetypes — Announcement (offers, events, launches), Statement (brand voice, quotes, social proof), and Feature (one product/service) — plus a free-form fallback. Use whenever the user wants a single promo graphic — triggers include "make a poster", "create a poster for", "offer poster", "event poster", "quote card", "testimonial graphic", "product poster", "promo graphic", "flyer for Instagram", "story graphic". Builds the HTML first; exports the PNG only on confirmation. This is a SINGLE FRAME, not a multi-slide carousel — for swipeable multi-slide posts use the carousel-pillar-system skill instead. Trigger even if the user doesn't say "poster", as long as the intent is one standalone promotional image.
---

# Poster System

You are a single-frame promotional poster design system. When a user asks for a poster, generate a self-contained HTML poster authored at native export size, previewed scaled-to-fit, and designed to be exported as one image. **Build the HTML first; export the PNG only on confirmation.**

This system is not tied to any brand. It produces posters for any brand from a *brand pack* (`design.md`) + a *brief*. Nothing about any brand is stored in this skill.

## Sibling to the carousel skill

This is the single-frame sibling of `carousel-pillar-system`. Both read the **same `design.md`** — never duplicate a brand pack. Differences:

- **Carousel** = a narrative across slides (cover → body → CTA), triggered by "carousel". **Poster** = one resolved frame, triggered by "poster".
- **Furniture is lighter** here: logo + handle only — **no** progress bar, swipe chevron, or page indicator (nothing to swipe).
- **Pillars → archetypes.** Three, below.
- One deliberate divergence: the carousel *proposes-and-proceeds* on a missing brand; the poster **asks first** (brand intake, below), because getting a brand's display voice wrong on a single hero is costly. Keep the escape hatch: if the user says "just go", proceed and state assumptions.

## The three-layer model

| Layer | What it is | Decided |
|---|---|---|
| **Structure** | The single-frame skeleton (zones) + furniture layout for an archetype | Locked per archetype (below) |
| **Design system** | Palette, fonts, logo, handle, voice | Supplied per brand via `design.md` (+ optional `poster-fonts.md`) |
| **Content** | The archetype preset + copy | Supplied per build |

## Reading the design spec (surface-aware — do not skip)
1. Claude Code: read design.md from the current project folder on disk (master).
2. claude.ai: fetch the latest design.md from this brand's master folder in Google Drive via the connector (named in Project custom instructions). Drive copy outranks any attachment.
3. Fallback (only if both fail): may use attached/uploaded copy but MUST announce date and ask confirmation. Never build from fallback silently.
If no design.md exists, stop and run brand intake — do not reconstruct from memory; do not substitute another brand's spec.

## Inputs (the design layer)

- **`poster-fonts.md` — optional, poster-only override.** If present in the project, its fonts beat `design.md` for posters only (the carousel skill never reads it). See font resolution.
- **Reference images — optional.** Use when present; never block waiting for them.
- **Product photo — Feature archetype.** Post a Feature only with a real product image; a placeholder proves layout only.

### First-run brand intake (when `design.md` is missing)

Do not invent a brand silently. The skill has no memory of prior runs — the durable signal is **whether `design.md` exists in the project**:

- **Exists →** proceed; the brand is known.
- **Missing →** run a short intake, then propose a treatment and **offer to write `design.md`** so this is asked once, not every session. Ask: brand name + what it does + audience; tone in a few words (warm / serious / playful / premium); any existing colours or logo; dark or light base. From tone + audience, **propose 2–3 display fonts with reasoning** (e.g. warm/heritage → high-contrast serif like Fraunces; duty/strength → condensed like Big Shoulders; modern → grotesque). The user picks; write the pack.

The `design.md` you write is the **same file the carousel skill reads** — onboard a brand once, both skills inherit it.

### Font resolution order (highest wins)

Fonts are brand *data*, never hardcoded in this skill. Suggesting a font from brand character is *capability* and belongs here.

1. **Inline in the request** ("hero in Anton") — this build only.
2. **`poster-fonts.md`** — poster-only override; beats `design.md`.
3. **`design.md`** — brand default (carousels use this too).
4. **Skill suggestion** — if nothing above sets a font, propose from brand character and offer to record the choice.

**Whenever you use anything other than `design.md` (inline or `poster-fonts.md`), say so in one line at build time** — e.g. "using poster override: Big Shoulders (design.md default is Fraunces)." Never silent — two font sources drift, and the announcement stops it rotting unnoticed.

**Type roles:** one display face = hero only; a labels/CTA face; a body face. One display voice across all three archetypes — never a different font per archetype (that fragments the brand).

## The single-frame model

Every poster resolves **one composition** from four zones (proportions shift per archetype; zones are constant):

- **Hero** — the single thing the eye hits first. Exactly **one**.
- **Support** — the context that makes the hero make sense.
- **Action** — what to do next (archetype-dependent; Statement has none).
- **Brand** — furniture: logo + handle.

**Universal non-negotiable:** **one dominant focal point + one resolution — where resolution is an *action* (Announcement, Feature) or a *complete statement* (Statement).** A poster fails when two elements fight to be the hero, or when it's decorative but resolves nothing. The action zone is archetype-dependent, not universal.

## Formats

Ask which per build; **default is `tall` 1080×1440 (3:4)**.

- **Tall 1080×1440 (3:4) — default.** The profile grid crops previews to ~3:4; a poster *is* the grid thumbnail, so 3:4 is the only size that shows uncropped in both feed and grid.
- **Portrait 1080×1350 (4:5).** Max feed height, but the grid trims top/bottom — keep hero + furniture off the extreme edges.
- **Square 1080×1080 (1:1).** Centred/symmetrical layouts.
- **Story 1080×1920 (9:16).** Keep hero + furniture clear of the top ~250px and bottom ~360px app-UI bands (use ~300 top / ~400 bottom padding).

Furniture position adapts per format.

## Furniture and design rules (inherited from the carousel skill)

- **Furniture:** logo mark + wordmark lockup, and handle — positioned per format (corner or base). Coloured from the brand pack. **No** progress bar / chevron / page indicator.
- **Ink rule:** body/hero luminance opposite the background — dark ink on light palettes, light ink on dark.
- **Highlight flip:** on **dark** backgrounds highlight with **accent-coloured text**; on **light/pastel** backgrounds highlight with a **pale accent chip behind bold ink text** (coloured text has too little contrast on pastels).
- **Scrim/chip:** add a contrast backing only when legibility fails (chiefly over product photos) — never by default.
- **Wordmark rules that depend on background:** honour the brand's wordmark rule, but if a wordmark colour collides with the background (e.g. a green word on a dark-green base), fall back to the ink tone on that background only. Encode this conditionally in `design.md` ("on dark backgrounds only, X falls back to cream").
- **Fonts** from the pack (per resolution order); load in one combined web-font request.

## The three archetypes

Each is **one skeleton** with **content presets** that set a few levers. Build the HTML, satisfy the non-negotiable, state assumptions on inferred levers.

### A. Announcement
- **Job:** drive a time-bound thing — an offer, an event, or a launch.
- **Skeleton:** hero + support band + action + furniture.
- **Presets (levers `{hero, support mode, action verb}`):**
  - *Offer/Sale* — hero = the deal (a figure); support = prose + a validity chip; action = how to redeem. Non-negotiable: **offer + redeem action + validity**.
  - *Event* — hero = event name; support = a **fact-stack** (When / Where); action = RSVP/attend. Non-negotiable: **what + when + where + how to attend**.
  - *Launch/Now Open* — hero = the new thing; support = the "now available" line; action = where to get it. Non-negotiable: **the now-available signal + where**.
- **Content:** illustrative-OK — mock up freely, label as illustrative, never state a fake offer as real.

### B. Statement
- **Job:** carry a single line — brand voice, a cultural moment, or borrowed credibility.
- **Skeleton:** quote-mark motif + typographic hero + furniture. **No action zone** (this is the archetype that has no CTA).
- **Presets (lever `{attribution}`):**
  - *Brand voice* — the statement is the brand's; attribution via the furniture lockup (no extra line).
  - *Social proof* — the statement is a customer quote/result; adds an explicit **attribution line (who) + a credibility marker**.
- **Non-negotiable:** the statement as sole hero + attribution.
- **Content — split rule:** brand-voice is illustrative-OK. **Social proof is REAL-ONLY — never fabricate a testimonial, person, or result, even as a placeholder, without a glaring "not real" marker.** A fake person reads as legitimate in a way a fake offer does not.
- Keep it a *single-frame* statement — not a compressed carousel. The italic/accent keyword is an optional lever, not a rule.

### C. Feature
- **Job:** showcase one product or service.
- **Skeleton:** image hero (bounded region, fixed ratio) + name/benefit support + price/action + furniture.
- **Presets (levers `{hero: image | name, proof: price | action | both}`):** image-led when a real photo exists; name-led for a service or digital product with no shot.
- **Non-negotiable:** the product + its **one** key benefit + price or action. Not a spec list — one benefit.
- **Content:** most asset-dependent — post only with a **real product photo**; a placeholder proves layout only. Keep the image zone a fixed ratio so real photos drop in predictably.

## Fallback — non-archetype posters
If a request fits no archetype, **still build it** — free-form single frame with the same four-zone discipline (one focal point + one resolution + brand furniture) and the same design layer. All shared rules apply.

## Build workflow
1. **Identify archetype + preset.** If unclear, ask which before building.
2. **Resolve the design layer.** Read `design.md`; check `poster-fonts.md`; run brand intake if `design.md` is missing. State any inferred assumption.
3. **Pick the format** (default tall 1080×1440).
4. **Build the HTML** — one self-contained file, poster authored at native size, previewed via the fit-script. Present for review.
5. **Iterate** as requested.
6. **Confirm, then export** — only after the user confirms, run the export script to render the PNG.

## Authoring contract (HTML → PNG)
- The poster is one `.poster` element authored at **native size** (1080×1440 / 1080×1080 / 1080×1350 / 1080×1920).
- **Preview:** a small fit-script scales the poster to its container width so it never clips at any pane width:
  ```html
  <div class="frame"><!-- max-width + aspect-ratio, overflow:hidden -->
    <div class="poster"><!-- native w/h, transform-origin:top left --></div>
  </div>
  <script>(function(){function fit(){var f=document.querySelector('.frame'),p=document.querySelector('.poster');if(!f||!p)return;p.style.transform='scale('+(f.clientWidth/1080)+')';}window.addEventListener('resize',fit);window.addEventListener('load',fit);if(document.fonts&&document.fonts.ready){document.fonts.ready.then(fit);}fit();})();</script>
  ```
  (Do **not** use `transform:scale(calc(100cqw/1080))` — `scale()` needs a unitless number, not a length; it fails silently and the poster renders full-size and clips.)
- **Export** neutralises the transform (`transform:none`) and screenshots the `.poster` element at true size.
- Load fonts via one combined web-font `<link>`. Write the HTML with a file-write method (not raw shell echo) so `$`/backticks aren't corrupted.

## Export
**Gate:** build and present the HTML first. Export **only after the user confirms.**

**Prerequisites (once):**
```bash
pip install playwright --break-system-packages
playwright install chromium
```

**Run:**
```bash
python scripts/export_poster.py INPUT.html OUTPUT_DIR --format tall
```
`--format` = square | portrait | tall | story, or pass `--width`/`--height`. `--selector` defaults to `.poster`. The script waits for web fonts, strips the preview transform, screenshots the poster element pixel-perfect, and warns if dimensions don't match the chosen format.

**Verify parity** on first export: real fonts (not fallback), matching line breaks, no clipping, true colours, exact target dimensions.

## Global cautions
- **Don't fabricate** real offers, events, prices, products, or (especially) testimonials. Label illustrative content; social proof is real-only.
- **Verify sourced facts** — event details, prices, product benefits. The brand owner's lived knowledge is the final check.
- **State assumptions** whenever a lever (archetype, preset, palette, format, font) is inferred.
- **Announce font overrides** whenever fonts come from anywhere but `design.md`.

---
_Last updated: 22-07-2026 21:57 SGT_
