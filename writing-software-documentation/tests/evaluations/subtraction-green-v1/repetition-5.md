## Keep — production prerequisites

> “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

- **Reader problem:** Prevents an unauthorized or inadequately scheduled production change.
- **Actual effect:** Safety and operational readiness.
- **Disposition:** **Keep**, with minor wording compression only.
- **Evidence:** Activation affects new connections immediately, while existing connections change only after reconnection.
- **If removed:** The operator loses the authorization check and the need to plan client reconnections.

## Keep — activation and rollback model

> “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

- **Reader problem:** Explains which connections use each credential and when rollback remains possible.
- **Actual effect:** Essential system understanding and safety.
- **Disposition:** **Keep**; compress the preceding “Relay accepts connections through gateways” sentence because it adds no necessary decision.
- **Evidence:** Every stated lifecycle behavior is established by the repository evidence.
- **If removed:** A first-time operator could incorrectly expect activation or rollback to alter existing connections.

## Compress — stage and inspect

> “Stage the replacement with `relay credential stage`.”

> “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

- **Reader problem:** Safely prepares and validates the replacement before activation.
- **Actual effect:** Enablement and pre-activation verification.
- **Disposition:** **Compress** into one numbered operation while retaining both commands and the fingerprint-and-expiry check.
- **Evidence:** Staging stores without activating; inspection prints the pending fingerprint and expiry.
- **If removed:** The operator loses both the safe preparation sequence and the verification gate before activation.

## Remove — generic command commentary

> “Relay has many commands and flags suitable for many different environments and organizational requirements.”

- **Reader problem:** Ostensibly signals configurability.
- **Actual effect:** Delay and distraction; it supplies no actionable detail.
- **Disposition:** **Remove**.
- **Evidence gap:** No repository evidence supports this broad characterization, and complete options already have an authoritative reference.
- **If removed:** No capability, decision, safety property, understanding, or navigation is lost.

## Keep — activation verification

> “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

- **Reader problem:** Activates the staged credential and verifies production authentication without relying on inference.
- **Actual effect:** Enablement and outcome verification.
- **Disposition:** **Keep**, formatted as a concise numbered operation.
- **Evidence:** Activation changes new connections; existing connections require reconnection.
- **If removed:** The operator cannot complete or verify the primary task safely.

## Keep — rollback and recovery verification

> “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

- **Reader problem:** Provides bounded recovery when post-activation authentication fails.
- **Actual effect:** Safety and recovery.
- **Disposition:** **Keep**, while naming the established **30-minute** window directly instead of requiring the reader to recover it from an earlier paragraph.
- **Evidence:** The previous credential remains available for rollback for 30 minutes and rollback affects new connections.
- **If removed:** The operator loses the only documented recovery procedure and its verification step.

## Remove — promotional introduction

> “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

- **Reader problem:** Attempts to orient and motivate the reader.
- **Actual effect:** Throat-clearing and unsupported promotional language.
- **Disposition:** **Remove** entirely; the title already states the task.
- **Evidence gap:** The repository evidence establishes credential behavior, not these product or organizational claims.
- **If removed:** Nothing identifiable is lost.

## Remove — generic security exhortation

> “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

- **Reader problem:** Attempts to provide broad security-policy guidance.
- **Actual effect:** Delay and distraction from the time-sensitive production operation.
- **Disposition:** **Remove** entirely.
- **Evidence gap:** None of these recommendations is established as Relay behavior or a required rotation step.
- **If removed:** No operational capability, concrete decision, safety property, understanding, or navigation is lost.

## Remove — elementary authentication definitions

> “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

- **Reader problem:** Attempts to explain basic authentication terminology.
- **Actual effect:** Distraction; it does not explain Relay’s relevant credential lifecycle.
- **Disposition:** **Remove** and preserve the link to the authentication architecture for readers needing deeper context.
- **Evidence gap:** The generic definitions are unnecessary to the documented operation.
- **If removed:** No task-relevant understanding is lost because the lifecycle model remains and deeper explanation stays discoverable.

## Compress and relocate — reference detail

> “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios. See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.”

- **Reader problem:** Routes readers to exhaustive command options and architectural detail.
- **Actual effect:** Useful navigation mixed with unnecessary option enumeration.
- **Disposition:** **Compress** to two contextual links at the end: command options in `docs/reference/credentials.md` and architecture in `docs/concepts/authentication.md`.
- **Evidence:** Both authoritative destinations are explicitly established; the individual flag categories are not.
- **If removed entirely:** Readers lose navigation to authoritative reference and conceptual material. If only the enumeration is removed, nothing is lost.

## Compress — overall structure

> The complete guide as presented.

- **Reader problem:** Must guide a first-time operator through preparation, activation, verification, and recovery.
- **Actual effect:** The valid operational path is obscured by promotional prose, generic advice, elementary definitions, and duplicated reference detail.
- **Disposition:** **Compress** into: prerequisite; lifecycle model; numbered stage–inspect–activate sequence; expected verification; rollback recovery; two reference links. Removing the three generic paragraphs and tightening the remaining material can exceed the requested 50% reduction without deleting safety-critical content.
- **Evidence:** The repository evidence supports each retained command, result, timing constraint, and link.
- **If the operational model or verification steps disappear to meet the arbitrary length target:** The first-time operator loses the ability to predict connection behavior, validate the replacement, verify success, or recover safely.
