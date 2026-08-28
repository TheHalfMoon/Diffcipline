# Implementation plan — 001 Proof Before Done

## Architecture

The v0.1 core has two independent layers:

1. **Behavioral layer** — `skills/diffcipline/SKILL.md` and `skills/diffcipline-review/SKILL.md`.
2. **Evidence layer** — a dependency-free Rust CLI that reads Git and repository policy.

The skill can be used without the CLI. The CLI can inspect a repository without an LLM. Their combination creates the closed loop.

## CLI modules for v0.1

The initial implementation may remain in one source file until a second stable responsibility boundary emerges. Premature module splitting is explicitly avoided.

Responsibilities:
- command parsing;
- policy parsing;
- Git diff/status collection;
- dependency and lockfile classification;
- verification command execution;
- proof rendering in human and JSON formats.

## Security

Verification commands are repository-provided executable material. `check` is read-only by default. Commands execute only with `--run`. Documentation must tell users to review policy before running an untrusted repository.

## Compatibility

- Linux, macOS, and Windows through Rust standard library process APIs.
- Git is required.
- Shell execution uses `sh -lc` on Unix and `cmd /C` on Windows.

## Distribution and supply chain

The v0.1 distribution path is repository-native and evidence-first:

1. cross-platform repository CI;
2. GitHub Action proof gate;
3. compatible Agent Skills installation verification;
4. release-candidate binary builds for Linux, macOS, and Windows;
5. SHA-256 manifests and GitHub/Sigstore provenance;
6. tag publication only from an exact verified canonical `main` commit whose crate version matches the tag.

T040–T044 are complete. A final `v0.1.0` tag is intentionally deferred until the benchmark/publication closeout below is canonical.

## Benchmark plan

The benchmark is a public falsification mechanism, not a marketing score. `benchmarks/PROTOCOL.md` was published before comparative claims, and the six-task corpus/scorer/preparer boundary was frozen before model execution.

### Frozen experiment boundary

Frozen revision:

`4f796058bddd840be31d3fbf7d74b34a5403c49c`

The following surfaces must remain byte-stable once valid benchmark task execution begins unless a documented defect forces invalidation and a complete affected-arm restart:

- `benchmarks/fixtures/**`;
- `benchmarks/harness/prepare_fixture.py`;
- `benchmarks/harness/score_run.py`;
- task prompts and manifests;
- treatment skill revisions/blobs;
- scoring semantics.

### Hosted-model preflight outcome

The first three GitHub-hosted Copilot benchmark workflow runs failed safely before any benchmark task executed:

- run #1 (`33177348082`): explicit `gpt-5.3-codex` unavailable;
- run #2 (`33177729891`): explicit `claude-sonnet-4.6` unavailable;
- run #3 (`33178142084`): all nine predeclared explicit hosted model candidates unavailable.

All downstream arms were skipped. These are excluded infrastructure runs. They are not benchmark evidence and must be published as exclusions in T055.

`auto` selection is forbidden because matched arms require one exact model identity.

### Local reproducible runtime recovery

The next authorized benchmark implementation step is to replace only the hosted model transport with one pinned local runtime inside GitHub Actions.

Before T052 starts:

1. Choose and pin an immutable local serving runtime release/image plus checksum or digest.
2. Select one exact open-weight coding-capable model without observing benchmark task outcomes.
3. Record the model artifact identifier and digest where the distribution format permits it.
4. Confirm license compatibility for public reproducible benchmark evidence.
5. Confirm the model/runtime fits the GitHub-hosted runner resource envelope.
6. Prove the required inference/tool interface with a harmless preflight.
7. Preserve the runtime/model identity in a shared immutable workflow artifact or equivalent exact provenance record.
8. Fail closed if the exact model cannot be reproduced. Never fall back to remote `auto` selection.

The benchmark is intended to measure the treatment effect under matched conditions. A small local coding model is acceptable for v0.1 if it satisfies the reproducibility and execution gates; frontier-model status is not a requirement.

### Harness migration rules

Perform the local-runtime migration through a dedicated feature branch and PR. Change only transport/provenance code needed to invoke the pinned local model.

Keep constant across every arm:

- exact model artifact and inference configuration;
- runner class;
- fixture revision;
- task prompts;
- scorer/preparer;
- per-task timeout policy;
- network prohibition during task execution;
- no commit/push rule;
- prompt suffix;
- treatment skill blob for each named treatment.

Any resource-limit change required for local feasibility must happen before the first valid T052 task and apply identically to every arm.

Exact-head normal CI plus benchmark infrastructure validation must pass before the migration merges. Benchmark tasks run only from canonical `main` after that merge.

### Arm execution order

Execute and verify in this order:

1. **T052 — baseline**: six tasks with no treatment skill.
2. Validate all six result bundles and evidence completeness.
3. **T053 — Karpathy**: same tasks/conditions with the pinned Karpathy skill.
4. **T053 — Ponytail**: same tasks/conditions with the pinned Ponytail skill.
5. Validate both comparison bundles.
6. **T054 — Diffcipline**: same tasks/conditions with the pinned Diffcipline skill.

Do not silently retry individual tasks to improve outcomes. Timeouts, failures, malformed responses, and abstentions remain outcomes under the published protocol. Any whole-experiment retry policy must be declared before the first valid T052 task.

### T055 durable publication

Publish durable evidence under `benchmarks/results/v0.1/` or, for artifacts too large for ordinary Git history, as immutable GitHub Release assets referenced by a committed manifest and checksums.

Publication must contain at minimum:

- canonical repository revision and fixture revision;
- runtime version/digest;
- exact model artifact identity/digest;
- treatment repository revisions and blob SHAs;
- raw transcripts where license and size permit;
- produced patches/diffs;
- verification/test outputs and exit codes;
- per-task scorer JSON;
- aggregate tables;
- token/cost/time metrics when actually observed, otherwise explicit `NOT AVAILABLE`;
- excluded hosted-model runs #1–#3;
- limitations and threats to validity;
- checksums for raw published artifacts.

Never publish only a favorable aggregate. Preserve losing metrics and failed runs.

## v0.1 closeout

After T055 is canonical:

1. Update `README.md` with only evidence-supported benchmark claims, including losing metrics.
2. Update `CHANGELOG.md`, `specs/CURRENT.md`, and `tasks.md`.
3. Run all repository-required canonical CI, Diffcipline, skills compatibility, benchmark-evidence, and release-candidate gates.
4. Create `v0.1.0` only from the exact verified canonical `main` commit with matching crate version.
5. Verify the tag-triggered release workflow, binary checksums, signatures/provenance/attestations, and published assets.
6. Claim `v0.1.0 COMPLETE_CANONICAL` only after post-tag evidence exists.

The detailed continuation contract and blocker evidence are maintained in `execution-frontier.md`.

## Deferred decisions after v0.1

- stable JSON schema versioning;
- signed proof artifacts beyond the current release supply chain;
- richer GitHub Action annotation UX;
- expected-file proof contracts;
- risk-path inference;
- additional package managers;
- enterprise policy distribution;
- semantic/LLM proof judging in the CLI.
