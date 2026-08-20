---
name: onboard
description: Start-of-session briefing. Reads the lean project state layer, summarises where things stand, names the next step, then stops and waits. Use at the beginning of every new Claude Code conversation before doing any work.
---

# Onboard

Get current on this project cheaply, then stop. Do NOT start work.

## Step 0 — Check the knowledge base exists
Before reading anything else, check whether `./CLAUDE.md` and the `.claude/` docs exist.

If `./CLAUDE.md` is missing, OR the `.claude/` folder has none of PROJECT.md / TODO.md / ROADMAP.md / DECISIONS.md:
- Stop here. Tell me plainly: "This project has no knowledge base yet. Run `/knowledge-builder` first — it will set up CLAUDE.md and the docs. I'll wait."
- Do NOT read source code, do NOT try to summarise, do NOT start work.

Only if the knowledge base exists, continue below.

## Read ONLY these (the state layer)
1. `./CLAUDE.md` (project root — the project's facts and conventions)
2. `.claude/PROJECT.md`
3. `.claude/TODO.md`
4. `.claude/ROADMAP.md`
5. `.claude/DECISIONS.md`

Do NOT read ARCHITECTURE.md, DATABASE.md, FILE_MAP.md, or FEATURES.md yet.
Do NOT inspect source code. Those load later, on demand, only when a task requires them.
If a `MEMORY.md` exists in the repo, note it and tell me it looks like an un-integrated handoff — suggest running `/knowledge-builder` to fold it in.

## Staleness check — verify the state layer before trusting it
Read-only. Do not write, edit, or run project code here.
If this is a git repo:
1. Latest commit date: `git log -1 --format=%ci`.
2. Last-modified time of `.claude/TODO.md` and `.claude/DECISIONS.md`.
3. If the latest commit is NEWER than both, the state layer is likely stale
   (last session probably ended without `/wrapup`). Then:
   - Open the briefing with: "⚠ State layer may be stale — code changed after the
     docs were last updated. Last commit: <date/message>. Docs last touched: <date>."
   - List the unaccounted commits: `git log --oneline --since=<doc date>`.
   - Still deliver the briefing from the docs, but mark it unverified.
4. Not a git repo → skip this check; note "(no git — staleness check skipped)".
Stale docs downgrade confidence; they do not block the briefing.

## Then report, concisely
- **Done last session** — what was completed.
- **In progress** — current task, exact status, any blocker.
- **Next step** — the single clearest next action, phrased as a proposal.
- **Watch-outs** — any relevant recent decision or project constraint.

## Then STOP
End with: "Confirm the next step or give me a task. I won't edit or run anything until you do."
Do not write, edit, or execute code until I explicitly approve.
