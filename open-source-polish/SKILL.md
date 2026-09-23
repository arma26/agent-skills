---
name: open-source-polish
description: >-
  Audit or improve a repository through stage-appropriate open-source maturity
  milestones. Use for prototype release, contributor readiness,
  public-project polish, governance, and release or production readiness
  reviews. Also use for documentation drift, convention drift, artifact safety,
  operational clarity, or data recovery readiness.
version: 0.1.0
author: Austin, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [open-source, maturity, audit, release-readiness, polish]
    related_skills: [hermes-agent-skill-authoring]
---

# Open source polish

## Purpose

Treat the repository as a public interface and a project operating system. Assess the maturity the project needs now. Do not grade a prototype against the obligations of an established project.

Separate two dimensions:

- Maturity is the project's current and intended operating stage.
- Risk is what the project handles, regardless of age.

A prototype does not need formal governance, a full security contract, or a production release process. A prototype that handles credentials, untrusted code, public traffic, or important data still needs controls for those risks.

Assume agents write or review changes from M0 unless the repository explicitly prohibits agent use. Keep the core environment and work contracts early. Defer autonomous and production authority until those capabilities exist.

## Operating modes

Choose one mode and state it before the audit.

### `prototype-polish`

Use for release, handoff, publication, outside review, or a full maturity assessment.

Assess every milestone. Mark requirements beyond the target as `not_due`, not as failures. Apply all triggered risk overlays.

### `continuous-polish`

Use during development to detect regression within the current milestone.

Focus on changed interfaces, documentation drift, artifact growth, contributor friction, conventions, inspection points, and triggered risk overlays. Do not reopen settled higher-stage questions without new evidence.

## Resource routing

Only this file loads with the skill. Read each selected reference completely before applying it. Do not preload conditional or maintenance resources.

### Every maturity audit

- After identifying the project shape, read the [project type matrix](references/project-type-matrix.md) to set type-specific expectations.
- Before selecting or rating a milestone, read [maturity milestones](references/maturity-milestones.md) for gates, statuses, and report tables.
- Before assessing agent readiness, read the [agent development baseline](references/agent-development-baseline.md) for environment, work-unit, handoff, and authority requirements.
- After selecting the target milestone, read the [polish checklist](references/polish-checklist.md) to cover each audit area and prioritize findings.
- Before finalizing findings, read the [audit field guide](references/audit-field-guide.md) to test suspicious patterns, edge cases, red flags, and low-value recommendations.

### Conditional audit references

- For a README audit or user-documentation rewrite, read [README by example](references/readme-by-example.md) before judging the first-success path.
- When repository behavior differs from ecosystem norms, read [convention drift](references/convention-drift.md) before classifying or recommending changes.
- When the security or supply-chain overlay activates, read [security and supply-chain evidence](references/security-supply-chain-evidence.md). Use it to assess the relevant controls.
- When important persistent data, synchronization, migration, replication, or recovery exists, read [data continuity](references/data-continuity.md) before assessing the overlay.
- After the user accepts the optional PRR, read [production readiness review](references/production-readiness-review.md) before defining scope or a decision.

### Detailed operator PRR format

Use the detailed operator format only in these cases:

- The user requests a standalone checklist.
- An existing review uses the `Pass`, `Fail`, `Blocked`, and `Accepted risk` terms.

1. Read the [production release rubric](references/production-release-rubric.md) for its evidence rules and release decision.
2. Copy and complete the [PRR template](assets/production-readiness-review.md) as an output artifact.

The compact PRR extension and detailed operator format are alternatives. Do not mix their decision states in one review.

Completing the detailed checklist does not authorize account access or live checks. Use available evidence and mark blocked items until the user separately authorizes external inspection.

### Skill maintenance resources

These files do not provide repository-audit evidence:

