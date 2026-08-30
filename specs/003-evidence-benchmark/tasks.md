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
- every required run bundle is present; base commits and comparison-contract digests match across all treatments for each fixture; runtime/model/treatment/sandbox identities match the pinned contract; qualification and containment both record `PASS`, no private credentials required or exposed;
- the attempt-local checksum list contains 463 pre-packaging entries; 295 corresponding files are present in the Actions artifact and all 295 match, while 168 omitted entries are hidden `.git` metadata from duplicate ephemeral `work/` repositories. No required transcript, stdout, stderr, score, patch, status, metadata, resulting workspace, reservation, qualification, validation, or provenance record is missing;
- the frozen scorer was not changed after observing the run. It counted test-generated `__pycache__` files as changed/unrelated/protected paths, making scorer-pass `0/6` for every arm while task correctness remained `1/6` for every arm. This limitation is preserved in the publication instead of repaired post hoc.

## Phase G — Publication and canonical closeout

- [x] T260 Publish raw evidence, manifest/checksums, and exact provenance.
- [x] T261 Publish a report stratified by executor/treatment with correctness, regressions, churn, verification, time, failures, exclusions, and unavailable metrics.
- [x] T262 Update README only with claims supported by the accepted experiment.
- [ ] T263 Pass exact-head repository, benchmark qualification, skills-compatibility, and release-candidate gates on the final v0.3 candidate.
- [ ] T264 Merge final v0.3 evidence and verify exact post-merge gates.
- [ ] T265 Record `COMPLETE_CANONICAL` only after T264 is machine-observed and the completion record itself becomes canonical.

T260–T262 publication candidate evidence:

- `benchmarks/results/v0.3/MANIFEST.json` records the accepted run/artifact identities, 24-row validation, exact base commits, treatment SHA-256 values, failures, unavailable metrics, scorer limitation, and checksum audit;
- `benchmarks/results/v0.3/RUNTIME-PROVENANCE.json` publishes the exact executor/model/runtime/sandbox/treatment contract and harness hashes from the accepted artifact;
- `benchmarks/results/v0.3/CHECKSUMS.txt` records canonical artifact, reservation, experiment-manifest, and runtime-provenance digests as explicit provenance identifiers without pretending that an absent raw binary can be verified as a repository-local file;
- `benchmarks/results/v0.3/REPORT.md` publishes the negative result, all treatment-level metrics, failures, limitations, and the exact raw Actions artifact identity/digest. Raw artifact `9720290597` remains the unfiltered publication surface created by the canonical workflow; its finite GitHub retention is disclosed rather than hidden;
- README claims only the observed four-way `1/6` correctness tie, the contaminated `0/6` scorer-pass signal, source-text no-edit finding, failure counts, timing, and the no-treatment-effect conclusion supported by the accepted experiment;
- T263 is intentionally not claimed until all required workflows succeed on the exact final candidate head.

## Ordering

T203 gates implementation. T215 gates adapter work. T225 gates matrix work. T235 gates reproducibility qualification. T245 gates real comparative execution. T255 gates publication. T265 is terminal and cannot be pre-recorded.
