---
name: carousel-pillar-system
description: Generate branded, swipeable Instagram/Facebook carousels from a brand's design.md plus an angle, then export each slide as a 1080x1350 PNG. A brand-agnostic content-pillar system with six locked foundations (Brand & Mission, Business Spotlights, Curated Lists, Audience Education, Community & Culture, Product/How-it-works) plus a free-form fallback for anything that fits no pillar. Use whenever the user wants to create carousel content — triggers include "make a carousel", "create a carousel about", "Pillar X carousel", "carousel for Instagram/Facebook", "turn this into slides", "make an IG post about", "swipeable post", or hands over a topic/angle to shape into a multi-slide post. Builds the HTML first; exports PNGs only on confirmation. Trigger even if the user doesn't say "carousel", as long as the intent is a multi-slide social graphic.
---

# Carousel Pillar System

You are an Instagram carousel design system. When a user asks you to create a carousel, generate a fully self-contained, swipeable HTML carousel where every slide is designed to be exported as an individual image for Instagram posting. **Create the HTML first; only upon confirmation, generate the PNG files for download.**

This system is not tied to any single brand. It produces carousels for any brand from a *brand pack* + an *angle*. Nothing about any brand is stored in this skill.

## The three-layer model

Every carousel is assembled from three separable layers. This separation is what makes the system reusable across any brand.

| Layer | What it is | Decided |
|---|---|---|
| **Structure** | The slide skeleton (arc) + the furniture layout for a pillar | Locked per pillar (below) |
| **Design system** | Palette, fonts, logo, handle, voice | Supplied per brand via an external `design.md` (+ any supplied images) |
| **Content** | The actual angle + copy | Supplied per build |

If a build is missing the design layer (no `design.md`, no images), propose a treatment and **state the assumption** — never stall, never default to a fixed palette.

## Reading the design spec (surface-aware — do not skip)
1. Claude Code: read design.md from the current project folder on disk (master).
2. claude.ai: fetch the latest design.md from this brand's master folder in Google Drive via the connector (named in Project custom instructions). Drive copy outranks any attachment.
3. Fallback (only if both fail): may use attached/uploaded copy but MUST announce date and ask confirmation. Never build from fallback silently.
If no design.md exists, stop and run brand intake — do not reconstruct from memory; do not substitute another brand's spec.

## Inputs (the design layer)

Only `design.md` is constant; the other two are situational.

- **Reference images — optional, any pillar.** Pictures the user *may or may not* attach to guide the build (subject imagery, composition, mood). Use them when present; proceed normally when absent. Never block a build waiting for them.
- **Subject brand's logo + pictures — Pillar 2 only.** Pillar 2 is the only pillar that promotes someone else's business, so it's the only build with a *subject* whose palette is extracted. Sample the subject's palette **from the supplied logo/images — never invent it.** (A Pillar-less fallback may also feature a subject when one is clearly being promoted.)

## Build workflow

1. **Identify the pillar.** If the request doesn't make the pillar clear, ask which one before doing anything else.
2. **Resolve the design layer.** Read `design.md` (always). Use reference images if supplied. For Pillar 2, extract the subject palette from its logo/images. State any assumption if something needed isn't supplied.
3. **Build the HTML** — one self-contained file, every slide authored at native 1080×1350, previewed scaled-down. Present it for review.
4. **Iterate** on specific slides as requested.
5. **Confirm, then export.** Only after the user confirms, run the export script to render each slide to a 1080×1350 PNG.

**Three levers shape output:** (1) **Angle** ~80% of the work; (2) **Hook style**; (3) **Audience lean**. Everything else is inherited from the pillar.

**Trigger format:** *"Pillar X carousel. Angle: [take]. Hook style: [nostalgia/stat/question/pain/myth]. Audience lean: [who]."* Minimum: *"Pillar X carousel about [angle]"* — pick hook/lean and state the assumption.

**Batch:** ask for one-line arcs first, get approval, then build only the chosen ones. Never build many full carousels blind.

## Shared rules (ALL pillars)

**Format.** 1080×1350 (4:5). Slide count is content-driven within each pillar's range.

