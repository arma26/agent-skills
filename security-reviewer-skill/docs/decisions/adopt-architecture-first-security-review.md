---
status: accepted
date: 2026-09-04
decision-makers: repository owner
consulted: Codex
informed: future maintainers and agents
---

# Adopt architecture-first security review at design and implementation boundaries

## Context and Problem Statement

How should a global security-review skill find material risks without becoming a noisy implementation-bug checklist or adding attack surface of its own?

Security failures often arise from system structure: unnecessary boundaries, excessive authority, duplicated policies, ambiguous ownership, long-lived state, broad interfaces, and uncontained dependencies. Reviewing only individual code defects can leave those causes intact and encourage accumulating controls around a structure that should instead be simplified.

The skill must review every completed design and implementation, distinguish requested external behavior from the mechanism chosen to provide it, and make security-surface reduction its primary objective. It must remain read-only and advisory. The repository has no prior code, conventions, or architecture decisions that constrain this choice.

## Decision Drivers

- Prevent vulnerability classes through structural change where possible.
- Preserve requested external behavior while treating implementation choices as replaceable.
- Minimize code, authority, state, dependencies, and boundary crossings.
- Investigate suspicious paths deeply without expanding into an unrelated repository audit.
- Detect duplicate implementations before their security assumptions drift.
- Identify personal information and developer-identity leakage without reproducing it.
- Produce evidence-backed findings and useful remediation without modifying reviewed systems.
- Trigger consistently after design work and after every implementation.

## Considered Options

- Fixed security checklist.
- Diff-only static review.
- Risk-adaptive, architecture-first read-only review.
- Exhaustive repository audit after every change.
- Active exploit execution and external probing.

## Decision Outcome

Chosen option: **Risk-adaptive, architecture-first read-only review**, because it focuses effort on changed or proposed surface while permitting investigation through connected call chains, data flows, authority, and trust boundaries. It can recommend categorical structural remedies without granting the reviewer mutation or probing authority.

The reviewer runs at two lifecycle boundaries:

1. After design or brainstorming and before implementation planning.
2. After functional verification of every implementation and before completion is claimed.

It is advisory at both boundaries. Other processes own prioritization, remediation, and completion decisions.

### Non-goals

- General maintainability, formatting, or style review without a security consequence.
- Active penetration testing, payload execution, network probing, or automated vulnerability scanning.
- Editing reviewed artifacts or implementing recommended remediation.
- Blocking completion or assigning remediation ownership.
- Exhaustively auditing repository areas unrelated to the proposed or implemented change.
- Claiming that a read-only review proves the absence of vulnerabilities.

### Consequences

- Good, because unnecessary surface is challenged before and after it becomes code.
- Good, because findings distinguish the required feature expression from replaceable implementation structure.
- Good, because duplicate policies and implementations are reviewed as drift risks rather than ordinary style problems.
- Good, because recommendations prefer deletion, consolidation, authority reduction, and isolation before adding controls.
- Good, because strict read-only authority prevents the reviewer from changing reviewed or external systems.
- Bad, because read-only analysis cannot validate every runtime condition or prove the absence of vulnerabilities.
- Bad, because adaptive call-chain investigation has variable cost and requires an explicit evidence-based stopping rule.
- Neutral, because the reviewer reports findings but does not block completion or perform remediation.

## Implementation Plan

- **Affected paths**: create `SKILL.md`, `agents/openai.yaml`, `references/adversarial-methods.md`, `references/security-footguns.md`, `evaluations/scenarios.md`, and `evaluations/results.md`; retain the detailed design in `docs/superpowers/specs/2026-09-04-architecture-first-security-reviewer-design.md`.
- **Dependencies**: add no runtime or development dependencies.
- **Patterns to follow**: keep the runtime skill concise; load detailed methods and footguns through one-level references; use imperative instructions; use repository-relative paths; make output structure explicit; preserve no review state.
- **Patterns to avoid**: do not add scanners, executable payloads, mutation helpers, network probes, generic style checks, duplicated guidance, machine-specific literals, or claims of proven safety.
- **Configuration**: provide discovery metadata in `agents/openai.yaml`; add no environment variables, feature flags, accounts, or external connections.
- **Migration steps**: establish baseline evaluation results before creating runtime skill instructions; implement the skill incrementally; validate it; then perform global installation as a separate explicit deployment action.

### Verification

- [ ] The skill triggers after design or brainstorming and after every verified implementation.
- [ ] Its instructions permit only demonstrably read-only inspection and forbid active payload execution, mutation, and external probing.
- [ ] Reports distinguish feature expression from implementation surface.
- [ ] Reports begin with a surface verdict and prominently display critical and high findings.
- [ ] Every finding includes evidence, attack path, consequence, necessity, structural remediation, and residual risk.
- [ ] Evaluation scenarios demonstrate adaptive call-chain and data-flow inspection rather than diff-only review.
- [ ] Evaluation scenarios demonstrate preference for deletion, consolidation, narrowing, and isolation over accumulated controls.
- [ ] Duplicate security mechanisms, fragile assumptions, personal information, and developer identity leaks are detected and sensitive values are redacted.
- [ ] Reports distinguish demonstrated issues, credible concerns, and open questions and never claim that no findings proves security.
- [ ] The runtime package contains no executable scripts, dependencies, machine-specific paths, or persisted review state.
- [ ] Skill validation succeeds and skill-enabled evaluations improve on recorded baselines.

## Pros and Cons of the Options

### Fixed security checklist

- Good, because it is predictable and inexpensive.
- Good, because common categories are easy to cover consistently.
- Bad, because it encourages mechanical compliance and shallow inspection.
- Bad, because it does not naturally follow suspicious system relationships.

### Diff-only static review

- Good, because it stays tightly bounded to new work.
- Good, because evidence maps directly to changed lines.
- Bad, because changed code can become unsafe through unchanged callers, sinks, configuration, or duplicated policies.
- Bad, because it cannot reconstruct the relevant system boundary.

### Risk-adaptive, architecture-first read-only review

- Good, because it can identify structural causes and categorical remedies.
- Good, because it expands only along relationships needed to understand the change.
- Good, because read-only authority limits review-induced risk.
- Bad, because review depth and duration vary with system complexity.
- Bad, because some runtime uncertainty necessarily remains.

### Exhaustive repository audit after every change

- Good, because it can expose unrelated latent risks.
- Bad, because repeated full audits are expensive and obscure findings attributable to current work.
- Bad, because it violates the requirement for a narrow, change-oriented reviewer.

### Active exploit execution and external probing

- Good, because runtime evidence can confirm exploitability.
- Bad, because it can mutate data, disrupt systems, leak information, or exceed authorization.
- Bad, because it requires environment-specific containment and consent beyond a global review skill.

## More Information

The detailed behavior and evaluation design are specified in `docs/superpowers/specs/2026-09-04-architecture-first-security-reviewer-design.md`.

Revisit this decision if read-only evidence repeatedly cannot resolve important findings, if an isolated authorized testing environment becomes available, or if downstream processes require the reviewer to become a completion gate.
