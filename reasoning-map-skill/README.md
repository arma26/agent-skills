# Decision Graph

This repository builds two related but separate deliverables:

- a `reasoning-map` skill for structuring design, investigation, and decision-making as a graph
- a `reasoning_map_visualizer` tool for rendering that graph artifact

The shared contract is a mutable JSON reasoning-map artifact. The skill authors or revises it. The visualizer consumes it. Neither should become the other's source of truth.

## Why This Exists

The project is aimed at agent-first reasoning support.

A reasoning map helps preserve:

- problems, questions, and goals
- options, constraints, and risks
- supporting and challenging claims
- decisions and unresolved gaps
- abandoned or muted branches that still matter as context

The intent is to reduce reasoning loss across long tasks, support investigation and brainstorming, and provide better structured input to ADRs and documentation.

## Should You Use It

The current evidence suggests the skill is most useful when the work has real
decision surface:

- design work with competing options, constraints, and risks
- investigations where problems raise subproblems and missing context matters
- long-running tasks where a future agent may need to resume without full prior
  conversational context
- ADR-oriented work where the shape of the reasoning matters more than a flat
  conclusion

It is less useful when:

- the task is short and mostly linear
- a checklist or direct answer is already enough
- the overhead of maintaining graph state would exceed the value of preserving
  it

The current A/B benchmarking points to a narrower claim than "always use it."
Persisted maps alone improved scope discipline and reinforced a single-source-
of-truth style of reasoning. Maps plus the `reasoning-map` skill performed
better overall on a clean-room replay task: clearer tradeoffs, better explicit
gap handling, and stronger latent-memory value for a fresh agent. The cost is
extra structure, extra artifact management, and some risk of widening scope if
the map is allowed to grow without a stopping rule.

In practice:

- use the skill when the reasoning itself is an asset you want to preserve
- skip it when the task is disposable, obvious, or too small to benefit from a
  persisted graph
- prefer compressing or muting weak branches rather than growing long tails

## Repository Layout

- `skills/reasoning-map/`: the skill, schema references, workflows, and minimal example
- `tools/reasoning_map_visualizer/`: loader, filters, render model, and render backends
- `tests/reasoning_map_visualizer/`: scenario-based tests for selection and rendering behavior
- `docs/reasoning-map-usage.md`: usage guidance for authoring and rendering maps
- `docs/reasoning-maps/`: repo-local example and active reasoning-map artifacts
- `docs/plans/`: design and implementation notes

## Reasoning-Map Artifact

The primary artifact is a rootless JSON graph with:

- stable semantic node ids
- first-class edges
- explicit deficiencies
- mutable node metadata
- non-destructive suppression through `status` and `visibility`

Common node kinds:

- `question`
- `problem`
- `goal`
- `claim`
- `option`
- `constraint`
- `risk`
- `decision`
- `gap`

The graph is allowed to sprawl. Problems can raise more problems. Submaps are allowed when a branch becomes dense or objective-oriented. Related maps should be linked explicitly.

## Quick Start

Render a single graph:

```bash
python -m tools.reasoning_map_visualizer.visualize docs/reasoning-maps/repo-development.json --format dot
python -m tools.reasoning_map_visualizer.visualize docs/reasoning-maps/repo-development.json --format mermaid
python -m tools.reasoning_map_visualizer.visualize docs/reasoning-maps/repo-development.json --format terminal
```

Inspect a focused neighborhood:

```bash
python -m tools.reasoning_map_visualizer.visualize docs/reasoning-maps/repo-development.json --format dot --focus decision.shared-render-pipeline --depth 1
```

Batch render a directory. Dry-run is the default:

```bash
python -m tools.reasoning_map_visualizer.batch_render docs/reasoning-maps/
```

Write outputs explicitly:

```bash
python -m tools.reasoning_map_visualizer.batch_render docs/reasoning-maps/ --format dot --write
python -m tools.reasoning_map_visualizer.batch_render docs/reasoning-maps/ --format mermaid --write
```

Useful flags:

- `--full-graph` to include muted, hidden, and non-active content
- `--include-muted` or `--include-hidden` for narrower overrides
- `--focus <node-id>` with `--depth <n>` for local inspection
- `--strict` to fail on dangling edges instead of warning

## Current Repo Maps

- `docs/reasoning-maps/repo-development.json`: repo-level primary map
- `docs/reasoning-maps/visualizer-backends.json`: task-level submap for visualizer backend work
- `docs/reasoning-maps/artifact-contract.json`: contract and anti-pattern map for the persisted graph shape

These are intended to be usable context artifacts for future agent work, not just examples.

When a fresh agent is spawned for meaningful design, investigation, or
implementation work, these maps are intended to be parsed as lazy-loaded repo
context alongside plans and docs rather than treated as optional decoration.

## Testing

Run the visualizer test suite:

```bash
python -m unittest tests.reasoning_map_visualizer.test_visualize -v
```

## Further Reading

- `docs/reasoning-map-usage.md`
- `docs/plans/2026-09-01-reasoning-map-skill-design.md`
- `docs/plans/2026-09-01-reasoning-map-visualizer-design.md`
- `skills/reasoning-map/SKILL.md`
