# Diffcipline Proof Contract v1

A proof card is a deterministic summary of repository facts observed for one change. Human output remains concise; `diffcipline check --json` is the stable machine contract.

## Machine schema

The v1 machine proof identifies itself with:

- `schema = "diffcipline.proof/v1"`
- `schema_version = "1.0"`

The repository-tracked schema is `schemas/proof-v1.json`. Required top-level fields and their meanings cannot be removed or silently reinterpreted within schema major version 1. Additive fields require a schema update, tests, and documentation.

Policy provenance is explicit. `policy.mode` is `default`, `repository`, or `enterprise`; `policy.sources` lists policy inputs evaluated for the proof. Enterprise mode is reserved by the stable schema before layered policy implementation lands.

## Verdicts and exit codes

- **PASS / 0** — every configured hard requirement was observed and satisfied.
- **REVIEW / 1** — no hard requirement failed, but judgment or missing optional evidence remains.
- **FAIL / 2** — at least one configured hard requirement failed or verification returned non-zero.
- **64** — usage or execution error; no proof verdict is implied.

## Evidence classes

1. **Diff evidence** — changed files and line counts from Git.
2. **Dependency evidence** — whether dependency manifests changed.
3. **Lockfile evidence** — whether lockfiles changed.
4. **Workspace evidence** — whether untracked files remain.
5. **Scope evidence** — expected files, forbidden surfaces, and violations.
6. **Risk evidence** — the selected risk profile when present.
7. **Verification evidence** — exact configured commands and PASS / FAIL / NOT RUN state.
8. **Policy provenance** — policy mode and evaluated policy sources.

## Invariants

- NOT RUN is never PASS.
- Command success is scoped to the exact command that ran; it does not imply unrelated checks passed.
- Diff size is a review signal, not a correctness metric.
- Minimality never overrides security, validation, accessibility, data integrity, or explicit requirements.
- A proof card reports observations. It does not invent intent or root cause.
- Existing v1 required fields keep their meanings for the lifetime of schema major version 1.
