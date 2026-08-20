# ARCHITECTURE — CET-Tracker

## Shape
Single-file client-side app. One `.html` contains the UI, CSS, all logic, and a minified
copy of **ExcelJS** (~1 MB — the reason the file is large). No backend, no build, no network.
A companion `.xlsx` workbook supplies the data. (The HTML is not committed to this repo yet.)

## Load & render flow
1. `handleFile(file)` — rejects non-`.xlsx`; reads the file via `file.arrayBuffer()`.
2. `new ExcelJS.Workbook(); workbook.xlsx.load(buffer)` — parse in-browser.
3. `createDashboardData(workbook)` — the parser + validator (see below). Throws a typed
   error (shown in a red box) on any structural or reconciliation failure.
4. `applyDashboardData(...)` → `render()` — populate the six tabs.

## Parser (position-based, not header-name-based)
- Constants: `CLUSTERS = [EC1,EC2,ICT1,ICT2]`, `FY_START/FY_END`, `FY_QUARTERS`,
  `CET_REPORTABLE_PROGRAMMES` (excludes ApLM), `CONFIG` (per-sheet column map).
- `parseActivities` — for each detail sheet, find the section header row (a keyword in
  column C) then read rows until a `Total` row. Cluster = col B; course = col C; other
  columns per `CONFIG`. Applies `applySctpEnrollmentRule`.
- `parseOverallTable` — reads the `Overall` and `Overall (Hours)` summary tables (targets,
  cluster columns, Total).
- `parseOfferings` / `parsePipeline` — Offerings tab (incl. `CoC Owners`) and the
  `9 Course Tracking` pipeline.
- `aggregate` — per-programme actuals and per-cluster totals from the activity rows.
- `buildQuality` — the Data-checks panel.

## The reconciliation gate (critical)
`createDashboardData` **refuses to load** the workbook unless the detail rows sum exactly to
the `Overall` sheet:
- each programme's detailed participation == its `Overall` row Total, and
- the grand detailed total == the `Overall` Total row, and
- CET-reportable detailed total == sum of CET-reportable `Overall` rows.
On mismatch it throws and names the differing programme. This is why the workbook must be
internally consistent (the template uses formulas so `Overall` auto-sums the detail sheets).

## Counting rules encoded in the parser
- **SCTP** — participation counted once at enrolment level = the SCTP `Total` row, column E
  (not the sum of module rows).
- **MLC** — annual-cumulative (no dates); feeds the FY bar and the latest quarter's
  cumulative, not a single quarter's actual.
- **ApLM** — monitoring-only; excluded from CET participation and CET training hours.
- **FY window** — 1 Apr 2026 → 31 Mar 2027; two-date activities included only if they overlap.
- **Quarter assignment** — FY term code if present (5264=Q1, 5267=Q2, 526X=Q3, 5261=Q4),
  else the activity date.
- Blank/0 participants ⇒ "Planned / not run" (kept, counts as 0).

## ExcelJS gotcha (learned building the template)
ExcelJS returns the **master value for every cell under a merged range**; a merged title
containing a section keyword (e.g. "Short Courses") bleeds into column C and false-triggers
the header regex. The template avoids merged cells on data sheets. Likewise, example/course
names must not contain a section header keyword (e.g. "short course").

## Tabs
Overview · Training Hours · Activities · Offerings · 9-course pipeline · Data checks.
