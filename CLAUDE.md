# CET-Tracker — Project Memory

A local-only progress dashboard for tracking SEIT's FY2026 CET (Continuing Education &
Training) participation and training hours, fed by an Excel workbook. This repo holds the
data workbook template; the dashboard itself is a single self-contained HTML file.

## Conventions
- Naming/prefix: none in use (small repo; no code package yet).
- Stack / target environment: static single-file HTML dashboard (vanilla JS + an embedded
  copy of ExcelJS), read entirely client-side in the browser. Data lives in an `.xlsx`
  workbook authored in Excel. No backend, no build step, no network calls.
- Phase discipline: none noted. Excel is the source of truth; the dashboard is a read-only view.

## Where knowledge lives (read the file — do NOT re-derive it)
| Need | File |
|------|------|
| What/why, scope | `.claude/PROJECT.md` |
| Current tasks | `.claude/TODO.md` |
| Direction, phases | `.claude/ROADMAP.md` |
| Decisions + rationale | `.claude/DECISIONS.md` |
| System design | `.claude/ARCHITECTURE.md` |
| Data model (workbook schema) | `.claude/DATABASE.md` |
| Where things live | `.claude/FILE_MAP.md` |
| Feature inventory | `.claude/FEATURES.md` |

Load the state files (PROJECT, TODO, ROADMAP, DECISIONS) at onboarding.
Load the heavy references (ARCHITECTURE, DATABASE, FILE_MAP) only when a task touches them.

## Direction (confirmed by the owner)
- **SOE = School of Engineering.** Target institution: **ITE College West.**
- Goal: build a NEW CET progress dashboard for SOE / ITE College West. The committed SEIT
  dashboard is **reference only** (see `reference/SEIT_CET_Dashboard.html`), not the source of
  truth and not the thing being shipped.
- The owner is still gathering requirements — what the **inputs** (data to track) and the
  **outputs** (how to present it) should be. Do NOT start building the SOE dashboard until
  those are provided. See `.claude/MEMORY.md` for the live handoff.
