# MEMORY — session handoff

> Scratch handoff between sessions. `onboard` reads it; `knowledge-builder` folds anything
> durable into the state layer and then this can be trimmed. Keep it short and current.

_Last updated: 2026-08-20_

## Where things stand
- **PR #1 is open** (branch `claude/cet-tracker-skills-install-shhsax` → `main`) with all of
  this session's work: https://github.com/fezxmamarab/CET-Tracker/pull/1 — awaiting the
  owner's review + Merge. Nothing is on `main` yet.
- Repo currently holds: the **reference** SEIT dashboard, a **blank workbook template**, the
  `.claude/` knowledge base, and 10 personal skills. Nothing here is the final SOE product yet.
- The committed `reference/SEIT_CET_Dashboard.html` is **reference material only** — the owner
  will use it as a model when building a dashboard for **SOE (School of Engineering), ITE
  College West**. It is NOT the source of truth and NOT what we ship.

## What we're waiting on (do not build yet)
- The owner is gathering requirements from others on **how to present the data**. Two things
  are needed before building the SOE dashboard:
  1. **Inputs** — what data will be tracked / what the source workbook (or other source) looks like.
  2. **Outputs** — how the dashboard should present it (KPIs, tabs, charts, audience).
- The owner will update us when that information is ready. Until then, hold on building.

## Useful context already captured (see the state layer)
- How the reference dashboard works, its strict reconciliation gate, and the full workbook
  schema: `.claude/ARCHITECTURE.md` and `.claude/DATABASE.md`.
- Two ExcelJS/parsing gotchas learned while building the template (merged-cell value bleed;
  example names must avoid section-header keywords): `.claude/DECISIONS.md`.
- The template and its validation approach (formulas + injected cached values because the web
  sandbox can't run LibreOffice recalc): `.claude/DECISIONS.md`, `.claude/FILE_MAP.md`.

## Open decisions for when the spec arrives
- Adapt the SEIT reference (same programmes/clusters/rules) vs. build fresh for SOE's model.
- Whether the template generator script gets committed for reproducibility.
- Repo policy for real (populated) data workbooks — probably keep off-repo.

## Corrections logged
- SOE = School of Engineering (confirmed). Focus institution: ITE College West.
