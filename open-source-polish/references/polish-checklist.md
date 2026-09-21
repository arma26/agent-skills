# Polish checklist

## Use

Apply this checklist after selecting a target milestone. Assess requirements at or below that target. Apply triggered risk overlays at every stage.

## Public interface

- Is the purpose obvious?
- Is the status honest?
- Is the smallest useful path visible and copy-pasteable?
- Does the documented result include a verification step?
- Are required and optional setup separate?
- Do support, issue, discussion, and security routes agree?

## Structure and artifacts

- Can readers distinguish source, tests, docs, scripts, configuration, fixtures, generated files, caches, and archives?
- Does each unusual root file have an owner or documented consumer?
- Do script names disclose their effects?
- Do generated trees identify their source and edit rule?
- Do tracked executables identify their source, purpose, rebuild or verification path, and update owner?
- Are stale artifacts marked as historical before they become misleading?

## Contributor path

- Can a contributor find wanted work before investing in setup?
- Is there one repository-owned setup path?
- Do local checks correspond to automated checks?
- Can contributors find component ownership and review expectations?
- Do claimed merge controls cover required checks and the latest reviewable change?
- Does the project state when an issue, proposal, or design record must precede implementation?

## Agent development

- Is there one canonical repository-owned instruction authority with explicit precedence?
- Can an agent establish the supported toolchain, writable boundaries, identity, credentials, setup side effects, cleanup, and smallest validation path without private context?
- Does one work unit represent one reviewable outcome with explicit acceptance and verification?
- Do work requests and handoffs preserve scope, authority, observed evidence, unresolved risk, and the next owner?
- Are human, agent, CI, VCS, and external-system responsibilities distinct?
- At later milestones, do automated agents have bounded roles, non-personal identities, owners, disable paths, and auditable production controls?

## Project operating system

- Who decides, reviews, merges, releases, supports, and responds to incidents?
- How does the project add, remove, and replace maintainers when its target milestone requires governance?
- Where are decisions and release results recorded?
- Does release automation have a documented owner and policy?
- Do documentation sources, generated output, and publication jobs have clear boundaries?

## Runtime and failure clarity

- Are main inputs, outputs, state owners, and side effects discoverable at the applicable stage?
- Is there a predictable first inspection point for each major component?
- Do errors contain context that helps the intended reader act?
- Can local behavior be understood without external dashboards?

## Risk overlays

- Security: Are untrusted inputs and code separated from privileged automation, and are tokens least-privilege?
- Security: Are privileged identities, vulnerability intake, and authenticated callbacks controlled in proportion to their authority?
- Data continuity: Are source-of-truth, backup, restore, integrity, and rollback defined?
- Operations: Are deployment ownership, inspection, incident, and rollback routes clear?
- Supply chain: Can maintainers review and update build dependencies without losing reproducibility?
- Supply chain: Can users relate published artifacts to reviewed source and perform the claimed verification?

## Prioritization

Apply this order:

1. Active safety contradiction.
2. Unmet gate in the current milestone.
3. Unmet gate in the target milestone.
4. Convention or documentation drift that blocks those gates.
5. Later-stage improvement.
6. Cosmetic cleanup.
