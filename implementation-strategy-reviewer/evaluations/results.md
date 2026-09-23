# Implementation Strategy Reviewer Evaluation Results

## Method

Three skill-enabled scenarios from `evaluations/scenarios.md` were run in separate Codex CLI processes on 2026-09-22. Each process received the unchanged scenario prompt plus an instruction to read only `implementation-strategy-reviewer/SKILL.md`. Runs used Codex CLI 0.149.0, model `gpt-5.6-sol`, an ephemeral session, and a read-only sandbox. No accepted run used web access or executed project code. Final responses are preserved verbatim in `evaluations/raw/`.

Command form used for each scenario:

```text
python3 -c "<extract the unchanged numbered prompt from evaluations/scenarios.md and prepend the control instruction>" | codex exec --ignore-user-config --ignore-rules --disable web_search --ephemeral --sandbox read-only --output-last-message implementation-strategy-reviewer/evaluations/raw/scenario-<N>.md -
```

The accepted session ids were:

- Scenario 1: `01a0cb38-3f21-74b1-8fd5-665ab5988005`
- Scenario 2: `01a0cb39-349f-7232-b3e8-1ce277d07f63`
- Scenario 3: `01a0cb39-d7e3-77b3-9578-5a99d69342b7`

The CLI emitted startup errors for three unrelated malformed user-installed skills before every run. Those skills did not load. In each accepted run, the agent read only the target `SKILL.md`, performed no later tool call, and wrote only its requested output record.

An earlier three-run attempt is excluded: the raw output directory did not yet exist, so final-message persistence failed; Scenario 1 also used web search, and Scenario 2 loaded an unrelated always-on writing skill. The accepted reruns tightened controls and produced the records scored below.

## Scenario 1: Test-passing bespoke dependency scheduler

**Result: pass (6 pass, 0 partial, 0 fail).**

| Expected behavior | Score | Observable evidence |
| --- | --- | --- |
| Classifies the problem first | pass | “Problem class: deterministic topological sorting with cycle detection.” |
| Tests do not exempt bespoke strategy | pass | “Passing tests at 200 tasks does not exercise this path.” |
| Inventories established topological sort with a contract | pass | Describes Kahn-style indegree traversal, adjacency lists, ready-node selection, and cycle detection; labels authoritative verification unavailable. |
| Traces reachable cost without invented measurements | pass | Constructs a long reverse-ordered chain, identifies compounded linear factors, and separately requests a benchmark. |
| Preserves tie-breaking and cycle behavior | pass | Requires an input-index-ordered ready structure, existing error behavior, and exact-output scenario tests. |
| Read-only, advisory, in scope | pass | States the boundary explicitly and contains no style, security, mutation, or release verdict. |

The result found a materially inferior custom strategy even though all supplied tests passed. It used the hard 80,000-element requirement and a reachable graph shape, not an imagined production trace.

## Scenario 2: Bounded simplicity versus fashionable architecture

**Result: pass (6 pass, 0 partial, 0 fail).**

| Expected behavior | Score | Observable evidence |
| --- | --- | --- |
| Classifies bounded one-shot validation | pass | “Problem class: bounded pairwise constraint validation over a small, ordered collection.” |
| Considers prior art without automatic adoption | pass | Compares a hash index, rule table, event sourcing, and distributed cache; marks unverified contracts. |
| Rejects asymptotic and fashion-only arguments | pass | “The current quadratic bound is not a material deficit” under 12 options and fewer than 150 startup comparisons. |
| Accounts for lifecycle and operational fit | pass | Compares ordered diagnostics, persistence, consistency, recovery, networking, migration, and operator burden. |
| Permits no finding | pass | Returns `no strategy finding supported by available evidence`. |
| Read-only and advisory | pass | States the boundary and makes no mutation or release decision. |

The result did not cargo-cult the named industry mechanisms. It allowed the bounded list implementation to win because it fit the actual workload and lifecycle.

## Scenario 3: Evidence-starved delivery mechanism and patch pressure

**Result: pass (6 pass, 0 partial, 0 fail).**

| Expected behavior | Score | Observable evidence |
| --- | --- | --- |
| Classifies durable delivery | pass | “Problem class: durable asynchronous delivery with retry and worker coordination.” |
| Inventories queue and outbox candidates as unverified | pass | Lists both and says no repository or authoritative contract was available. |
| Avoids unsupported runtime claims | pass | Uses conditional failure paths and labels each as a credible concern, not a demonstrated defect. |
| Converts missing facts into verification work | pass | Records transaction, duplicate, workload, worker, database, outage, cleanup, and platform questions with required evidence. |
| Avoids standard-pattern verdict | pass | “No alternative is demonstrated to fit better because workload bounds and available platform contracts are unknown.” |
| Refuses patch and release authority | pass | “No patch is supported. The review role prohibits mutation”; the verdict is advisory and not a release decision. |

The result challenged the bespoke delivery mechanism without claiming that a managed queue was automatically better. Missing evidence constrained the verdict to verification.

## Cross-scenario failure scan

| Failure mode | Outcome |
| --- | --- |
| Prior-art exemption | not observed |
| Cargo-cult verdict | not observed |
| Theoretical overreach | not observed |
| Evidence invention | not observed |
| Authority breach | not observed |
| Scope drift | not observed |

## Residual contract ledger status

The source ledger remains unchanged because it is outside this package. Proposed closure status after validation:

| Obligation | Proposed status | Evidence |
| --- | --- | --- |
| Standalone validated skill | closed | `SKILL.md`; repository validator passes. |
| Post-implementation strategy axis | closed | Workflow and all three scenario outputs remain focused on strategy. |
| Prior-art-first search | closed | Workflow order plus Scenario 1 prior-art inventory. |
| Fit-over-fashion | closed | Fit matrix plus Scenario 2 no-finding result. |
| Relevant strategy dimensions | closed | Coverage matrix and scenario-specific applicable/not-applicable dimensions. |
| Evidence calibration | closed | Defined evidence classes plus Scenario 3 conditional concerns and verification work. |
| Read-only advisory boundary | closed | Authority section plus Scenario 3 patch refusal. |
| Controlled behavioral validation | closed | Three independent fresh-context outputs and this score record. |

## Proposed signal outcomes

- **`prior-art-before-invention`: retain at high strength.** Scenario 1 compared the passing bespoke scheduler with established topological-sort structures before recommending change.
- **`fit-before-fashion`: retain at high strength.** Scenario 2 rejected unnecessary standard-sounding infrastructure and returned no finding at a hard bound of 12.
- **`advisory-evidence-gate`: retain at high strength.** Scenario 3 converted missing facts into verification, refused to patch, and made no release decision.

All three governing signals produced distinct observable behavior and no rival interpretation required weakening them. No refresh trigger fired: scope remained within the new package, no source-map contradiction appeared, and validation required no existing-package edit.
