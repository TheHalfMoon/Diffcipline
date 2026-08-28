# Diffcipline Proof Contract v0.1

A proof card is a deterministic summary of repository facts observed for one change.

## Verdicts

- **PASS** — every configured hard requirement was observed and satisfied.
- **REVIEW** — no hard requirement failed, but human judgment or missing optional evidence remains.
- **FAIL** — at least one configured hard requirement failed or verification returned non-zero.

## Evidence classes

1. **Diff evidence** — changed files and line counts from Git.
2. **Dependency evidence** — whether dependency manifests changed.
3. **Lockfile evidence** — whether lockfiles changed.
4. **Workspace evidence** — whether untracked files remain.
5. **Verification evidence** — exact configured commands and exit status.

## Invariants

- NOT RUN is never PASS.
- Command success is scoped to the exact command that ran; it does not imply unrelated checks passed.
- Diff size is a review signal, not a correctness metric.
- Minimality never overrides security, validation, accessibility, data integrity, or explicit requirements.
- A proof card reports observations. It does not invent intent or root cause.
