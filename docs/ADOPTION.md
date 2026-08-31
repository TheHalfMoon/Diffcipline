# Adoption guide

Diffcipline has three complementary adoption surfaces. Choose the smallest surface that matches the repository's needs, then add more only when the added proof is useful.

## 1. Agent Skills

Install the canonical Agent Skills source:

```bash
npx skills add TheHalfMoon/Diffcipline
```

For deterministic non-interactive installation of both skills into a qualified installer target:

```bash
npx skills add TheHalfMoon/Diffcipline \
  --skill diffcipline \
  --skill diffcipline-review \
  --agent <agent> \
  --copy \
  --yes
```

The repository qualifies the same canonical skill text for these installer targets:

| Client | Installer target | Qualified skill directory |
| --- | --- | --- |
| Claude Code | `claude-code` | `.claude/skills` |
| Codex | `codex` | `.agents/skills` |
| Cursor | `cursor` | `.agents/skills` |
| OpenCode | `opencode` | `.agents/skills` |
| GitHub Copilot | `github-copilot` | `.agents/skills` |
| Gemini CLI | `gemini-cli` | `.agents/skills` |

Qualification proves discovery, installation, and byte identity against the canonical `skills/` sources. It does not claim vendor endorsement or exhaustive client UI/runtime integration. See `docs/INSTALLATION.md` for the full portability contract.

## 2. CLI and repository policy

Install the immutable v1 CLI:

```bash
cargo install --git https://github.com/TheHalfMoon/Diffcipline --tag v1.0.0 diffcipline
```

Create a detected starting policy:

```bash
diffcipline init
```

Or start from a checked-in ecosystem example:

- `examples/policies/rust.toml`
- `examples/policies/node.toml`
- `examples/policies/python.toml`
- `examples/policies/go.toml`

Copy the closest example to the repository root as `.diffcipline.toml`, then review every command before enabling execution.

Inspect without executing configured verification:

```bash
diffcipline check --base origin/main
```

Run configured verification explicitly:

```bash
diffcipline check --base origin/main --run
```

Use a risk profile only when that profile is actually configured:

```bash
diffcipline check --base origin/main --risk R2 --run
```

If verification is configured but `--run` is absent, Diffcipline reports it as `NOT RUN` and does not return a clean `PASS`. A requested missing or empty risk profile fails closed instead of falling back to weaker checks.

## 3. GitHub Action

For a readable stable reference, use the immutable `v1.0.0` release tag:

```yaml
permissions:
  contents: read

steps:
  - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7.0.1
    with:
      fetch-depth: 0

  - uses: TheHalfMoon/Diffcipline@v1.0.0
    with:
      base: ${{ github.event.pull_request.base.sha }}
      run-verification: "true"
```

For the strongest source-identity pin, reference the exact immutable v1 release commit instead:

```yaml
  - uses: TheHalfMoon/Diffcipline@5cb1c77340b75649f6168e0e8f66479ea047ea96
    with:
      base: ${{ github.event.pull_request.base.sha }}
      run-verification: "true"
```

Add `risk: R0|R1|R2|R3` only when the corresponding repository policy profile exists. The Action preserves the CLI exit status and requires explicit `run-verification: "true"` before executing repository-declared commands.

Review `.diffcipline.toml` before executing verification on untrusted changes.

## Recommended adoption sequence

1. Install the Agent Skills if the coding agent can consume them.
2. Add or review `.diffcipline.toml` using a validated ecosystem example as a starting point.
3. Run `diffcipline check` without `--run` first to inspect scope and pending verification.
4. Run `diffcipline check --run` only after the repository-declared commands are trusted.
5. Add the pinned GitHub Action when the same deterministic gate should run in CI.
6. For high-risk repositories, define explicit risk profiles and enterprise policy rather than assuming generic defaults are sufficient.

These surfaces are composable, not mandatory as a bundle. Agent Skills shape behavior; the CLI emits deterministic repository proof; the Action carries the same CLI contract into GitHub CI.
