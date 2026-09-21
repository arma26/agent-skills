# Maturity milestones

## Model

Maturity describes the project's operating capability. It does not describe popularity, code volume, company size, or age.

Milestones are cumulative. A project reaches a milestone when it satisfies that milestone's required gates and all earlier gates. A requirement can be `not_applicable` when repository evidence explains why.

Risk overlays can pull a later capability forward. This does not advance the project's general maturity level.

## M0: reproducible prototype

Goal: another informed person can understand the experiment and reproduce its claimed result.

Required gates:

- The repository states what the project is and what status it has.
- It states the supported use or narrow claim.
- It gives a minimal run or reproduction path with prerequisites, inputs, and expected result.
- The root separates durable work from obvious temporary or generated output.
- No setup-looking command hides destructive behavior.
- Known limitations and major non-goals are visible.
- One canonical agent instruction entry point defines authority, scope, and precedence, unless the repository explicitly prohibits agent-authored or agent-reviewed changes.
- The agent environment contract provides repository-owned setup and validation, tool and identity expectations, writable and state ownership boundaries, side effects, least-privilege external capabilities, and failure cleanup.
- The project defines an acceptable work unit, an applicable quality floor, and the minimum work-request, verification, status, and handoff information needed to distinguish complete work from partial work.

Not required by default:

- Formal governance.
- A security contract.
- A release cadence.
- Broad contributor automation.
- Production operations guidance.
- Long-term compatibility promises.

## M1: public prototype

Goal: an outside user can evaluate or use the project without private maintainer context.

Required gates:

- M0 is fulfilled.
- The repository has a clear license when public reuse is intended.
- The README leads to the smallest useful success.
- Install or run commands use ordinary ecosystem conventions or explain deviations.
- The repository states where users should ask questions or report defects.
- Public artifacts or releases have a discoverable source and status.
- Basic failure guidance identifies the first place to inspect.
- A clean external agent environment can reproduce setup and validation without private machine context.
- The project states whether agent-authored contributions are accepted and which review or disclosure rules apply.

Not required by default:

- Maintainer elections or succession.
- Scoped review teams.
- Formal design proposals.
- Multiple supported release lines.
- A complete security response process.

## M2: contributor-ready project

Goal: an outside contributor can select wanted work, prepare a change, verify it, and submit it through the expected interface.

Required gates:

- M1 is fulfilled.
- The project states whether it accepts outside contributions.
- Contributor setup and tests use repository-owned commands.
- Local validation corresponds to continuous integration checks.
- Contribution guidance states when prior discussion is required.
- Issue and pull request routes collect the information maintainers need.
- A maintainer or owner can be found for each major component.
- The repository maps its major directories or components.
- Source and generated documentation boundaries are explicit.
- A code of conduct or governing community conduct policy is discoverable when community interaction occurs.
- Agent instructions cover the applicable issue, change, test, documentation, generated-file, and review workflow.
- Agents can identify work that requires prior discussion or specialist approval and can route changes to the correct owner.

Useful but not universal:

- Starter issue labels.
- Development containers.
- Pull request templates.
- Path-scoped ownership.
- Dependency update automation.

## M3: maintained project

Goal: the project can make decisions, ship changes, support releases, and transfer routine maintenance without relying on one person's memory.

Required gates:

- M2 is fulfilled.
- Decision authority and maintainer responsibilities are documented.
- The project defines how maintainers join, leave, or become inactive when more than one maintainer exists.
- Significant changes have an intake and durable decision process.
- Release ownership, release-note authority, and release procedure are clear.
- Supported versions, compatibility, deprecation, or an explicit no-support policy are clear.
- Security reports have a private route and a proportional response process.
- Component ownership becomes scoped when a flat roster no longer routes review well.
- Support routes distinguish questions, defects, proposals, and incidents.
- Dependency acceptance and update responsibility are defined.
- Contributor and operator documentation has an owned publication path.
- Component-scoped agent instructions refine one canonical authority without contradiction.
- Automated agents have named owners, bounded roles, identities, credential scopes, generated-source boundaries, and escalation or disable paths.

Useful but context-dependent:

- Scheduled release cadence.
- Voting thresholds.
- Formal proposal templates.
- Backport automation.
- Adopters lists.
- Public roadmaps.

## M4: operationally mature project

Goal: the project can sustain production use, important data, multiple maintainers, releases, and failure recovery.

Required gates apply only to relevant project shapes:

- M3 is fulfilled.
- Production ownership and inspection points are clear.
- Incident, rollback, and upgrade or downgrade responsibilities are documented.
- Important data has a tested backup, isolated restore, integrity check, and recovery path.
- Release artifacts have provenance and verification appropriate to their distribution risk.
- Supported release lines have backport and end-of-life rules.
- Maintainer succession and sensitive-area ownership reduce single-person dependency.
- Community triage and design processes remain usable at project scale.
- Operators can distinguish source-of-truth, cached, derived, and disposable state.
- Production-affecting agents use least privilege, explicit approval gates, durable audit trails, non-personal identities, and credential lifecycle controls.
- Operators can inspect, pause, disable, roll back, and recover agent activity, including partial, duplicate, retried, or stale work.
- Untrusted content is separated from instruction authority, and rate, cost, retry, and false-positive limits are defined.

Useful but context-dependent:

- Release champions.
- Specialist review teams.
- Security advisories and CVE coordination.
- Software bills of materials.
- Recovery rehearsals.
- Formal service objectives.
- Public adoption evidence.

## Target selection guide

Use these signals to select a target:

| Project intent | Usual target |
|---|---|
| Experiment, research claim, or handoff | M0 |
| First public release or public evaluation | M1 |
| Soliciting outside changes | M2 |
| Recurring releases and shared maintenance | M3 |
| Sustained production service, broad distribution, or a large contributor base | M4 plus relevant overlays |

Important data activates the data-continuity overlay at the project's actual target. It does not promote a prototype to M4 by itself.

The author's explicit goal overrides these defaults unless it conflicts with active risk.

## Audit presentation

Begin with a summary like this:

| Milestone | State | Blocking gaps | Next improvement |
|---|---|---|---|
| M0 reproducible prototype | fulfilled | None | Preserve the minimal reproduction path. |
| M1 public prototype | partial | No expected output | Add one observable result. |
| M2 contributor-ready | not_due | Not assessed as a failure | Revisit when outside contributions open. |
| M3 maintained | not_due | Not assessed as a failure | Revisit before recurring supported releases. |
| M4 operationally mature | not_due | Not assessed as a failure | Revisit before sustained production or ecosystem scale. |

For each assessed requirement, record:

| Requirement | Status | Evidence | Effect | Smallest next improvement |
|---|---|---|---|---|

Do not collapse `not_due`, `not_applicable`, and `evidence_gap` into `unmet`.
