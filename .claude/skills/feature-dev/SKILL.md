---
name: feature-dev
description: Implement a new feature in a disciplined, minimal-context way. Loads heavy reference docs only when the task needs them. Use when I ask you to build or change a feature.
---

# Feature Development

## Process
1. **Understand** — restate the request in one or two sentences. Ask a clarifying question if ambiguous; do not guess.
2. **Scope** — identify the *minimum* set of files to change. Only now, load the reference docs you actually need:
   - touching structure/flow → read `.claude/ARCHITECTURE.md`
   - touching data/storage → read `.claude/DATABASE.md`
   - need to locate code → read `.claude/FILE_MAP.md`
   Do not load references the task doesn't touch.
   If a needed reference is missing, work from the code and suggest `/knowledge-builder`; don't stall.
   Treat FILE_MAP.md as a pointer — confirm against the actual files before editing.
3. **Plan** — present the plan and the file list. Wait for my go-ahead before writing code.
4. **Implement** — make the change. Follow the conventions in the global and project `CLAUDE.md`, and the standard practices of the project's stack.
5. **Validate** — check it works: syntax, wiring, edge cases, clean startup/activation. State what you verified and what you couldn't.

## Guardrails
- Respect any phase discipline the project's docs define (e.g. design/mockup before build). If we're at the wrong phase, flag it before writing code.
- Keep changes surgical. Don't refactor unrelated code.
- If the change alters architecture, data model, or file layout, note it so `/wrapup` can record it.
