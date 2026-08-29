# Plan — 003 Evidence Benchmark

## Delivery principles

- preserve the frozen v0.1 fixture/scorer/result boundary;
- separate executor identity from treatment identity before expanding the matrix;
- keep benchmark orchestration and schemas Python standard-library only;
- qualify each unit on exact GitHub heads before canonical merge;
- publish failures and exclusions instead of filtering them away;
- prefer a small explicit schema over plugin frameworks or implicit discovery.

## Phase A — Canonical planning

Establish this specification, task order, and execution frontier from the README roadmap and current benchmark truth. No harness implementation begins before the planning authority is canonical.

## Phase B — Executor/profile schema

Introduce a versioned public experiment configuration that can describe multiple executor profiles independently of treatment arms. Validation must fail closed on missing IDs, duplicate IDs, unsupported adapter kinds, malformed treatment references, or unmatched resource constraints.

Keep the existing v0.1 `run-config.json` frozen as historical experiment evidence. v0.3 configuration uses a new path/schema rather than rewriting the old experiment definition.

## Phase C — Adapter boundary

Refactor orchestration so `run_arm.py` no longer hardcodes `local_agent.py`. Add a narrow adapter invocation contract with a reference adapter for the existing repository-local OpenAI-compatible tool loop.

Provide a deterministic test adapter used only for harness contract tests. It may mutate disposable fixture workspaces under explicit test instructions, but it is not a benchmark treatment result and must never be reported as comparative model evidence.

## Phase D — Matrix orchestration and evidence

Add an experiment runner that expands `executor × treatment × fixture` deterministically, preserves the same task/revision/limits across treatment arms for one executor, invokes the existing objective scorer, and writes per-run evidence plus an experiment manifest.

The manifest must distinguish included, failed, timed-out, and excluded runs. Reruns are new attempts with lineage; they do not overwrite earlier attempts.

## Phase E — Reproducibility qualification

Add fixture-sized contract tests and CI qualification for:

- profile/config validation;
- adapter invocation and timeout/exit preservation;
- deterministic matrix expansion;
- arm matching invariants;
- evidence manifest completeness;
- no private credentials required for the reference qualification path;
- no scorer dependency on executor implementation.

Do not run the expensive comparative experiment on ordinary pull requests. CI may use deterministic contract fixtures/stubs; real experiment execution requires an explicit canonical workflow path and exact revision evidence.

## Phase F — Public reference experiment

Define one fully pinned, secret-free reference executor using the existing local model/runtime lineage or another equivalently reproducible public configuration. Run baseline, eligible comparison skills, and Diffcipline with identical executor/model/task/revision/limits.

A candidate experiment is valid only if every arm has complete artifacts, base commits match per task, runtime/treatment digests are recorded, exclusions are explicit, and the objective scorer boundary is unchanged or separately justified before execution.

## Phase G — Publication and canonical closeout

Publish raw evidence, manifest/checksums, a report with per-executor/per-treatment tables, failures, exclusions, unavailable metrics, and limitations. Update README only with findings actually supported by the canonical experiment.

Final closeout requires exact-head repository gates, benchmark qualification gates, review reconciliation, canonical merge, post-merge verification, and a separate final evidence record before `COMPLETE_CANONICAL` is claimed.

## Ordering

A → B → C → D → E → F → G.

The reference experiment cannot begin until the harness/config/evidence contract is canonical. Publication cannot begin until the exact experiment is validated. No later phase may retroactively modify earlier benchmark inputs to improve results.
