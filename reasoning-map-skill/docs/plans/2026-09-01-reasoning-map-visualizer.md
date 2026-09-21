# Reasoning Map Visualizer Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a standalone Python visualizer that reads reasoning-map JSON artifacts and emits Graphviz, Mermaid, and terminal inspection views with consistent filtering semantics.

**Architecture:** Implement a small shared core for loading, validating, normalizing, and filtering reasoning-map graphs, then route the filtered subgraph into backend-specific emitters for DOT, Mermaid, and terminal text. Keep the tool read-only and independent from skill invocation, sharing only the graph JSON contract.

**Tech Stack:** Python standard library, `unittest`, JSON fixtures, CLI via `argparse`.

---

### Task 1: Add visualizer test fixtures and failing tests

**Files:**
- Create: `tests/reasoning_map_visualizer/fixtures/sample_graph.json`
- Create: `tests/reasoning_map_visualizer/test_visualize.py`

**Step 1: Write a fixture graph**

Create `tests/reasoning_map_visualizer/fixtures/sample_graph.json` with:

- active, muted, and hidden nodes
- active and rejected statuses
- at least one dangling edge fixture variant or inline test case
- one decision cluster suitable for focus rendering

**Step 2: Write failing tests for default filtering**

Add tests that invoke the CLI or backend entrypoints and assert:

- default output excludes muted and hidden nodes
- default output excludes non-current statuses

**Step 3: Run tests to verify failure**

Run: `python -m unittest tests.reasoning_map_visualizer.test_visualize -v`
Expected: FAIL because the visualizer modules do not exist yet

**Step 4: Commit**

```bash
git add tests/reasoning_map_visualizer
git commit -m "test: add reasoning-map visualizer fixtures and failing tests"
```

### Task 2: Implement loader and filter core

**Files:**
- Create: `tools/reasoning_map_visualizer/__init__.py`
- Create: `tools/reasoning_map_visualizer/loader.py`
- Create: `tools/reasoning_map_visualizer/filters.py`
- Modify: `tests/reasoning_map_visualizer/test_visualize.py`

**Step 1: Implement loader**

Load JSON graphs, validate required top-level keys, normalize optional fields, and preserve unknown fields without mutation.

**Step 2: Implement filtering**

Implement:

- default visibility filtering
- `--include-muted`
- `--include-hidden`
- `--all-visibility`
- `--all-status`
- `--full-graph`
- `--focus`
- `--depth`

**Step 3: Add or refine unit tests**

Cover:

- default filtered subgraph
- full-graph selection
- focused neighborhood selection
- dangling edge handling inputs

**Step 4: Run tests**

Run: `python -m unittest tests.reasoning_map_visualizer.test_visualize -v`
Expected: some tests still fail because emitters and CLI are not implemented

**Step 5: Commit**

```bash
git add tools/reasoning_map_visualizer tests/reasoning_map_visualizer/test_visualize.py
git commit -m "feat: add reasoning-map visualizer loader and filters"
```

### Task 3: Implement Graphviz emitter and CLI

**Files:**
- Create: `tools/reasoning_map_visualizer/emit_dot.py`
- Create: `tools/reasoning_map_visualizer/visualize.py`
- Modify: `tests/reasoning_map_visualizer/test_visualize.py`

**Step 1: Write failing Graphviz-specific tests**

Add tests for:

- DOT header and footer
- node labels present for selected nodes
- muted and rejected content shown under override flags
- strict mode failing on dangling edges

**Step 2: Run tests to verify failure**

Run: `python -m unittest tests.reasoning_map_visualizer.test_visualize -v`
Expected: FAIL on missing DOT emitter or CLI behavior

**Step 3: Implement minimal DOT backend**

Emit valid DOT text with:

- graph title
- node shape by kind
- status and deficiency styling
- edge labels by type

**Step 4: Implement CLI argument parsing**

Parse arguments, load graph, apply filters, select backend, and write to stdout or `--output`.

**Step 5: Run tests to verify pass**

Run: `python -m unittest tests.reasoning_map_visualizer.test_visualize -v`
Expected: Graphviz-related tests PASS; Mermaid and terminal tests may still fail

**Step 6: Commit**

```bash
git add tools/reasoning_map_visualizer tests/reasoning_map_visualizer/test_visualize.py
git commit -m "feat: add Graphviz reasoning-map renderer"
```

### Task 4: Implement Mermaid and terminal backends

**Files:**
- Create: `tools/reasoning_map_visualizer/emit_mermaid.py`
- Create: `tools/reasoning_map_visualizer/emit_terminal.py`
- Modify: `tests/reasoning_map_visualizer/test_visualize.py`

**Step 1: Write failing backend tests**

Add tests that assert:

- Mermaid emits flowchart text for the selected subgraph
- terminal mode emits readable node and edge summaries
- all three backends operate on the same filtered selection

**Step 2: Run tests to verify failure**

Run: `python -m unittest tests.reasoning_map_visualizer.test_visualize -v`
Expected: FAIL for Mermaid and terminal output expectations

**Step 3: Implement Mermaid backend**

Emit portable topology with compact labels and minimal class styling.

**Step 4: Implement terminal backend**

Emit text-first inspection output with:

- graph header
- node list
- edge list
- deficiency markers
- useful focus rendering

**Step 5: Run tests to verify pass**

Run: `python -m unittest tests.reasoning_map_visualizer.test_visualize -v`
Expected: PASS

**Step 6: Commit**

```bash
git add tools/reasoning_map_visualizer tests/reasoning_map_visualizer/test_visualize.py
git commit -m "feat: add Mermaid and terminal reasoning-map renderers"
```

### Task 5: Document usage and verify end-to-end behavior

**Files:**
- Modify: `docs/reasoning-map-usage.md`
- Modify: `skills/reasoning-map/SKILL.md`
- Modify: `skills/reasoning-map/references/workflows.md`

**Step 1: Document the visualizer boundary**

Update docs to state:

- the visualizer is separate from the skill
- how to invoke the CLI
- what `--full-graph` and related flags do

**Step 2: Wire the skill references**

Update the skill docs only enough to point users to the separate visualizer when rendering is desired. Do not couple skill usage to the renderer.

**Step 3: Run end-to-end verification**

Run:

- `python -m unittest tests.reasoning_map_visualizer.test_visualize -v`
- `python tools/reasoning_map_visualizer/visualize.py tests/reasoning_map_visualizer/fixtures/sample_graph.json --format dot`
- `python tools/reasoning_map_visualizer/visualize.py tests/reasoning_map_visualizer/fixtures/sample_graph.json --format mermaid`
- `python tools/reasoning_map_visualizer/visualize.py tests/reasoning_map_visualizer/fixtures/sample_graph.json --format terminal`
- `python tools/reasoning_map_visualizer/visualize.py tests/reasoning_map_visualizer/fixtures/sample_graph.json --format dot --full-graph`

Expected:

- tests pass
- commands exit successfully
- output includes or suppresses nodes according to the selected flags

**Step 4: Commit**

```bash
git add docs/reasoning-map-usage.md skills/reasoning-map tools/reasoning_map_visualizer tests/reasoning_map_visualizer
git commit -m "docs: add reasoning-map visualizer usage and integration notes"
```
