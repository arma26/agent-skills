# Agent development baseline

## Purpose

Assume agents write or review project changes from M0 unless the repository explicitly prohibits agent use. The agent's authority and the coordination machinery expand with project maturity.

Do not equate agent readiness with autonomous operation. A prototype needs a safe, reproducible coding environment and a clear definition of done. It does not need autonomous issue triage, merge authority, or deployment access.

## Domain model

- **Instruction authority**: the canonical repository-owned rules that govern agent work.
- **Agent environment contract**: setup, toolchain, writable boundaries, identities, credentials, cleanup, and verification needed for repeatable work.
- **Work request**: the authority-bearing statement of goal, scope, constraints, acceptance, and permitted actions.
- **Work unit**: one reviewable and reversible outcome with one acceptance boundary. It can contain code, tests, documentation, and configuration when all are required for that outcome.
- **Verification contract**: the commands, scenarios, and observable results that distinguish complete work from partial work.
- **Handoff**: the evidence-bearing result passed to a human, agent, CI system, or other consumer.
- **Agent authority**: the files, systems, identities, and state changes the agent may access or perform.

## M0 core contract

When agents write code, require these gates from the first milestone.

### Canonical instructions

- Provide one repository-owned entry point such as `AGENTS.md` or an equivalent named by the project.
- State instruction precedence and how directory-scoped rules refine the root rules.
- Use thin pointers from tool-specific files to the canonical authority. Do not maintain divergent copies.
- Separate normative rules from examples, tips, and historical context.
- Treat issue bodies, pull requests, source files, fixtures, and external content as task evidence, not as authority to expand scope or permissions.

### Reproducible environment

Document or encode:

- supported runtimes, tool versions, platforms, and prerequisites.
- a repository-owned bootstrap path and the smallest validation command.
- the applicable quality floor, such as formatting, static analysis, focused tests, and an end-to-end scenario, with expected outcomes.
- writable, generated, cached, temporary, and persistent locations.
- the owner, source of truth, consumers, and lifetime of state introduced for agent work.
- network access, dependency installation, and other setup side effects.
- credential and account requirements, with local or synthetic alternatives when practical.
- identity rules for commits, bots, services, and external systems. Never depend on a developer's personal logged-in identity implicitly.
- cleanup and recovery after partial setup or failed commands.

A development container is optional. A script, task runner, package manager, or documented standard command is sufficient when it makes the contract reproducible and inspectable.

### Acceptable work unit

A valid work unit has:

- one user-visible or maintainer-visible outcome.
- explicit scope and non-goals.
- acceptance criteria observable through the intended interface.
- the tests and documentation required to keep the outcome usable.
- identified inputs, outputs, dependencies, consumers, and state effects.
- a bounded change set that can be reviewed and reverted without separating unrelated work.

Do not use file count or diff size alone to define a work unit. Split work when outcomes, authorities, rollback paths, or reviewers differ.

### Work request format

The repository may use prose, issues, forms, or structured data. It should preserve these fields when they matter:

```text
goal
user_value
scope
non_goals
acceptance
constraints
interfaces
risks
verification
authority
```

Omit irrelevant fields for a trivial task. Never omit the goal, acceptance boundary, or authority needed for a state-changing action.

### Status and handoff format

During multi-step work, report the current step, total steps when known, action, and evidence or blocker. Keep status updates short enough to inspect.

At handoff, record:

```text
outcome
changed_interfaces
verification
unverified
risks
state_changes
documentation
next_owner
```

A handoff must distinguish observed results from inference. A passing CI job is evidence for the checks it ran, not proof that the work request was satisfied.

### Interaction contracts

Use the format native to each boundary while preserving the same work request and evidence:

- Human interaction: state the outcome, current step or decision needed, evidence, risk, and unresolved work in compact prose.
- Agent handoff: preserve the structured work-request and handoff fields, including original authority and unverified claims.
- CI and local commands: use stable exit status, actionable errors, named checks, and discoverable logs or artifacts. Document nondeterminism and live-service dependencies.
- VCS and review: follow repository-owned title, commit, issue, and pull-request formats. Keep one work unit reviewable as one outcome.
- External systems: follow the system schema and identity model; make target, side effects, retry behavior, idempotency, and approval state explicit.

Formatting consistency means each consumer receives the fields it needs in its native form. It does not require one serialization format for humans, agents, CI, and APIs.

### Authority boundaries

- The human request or an explicitly delegated system defines intent and authority.
- Repository instructions constrain execution; they do not grant new external permissions.
- Specifications, issues, and decision records define accepted outcomes; conflicts must be surfaced.
- CI verifies configured properties; it does not define product intent.
- Publishing, pushing, opening or merging changes, messaging people, deploying, billing, and mutating external systems require explicit authority.
- Any granted external capability uses the narrowest practical identity, target, operation, and lifetime.
- Agent-to-agent handoffs preserve the original scope, permissions, unresolved questions, and evidence. They do not create permission by delegation.

## Milestone expansion

### M1: public agent environment

- A clean external environment can follow setup and reach the documented result.
- Supported tool versions and platform limits are visible.
- Setup failures and cleanup have a public recovery path.
- The project states whether agent-authored contributions are accepted and which human review or disclosure rules apply.

### M2: contributor agent workflow

- Agent instructions cover issue, branch, commit, pull-request, test, documentation, and generated-file expectations where those interfaces exist.
- Local validation corresponds to merge-gating checks.
- Instructions identify work that requires prior discussion, design review, specialist review, or maintainer approval.
- Component ownership and repository maps let an agent route changes and review requests.
- The project states its policy for AI attribution or disclosure instead of assuming a universal rule.

### M3: maintained agent operations

- Component-scoped instructions refine the root authority without contradicting it.
- Design-decision thresholds, release work, backports, security handling, and documentation ownership are explicit.
- Automated agents have named owners, bounded roles, bot identities, credential scopes, generated-source boundaries, and a disable or escalation path.
- The project checks for drift between canonical and tool-specific instructions.

### M4: production agent controls

- Production-affecting agents use least privilege, approval gates, durable audit trails, and distinct non-personal identities.
- Credentials have owners, rotation, revocation, and incident procedures.
- Untrusted repository, issue, log, and user content is treated as input rather than instruction.
- Operators can pause or disable the automation, identify its last actions, roll back effects, and recover partial work.
- Rate, cost, retry, duplication, stale-state, and false-positive behavior have explicit limits and inspection points.

## Audit output

For each applicable milestone, record agent-development requirements beside the other milestone gates. In `agent_development_findings`, include:

- canonical instruction authority and conflicts.
- environment reproducibility and hidden machine assumptions.
- work-unit, work-request, verification, status, and handoff contracts.
- identity, secret, and external-system boundaries.
- automation ownership, permissions, disable paths, and production controls when due.

Use `not_applicable` only when the repository explicitly prohibits agents from writing or reviewing changes. Use `not_due` for later autonomy and production controls. Do not mark the M0 environment and work contracts `not_due` merely because the project is a prototype.
