# Audit field guide

## Purpose

Use these patterns to improve judgment during a repository audit. They are leads to validate, not automatic findings.

## Suspicious patterns

Investigate when you find:

- a generic root script such as `prepare`, `setup`, or `clean` that moves, removes, commits, publishes, or changes external state.
- a required workflow that exists only as a maintainer's shell alias.
- setup commands that write to global, home-directory, or shared configuration without explaining scope and cleanup.
- a changelog, roadmap, support table, or version policy that looks authoritative but stopped updating.
- release automation without a documented release owner or support policy.
- a maintainer roster without review routing in a multi-component repository.
- a governance link to another repository without a local source-of-truth map.
- generated files whose source and edit rules are unclear.
- issue, support, discussion, and security links that route the same request differently.
- a wrapper that hides ordinary ecosystem commands or adds undocumented side effects.
- backup instructions without inspection, isolated restore, integrity checks, or rollback.
- a "dry run" that still authenticates, writes cache state, sends requests, or changes remote state.
- examples that place secrets in command arguments, tracked files, logs, or shell history.
- a production guide that describes creation but not inspection, failure, or recovery.
- tool-specific agent files that restate the same rules but disagree on scope, commands, or completion.
- agent setup that depends on personal shell aliases, home-directory paths, an ambient logged-in account, or undocumented credentials.
- an agent work request with no observable acceptance boundary or with several unrelated outcomes.
- a handoff that says checks passed without naming the command, scenario, result, or unverified surface.
- instructions that let repository, issue, pull-request, log, or user content expand agent permissions.
- automated agents that can push, merge, publish, message, deploy, or spend money without an explicit authority boundary and disable path.
- a privileged workflow that interpolates issue, pull-request, branch, commit, or log content into executable scripts.
- a privileged workflow that checks out or runs code from an untrusted change.
- third-party workflow code or build images that use mutable identifiers without an integrity and update policy.
- a generated executable with no identified source, rebuild path, verification method, or update owner.
- a dependency update bot with no owner or response path for blocked updates.
- release signatures or provenance with no documented consumer verification path.
- a privileged webhook or callback with no origin-authentication mechanism.
- an inaccessible forge or account setting reported as fulfilled instead of an evidence gap.

For each pattern, find its owner, consumers, actual effects, and documentation before recommending a change.

## Edge cases

### Central governance

A project family can keep governance, conduct, or membership in one repository. Treat this as mature only when the local repository names the external source of truth and explains local authority.

### Small or single-maintainer projects

A flat owner list can be sufficient. Recommend path-scoped ownership only when components, sensitive areas, or review load make routing ambiguous.

### Projects that do not accept contributions

They do not need a contributor workflow. They do need an explicit statement that outside changes are not accepted and a route for defects or feedback.

### Research, archived, and demonstration repositories

Honest status, reproducibility, inputs, outputs, and limitations matter more than release machinery. Do not prescribe governance or support promises that the project does not intend to provide.

### Hosted documentation

Hosted docs can remain authoritative. The repository should still provide a stable local bridge and explain source, generation, and publication boundaries.

### Generated or vendored trees

Their unusual size or shape is not clutter by itself. Check whether contributors can identify the source, generator, update command, review rule, and generated status.

### Monorepos

A busy root can be justified. Require a component map and ownership model before recommending directory normalization.

### Public prototypes with risk

Risk can pull one control forward without requiring the entire later milestone. For example, a prototype that accepts credentials needs secret-handling guidance, not a full maintainer succession policy.

### Prototypes developed by agents

Agent use pulls the M0 instruction, environment, work-unit, verification, and handoff contracts forward. It does not pull autonomous triage, merge authority, bot credential rotation, or production controls forward unless those capabilities exist.

### Several agent tools

Different tools can need adapter files or directory-scoped instructions. Prefer pointers to one canonical authority plus genuinely tool-specific deltas. Do not require one physical file when the repository has a coherent precedence model.

### Closed contribution model

A project can reject external contributions while using internal coding agents. Audit the agent environment and authority contracts. Apply submission requirements according to the contribution policy.

### Libraries, CLIs, services, and web applications

Apply the project-type matrix. A library needs an import example. A CLI needs an invocation and output. A service needs startup and request verification. A web application needs a route or screen and a verification path.

### Historical documents

