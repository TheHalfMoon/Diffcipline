# Diffcipline policy examples

These examples are copyable starting policies for repositories that use Diffcipline's current policy schema.

Copy the closest example to the repository root as `.diffcipline.toml`, then review every verification command before using `diffcipline check --run`.

The examples deliberately stay conservative:

- policy budgets match Diffcipline's documented defaults;
- dependency manifest, lockfile, and untracked changes require `REVIEW`;
- verification commands use common ecosystem-native commands only;
- risk-specific profiles are omitted because they must reflect a repository's real graded verification commands rather than invented defaults.

Published examples:

- `policies/rust.toml` — Rust workspace verification;
- `policies/node.toml` — Node package test verification;
- `policies/python.toml` — Python pytest verification;
- `policies/go.toml` — Go module test verification.

These files are executable documentation. Repository integration tests load the exact checked-in files, run them through the released CLI parser path, and assert that the expected verification command is exposed as `NOT RUN` when `--run` is omitted. A malformed or drifted example therefore fails CI instead of becoming stale documentation.

An example proves only that the policy is accepted by the current Diffcipline contract. It does not prove that its verification command is sufficient for every project in that ecosystem. Maintainers remain responsible for choosing commands that match their own build, test, lint, security, and risk requirements.
