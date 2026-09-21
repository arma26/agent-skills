# Reasoning Map Skill Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Create a reusable skill that builds and stress-tests rootless reasoning maps as mutable JSON graphs for agent reasoning, investigation, documentation support, and ADR preparation.

**Architecture:** The skill will live as a self-contained skill folder with a concise `SKILL.md`, a small set of reference files, and example graph artifacts. The skill will guide agents to create and revise a rootless graph with first-class edges, explicit deficiencies, and non-destructive suppression of weak branches.

**Tech Stack:** Markdown skill files, JSON example artifacts, optional shell-based validation through existing repo tooling if introduced.

---

### Task 1: Create the skill skeleton

**Files:**
- Create: `skills/reasoning-map/SKILL.md`
- Create: `skills/reasoning-map/agents/openai.yaml`
- Create: `skills/reasoning-map/references/schema.md`
- Create: `skills/reasoning-map/references/workflows.md`
- Create: `skills/reasoning-map/examples/minimal-graph.json`

**Step 1: Create the folder structure**

Run: `mkdir -p skills/reasoning-map/agents skills/reasoning-map/references skills/reasoning-map/examples`
Expected: directories created with no output

**Step 2: Draft `SKILL.md` frontmatter and trigger description**

Write concise metadata that triggers on brainstorming, reasoning structure, argument mapping, issue investigation, and ADR support.

**Step 3: Draft the skill workflow**

In `skills/reasoning-map/SKILL.md`, define:

- when to use the skill
- the rootless graph model
- required node and edge expectations
- deficiency and visibility rules
- the three operating modes: `map`, `stress-test`, `extract`

**Step 4: Add skill UI metadata**

Create `skills/reasoning-map/agents/openai.yaml` with deterministic values aligned to `SKILL.md`.

**Step 5: Commit**

```bash
git add skills/reasoning-map
git commit -m "feat: scaffold reasoning-map skill

- add skill skeleton and metadata
- add schema and workflow references
- add example reasoning graph artifact"
```

### Task 2: Write the schema reference

**Files:**
- Modify: `skills/reasoning-map/references/schema.md`
- Test: `skills/reasoning-map/examples/minimal-graph.json`

**Step 1: Write the schema guidance**

Document:

- core node kinds
- optional roles
- required node fields
- edge types
- lifecycle fields
- deficiency fields

**Step 2: Add a complete minimal example**

Create `skills/reasoning-map/examples/minimal-graph.json` showing:

- at least one problem
- one subproblem
- one decision
- one gap
- edges for `causes`, `addresses`, and `challenges`

**Step 3: Review for over-modeling**

Verify the reference does not introduce more kinds or fields than the design requires.

**Step 4: Commit**

```bash
git add skills/reasoning-map/references/schema.md skills/reasoning-map/examples/minimal-graph.json
git commit -m "feat: define reasoning-map schema reference

- document nodes edges and lifecycle fields
- add minimal graph example
- keep ontology compact for agent use"
```

### Task 3: Write the workflow reference

**Files:**
- Modify: `skills/reasoning-map/references/workflows.md`

**Step 1: Write the mapping workflow**

Describe how to:

- start from a problem or question
- add context and decomposition
- connect claims, risks, constraints, options, and gaps

**Step 2: Write the stress-test workflow**

Describe checks for:

- missing evidence
- untested assumptions
- no alternatives
- no counterarguments
- unmitigated risks
- weak decision rationale

**Step 3: Write the extraction workflow**

Describe how to derive:

- ADR inputs
- issue investigation summaries
- design notes
- documentation outlines

**Step 4: Commit**

```bash
git add skills/reasoning-map/references/workflows.md
git commit -m "feat: add reasoning-map operating workflows

- define map stress-test and extract modes
- include investigation and ADR preparation guidance
- surface deficiency checks explicitly"
```

### Task 4: Validate the skill contents against the design

**Files:**
- Modify: `skills/reasoning-map/SKILL.md`
- Modify: `skills/reasoning-map/references/schema.md`
- Modify: `skills/reasoning-map/references/workflows.md`

**Step 1: Review for trigger quality**

Check that the skill description and body make it obvious when this skill should trigger.

**Step 2: Review for context economy**

Reduce duplication between `SKILL.md` and reference files. Keep only procedural essentials in `SKILL.md`.

**Step 3: Review for design alignment**

Confirm all of the following:

- rootless graph, not centered tree
- mutable JSON artifact for MVP
- stable node ids
- first-class edges
- visible deficiencies
- non-destructive suppression instead of pruning
- ADR extraction boundary is clear

**Step 4: Optional validation command**

If a local validation script or skill initialization helper is introduced, run it here. Otherwise perform a manual review and capture any gaps in the commit message body.

**Step 5: Commit**

```bash
git add skills/reasoning-map
git commit -m "refactor: tighten reasoning-map skill guidance

- align skill text with approved design
- reduce duplication across references
- verify lifecycle and deficiency rules"
```

### Task 5: Add repo-level documentation for use

**Files:**
- Create: `docs/reasoning-map-usage.md`

**Step 1: Write brief usage documentation**

Document:

- what the skill is for
- where graph artifacts should live
- how it relates to ADR creation
- what is intentionally out of scope for the MVP

**Step 2: Check path hygiene**

Verify all paths are repo-relative and no local machine paths are referenced.

**Step 3: Commit**

```bash
git add docs/reasoning-map-usage.md
git commit -m "docs: add reasoning-map usage guide

- describe intended use across design and investigation
- define ADR relationship and MVP scope
- keep file references repo-relative"
```
