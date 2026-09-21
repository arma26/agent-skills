# Adversarial Architecture Methods

## Contents

- Feature expression and surface delta
- Authority topology
- Data lifecycle and trust boundaries
- Adaptive call-chain investigation
- Duplicate-policy drift
- Failure containment
- Dependency and integration boundaries
- Categorical remediation
- Evidence and stopping rules

## Feature Expression and Surface Delta

Write the smallest externally observable contract that satisfies the request. Separately list every mechanism introduced to provide it. Challenge mechanisms that add generic capability, new formats, optional modes, public interfaces, persistence, or future-oriented reuse without a current consumer.

Use counterfactual removal: if deleting a component still permits the feature expression through a narrower path, that component is not required surface.

## Authority Topology

Map who can initiate each operation, which identity reaches the decision point, and which authority performs the effect. Look for ambient credentials, broad service accounts, role strings detached from subjects or resources, cross-tenant context, fail-open defaults, and confused-deputy paths.

Prefer capability removal or a narrower authority boundary over repeated authorization checks. An authenticated caller is not necessarily authorized for the target resource or effect.

## Data Lifecycle and Trust Boundaries

For each relevant datum, identify owner, source of truth, producers, consumers, transformations, lifetime, persistence, and boundary crossings. Prefer local over shared, shared over persisted, persisted over cross-boundary, and derived over stored state unless the feature requires broader scope.

Trace attacker influence, not merely declared types. Include defaults, missing values, stale state, caches, normalization, serialization, logs, errors, backups, generated artifacts, and deletion behavior.

## Adaptive Call-Chain Investigation

Begin at the proposed change or diff. Expand toward callers when provenance, identity, validation, or reachability is unclear. Expand toward callees when authority, side effects, storage, egress, or error behavior is unclear. Follow alternate entry points when they can reach the same policy or sink.

A clean-looking diff is weak evidence when it delegates to broad unchanged authority. A suspicious diff is not itself a finding; trace it until the unsafe path is supported or the relevant invariant is established.

## Duplicate-Policy Drift

Search for more than textual copies. Identify implementations that express the same authorization, validation, parsing, canonicalization, serialization, retry, cleanup, or logging policy through different code. Compare their inputs, defaults, failure modes, and consumers.

Treat divergence as architectural risk when callers can receive different security decisions for equivalent input. Recommend one canonical policy with explicit consumers, then remove the redundant paths and tests that encode obsolete behavior.

## Failure Containment

Trace partial failure, cancellation, retries, replay, restart, concurrent execution, and cleanup. Ask whether a failure crosses tenants, corrupts the source of truth, leaks data, leaves authority active, or converts temporary state into durable state.

Prefer transaction or isolation boundaries that contain whole failure classes. Local catches, retries, and cleanup handlers cannot compensate for an incoherent ownership boundary.

## Dependency and Integration Boundaries

Treat every dependency, plugin, subprocess, remote service, downloaded artifact, and parser as an expansion of the trusted computing base. Identify its authority, data access, update path, outputs, and compromise blast radius.

Ask whether an existing narrower mechanism satisfies the feature. If a dependency remains necessary, minimize its permissions and isolate untrusted outputs before they enter domain state.

## Categorical Remediation

Prefer remedies in this order:

1. Delete unnecessary behavior or code.
2. Reuse an existing narrow mechanism.
3. Narrow accepted inputs, outputs, authority, lifetime, and visibility.
4. Consolidate duplicate policy or parsing.
5. Isolate untrusted work and contain failure.
6. Add validation, filtering, monitoring, or other local controls.

After choosing a categorical remedy, analyze the resulting architecture. Do not preserve a checklist for the removed architecture unless explicitly documenting the risk of rejecting the recommendation.

## Evidence and Stopping Rules

Use three evidence classes:

- **Demonstrated issue:** available artifacts establish the entry point, path, violated invariant, and consequence.
- **Credible concern:** a plausible path exists, but read-only evidence cannot resolve a material condition.
- **Open question:** context needed to evaluate the path is unavailable.

Stop expanding a branch when its relevant provenance, authority, trust transitions, effects, controls, and failure containment are understood, or when further progress requires forbidden access. State the stopping reason and residual uncertainty. Never convert incomplete evidence into proof of safety or a higher severity.
