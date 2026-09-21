# Architecture-First Security Reviewer Design

## Purpose

Create a globally discoverable skill that reviews every completed software design and every completed implementation from an adversarial, systems-oriented security perspective. The skill preserves the requested external behavior while treating its implementation structure as replaceable and its added security surface as suspect.

The reviewer is read-only and advisory. It reports findings and remediation options; other processes decide whether and how to act on them.

## Governing Doctrine

Security is primarily architectural. Prefer changing system structure so classes of failure cannot occur over finding and patching each local defect.

For review purposes, separate:

- **Feature expression**: externally observable behavior required by the user or specification.
- **Implementation surface**: inputs, outputs, interfaces, parsers, formats, permissions, dependencies, storage, filesystem access, network access, configuration, logging, and executable paths introduced or expanded to provide that behavior.

Preserve the feature expression. Challenge every element of implementation surface. Remediation priority is:

1. Delete unnecessary code or capability.
2. Reuse an existing narrower mechanism.
3. Reduce authority, visibility, accepted inputs, outputs, or lifetime.
4. Consolidate parallel implementations behind one canonical policy.
5. Isolate the remaining boundary or untrusted component.
6. Add local controls only when structural elimination is unavailable.

## Invocation Points

### Design review

Invoke after design or brainstorming and before implementation planning. Review the proposed feature contract, authority model, data ownership, trust boundaries, dependencies, externally reachable capabilities, failure containment, and proposed state lifetimes.

Design findings cite proposed structures and unresolved assumptions. Their purpose is to prevent unnecessary surface from hardening into code.

### Implementation review

Invoke after functional verification of every implementation and before completion is claimed. Compare the implementation with the requested feature expression and the reviewed design. Identify added surface, architectural drift, duplicate mechanisms, fragile assumptions, sensitive-data exposure, and developer-identity leakage.

Implementation findings cite repository-relative files and reachable call or data paths.

Both reviews are advisory. They neither modify artifacts nor determine whether downstream work may proceed.

## Authority and Safety Boundary

The reviewer may use read-only inspection of repository files, diffs, history, configuration, dependency metadata, tests, and documentation. It must analyze each command before use and must not run a command whose read-only behavior is uncertain.

The reviewer must not:

- Edit, create, move, or delete reviewed artifacts.
- Execute exploit payloads or untrusted project code.
- Run tests or analyzers that may create caches, snapshots, temporary files, or other state.
- Probe network services or external systems.
- Change local, repository, account, or production state.
- Reproduce secrets, personal data, or developer identity values in its report.

Adversarial testing means constructing abuse cases and tracing their consequences through available evidence. A read-only review may establish a demonstrated unsafe path or a credible concern; it cannot prove the absence of vulnerabilities.

## Investigation Workflow

### 1. Establish contract and scope

Read the request or specification, repository instructions, applicable architecture decisions, relevant documentation, and the implementation diff when one exists. State the required external behavior without treating implementation choices as requirements.

### 2. Perform a surface sniff-test

Inspect additions and expansions involving:

- User or externally controlled inputs.
- Outputs and data egress.
- Public interfaces and accepted formats.
- Authentication, authorization, and ambient authority.
- Filesystem and network access.
- Storage, caches, sessions, and other state.
- Parsers, serialization, normalization, and canonicalization.
- Dependencies and external integrations.
- Logging, errors, diagnostics, and generated artifacts.

An unexplained addition is suspicious until it maps to required feature behavior.

### 3. Reconstruct the relevant system

Build a transient reasoning model; do not persist review state. For each relevant surface, identify:

- Owner and source of truth.
- Producers and intended consumers.
- Trust level and authority.
- Lifetime and deletion boundary.
- Entry points and reachable effects.
- Required boundary crossings.
- Failure containment and recovery behavior.

### 4. Investigate adaptively

Follow call chains toward both entry points and effects until the affected trust boundaries, authority, and consequences are understood. Trace data from sources through transformations to sinks. Inspect directly connected unchanged code when the change relies on its assumptions.

Search for parallel implementations of the same feature or security policy. Compare authorization, validation, normalization, parsing, serialization, error handling, and data-handling assumptions. Treat drift between copies as a security risk and recommend one canonical mechanism followed by removal of redundant paths.

### 5. Apply relevant adversarial methods

Select methods based on the observed surface rather than mechanically applying every check. Consider injection, traversal, symlinks and races, confused-deputy behavior, authorization bypass, request forgery, redirects, unsafe deserialization, resource exhaustion, replay and retry effects, concurrency, partial failure, fail-open behavior, dependency compromise, cleanup, secret leakage, personal data, and developer identity.

