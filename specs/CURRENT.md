# Current specification

Active: [`001-proof-before-done`](001-proof-before-done/spec.md)

Status: `BENCHMARK_EXECUTION_BLOCKED_HOSTED_MODEL_ENTITLEMENT`

## Canonical continuation

Read in this order before acting:

1. `AGENTS.md`
2. this file
3. `specs/001-proof-before-done/spec.md`
4. `specs/001-proof-before-done/plan.md`
5. `specs/001-proof-before-done/tasks.md`
6. `specs/001-proof-before-done/execution-frontier.md`
7. `benchmarks/PROTOCOL.md`
8. `benchmarks/run-config.json`
9. `.github/workflows/benchmark-arms.yml`

Live GitHub/repository truth overrides every recorded SHA below.

Last verified canonical `main` before the handoff documentation change:

`c71d3f81016ae6bc1d8516b47d1b3c5cb7258e45`

T001–T051 are complete. T052–T055 remain open.

The six-task benchmark corpus and scoring/preparation boundary are frozen at:

`4f796058bddd840be31d3fbf7d74b34a5403c49c`

Three hosted-model infrastructure preflights have failed safely before any benchmark task executed. `benchmark-arms` runs #1 (`33177348082`), #2 (`33177729891`), and #3 (`33178142084`) are excluded infrastructure evidence, not benchmark results. Current valid benchmark task execution count is **0**.

The next authorized path is defined in [`execution-frontier.md`](001-proof-before-done/execution-frontier.md): establish one pinned local reproducible model/runtime, migrate only the transport/provenance layer without changing frozen experiment semantics, then execute T052 → T053 → T054 → T055 in order and complete the v0.1 closeout only after durable raw evidence is canonical.