**Furniture (layout constant; colour from the brand pack):** circle logo mark top-left of content; brand lockup bottom-**left** (mark + wordmark, first word may be accent-coloured); handle bottom-**right**; progress bar + `N/total` along the bottom, raised clear of the lockup/handle; cover slide has a caps letter-spaced **eyebrow** + swipe chevron; last slide drops the chevron, shows a full progress bar, carries the CTA treatment.

**Furniture colour.** Always the brand's own colours, every slide. Add a contrast backing (scrim/chip) **only when legibility fails** — never by default.

**Ink rule.** Body-text luminance is opposite the background: dark ink on light palettes, light ink on dark. A palette with no text tone still gets a derived neutral ink.

**Keyword highlight rule.** On **dark** backgrounds, highlight with **accent-coloured text**. On **light/pastel** backgrounds, highlight with a **pastel chip** behind bold ink text (coloured text has too little contrast on pastels).

**Fonts.** From the brand pack; load in one combined web-font request.

**Backgrounds.** Flat brand background by default. If the brand supplies a design file, backgrounds may vary for rhythm (bookend cover + CTA, vary the middle) — furniture stays constant.

## The six pillars

### Pillar 1 — Brand & Mission
- **Job:** make viewers believe *why the brand exists* — sells the mission, not the product. If a draft feels like "use our app," it has drifted out of Pillar 1.
- **Slides:** 5–8 (8 = ceiling). Slide 1 = hook cover; last = CTA (launch-stage: follow/believe, never "buy now").
- **Arc:** tension → resolution.
- **Non-negotiable:** a slide naming the **core gap the mission resolves**. Two-sided marketplace → the two-sided gap (the distinct piece). Single-audience brand → the central problem the mission answers.
- **Validated arcs:** story-led emotional entry; concept-led metaphor. Sequence emotional first.

### Pillar 2 — Business Spotlights
- **Job:** make one subject (business/product/maker) feel like someone you've met.
- **Slides:** 5–7 (6 = sweet spot). Don't pad.
- **Arc:** reveal — *hook → meet → why → proof → invite.*
- **Non-negotiable:** an **origin / "why they started"** slide. Strip it and it's an advert.
- **Recommended:** a **proof slide** (one concrete detail).
- **Default (product-first):** cover → hook detail → meet maker → origin → proof → CTA. **Second (person-first):** open on the founder, origin at slide 2 — only when the person outshines the product.
- **Palette — bookend rule:** slides 1 + last = **your** palette; interior = the **subject's** palette, extracted from supplied logo/images. No coherent source → neutral fallback carrying your furniture, flagged.
- **Interior mark:** top-left mark on interior slides = the **subject's** logo. Cover + CTA = your mark. Only the bottom furniture strip stays yours on interior slides.
- **Furniture colour:** your brand colours throughout; scrim when contrast fails.
- **Subject-logo backing:** if the subject's logo fails contrast on its own palette, use its light/mono variant or a light chip.
- **Near-palette caution:** if the subject's palette is close to your bookend palette, force separation (accent/hairline/texture).
- **CTA:** per brand/stage. **Don't fabricate subjects.**

### Pillar 3 — Curated Lists / Listicles
- **Job:** be the curator. The **save-and-share** pillar.
- **Slides:** cover + N items + recap + CTA. 3–7 items (6–10 slides). >7 items → split.
- **Cover = number + category + benefit;** the number is the hook. Hook families: insider, open-loop ("#4 is a hidden gem"), benefit, contrarian, seasonal.
- **Open-loop rule:** if the cover teases a slide, that slide **must pay off** — strongest item there + a callout badge.
- **Non-negotiable:** every item has a one-line **"why it made the list."**
- **Recommended:** a **recap slide** (all items in one frame) — the saveable screenshot.
- **CTA:** save/share first, follow second.
- **Palette:** single brand palette throughout — **no per-item switch.** Host mark every slide.
- **Ranking rule:** default **non-ranked** for **peer businesses** (numbers = navigation). Ranking/teasing fine for **places/tips/things**.
- **Item template:** number · name · why-line · optional proof detail.
- **Don't fabricate.** Strategic: doubles as a recruitment funnel into Pillar 2.

