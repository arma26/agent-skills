### Keep — activation and rollback model

- **Location/passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”
- **Reader problem:** Predicting which credential each connection will use and how long rollback remains available.
- **Actual effect:** Enablement and risk reduction.
- **Evidence:** Every behavior is explicitly established by the repository evidence.
- **Direction:** Retain. Removing it would eliminate the minimum system model needed to rotate safely.

### Keep — pending credential verification

- **Location/passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”
- **Reader problem:** Preventing activation of the wrong or expired credential.
- **Actual effect:** Enablement and safety.
- **Evidence:** The command prints the pending fingerprint and expiry.
- **Direction:** Retain. Removing it would eliminate the pre-activation verification gate.

### Keep — activation and controlled validation

- **Location/passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”
- **Reader problem:** Activating the replacement and verifying the result without relying on unaffected existing connections.
- **Actual effect:** Enablement and safety.
- **Evidence:** Activation affects new connections; existing connections retain the old credential until reconnection.
- **Direction:** Retain. Removing any of these steps would leave the primary task incomplete or unverified.

### Keep — rollback and recovery verification

- **Location/passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”
- **Reader problem:** Recovering from failed activation while rollback is available.
- **Actual effect:** Recovery and risk reduction.
- **Evidence:** The previous credential remains available for rollback for 30 minutes and rollback restores it for new connections.
- **Direction:** Retain. Removing it would eliminate the documented recovery path and its verification.

### Keep — staging operation

- **Location/passage:** “Stage the replacement with `relay credential stage`.”
- **Reader problem:** Storing the replacement without prematurely activating it.
- **Actual effect:** Enablement.
- **Evidence:** The command stores a replacement credential without activating it.
- **Direction:** Retain. Removing it would omit the first required operation.

### Compress — prerequisites

- **Location/passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”
- **Reader problem:** Avoiding an unauthorized change and allowing time to test a new connection.
- **Actual effect:** Safety, but with more wording than necessary.
- **Evidence:** Authorization is labeled general operational guidance; reconnect planning follows from the documented connection behavior.
- **Direction:** Compress to a short authorization and controlled-reconnection prerequisite. Removing it entirely would lose an important production-change safeguard.

### Remove — unsupported gateway detail

- **Location/passage:** “Relay accepts connections through gateways.”
- **Reader problem:** Purported system orientation.
- **Actual effect:** Distraction and unsupported background.
- **Evidence gap:** The supplied repository evidence does not establish gateways, and the fact is unnecessary for credential rotation.
- **Direction:** Remove. No required capability or decision would be lost.

### Remove — promotional introduction

- **Location/passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”
- **Reader problem:** Purported orientation and motivation.
- **Actual effect:** Delay and generic promotion.
- **Evidence gap:** None of these claims helps execute or verify the rotation.
- **Direction:** Remove the paragraph. No capability, safety property, or useful understanding would be lost; the title already states the goal.

### Remove — generic command commentary

- **Location/passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”
- **Reader problem:** Purported awareness of configuration flexibility.
- **Actual effect:** Delay and ambiguity.
- **Evidence gap:** The evidence establishes only that complete command options live in the credential reference.
- **Direction:** Remove. Navigation is preserved by the reference link.

### Remove — aspirational security prose

- **Location/passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”
- **Reader problem:** Purported broader security guidance.
- **Actual effect:** Distraction and delay during an operational procedure.
- **Evidence gap:** The statements are generic and establish no product behavior or actionable decision.
- **Direction:** Remove the paragraph. Nothing identifiable would be lost.

### Remove — elementary authentication definition

- **Location/passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”
- **Reader problem:** Purported conceptual background.
- **Actual effect:** Delay; it does not explain behavior needed for the rotation.
- **Evidence gap:** The repository evidence supports linking to the authentication architecture, not these generic statements.
- **Direction:** Remove. No operational capability or necessary mental model would be lost.

### Remove — unsupported option inventory

- **Location/passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”
- **Reader problem:** Purported preview of reference material.
- **Actual effect:** Duplication and unsupported detail.
- **Evidence gap:** The evidence confirms that complete options are documented elsewhere but does not establish this specific list.
- **Direction:** Remove the inventory. The reference link preserves discovery without duplicating details.

### Relocate — command reference link

- **Location/passage:** “See `docs/reference/credentials.md` for every command option.”
- **Reader problem:** Finding required command syntax and less-common options.
- **Actual effect:** Useful navigation, currently separated from the first command.
- **Evidence:** The evidence identifies this file as the authoritative command-option reference.
- **Direction:** Preserve the link but place it beside the staging command or at the start of the procedure. Removing it would strand readers who need actual option syntax.

### Relocate — authentication architecture link

- **Location/passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”
- **Reader problem:** Supporting deeper conceptual inquiry.
- **Actual effect:** Useful secondary navigation.
- **Evidence:** The evidence identifies this file as the authoritative architecture source.
- **Direction:** Preserve as a compact related-concept link after the system model or at the end. Removing it would eliminate the discovery path for deeper authentication questions.
