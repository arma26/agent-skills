---
name: open-source-polish
description: >-
  Improve functional codebases for public contribution and production release.
  Use for prototype polish, production readiness reviews, open-source preparation,
  contributor friction, documentation drift, ecosystem conventions, stray
  artifacts, runtime inspection, and data recovery.
---

# Open Source Polish

## Overview

Treat the repository as a public interface. Optimize for reader attention, contributor trust, transferable ecosystem understanding, and predictable inspection when behavior fails.

Assume the user may have little or no experience preparing software for outside contributors. Guide the work from prototype reality to mature project shape without silently destroying ambiguous artifacts.

## Operating Modes

Choose one mode early and say which mode you are using.

### `prototype-polish`

Use near release, handoff, publication, or outside review.

Run the full pass:

- first-impression audit
- structure and artifact audit
- convention drift audit
- contributor path audit
- runtime clarity audit
- failure handling audit
- data continuity audit when important data exists
- documentation reconciliation

### `continuous-polish`

Use during development to catch drift before it accumulates.

Run a lighter pass focused on:

- README and example drift
- growing repo clutter
- convention drift
- contributor setup friction
- logging, exception, and inspection-point regressions

### `production-readiness`

Use before a production release or a formal production readiness review (PRR).

Run `prototype-polish`, then read:

- [references/production-release-rubric.md](references/production-release-rubric.md)
- [assets/production-readiness-review.md](assets/production-readiness-review.md)

Copy the template into the target repository. Complete it from repository and operational evidence. End with an explicit release decision.

## First Questions

Answer these before recommending cleanup:

- what kind of project is this
- what would a stranger try in the first two minutes
- what is the smallest successful example
- what commands should be copy-pasteable
- what local behaviors differ from ecosystem norms
- what files or scripts have unclear ownership or integration
- what would block a first external contribution
- does the project handle important persistent data

## Workflow

### 1. Orient

Identify:

- project type
- language and tooling layer
- public entrypoints
- test and verification path
- important state or data boundaries
- likely first-impression path

Then read:

- [references/project-type-matrix.md](references/project-type-matrix.md)
- [references/polish-checklist.md](references/polish-checklist.md)

If the README or docs are central to the task, also read:

- [references/readme-by-example.md](references/readme-by-example.md)

If the repo appears unusual for its ecosystem, also read:

- [references/convention-drift.md](references/convention-drift.md)

If the project handles important data, also read:

- [references/data-continuity.md](references/data-continuity.md)

### 2. Audit First Impressions

Check whether the repo earns trust quickly:

- README explains the project in one short pass
- setup path is real
- examples are copy-pasteable
- root-level layout feels intentional
- current status is honest

Prioritize attention economy over exhaustive prose. Show the smallest useful path first.

### 3. Audit Structure And Artifacts

Map:

- source
- tests
- docs
- scripts
- configs
- fixtures
- generated output
- temporary residue
- files with unclear purpose

Treat dangling artifacts as hypotheses. Do not assume they are safe to remove.

### 4. Audit Convention Drift

Compare the repo against ecosystem expectations.

Warn explicitly when the project forces a newcomer to learn local conventions before they can apply prior knowledge from similar projects.

For each meaningful deviation, state:

- expected standard
- current behavior
- newcomer cost
- whether to remove or justify the deviation

### 5. Audit Contribution Friction

Check whether a stranger can:

- set up the project
- run the project
- run tests
- identify a small safe change
- understand where to inspect failures

Treat confusion about workflow, file ownership, hidden state, or setup as contributor friction.

### 6. Audit Runtime And Failure Clarity

Inspect:

- main inputs and outputs
- state ownership and boundaries
- side effects
- boundary logging
- exception quality
- predictable inspection points

Warn when telemetry or external dashboards are required just to understand normal local behavior.

### 7. Audit Data Continuity When Needed

If important data exists, inspect:

- source-of-truth vs cache vs derived state
- lifecycle of important data
- backup and restore paths
- bad-data detection
- repair, replay, or quarantine paths
- maintenance scripts and their safety posture

Require recovery-oriented documentation when data continuity matters.

### 8. Reconcile Documentation

Compare docs against code, scripts, and configuration.

Flag:

- drifted commands
- hidden prerequisites
- stale claims
- examples that are not the easiest path
- missing recovery guidance for data-bearing systems

### 9. Propose Cleanup

Produce a structured proposal with these sections:

- `first_impression_findings`
- `convention_drift_warnings`
- `artifact_candidates`
- `documentation_drift_findings`
- `contributor_friction_findings`
- `runtime_clarity_findings`
- `failure_handling_findings`
- `recommended_cleanup_sequence`

Add `data_continuity_findings` when the project handles important data.

For `production-readiness`, also provide:

- the completed PRR location
- the release decision
- unresolved blockers and accepted risks
- the owner and due date for each follow-up

### 10. Gate State-Changing Cleanup

Require explicit approval before:

- moving files
- removing files
- normalizing directory layout
- rewriting large documentation surfaces
- changing contributor workflows
- introducing or changing state-modifying scripts

Prefer moving over deleting when cleanup is needed.

If a command or script modifies external or persistent state, require `--dry-run` and default to safe behavior unless the repo already defines a different doctrine.

## Judgment Rules

- Prefer example-first documentation over concept-first exposition.
- Prefer transferable conventions over repo-local quirks.
- Prefer obvious entrypoints over clever layouts.
- Prefer understandable boundaries over hidden state.
- Prefer useful inspection points over noisy telemetry.
- Prefer explicit recovery procedures over implied operator knowledge.
- Prefer a small number of high-value recommendations over a long cosmetic list.

## Anti-Patterns

Treat these as maturity warnings:

- long README prose before the first runnable example
- mystery files or scripts at repo root
- setup docs that require interpretation instead of copy-paste
- swallowed exceptions or generic failures without context
- excessive logs that still do not reveal what failed
- machine-local paths or assumptions
- custom wrappers that hide ordinary ecosystem commands
- important data without backup or restore guidance

## Output Style

Be direct. Explain why each finding matters to a newcomer.

When possible, tie findings to one of these pressures:

- trust
- attention cost
- convention drift
- contributor activation energy
- runtime opacity
- recovery risk
