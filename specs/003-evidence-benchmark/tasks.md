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
- [ ] T252 Execute baseline and eligible comparison-skill arms in canonical order.
- [ ] T253 Execute the Diffcipline arm under the identical executor contract.
- [ ] T254 Validate complete artifacts, matching base commits, runtime/treatment digests, and explicit exclusions.
- [ ] T255 Freeze the accepted experiment revision and raw evidence without selective reruns or filtering.

## Phase G — Publication and canonical closeout

- [ ] T260 Publish raw evidence, manifest/checksums, and exact provenance.
- [ ] T261 Publish a report stratified by executor/treatment with correctness, regressions, churn, verification, time, failures, exclusions, and unavailable metrics.
- [ ] T262 Update README only with claims supported by the accepted experiment.
- [ ] T263 Pass exact-head repository, benchmark qualification, skills-compatibility, and release-candidate gates on the final v0.3 candidate.
- [ ] T264 Merge final v0.3 evidence and verify exact post-merge gates.
- [ ] T265 Record `COMPLETE_CANONICAL` only after T264 is machine-observed and the completion record itself becomes canonical.

## Ordering

T203 gates implementation. T215 gates adapter work. T225 gates matrix work. T235 gates reproducibility qualification. T245 gates real comparative execution. T255 gates publication. T265 is terminal and cannot be pre-recorded.