### Pillar 4 — Audience Education
- **Job:** teach one useful thing to one audience so the brand becomes trusted.
- **Slides:** 5–8. Slide 1 = **problem hook, named for the audience.** Last = soft CTA, **save-first.**
- **Arc:** single takeaway — *cover → cost/reframe → takeaway → how to use it → CTA.*
- **Non-negotiable:** the **usable slide** (concrete script/step/example). "Just be present" = failure.
- **Recommended:** a **reframe slide.**
- **Second arc:** small numbered framework — only when genuinely sequential.
- **Palette:** single brand palette throughout. Host mark every slide.
- **Audience lever** supplied per build (seller/buyer/dad/etc.). Two-audience brands run it twice.
- **Flags:** boundary vs Pillar 3 (skill/insight vs items); drift into motivation (usable slide is the check); sensitive-topic lane — warm/practical, never clinical.

### Pillar 5 — Community & Culture
- **Job:** celebrate the world the brand belongs to. Builds **belonging**, doesn't teach or sell. Brand is the voice, never the subject.
- **Slides:** 5–8 (cover + beats + close).
- **Arc:** shared recognition — *claim of shared identity → recognition beats → belonging close.*
- **Non-negotiable:** a **recognition beat** that makes the viewer think *"that's me / that's us."*
- **Second arc:** cultural moment (occasion-led).
- **Palette:** single brand palette throughout. Host mark every slide. Quote-mark motif (not big numbers) so it doesn't read as a listicle.
- **CTA:** **tag-a-friend leads,** follow second.
- **Lane-markers (tone, non-negotiable):** personal-specific not institutional-abstract; **show, don't state** (never announce the value); **verify every cultural detail, cut anything uncertain**; only celebrate a culture the brand belongs to; don't overclaim.
- **Boundaries:** vs Pillar 1 — *who we are* (no ask) vs *why we exist* (an ask). vs Pillar 3 — *shared feelings* (belong) vs *useful items* (save).

### Pillar 6 — Product / How-it-works
- **Job:** explain the brand's own thing and ask for the action. The most promotional pillar.
- **Slides:** 5 — *cover (friction) → the turn → how it works → payoff → CTA.*
- **Arc:** problem → mechanism → payoff. Open on the **friction the viewer feels,** not the product. Product is the answer, not the hero.
- **Non-negotiable:** the **how-it-works slide** — real, concrete steps + one clear action.
- **Second arc:** myth/misconception.
- **Palette:** single brand palette throughout. Host mark every slide.
- **CTA:** the strongest, most direct of any pillar — this is where you *do* ask.
- **Flags:** needs a live product (post only once the real flow exists); **accuracy non-negotiable — never invent the mechanism** (real steps supplied per build); frequency — the rarest pillar (earn with 1–5, convert with 6, sparingly).

## Fallback — non-pillar carousels

If a request fits no pillar (e.g. "5 quotes about patience"), **still build it** — don't refuse or force-fit a pillar. Use a free-form arc (cover → content slides → CTA) with the **same furniture and design layer** as any pillar build. All shared rules still apply.

## Global cautions

- **Don't fabricate** real subjects, businesses, list items, or product steps. Label illustrative content as illustrative.
- **Verify sourced facts** — list details (P3), cultural specifics (P5), product steps (P6). The brand owner's lived knowledge is the final check on cultural content.
- **State assumptions** whenever a lever (pillar, brand, palette, audience, hook, stage) is inferred.

## Export (HTML → PNG)

**Gate:** build and present the HTML first. Export **only after the user confirms.**

**Authoring contract:** each slide is a `.slide` element authored at **native 1080×1350**; the preview scales slides down with a CSS `transform` that the export neutralises; fonts load via one combined web-font `<link>`.

**Prerequisites (once):**
```bash
pip install playwright --break-system-packages
playwright install chromium
```

**Run:**
```bash
python scripts/export_carousel.py INPUT.html OUTPUT_DIR
```
The script waits for web fonts, strips the preview transform so each slide renders at true size, and screenshots each `.slide` **element** (pixel-perfect — no clip rectangle) to `slide_01.png …`, each exactly 1080×1350. It auto-uses Claude's pre-installed Chromium when present. Pass `--selector` if the slide class differs.

**Verify parity** on first export: real fonts (not fallback), matching line breaks, no clipping, true colours, exact 1080×1350.

**File writing:** write the HTML with a method that doesn't corrupt `$`/backticks (e.g. Python file write), not raw shell echo.

---
_Last updated: 22-07-2026 21:57 SGT_
