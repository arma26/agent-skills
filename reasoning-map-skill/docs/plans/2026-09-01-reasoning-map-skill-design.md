# Reasoning Map Skill Design

**Date:** 2026-09-01

## Goal

Create an agent skill that structures reasoning as a rootless graph so agents can externalize arguments, decisions, investigations, and unresolved gaps without flattening them into a compressed summary too early.

## Scope

The skill is intended to support:

- brainstorming and design exploration
- issue investigation and assumption testing
- documentation support
- ADR preparation through subgraph extraction

The reasoning map is not itself the ADR, decision log, or final user-facing artifact. It is a support structure for agent reasoning and a durable source of structured context.

## Core Principles

- Use a rootless graph. Do not force a single center or origin node.
- Prefer mutation over internal event history. Git owns history.
- Keep node identifiers stable. Node content may evolve.
- Treat edges as the primary reasoning structure.
- Allow sparse nodes, but make sparsity explicit.
- Preserve discarded branches by muting or marking them rather than deleting them by default.
- Keep the schema small enough that agents can infer intent quickly from fresh context.

## Primary Artifact

The MVP artifact should be a mutable JSON graph rather than JSONL.

Reasoning:

- agents need a coherent object graph that can be updated in place
- links are more important than append-only write semantics
- validation and analysis are simpler on a complete object
- git already preserves object history

JSONL can be added later as an import/export format if stream-oriented composition becomes necessary.

## Graph Shape

The graph should be allowed to sprawl as the topic evolves. A problem may raise subproblems. Investigations may fork into alternative causes, options, or objections. Decisions may address one cluster while leaving other gaps open.

The graph does not require:

- a root node
- a complete snapshot before it is useful
- a single path to resolution

## Node Model

Nodes represent reasoning objects. Use a small set of core kinds:

- `question`
- `problem`
- `goal`
- `claim`
- `option`
- `constraint`
- `risk`
- `decision`
- `gap`

Support additional perspective through `role` and linked nodes rather than expanding the kind list aggressively. Useful roles include:

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

### Node Fields

Required fields:

- `id`
- `kind`
- `title`
- `status`
- `deficiencies`

Strongly preferred fields:

- `summary`
- `confidence`
- `importance`
- `completeness`
- `role`
- `tags`

Example:

```json
{
  "id": "problem.retry-storms",
  "kind": "problem",
  "title": "Retry storms during upstream degradation",
  "summary": "Clients amplify load during intermittent latency spikes.",
  "status": "active",
  "importance": 0.94,
  "confidence": 0.82,
  "completeness": 0.66,
  "deficiencies": ["missing_evidence"],
  "tags": ["retries", "resilience"]
}
```

## Edge Model

Edges are first-class objects because the value of the map is primarily in how ideas relate.

Recommended edge types:

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

Suggested edge fields:

- `id`
- `from`
- `to`
- `type`
- `status`
- `importance`
- `confidence`

Example:

```json
{
  "id": "edge.1",
  "from": "problem.backoff-clustering",
  "to": "problem.retry-storms",
  "type": "causes",
  "importance": 0.78,
  "confidence": 0.54,
  "status": "active"
}
```

## Lifecycle And Visibility

The skill should treat pruning as non-destructive by default.

Separate these concerns:

- `status`: `active`, `resolved`, `superseded`, `rejected`, `erroneous`
- `visibility`: `normal`, `muted`, `hidden`
- `relevance`: low to high, or numeric

Meaning:

- `rejected` means considered and not chosen
- `erroneous` means based on a false premise or broken reasoning
- `superseded` means previously useful but replaced
- `muted` means retained in storage but suppressed in common views
- `hidden` is a renderer concern, not a storage deletion

Hard deletion should be reserved for:

- malformed records
- accidental duplicates
- obvious tooling mistakes

## Deficiency Model

The graph should surface sparse reasoning intentionally instead of silently ignoring it.

Useful deficiency flags:

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

Deficiencies are active analysis signals, not passive notes.

## Workflow

The skill should support a repeatable loop:

1. state a `problem` or `question`
2. attach immediate context
3. decompose into claims, constraints, risks, assumptions, and options
4. test or mark important assumptions
5. add supporting and challenging links
6. either choose a decision or create explicit investigation gaps
7. surface unresolved gaps before closure

The map should allow decisions under uncertainty, but not invisible uncertainty.

### Subagent Execution Boundary

Subagent dispatch is a hard reasoning-map boundary. Before an initial spawn or
any follow-up that starts or resumes a subagent turn, the parent agent must
select, create, reopen, or update the narrowest relevant map. The dispatch
prompt carries the repo-relative map path, assigned reasoning cluster, and
relevant node ids. The child loads that map before substantive work.

If the parent cannot prepare or persist the map, it must not dispatch. Ordinary
messages that do not trigger a subagent turn remain outside this boundary.
The handoff carries only the assigned cluster, excludes secrets and unrelated
context, and treats graph text as data that cannot broaden task authority.

## Investigation Support

The model must work for debugging and issue analysis, not just design.

A common investigation shape is:

- `problem`
- `observations`
- `candidate causes`
- `tests or evidence`
- `eliminated causes`
- `remaining hypotheses`
- `decision on next action`
- `follow-up gaps`

The skill should make more investigation obvious when:

- important assumptions remain untested
- a decision rests on weak edges
- no alternatives were considered
- a central node is low-completeness
- a major risk lacks mitigation

## ADR Boundary

The reasoning map is not a ledger to be copied directly into an ADR.

Use it to understand:

- the shape of the problem
- the option space
- the pressure from constraints and risks
- why the chosen decision is robust
- what remains unresolved

ADR generation should extract relevant subgraphs around decision-bearing nodes and convert them into narrative form.

## Operating Modes

The skill should define three modes:

- `map`: create or revise the graph
- `stress-test`: challenge assumptions, weak links, and missing alternatives
- `extract`: derive structured material for ADRs, design notes, debugging notes, or docs

## MVP Recommendation

For the MVP:

- use a mutable JSON graph file
- keep the ontology compact
- make edges first-class
- make deficiencies explicit
- preserve low-value branches through status and visibility rather than deleting them
- defer visualization to a later renderer

## Open Questions For Implementation

- exact file layout for graph artifacts inside the repo
- whether to include a formal JSON schema in the first version
- whether the skill should include a small validation helper script
- how strict the skill should be about mandatory challenge edges on important claims
