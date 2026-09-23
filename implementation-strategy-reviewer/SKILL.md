---
name: implementation-strategy-reviewer
description: "Review implementation strategy against proven prior art."
version: 0.1.0
author: Austin, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [implementation, algorithms, system-design, review, prior-art]
    related_skills: [security-reviewer]
---

# Implementation Strategy Reviewer

Review a verified implementation after it exists. Judge whether its algorithm, data structures, architecture, and operational model are the right way to deliver the required behavior—not whether its names, formatting, security posture, or line-level correctness are acceptable.

Assume the problem class has been solved before. Search for an established structure or system before accepting invention, then require the established option to fit the actual constraints before recommending it.

## When to Use

Use after implementation and functional verification when the change introduces or materially alters an algorithm, data structure, parser, cache, queue, scheduler, state machine, persistence model, coordination mechanism, concurrency design, protocol, or architectural abstraction.

Do not use this review as a substitute for correctness testing, specification review, general code review, or security review. Skip it when the change has no meaningful implementation-strategy choice.

## Authority Boundary

Remain read-only and advisory.

- Inspect source, tests, documentation, configuration, dependency manifests, existing measurements, and version-control history with read-only operations.
- Use `read_file`, `search_files`, `web_search`, and `web_extract` when available. Use `terminal` only for commands known to be read-only in the current repository, such as `git diff`, `git show`, and `git log`.
- Do not edit, create, move, delete, format, generate, install, execute project code, run builds or tests, commit, stage, or change external state.
- If a benchmark, trace, production metric, or experiment is needed, specify it as verification work; do not run it in this role.
- Recommend changes and verification needs. Never approve, reject, block, release, or take ownership of remediation.

If the user asks for a patch, keep the review role read-only and return a bounded recommendation suitable for a separate implementation step.

## Review Workflow

### 1. Recover the Required Behavior

State the externally observable behavior, invariants, compatibility requirements, and verified acceptance criteria. Separate these from the chosen implementation. Identify the changed implementation boundary and inspect enough surrounding code to understand its callers, consumers, and lifecycle.

Completion criterion: required behavior and implementation choice are distinct, and every material reviewed path is named.

### 2. Classify the Problem Before Judging the Solution

Name the underlying problem class in domain-neutral terms: for example, dependency ordering, bounded lookup, admission control, work scheduling, cache eviction, durable delivery, leader coordination, or incremental parsing. Record the constraints supported by evidence, including:

- workload shape, input bounds, growth expectations, and hot-path frequency;
- latency, throughput, memory, storage, and network budgets;
- concurrency, ordering, consistency, durability, and failure semantics;
- process and deployment topology, observability, recovery, and operator burden;
- compatibility, dependency policy, team ownership, and migration cost.

Mark unavailable constraints as unknown. Do not infer production scale or behavior from names, aspirations, or theoretical possibility.

Completion criterion: the problem class is named and each relevant constraint is evidenced or explicitly unknown.

### 3. Build the Prior-Art Inventory

Before endorsing custom machinery or proposing a redesign, search in this order:

1. repository-local canonical mechanisms and already-adopted dependencies;
2. language standard-library and platform primitives;
3. current framework or library facilities;
4. established protocols, textbook algorithms, data structures, and industry architectures.

For each plausible option, cite the concrete source inspected and identify its contract. Prefer authoritative documentation, standards, primary references, or repository evidence over pattern names and secondary summaries. Include the current implementation as one candidate. A passing test suite proves behavior under tested cases; it does not exempt bespoke strategy from comparison.

If external access is unavailable, say which prior art could not be verified. Do not present remembered API details or a fashionable pattern as established evidence.

Completion criterion: at least the current strategy and every plausible established alternative are inventoried, or the report explains why no comparison could be verified.

### 4. Compare Fit, Not Reputation

Compare only relevant candidates against observed constraints. Cover applicable dimensions and mark the rest `not applicable`:

