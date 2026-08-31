# Security policy

Diffcipline treats vulnerability reports as evidence-sensitive engineering work. Do not publish exploit details, secrets, tokens, private data, or weaponized reproduction steps in a public issue.

## Supported versions

| Version | Security support |
| --- | --- |
| `1.0.x` | Supported |
| `< 1.0` | Historical releases and benchmark evidence only; no security-fix commitment |

Security fixes are developed on canonical `main`, verified against the exact change, and released through the documented release process.

## Report a vulnerability privately

Use a private GitHub Security Advisory when GitHub offers the report form:

https://github.com/TheHalfMoon/Diffcipline/security/advisories/new

Include, when available:

- affected version or exact commit;
- affected CLI, Action, policy, installation, or release surface;
- minimal reproduction steps;
- expected and observed behavior;
- realistic impact and attack preconditions;
- relevant logs with credentials and private data removed.

If GitHub does not offer you access to the private advisory form, open a public issue titled `Security contact request` **without vulnerability details**. Use that issue only to establish a private contact path. Never attach exploit code or sensitive logs there.

## Executable-policy trust boundary

`.diffcipline.toml` may contain verification commands. Those commands are executable repository content:

- `diffcipline check` does not execute them;
- `diffcipline check --run` does;
- review repository policy before using `--run` on untrusted changes;
- CI should pin trusted actions and minimize token permissions.

Diffcipline must never label an unexecuted verification command as `PASS`.

## Fix and disclosure standard

A report is not considered fixed merely because a patch exists. A security fix must pass repository policy and machine-observed verification appropriate to its risk. Public disclosure should wait until a safe fix and release path exist unless earlier disclosure is necessary to protect users.

Reports about third-party coding agents, GitHub itself, skills.sh, or other external services should go to those maintainers unless Diffcipline introduces the vulnerable integration behavior.