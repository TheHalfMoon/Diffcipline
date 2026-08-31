# Independent validation protocol

This document is a reproducible protocol, not an external validation result. A third party may execute it against immutable `v1.0.0` and retain the resulting evidence. If a step cannot be executed, record `NOT RUN`; never convert missing infrastructure into `PASS`.

## Fixed target

- release: `v1.0.0`
- release commit: `5cb1c77340b75649f6168e0e8f66479ea047ea96`
- expected release assets: three native binaries, `SHA256SUMS`, and `PROVENANCE.sigstore.json`

Before testing, record:

```text
validation_date=
os=
architecture=
git_version=
rustc_version=
cargo_version=
gh_version=
skills_cli_version=
```

Use `NOT AVAILABLE` for tools that are not installed. Do not infer a successful check from an unavailable tool.

## A. Source identity

```bash
git clone https://github.com/TheHalfMoon/Diffcipline.git
cd Diffcipline
git checkout v1.0.0
test "$(git rev-parse HEAD)" = "5cb1c77340b75649f6168e0e8f66479ea047ea96"
git ls-remote --refs origin refs/tags/v1.0.0
```

Expected result: the local and remote tag resolve to the fixed release commit.

Retain the command output and exact checkout SHA.

## B. Published release integrity

This section requires an authenticated GitHub CLI with release and attestation verification support.

```bash
gh release view v1.0.0 --repo TheHalfMoon/Diffcipline \
  --json tagName,url,isDraft,isImmutable,publishedAt,assets

gh release verify v1.0.0 --repo TheHalfMoon/Diffcipline

rm -rf published-v1
mkdir published-v1
gh release download v1.0.0 \
  --repo TheHalfMoon/Diffcipline \
  --dir published-v1

cd published-v1
test "$(find . -maxdepth 1 -type f | wc -l)" -eq 5
test "$(wc -l < SHA256SUMS)" -eq 3
sha256sum -c SHA256SUMS
for file in diffcipline-*; do
  gh attestation verify "$file" --repo TheHalfMoon/Diffcipline
done
for file in *; do
  gh release verify-asset v1.0.0 "$file" --repo TheHalfMoon/Diffcipline
done
cd ..
```

Expected result: the release is not a draft, reports immutable state, release verification succeeds, exactly five assets are downloaded, the three binary checksums verify, every native binary passes attestation verification, and every asset passes release-asset verification.

If the platform lacks `sha256sum`, use a platform-native SHA-256 verifier and record the exact replacement command. Do not claim the canonical command ran when it did not.

## C. CLI proof semantics

Install the fixed release source:

```bash
cargo install --git https://github.com/TheHalfMoon/Diffcipline \
  --tag v1.0.0 diffcipline
```

Create a disposable Rust repository and execute the canonical proof path:

```bash
DEMO="$(mktemp -d)"
cd "$DEMO"
git init -q
git config user.name "Diffcipline Independent Validation"
git config user.email "diffcipline-validation@example.invalid"
mkdir -p src
printf '[package]\nname = "diffcipline-validation"\nversion = "0.1.0"\nedition = "2024"\n' > Cargo.toml
printf 'fn main() {}\n' > src/main.rs
cargo generate-lockfile -q
git add .
git commit -qm "validation base"

diffcipline init
git add .diffcipline.toml
git commit -qm "add diffcipline policy"
printf '\n// Bounded validation change.\n' >> src/main.rs

diffcipline check --json > proof-not-run.json
not_run_status=$?
diffcipline check --run --json > proof-run.json
run_status=$?
printf 'not_run_status=%s\nrun_status=%s\n' "$not_run_status" "$run_status"
```

Expected semantics:

- configured verification without `--run` is `NOT RUN`; a clean `PASS` is impossible and the CLI exits `1` for `REVIEW` in the clean bounded fixture;
- after formatting, linting, and tests execute successfully, the bounded fixture reaches `PASS` and exits `0`;
- a policy violation or failed verification produces `FAIL` and exits `2`;
- usage/execution errors exit `64`.

Retain `.diffcipline.toml`, both JSON proofs, exit codes, Git status/diff, and tool versions.

## D. Agent Skills source and installation identity

At the fixed checkout, record hashes for the two canonical behavioral sources:

```bash
sha256sum skills/diffcipline/SKILL.md skills/diffcipline-review/SKILL.md
```

If the Agent Skills CLI is available, record its version, select one qualified installer target from `docs/INSTALLATION.md`, install both skills non-interactively, and byte-compare the installed `SKILL.md` files with the fixed checkout sources.

Example installation shape:

```bash
npx skills add TheHalfMoon/Diffcipline \
  --skill diffcipline \
  --skill diffcipline-review \
  --agent <agent> \
  --copy \
  --yes
```

Do not label a client as runtime-validated merely because file installation succeeds. The repository qualification contract covers discovery, installation, layout, and byte identity, not exhaustive client UI/runtime behavior.

## Evidence record

A useful independent result should preserve at least:

- validator identity or organization if they choose to disclose it;
- date, OS, architecture, and tool versions;
- exact tag and commit SHA;
- raw stdout/stderr and exit codes;
- downloaded release metadata and asset hashes;
- release/attestation verification output;
- CLI JSON proof files and repository diff/status;
- Agent Skills source hashes and any installation byte comparisons;
- every skipped or unavailable step explicitly marked `NOT RUN` or `NOT AVAILABLE`.

## Result language

Use bounded language:

- `PASS` only for a check that actually ran and met its stated acceptance condition;
- `REVIEW` only when the Diffcipline proof contract returns that verdict or the evaluator explicitly identifies unresolved evidence;
- `FAIL` for an executed check that violates its acceptance condition;
- `NOT RUN` when execution did not occur;
- `NOT AVAILABLE` when required tooling or infrastructure was unavailable.

This protocol does not establish universal superiority, benchmark treatment effect, vendor endorsement, or independent adoption. Those require separate evidence.
