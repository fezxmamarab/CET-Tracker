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
