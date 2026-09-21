# Production release rubric

Use this rubric with [the PRR template](../assets/production-readiness-review.md). The template is a one-hop operational index and collects facts. This rubric controls the release decision.

## Operator handoff contract

Write for an operations specialist who has no project context or operational
history. Describe the service as a black box through its purpose, interfaces,
dependencies, state, controls, signals, limits, failure behavior, and recovery.
Operation must not require source-code reading.

Keep every concern within one degree of its answer. Put the answer in the PRR or
link directly to the authoritative runbook, dashboard, configuration reference,
exercise result, or owner record. A general project page, source-code location,
or document that requires another search does not satisfy this rule.

For every applicable item, record:

- `Result`: `Pass`, `Fail`, `Blocked`, `Accepted risk`, or `N/A`.
- `Answer`: the concise operational fact.
- `Source`: the direct operational source when the answer needs supporting detail.
- `Owner`: the role or team accountable for the fact and its maintenance.
- `Last verified`: the date of the latest verification.

Do not copy credentials into the PRR. Link to the protected control system and
state how an authorized operator requests, verifies, and relinquishes access.
Mark the item `Blocked` when no direct operational source exists.

Place the live operational interfaces near the start of the PRR. Treat this
section as the observation front door for a zero-context operator. Include each
applicable service dashboard, runtime platform, saved log search, database status
view, trace or job view, deployment view, alert interface, and dependency status
page. Link to the service and environment scope, not a vendor homepage. State
what each interface can prove and link to its access procedure. Prefer a
least-privilege, read-only role. Mark an absent interface `N/A` with a reason.
Set the PRR's access boundary for the most sensitive linked interface. Do not
include links with embedded credentials or signed access parameters.

## Assessment method

Assess every applicable checklist item. Record one result beside each item:

- `Pass`: current evidence proves the requirement.
- `Fail`: current evidence disproves the requirement.
- `Blocked`: the required evidence or decision is unavailable.
- `N/A`: the item does not apply. State the reason.

Link each `Pass` to a direct operational source or include the complete answer.
Name an owner and due date for each `Fail` or `Blocked` item.

A checked box means that a reviewer assessed the item. It does not mean that the result passed. Keep the written result beside the box.

## Required coverage

Complete each PRR section. Do not omit a section because the project is small. Use `N/A` with a reason when a section does not apply.

Reviewers can use different local titles. Preserve these responsibilities:

- production operation and reliability
- build, deployment, and rollback
- security and compliance

One person can hold more than one responsibility. Record this choice when independent review is unavailable.

## Evidence rules

Use current, reproducible evidence. A plan is evidence of intent, not evidence that the control works.

For the end-to-end path, start with the user action and observe the result.
Record dependencies, failure handling, and rollback without requiring an
operator to learn the internal call path.

For backup, restore, failover, rollback, load, and incident response claims, cite the latest exercise or test. State its date and result.

For external systems, identify the owner, protocol, authentication, timeout, retry policy, failure mode, and degradation behavior.

Exercise every live operational link from an operator account. Ensure that the
link opens the stated service and environment scope. Ensure that the linked view
answers its stated question without another search. Record the verification date.

Exercise the operator quick index after completing the detailed sections. Start
from each concern and ensure that the answer or linked source enables the next
inspection, control, recovery, or escalation action without another search.

## Release decisions

Choose exactly one decision:

- `Ready`: all applicable required items pass. No release blocker remains.
- `Ready with accepted risks`: no blocker remains. An authorized owner accepted each remaining failure, with an expiry date and mitigation.
- `Not ready`: at least one blocker remains, evidence is stale, or a required review is incomplete.

A deadline alone does not convert a blocker into an accepted risk. Record who has authority to accept the risk.

## Completion gate

The PRR is complete only when:

- every item has a result and evidence or an `N/A` reason
- every applicable item has an answer, owner, and last-verified date
- every source link resolves directly to an operational answer or action
- the live operational interfaces provide scoped observation links, access procedures, owners, and verification dates
- an operator can open each applicable interface through a documented least-privilege access procedure
- the operator quick index covers the service contract, control plane, first inspection point, state, background work, failure recovery, and escalation
- required reviewers recorded a decision
- the user-to-result path passed end-to-end verification
- rollback and recovery evidence match the release artifact
- each follow-up has an owner and due date
- the final decision follows the rules above
