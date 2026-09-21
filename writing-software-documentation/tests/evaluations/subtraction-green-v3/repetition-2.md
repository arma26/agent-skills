### Stage operation — primary-task blocker

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Begin the rotation without activating the replacement.

**Actual effect:** Identifies the required operation, but the supplied evidence does not establish how the credential is passed. Keep the step and place the credentials-reference link immediately beside it.

**Evidence:** Repository evidence establishes that the command stores a replacement without activating it; complete options live in `docs/reference/credentials.md`.

**Disposition:** keep

**Loss if absent:** The operator cannot begin the rotation.

### Pending-credential verification

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Prevent activation of the wrong or expired credential.

**Actual effect:** Provides the necessary pre-activation safety check and observable result.

**Evidence:** Repository evidence establishes that the command prints the pending credential fingerprint and expiry.

**Disposition:** keep

**Loss if absent:** The operator could activate an unintended credential without detecting the mismatch.

### Activation and controlled verification

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activate the replacement and verify that new authentication succeeds.

**Actual effect:** Supplies the central state-changing operation, its result, and a bounded verification action.

**Evidence:** Repository evidence establishes that activation affects new connections while existing connections retain the previous credential until reconnection. Controlled-client verification is general operational guidance consistent with that behavior.

**Disposition:** keep

**Loss if absent:** The operator loses both the activation procedure and the first practical confirmation that it worked.

### Rollback and recovery boundary

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recover from failed authentication after activation.

**Actual effect:** Gives an evidence-backed rollback and verification path. Add one concise limitation that recovery after the 30-minute window is not established by repository evidence.

**Evidence:** Repository evidence establishes that rollback restores the previous credential for new connections during the 30-minute retention window. It provides no recovery behavior after that window.

**Disposition:** keep

**Loss if absent:** The operator loses the documented recovery action during the only established rollback window.

### Credential lifecycle model

**Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Predict which credential each connection uses and when rollback remains possible.

**Actual effect:** Provides the minimum system model needed to plan reconnections and avoid misunderstanding activation as an immediate change to every connection.

**Evidence:** Every clause is directly established by the supplied repository evidence.

**Disposition:** keep

**Loss if absent:** A first-time operator cannot predict activation scope, reconnection behavior, or rollback lifetime.

### Production prerequisite

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Avoid an unauthorized or poorly scheduled production change.

**Actual effect:** Supplies useful safety guidance but can be shortened to a direct prerequisite such as “Confirm authorization and plan a window for controlled client reconnection.” Authorization should remain recognizable as general operational guidance, not claimed product enforcement.

**Evidence:** Reconnection behavior is established by repository evidence. No supplied evidence establishes an authorization mechanism or formal maintenance-window requirement.

**Disposition:** compress

**Loss if absent:** The operator loses the explicit prompt to confirm change authority and allocate time for reconnection testing.

### Command reference placement

**Passage:** “See `docs/reference/credentials.md` for every command option.”

**Reader problem:** Find the complete syntax omitted from the operational guide.

**Actual effect:** Provides necessary navigation, but it arrives after every command. Move it beside the first command so the operator can stage the credential without guessing.

**Evidence:** Repository evidence identifies this file as the authoritative location for complete command options.

**Disposition:** relocate

**Loss if absent:** The operator has no evidence-backed route to the complete command syntax.

### Authentication architecture navigation

**Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Find deeper conceptual material when the operational model is insufficient.

**Actual effect:** Preserves a concise discovery path without interrupting the procedure.

**Evidence:** Repository evidence identifies this file as the authentication-architecture destination.

**Disposition:** keep

**Loss if absent:** Readers needing deeper architectural context lose the documented navigation path.

### Guide title

**Passage:** “# Rotate a Relay credential”

**Reader problem:** Identify the operation covered by the page.

**Actual effect:** States the reader goal directly.

**Evidence:** The scenario defines credential rotation as the guide’s task.

**Disposition:** keep

**Loss if absent:** The page no longer clearly names its operational goal.

### Marketing and throat-clearing

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Introduce the product and topic.

**Actual effect:** Delays the procedure without adding a prerequisite, system behavior, decision, or recovery capability. The title already states the topic.

**Evidence:** The supplied evidence supports none of the marketing or organizational-maturity claims.

**Disposition:** remove

**Loss if absent:** None.

### Unsupported gateway detail

**Passage:** “Relay accepts connections through gateways.”

**Reader problem:** Orient the reader to connection architecture.

**Actual effect:** Adds an architectural claim that is unnecessary for rotation and unsupported by the supplied evidence.

**Evidence:** The repository evidence describes connection behavior but does not mention gateways.

**Disposition:** remove

**Loss if absent:** None for credential rotation.

### Generic command commentary

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Signal that additional command choices exist.

**Actual effect:** Adds vague, unsupported commentary while delaying the verification step. The authoritative reference link handles discovery more precisely.

**Evidence:** Repository evidence establishes only that complete command options live in `docs/reference/credentials.md`.

**Disposition:** remove

**Loss if absent:** None; the relocated reference link preserves navigation.

### Motivational security commentary

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Encourage broader security-process reflection.

**Actual effect:** Interrupts time-sensitive recovery guidance with generic advice that enables no concrete action in this rotation.

**Evidence:** None of these claims is established by the supplied repository evidence.

**Disposition:** remove

**Loss if absent:** None for the primary reader’s task.

### Generic authentication explanation

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Explain basic authentication and security concepts.

**Actual effect:** Repeats background knowledge without clarifying Relay’s credential lifecycle or enabling an operational decision.

**Evidence:** The first sentence is only implicit in the scenario; the remaining sentences are generic guidance rather than documented product behavior.

**Disposition:** remove

**Loss if absent:** None; the retained lifecycle model and architecture link provide relevant understanding and navigation.

### Unsupported option inventory

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Preview available command options.

**Actual effect:** Duplicates reference-level detail and makes claims about specific option categories not established by the supplied evidence.

**Evidence:** Repository evidence says only that complete command options live in `docs/reference/credentials.md`.

**Disposition:** remove

**Loss if absent:** None; the reference link remains.

The removals and prerequisite compression cut approximately half the guide while preserving the lifecycle model, authorization warning, stage–inspect–activate workflow, verification, rollback, and authoritative navigation.
