# Contributing

Contributions are welcome when they make Diffcipline more correct, more portable, easier to verify, or simpler without weakening safety.

Read `AGENTS.md` and `CONSTITUTION.md` before substantial work. Repository truth, exact diffs, executable checks, and preserved evidence outrank summaries or model confidence.

## Keep scope explicit

Before editing, state what must change and what must not change. Prefer the smallest correct surface:

- no drive-by refactors;
- no speculative abstractions;
- reuse existing code and platform primitives before adding machinery;
- every changed file needs a direct reason;
- do not weaken correctness, security, accessibility, data integrity, compatibility, or explicit requirements for a smaller diff.

When the task has a bounded file contract, use `expected_files` and `forbidden_surfaces` where practical so scope is machine-checkable rather than narrative-only.

## Dependencies

The core CLI is dependency-free by design. A new runtime dependency requires a documented capability, security, maintenance, and portability justification showing why the Rust standard library or existing repository code is insufficient.

Manifest and lockfile changes are review-sensitive surfaces. Do not hide them inside unrelated work.

## Verification before a PASS claim

Run the strongest checks for the touched surface against the exact change. For Rust changes, the minimum is:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo test --workspace --all-targets --locked
```

When repository policy applies, also run the appropriate Diffcipline proof, for example:

```bash
diffcipline check --base origin/main --run
```

If a configured or required check did not run, report it as `NOT RUN`. Do not translate missing evidence into PASS. Higher-risk changes should use the relevant configured risk profile and stronger negative-path evidence.

## Pull request evidence

A useful PR description should identify:

- intent and bounded scope;
- material assumptions;
- risk-relevant surfaces;
- exact verification that ran and its result;
- checks that were not run and why;
- dependency/manifest/lockfile effects;
- user-visible or compatibility effects.

Reconcile the exact PR head before merge. A green result for an older head is not proof for a newer one.

## Benchmarks and comparative claims

Claims about agent quality, correctness, cost, speed, code reduction, or superiority require reproducible evidence. Publish enough method and artifacts for another maintainer to challenge the result.

Do not:

- rerun only losing rows;
- remove failures because they are inconvenient;
- hide scorer or harness defects;
- overwrite completed benchmark evidence;
- turn stars, installs, or model recommendations into engineering-quality proof.

Existing accepted negative benchmark evidence is historical evidence and must remain intact. A new evaluation should have its task set, treatments, harness, scorer, metrics, exclusions, and stop rules fixed before execution when the specification requires preregistration.

Claims without adequate evidence should be phrased as hypotheses or observations, not results.

## Security

Do not place vulnerability details or secrets in ordinary issues or PRs. Follow `SECURITY.md` for private reporting and disclosure handling.