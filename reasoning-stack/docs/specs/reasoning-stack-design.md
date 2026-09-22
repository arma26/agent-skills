# Reasoning stack design

## Status

Proposed implementation design for the `reasoning-stack` skill.

## Problem

Reasoning maps preserve a broad, durable reasoning surface, while Mosaic Harvest derives compact behavioral signals for a bounded assignment. Used independently, they leave orchestration gaps:

- subagents may receive an entire graph when they need one cluster;
- compact handoffs can become stale without map revision provenance;
- ranked signals can hide ordinary compatibility and proof obligations;
- execution findings may never return to the durable map;
- mechanical tasks may pay for unnecessary extraction.

The repository needs one process-bearing skill that owns the transfer lifecycle without merging the reasoning-map and Mosaic contracts into another persisted source of truth.

## Goals

- Coordinate a reasoning map and Mosaic handoff as separate artifacts.
- Produce a bounded, revisioned subagent packet.
- Preserve both decision-shaping signals and exhaustive ordinary obligations.
- Take a fast path when harvesting cannot change downstream behavior.
- Require closure review against the original source, not only the ranked signals.
- Require a local intent scaffold and drift review when a delegated assignment changes code behavior.
- Merge durable evidence back into the owning map after execution.

## Non-goals

- Replace the reasoning-map JSON graph.
- Define a second reasoning graph schema.
- Make Mosaic mandatory for mechanical work.
- Turn every checklist item into a signal.
- Store execution logs in the reasoning map.
- Persist local intent scaffolds by default.
- Route users among unrelated skills.

## Artifact model

The reasoning map remains the only durable reasoning source model:

```text
reasoning/
  <task-map>.json
  handoffs/
    <assignment>.md
    <assignment>-ledger.yaml
```

The handoff is a derived projection with declared provenance:

```yaml
generated_from:
  map: reasoning/<task-map>.json
  cluster: [node.id]
  revision: <hash-or-version>
mission: <bounded objective>
signals: []
residual_contract_ledger: []
constraints: []
open_questions: []
refresh_triggers: []
instructions_boundary: <authority boundary>
```

The ledger may be embedded in the handoff when small. It is separate when independent review or machine processing benefits from a dedicated file.

## Workflow

1. **Qualify** — decide whether durable reasoning and judgment transfer are useful.
2. **Map** — create or update the narrowest owning reasoning cluster.
3. **Project** — run the Mosaic value gate and produce either a minimal packet, one-signal micro-harvest, or full signal stack plus ledger.
4. **Revision-bind** — record map path, node ids, and revision in the handoff.
5. **Dispatch** — give the subagent the handoff first; it opens the broader map only on a refresh trigger.
6. **Monitor, scaffold, and execute** — activate refresh-trigger monitoring before execution. For behavioral code changes, the subagent derives an ephemeral local intent scaffold from the handoff and surrounding code, reconciles staleness whenever a trigger fires, implements against the current scaffold, and performs drift review. Other assignments execute directly under the same staleness checks.
7. **Close** — a fresh reviewer checks the result against the original source, residual ledger, and any scaffold drift findings.
8. **Merge back** — update the map with durable evidence, signal outcomes, changed constraints, reusable rejected paths, and unresolved gaps. Do not merge the ephemeral scaffold itself.

## Fast paths

- **No map:** use a normal direct task when the work is mechanical, fully specified, and unlikely to produce reusable reasoning.
- **Map only:** preserve active exploration when no delegation boundary exists yet.
- **Minimal map-backed handoff:** use when a map exists but Mosaic finds no behavior-changing latent signal.
- **Micro-harvest:** transfer at most one signal when only one weak but useful course-correction anchor exists.
- **Full stack:** use when a fresh agent must inherit judgment, uncertainty, and ordinary proof obligations.

## Authority and staleness

The map is authoritative for the broad reasoning surface. The handoff is authoritative only for its assignment and source revision.

Refresh the handoff when:

- assigned scope changes;
- source map revision changes materially;
- a signal release condition fires;
- new evidence contradicts a governing signal;
- the receiving agent must reconsider an excluded branch.

A stale handoff must be regenerated or explicitly reconciled. It must not silently override a newer map.

## Closure discipline

Signals are selective; closure is exhaustive. The reviewer receives:

- original task or bounded source;
- source map cluster and revision;
- residual contract ledger;
- produced result or diff;
- verification evidence.

The review checks public seams, runtime behavior, type or structural contracts, negative probes, compatibility behavior, ordering, cleanup, fixtures, callers, unsupported cases, and scope creep.

For behavioral code changes, the reviewer also receives the intent scaffold and post-implementation drift findings. The scaffold explains the local implementation story; it does not replace the ledger or broaden the assignment.

## Merge-back discipline

Merge only information likely to change future action, risk, or framing:

- new observations or evidence;
- signals marked `held`, `weakened`, `released`, or `unresolved`;
- changed constraints;
- reusable rejected paths;
- remaining ledger gaps;
- newly distinct reasoning clusters.

Keep routine logs, completed checklist items, and transient implementation details in tests, task records, or handoff history.

## Acceptance criteria

- The skill defines a clear fast exit and does not require Mosaic for low-value tasks.
- The persisted reasoning-map JSON remains the only durable reasoning source model.
- Every map-derived handoff identifies source path, node ids, and revision.
- The handoff separates ranked signals from the residual contract ledger.
- Refresh triggers make staleness explicit.
- Closure review uses the original source and ledger, not only the signals.
- Behavioral code assignments run intent scaffolding after handoff and before implementation, then include drift findings in closure review.
- Intent scaffolds remain ephemeral unless the user or repository explicitly requires persistence.
- Merge-back preserves durable evidence without polluting the map with logs.
- Repository validation passes and the root README lists the new component.