- When changing this skill's purpose, workflow, or resource boundaries, read the [design specification](docs/specs/2026-09-02-open-source-polish-design.md) for original intent. Treat this `SKILL.md` as current authority when the dated design differs.
- When revising major design decisions or investigating their rationale, read the [polish reasoning map](docs/reasoning-maps/2026-09-02-open-source-polish.json) and [skill-creation reasoning map](docs/reasoning-maps/2026-09-02-open-source-polish-skill-creation.json).
- When changing the displayed name, discovery summary, or default invocation text, update [agent UI metadata](agents/openai.yaml) and keep it consistent with the frontmatter and workflow.

## Audit workflow

### 1. Establish context

Identify:

- project type and primary audience.
- current status and intended next release or handoff.
- public entry points and smallest successful use.
- contributor entry point and verification path.
- agent instruction entry point, environment contract, and work-unit contract.
- source, generated, cached, temporary, and persistent boundaries.
- human, agent, CI, VCS, and external-system authority boundaries.
- accepted project risks and explicit non-goals.
- evidence limits for this audit, including settings that exist outside the repository.

Use repository evidence before inference. When intent is unclear, infer the narrowest defensible target and label the inference.

### 2. Select the target milestone

Use the author's stated goal when available. Otherwise use public claims and operating behavior.

Do not infer a high target only because advanced files exist. A copied security policy, CI workflow, or governance template is not proof that the process operates.

### 3. Activate risk overlays

Apply an overlay at any milestone when its trigger exists:

- Security: credentials, private data, untrusted input or code, privileged access, network exposure, or distributed executables.
- Data continuity: important persistent data, synchronization, migration, replication, or state that cannot be recreated safely.
- Operations: a public service, production deployment, scheduled jobs, on-call expectations, or external integrations.
- Supply chain: published packages, binaries, images, installers, plugins, or generated release artifacts.

Use proportional requirements. For example, a public prototype that accepts vulnerability reports needs a safe contact route. It does not automatically need response-time promises, supported-version tables, or a security response team.

### 4. Audit milestone gates

Assess every requirement at or below the target milestone. For later milestones, record only clear strengths or dangerous contradictions. Mark the remainder `not_due`.

Use these statuses:

- `fulfilled`: repository evidence satisfies the requirement.
- `partial`: useful evidence exists, but a material gap remains.
- `unmet`: the target milestone requires it and evidence is absent or contradictory.
- `not_applicable`: the project shape makes the requirement irrelevant. State why.
- `not_due`: the requirement belongs to a later milestone and no overlay activates it.
- `evidence_gap`: the audit scope cannot establish the answer.

The current milestone is the highest milestone for which repository evidence satisfies every required gate or proves it not applicable. A serious safety contradiction can cap the result. Examples include a destructive script presented as setup, a published secret, or a restore procedure with an unmarked destructive default.

### 5. Inspect the public interface

Check whether a new reader can:

- understand the project's purpose and status.
- reach the smallest useful result.
- predict the result of documented commands.
- find the correct support or contribution route.
- distinguish required setup from optional or advanced setup.

Prefer a short successful path over exhaustive front-page prose.

### 6. Inspect the project operating system

At the applicable milestone, inspect:

- ownership and review boundaries.
- change intake and design-decision thresholds.
- local and automated verification parity.
- governance and maintainer lifecycle.
- release ownership, support boundaries, and backports.
- community request routing.
- documentation source and publication boundaries.

Distinguish policy from mechanism. A credible policy names its owner, operating method, and result location.

### 7. Inspect agent development

Assess the agent-development requirements for every milestone at or below the target. Agent instructions are an M0 baseline when agents write code. Autonomy and production authority are later-stage concerns.

Check these items:

- Repository-owned instruction authority.
- Reproducible environment.
- Acceptable work unit.
- Work-request and handoff formats.
- Verification contract.
- Identity and secret boundaries.
- Approval gates for external state changes.

Treat tool-specific instruction files as adapters to one canonical authority. Flag conflicting copies, personal-machine assumptions, unbounded work requests, unverifiable completion claims, and permissions inferred from issue or repository content.

