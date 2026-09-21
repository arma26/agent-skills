# Polish Checklist

## Goal

Run a compact maturity audit that favors the most trust-breaking issues first.

## First Impression

- Is the project value obvious quickly?
- Is the status honest?
- Is the shortest run path visible?
- Does the root feel intentional?

## Structure

- Can source, tests, docs, scripts, configs, fixtures, and generated files be distinguished quickly?
- Do top-level files have obvious purpose?
- Do any files appear orphaned or ambiguous?

## Contributor Path

- Is setup easy to follow?
- Is there one obvious test path?
- Can a newcomer identify a small safe change?
- Are local assumptions minimized?

## Runtime Clarity

- Are the main inputs and outputs discoverable?
- Are state boundaries explicit?
- Do logs help inspection?
- Are external integrations visible at their boundaries?

## Failure Clarity

- Do errors fail with enough context?
- Are exceptions swallowed?
- Is there a predictable place to look first when behavior goes wrong?

## Convention Leverage

- Can ecosystem knowledge transfer immediately?
- Which local conventions need justification?

## Data Continuity

Apply only when important persistent data exists.

- Is source-of-truth state identified?
- Are backup and restore procedures documented?
- Can bad data be detected and recovered from?
- Are maintenance scripts discoverable and safe?

## Prioritization Rule

Prioritize findings that break trust or waste newcomer attention before cosmetic cleanup.
