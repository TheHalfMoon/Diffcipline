# Execution frontier — Spec 004

Live GitHub/repository truth overrides this snapshot.

## Canonical baseline

Spec 003 is `COMPLETE_CANONICAL` at `d09757237560e0963c2eed8ac49eefcae378f780`; its accepted benchmark and limitations remain frozen.

Spec 004 planning/T403 is canonical at `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`.

Stable proof schema/T416 is canonical at `fd42970ccf868c5a808b9b3bd03f26c27b7c9161` after exact post-merge `ci` `33356644286`, `skills-compat` `33356644238`, and `release` `33356644296` succeeded.

Enterprise policy/T427 is canonical at `f0198395f0a141048b272bfd495f585fb76f6011` after PR #58 exact head `7ae53bfde368287a3a780fb591e7a3d21166856f` passed `ci` `33357573607` and `release` `33357573613`, then exact post-merge `ci` `33357739486` and `release` `33357739507` succeeded. The trusted canonical release run also created and verified signed Sigstore provenance over the locked three-platform candidate artifacts.

## Preserved capability

- dependency-free Rust CLI and existing exit semantics;
- stable proof schema `diffcipline.proof/v1` / `1.0`;
- repository policy version 1 when enterprise mode is absent;
- explicit local enterprise policy with monotonic layering and stable provenance;
- shared `diffcipline` and `diffcipline-review` Agent Skills;
- six-client installer qualification already present in `skills-compat`;
- locked native release builds, SHA-256 aggregation, and trusted-push GitHub/Sigstore provenance;
- all canonical v0.x evidence.

## Immediate frontier — Phase D

T430–T435 are authorized now that T427 is canonical:

1. publish a generic Agent Skills installation/portability contract;
2. preserve one canonical behavioral copy of each skill across clients;
3. requalify Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI from the exact candidate head;
4. add a generic layout/content qualification independent of one named client;
5. document platform-neutral CLI/skill boundaries and limitations;
6. merge and verify the portability unit canonically before relying on it for integrated closeout.

Do not create client-specific behavioral forks. Thin installer/layout adapters may differ only where client filesystem conventions require it.

## Stop conditions

Stop rather than weaken governance if canonical `main` moves unexpectedly, required exact-head/post-merge gates fail or disappear, a valid review finding remains unresolved, a client requires divergent core skill text, qualification cannot prove exact-head installation/discovery, or later release work requires long-lived signing credentials.

No public v1 tag/release is authorized by Phase D.
