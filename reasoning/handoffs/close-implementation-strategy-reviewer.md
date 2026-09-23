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
    - evidence.controlled-evaluations
  revision: 3
mission: Independently determine whether the produced implementation-strategy-reviewer package satisfies every original obligation and whether its claimed evaluation evidence supports closure.
assignment_boundary:
  may_change: []
  must_not_change:
    - all repository files
    - evaluation records
    - source map and ledger
  may_reconsider_when: []
signals: []
residual_contract_ledger: reasoning/handoffs/author-implementation-strategy-reviewer-ledger.yaml
constraints:
  - Read only the original ledger, produced package, raw evaluation outputs, and actual validator output supplied in context.
  - Do not inherit the author's scoring as authoritative.
  - Distinguish blocking defects from non-blocking improvements.
assumptions: []
open_questions: []
rejected_paths:
  - path: Review only the ranked signals.
    reason: Closure must check every original obligation and nearby compatibility risk.
refresh_triggers:
  - source map revision changes
  - produced package changes
  - new verification evidence contradicts the supplied validator output
instructions_boundary: Perform an independent closure review only. Do not edit files, repeat implementation, or broaden the requested skill.
---

Acceptance evidence supplied by the parent:

- `mise exec -- python scripts/validate.py` exited 0 with 7 repository-validator tests, 35 reasoning-map tests, 8 skill passes, 2 test-suite passes, and final line `Validation passed: 8 skills and 2 test suites.`
- The first closure review found an unresolved `related_skills` entry. It was replaced with the existing `security-reviewer` package, and the full validator again exited 0 with the same totals.
- Existing unrelated modified files remain modified; the new work is confined to `implementation-strategy-reviewer/` and `reasoning/`.
- The implementation author recorded three fresh-context scenario outputs under `implementation-strategy-reviewer/evaluations/raw/`.

Check the original task and every ledger item against the actual files. Inspect raw outputs rather than trusting `evaluations/results.md`. Return a concise verdict, blocking findings, non-blocking findings, ledger status, and recommended signal outcomes.
