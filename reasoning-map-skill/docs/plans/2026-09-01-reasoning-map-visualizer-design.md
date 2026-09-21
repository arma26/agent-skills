# Reasoning Map Visualizer Design

**Date:** 2026-09-01

## Goal

Create a standalone Python visualizer for reasoning-map JSON artifacts that can emit Graphviz first, Mermaid second, and a terminal-oriented inspection view last.

## Product Boundary

The visualizer is a separate addition from the `reasoning-map` skill.

- The skill defines how reasoning maps are authored.
- The visualizer consumes the JSON artifact format.
- The visualizer must not require skill invocation to function.
- The visualizer must not mutate graph files.

This separation keeps the graph artifact as the only shared contract.

## Core Constraints

- Graphviz export is the primary output.
- Mermaid export is secondary.
- Terminal visualization is useful for agent TUI inspection but is lower priority.
- The implementation should use Python and standard library tooling for the MVP.
- CLI flags must allow default filtered views and explicit full-graph overrides.

## Architecture Options

### Option 1: Single CLI script with multiple backends

One script loads JSON, filters the graph, and emits all formats.

Pros:

- minimal file count
- one entry point

Cons:

- backend logic can become tangled
- harder to extend without growing one large file

### Option 2: Shared core plus backend emitters

A small loader and filter layer feeds backend-specific emitters for DOT, Mermaid, and terminal text.

Pros:

- keeps parsing and filtering consistent
- keeps backend concerns separate
- reduces duplication while staying lightweight

Cons:

- slightly more structure than the smallest possible MVP

### Option 3: Independent exporters

Separate scripts emit DOT, Mermaid, and terminal views directly from raw JSON.

Pros:

- fastest initial implementation

Cons:

- duplicated parsing and filtering logic
- high risk of backend drift

## Recommendation

Use Option 2 with a very small shared core.

This gives the visualizer a clean standalone boundary while preventing output drift between Graphviz, Mermaid, and terminal backends.

Use a narrow internal render model between filtering and backend emission. Do not persist it as a second artifact format. It exists only to normalize labels, style tokens, warnings, and selected connections once so each backend consumes the same render-ready structure.

## Proposed File Layout

Create a separate tool area:

- `tools/reasoning_map_visualizer/visualize.py`
- `tools/reasoning_map_visualizer/loader.py`
- `tools/reasoning_map_visualizer/filters.py`
- `tools/reasoning_map_visualizer/emit_dot.py`
- `tools/reasoning_map_visualizer/emit_mermaid.py`
- `tools/reasoning_map_visualizer/emit_terminal.py`

Add tests and sample fixtures:

- `tests/reasoning_map_visualizer/test_visualize.py`
- `tests/reasoning_map_visualizer/fixtures/*.json`

## CLI Contract

Recommended invocation shape:

```bash
python tools/reasoning_map_visualizer/visualize.py path/to/graph.json --format dot
python tools/reasoning_map_visualizer/visualize.py path/to/graph.json --format mermaid
python tools/reasoning_map_visualizer/visualize.py path/to/graph.json --format terminal
python tools/reasoning_map_visualizer/visualize.py path/to/graph.json --format dot --full-graph
```

Recommended flags:

- `--format {dot,mermaid,terminal}`
- `--output <path>`
- `--focus <node-id>`
- `--depth <n>`
- `--strict`
- `--include-muted`
- `--include-hidden`
- `--all-visibility`
- `--all-status`
- `--full-graph`
- `--title <text>`

## Filtering Semantics

Default view:

- include active, useful current reasoning
- suppress muted branches unless asked for
- suppress hidden branches unless asked for
- suppress non-current status branches unless asked for

Override behavior:

- `--include-muted` includes muted visibility
- `--include-hidden` includes hidden visibility
- `--all-visibility` includes normal, muted, and hidden
- `--all-status` includes rejected, erroneous, superseded, and resolved content
- `--full-graph` acts as a convenience flag for exhaustive inspection

The renderer should be read-only. No cleanup or auto-repair flags should exist.

## Output Contract

### Graphviz

Emit valid DOT text with rich visual semantics:

- node shape by `kind`
- styling by `status`
- muted or hidden appearance by `visibility`
- warning emphasis for deficiencies
- edge labels and styling by edge type

Graphviz is the primary view for dense reasoning graphs.

### Mermaid

Emit valid Mermaid flowchart text with simpler styling:

- preserve topology
- keep labels compact
- use limited class-based styling for major distinctions

Mermaid is a portability export, not the richest view.

### Terminal

Emit a text-first inspection view rather than spatial ASCII art:

- node summary
- local neighborhood or filtered subgraph listing
- edge relationships
- deficiency and status markers

This is meant for quick agent TUI inspection, not a full layout engine.

## Error Handling

- fail on missing required top-level structure
- degrade gracefully on missing optional fields
- warn on dangling edges by default
- fail on dangling edges under `--strict`
- ignore unknown extra fields

## Intent Scaffolding For Implementation

Current behavior:

- the repo contains a reasoning-map skill and schema references
- no visualizer exists yet

Required behavior:

- load a reasoning-map JSON graph
- normalize and filter it without mutating input
- emit DOT first, Mermaid second, terminal text last
- keep filtering semantics consistent across backends

Must remain true:

- the visualizer stays separate from the skill as a shippable product
- the graph artifact remains the only integration surface
- full-graph overrides remain explicit and user-controlled

## Testing Strategy

Use scenario-based tests centered on user-visible behavior:

- default render suppresses muted and hidden content
- `--include-muted` shows muted content only in addition to default visibility
- `--full-graph` shows suppressed visibility and non-current statuses
- `--focus` with `--depth` renders only the local neighborhood
- dangling edges warn by default
- dangling edges fail under `--strict`
- the same filtered subgraph emits valid text for DOT, Mermaid, and terminal outputs

## MVP Recommendation

For the MVP:

- implement the shared loader and filter path
- implement Graphviz backend completely first
- implement Mermaid with simpler semantics next
- implement terminal inspection last
- avoid dependency on external Graphviz binaries for tests

## Non-Goals

- editing graph artifacts
- auto-fixing malformed graph files
- building an interactive TUI in the first version
- coupling the visualizer to skill invocation
