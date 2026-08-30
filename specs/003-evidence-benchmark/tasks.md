# Tasks — 003 Evidence Benchmark

## Phase A — Canonical planning

- [x] T200 Define the v0.3 evidence-benchmark contract from canonical roadmap and benchmark truth.
- [x] T201 Define executor-profile, treatment-arm, adapter, evidence, and reporting invariants.
- [x] T202 Define implementation phases, experiment authorization boundary, and fail-closed stop conditions.
- [x] T203 Merge Spec 003 authority to canonical `main` with exact-head and post-merge gates.

## Phase B — Executor/profile schema

- [x] T210 Add a versioned v0.3 experiment configuration separate from frozen v0.1 `run-config.json`.
- [x] T211 Define executor profiles independently from treatment arms.
- [x] T212 Validate IDs, adapter kinds, treatment references, revisions/digests, and resource limits fail-closed.
- [x] T213 Preserve explicit network/Git-push/workspace restrictions in executor profiles.
- [x] T214 Add deterministic config normalization/serialization for evidence manifests.
- [x] T215 Add unit coverage for valid and invalid profile/treatment configurations.

## Phase C — Adapter boundary

- [x] T220 Remove hardcoded `local_agent.py` selection from arm orchestration.
- [x] T221 Define the process-level executor adapter contract.
- [x] T222 Add a reference adapter for the existing local OpenAI-compatible tool loop.
- [x] T223 Add a deterministic contract-test adapter that is excluded from comparative evidence.
- [x] T224 Preserve timeout, exit, stdout, stderr, transcript, and treatment-input evidence across adapters.
- [x] T225 Add adapter contract and failure-path tests.

## Phase D — Matrix orchestration and evidence

- [x] T230 Add deterministic `executor × treatment × fixture` matrix expansion.
- [x] T231 Enforce matched task/revision/model/permissions/limits across treatment arms for each executor.
- [x] T232 Produce attempt-aware per-run metadata without overwriting prior attempts.
- [x] T233 Produce an experiment manifest covering included, failed, timed-out, and excluded runs.
- [x] T234 Keep objective scoring independent from executor implementation.
- [x] T235 Add matrix, matching-invariant, manifest, and scorer-boundary tests.

## Phase E — Reproducibility qualification

- [x] T240 Add secret-free harness qualification using deterministic fixtures/adapters.
- [x] T241 Add CI validation for configuration, adapters, matrix, and evidence completeness.
- [x] T242 Prove the reference qualification path requires no private credentials.
- [x] T243 Preserve frozen v0.1 evidence and scorer/fixture history.
- [x] T244 Define an explicit real-experiment workflow path that does not run on ordinary pull requests.
- [x] T245 Merge the qualified public harness before authorizing comparative execution.

## Phase F — Public reference experiment

- [x] T250 Pin one secret-free reference executor/model/runtime configuration and all treatment revisions/digests.
- [x] T251 Verify identical task revisions, permissions, prompt suffix, timeouts, and resource limits across arms.
- [x] T252 Execute baseline and eligible comparison-skill arms in canonical order.
- [x] T253 Execute the Diffcipline arm under the identical executor contract.
- [x] T254 Validate complete artifacts, matching base commits, runtime/treatment digests, and explicit exclusions.
- [x] T255 Freeze the accepted experiment revision and raw evidence without selective reruns or filtering.

T252–T255 exact evidence:

