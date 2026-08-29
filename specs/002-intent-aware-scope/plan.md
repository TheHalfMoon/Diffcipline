# Implementation plan — 002 Intent-Aware Scope

## Constraints

- Preserve the dependency-free Rust core.
- Preserve v0.1 policy compatibility when new fields are absent.
- Keep intent matching deterministic and deliberately narrower than a general glob engine.
- Do not infer task intent or risk with an LLM.
- Keep GitHub Action annotation read-only: no issue/PR write permission.
- Keep repository changes within `.diffcipline.toml` limits per PR.

## Delivery sequence

### Phase A — Intent contract

Extend `Policy` with optional expected and forbidden path patterns. Validate patterns while parsing. Evaluate every changed repository-relative path after Git statistics collection.

Rules:
- expected patterns configured + any changed path unmatched => FAIL;
- any forbidden match => FAIL;
- empty expected list means no expected-file restriction;
- empty forbidden list means no forbidden-surface restriction.

Expose matched contract state through reasons and structured proof output.

### Phase B — Risk verification profiles

Add explicit CLI `--risk R0|R1|R2|R3` parsing. Extend `[verification]` with `r0_commands`, `r1_commands`, `r2_commands`, and `r3_commands`.

When `--risk` is absent, use existing `commands` exactly as v0.1 does. When risk is present, the corresponding profile must exist and contain at least one command; otherwise return an execution/configuration error and do not silently weaken verification.

### Phase C — Proof output contract

Human output adds explicit scope/risk lines. JSON remains manually serialized and dependency-free, adding fields without claiming stable-v1 schema guarantees:
- `risk`;
- `expected_files`;
- `forbidden_surfaces`;
- `scope_violations`;
- verification entries with command/state.

### Phase D — GitHub Action annotation

Add Action input `risk` and forward it to the CLI only when non-empty. Run a JSON proof capture for summary generation while preserving the CLI exit code. Write deterministic Markdown to `$GITHUB_STEP_SUMMARY` with verdict, risk, changed-file count, diff size, and reasons.

The Action must not request pull-request write permissions and must not post comments.

## Verification

Every implementation PR must run the repository-required exact-head gates. Rust changes require at minimum:

```bash
cargo fmt --all -- --check
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo test --workspace --all-targets --locked
```

The dogfood Action must pass on Ubuntu, macOS, and Windows. Existing installer compatibility and release-candidate workflows must remain green.

## Completion

After all implementation tasks are canonical, update `README.md` and the Spec 002 ledger with only implemented behavior. Do not create a `v0.2.0` tag unless a later explicit release closeout task is added to this spec and all corresponding exact-release gates are defined and passed.
