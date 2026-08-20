# FEATURES — CET-Tracker

## In this repo
- **Blank workbook template** (`SEIT CET Tracking 2026 - TEMPLATE.xlsx`) — status: **done**.
  All 12 worksheets the dashboard needs; one marked example row + empty input rows per detail
  sheet; `Overall`/`Overall (Hours)` totals as live cross-sheet formulas that auto-reconcile;
  a Read Me tab. Validated against the dashboard's own parser and a browser render.
- **Personal skills** under `.claude/skills/` — status: **installed** (10 skills:
  ask-the-board, carousel-pillar-system, code-review, explain-plainly, feature-dev,
  knowledge-builder, onboard, poster-system, release-prep, wrapup).

## The dashboard (external file, not committed — documented from the provided upload)
Status of features observed in `SEIT_CET_Dashboard.html`:
- **Local upload** of an `.xlsx`, parsed on-device (no transmission). — done
- **Overview tab** — KPIs (recorded CET participation, FY target, achievement %, remaining
  gap); FY quarterly progress bar + Q1–Q4 cards with checkpoints; progress-by-programme;
  cluster-contribution; activity snapshot; management notes. — done
- **Training Hours tab** — CET training hours by programme and cluster. — done
- **Activities tab** — filterable/searchable activity table (by programme, cluster, status). — done
- **Offerings tab** — unique course offerings derived from the sheets + `CoC Owners`. — done
- **9-course pipeline tab** — upcoming courses from `9 Course Tracking`. — done
- **Data checks tab** — required-sheets, FY-boundary overlaps, planned/not-run, missing
  dates, Pending short courses, reconciliation difference. — done
- **Reconciliation gate** — refuses to load on detail-vs-Overall mismatch. — done
- **Print summary** and an embedded-snapshot mode (SHA-256 integrity-checked). — present

## Not built / open
- Dashboard HTML is not version-controlled here (see TODO).
- No automated tests in-repo (validation was done ad hoc this session with Node + ExcelJS).
