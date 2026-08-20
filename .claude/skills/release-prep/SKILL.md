---
name: release-prep
description: Prepare a production release. Owns CHANGELOG.md and version bumping. Use when I'm ready to cut a release.
---

# Release Preparation

## Tasks
1. **Version** — bump the version wherever the project declares it (manifest, package file, plugin header, readme, and any version string in the project's root `CLAUDE.md`). Confirm the new number with me first. If no version is declared anywhere, ask where it should live.
2. **CHANGELOG.md** — add a dated entry: Added / Changed / Fixed / Removed. This file is release-prep's responsibility; other skills leave it alone. If this is a git repo, derive entries from `git log <last-release-tag-or-date>..HEAD` and `git diff --stat` — not from session memory. Fall back to memory only if not a git repo, and say so.
3. **Release notes** — a short, human-readable summary for users, derived from the changelog.
4. **Readiness check** — no debug/leftover logging, no stray warnings, clean startup/activation, version numbers consistent everywhere.
5. **Deployment checklist** — a step list for shipping (backup, deploy, activate, smoke-test on the target environment, rollback plan).

## Rules
- Do not invent changelog entries — derive them from actual changes this cycle (git evidence first). Flag gaps.
- Follow semantic versioning unless I say otherwise.
- End by confirming version consistency across all files.
