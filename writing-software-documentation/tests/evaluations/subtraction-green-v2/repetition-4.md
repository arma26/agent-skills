### Opening paragraph

- **Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”
- **Reader problem:** Orient the operator to the procedure.
- **Actual effect:** Delays the procedure with promotional, generic, and self-evident background.
- **Disposition:** remove
- **Loss if absent:** Nothing; the title already establishes the task.

### Connection and rollback model

- **Passage:** “Relay accepts connections through gateways. A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”
- **Reader problem:** Explain when credentials take effect and which connections rollback affects.
- **Actual effect:** Provides the minimum system model needed to plan reconnections and understand rollback limits. The gateway sentence adds no behavior needed for this task.
- **Disposition:** compress
- **Loss if absent:** The operator could wrongly expect staging or activation to change existing connections, or miss the 30-minute recovery window. Remove only the gateway sentence and tighten the remaining verified behavior.

### Prerequisites

- **Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”
- **Reader problem:** Prevent an unauthorized or operationally incomplete production change.
- **Actual effect:** Establishes necessary authority and scheduling prerequisites.
- **Disposition:** keep
- **Loss if absent:** The operator may begin without authorization or sufficient time to validate reconnected clients.

### Staging operation

- **Passage:** “Stage the replacement with `relay credential stage`.”
- **Reader problem:** Store the replacement without activating it.
- **Actual effect:** Gives the first required operation directly.
- **Disposition:** keep
- **Loss if absent:** The operator cannot begin the rotation procedure.

### Generic command commentary

- **Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”
- **Reader problem:** Indicate that additional command variants exist.
- **Actual effect:** Adds no actionable detail and interrupts the stage–inspect–activate sequence.
- **Disposition:** remove
- **Loss if absent:** Nothing; the command reference supplies discoverability.

### Pending-credential verification

- **Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”
- **Reader problem:** Verify that the staged credential is the intended replacement before activation.
- **Actual effect:** Supplies both the inspection command and its decision criterion.
- **Disposition:** keep
- **Loss if absent:** The operator could activate the wrong credential or one with an unsuitable expiry.

### Activation and controlled verification

- **Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”
- **Reader problem:** Activate the credential and verify production authentication safely.
- **Actual effect:** Connects activation to its observable result and gives a bounded verification step.
- **Disposition:** keep
- **Loss if absent:** The operator loses either the activation instruction, the new-connection behavior, or the evidence needed to conclude the rotation succeeded.

### Failure recovery

- **Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”
- **Reader problem:** Recover from failed authentication while rollback remains possible.
- **Actual effect:** Provides the supported recovery operation, its scope, and post-rollback verification.
- **Disposition:** keep
- **Loss if absent:** The operator may miss the 30-minute recovery opportunity or assume rollback repairs existing connections.

### Security exhortation

- **Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”
- **Reader problem:** Encourage broader security governance.
- **Actual effect:** Adds generic advice unrelated to completing or verifying this rotation.
- **Disposition:** remove
- **Loss if absent:** Nothing needed for the primary task.

### Generic authentication definitions

- **Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”
- **Reader problem:** Explain authentication to an inexperienced reader.
- **Actual effect:** States generic concepts without improving the operator’s decisions or actions.
- **Disposition:** remove
- **Loss if absent:** Nothing needed for rotation; deeper architecture remains discoverable through the concept link.

### Option inventory

- **Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”
- **Reader problem:** Signal the availability of less-common command options.
- **Actual effect:** Duplicates reference-level detail and distracts from the primary procedure.
- **Disposition:** relocate
- **Loss if absent:** Discoverability of advanced options would disappear only if the adjacent command-reference link were also removed; retain that link.

### Command reference

- **Passage:** “See `docs/reference/credentials.md` for every command option.”
- **Reader problem:** Find complete syntax and options without expanding the operational guide.
- **Actual effect:** Provides concise navigation to the authoritative command reference.
- **Disposition:** keep
- **Loss if absent:** Operators needing profiles, paths, output settings, or other options lose the route to authoritative details.

### Authentication architecture link

- **Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”
- **Reader problem:** Support deeper conceptual inquiry outside the immediate operation.
- **Actual effect:** Preserves optional navigation without interrupting the procedure.
- **Disposition:** keep
- **Loss if absent:** Readers who need the broader authentication model lose its discovery path.
