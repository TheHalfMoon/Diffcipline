# Execution frontier — Spec 004

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 003 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`. Its accepted benchmark and published limitations remain frozen. No v0.3 release tag was created.

Spec 004 planning became canonical at `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`. Planning PR #56 exact head `cb590fde5dc3bf76abee1ec3bd8b512607d63dcf` passed `ci` `33302675371`, `skills-compat` `33302675367`, and `release` `33302675373`. Exact post-merge `ci` `33302752212`, `skills-compat` `33302752218`, and `release` `33302752209` also succeeded.

## Existing capability to preserve

- dependency-free Rust CLI and PASS / REVIEW / FAIL / usage exit semantics;
- repository policy version 1 behavior when enterprise mode is absent;
- portable shared Agent Skills and six-client qualification;
- locked three-platform release builds, SHA-256 aggregation, and GitHub/Sigstore provenance;
- all canonical v0.x benchmark and release evidence.

## Phase B stable-schema candidate

T410–T415 are implemented without rewriting legacy proof logic:

- `schemas/proof-v1.json` is the repository-versioned machine contract;
- the CLI entrypoint reuses existing check/render behavior and prepends stable schema identity plus policy provenance to JSON output;
- existing verdict/diff/scope/risk/reason/verification fields and exit codes are preserved;
- schema policy modes reserve `enterprise` while current runtime provenance is only `default` or `repository`;
- Rust tests cover schema identity and preserved fields;
- the Python stdlib validator parses real CLI output, enforces exact schema field order/identity, and rejects an incompatible schema version;
- CI executes the validator on Linux in addition to cross-platform Rust and dogfood gates.

## Immediate frontier

The only authorized next task is **T416**: qualify, review, merge, and post-merge verify this exact stable-schema unit. Do not start enterprise policy mode before T416 is canonical.

After T416, Phase C may add explicit local enterprise policy layering. It must use the already-stable v1 `policy` object rather than introducing an incompatible proof schema.

## Stop conditions

Stop rather than weaken governance if canonical `main` moves unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, schema output drops or reinterprets an existing field, runtime dependencies are introduced without explicit authority, or any later enterprise layer can weaken its baseline.

No public v1 tag/release is authorized by Phase B.
