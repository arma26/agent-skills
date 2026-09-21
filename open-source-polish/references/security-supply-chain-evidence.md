# Security and supply-chain evidence

## Purpose

Use this reference when the security or supply-chain overlay activates. Inspect the mechanisms that exist. Do not require a mechanism only because an external checklist includes it.

Prefer precise behavior observations over scores, badges, or broad labels. Record an unavailable external setting as an `evidence_gap`. Keep maintainer context separate from observed evidence.

## Workflow trust

When automation has secrets, tokens, or write authority, determine:

- whether untrusted event data can become executable script text.
- whether a privileged trigger checks out or runs code from an untrusted change.
- whether permissions default to read-only and expand only for the job that needs them.
- whether third-party actions, build images, and executable build inputs use reviewable immutable identities or another documented integrity control.
- whether dependency updates preserve both reviewability and timely security updates.

Apply these questions from M0 when the mechanism exists. Project age does not reduce workflow injection or credential risk.

## Executable artifacts

For each tracked or distributed executable artifact, identify:

- its purpose and consumers.
- its source and build path.
- its update owner and review rule.
- the method that relates it to reviewed source, such as a reproducible build, digest, signature, or provenance.

Distinguish executables from images, documentation, test fixtures, vendored data, and required platform files. A binary format alone is not a defect.

## Change controls

When the project claims protected changes or independent review, determine:

- whether changes use the intended pull-request or merge-request route.
- whether required checks gate the merge.
- whether approval covers the latest reviewable change.
- whether a material change invalidates stale approval.
- whether release logic, credentials, privileged workflows, and other sensitive paths receive suitable review.

Independent review is risk-dependent for a single-maintainer project. Record the limitation instead of prescribing an inoperable process.

## Dependency integrity and response

Determine:

- which dependencies execute during build, test, release, or automation.
- how maintainers fix those dependencies to reviewable identities when reproducibility or privilege requires it.
- who owns dependency intake and updates.
- how maintainers learn about known vulnerabilities.
- what happens when an update cannot be accepted promptly.

A lock file or update bot proves configuration. Establish ownership and response before crediting an operating process. Pair pinning with an update path so integrity controls do not create unmanaged staleness.

## Release verification

Separate these claims:

1. A defined workflow builds packages from reviewed source.
2. A release includes a signature or provenance statement.
3. The project provides consumer verification steps.
4. The verification binds the artifact to the expected source and release identity.
5. A component inventory exists when downstream vulnerability response needs one.

Do not treat a signature file, provenance file, or software bill of materials as proof of consumer verification.

## Specialized analysis

Recommend fuzzing, static analysis, or similar techniques when the attack surface justifies them. Relevant triggers include parsers, protocol handlers, file readers, memory-unsafe code, and complex untrusted inputs.

Do not require a specific tool when an existing method covers the risk. State what risk remains and what evidence the method produces.

## External integrations and identities

When privileged callbacks or webhooks exist, identify how the receiver authenticates their origin and prevents replay when replay has material effects.

For privileged maintainer, automation, and release identities, identify:

- required strong authentication.
- account and credential recovery ownership.
- rotation or revocation paths where credentials exist.
- the evidence boundary when account settings are not visible from the repository.

Do not request administrative credentials only to complete an audit. Mark inaccessible settings as `evidence_gap` and state what evidence would resolve the gap.

## Finding record

For each finding, record:

- the precise behavior under review.
- why it applies at the target milestone or under an active risk overlay.
- direct repository or authorized external evidence.
- evidence limits and detection uncertainty.
- maintainer context or an alternative control, kept separate from the observation.
- the smallest applicable remediation.

Discard a recommendation when it only improves a badge, score, or checklist result without unlocking a milestone gate or reducing an active risk.