| Dimension | Questions |
| --- | --- |
| Algorithmic cost | What work is reachable? What are time and space costs under evidenced bounds? |
| Data representation | Do invariants, access patterns, mutation, locality, and ownership fit the structure? |
| Failure behavior | What happens on partial failure, retry, cancellation, restart, corruption, or overload? |
| Concurrency and consistency | Which ordering, synchronization, atomicity, and visibility guarantees are required? |
| Resource and operational fit | What CPU, memory, I/O, dependencies, deployment, observability, and on-call burden follow? |
| Lifecycle and compatibility | How does initialization, migration, rollback, evolution, and behavioral preservation work? |

Treat asymptotic complexity as one input, not a verdict. A simpler linear implementation over a hard bound of twelve items may fit better than an index. A distributed queue, event log, cache, actor system, or database is not an improvement when its failure modes and operating cost exceed the problem.

Completion criterion: every recommendation identifies both the current strategy's material deficit and why the alternative fits the evidenced constraints better.

### 5. Calibrate the Result

Use exactly these evidence classes:

- **Demonstrated issue:** repository evidence, a reachable cost path, an existing measurement, or a stated hard constraint shows material harm or violated requirements.
- **Credible concern:** the mechanism and plausible impact are concrete, but a material runtime fact or bound is missing.
- **Open question:** the answer could change the strategy verdict and available evidence cannot resolve it.

A demonstrated issue may support a direct recommendation. A credible concern must include the cheapest verification that would resolve it. An open question is not a finding. Downgrade any claim that depends on imagined scale, unverified library behavior, or an unmeasured bottleneck.

`No strategy finding supported by available evidence` is a complete result. Do not manufacture a rewrite to justify the review.

Completion criterion: every claim has one evidence class, and recommendation strength does not exceed its evidence.

## Report Contract

Produce these sections in order.

### Strategy Verdict

- Required behavior and reviewed implementation boundary.
- Problem class.
- Current strategy in one paragraph.
- Outcome: `change recommended`, `verification recommended`, or `no strategy finding supported by available evidence`.
- Explicit statement that the review is read-only, advisory, and not a release decision.

### Constraint Ledger

List each relevant constraint, its evidence, and status: `known`, `assumed`, or `unknown`. Correct any assumption that cannot be tied to supplied or inspected evidence by marking it unknown.

### Prior-Art Inventory

For the current strategy and each plausible established alternative, give the source, contract, fit, and disqualifying mismatch if any. Distinguish verified prior art from a candidate needing verification.

### Findings

Order findings by material impact. For each include:

- evidence class and confidence;
- repository-relative evidence and reachable path;
- current algorithmic, structural, or operational consequence;
- established alternatives considered;
- fit comparison across relevant dimensions;
- recommendation and behavioral-preservation or migration needs;
- cheapest verification that could falsify the recommendation;
- residual tradeoffs.

Exclude style, naming, generic maintainability, speculative optimization, and security findings. Group symptoms that share one strategy cause.

### Open Questions and Verification

List only questions that could change the verdict. State the benchmark, trace, workload bound, failure exercise, or documentation needed to answer each without performing it.

### Coverage

Name inspected artifacts, applicable review dimensions, `not applicable` dimensions, investigation limits, and unresolved prior-art searches.

## Rationalization Checks

| Temptation | Required response |
| --- | --- |
| “The tests pass, so the design is good.” | Preserve tested behavior, then compare the strategy with established alternatives. |
| “This pattern is industry standard.” | Name its contract and prove fit against this workload and operating model. |
| “Big-O is worse, so rewrite it.” | Quantify reachable bounds and frequency; accept simpler bounded work when material harm is unsupported. |
| “We may need internet scale later.” | Mark future scale unknown until a requirement or growth path supplies evidence. |
| “Custom code avoids a dependency.” | Compare ownership, failure modes, maintenance, and existing platform capabilities—not dependency count alone. |
| “The reviewer found it, so the reviewer should fix it.” | Keep the report read-only and hand remediation to a separate implementation workflow. |

## Verification

Before returning the report, verify that:

- the problem class appears before the prior-art comparison;
- custom machinery did not receive a tests-pass exemption;
- every named standard or pattern has a verified contract or is labeled unverified;
- every recommended alternative materially fits known constraints better;
- bounded simplicity is allowed to win;
- missing runtime evidence produces verification work or an open question rather than a factual claim;
- the response contains no artifact mutation or release decision.
