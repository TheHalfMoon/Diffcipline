## Intent

<!-- What user or maintainer outcome does this change deliver? -->

## Scope

<!-- Name the bounded surfaces changed and the important surfaces intentionally left unchanged. -->

- Changed:
- Intentionally unchanged:

## Risk

<!-- Note security, compatibility, executable policy, release, benchmark, dependency, or other risk-relevant effects. Use "None identified" only after checking. -->

## Verification

<!-- Record only checks that actually ran against the exact PR head. Missing checks are NOT RUN, never implied PASS. -->

| Check | Result |
| --- | --- |
| `cargo fmt --all -- --check` | NOT RUN |
| `cargo clippy --workspace --all-targets --locked -- -D warnings` | NOT RUN |
| `cargo test --workspace --all-targets --locked` | NOT RUN |
| Diffcipline proof for the touched surface | NOT RUN |

## Change discipline

- [ ] Every changed file has a direct reason.
- [ ] No drive-by refactor or speculative abstraction is included.
- [ ] Dependency, manifest, and lockfile effects are called out explicitly.
- [ ] User-visible and compatibility effects are documented.
- [ ] Benchmark or comparative claims, if any, include reproducible evidence and limitations.
- [ ] No required check is represented as `PASS` without exact machine-observed evidence.

## Reconciliation

<!-- Before merge, reconcile the exact head: CI, reviews, threads, substantive comments, mergeability, and canonical main. A head change invalidates earlier exact-head qualification. -->
