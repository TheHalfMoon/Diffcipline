# Execution frontier — Spec 004

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 003 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`; its accepted benchmark and limitations remain frozen.

Spec 004 planning/T403 is canonical at `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`.

Stable proof schema/T416 is canonical at `fd42970ccf868c5a808b9b3bd03f26c27b7c9161`.

Enterprise policy/T427 is canonical at `f0198395f0a141048b272bfd495f585fb76f6011`.

Broad portability/T435 is canonical at `066c0138e5e2970781cc91abba38797654f92c77`.

Signed release-artifact capability/T447 is canonical at `b20b2671c75c5076fcf66397ee4a3f7c308bdfba`. PR #62 exact head `4dbc751e09808999df61383092c2720f289c34d8` passed `ci` `33361112731` and `release` `33361112742`; exact post-merge `ci` `33361219139` and `release` `33361219144` also completed `SUCCESS`. The canonical release run proved the three locked native builds, deterministic checksum closure, keyless GitHub/Sigstore provenance, attestation-bundle preservation, and subject verification for every native binary. Release drafting was skipped because there was no authorized v1 tag.

## Preserved capability

- dependency-free Rust CLI and existing PASS / REVIEW / FAIL / usage exit semantics;
- stable proof schema `diffcipline.proof/v1` / `1.0` with deterministic policy provenance;
- repository policy version 1 when enterprise mode is absent;
- explicit local enterprise policy with monotonic layering and fail-closed loading;
- one canonical behavioral source for `diffcipline` and one for `diffcipline-review`;
- generic Agent Skills contract plus exact-head qualification for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI;
- explicit v1 release-candidate contract with locked Linux/macOS/Windows builds, exactly three checksum subjects, keyless signed provenance, and independent verification instructions;
- all canonical v0.x evidence and immutable v0.1 release truth.

## Immediate frontier — Phase F

T450–T455 are authorized after the T447 evidence record becomes canonical:

1. update README and contract documentation only with capabilities that are implemented and machine-proven;
2. require one final exact-head candidate to pass `ci`, `skills-compat`, and `release` together;
3. reconcile every valid review/thread and reverify canonical `main` before merge;
4. merge with an expected-head guard;
5. verify exact post-merge repository, proof schema/policy, six-client portability, locked native builds, checksum closure, signed provenance, and attestation subjects;
6. only after T454 is machine-observed, create a separate terminal record for T455;
7. make `COMPLETE_CANONICAL` externally effective only after the terminal record itself is canonical and its required post-merge gates succeed.

No dedicated v1 qualification workflow currently exists; T451 therefore requires the existing authoritative `ci`, `skills-compat`, and `release` workflows on the same final candidate head rather than inventing an unproven replacement gate during closeout.

## Stop conditions

Stop rather than weaken governance if canonical `main` moves unexpectedly, a required exact-head/post-merge workflow fails or disappears, a valid review finding remains unresolved, README claims a capability not already canonical, proof/policy/skill/release contracts regress, signing or subject verification fails, or any public v1 tag/release would be created without separate authority.

No public v1 tag/release is authorized by Spec 004 closeout.
