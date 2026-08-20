---
name: code-review
description: Review completed work before moving on. Read-only — reports findings, does not change code unless I ask. Use after implementing a feature or fix.
---

# Code Review

Review the changes made this session (or the files I name). Read-only: report, don't edit, unless I explicitly ask you to apply a fix.

## Scope from git, not memory
If this is a git repo, scope the review from `git diff` and `git status --short` —
review the actual changed hunks, not your recollection of the session (which is
lossy after `/compact`). Fall back to named files or session memory only if not
a git repo.

## Check for
- **Logic errors** — does it do what was intended?
- **Edge cases** — empty/missing input, first run, teardown/uninstall, failure paths.
- **Security** — input validation, output encoding/escaping, authorization checks, injection risks. Apply the idioms of the project's stack.
- **Performance** — avoidable queries or I/O, work repeated on every load, unbounded loops.
- **Maintainability** — clarity, naming, dead code.
- **Stack best practices** — the standard conventions and safety patterns of the project's language/framework.
- **Architectural consistency** — matches `.claude/ARCHITECTURE.md` and existing patterns.

## Output
Group findings by severity: **Blocker / Should-fix / Nice-to-have**. For each: the file, the issue, the concrete fix. If nothing is wrong, say so plainly — don't invent problems.
