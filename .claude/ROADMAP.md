# ROADMAP — CET-Tracker

## Now
- Workbook template shipped and validated. Skills installed.

## Next (suggested)
1. **Commit the dashboard HTML** so the docs are verifiable against real code and the app is
   version-controlled alongside its template.
2. **Commit the template generator script** for reproducible template builds (and to make
   schema changes reviewable as code rather than a binary blob).
3. Decide whether populated real-data workbooks live in the repo or stay off-repo (they are
   operational data, not code — likely off-repo / gitignored).

## Later / possible
- Lightweight automated check (Node + ExcelJS) that a workbook passes `createDashboardData`,
  runnable in CI or as a pre-commit, so template/schema changes can't silently break loading.
- A one-click "export snapshot" workflow if the embedded-snapshot mode is to be used.

## Not planned
- No backend/server; the on-device, no-transmission model is intentional.
