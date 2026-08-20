---
name: knowledge-builder
description: Set up or refresh a project's knowledge base from the codebase, and fold any un-integrated .claude/MEMORY.md handoff into the state layer. On a fresh project it also creates the root CLAUDE.md, so no manual setup is needed — just run it. This is the ONE skill allowed to read everything. Run when setting up a new project, when docs have drifted, after a big change, or when onboard/wrapup flags a MEMORY.md handoff. Not for daily use.
---

# Knowledge Builder

The codebase is the source of truth. Documentation is a derived summary of it.
Inspect the repo and make the project's memory files match reality.

## Step 0 — Bootstrap the root CLAUDE.md (only if it's missing)
Check whether `./CLAUDE.md` exists in the repo root.

If it does NOT exist, create it before anything else:
1. Infer as much as possible from the repo: project name (from folder/package/manifest), the language/framework stack, and any obvious naming prefix already used in the code.
2. Draft `./CLAUDE.md` using this structure:
   ```
   # <PROJECT NAME> — Project Memory

   <one line: what this project is and who it serves>

   ## Conventions
   - Naming/prefix: <inferred, or a sensible default>
   - Stack / target environment: <inferred>
   - Phase discipline: <e.g. design before build, or "none noted">

   ## Where knowledge lives (read the file — do NOT re-derive it)
   | Need | File |
   |------|------|
   | What/why, scope | `.claude/PROJECT.md` |
   | Current tasks | `.claude/TODO.md` |
   | Direction, phases | `.claude/ROADMAP.md` |
   | Decisions + rationale | `.claude/DECISIONS.md` |
   | System design | `.claude/ARCHITECTURE.md` |
   | Data model | `.claude/DATABASE.md` |
   | Where code lives | `.claude/FILE_MAP.md` |
   | Feature inventory | `.claude/FEATURES.md` |

   Load the state files (PROJECT, TODO, ROADMAP, DECISIONS) at onboarding.
   Load the heavy references (ARCHITECTURE, DATABASE, FILE_MAP) only when a task touches them.
   ```
3. Anything you had to guess (prefix, phase rule, one-line purpose), flag clearly at the end so I can correct it. Do NOT stall waiting for answers — fill a sensible default and move on.

If `./CLAUDE.md` already exists, read it, follow its conventions, and leave it alone.

## Step 1 — Build the knowledge base
1. Inspect the repository: structure, main modules, data storage (tables/schemas/files/options), entry points, key classes and functions.
2. If a `MEMORY.md` or similar note file exists, merge any still-accurate context; discard anything the code contradicts.
3. Create or update each file below under `.claude/`. Overwrite stale content; don't append duplicates. Keep each file tight — a summary, not a transcript.

### Files to produce
- `PROJECT.md` — what it is, who it serves, scope boundaries. One screen.
- `ARCHITECTURE.md` — how the pieces fit: modules, data flow, extension points.
- `DATABASE.md` — the data model: tables, schemas, stored options, or equivalent for the stack.
- `FEATURES.md` — implemented features and their status.
- `FILE_MAP.md` — where things live; the map a fresh session uses to find code fast.
- `ROADMAP.md` — phases and what's next.
- `DECISIONS.md` — key decisions, one line of rationale each.
- `TODO.md` — outstanding tasks, most actionable first.

If the repo is new and nearly empty, create these files with honest placeholders and note what's missing, rather than inventing content.

## Rules
- Verify claims against the code. If something can't be confirmed from the repo, flag it rather than inventing it.
- Do NOT touch `CHANGELOG.md` — that belongs to `/release-prep`.
- End by listing: whether you created CLAUDE.md, which `.claude/` files you created or changed, and anything you guessed or were unsure about.
