# Tasks — 004 Universal Engineering Governor

## Phase A — Canonical planning

- [x] T400 Derive the v1 capability contract from the canonical README and completed v0.x truth.
- [x] T401 Define compatibility, preservation, non-goals, and irreversible release boundaries.
- [x] T402 Define ordered implementation and qualification phases.
- [x] T403 Merge Spec 004 planning authority to canonical `main` and verify exact post-merge gates.

T403 exact evidence:

- planning PR #56 exact head `cb590fde5dc3bf76abee1ec3bd8b512607d63dcf` passed `ci` `33302675371`, `skills-compat` `33302675367`, and `release` `33302675373`;
- expected-head squash merge produced canonical `df9c0216723d3e241b6cea99bfe58c6212c1cd6a`;
- exact post-merge `ci` `33302752212`, `skills-compat` `33302752218`, and `release` `33302752209` all completed `SUCCESS`.

## Phase B — Stable proof schema

- [x] T410 Define repository-versioned proof schema major version 1.
- [x] T411 Emit explicit schema identity/version from `check --json`.
- [x] T412 Preserve existing proof meanings and exit-code semantics.
- [x] T413 Add policy-mode and policy-source provenance fields required by v1.
- [x] T414 Add deterministic schema/output contract tests and invalid-schema guard coverage.
- [x] T415 Document compatibility rules for schema major version 1.
- [x] T416 Merge and verify the stable-schema unit canonically.

T416 exact evidence:

- PR #57 final exact head `11ffd2f7b05d2012e26cad1726b603c93e3ca39d` passed `ci` `33303429558`, `skills-compat` `33303429551`, and `release` `33303429569`;
- expected-head squash merge produced canonical `fd42970ccf868c5a808b9b3bd03f26c27b7c9161`;
- exact post-merge `ci` `33356644286`, `skills-compat` `33356644238`, and `release` `33356644296` all completed `SUCCESS`.

## Phase C — Enterprise policy mode

- [x] T420 Add explicit local enterprise-policy CLI input with no network discovery.
- [x] T421 Enforce stricter numeric limits across enterprise and repository layers.
- [x] T422 Enforce stricter dependency/lockfile/untracked decisions across layers.
- [x] T423 Enforce cumulative forbidden surfaces and every non-empty expected-file contract.
- [x] T424 Enforce cumulative deterministic verification commands and risk profiles.
- [x] T425 Fail closed on malformed, unsupported, missing, or weakening layered policy states.
- [x] T426 Expose enterprise-policy activation and source provenance in proof output.
- [x] T427 Merge and verify enterprise policy mode canonically.

T427 exact evidence:

- PR #58 final exact head `7ae53bfde368287a3a780fb591e7a3d21166856f` stayed within repository policy at 3 files and +400/-1;
- exact-head `ci` `33357573607` and `release` `33357573613` completed `SUCCESS`;
- expected-head squash merge produced canonical `f0198395f0a141048b272bfd495f585fb76f6011`;
- exact post-merge `ci` `33357739486` and `release` `33357739507` completed `SUCCESS`.

## Phase D — Broad agent portability

- [x] T430 Publish a generic Agent Skills installation/portability contract.
- [x] T431 Preserve one canonical `diffcipline` and `diffcipline-review` behavior across agents.
- [x] T432 Qualify Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI from exact heads.
- [x] T433 Add a generic layout/content qualification independent of one named client.
- [x] T434 Document platform-neutral CLI/skill boundaries and limitations.
- [x] T435 Merge and verify broad portability canonically.

T435 exact evidence:

- PR #60 final exact head `5d8192bb25e3ea62224ea38ac7a090edf3da25be` passed `ci` `33360432458` and `skills-compat` `33360432460`;
- expected-head squash merge produced canonical `066c0138e5e2970781cc91abba38797654f92c77`;
- exact post-merge `skills-compat` `33360553460` and `ci` `33360553459` completed `SUCCESS`.

## Phase E — Signed release-artifact contract