### 8. Inspect artifacts and conventions

Map source, tests, docs, scripts, configuration, fixtures, generated output, caches, temporary residue, and archives.

Treat ambiguous artifacts as hypotheses. Do not recommend removal until you identify their ownership and consumers.

For each meaningful convention deviation, state:

- expected ecosystem convention.
- current behavior.
- newcomer cost.
- demonstrated benefit.
- whether to converge, isolate, or document the deviation.

### 9. Inspect clarity, failure, and continuity

Within audit scope, identify primary inputs, outputs, side effects, state owners, external boundaries, inspection points, and failure routes.

Apply recovery requirements only when the data-continuity overlay triggers. Separate source-of-truth data from cache, derived state, and disposable development data.

### 10. Reconcile documentation

Compare documentation with scripts, configuration, templates, and automation definitions. Flag drifted commands, hidden prerequisites, conflicting routes, stale status claims, generated-file ambiguity, and unsupported recovery claims.

### 11. Produce the maturity report

Use this structure:

- `audit_context`
- `target_milestone`
- `risk_overlays`
- `milestone_summary`
- `milestone_findings`
- `agent_development_findings`
- `cross_cutting_red_flags`
- `convention_drift_warnings`
- `artifact_candidates`
- `documentation_drift_findings`
- `recommended_improvement_sequence`
- `evidence_limits`

In `milestone_summary`, include every milestone and its state. In `milestone_findings`, give each requirement a status, evidence, reader or maintainer effect, and smallest next improvement.

For a finding with incomplete or disputed evidence, keep the observed evidence, evidence limit, and maintainer context separate. A maintainer explanation can support an exception. It cannot replace evidence that a control operates.

Order recommendations by the next milestone gate. Put safety contradictions before maturity work. Do not recommend later-stage ceremony while a lower-stage user or contributor path remains broken.

### 12. Offer the production readiness extension

End every completed maturity audit with this optional next step:

> Optional extension: I can run a Production Readiness Review for a defined deployment, release, or operating environment.

Do not run the extension without user acceptance. Do not count it as due or missing in the maturity report. If the project has no production use, keep the offer available for a future production scope.

### 13. Gate changes

Require explicit approval before moving or removing files, normalizing layout, rewriting large documentation areas, changing contributor workflows, or adding state-changing scripts.

Prefer moving ambiguous material to a named archive over immediate deletion. Require safe target checks and an explicit destructive flag for state-changing maintenance tools. Use `--dry-run` by default when the operation can provide a truthful preview.

## Judgment rules

- Treat maturity as cumulative capability, not a count of documents or configured tools.
- Treat risk overlays as independent of maturity.
- Prefer observed mechanisms over policy-shaped files.
- Prefer transferable ecosystem conventions over private maintainer habits.
- Prefer repository-owned commands over required shell aliases.
- Prefer one canonical agent authority with thin tool-specific pointers over duplicated instruction sets.
- Treat a work unit as one reviewable outcome with explicit acceptance and verification, not as an arbitrary quantity of changed files.
- Treat CI as verification evidence, not as the source of intent or permission.
- Prefer precise behavior observations over broad labels or third-party claims.
- Treat a configured mechanism as evidence of intent. Confirm its operation before crediting an operating process.
- Require explicit authority for agent actions that publish, deploy, message, bill, or otherwise change external state.
- Prefer scoped ownership over an unexplained roster when several components exist.
- Prefer explicit release and support authority over automation alone.
- Prefer useful local inspection points over mandatory external telemetry.
- Prefer recovery rehearsal and verification over backup commands alone.
- Preserve intentional deviations when they have an owner, a benefit, and adjacent documentation.
- Recommend the smallest change that unlocks the next milestone.

## Output style

Be direct. Explain why each gap matters at the target milestone. Separate missing maturity from triggered risk. Use repository-relative evidence. Do not manufacture findings to fill every category.
