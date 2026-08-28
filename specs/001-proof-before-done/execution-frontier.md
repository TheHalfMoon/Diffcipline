# Execution frontier — Spec 001

This document is the canonical continuation handoff for `001-proof-before-done`.

Live GitHub/repository truth always overrides this snapshot. Re-verify `main`, open pull requests, Actions runs, and the files in the read order below before making changes.

## Canonical read order

1. `AGENTS.md`
2. `specs/CURRENT.md`
3. `specs/001-proof-before-done/spec.md`
4. `specs/001-proof-before-done/plan.md`
5. `specs/001-proof-before-done/tasks.md`
6. this file
7. `benchmarks/PROTOCOL.md`
8. `benchmarks/run-config.json`
9. `.github/workflows/benchmark-arms.yml`

## Last verified canonical state

Last verified canonical `main` before this handoff documentation branch:

`c71d3f81016ae6bc1d8516b47d1b3c5cb7258e45`

Canonical tree:

`c550eff41ad72cbd1891acbca3aef80826eaf7ba`

PR #16 was squash-merged to that commit after exact-head repository CI passed. The repository has completed T001–T051. T052–T055 remain open.

The benchmark fixture/scorer/preparer boundary remains frozen at:

`4f796058bddd840be31d3fbf7d74b34a5403c49c`

Do not modify the frozen fixture corpus, `benchmarks/harness/prepare_fixture.py`, or `benchmarks/harness/score_run.py` after benchmark execution has begun. If a genuine defect is discovered, stop, document it, invalidate affected runs, repair through review, establish a new frozen revision, and restart every affected arm under matching conditions.

## Excluded infrastructure preflights

The following runs are **not benchmark evidence**. No benchmark task executed in any of them.

| Run | Canonical commit | Result | Task arms |
| --- | --- | --- | --- |
| `benchmark-arms` #1 / `33177348082` | `f5f17b9d0fa025bbed436075c462ce48a5766151` | `gpt-5.3-codex` explicit model unavailable | baseline, Karpathy, Ponytail, Diffcipline all skipped |
| `benchmark-arms` #2 / `33177729891` | `d20f6b615fc9c1285b01b74377aa6e53e7fa081a` | `claude-sonnet-4.6` explicit model unavailable | all skipped |
| `benchmark-arms` #3 / `33178142084` | `c71d3f81016ae6bc1d8516b47d1b3c5cb7258e45` | every predeclared explicit hosted model unavailable | all skipped |

Run #3 verified the frozen corpus, pinned Copilot CLI `v1.0.81` checksum, pinned treatment skill blobs, and `GITHUB_TOKEN` permission `CopilotRequests: write` before probing the model list. Nine explicit model IDs were rejected as unavailable. `auto` was intentionally refused because different arms must not silently receive different models.

Current benchmark task execution count: **0**.

## Current blocker

`T052 BLOCKED_HOSTED_MODEL_ENTITLEMENT`.

The GitHub-hosted Copilot Actions path cannot currently provide any of the predeclared explicit models for this repository/account. This is an infrastructure/entitlement blocker, not a benchmark result.

Do not:

- use Copilot `auto` selection;
- count a model preflight as a benchmark task;
- change task fixtures or scorer behavior to make execution easier;
- publish comparative claims from partial or unmatched arms;
- hide excluded runs.

## Authorized continuation plan

### Stage 1 — Establish one pinned local model runtime

Move the benchmark execution path to a local, reproducible provider inside GitHub Actions, with no hosted model entitlement dependency. Ollama or an equivalent OpenAI-compatible local runtime is acceptable if it satisfies every gate below.

Before any benchmark task runs:

1. Pin the runtime version or image to an immutable release identifier and checksum/digest.
2. Select one exact open-weight model **without inspecting benchmark task outcomes**.
3. Record the exact model artifact identifier and cryptographic digest where the distribution format permits it.
4. Require a license compatible with public reproducible benchmarking.
5. Require the model/runtime to fit the GitHub-hosted runner resource envelope with a documented safety margin.
6. Require the interface needed by the benchmark harness; if tool calling is required by the chosen agent runtime, prove it in preflight.
7. Run a harmless model preflight before T052 and preserve its output as infrastructure evidence.
8. Fail closed if the exact runtime/model cannot be reproduced. Do not fall back to remote `auto` selection.

