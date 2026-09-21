# AGENTS.md

## Mission

This repository builds two related but separate products:

- a `reasoning-map` skill for structuring decisions, arguments, investigations, and design reasoning as a graph
- a `reasoning_map_visualizer` tool that renders the graph artifact without owning authorship of it

The shared contract is the reasoning-map JSON artifact. Do not introduce alternate persisted sources of truth casually.

## Product Boundaries

### Reasoning-map skill

The skill is for agent reasoning support.

- author or revise reasoning maps
- stress-test assumptions, options, risks, and decisions
- extract focused subgraphs into ADR inputs, design notes, debugging notes, or documentation support

The skill is not:

- the ADR itself
- a final user-facing document format
- a visualization tool
- a ledger that replaces judgment

### Visualizer

The visualizer is a separate deliverable.

- consume the reasoning-map JSON artifact
- filter and select a subgraph
- project the graph into Graphviz, Mermaid, or terminal-oriented views

The visualizer must remain read-only with respect to graph artifacts.

### Internal render model

The renderer may use an internal render model in memory.

- it exists to normalize labels, style tokens, warnings, and connections
- it is not a persisted artifact format
- it must not become a second source of truth

## Reasoning-map Contract

### Core shape

The primary artifact is a mutable JSON graph.

- rootless by default
- stable semantic node ids
- first-class edges
- explicit deficiencies
- non-destructive suppression of weak or rejected branches

Do not force a single center node. Problems may raise more problems. Investigations may fork. Decisions may resolve one cluster while leaving other gaps open.

### Node expectations

Keep the ontology compact unless repeated use proves otherwise.

Current core kinds:

- `question`
- `problem`
- `goal`
- `claim`
- `option`
- `constraint`
- `risk`
- `decision`
- `gap`

Use `role` and linked structure before adding more top-level kinds.

Required node fields:

- `id`
- `kind`
- `title`
- `status`
- `deficiencies`

Strongly preferred fields:

- `summary`
- `importance`
- `confidence`
- `completeness`
- `visibility`
- `relevance`

### Edge expectations

Edges are the primary reasoning structure.

- represent meaningful relationships explicitly
- prefer links over longer prose
- do not hide important structure inside node summaries

Current common edge types:

- `raises`
- `addresses`
- `supports`
- `challenges`
- `causes`
- `mitigates`
- `depends_on`
- `decomposes`
- `leads_to`
- `relates_to`
- `supersedes`

### Identity discipline

Use stable semantic ids.

Good examples:

- `problem.retry-storms`
- `claim.latency-spike-observed`
- `decision.safer-retry-defaults`

Rules:

- prefix ids by kind
- keep ids semantic and compact
- update node metadata instead of replacing ids
- if duplicate nodes appear, converge on one canonical id

### Facts vs inferences

Do not collapse observed facts and inferred explanations into one node when the distinction matters.

- use fact-oriented claims such as `assertion_kind: observation` for direct findings
- use inference-oriented claims such as `assertion_kind: inference` or `role: cause` for explanations
- connect them through explicit edges

### Deficiency discipline

Sparse reasoning is allowed. Silent omission is not.

Useful deficiency flags include:

- `missing_evidence`
- `untested_assumption`
- `no_alternative_considered`
- `no_counterargument`
- `unclear_constraint`
- `risk_unmitigated`
- `decision_without_rationale`
- `investigation_required`
- `stale_context`
- `ambiguous_scope`

If a decision is usable but not fully justified, record both the decision and the gap.

### Lifecycle and suppression

Prefer marking over deleting.

Useful fields:

- `status`: `active`, `resolved`, `superseded`, `rejected`, `erroneous`
- `visibility`: `normal`, `muted`, `hidden`

Deletion should be rare and reserved for malformed records, duplicates, or obvious tooling mistakes.

## Visualizer Contract

### Architecture

The visualizer should follow this pipeline:

1. load graph JSON
2. validate and normalize
3. select filtered subgraph
4. build internal render model
5. emit backend output

Do not let individual backends re-interpret selection semantics independently.

### Filtering

Default behavior should show useful current reasoning.

- suppress muted branches unless explicitly requested
- suppress hidden branches unless explicitly requested
- suppress non-current statuses unless explicitly requested

Important flags:

- `--include-muted`
- `--include-hidden`
- `--all-visibility`
- `--all-status`
- `--full-graph`
- `--focus`
- `--depth`
- `--strict`

### Output safety

Renderer output must be safe.

- no mutation of source graph files
- use atomic writes for output files
- fail before writing output under `--strict` when dangling edges or equivalent hard failures are present

### Current backend priority

Backend order:

1. Graphviz
2. Mermaid
3. terminal inspection view

Graphviz is the primary expressive backend. Mermaid is a portability export. Terminal output is for quick inspection, not spatial ASCII art.

## Development Workflow

### Design first

Before adding behavior:

- brainstorm the design
- write or update a design doc in `docs/plans/`
- keep the design scoped and explicit

Use the repo’s existing plans as precedent.

### Isolated work

- use a git worktree for feature work
- keep `.worktrees/` ignored
- do not implement on `main`

### Testing

Prefer scenario-based tests over micro-tests detached from real use.

- preserve red/green boundaries between layers
- test loader/filter behavior separately from renderer behavior
- keep tests aligned to the actual contract, not accidental serialization details
- use standard library tooling unless there is a clear reason not to

### Dogfooding

When improving the reasoning-map skill, prefer A/B-style evaluation:

- compare current and previous skill versions in isolated directories
- use no-context subagents where possible
- give the same seeded problems to both versions
- compare graph growth, topic coverage, edge-case surfacing, depth of consideration, and latent-memory usefulness

Do not treat long-tail sprawl as automatic value. Favor graphs where important nodes carry meaningful weight and weak branches are explicit but not dominant.

### Documentation

Update relevant docs when behavior changes.

Current important docs:

- `docs/reasoning-map-usage.md`
- `docs/plans/2026-09-01-reasoning-map-skill-design.md`
- `docs/plans/2026-09-01-reasoning-map-visualizer-design.md`

## Repository Layout

- `skills/reasoning-map/`: skill contract and references
- `tools/reasoning_map_visualizer/`: loader, filter, render model, and exporters
- `tests/reasoning_map_visualizer/`: scenario-based tests for loader, filtering, and renderers
- `docs/plans/`: design and implementation plans
- `docs/reasoning-map-usage.md`: repo-level usage guidance

## Current Open Work

- implement Mermaid backend
- implement terminal inspection backend
- decide how strict loader validation should become beyond structural checks
- forward-test the skill and visualizer together with broader A/B evaluation

## Guardrails

- keep the reasoning-map JSON artifact as the only persisted contract between authoring and rendering
- avoid ontology growth unless repeated use demonstrates real need
- prefer explicit links over narrative padding
- preserve abandoned reasoning paths through status and visibility instead of destructive cleanup
- keep renderer logic read-only and backend-agnostic until the final emission step