An old changelog or proposal archive can be useful. It becomes a problem only when readers can mistake it for current authority.

## Low-value recommendations

Avoid these unless evidence shows a concrete need:

- adding formal governance to a first public prototype.
- demanding a full security policy when the project has no meaningful exposure and makes no support promise.
- creating `CODEOWNERS` for a simple single-owner repository.
- requiring a release cadence before recurring releases exist.
- requiring an Architecture Decision Record for routine local choices.
- moving conventional files only to make the root look cleaner.
- deleting ambiguous artifacts before identifying ownership and consumers.
- adding dashboards when local logs and errors would provide enough clarity.
- manufacturing roadmap dates, support promises, or adoption evidence.
- copying generic community templates that no maintainer will operate.
- rewriting a large README when moving one runnable example would solve the main problem.
- requiring a development container when repository-owned setup and validation are already reproducible.
- requiring identical agent tooling across platforms instead of one stable environment and verification contract.
- requiring AI attribution when the project can instead state a deliberate no-attribution policy.
- adding autonomous bots to demonstrate maturity when bounded human-invoked agents satisfy the project need.
- creating several tool-specific instruction files when one canonical entry point is sufficient.
- requiring fuzzing or static analysis without a relevant attack surface or an unresolved risk that the analysis addresses.
- requiring independent review that a single-maintainer project cannot operate, unless the affected path carries exceptional risk.

## Erroneous audit practices

- Treating every missing later-stage practice as a defect.
- Equating project popularity or age with maturity.
- Treating the presence of a file as proof that its process operates.
- Treating automation as policy or ownership.
- Assuming a nonstandard layout is wrong before finding its purpose.
- Recommending deletion because a file has no obvious consumer after a shallow search.
- Calling cache or generated data a source of truth without evidence.
- Requiring production recovery for disposable development data.
- Accepting backup creation as proof of recoverability.
- Recommending more documentation when the problem is conflicting authority.
- Using an external dashboard as the only inspection route for normal local failure.
- Expanding scope from audit to cleanup without explicit approval.
- Treating an `AGENTS.md`, `CLAUDE.md`, or similar filename as proof that its commands, precedence, and authority model work.
- Treating CI as the source of product intent, task authority, or complete verification.
- Measuring work units by diff size while ignoring distinct outcomes, owners, permissions, or rollback paths.
- Treating agent-to-agent delegation as new permission to mutate external systems.
- Requiring production automation controls for a local coding assistant that has no production authority.
- Treating a workflow file, dependency bot, security policy, or signature as proof that its process operates.
- Equating commit frequency or contributor-company diversity with project maturity.
- Treating a hidden forge, webhook, or account setting as satisfied because the audit cannot inspect it.
- Recommending dependency pinning without an owner and update path.

## Red flags that can cap maturity

Validate and report these before ordinary polish findings:

- setup instructions can destroy unrelated or ambiguously targeted state.
- tracked content contains a credential, private key, personal data, or machine-specific identity.
- the documented default publishes, deploys, bills, emails, or changes remote state.
- recovery instructions overwrite active data without target checks or isolation.
- security reports route to a public channel for a project with meaningful exposure.
- release artifacts cannot be related to their source or version.
- multiple documents claim conflicting authority for releases, support, security, or governance.
- required contributor commands differ materially from the checks that gate merge.
- agent setup uses a personal identity or credential implicitly, or writes outside declared boundaries without recovery guidance.
- conflicting instruction files make the applicable authority or safe command path indeterminate.
- the documented agent default can publish, merge, deploy, message, bill, or mutate external state without explicit approval.
- an autonomous agent consumes untrusted content as instruction and has privileged external authority without containment or a disable path.
- privileged automation executes untrusted code or interpolates untrusted content with access to secrets or write authority.
- a distributed executable cannot be related to reviewed source or a reproducible, verifiable build.
- privileged callbacks accept unauthenticated events that can change repository, release, deployment, or production state.

## Recommendation test

Before retaining a recommendation, ask:

1. Which target milestone gate does it unlock?
2. Which active risk does it reduce?
3. What repository evidence supports it?
4. What is the smallest change that resolves the gap?
5. Would the recommendation create maintenance work without a clear owner?

Remove a recommendation when it unlocks no gate, reduces no active risk, or creates unsupported ceremony.
