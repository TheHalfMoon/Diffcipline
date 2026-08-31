# Execution frontier — Spec 004

Live GitHub/repository truth overrides this snapshot.

## Terminal state

Spec 004 has no remaining implementation task after T455.

The terminal `COMPLETE_CANONICAL` state recorded here is effective only after this completion record is merged to canonical `main` and its required exact post-merge gates succeed. Until then, this branch is only the terminal completion candidate.

## Canonical capability chain

- Spec 003 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`; its accepted benchmark and limitations remain frozen.
- Spec 004 planning/T403 is canonical at `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`.
- Stable proof schema/T416 is canonical at `fd42970ccf868c5a808b9b3bd03f26c27b7c9161`.
- Enterprise policy/T427 is canonical at `f0198395f0a141048b272bfd495f585fb76f6011`.
- Broad portability/T435 is canonical at `066c0138e5e2970781cc91abba38797654f92c77`.
- Signed release-artifact capability/T447 is canonical at `b20b2671c75c5076fcf66397ee4a3f7c308bdfba`.
- Integrated capability milestone/T453 is canonical at `2ff687c038f72a3b747e85ad907d2400955cb649`.

## T454 machine evidence

On exact canonical `2ff687c038f72a3b747e85ad907d2400955cb649`:

- `ci` `33365950241` completed `SUCCESS` across Rust and dogfood jobs on Linux, macOS, and Windows, with proof-v1 schema validation on Linux;
- `skills-compat` `33365950200` completed `SUCCESS` for the generic Agent Skills contract and Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI;
- `release` `33365950214` completed `SUCCESS`, including the locked Linux/macOS/Windows builds, deterministic SHA-256 manifest verification, signed GitHub/Sigstore provenance, attestation-bundle preservation, and verification of every native binary subject;
- `stage GitHub release draft` was intentionally skipped because no public v1 tag exists or is authorized.

## Preserved terminal capability

- dependency-free Rust CLI and existing PASS / REVIEW / FAIL / usage exit semantics;
- stable proof schema `diffcipline.proof/v1` / `1.0` with deterministic policy provenance;
- repository policy version 1 when enterprise mode is absent;
- explicit local enterprise policy with monotonic layering and fail-closed loading;
- one canonical behavioral source for `diffcipline` and one for `diffcipline-review`;
- generic Agent Skills contract plus six-client exact-head portability qualification;
- explicit signed release-candidate contract with locked Linux/macOS/Windows builds, deterministic checksum closure, keyless signed provenance, and independent verification instructions;
- all canonical v0.x evidence and immutable v0.1 release truth.

## Future authority boundary

No later roadmap item or specification becomes active implicitly from Spec 004 completion. Future implementation requires a new canonical specification derived from live repository truth.

A public v1 tag, draft release, or published release is not authorized by Spec 004 and must not be inferred from `COMPLETE_CANONICAL`. That irreversible publication action requires separate explicit canonical authority.
