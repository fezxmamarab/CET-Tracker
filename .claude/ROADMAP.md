# ROADMAP — CET-Tracker

## Now
- SOE build has started. First draft of the SOE workbook (`SOE CET Tracking 2026.xlsx`,
  department-based model) shipped for owner review. Awaiting sign-off on two design questions.

## Next (suggested)
1. **Finalise the SOE workbook** after owner review, then document its schema in DATABASE.md.
2. **Build the SOE dashboard (HTML)** once the owner provides the output spec. The SEIT
   dashboard is reference only; its parser assumes the old programme/cluster schema and must be
   rewritten for the department-based model.
3. **Commit the template generator scripts** (`build_soe.py`, `inject_cache.py`) for
   reproducible builds.
4. Decide whether populated real-data workbooks live in the repo or stay off-repo (likely
   off-repo / gitignored).

## Later / possible
- Lightweight automated check (Node + ExcelJS) that a workbook passes `createDashboardData`,
  runnable in CI or as a pre-commit, so template/schema changes can't silently break loading.
- A one-click "export snapshot" workflow if the embedded-snapshot mode is to be used.

## Not planned
- No backend/server; the on-device, no-transmission model is intentional.
