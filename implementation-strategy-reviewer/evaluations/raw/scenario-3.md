### Strategy Verdict

Required behavior: notifications should survive process failure and eventually reach consumers while preserving whatever latency, duplication, and ordering guarantees the service requires. Only enqueue, one retry, and cleanup are verified.

Reviewed boundary: the replacement of direct in-process callbacks with a persistent delivery table, polling worker, leases, retry counters, and cleanup job.

Problem class: durable asynchronous delivery with retry and worker coordination.

The current strategy is a custom database-backed work queue. It may be appropriate, especially if notification creation and delivery-row insertion share a transaction, but the supplied evidence does not establish that contract or justify custom machinery over existing platform facilities.

Outcome: **verification recommended**. The evidence supports neither patching nor recommending a redesign. This review is read-only and advisory; it is not a release decision.

### Constraint Ledger

| Constraint | Evidence | Status |
|---|---|---|
| Notifications must not be lost | Author’s stated objective | assumed |
| Persistence is required | Persistent table was implemented, but no outage requirement was supplied | assumed |
| Enqueue and originating state change are atomic | Not supplied | unknown |
| Delivery semantics: at-most-once, at-least-once, or effectively-once | Not supplied | unknown |
| Consumer idempotency | Not supplied | unknown |
| Ordering requirements | Not supplied | unknown |
| Notification volume and growth | Not supplied | unknown |
| Acceptable delivery delay | Not supplied | unknown |
| Worker count and deployment topology | Not supplied | unknown |
| Lease duration and renewal behavior | Not supplied | unknown |
| Database isolation, locking, and availability guarantees | Not supplied | unknown |
| Recovery after worker or database outage | Not supplied | unknown |
| Retry backoff and terminal-failure policy | Only one retry is tested | unknown |
| Cleanup retention and race guarantees | Cleanup is unit-tested; contract is absent | unknown |
| Metrics and operator procedures | Not supplied | unknown |
| Existing queue or transactional-outbox capability | Not supplied | unknown |
| Enqueue, one retry, and cleanup work in tested unit cases | Supplied test summary | known |
| “Future scale” requires this architecture | No measurements or growth requirements | unknown |

### Prior-Art Inventory

| Candidate | Source and contract | Fit |
|---|---|---|
| Current custom delivery table and polling worker | Supplied summary only. Intended contract appears to be persistent enqueue, leased polling, retry, and cleanup. Transactional and delivery guarantees are unspecified. | Plausible, but unverified against workload and failure requirements. |
| Direct in-process callbacks | Supplied description of the previous implementation. Delivery depends on process execution and callback success unless protected by an unstated surrounding mechanism. | Simpler and lower latency, but cannot be compared without the actual durability requirement. |
| Platform-managed queue | Candidate only; platform and authoritative documentation were unavailable and external research was prohibited. | Could reduce custom operational machinery, but fit and availability are unverified. |
| Transactional outbox | Candidate architecture only; no repository or external contract was inspected. It ordinarily matters when a domain write and message publication must be atomic, but that requirement is unknown here. | Potentially relevant; no evidence establishes that it fits better than the current table, which may already implement part of this structure. |

No prior-art contract could be verified from the permitted evidence.

### Findings

#### 1. Atomic notification capture is unresolved

- **Evidence class:** Credible concern; high confidence.
- **Evidence:** Supplied summary only; no source path or transaction boundary was available.
- **Consequence:** If the domain change commits separately from delivery-row insertion, failure between them can still lose a notification. Persistence alone does not establish the stated benefit.
- **Alternatives considered:** A delivery row written in the same database transaction; a verified transactional-outbox facility; a platform transaction-to-queue integration.
- **Fit comparison:** Same-transaction insertion directly addresses loss between state change and enqueue when both share a transactional database. External queue publication may introduce a dual-write problem unless the platform supplies an atomic bridge.
- **Recommendation:** Document and test the required transaction boundary before changing the implementation. Preserve the current notification trigger and payload semantics.
- **Cheapest falsification:** Inspect one complete mutation-to-enqueue path and add a failure scenario at the boundary immediately before and after commit.
- **Residual tradeoff:** Transactional capture prevents omission at enqueue time; it does not prevent duplicate delivery.

