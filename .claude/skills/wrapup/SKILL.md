---
name: wrapup
description: End-of-session close-out. Updates only the knowledge files affected by today's work so the next session resumes with zero re-explanation. Use before ending a Claude Code conversation.
---

# Wrap-up

Preserve today's work so the next session resumes with zero re-explanation.

## Step 0 — Safety net: is there a knowledge base to update?
Check whether `./CLAUDE.md` and the `.claude/` state docs (PROJECT.md, TODO.md, ROADMAP.md, DECISIONS.md) exist.

If they are missing (e.g. `/knowledge-builder` was never run this project):
- Do NOT attempt a full build — that's the wrong tool at the end of a session.
- Instead, write a lossless handoff to `.claude/MEMORY.md` using these headings:
  - `## Project Status` — what's built, what works, what's half-done.
  - `## Decisions Made` — decisions from this session, one line of rationale each; include reasoning that isn't obvious from the code.
  - `## Outstanding Tasks` — most actionable first.
  - `## Open Questions / Blockers` — anything unresolved.
  Keep it factual and terse; the reader is a fresh session that hasn't seen this chat.
  Build this handoff from git evidence + memory, not memory alone: if this is a git
  repo, run `git status --short` and `git log --oneline` / `git diff --stat` since
  session start and fold in anything git shows that memory missed.
- Then tell me: "No knowledge base yet — I saved everything to `.claude/MEMORY.md`. Run `/knowledge-builder` next session to fold it in properly."
- Stop here.

If the knowledge base exists, proceed to the normal update below.

## Normal update — touch only what changed
0. Ground-truth check before writing anything. If this is a git repo, reconcile
   memory against reality (git wins when they disagree):
   - `git status --short` — uncommitted work this session.
   - `git log --oneline` since session start (or since the last DECISIONS.md
     entry date if session start is unclear).
   - `git diff --stat` for the same range.
   Compare against what you remember doing. For changes git shows but you don't
   recall (likely lost to `/compact`), inspect the diffs enough to describe them
   accurately and include them. Flag anything you can't explain: "git shows X
   changed but I have no record of why — Hafiz, please confirm before I log it."
   Do NOT auto-commit; wrapup observes git, it does not drive it.
   Not a git repo → fall back to file modification times and note the weaker check.
1. Identify what was done this session (features, fixes, decisions, new files).
2. Update **only** the affected files under `.claude/`:
   - `TODO.md` — tick off completed items; add anything newly surfaced; most actionable first.
   - `ROADMAP.md` — only if direction/phase moved.
   - `DECISIONS.md` — add any decision made today, one line of rationale each.
   - `ARCHITECTURE.md` / `DATABASE.md` / `FILE_MAP.md` — only if structure, data model, or file locations actually changed.
   - `FEATURES.md` — only if a feature's status changed.
3. Leave unchanged files alone. Do not rewrite docs that didn't change.
4. Do NOT touch `CHANGELOG.md` — that belongs to `/release-prep`.

## Style
Factual and terse. No narrative. The reader is a fresh session tomorrow.

## Finish
List exactly which files you changed (or that you wrote MEMORY.md) and the one-line reason for each.

## Chat title (for Hafiz's archive)
End with a suggested title for this chat, on its own line so it's easy to copy:

> **Suggested chat title:** `<title>`

Format: `<Project> — <main outcome(s)>` (e.g. `OneKampung — v1.5.0 SEO pass built + deployed`).
Keep it under ~60 characters, name the concrete outcome (versions shipped, feature built,
decision made) — not the activity ("worked on SEO"). If the session was mostly discussion
with no artefact, title the decision or topic instead.
