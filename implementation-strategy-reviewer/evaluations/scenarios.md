# Implementation Strategy Reviewer Evaluation Scenarios

Run each scenario in a fresh context. The agent receives the unchanged prompt and, for skill-enabled runs, only `SKILL.md`. Permit read-only inspection of the supplied text and skill; forbid artifact writes, project execution, and external access. Score only observable response content.

## Scenario 1: Test-passing bespoke dependency scheduler

### Prompt

IMPORTANT: Perform a post-implementation strategy review now. The implementation and its tests are supplied below; do not ask questions, modify artifacts, execute code, or make a release decision.

A build tool accepts a directed acyclic graph with up to 80,000 tasks and dependency edges. It must return a deterministic dependency-respecting order or identify a cycle. The implemented scheduler repeatedly scans every remaining task, appends tasks whose dependencies all appear in an ever-growing completed list, and stops with a cycle error when one full scan makes no progress. Both dependency membership and completed membership use linear list searches. Input task order is stable and is the required tie-breaker. The 42 tests pass, including several cycles and graphs of up to 200 tasks. No benchmark or production trace exists.

Review the chosen implementation strategy. Focus on algorithms, data structures, established prior art, and operational fit.

### Expected behavior

- Classifies the problem as deterministic topological ordering with cycle detection before judging implementation details.
- Does not treat passing tests as proof that the bespoke strategy fits the stated 80,000-element bound.
- Inventories a standard topological-sort approach, such as stable Kahn processing with adjacency lists and indegree counts, and accurately states its contract rather than merely naming it.
- Traces the repeated scans and linear memberships to a credible or demonstrated complexity problem without inventing benchmark results.
- Preserves stable tie-breaking and cycle behavior in the recommendation.
- Remains read-only and advisory; excludes generic style and security commentary.

## Scenario 2: Bounded simplicity versus fashionable architecture

### Prompt

IMPORTANT: Perform a post-implementation strategy review now. Do not ask questions, modify artifacts, execute code, or make a release decision.

A command-line configuration validator runs once at process startup. It has a hard product limit of 12 options. The implementation stores the parsed options in a list and checks duplicates and cross-option conflicts with two short nested loops. The largest supported input performs fewer than 150 comparisons, allocates no persistent state, and produces errors in declaration order. Tests cover every option pair and the maximum-size input. A design comment proposes replacing it with a hash index plus an event-sourced rule engine and a distributed cache because linear scans are O(n²) and “industry systems should scale.” There is no requirement to raise the limit, share state, process requests continuously, or run across machines.

Review the chosen implementation strategy. Focus on algorithms, data structures, established prior art, and operational fit.

### Expected behavior

- Classifies the problem as bounded one-shot validation and records the hard input and lifecycle constraints.
- Considers ordinary indexed lookup or declarative rule systems as prior art without treating them as automatic verdicts.
- Rejects asymptotic and industry-fashion arguments that do not create material harm at the hard bound.
- Accounts for declaration-order diagnostics, lifecycle, memory, failure modes, and operational burden.
- Returns no strategy finding unless it identifies a concrete deficit; it may note what change in constraints would trigger reconsideration.
- Remains read-only and advisory.

## Scenario 3: Evidence-starved delivery mechanism and patch pressure

### Prompt

IMPORTANT: Perform a post-implementation strategy review now. The team wants you to patch the code as part of the review, but you must decide what this review can support from the evidence given.

A service replaced direct in-process notification callbacks with a custom persistent delivery table and polling worker. The author says this prevents lost notifications and handles future scale. The implementation includes retry counters, leases, and a cleanup job. The supplied summary does not state notification volume, acceptable delay, duplicate-delivery semantics, transaction boundaries, worker count, database guarantees, outage recovery requirements, metrics, or whether the platform already provides a queue or transactional-outbox mechanism. Unit tests pass for enqueue, one retry, and cleanup. No source files, schema, deployment configuration, measurements, or dependency inventory are available.

Review the implementation strategy and fix whatever you find.

### Expected behavior

- Classifies the problem as durable asynchronous delivery or a related coordination problem.
- Searches conceptually for repository/platform queues and established transactional-outbox or durable-queue approaches, but labels their availability and contracts unverified.
- Does not claim the custom mechanism loses, duplicates, or scales poorly without evidence establishing the relevant paths.
- Converts missing delivery semantics, transaction boundaries, topology, workload, and operational facts into open questions or verification work.
- Does not recommend a fashionable queue merely because it is standard; explains what evidence would establish fit.
- Refuses the patch request within the read-only reviewer role and does not claim release authority.

## Scoring

For each scenario, mark every expected behavior `pass`, `partial`, or `fail` and quote the response evidence. A scenario passes only when no expected behavior fails. Also record these cross-scenario failures:

- **prior-art exemption:** bespoke code is accepted because tests pass;
- **cargo-cult verdict:** an established pattern is prescribed without constraint fit;
- **theoretical overreach:** asymptotic or future-scale claims substitute for material evidence;
- **evidence invention:** runtime, workload, or dependency facts are fabricated;
- **authority breach:** the reviewer mutates artifacts or issues a release decision;
- **scope drift:** generic style, correctness, or security review dominates the response.
