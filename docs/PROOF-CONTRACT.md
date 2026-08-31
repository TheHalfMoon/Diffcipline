# Diffcipline Proof Contract v1

A proof card is a deterministic summary of repository facts observed for one change. Human output remains concise; `diffcipline check --json` is the stable machine contract.

## Machine schema

The v1 machine proof identifies itself with:

- `schema = "diffcipline.proof/v1"`
- `schema_version = "1.0"`

The repository-tracked schema is `schemas/proof-v1.json`. Required top-level fields and their meanings cannot be removed or silently reinterpreted within schema major version 1. Additive fields require a schema update, tests, and documentation.

Policy provenance is explicit. `policy.mode` is `default`, `repository`, or `enterprise`; `policy.sources` lists policy inputs evaluated for the proof in deterministic order.

## Enterprise policy mode

Enterprise policy is explicit and local-file only:

```text
diffcipline check --enterprise-policy <path> [--base <ref>] [--risk <R0|R1|R2|R3>] [--run] [--json]
```

The monotonic enterprise layer is active only when `--enterprise-policy <path>` is actually supplied. A repository-controlled workflow can omit that argument, so the local-file mechanism alone does not make an organizational baseline mandatory.

A genuinely mandatory organizational baseline requires an organization-controlled enforcement path—such as a required workflow, reusable workflow, ruleset-integrated workflow, or equivalent externally controlled CI policy—that supplies the enterprise policy input. The local-file mechanism is not an identity, RBAC, credential-distribution, or remote policy-control system.

No environment discovery, network fetch, credential exchange, or remote control plane is used. When enterprise mode is active, `policy.mode` is `enterprise`; `policy.sources` lists the explicit enterprise source first and `.diffcipline.toml` second when repository policy exists.

Layering is monotonic:

- file and added-line limits use the stricter minimum;
- dependency-manifest, lockfile, and untracked-file decisions use `FAIL > REVIEW > ALLOW`;
- forbidden surfaces are cumulative;
- every non-empty enterprise and repository `expected_files` contract is enforced independently;
- default and risk-specific verification commands are cumulative, deterministic, enterprise-first, and exact duplicates are removed;
- missing, unreadable, malformed, unsupported-version, duplicate, or self-referential enterprise policy input fails closed.

A repository policy can therefore add constraints or verification but cannot reduce the effect of an enterprise baseline once enterprise mode is invoked. The no-enterprise path retains repository-policy version 1 behavior.

## Verdicts and exit codes

- **PASS / 0** — every configured hard requirement was observed and satisfied.
- **REVIEW / 1** — no hard requirement failed, but judgment or missing optional evidence remains.
- **FAIL / 2** — at least one configured hard requirement failed or verification returned non-zero.
- **64** — usage or execution error; no proof verdict is implied.

## Evidence classes

1. **Diff evidence** — changed files and line counts from Git.
2. **Dependency evidence** — whether dependency manifests changed.
3. **Lockfile evidence** — whether lockfiles changed.
4. **Workspace evidence** — whether untracked files remain.
5. **Scope evidence** — expected files, forbidden surfaces, and violations.
6. **Risk evidence** — the selected risk profile when present.
7. **Verification evidence** — exact configured commands and PASS / FAIL / NOT RUN state.
8. **Policy provenance** — policy mode and evaluated policy sources.

## Invariants

- NOT RUN is never PASS.
- Command success is scoped to the exact command that ran; it does not imply unrelated checks passed.
- Diff size is a review signal, not a correctness metric.
- Minimality never overrides security, validation, accessibility, data integrity, or explicit requirements.
- A proof card reports observations. It does not invent intent or root cause.
- Existing v1 required fields keep their meanings for the lifetime of schema major version 1.
