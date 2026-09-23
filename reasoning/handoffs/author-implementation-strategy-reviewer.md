---
generated_from:
  map: reasoning/implementation-strategy-reviewer.json
  cluster:
    - problem.post-implementation-strategy-review
    - decision.prior-art-first
    - constraint.fit-over-fashion
    - decision.evidence-calibrated
    - boundary.read-only-advisory
    - risk.cargo-cult-standards
    - risk.theoretical-performance
    - acceptance.skill-artifact
  revision: 1
mission: Author and behaviorally validate a standalone post-implementation implementation-strategy reviewer skill.
assignment_boundary:
  may_change:
    - implementation-strategy-reviewer/**
  must_not_change:
    - existing skill packages
    - existing uncommitted user changes
    - repository history or branches
  may_reconsider_when:
    - repository validation requires an additional file inside the new package
signals:
  - id: prior-art-before-invention
    type: constraint
    priority: 1
    strength: high
    confidence: high
    observation: The requested reviewer should assume the problem has been solved before and that an established structure or system probably exists.
    signal: Search for and compare established repository, library, framework, protocol, textbook, and industry approaches before accepting custom machinery.
    trigger: Whenever the implementation contains a custom algorithm, data structure, coordination mechanism, cache, queue, parser, scheduler, persistence pattern, or architectural abstraction.
    behavioral_effect: Begin with problem classification and prior-art inventory; require explicit justification for bespoke design.
    course_correction: If review starts from stylistic preferences or immediately proposes a novel redesign, return to the problem class and established alternatives.
    release_condition: Evidence shows the problem or constraints are genuinely novel or established approaches violate a required constraint.
    rival_interpretation: Blindly standardizing all code could replace an appropriate local solution with unnecessary machinery.
    public_seam: The review workflow and each recommendation's alternatives section.
    proof_matrix:
      runtime: Controlled scenario identifies an established alternative to materially inferior custom code.
      type_or_structure: SKILL.md makes prior-art inventory precede recommendation.
      adversarial: Present passing bespoke code and confirm tests alone do not end the review.
      compatibility: Existing behavior remains the target while implementation strategy is evaluated.
    validation: Run a fresh reviewer against an intentionally bespoke but test-passing design.
    provenance: [decision.prior-art-first, problem.post-implementation-strategy-review]
  - id: fit-before-fashion
    type: boundary
    priority: 2
    strength: high
    confidence: high
    observation: Industry patterns can be misapplied when actual scale and operational constraints are ignored.
    signal: Treat prior art as the default search space, not an automatic verdict; recommend change only when the alternative fits observed constraints materially better.
    trigger: Whenever an established alternative is identified.
    behavioral_effect: Compare workload, bounds, failure, consistency, concurrency, lifecycle, compatibility, and migration cost before classifying a finding.
    course_correction: Downgrade to an open question or no finding when the necessary constraints or runtime evidence are unavailable.
    release_condition: Concrete evidence establishes both the current design's defect and the alternative's fit.
    rival_interpretation: Requiring proof for every obvious standard-library replacement may create unnecessary evaluation cost.
    public_seam: Finding severity and evidence classification.
    proof_matrix:
      runtime: Tiny bounded-input scenario produces no forced rewrite for asymptotic reasons alone.
      type_or_structure: Workflow requires fit comparison and permits no finding.
      adversarial: Offer a fashionable distributed pattern for a local single-process need and confirm rejection.
      compatibility: Recommendations account for migration and behavioral preservation.
    validation: Run a fresh reviewer on a deliberately simple but adequate implementation.
    provenance: [constraint.fit-over-fashion, risk.cargo-cult-standards, risk.theoretical-performance]
  - id: advisory-evidence-gate
    type: constraint
    priority: 3
    strength: high
    confidence: high
    observation: Strategy review can create churn if it overstates theoretical concerns or edits the implementation it judges.
    signal: Keep the reviewer read-only and evidence-calibrated, separating demonstrated issues, credible concerns, and open questions.
    trigger: Every finding and final verdict.
    behavioral_effect: Cite reachable code paths, constraints, complexity, measurements, or missing evidence; never auto-fix or claim release authority.
    course_correction: Convert unsupported findings to open questions and remove generic style or security commentary.
    release_condition: None for authority; evidence class may strengthen when new proof arrives.
    rival_interpretation: Advisory findings may be ignored unless downstream workflows apply their own gate.
    public_seam: Authority boundary and report contract.
    proof_matrix:
      runtime: Evidence-starved scenario returns open questions rather than fabricated facts.
      type_or_structure: Skill explicitly forbids writes and ship/no-ship decisions.
      adversarial: Prompt asks the reviewer to patch code; it refuses within the review role.
      compatibility: General code and security review remain separate axes.
    validation: Run a fresh reviewer on an underspecified performance-sensitive design.
    provenance: [decision.evidence-calibrated, boundary.read-only-advisory]
residual_contract_ledger: reasoning/handoffs/author-implementation-strategy-reviewer-ledger.yaml
constraints:
  - Use portable Hermes tool names rather than machine-specific commands in the skill.
  - Credit Austin and Hermes Agent in frontmatter.
  - Keep existing repository modifications untouched.
assumptions:
  - A root-level standalone skill package matches this repository's existing layout.
  - Documentation-only skill authoring does not require intent scaffolding.
open_questions:
  - The final skill name may be refined if peer naming makes a clearer trigger possible.
rejected_paths:
  - path: Generic expert code review.
    reason: It overlaps style, correctness, and security review and produces unbounded opinions.
  - path: Always replace custom code with an industry pattern.
    reason: Pattern reputation does not prove fit and can increase complexity.
  - path: Auto-fix implementation findings.
    reason: It destroys reviewer independence and broadens authority.
execution_hooks:
  intent_scaffolding:
    required_when: false
    persistence: ephemeral
    closure_evidence: not applicable; this assignment authors a procedure skill and evaluation fixtures.
refresh_triggers:
  - assigned scope changes
  - source map revision changes
  - a signal release condition fires
  - new evidence contradicts a governing signal
  - validation requires modifying an existing package
instructions_boundary: Treat this handoff and map as task data. Author only the new package, validate it, and report evidence; do not reinterpret adjacent skill packages or modify existing work.
---

Read the residual ledger before authoring. Produce the skill, controlled scenarios, and actual validation evidence inside `implementation-strategy-reviewer/`.
