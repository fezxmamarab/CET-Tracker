# DECISIONS — CET-Tracker

- **Excel is the source of truth; the dashboard is read-only.** Keeps existing coordinator
  workflow; the app never writes back.
- **On-device only, no transmission.** Workbook is parsed in the browser via ExcelJS; privacy
  by construction.
- **Strict reconciliation gate.** The dashboard refuses to load unless detail rows sum to the
  `Overall` totals — trades convenience for trustworthy figures and catches data-entry drift.
- **Template uses formulas, not hardcoded totals**, so `Overall`/`Overall (Hours)` auto-sum
  the detail sheets and stay reconciled as the user edits.
- **Cached formula values injected into the `.xlsx` XML.** The web sandbox's LibreOffice can't
  recalc; openpyxl leaves formula caches empty, which would read as 0 and fail the
  reconciliation gate on first load. Injecting cached values lets the file load directly while
  formulas still recalc in the user's Excel on save.
- **No merged cells on data sheets; example/course names avoid section keywords.** ExcelJS
  propagates a merged cell's value to every covered cell, false-triggering the position-based
  header regex — both bugs found and fixed while validating the template.
- **ApLM excluded from CET totals; MLC treated as annual-cumulative; SCTP counted at
  enrolment level.** These mirror the dashboard's business rules so the template reconciles.

## SOE workbook (2026-08-24)
- **SOE governed by DEPARTMENT, not course type.** Tabs are the 6 departments (LTE1, LTE2, EE,
  MCE, ME, BE), each owned by one rep; course type became a dropdown column. This is the owner's
  org model — replaces SEIT's tab-per-course-type + EC/ICT cluster column.
- **Built the SOE workbook FRESH, not adapted from SEIT.** The tab axis flipped (department vs.
  course-type), so a rewrite was cleaner than editing the SEIT template.
- **One merged `Overall` tab** (participation + hours side by side) instead of SEIT's two
  Overall tabs — owner wants to monitor from a single sheet.
- **`All Courses` is a manual register + COUNTIF counts**, not auto-consolidated from the dept
  tabs. Excel can't reliably gather a growing cross-sheet list without dynamic-array functions
  (FILTER/UNIQUE), which the sandbox's LibreOffice can't evaluate — so a manual list is robust.
- **Dropdowns sourced from a `Lists` sheet** (15 course types, 6 departments) via cross-sheet
  list validation, so the vocabulary is edited in one place.
- **Reused the SEIT cached-value-injection method** (`build_soe.py` + `inject_cache.py`):
  openpyxl writes formulas, then cached values are injected into the XML because the sandbox
  LibreOffice recalc (both the StarBasic macro and `--convert-to` paths) hangs/fails here.
  Excel recalculates live on open.
