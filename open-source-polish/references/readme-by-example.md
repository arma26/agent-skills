# README By Example

## Goal

Reduce cognitive overhead. Help the reader reach first success before asking them to absorb architecture or abstractions.

## Required Posture

- lead with exact commands
- show the smallest working path first
- expand from minimal usage to common usage to advanced configuration
- keep explanatory prose behind the examples rather than ahead of them
- separate required setup from optional setup
- mark non-runnable examples clearly

## Preferred README Shape

1. One-sentence description
2. Current status
3. Quickstart with copy-pasteable commands
4. Smallest working example
5. One or two richer examples
6. Links to deeper docs only after first success is visible

## Questions To Ask

- Can a fresh reader copy-paste from the README and get a useful result quickly?
- Is the first example the minimum successful path?
- Do later examples build monotonically instead of branching into complexity early?
- Are environment assumptions explicit and minimal?
- Are expected outputs or effects visible?

## Failure Signals

- concept prose appears before any example
- commands are fragmented across sections
- optional setup is mixed with required setup
- examples skip outputs or expected effects
- the shortest path is hidden below advanced material

## Recommendation Pattern

When the README is too abstract:

- move runnable commands upward
- cut or defer exposition that does not help first success
- collapse duplicated setup into one obvious path
- replace synthetic examples with the smallest real example
