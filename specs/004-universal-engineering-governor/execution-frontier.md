# Execution frontier — Spec 004

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 003 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`; its accepted benchmark and limitations remain frozen.

Spec 004 planning/T403 is canonical at `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`.

Stable proof schema/T416 is canonical at `fd42970ccf868c5a808b9b3bd03f26c27b7c9161` after exact post-merge `ci` `33356644286`, `skills-compat` `33356644238`, and `release` `33356644296` succeeded.

Enterprise policy/T427 is canonical at `f0198395f0a141048b272bfd495f585fb76f6011` after PR #58 exact head `7ae53bfde368287a3a780fb591e7a3d21166856f` passed `ci` `33357573607` and `release` `33357573613`, then exact post-merge `ci` `33357739486` and `release` `33357739507` succeeded. The trusted canonical release run also created and verified signed Sigstore provenance over the locked three-platform candidate artifacts.

Broad portability/T435 is canonical at `066c0138e5e2970781cc91abba38797654f92c77`. PR #60 exact head `5d8192bb25e3ea62224ea38ac7a090edf3da25be` passed `ci` `33360432458` and `skills-compat` `33360432460`; exact post-merge `ci` `33360553459` and `skills-compat` `33360553460` also succeeded. The portability gate proves the generic layout/content contract and byte-identical installation of both canonical skills for all six named clients.

## Preserved capability

- dependency-free Rust CLI and existing exit semantics;
- stable proof schema `diffcipline.proof/v1` / `1.0`;
- repository policy version 1 when enterprise mode is absent;
- explicit local enterprise policy with monotonic layering and stable provenance;
- exactly one canonical behavioral source for `diffcipline` and `diffcipline-review`;
- generic Agent Skills portability contract plus exact-head qualification for Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI;
- locked native release builds, SHA-256 aggregation, and trusted-push GitHub/Sigstore provenance;
- all canonical v0.x evidence.

## Immediate frontier — Phase E

T440–T447 are authorized after the portability record becomes canonical:

1. define the exact v1 signed release-candidate artifact set and trust/provenance contract;
2. preserve locked native builds for Linux, macOS, and Windows from exact checkouts;
3. preserve deterministic SHA-256 closure over exactly the three host-native binaries;
4. preserve GitHub/Sigstore keyless provenance without repository-stored long-lived signing keys;
5. verify every attested binary subject on trusted canonical pushes;
6. document independent checksum and provenance verification;
7. keep public tag/release creation outside the v1 capability milestone unless separately authorized;
8. merge and verify the release-artifact contract canonically before integrated closeout.

The existing `.github/workflows/release.yml` already implements the required build/checksum/attestation mechanics. Phase E should promote and explicitly qualify that machinery rather than replace it without evidence of a gap.

## Stop conditions

Stop rather than weaken governance if canonical `main` moves unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, release candidate closure no longer covers exactly the three native binaries, provenance requires long-lived repository signing credentials, attestation subjects are not verified, or public tag/release creation would occur without separate authority.

No public v1 tag/release is authorized by Phase E.