Common footguns are findings only when they create ambiguity about a security invariant, increase exploitability, conceal failure, leak sensitive information, or make future security drift likely. General style criticism is out of scope.

### 6. Challenge structural necessity

For each expanded surface, ask whether the feature expression requires it. Prefer categorical remedies: remove the boundary, eliminate ambient authority, narrow the interface, localize or derive state, centralize policy, isolate untrusted processing, or remove a dependency.

Group related implementation defects beneath their common architectural cause. Do not inflate the report with repeated symptoms.

### 7. Stop on evidence

Stop following a branch when its relevant trust boundaries, reachable effects, authority, and controls are understood and no material unsupported assumption remains. Classify the result as:

- **Demonstrated issue**: repository or design evidence establishes the unsafe path.
- **Credible concern**: the path is plausible, but read-only evidence cannot resolve a material condition.
- **Open question**: necessary context is absent; do not present this as a vulnerability.

Use “no finding supported by available evidence,” never “proven safe.”

## Finding Contract

Lead with a security-surface verdict:

- Whether exposed surface increases.
- Which increases are necessary for the feature expression.
- Which additions should be removed, consolidated, narrowed, or isolated.
- Whether any critical or high findings exist.

Display critical and high findings first. Report all substantiated findings by severity, but do not block completion or implement fixes.

Use impact and reachability rather than code complexity to assign severity:

- **Critical**: a reachable path can plausibly produce system-wide compromise, arbitrary execution, unrestricted authority, or catastrophic sensitive-data loss with minimal preconditions.
- **High**: a reachable path can plausibly produce material unauthorized access, control, or sensitive-data exposure.
- **Medium**: exploitation requires meaningful preconditions or the flaw materially weakens containment or a security invariant.
- **Low**: limited current impact, but concrete fragility or drift can weaken a security assumption over time.

Each finding contains:

- Severity and confidence.
- Concise title.
- Evidence with repository-relative file and line references when applicable.
- Attacker-controlled source or entry point.
- Call or data path to the affected sink or boundary.
- Consequence and required preconditions.
- Feature-expression versus implementation-surface classification.
- Necessity verdict: required, reducible, duplicative, or unnecessary.
- Minimal remediation ordered by structural elimination before local controls.
- Residual risk after remediation.

Redact suspected credentials, personal information, account identifiers, machine-specific paths, names, email addresses, hostnames, and production values. Cite locations without repeating values.

If no findings exist, state which surfaces and call chains were inspected, why the added surface appears necessary, and which uncertainties remain.

## Skill Package

The runtime package contains:

- `SKILL.md`: doctrine, triggers, workflow, stopping rules, and report contract.
- `agents/openai.yaml`: discovery metadata and default invocation prompt.
- `references/adversarial-methods.md`: system-level review methods selected according to observed boundaries.
- `references/security-footguns.md`: boundary-specific hazards and fragility amplifiers.

Do not add executable scripts or assets initially. Generic security automation would add maintenance and execution surface without enough evidence that it improves this reasoning-oriented workflow.

Repository development artifacts include this specification, the architecture decision record, `evaluations/scenarios.md`, and `evaluations/results.md`. They are not runtime instructions.

## Evaluation Strategy

Apply test-driven skill development. Run realistic scenarios without the skill, preserve the observed failure modes and rationalizations, then write the minimum instructions needed to correct them. Re-run the same scenarios with the skill and tighten only demonstrated gaps.

At minimum, evaluations cover:

1. An external download feature with unnecessary network authority, redirects, unbounded content, and unsafe output handling.
2. Parallel authorization or validation paths whose assumptions can drift.
3. Generated tests or fixtures containing personal information, developer identity, machine-specific paths, or copied production identifiers.
4. A large defensive implementation whose boundary can instead be removed.
5. Pressure to enumerate local bugs while overlooking a single structural cause.

Success requires the reviewer to:

- Trigger at both approved lifecycle points.
- Remain read-only and avoid active probes.
- Reconstruct relevant boundaries and follow suspicious call and data chains.
- Prefer categorical surface reduction over accumulating controls.
- Identify security-relevant duplication and fragility.
- Redact sensitive and developer-specific values.
- Separate demonstrated issues, credible concerns, and open questions.
- Prominently surface critical and high findings with actionable remediation.

## Non-Goals

- General maintainability or style review.
- Automated vulnerability scanning.
- Active penetration testing.
- Remediation implementation.
- Approval or completion gating.
- Exhaustive auditing of unrelated repository areas.
- Claims that a read-only review proves security.
