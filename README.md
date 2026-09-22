# Agent skills

This repository is an experimental collection of Codex skills and supporting evaluation tools.

## Status

The repository is a reproducible prototype. It does not define a release, compatibility policy, support commitment, or contribution process.

No license is present. Treat the contents as evaluation source, not as a reusable release.

## Quick start

Prerequisite: [mise](https://mise.jdx.dev/).

Review `.mise.toml`, trust that repository configuration, install the pinned Python version, and validate the repository:

```bash
mise trust .mise.toml
mise install python@3.14.0
mise exec -- python scripts/validate.py
```

The command validates every discovered skill package. It also runs the validator and reasoning-map visualizer tests.

```text
Validation passed: <count> skills and 2 test suites.
```

The command returns a nonzero status when a package or test fails. Inspect the named skill file or failing test output first.

## Components

| Component | Entry point | Verification |
| --- | --- | --- |
| Open source polish | [Skill instructions](open-source-polish/SKILL.md) | Package validation |
| Mosaic harvest | [Skill instructions](mosaic-harvest/SKILL.md) | Package validation |
| Reasoning map | [Skill instructions](reasoning-map-skill/skills/reasoning-map/SKILL.md) | Package validation and the visualizer test suite |
| Reasoning stack | [Skill instructions](reasoning-stack/SKILL.md) | Package validation |
| Security reviewer | [Skill instructions](security-reviewer/SKILL.md) | Package validation and recorded evaluations |
| Software documentation writer | [Skill instructions](writing-software-documentation/SKILL.md) | Package validation and recorded evaluations |

Each skill directory contains its instructions and optional `agents/`, `references/`, or `assets/` resources. The reasoning-map component also contains executable visualization tools.

## Repository boundaries

- `SKILL.md`, `references/`, `assets/`, and `tools/` contain maintained skill or tool source.
- `tests/` contains executable tests when a component has runtime code.
- `docs/specs/`, `docs/plans/`, and `docs/decisions/` contain design history and decisions.
- `tests/evaluations/` and `evaluations/` contain recorded evaluation evidence. They are not live test suites.
- The root `.gitignore` excludes `.worktrees/`, `.DS_Store`, and `states` as local state.

## Limitations

- Structural validation cannot prove that a skill produces good decisions.
- Recorded evaluations describe specific prompts and runs. They do not establish universal performance.
- The production-readiness material is an audit framework. It does not validate a deployment without deployment evidence.
- The repository does not publish installable packages or release artifacts.

## Component documentation

- [Reasoning-map overview](reasoning-map-skill/README.md)
- [Reasoning-map usage](reasoning-map-skill/docs/reasoning-map-usage.md)
- [Open-source-polish design](open-source-polish/docs/specs/2026-09-02-open-source-polish-design.md)
- [Security-reviewer decision](security-reviewer/docs/decisions/adopt-architecture-first-security-review.md)
- [Documentation decisions](writing-software-documentation/docs/decisions/README.md)
