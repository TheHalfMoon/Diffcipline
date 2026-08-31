# Agent Skills installation and portability contract

Diffcipline publishes one platform-neutral Agent Skills core. Agent clients may differ in discovery or installation paths, but they must consume the same canonical skill behavior.

## Canonical skills

The repository contains exactly one behavioral authority for each shipped skill:

- `skills/diffcipline/SKILL.md`
- `skills/diffcipline-review/SKILL.md`

Client-specific copies of either skill are not maintained in the repository. If an installer copies a skill into a client-specific directory, the installed `SKILL.md` must be byte-identical to the canonical source at the exact repository revision being qualified.

## Generic Agent Skills layout

A portable Diffcipline source follows this repository-relative layout:

```text
skills/
  diffcipline/
    SKILL.md
  diffcipline-review/
    SKILL.md
```

Each `SKILL.md` uses Agent Skills frontmatter with a stable `name`, a human-readable `description`, and `license: MIT`. The behavioral contract lives in the Markdown body; filesystem placement chosen by a client is an installation adapter, not a second behavioral authority.

A compatible installer must be able to discover both canonical names from the repository source and install both without rewriting their content.

## Generic installation

With the Agent Skills CLI:

```bash
npx skills add TheHalfMoon/Diffcipline
```

For deterministic non-interactive installation of both skills into a supported client:

```bash
npx skills add TheHalfMoon/Diffcipline \
  --skill diffcipline \
  --skill diffcipline-review \
  --agent <agent> \
  --copy \
  --yes
```

Repository CI pins the installer version used for qualification and installs from the exact checked-out candidate head rather than from a moving remote branch.

## Qualified clients

The canonical compatibility matrix covers:

| Client | Qualified installer target | Qualified skill directory |
| --- | --- | --- |
| Claude Code | `claude-code` | `.claude/skills` |
| Codex | `codex` | `.agents/skills` |
| Cursor | `cursor` | `.agents/skills` |
| OpenCode | `opencode` | `.agents/skills` |
| GitHub Copilot | `github-copilot` | `.agents/skills` |
| Gemini CLI | `gemini-cli` | `.agents/skills` |

These directory names describe the pinned installer contract under test. They do not authorize client-specific changes to the canonical skill text.

## Qualification contract

`skills-compat` must prove all of the following on the exact candidate head:

1. the generic repository layout contains one canonical `diffcipline` and one canonical `diffcipline-review` behavioral source;
2. both files expose the expected Agent Skills names and required portable content markers;
3. no second `SKILL.md` in the repository claims either canonical skill name;
4. the pinned installer discovers both skills from the exact local checkout;
5. each of the six named clients installs both skills non-interactively;
6. each installed `SKILL.md` is byte-identical to its canonical repository source.

A client is not qualified by documentation alone. Its exact-head installer job must complete successfully.

## CLI boundary

The Agent Skills core and the Rust CLI are complementary but separate portability surfaces:

- the skills define the platform-neutral engineering behavior;
- the CLI observes repository facts and emits deterministic proof;
- a skill may be used where the CLI is unavailable, but it must report unavailable proof as NOT RUN rather than inventing PASS;
- the CLI does not require an agent-specific runtime or client SDK;
- client-specific wrappers may select installation paths or invoke the CLI, but they must not silently reinterpret verdicts, risk, policy, or proof semantics.

## Limitations

The compatibility workflow proves discovery, installation, layout, and content identity using the pinned Agent Skills installer on GitHub-hosted Linux runners. It does not claim exhaustive UI/runtime integration testing inside every client application or every host operating system.

Installer directory conventions can evolve upstream. A future directory change may require a thin qualification adapter, but any change that requires divergent Diffcipline skill behavior is a compatibility failure and must not be hidden by maintaining separate client-specific skill text.
