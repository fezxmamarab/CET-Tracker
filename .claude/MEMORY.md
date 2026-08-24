# MEMORY — session handoff

> Scratch handoff between sessions. `onboard` reads it; `knowledge-builder` folds anything
> durable into the state layer and then this can be trimmed. Keep it short and current.

_Last updated: 2026-08-24_

## Where things stand
- **SOE workbook first draft built and shipped for owner review:** `SOE CET Tracking 2026.xlsx`
  (repo root, committed on branch `claude/onboarding-9z5cx5`). Department-based model.
- Owner provided the **inputs**: 6 departments — LTE1 (AE Higher Nitec), LTE2 (AE TED & RTE),
  EE (Electrical Engr), MCE (Mechatronic Engr), ME (Mechanical Engr), BE (Built Environment);
  and 15 course types — WSDip, Higher Nitec, Higher Nitec (Enhanced), Nitec, ISC, ISC (WTC),
  SCTP, CoC (ITE), CoC (WTC), Short Courses, MLC, JIND, WSQ, TTT, GE.
- Workbook tabs: Read Me · Overall (merged participation+hours monitor) · one tab per dept ·
  All Courses (register + counts) · Lists (dropdown source). See DECISIONS.md for rationale.
- The committed `reference/SEIT_CET_Dashboard.html` is **reference only**; its parser assumes
  the OLD programme/cluster schema and must be rewritten for the department model.

## What we're waiting on
- **Owner review of the workbook draft.** Two open questions: (a) keep both "Hours" and
  "Total Hours" columns on dept tabs, or one? (b) keep "Runs" on All Courses, or plain list?
- **Output spec for the SOE dashboard** (KPIs, charts, audience) — still needed before the
  dashboard (HTML) is built. Workbook sign-off comes first.

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
