# Reasoning Map Schema

Use a mutable JSON graph for the MVP. Keep the graph rootless and edge-centric.

## Top-Level Shape

```json
{
  "schema_version": "0.1.0",
  "graph_id": "reasoning-map.retry-storms",
  "title": "Short topic label",
  "scope": "service.retry-policy",
  "status": "active",
  "nodes": [],
  "edges": []
}
```

The top-level object is a container, not a semantic root. Do not force all nodes to descend from a single origin.

Recommended top-level metadata:

- `graph_id`: stable identifier for the map
- `title`: human-readable label
- `scope`: short boundary label for the current reasoning cluster
- `status`: `active`, `paused`, `resolved`, or similar workflow state
- `related_graphs`: optional list of related graph ids when work forks across documents or sessions

## Core Node Kinds

Use a compact kind list:

- `question`
- `problem`
- `goal`
- `claim`
- `option`
- `constraint`
- `risk`
- `decision`
- `gap`

Use `role` or linked nodes for more specific perspective such as:

- `cause`
- `detriment`
- `component`
- `dependency`
- `mitigation`
- `obstacle`
- `support`
- `counterpoint`
- `example`
- `consequence`
- `assumption`
- `subproblem`

Promote a concept into its own node when it has multiple important relationships or must be reasoned about independently.

Keep the core kind list small. For the MVP, treat observations and evidence as:

- `claim` nodes with a clear `role`
- linked support or challenge structure
- concise summaries rather than a separate evidence ontology

Add a first-class `evidence` kind only if repeated usage shows the distinction is operationally necessary rather than just semantically attractive.

When facts and inferences must stay separate, represent both explicitly:

- use a `claim` node with a fact-oriented role such as `observation` for direct findings
- use a separate `claim` node with an inference-oriented role such as `cause` or `interpretation`
- link them through `supports`, `challenges`, or `causes` rather than blending them into one node

Do not let one node simultaneously stand for both "what was observed" and "what that observation means" when the distinction affects a decision.

## Node Id Strategy

Use semantic, stable ids:

- `problem.retry-storms`
- `claim.latency-spike-observed`
- `decision.safer-retry-defaults`

Rules:

- prefix with the node kind
- use short kebab-style semantic labels
- avoid sequence-only ids like `n1` unless the graph is purely temporary
- keep the id stable even if `title` or `summary` improves
- add a numeric suffix only when two distinct nodes would otherwise collide

When duplicate nodes are discovered:

- prefer one canonical id
- redirect future edges to the canonical id
- mark the duplicate `superseded`, `erroneous`, or `muted`
- reserve hard deletion for obvious tooling mistakes

## Required Node Fields

- `id`
- `kind`
- `title`
- `status`
- `deficiencies`

Strongly preferred fields:

- `summary`
- `role`
- `assertion_kind`
- `confidence`
- `importance`
- `completeness`
- `latent_memory_value`
- `visibility`
- `relevance`
- `tags`

Example:

```json
{
  "id": "problem.retry-storms",
  "kind": "problem",
  "title": "Retry storms during upstream degradation",
  "summary": "Clients amplify load during intermittent latency spikes.",
  "status": "active",
  "confidence": 0.82,
  "importance": 0.94,
  "completeness": 0.66,
  "latent_memory_value": 0.87,
  "visibility": "normal",
  "relevance": 0.92,
  "deficiencies": ["missing_evidence"],
  "tags": ["retries", "resilience"]
}
```

For `claim` nodes, use `assertion_kind` when fact and inference need to stay distinct:

- `observation`
- `inference`
- `interpretation`
- `assumption`

## Edge Types

Edges are first-class records. Use explicit relationship types:

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

Add a new edge type only when existing types cannot carry the meaning cleanly.

## Edge Fields

Required fields:

- `id`
- `from`
- `to`
- `type`

Strongly preferred fields:

- `status`
- `confidence`
- `importance`
- `visibility`
- `relevance`

Example:

```json
{
  "id": "edge.cause.1",
  "from": "problem.backoff-clustering",
  "to": "problem.retry-storms",
  "type": "causes",
  "status": "active",
  "confidence": 0.54,
  "importance": 0.78,
  "visibility": "normal",
  "relevance": 0.73
}
```

## Lifecycle And Visibility

Use lifecycle markers instead of destructive pruning.

Recommended `status` values:

- `active`
- `resolved`
- `superseded`
- `rejected`
- `erroneous`

Recommended `visibility` values:

- `normal`
- `muted`
- `hidden`

Use `relevance` to separate low-value branches from false branches.

Reserve hard deletion for malformed records, accidental duplicates, or obvious tooling errors.

## Deficiency Flags

Treat deficiencies as explicit reasoning pressure:

- `missing_evidence`
- `untested_assumption`
- `no_alternative_considered`
- `no_counterargument`
- `no_inverse_explored`
- `unclear_constraint`
- `risk_unmitigated`
- `decision_without_rationale`
- `investigation_required`
- `stale_context`
- `ambiguous_scope`

Add a deficiency only when it influences the quality or safety of the reasoning.
Use `no_counterargument` when a claim or decision lacks meaningful pushback in
general, and `no_inverse_explored` when an important branch lacks the strongest
credible case in the opposite direction.

## Artifact Discipline

- Keep node ids stable once introduced.
- Revise node metadata when the problem statement evolves.
- Prefer explicit edges over longer node text.
- Preserve weak or rejected paths through status and visibility fields.
- Keep the ontology small enough that a fresh agent can understand it immediately.
- Let problems raise more problems without forcing a center node or single top-down hierarchy.
- Reuse an existing graph when the reasoning cluster is still the same; fork when scope drift would make the graph ambiguous.
- Prefer branch growth that is likely to reactivate future reasoning. When a long-tail branch no longer changes likely future action or framing, compress it into a summary node, muted node, or gap instead of continuing to elaborate it.

## Latent Memory Value

Use `latent_memory_value` as an optional heuristic field when a node's future retrieval value matters.

Interpret it as: how likely a future fresh agent is to need this node to make a better decision, reopen a path, or avoid repeating investigation.

Useful signals:

- proximity to an active decision, risk, or gap
- uniqueness relative to parent or sibling nodes
- likely reuse in future sessions
- whether compressing the node would lose operationally important structure

Low `latent_memory_value` does not mean deletion. It usually means:

- stop expanding the branch
- aggregate sibling leaves
- lower `visibility`
- preserve the branch in compressed form