#### 2. Delivery and lease semantics are not established

- **Evidence class:** Credible concern; high confidence.
- **Evidence:** Retry counters and leases exist, but worker count, database behavior, lease renewal, duplicate semantics, and outage recovery are unknown.
- **Consequence:** A worker crash or slow handler may cause redelivery; lease expiry may permit concurrent handling; an overly long lease may delay recovery. These may be valid at-least-once behavior, but no acceptance contract exists.
- **Alternatives considered:** Custom database leasing, a verified platform queue, or synchronous callbacks where durability is not required.
- **Fit comparison:** Custom leasing is reasonable when database coordination, modest volume, and at-least-once delivery are acceptable. A managed queue may fit better if it already supplies required visibility-timeout and redelivery behavior, but that capability is unverified.
- **Recommendation:** Define delivery semantics before modifying the mechanism. If redelivery is allowed, require idempotent consumption or an explicit deduplication boundary.
- **Cheapest falsification:** Run a documented failure exercise in which a worker acquires a notification, performs the external effect, and dies before acknowledgement; observe whether a duplicate is safe.
- **Residual tradeoff:** Deduplication adds state and cannot generally guarantee exactly-once external effects without cooperation from the destination.

#### 3. Operational cost and claimed scale benefit are unverified

- **Evidence class:** Credible concern; medium confidence.
- **Evidence:** No volume, latency target, polling interval, indexes, measurements, metrics, dependency inventory, or worker topology was supplied.
- **Consequence:** Polling may create unnecessary database load or unacceptable latency, while cleanup and retries add operator-owned failure modes. Conversely, the design may be entirely adequate at bounded volume.
- **Alternatives considered:** Existing platform queue, framework job facility, transactional outbox relay, and the current database-backed worker.
- **Fit comparison:** No alternative is demonstrated to fit better because workload bounds and available platform contracts are unknown.
- **Recommendation:** Do not rewrite for hypothetical scale. Measure queue depth, oldest-item age, claim rate, delivery latency, retry distribution, lease expiry, terminal failures, and polling query cost under a representative workload.
- **Cheapest falsification:** Capture an expected peak-rate workload and query plan, then verify latency and database-load budgets.
- **Residual tradeoff:** Instrumentation adds modest operational work but is necessary to validate the scale claim.

No patch is supported. The review role prohibits mutation, and no source, schema, configuration, or established alternative contract was available from which to derive a safe change.

### Open Questions and Verification

- Must notification creation commit atomically with the originating domain change? Provide the transaction trace and a crash-boundary scenario.
- Are duplicates acceptable, and are consumers idempotent? Provide the externally observable delivery contract and a post-effect/pre-ack crash exercise.
- What are peak enqueue rate, backlog bound, and latency objective? Provide representative measurements and polling-query plans.
- How many workers run, and what database locking/isolation contract coordinates them? Provide deployment configuration and database documentation.
- What happens after prolonged worker or database outage? Exercise backlog recovery and record drain time and load.
- Can cleanup race with leased, retryable, or diagnostically required records? Provide the retention contract and concurrent-cleanup scenario.
- Does the adopted platform already provide a queue, job system, or transactional outbox? Inventory dependencies and verify authoritative contracts before comparing ownership cost.

### Coverage

Inspected artifact: only the supplied implementation summary.

Applicable dimensions: data representation, failure behavior, concurrency and consistency, resource and operational fit, lifecycle, recovery, and compatibility.

Not applicable from available evidence: a concrete algorithmic-complexity comparison.

Limits: no source files, tests, schema, documentation, configuration, history, measurements, dependency inventory, or authoritative prior-art documentation were available. Web research was prohibited. Repository-local, framework, platform-queue, and transactional-outbox searches therefore remain unresolved.