A small coding-capable local model may be used for v0.1. The benchmark measures the treatment effect under matched conditions; it does not require a frontier model. Model selection must be frozen before the first benchmark task.

### Stage 2 — Migrate the harness without changing the experiment

Use a dedicated feature branch and pull request. Keep these experiment surfaces unchanged unless a separately documented pre-execution defect requires repair:

- fixture bytes and manifests;
- task prompts;
- scorer and preparer behavior;
- treatment skill revisions/blobs;
- arm order and identity;
- prompt suffix;
- network prohibition during task execution;
- no commit/push rule;
- per-task timeout, unless runner feasibility requires a pre-execution change applied identically to all arms.

The harness migration may change only what is necessary to replace hosted model transport with the pinned local transport and to capture runtime/model provenance.

Exact-head normal CI and any benchmark infrastructure validation must pass before merge. Benchmark task execution starts only from canonical `main` after that merge.

### Stage 3 — Execute T052–T054 in protocol order

Run arms in this order and do not skip ahead:

1. **T052 baseline** — six frozen tasks, no treatment skill.
2. Verify that all six baseline result bundles exist, are parseable, match the frozen task IDs, and contain the required raw transcript/patch/test/scoring evidence.
3. **T053 Karpathy comparison** — same six tasks, exact pinned Karpathy skill blob.
4. **T053 Ponytail comparison** — same six tasks, exact pinned Ponytail skill blob.
5. Verify both comparison bundles before proceeding.
6. **T054 Diffcipline** — same six tasks, exact pinned Diffcipline skill blob.

Every arm must use the exact same:

- model artifact;
- model/runtime configuration;
- runner class;
- task corpus;
- timeout policy;
- tool/network policy;
- scorer;
- prompt suffix, except for the treatment skill itself.

Record failures, timeouts, abstentions, and malformed outputs as outcomes according to the published protocol. Do not silently retry individual tasks to improve results. Any permitted whole-experiment retry policy must be declared before the first valid T052 task run.

### Stage 4 — T055 durable publication

After all valid arms finish, create a publication branch containing durable benchmark evidence under a versioned results directory such as:

`benchmarks/results/v0.1/`

Publish at minimum:

- execution manifest with canonical repository revision;
- runtime version/digest and exact model identity/digest;
- treatment repository revisions and blob SHAs;
- task IDs and frozen fixture revision;
- raw model/agent transcripts where license and size permit;
- produced patches/diffs;
- test outputs and exit codes;
- per-task scorer JSON;
- aggregate tables;
- token/cost/time metrics when actually available, otherwise explicitly `NOT AVAILABLE`;
- excluded infrastructure runs #1–#3 and their reasons;
- limitations and threats to validity;
- checksums for published raw artifacts.

Do not publish only an aggregate score. Preserve losing metrics and failed runs.

If raw artifacts are too large for ordinary Git history, publish them as immutable GitHub Release assets and commit the manifest, checksums, asset references, and summaries to the repository. Do not rely only on expiring Actions artifacts.

### Stage 5 — v0.1 closeout and release

Only after T055 is canonical:

1. Update `README.md` with benchmark claims that are exactly supported by the published evidence. If Diffcipline loses a metric, say so.
2. Update `CHANGELOG.md`, `specs/CURRENT.md`, and `tasks.md`.
3. Re-run canonical Rust, Diffcipline, skill compatibility, benchmark evidence, and release-candidate gates required by the repository.
4. Create the matching `v0.1.0` release tag only from an exact verified canonical `main` commit.
5. Verify the tag-triggered release workflow, checksums, provenance/attestations, and published binaries.
6. Claim `v0.1.0 COMPLETE_CANONICAL` only after post-tag evidence is available.

## Stop conditions

Stop and record a blocker instead of weakening the experiment if any of these occurs:

- no reproducible local model fits the available runner;
- model/runtime artifact identity cannot be pinned sufficiently for reproduction;
- the harness requires changing frozen benchmark semantics after a valid task run exists;
- a provider/runtime requires credentials or authority that are not available;
- raw evidence cannot be published under applicable licenses/security constraints.

Repository truth and proof-before-done rules remain authoritative over the desire to finish quickly.
