# Production readiness review extension

## Purpose

Use this extension after the user accepts the offer at the end of an open-source maturity audit. A Production Readiness Review (PRR) makes a go-live decision for one defined production scope.

A PRR is not a maturity milestone. Repository maturity measures durable project capability. A PRR assesses whether a specific release, deployment, workload, or operating environment is ready now.

## Activation and scope

Run the extension only after explicit user acceptance. Define:

- System or component under review.
- Release, artifact, or commit under review.
- Target environment and operator.
- Expected users, traffic, or workload.
- Important data and external dependencies.
- Planned launch or change window.
- Decision owner and decision date.

If repository evidence cannot establish the scope, mark the decision `unable_to_assess`. Ask only for missing facts that can change the decision.

Acceptance authorizes the review only. It does not authorize deployment, production access, failover, restore, migration, load generation, or another state-changing check.

## Decision states

Use one final decision:

- `go`: all launch-critical requirements have adequate evidence.
- `conditional_go`: no blocker remains, and each condition has an owner, deadline, and verification step.
- `no_go`: one or more launch blockers remain.
- `unable_to_assess`: evidence gaps prevent a defensible decision.

The report recommends a decision. The named decision owner retains launch authority.

Use these requirement statuses:

- `ready`: evidence satisfies the requirement for this scope.
- `condition`: the gap can close before or shortly after launch without accepting an unbounded launch risk.
- `blocker`: launching with the gap would create an unacceptable or unrecoverable risk.
- `not_applicable`: the production shape does not need the requirement. State why.
- `evidence_gap`: the review cannot establish readiness.

A launch-critical `evidence_gap` prevents `go`. Do not convert an evidence gap into a condition merely to reach a decision.

## Evidence strength

Classify the strongest evidence for each requirement:

- `declared`: a person or document states the behavior.
- `implemented`: configuration, code, automation, or a runbook defines the behavior.
- `verified`: a safe check demonstrates the behavior in a representative environment.
- `exercised`: a rehearsal, incident, recovery event, or production observation demonstrates the full response path.

Use evidence strength that matches the consequence. Documentation can establish ownership. Recovery, rollback, migration, and capacity claims usually need verified or exercised evidence.

Do not run deployment, failover, restore, load, migration, vulnerability, incident, or live endpoint tests unless the user separately authorizes and scopes them. Static evidence does not become exercised evidence because a command exists.

Use repository-relative evidence. Cite the location of secrets, personal data, or machine-specific identity without reproducing the value.

## Review areas

Assess only areas relevant to the defined production shape.

### Scope and ownership

- A named owner can make the go-live decision.
- Operators know component, dependency, and escalation ownership.
- The review identifies accepted risks and launch-blocking risks.

### Deployment and change safety

- The release artifact and configuration are identifiable.
- Deployment steps have verification and stopping criteria.
- Rollback or roll-forward criteria match the actual change.
- Database or state migrations account for compatibility and partial failure.
- The change process identifies who can deploy and reverse the change.

### Health and inspection

- Operators can distinguish process health from dependency and user-path health.
- Logs, metrics, traces, events, or local inspection points answer expected failure questions.
- Alerts have an owner and an actionable response.
- Success criteria describe what to observe after launch.

### Reliability and capacity

- The review states expected workload and known limits.
- Resource, quota, rate, timeout, queue, and concurrency limits are visible where relevant.
- The system bounds external dependency failures.
- Capacity evidence matches the expected workload and failure cost.

Do not require formal service objectives for every project. Require them when the operator or user promise depends on measured availability or latency.

### Configuration, access, and secrets

- Production configuration has an owner and source of truth.
- Secrets avoid tracked files, command arguments, logs, and unsafe examples.
- Production access follows the minimum authority needed for operation and recovery.
- Credential rotation and emergency access have proportional procedures.

This area does not replace a security review. Record a separate security-review requirement when the production scope needs threat or vulnerability analysis.

### Data, migration, and recovery

- Operators can distinguish authoritative, cached, derived, and disposable state.
- Backup scope and retention match the production data.
- Restore uses an isolated target before cutover when practical.
- Integrity checks define a successful restore.
- Migration, replay, repair, quarantine, and rollback paths cover credible failure modes.

### Incident and support readiness

- A person or team owns production incidents for the declared support period.
- Runbooks cover high-consequence and likely failure scenarios.
- Escalation routes provide the access needed to diagnose and recover.
- User communication and security reporting routes match the project promise.

### Release and supply chain

- Operators can relate the deployed artifact to source and version.
- Artifact integrity, provenance, and dependency controls match distribution risk.
- Release notes identify operational changes, migrations, and compatibility limits.
- The project can identify and replace a vulnerable or defective release.

## Project-shape adjustments

- Library: focus on compatibility, release integrity, deprecation, dependency risk, and consumer rollback.
- CLI: focus on artifact integrity, configuration scope, safe defaults, failure output, compatibility, and data effects.
- Batch or scheduled job: focus on idempotency, duplicate work, replay, checkpoints, schedules, and partial completion.
- Service or API: focus on dependencies, health, capacity, traffic, incident response, rollback, and data continuity.
- Web application: include client deployment, asset compatibility, backend coupling, user-path health, and rollback.
- Managed service dependency: record the provider boundary and the responsibilities that remain with the project.

Do not add service-only requirements to a library or disposable local tool.

## Suspicious evidence

Investigate these patterns before accepting readiness:

- A dashboard exists, but no owner or response uses it.
- A health endpoint reports process status but ignores critical dependencies.
- A rollback procedure cannot reverse the accompanying schema or state change.
- A backup exists, but no restore or integrity evidence exists.
- Autoscaling exists, but quotas, downstream limits, or cost bounds are unknown.
- An on-call route exists, but responders lack access or recovery instructions.
- A deployment checklist has checkboxes but no observable acceptance criteria.
- A runbook assumes external context, personal credentials, or one maintainer's machine.
- A staging result stands in for production without explaining material differences.
- A successful prior release stands in for evidence about a changed dependency or migration.

## Output contract

Append this section after the maturity report:

- `production_readiness_extension`
  - `review_scope`
  - `decision`
  - `launch_blockers`
  - `launch_conditions`
  - `readiness_matrix`
  - `failure_scenarios`
  - `rehearsal_and_evidence_gaps`
  - `go_live_and_rollback_criteria`
  - `follow_up_owners`
  - `evidence_limits`

Use this matrix:

| Area | Requirement | Status | Evidence strength | Evidence | Production effect | Required action | Owner |
|---|---|---|---|---|---|---|---|

List blockers before conditions. Keep later improvements outside the launch decision unless they reduce a stated production risk.

## Completion criteria

The extension is complete when:

- The review scope identifies one production decision.
- Every relevant review area has a status and evidence strength.
- Each blocker and condition has a concrete closure test.
- The final decision follows the status rules.
- Owners and dates come from evidence or remain explicitly unassigned.
- Evidence limits separate repository facts from assumptions.