- canonical target `234f007dc8765f7b7649ada7d7d1d00ae4c12538` was reserved once by `benchmark-v0.3-reference` run `33269484561` (#16) after exact qualification run `33269349342` was verified;
- the workflow executed one 24-row attempt in canonical order `baseline -> karpathy -> ponytail -> diffcipline` and completed `SUCCESS` without a rerun;
- exact results artifact `9720290597`, name `v0.3-reference-experiment-234f007dc8765f7b7649ada7d7d1d00ae4c12538`, has GitHub-recorded digest `sha256:dcad221a52e110a34198109ac31bfe164e2ac47610e78b83b9d98f17102c3218`; the independently downloaded artifact matched that digest byte-for-byte during T254 inspection;
- exact reservation artifact `9719653684` has digest `sha256:f63e381cb199a064b875cdaf25eba614f3ea9b38048cd20bfbc18a689d6e28b7` and records `status=RESERVED_ONCE` for the same target;
- the accepted manifest contains 24 rows: 12 `included`, 12 `failed`, 0 `timed_out`, and 0 `excluded`; failures are retained and no failed or losing task was selectively rerun;
- every required run bundle is present; base commits and comparison-contract digests match across all treatments for each fixture; runtime/model/treatment/sandbox identities match the pinned contract; qualification and containment both record `PASS`, with no private credentials required or exposed;
- the attempt-local checksum list contains 463 pre-packaging entries; 295 corresponding files are present in the Actions artifact and all 295 match, while 168 omitted entries are hidden `.git` metadata from duplicate ephemeral `work/` repositories. No required transcript, stdout, stderr, score, patch, status, metadata, resulting workspace, reservation, qualification, validation, or provenance record is missing;
- the frozen scorer was not changed after observing the run. It counted test-generated `__pycache__` files as changed/unrelated/protected paths, making scorer-pass `0/6` for every arm while task correctness remained `1/6` for every arm. This limitation is preserved in the publication instead of repaired post hoc.

## Phase G — Publication and canonical closeout

- [x] T260 Publish raw evidence, manifest/checksums, and exact provenance.
- [x] T261 Publish a report stratified by executor/treatment with correctness, regressions, churn, verification, time, failures, exclusions, and unavailable metrics.
- [x] T262 Update README only with claims supported by the accepted experiment.
- [x] T263 Pass exact-head repository, benchmark qualification, skills-compatibility, and release-candidate gates on the final v0.3 candidate.
- [x] T264 Merge final v0.3 evidence and verify exact post-merge gates.
- [x] T265 Record `COMPLETE_CANONICAL` only after T264 is machine-observed and the completion record itself becomes canonical.

T260–T265 exact closeout evidence:

- publication records are canonical under `benchmarks/results/v0.3/`; README claims only the accepted negative findings and disclosed limitations;
- PR #54 final exact head `e5e3b2675af2af55426229dc4afbbb349db956d8` independently passed `benchmark-v0.3-qualification` run `33301772574`, `skills-compat` run `33301772570`, `release` run `33301772566`, and `ci` run `33301772564`, all `SUCCESS` on that same head;
- the same final head passed guarded `benchmark-v0.3-reference` validation run `33301772610` plus v0.1 tag/stage/immutable-release validation runs `33301772581`, `33301772606`, and `33301772565`; no second comparative experiment was executed;
- PR #54 had no submitted reviews and no inline review threads. Qodo billing and CodeRabbit review-skip notices contained no code finding;
- canonical `main` remained at exact PR base `234f007dc8765f7b7649ada7d7d1d00ae4c12538` until expected-head squash merge of exact head `e5e3b2675af2af55426229dc4afbbb349db956d8`;
- PR #54 merged as canonical commit `d59cc6ec570c894713d6bf32aa0b4af9d60d7c38`;
- exact post-merge push `ci` run `33301846572`: `SUCCESS` across Rust and Diffcipline proof-gate jobs on Ubuntu, macOS, and Windows;
- exact post-merge `benchmark-v0.3-qualification` run `33301846507`: `SUCCESS`;
- exact post-merge `skills-compat` run `33301846603`: `SUCCESS`;
- exact post-merge `release` run `33301846610`: `SUCCESS`, including native builds, checksum generation/verification, and signed Sigstore provenance; the GitHub release draft job remained intentionally skipped because no release tag was authorized;
- T264 was therefore machine-observed on canonical `main` before this terminal completion record was authored;
- this completion record marks T265 and Spec 003 `COMPLETE_CANONICAL`, but that terminal status is effective externally only after this completion record itself is merged to canonical `main` and its own required post-merge gates are machine-observed successful.

## Ordering

T203 gated implementation. T215 gated adapter work. T225 gated matrix work. T235 gated reproducibility qualification. T245 gated real comparative execution. T255 gated publication. T264 was machine-observed before T265 was authored. No later task exists in Spec 003.
