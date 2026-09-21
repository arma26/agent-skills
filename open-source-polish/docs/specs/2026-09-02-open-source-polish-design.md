# Open Source Polish Skill Design

## Purpose

`open-source-polish` turns a functional solo-built project into mature, public-facing software. Other people can understand, run, inspect, and contribute without private context.

The skill assumes the user may have little or no open source release experience. It should guide the repo from prototype state toward an intentional, legible, contributor-friendly project while keeping cleanup actions approval-gated.

## Problem Statement

A working prototype is not automatically a project that is fit for outside readers or contributors.

Common failure modes:

- documentation explains too much before showing a runnable example
- setup paths drift from reality
- the repo contains prototype residue, dangling scripts, local notes, generated debris, or machine-local assumptions
- the codebase depends on repo-specific conventions instead of ecosystem standards
- runtime behavior is opaque, with poor logging, weak exception context, and no predictable inspection points
- important data exists without clear lifecycle, backup, restore, or recovery guidance

These failures exhaust attention. New readers stop before the code's strengths become visible.

## Design Goals

The skill should optimize for:

1. Reader attention economy
2. Trust and operational honesty
3. Structural legibility
4. Low-friction contributor onboarding
5. Runtime understandability
6. Predictable failure inspection
7. Data continuity when the project handles important data
8. Convergence toward industry-standard conventions unless deviation is justified

## Non-Goals

- autonomous destructive cleanup
- repo-wide beautification for style alone
- forcing identical standards across all project types
- inventing process or documentation sections the project does not need

## Core Principles

### Example-First Documentation

The skill should prefer "readmes by example."

Rules:

- lead with copy-pasteable commands
- show the smallest working path first
- expand from minimal usage to realistic usage to advanced configuration
- keep prose subordinate to examples
- separate required setup from optional setup
- mark illustrative examples clearly if they are not directly runnable

The README should let a new reader reach first success with minimal interpretation.

### Convention Leverage

The skill should explicitly warn when a repo drifts away from industry-standard behavior in ways that force contributors to learn local conventions first.

For each significant deviation, the skill should identify:

- expected standard behavior
- current repo behavior
- newcomer cost
- whether the deviation should be removed or documented as intentional

The default recommendation is to converge back to the ecosystem standard unless there is a real benefit to the deviation.

### Approval-Gated Cleanup

The skill must not move, remove, or broadly rewrite project artifacts without explicit user approval.

Allowed by default:

- inspection
- classification
- documentation of findings
- read-only inventories
- proposed cleanup sequences

Approval required:

- file moves
- file removals
- normalization of repo structure
- changes to contributor workflows
- broad documentation rewrites

### Contributor UX Includes Runtime Clarity

A project is not mature if readers can run it but cannot understand what it is doing.

The skill should treat these as contributor UX concerns:

- understandable inputs and outputs
- explicit side effects
- obvious state ownership
- useful logs
- exceptions with context
- predictable inspection points when something fails

### Conditional Data Continuity Requirements

If a project stores, transforms, syncs, or depends on important data, the skill should require a recovery and continuity surface in documentation and tooling.

If the project does not manage meaningful persistent data, the skill should say so explicitly and skip the continuity section.

## Operating Modes

### `prototype-polish`

Use near publication, handoff, release, or public review.

This mode performs a full maturity pass across:

- first impressions
- documentation
- repo structure
- convention drift
- contributor onboarding
- runtime clarity
- failure behavior
- data continuity, if applicable

### `continuous-polish`

Use during development to catch drift before it accumulates.

This mode performs a lighter pass focused on:

- documentation drift
- growing repo clutter
- convention drift
- observability and failure clarity regressions
- contributor setup friction

## Project-Type Matrix

The skill should adapt expectations by project type while keeping the same example-first posture.

Project types:

- library
- CLI
- service / API
- web app
- research or exploratory project

Each type should answer:

- what is the smallest successful example
- what exact commands get the reader there
- what setup can be deferred
- what the next more realistic example is
- what public-facing standards are normal in that ecosystem

## Maturity Rubric

### 1. Attention Economy

Questions:

- can a reader understand the project in under two minutes
- does the README front-load value and execution rather than concept prose
- is the smallest successful path immediately visible

Failure signals:

- long exposition before any example
- fragmented commands that require assembly
- unclear required vs optional setup

### 2. Structural Legibility

Questions:

- is the repo tree easy to parse at a glance
- can a reader distinguish source, tests, docs, scripts, fixtures, and generated output
- do top-level files have clear purpose

Failure signals:

- mystery files at repo root
- scripts without a clear relationship to the project
- generated or scratch artifacts mixed with maintained files

### 3. Narrative Coherence

Questions:

- do docs, scripts, config, and code describe the same reality
- are commands in docs current
- is project status stated honestly

Failure signals:

- drifted setup or run instructions
- stale architecture claims
- hidden prerequisites

### 4. Contributor Ergonomics

Questions:

- can a newcomer make a small safe change
- is there one obvious path to run tests
- are local assumptions minimized

Failure signals:

- contributor flow depends on tribal knowledge
- no obvious first contribution surface
- bespoke workflow wrappers hide standard commands

### 5. Runtime Understandability

Questions:

- are the main inputs, outputs, and side effects easy to identify
- are logs informative rather than noisy
- are inspection points predictable

Failure signals:

- hidden state transitions
- poor boundary logging around I/O and integrations
- telemetry required just to understand local behavior

### 6. Failure Predictability

Questions:

- do errors fail loudly enough at the right boundary
- do exceptions retain useful context
- can a contributor tell where to look when behavior goes wrong

Failure signals:

- swallowed exceptions
- generic errors without context
- no clear debug surface

### 7. Convention Leverage

Questions:

- can an experienced contributor apply ecosystem knowledge immediately
- where does the repo require learning local exceptions first

Failure signals:

- nonstandard layout without explanation
- custom wrappers for ordinary workflows
- local naming or configuration schemes that obscure familiar concepts

### 8. Data Continuity

Conditional: only apply when the project handles important persistent data.

Questions:

- what data matters
- what is source-of-truth vs cache vs derived output
- how is data backed up
- how is it restored
- how is corruption or bad data detected
- how are destructive operations made safe

Failure signals:

- important data without backup or restore guidance
- undocumented recovery steps
- destructive scripts without dry-run or warnings
- unclear separation between persistent state and cache state

## Required Documentation Shape

The skill should prefer a compact, layered documentation shape.

Expected README flow:

1. one-sentence project description
2. current project status
3. quickstart with exact commands
4. smallest working example
5. one or two expanded examples
6. links to deeper docs only after first success is visible

If the project handles important data, documentation should also include a recovery-oriented section covering:

- data model and ownership summary
- backup and restore process
- recovery from bad data scenarios
- disaster recovery assumptions and limits
- maintenance scripts and their safe usage
- continuity risks that still remain

## Skill Workflow

### Phase 1: Orientation

Identify:

- project type
- language and tooling layer
- public entrypoints
- test and verification path
- data-bearing surfaces
- likely first impression path for a new outsider

### Phase 2: First-Impression Audit

Inspect:

- README
- top-level repo layout
- setup path
- example quality
- project status honesty

Output:

- `first_impression_findings`

### Phase 3: Structure And Artifact Audit

Map:

- source code
- tests
- docs
- scripts
- configs
- fixtures
- generated outputs
- temporary files
- local dev artifacts
- files with unclear ownership or integration

Output:

- `artifact_candidates`

### Phase 4: Convention Drift Audit

Compare repo patterns against language, framework, and packaging norms.

Output:

- `convention_drift_warnings`

Each warning should state:

- standard expectation
- observed deviation
- newcomer cost
- recommended action

### Phase 5: Contributor Path Audit

Check whether a stranger can:

- set up the project
- run it
- run tests
- identify a small safe change

Output:

- `contributor_friction_findings`

### Phase 6: Runtime Clarity Audit

Inspect:

- input/output boundaries
- state boundaries
- logging
- exception handling
- inspection points
- internal visibility of integrations and failure paths

Output:

- `runtime_clarity_findings`
- `failure_handling_findings`

### Phase 7: Data Continuity Audit

Conditional on important data handling.

Inspect:

- ownership of data
- lifecycle of data
- backup and restore paths
- repair and quarantine paths
- maintenance and migration tooling
- safety of state-changing scripts

Output:

- `data_continuity_findings`

### Phase 8: Documentation Reconciliation

Compare README, deeper docs, scripts, config, and code behavior.

Output:

- `documentation_drift_findings`

### Phase 9: Cleanup Proposal

Produce a structured proposal grouped by:

- trust-breaking issues
- convention drift warnings
- likely dead or stray artifacts
- documentation fixes
- contributor-onramp improvements
- runtime clarity improvements
- failure handling improvements
- data continuity improvements, if applicable

Output:

- `recommended_cleanup_sequence`

### Phase 10: Approval Gate

Before making state-changing edits, the skill must ask for approval.

Special care:

- removal candidates are hypotheses, not facts
- moving files is preferable to deleting files when cleanup is needed
- scripts that modify external state should support `--dry-run` and default to safe behavior

### Phase 11: Verification Pass

After approved changes:

- re-check quickstart
- re-check examples
- re-check documented commands
- re-check contribution path
- re-check any recovery or maintenance docs affected by the changes

## Output Contract

The skill should emit consistent categories so polishing is repeatable rather than taste-driven.

Required outputs:

- `first_impression_findings`
- `convention_drift_warnings`
- `artifact_candidates`
- `documentation_drift_findings`
- `contributor_friction_findings`
- `runtime_clarity_findings`
- `failure_handling_findings`
- `recommended_cleanup_sequence`

Conditional outputs:

- `data_continuity_findings`
- completed production readiness review, release decision, blockers, and accepted risks for production-release work

## Potential Bundled Resources

Recommended references:

- `references/readme-by-example.md`
- `references/convention-drift.md`
- `references/project-type-matrix.md`
- `references/polish-checklist.md`
- `references/data-continuity.md`
- `references/production-release-rubric.md`
- `assets/production-readiness-review.md`

Potential future script:

- `scripts/inventory_repo.py`

This script should remain read-only by default and only exist if repeated real-world use shows that deterministic inventory generation saves time without obscuring judgment.

## Open Questions

- how aggressively should the skill normalize project structure when a repo is functional but unusual
- should project-type expectations include language-specific overlays later

## Recommendation

Implement `open-source-polish` as a guided global skill with references-first support and optional read-only audit helpers later.

Do not begin with heavy automation. The main value is high-quality judgment about maturity, trust, contributor attention, and avoidable repo-local friction.