- [x] T440 Define the v1 signed release-candidate artifact set and provenance contract.
- [x] T441 Prove locked native builds for Linux, macOS, and Windows.
- [x] T442 Prove deterministic SHA-256 manifest closure over all native binaries.
- [x] T443 Prove GitHub/Sigstore provenance without repository-stored long-lived signing keys.
- [x] T444 Verify attestation subjects against exact candidate binaries on trusted canonical pushes.
- [x] T445 Document independent checksum and provenance verification.
- [x] T446 Keep public tag/release creation outside the capability milestone unless separately authorized.
- [x] T447 Merge and verify the signed release-artifact capability canonically.

T447 exact evidence:

- PR #62 exact head `4dbc751e09808999df61383092c2720f289c34d8` changed only `docs/RELEASES.md` at +89/-0;
- exact-head `ci` `33361112731` and `release` `33361112742` completed `SUCCESS`;
- expected-head squash merge produced canonical `b20b2671c75c5076fcf66397ee4a3f7c308bdfba`;
- exact post-merge `ci` `33361219139` and `release` `33361219144` completed `SUCCESS`;
- canonical `release` `33361219144` built the locked native binaries, verified `SHA256SUMS`, created signed Sigstore provenance through GitHub OIDC, preserved the attestation bundle, and verified every native binary subject;
- `stage GitHub release draft` was intentionally skipped because no v1 tag or public release is authorized.

## Phase F — Integrated qualification and closeout

- [x] T450 Update README and contract docs only with implemented v1 capabilities.
- [x] T451 Pass exact-head `ci`, `skills-compat`, `release`, and any dedicated v1 qualification gate on one final candidate.
- [x] T452 Reconcile valid reviews/threads and reverify canonical `main` before merge.
- [x] T453 Merge the final v1 capability candidate with an expected-head guard.
- [x] T454 Verify exact post-merge repository, portability, schema/policy, and signed-release evidence.
- [x] T455 Record `COMPLETE_CANONICAL` separately only after T454 is machine-observed and the terminal record itself becomes canonical.

T450–T454 exact evidence:

- PR #64 final exact head `4e3e2d25754e72f1a0becd953a8f91405f955f01` changed only `README.md`, `docs/INSTALLATION.md`, and `docs/RELEASES.md` at 3 files and +25/-1;
- exact-head `ci` `33365761812`, `skills-compat` `33365761816`, and `release` `33365761900` all completed `SUCCESS` on that same head;
- the exact-head portability run passed the generic Agent Skills contract and all six named clients; the release run passed all three locked native builds and deterministic checksum closure, while provenance signing and release drafting were correctly skipped on the pull-request event;
- no submitted reviews or inline review threads remained; Qodo reported only a billing pause and CodeRabbit reported only that automatic review was skipped;
- canonical `main` remained exactly `54ef361f817846e35fbe238806d0a09d84e09e0b` immediately before merge;
- expected-head squash merge of PR #64 produced canonical `2ff687c038f72a3b747e85ad907d2400955cb649`;
- exact post-merge `ci` `33365950241`, `skills-compat` `33365950200`, and `release` `33365950214` all completed `SUCCESS` on `2ff687c038f72a3b747e85ad907d2400955cb649`;
- post-merge CI passed Rust and dogfood gates across Linux, macOS, and Windows plus proof-v1 schema validation on Linux;
- post-merge portability passed the generic contract and Claude Code, Codex, Cursor, OpenCode, GitHub Copilot, and Gemini CLI;
- post-merge release built and packaged all three locked native binaries, generated and verified the deterministic SHA-256 manifest, created signed Sigstore provenance, preserved the attestation bundle, verified every native binary subject, and intentionally skipped `stage GitHub release draft` because no public v1 tag exists.

T455 terminal record:

- T454 was machine-observed before this terminal record was authored;
- this record closes the Spec 004 task ledger and records `COMPLETE_CANONICAL` with no active implementation frontier;
- the completion claim is candidate-only until this terminal record itself is merged to canonical `main` and its required post-merge `ci`, `skills-compat`, and `release` gates succeed on the resulting canonical SHA;
- no public v1 tag or release is created or authorized by this record.

## Ordering

T403 gated all implementation. T416 gated enterprise policy work. T427 gated final portability/release integration. T447 gated integrated closeout. T455 is terminal.
