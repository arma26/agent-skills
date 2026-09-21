# Convention Drift

## Goal

Warn when the project spends reader attention on avoidable local conventions instead of borrowing understanding from its ecosystem.

## Core Rule

Do not tolerate drift silently. For each meaningful deviation, state:

- expected standard
- current repo behavior
- newcomer cost
- whether the deviation should be removed or explicitly justified

## Surfaces To Inspect

- repo layout
- install, run, test, and release workflow
- script naming and wrapper behavior
- configuration discovery and env var layout
- code organization and naming
- documentation structure

## Classification

### Acceptable Variation

Variation that remains legible to ecosystem users and does not require private context.

### Justified Deviation

A nonstandard choice with a real benefit that is documented where the reader needs it.

### Unnecessary Deviation

A local convention that adds attention cost without compensating value.

## High-Value Warnings

- custom wrapper scripts hide ordinary `test`, `build`, or `run` behavior
- source or test layout fights ecosystem norms without explanation
- config files are loaded from surprising locations
- names obscure standard concepts behind repo-local terminology
- docs teach exceptions before the normal path

## Recommendation Pattern

- recommend convergence to the ecosystem standard by default
- if convergence is not practical, isolate the deviation and document it explicitly
- explain the cost in newcomer attention, not just in maintainability terms
