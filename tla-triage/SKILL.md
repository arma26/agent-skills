---
name: tla-triage
description: "Use when a code or design change might need bounded TLA+ modeling before implementation because correctness depends on allowed or forbidden sequences across boundaries such as network, filesystem, timers, persistence, cryptographic state, or session state; especially when replay, retries, stale state, duplicate delivery, recovery, approval, authority, or trust transitions drive the risk."
version: 0.1.0
author: Austin, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [formal-methods, tla+, modeling, verification, design]
    related_skills: [hermes-agent-skill-authoring]
---

# TLA Triage

## Overview

Use this skill to decide whether risky work should be gated behind a bounded
TLA+ modeling pass before implementation.

The point is not to model everything. The point is to model the narrow workflow
where safety depends on ordering, side effects, replay, retries, stale state,
or authority transitions rather than correctness inside one local step.

If a repository already carries its own stricter TLA policy, ADR, or local
skill, treat that repository-local rule as an override after reading this
global skill.

## Triage

Classify the work into exactly one outcome:

- `model-required`
- `model-not-useful`
- `model-optional-but-skipped`

Default to brief triage first when the case is borderline.

Choose `model-required` when any of these apply:

- the change alters authority, approval, membership, recovery, retry, resume,
  revocation, consensus, permission-bearing transitions, or trust broadening;
- one workflow crosses two or more boundaries such as network, filesystem,
  timers or timeouts, permissions, local persistence, process execution, or
  cryptographic or session state;
- actors, retries, replays, stale artifacts, or ordering constraints determine
  whether the behavior is safe;
- confidence would otherwise require a large scenario matrix for duplicate
  delivery, supersession, replay safety, or out-of-order steps.

Choose `model-not-useful` when the real risk is mostly within one operation:

- pure algorithmic or numeric correctness;
- parsing, formatting, validation, or serialization logic with no meaningful
  cross-step state;
- UI or presentation changes;
- performance-only work;
- local refactors with no semantic state change;
- linear single-process flows with straightforward guard clauses and no replay,
  retry, stale state, or authority boundary.

Choose `model-optional-but-skipped` only when TLA+ could be relevant but the
bounded model would add little beyond cheaper verification. In that case,
record why the skipped model would be low-value and what verification method
replaces it.

Tie-breaker:

- use TLA+ when confidence depends on allowed or forbidden sequences across
  boundaries;
- do not use TLA+ when confidence depends mainly on correctness within one
  step.

## Required Outputs

For each invocation, leave a short written record wherever the repository keeps
design notes or plans.

For `model-not-useful` or `model-optional-but-skipped`, record:

- the risk being evaluated;
- why TLA+ is a poor fit or not worth the cost;
- which cheaper verification method should be used instead.

For `model-required`, the design note must also define:

- the risky workflow and control surface being modeled;
- actors, resources, boundaries crossed, and ordering points;
- three to seven invariants or forbidden states that matter;
- what implementation details are intentionally omitted from the model.

## Model-Required Workflow

When the case is `model-required`, follow this sequence:

1. Inspect relevant ADRs, existing model directories, plans, and code
   surfaces.
2. Write the TLA design note in the repository’s design or planning area.
3. Define the smallest model slice that can falsify the risky assumptions.
4. Create or update the repository’s model directory, `.tla` specs, and
   matching `.cfg` files.
5. Run TLC using the repository’s preferred wrapper or direct `tla2tools`
   invocation.
6. Record what was checked, what bound was used, what was omitted, and whether
   any counterexample changed the design.
7. Only after the modeling pass is complete, write an implementation plan or
   begin code changes.

Do not shortcut this by writing tests first when the core uncertainty is
workflow ordering or state interaction.

## Modeling Heuristics

Use these heuristics as constraints:

- model semantics, not code layout;
- start from invariants and forbidden states, then keep only enough state to
  falsify them;
- use the smallest slice that can expose the dangerous assumption;
- bound actors and resources aggressively;
- abstract payload bytes, exact crypto algorithms, wall-clock precision, UI
  structure, and production module layout unless those details are the actual
  risk;
- model replay, stale artifacts, duplicate delivery, supersession, and
  out-of-order steps explicitly when they matter;
- prefer separate slices over one large combined model;
- reduce the model rather than weakening invariants when TLC state space grows
  too large;
- treat counterexamples as design defects first and modeling defects second.

## Decomposition Rules

Model one bounded control surface per slice.

Derive the slice in this order:

1. name the risky workflow;
2. identify actors, resources, boundaries crossed, and ordering points;
3. derive three to seven invariants that would matter if violated;
4. choose the abstraction boundary;
5. choose the smallest useful actor and resource bounds.

Warn yourself when any of these happen:

- the spec starts mirroring production modules or class structure;
- unrelated concerns are combined into one model;
- the property is being weakened just to make TLC finish.

If one artifact boundary cleanly separates two concerns, split them into
separate models.

## TLC Summary

After TLC runs, summarize the result in prose:

- what was checked;
- what bounds were used;
- what was intentionally omitted;
- whether the model found a contradiction or forced a design change.

Do not treat a passing TLC run as stronger than the abstraction boundary you
chose.
