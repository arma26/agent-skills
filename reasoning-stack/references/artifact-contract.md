# Reasoning transfer artifact contract

## Authority

The reasoning-map JSON graph is the durable reasoning source model. A handoff is a derived projection for one assignment and one source revision. A residual contract ledger is execution support, not a second reasoning graph.

## Package shape

Follow repository conventions when they exist. Otherwise use:

```text
reasoning/
  <task-map>.json
  handoffs/
    <assignment>.md
    <assignment>-ledger.yaml
```

Embed a small ledger directly in the handoff. Split it into YAML when independent review or machine processing benefits from a separate file.

## Handoff fields

```yaml
generated_from:
  map: reasoning/<task-map>.json
  cluster:
    - decision.example
    - risk.example
  revision: sha256:<digest>

mission: One bounded objective.
assignment_boundary:
  may_change: []
  must_not_change: []
  may_reconsider_when: []

signals:
  - id: stable-signal-id
    type: objective | constraint | preference | tension | anomaly | risk | leverage | boundary | stopping | escalation
    priority: 1
    strength: high | medium | low
    confidence: high | medium | low
    observation: Directly supported source pattern.
    signal: Smallest interpretation that changes action.
    trigger: Condition that activates the signal.
    behavioral_effect: Change to the next action or decision.
    course_correction: Recovery when drift appears.
    release_condition: Evidence that weakens or retires it.
    rival_interpretation: Strongest plausible alternative explanation.
    public_seam: Observable boundary where the claim must hold.
    proof_matrix:
      runtime: Positive observable proof or not-applicable reason.
      type_or_structure: Static proof or not-applicable reason.
      adversarial: Cheapest falsifying probe.
      compatibility: Existing behavior that must remain unchanged.
    validation: Concrete test that could confirm or reject the signal.
    provenance: []

residual_contract_ledger:
  - obligation: Ordinary requirement or preservation rule.
    source: Spec, test, interface, or observed compatibility behavior.
    seam: Observable boundary.
    dimensions: [runtime, type, compatibility, fixture, ordering, documentation]
    positive_proof: Evidence of success.
    negative_probe: Misuse or failure that must be rejected.
    affected_callers: []
    preservation_rule: Behavior that must not disappear.
    status: open | verified | unresolved

constraints: []
assumptions: []
open_questions: []
rejected_paths: []
execution_hooks:
  intent_scaffolding:
    required_when: Assignment adds or changes code behavior.
    persistence: ephemeral
    closure_evidence: intent scaffold and post-implementation drift findings
refresh_triggers:
  - assigned scope changes
  - source map revision changes
  - a signal release condition fires
  - new evidence contradicts a governing signal
instructions_boundary: What the receiver may and may not reconsider.
```

## Revision rules

Prefer a selected-cluster content hash when the map artifact is stable and cheap to hash. Otherwise use an explicit monotonic map revision plus the selected node ids. Do not use wall-clock time alone as a revision identity.

A handoff is stale when its selected cluster changes materially, not merely when unrelated map metadata changes. A whole-map hash may be recorded for provenance, but do not use unrelated whole-map churn as the only staleness trigger. Reconcile by regenerating the projection or recording the exact accepted divergence.

## Minimal handoff

A legitimate Mosaic fast exit still produces a useful map-backed packet when delegation is required:

```yaml
generated_from: {map: reasoning/task.json, cluster: [goal.task], revision: 4}
mission: Execute the bounded task.
signals: []
residual_contract_ledger:
  - obligation: No additional acceptance or preservation obligations were found beyond the explicit mission and constraints.
    source: Bounded source review.
    seam: Assignment boundary.
    dimensions: []
    positive_proof: Direct task acceptance check.
    negative_probe: Scope does not broaden beyond the mission.
    affected_callers: []
    preservation_rule: Preserve explicit constraints.
    status: verified
constraints: []
open_questions: []
refresh_triggers: [assigned scope changes, source map revision changes]
instructions_boundary: Do not broaden the task.
```

Do not add empty signal cards or speculative risks.

## Signal outcomes

After execution, classify each transferred signal:

- `held` — evidence supported it and it usefully governed action;
- `weakened` — partially useful, but evidence reduced confidence or scope;
- `released` — its release condition fired or the interpretation was rejected;
- `unresolved` — execution did not discriminate among live interpretations.

Merge these outcomes into existing map nodes or edges when they have future reasoning value. Do not add one graph node per handoff field.

## Closure review input

A closure reviewer needs:

- original bounded source;
- source map path, cluster, and revision;
- handoff and ledger;
- produced result or diff;
- actual verification output.
- intent scaffold and drift findings for behavioral code changes.

The reviewer should not be told which signals are expected to be correct. It checks the result against the source and ledger independently.

The scaffold is local execution evidence, not a durable reasoning artifact. Merge back only new evidence, changed constraints, signal outcomes, rejected paths, or gaps that remain useful after the implementation context is gone.
