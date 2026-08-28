# Diffcipline repository instructions

Diffcipline is a proof-before-done discipline layer for coding agents.

## Non-negotiable engineering rules

1. Understand before editing. Trace the real flow and name material assumptions.
2. Prefer no code, existing code, the standard library, platform primitives, and already-installed dependencies before adding new machinery.
3. Keep diffs surgical. Every changed file must have a direct reason.
4. Correctness, security, accessibility, data integrity, and explicit user requirements are never sacrificed for fewer lines.
5. Risk changes rigor. Higher-risk changes require stronger verification, not merely smaller diffs.
6. Do not claim PASS without machine-observed evidence from the exact change under review.
7. Benchmarks must publish tasks, configuration, raw outputs, scoring logic, and limitations. Never hide losing metrics.
8. Keep the core CLI dependency-free until a dependency has a demonstrated net benefit that cannot be achieved reasonably with the Rust standard library.

## Change discipline

- No drive-by refactors.
- No speculative abstractions.
- No new dependency without a documented reason.
- Tests should target behavior and regressions, not implementation trivia.
- Repository technical content is written in English.

## Verification

Before declaring a repository change complete, run the strongest available checks for the touched surface. At minimum for Rust changes:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace --all-targets
```

If the local environment cannot run a required check, report that check as NOT RUN. Never convert absence of evidence into PASS.
