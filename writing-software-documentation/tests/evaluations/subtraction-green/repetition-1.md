### 1

**Passage:** “# Rotate a Relay credential”

**Reader problem:** Identifies the production operation.

**Actual effect:** Provides immediate orientation.

**Evidence:** The supplied repository evidence describes the credential-rotation workflow.

**Disposition:** keep

**Loss if absent:** The guide would lack a clear task identity.

### 2

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Attempts to introduce the product and justify rotation.

**Actual effect:** Delays the operational procedure with promotional language, generic security advice, and throat-clearing.

**Evidence:** No repository evidence supports the promotional characterizations or organization-wide security recommendation.

**Disposition:** remove

**Loss if absent:** None; the title already establishes the guide’s purpose.

### 3

**Passage:** “Relay accepts connections through gateways.”

**Reader problem:** Attempts to provide architectural context.

**Actual effect:** Introduces an architectural assertion that is unnecessary for rotation and unsupported by the supplied evidence.

**Evidence:** The evidence discusses new and existing connections but does not establish that Relay accepts them through gateways.

**Disposition:** remove

**Loss if absent:** None for completing or verifying credential rotation.

### 4

**Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Explains staging, activation, connection behavior, and the rollback window.

**Actual effect:** Supplies the minimum lifecycle model needed to predict the operation’s effect and plan verification or recovery.

**Evidence:** Every behavior is explicitly established by the supplied repository evidence.

**Disposition:** keep

**Loss if absent:** The operator could misunderstand when the replacement takes effect, how existing connections behave, or when rollback remains possible.

### 5

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Prevents an unauthorized or poorly scheduled production change.

**Actual effect:** Provides useful safety prerequisites, but combines general organizational guidance with a product-specific reconnection constraint.

**Evidence:** Existing connections retaining the previous credential until reconnection supports planning for reconnecting clients. Authorization is reasonable general guidance, but no repository evidence establishes the organization’s approval policy.

**Disposition:** compress

**Loss if absent:** The operator could begin without appropriate authority or enough time to verify a reconnected client. Retain both prerequisites tersely and identify authorization as organizational policy rather than Relay behavior.

### 6

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Tells the operator how to store the replacement without activating it.

**Actual effect:** Enables the first operational step.

**Evidence:** The supplied evidence establishes that this command stages a replacement without activating it.

**Disposition:** keep

**Loss if absent:** The operator cannot begin the documented rotation workflow.

### 7

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Attempts to acknowledge additional CLI flexibility.

**Actual effect:** Interrupts the procedure with vague, unsupported information and provides no actionable option.

**Evidence:** The evidence establishes only that complete command options are documented in `docs/reference/credentials.md`.

**Disposition:** remove

**Loss if absent:** None; the reference link provides the useful navigation.

### 8

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Prevents activation of the wrong or expired pending credential.

**Actual effect:** Pairs the inspection command with the exact verification the operator must perform.

**Evidence:** The supplied evidence states that the command prints the pending credential fingerprint and expiry.

**Disposition:** keep

**Loss if absent:** The operator loses the pre-activation verification step and could activate an unintended credential.

### 9

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activates the staged credential and verifies production authentication safely.

**Actual effect:** Gives the activation command, expected result, and a bounded verification action.

**Evidence:** The supplied evidence establishes that activation affects new connections and that existing connections retain the prior credential until reconnection. Controlled-client verification is operational guidance consistent with that behavior.

**Disposition:** keep

**Loss if absent:** The operator could neither complete activation nor verify that a new connection authenticates with the replacement.

### 10

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recovers from failed authentication after activation.

**Actual effect:** Supplies the time-bounded rollback condition, command, expected effect, and post-rollback verification.

**Evidence:** The supplied evidence establishes a 30-minute retention window and that rollback restores the previous credential for new connections.

**Disposition:** keep

**Loss if absent:** The operator loses the documented recovery path and its verification step.

### 11

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Attempts to promote continuing security governance.

**Actual effect:** Adds generic advice after the recovery procedure without helping the operator complete, verify, or recover this rotation.

**Evidence:** No supplied repository evidence supports these governance recommendations.

**Disposition:** remove

**Loss if absent:** None for the primary reader’s task.

### 12

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Attempts to explain basic authentication and security concepts.

**Actual effect:** States generic definitions that do not improve the operator’s decisions or execution.

**Evidence:** The evidence identifies `docs/concepts/authentication.md` as the authoritative architectural explanation; it does not support these simplified claims.

**Disposition:** remove

**Loss if absent:** None; operators needing the architecture retain a direct link to it.

### 13

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Attempts to preview reference-level command options.

**Actual effect:** Duplicates reference scope and asserts a specific option inventory that the supplied evidence does not verify.

**Evidence:** The evidence confirms only that complete command options live in `docs/reference/credentials.md`.

**Disposition:** remove

**Loss if absent:** None; the following reference link remains authoritative.

### 14

**Passage:** “See `docs/reference/credentials.md` for every command option.”

**Reader problem:** Routes operators who need environment-specific command details to the authoritative reference.

**Actual effect:** Keeps exhaustive CLI detail out of the primary procedure while preserving discoverability.

**Evidence:** The supplied evidence identifies this exact file as the complete command-option reference.

**Disposition:** keep

**Loss if absent:** Operators needing flags or configuration options would lose the documented navigation path.

### 15

**Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Routes readers who need a deeper system model to the conceptual documentation.

**Actual effect:** Preserves optional architectural context without interrupting the operational journey.

**Evidence:** The supplied evidence identifies this exact file as the authentication architecture document.

**Disposition:** keep

**Loss if absent:** Readers needing deeper authentication context would lose the documented navigation path.

### Attainable reduction

Removing findings 2, 3, 7, 11, 12, and 13, then tightening finding 5, should approach the requested reduction without sacrificing a required command, observable result, safety prerequisite, recovery step, or reference path. A strict 50% cut should not be achieved by deleting the lifecycle model or verification and rollback instructions; “experienced operators can infer the rest” is unsafe for the stated first-time operator audience.
