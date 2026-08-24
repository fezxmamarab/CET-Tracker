# TODO — CET-Tracker

Most actionable first.

- [ ] **AWAIT OWNER REVIEW** of `SOE CET Tracking 2026.xlsx` (first draft). Two open design
      questions put to the owner: (a) keep both "Hours" and "Total Hours" columns on dept tabs
      or just one? (b) keep the "Runs" column on All Courses or make it a plain list?
- [ ] After the workbook is signed off: build the SOE progress **dashboard** (HTML). Still need
      the owner's output spec (KPIs, charts, audience). The SEIT dashboard is reference only and
      its parser assumes the OLD schema — it will need rewriting for the department-based model.
- [ ] Commit the template generator script(s) for reproducible builds (SEIT + SOE). The SOE
      build used two scratchpad scripts: `build_soe.py` (structure/formulas) and
      `inject_cache.py` (cached-value injection). Currently off-repo.
- [ ] Once the SOE schema is finalised, document it in `.claude/DATABASE.md` (currently SEIT-only).
- [ ] Decide repo policy for populated real-data workbooks (likely keep off-repo / gitignore).
- [ ] (Optional) Add a Node + ExcelJS smoke test that a workbook passes `createDashboardData`.

## Done recently
- Built `SOE CET Tracking 2026.xlsx` — first draft of the department-based SOE template
  (6 dept tabs + merged Overall + All Courses register + Lists). Committed + pushed to
  `claude/onboarding-9z5cx5`. Owner received departments (LTE1, LTE2, EE, MCE, ME, BE) and
  15 course types.
- Installed 10 personal skills under `.claude/skills/`.
- Built + validated the blank workbook template; committed it.
- Created the `.claude/` knowledge base + root `CLAUDE.md`.
- Committed the SEIT dashboard as `reference/SEIT_CET_Dashboard.html` (reference only).
- Confirmed direction: SOE = School of Engineering, ITE College West.
