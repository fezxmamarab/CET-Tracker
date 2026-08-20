# DATA MODEL — the workbook schema

The "database" is the Excel workbook (`SEIT CET Tracking 2026.xlsx`). The dashboard parser
reads it by **fixed column positions** (1-indexed: A=1, B=2, …). On every detail sheet:
**cluster = column B**, **course/module = column C**. A section starts at a header row (a
keyword in column C) and ends at a row whose column C is `Total`.

## Detail sheets (activity rows)
| Sheet | Header keyword (col C) | Cluster | Course | Date(s) | Participants | Trainer | Hours | Total Hours | Notes |
|---|---|---|---|---|---|---|---|---|---|
| WSDip | `WSDip Module` | B | C | D | **E** | F | H | I | J |
| Higher Nitec (CET) | `Higher Nitec…Module` | B | C | D | **F** | E | G | H | — |
| SCTP | `SCTP Module` | B | C | D | **E** | F | G | H | I |
| CoC | exactly `CoC` | B | C | D | **F** | E | G | H | — |
| Short Courses | `Short Course` | B | C | D=start, E=end | **G** | F | H | I | J |
| MLC | `MLC` / `MLC Course Name` | B | C | *(none)* | **D** | F | G | H | — |
| APLM | `APLM Course Name` | B | C | D=start, E=end | **G** | F | H | I | J |

- The header row's participant column must contain the word "Participant"/"Trainee" or the
  parser throws `MISSING_REQUIRED_COLUMN`.
- A data row counts only when col B ∈ {EC1,EC2,ICT1,ICT2} AND col C is non-blank.
- `APLM` sheet → programme name `ApLM` (monitoring-only).

## Summary sheets
**Overall** and **Overall (Hours)** — same layout. Header row = col B matches `Programme(s)`
and col I = `Total`; body rows one per programme; a final `Total` row.
| B | C | D | E | F | G | H | I | J |
|---|---|---|---|---|---|---|---|---|
| Programme | Target | Cluster Target | EC1 | EC2 | ICT1 | ICT2 | **Total** | % |

- Only **col C (target)**, **col D (cluster target)** and **col I (Total)** are load-bearing.
  Col I is the reconciled figure; E–H are display-only. The `Overall` grand-total row col C =
  the school FY target KPI; col D = approved cluster target.
- `Overall (Hours)` is display-only (drives the Training Hours tab; not reconciled).
- Programme rows must exist for all seven (WSDip, Higher Nitec (CET), SCTP, CoC, Short
  Courses, MLC, ApLM); names are matched case/space-insensitively.

## Support sheets
- **9 Course Tracking** (pipeline) — data from **row 3**: B=S/N, C=title (required),
  E=type, I=month(date), J=remarks, K=update. Owner parsed from remarks/update
  ("in charge" / "update by").
- **CoC Owners** (optional) — B=cluster, C=title, D=AD owner, E=manager owner (feeds CoC
  entries on the Offerings tab).

## Special counting rules (see ARCHITECTURE.md)
- SCTP participation = SCTP `Total` row col E (enrolment), counted once per section.
- MLC = annual-cumulative (no dates). ApLM = excluded from CET totals.
- Training hours for a row count only when participants > 0 and Total Hours > 0.

## Reconciliation invariant
Σ(detail participation per programme) == Overall row Total (col I) for each programme, and
the grand totals must match, else the dashboard refuses to load. In the template, `Overall`
col I cells are **formulas** that sum the detail sheets so this holds automatically.

## Required worksheets
`Overall`, `Overall (Hours)`, `WSDip`, `Higher Nitec (CET)`, `MLC`, `SCTP`, `CoC`,
`Short Courses`, `APLM`, `9 Course Tracking` (+ optional `CoC Owners`).
