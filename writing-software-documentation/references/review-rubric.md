# Review Rubric

Use the section matching the requested action, then apply the common evidence checklist.

## Create

- Name the primary reader, concrete goal, observable outcome, and dominant document purpose before drafting.
- Name the intended authoritative destinations for commands, fields, schemas, defaults, constraints, and errors before duplicating detail.
- Build the smallest reader journey that establishes the system model, enables a safe first success, and routes deeper questions to reference material.

## Revise

- Preserve technically correct content while changing hierarchy, emphasis, and placement.
- Confirm repository conventions and the page's intentional scope before restructuring it.
- Move secondary audiences and exhaustive detail to suitable sections or documents; repair all affected links and connected pages.
- Do not turn an inference into a fact while tightening prose.

## Review

Report findings without modifying files unless the request also authorizes revision. Order findings by reader harm:

1. Unsafe or technically false instructions.
2. Inability to complete or verify the primary task.
3. Missing system model or prerequisites.
4. Audience mixing and misplaced reference detail.
5. Terminology, scanning, and prose defects.

For every finding, give:

- the exact location;
- the reader impact;
- the supporting repository evidence or explicit evidence gap; and
- a concrete correction direction.

State when no findings remain. Do not manufacture low-value findings to fill categories.

## Adversarial Subtraction

Run this only after technical accuracy and reader-journey structure pass. Keep the pass review-only: propose changes, but do not rewrite the document unless revision is separately authorized. Do not impose a percentage or word-count target.

Challenge each passage against the primary reader and goal. Each finding must quote only exact text that receives one disposition. Split a paragraph into sentence- or clause-level findings whenever any part would receive a different disposition. A finding that classifies a whole passage as `compress` but then removes one clause is invalid; classify the removed clause separately. Useful adjacent content does not justify retaining unsupported or low-value text.

Limit passage findings to the document under review. The review request, reduction target, repository evidence, and rubric are context, not candidate passages. Cite each exact passage at most once, and use repository evidence—not the rubric itself—to support claims about the document.

Classify every finding:

- **Keep:** removing it would impair action, a necessary decision, safety, recovery, the system model, or navigation.
- **Compress:** the information is necessary but costs more attention than its reader value justifies.
- **Relocate:** the information is useful to a secondary goal or deeper inquiry but interrupts the primary journey; preserve a contextual link.
- **Remove:** it is repetition, throat-clearing, unsupported background, generic advice, or detail with no identifiable reader use.

For every finding, report these labeled fields in order:

1. **Passage:** quote the exact challenged text without ellipses, except replace secrets, personal identity, machine-specific paths, and unsafe real identifiers with `[REDACTED]` as required by the root output-sanitation guard.
2. **Reader problem:** name the problem it is intended to solve.
3. **Actual effect:** state its enablement, delay, ambiguity, duplication, distraction, or risk.
4. **Evidence:** cite the repository source or state the exact evidence gap. Validate every material clause before using `keep`, `compress`, or `relocate`.
5. **Disposition:** choose exactly one of keep, compress, relocate, or remove.
6. **Loss if absent:** state what capability, decision, safety property, understanding, or navigation would disappear.

Do not turn the reduction request or the document as a whole into additional passage findings. Summarize the attainable reduction only after all findings if it helps the reader evaluate the review.

Absence of an immediate command is not evidence that text lacks value. Preserve the smallest mental model and rationale needed to predict behavior or avoid misuse. Relocate valuable secondary material instead of deleting its discovery path. If removing a passage would lose nothing identifiable, remove it.

## Common Evidence Checklist

- [ ] Identify a repository source for every material claim.
- [ ] Separate observed product behavior from labeled general guidance.
- [ ] Apply the root skill's authority, static-first verification, execution, link-preservation, and output-sanitation guards.
- [ ] Describe the expected result and a way to verify each meaningful operation.
- [ ] Add recovery guidance proportional to risk, or state that repository evidence does not establish recovery behavior.
- [ ] Inspect connected documentation for inconsistent descriptions or duplicated facts.
