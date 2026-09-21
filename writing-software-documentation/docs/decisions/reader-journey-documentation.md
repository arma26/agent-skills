---
status: "accepted"
date: 2026-09-06
decision-makers: "Repository maintainers"
---

# Organize Software Documentation Around Reader Journeys

## Context and Problem Statement

Unconstrained large language model (LLM) documentation tends to lead with detail, mix user and contributor audiences, omit usable examples, and optimize prose without repairing the information architecture. Users and operators instead need enough of the system model to complete, verify, and recover from a real task safely. The approved [skill design](../superpowers/specs/2026-09-06-software-project-documentation-skill-design.md) and RED [evaluation scorecard](../../tests/evaluations/scorecard.md) establish the constraints and observed failures.

## Decision

Organize the skill around user and operator journeys. Require the smallest useful system model, pair every meaningful operation with an example and expected result, and keep exhaustive material in linked reference documents. Apply the article's directness, consistency, scannability, and deletion rules only after structure and technical accuracy are sound.

Finish with an adversarial, review-only subtraction pass. Judge passages by reader value rather than word count: keep necessary material, compress attention-heavy material, relocate useful secondary material with a contextual link, and remove material whose absence loses no identifiable capability or understanding.

Keep the runtime surface to repository-native Markdown and YAML. Do not add a documentation framework, runtime dependency, screenshots by default, or a deterministic prose linter.

## Alternatives Considered

- **Rigid templates by document type:** Predictable shapes can prevent omissions, but they become formulaic when a reader goal requires different emphasis. Use lightweight patterns instead.
- **Editorial-only review:** This is cheap to apply and improves weak prose, but it cannot repair a missing system model, unsafe or absent examples, mixed audiences, or the wrong reader journey.

## Consequences

- The skill must inspect repository evidence and expose conflicts or limitations rather than invent behavior.
- Operational guidance must make safety, verification, failure, and recovery proportional to consequences.
- Document-pattern and review guidance must remain separate, directly linked references so the main workflow stays compact.
- Behavioral scenarios and maintenance checks must test the guidance against observed failures.
- Some existing pages may need splitting to preserve one dominant purpose and primary audience.
- Review findings become more accountable because every proposed cut must name its reader impact and counterfactual loss.

## Non-goals

- Introduce a documentation framework or runtime dependency.
- Generate screenshots by default.
- Enforce prose through a deterministic linter.
- Replace complete command, API, schema, configuration, or error reference material.

## Implementation Plan

- **Affected paths:** [SKILL.md](../../SKILL.md), [agents/openai.yaml](../../agents/openai.yaml), [document patterns](../../references/document-patterns.md), [review rubric](../../references/review-rubric.md), [decision index](README.md), and this decision.
- **Behavioral evidence:** use the Task 1 [scorecard](../../tests/evaluations/scorecard.md), the [database backup](../../tests/evaluations/baseline/database-backups.md), [CLI quick-start](../../tests/evaluations/baseline/cli-quick-start.md), [API integration](../../tests/evaluations/baseline/api-integration.md), and [mixed-audience review](../../tests/evaluations/baseline/mixed-audience-review.md) outputs. Keep database-backup repetitions in the same [baseline directory](../../tests/evaluations/baseline/) for variance analysis.
- **Dependencies:** add none; use repository-native Markdown and YAML.
- **Configuration and migration:** make no configuration or migration changes.
- **Patterns to follow:** keep the executable workflow in `SKILL.md`; load each reference directly from it; treat the accepted specification and repository evidence as sources of truth.
- **Patterns to avoid:** do not add scripts, rigid universal templates, inferred product guarantees, or exhaustive reference dumps to operational guides.
- **Maintenance:** update connected documentation whenever behavior, interfaces, lifecycle, configuration, examples, failure modes, or results change.

### Verification

- [x] An independent reviewer can identify the primary reader.
- [x] An independent reviewer can identify the goal the reader can accomplish.
- [x] An independent reviewer can identify the system model the page establishes.
- [x] Every meaningful operation has a concise example and expected result.
- [x] Meaningful extensions are explained and demonstrated.
- [x] Safety, failure, and recovery guidance is proportional to operational risk.
- [x] Exhaustive detail is placed in or linked to reference material.
- [x] Every material technical claim traces to evidence or an explicit limitation.
- [x] The page remains easy to scan without fragmenting the explanation.
- [x] The official skill validator succeeds for the repository root.
- [x] An adversarial subtraction review protects necessary context while identifying removable, compressible, and relocatable material.

## More Information

### 2026-09-06 — Task 4 verification

- **Validator:** the standard skill validator completed successfully with `Skill is valid!`; JSON parsing, `git diff --check`, placeholder, forbidden-path, machine-path, token, and targeted whitespace checks also passed.
- **Behavioral results:** the four baseline scenarios passed 27/32 rubric cells; the four initial skill-enabled scenarios passed 29/32; focused API and CLI reruns passed 16/16. The adversarial security RED repetitions passed 22/30 controls and the GREEN repetitions passed 29/30.
- **Reviews:** the repeated security review reported no Critical, High, or Important findings. The repeated whole-branch specification and quality reviews both reported PASS.
- **Accepted limitation:** the GREEN unestablished-execution-path control passes in 4/5 repetitions. Repetition 5 labels disposable-vault use as general guidance but still recommends execution before command safety is established. The scorecard retains this variance explicitly; it does not weaken the static-first runtime rule.
- **Provenance:** the controller supplied isolated adversarial outputs; the scoring implementer did not observe their dispatch contexts. The with-skill mixed-audience output received whitespace-only normalization after scoring in `9657c1f`; its original blob remains in `ae5e6f3`, with prose and semantics unchanged.
- **Implementation lineage:** `83bf5aa`, `3310f91`, `3d564c5`, `12d811d`, `fcf40c6`, `e67def3`, `8c0d45e`, `bc319f5`, `9c1f74e`, `ae5e6f3`, and `9657c1f` contain the scenarios, skill, behavioral evidence, security hardening, and accepted review fixes.

### 2026-09-06 — Adversarial subtraction review

- **Observed baseline:** the controller reports five isolated reviewers passed 8/35 controls. They generally protected obvious safety steps, but inconsistently preserved the mental-model link, sometimes rewrote a review-only document, and did not systematically justify removals against reader loss. The artifacts do not independently prove dispatch-context isolation.
- **Skill-enabled result:** after three wording-refinement rounds exposed incomplete fields, mixed-passage classifications, duplication, and scope drift, the fourth five-run variant passed 34/35 controls. Every run preserved the operational model and both established links, remained review-only, and stated the reader consequence of removal.
- **Accepted limitation:** one of five final runs assigned `keep` to a passage while also directing removal of an unsupported clause. The atomic-disposition control therefore remains 4/5 rather than being reported as complete compliance.
- **Boundary:** the pass follows accuracy and structure review. It rejects arbitrary length quotas and cannot remove prerequisites, examples, results, verification, recovery, rationale, or navigation when those serve an identifiable reader need.
