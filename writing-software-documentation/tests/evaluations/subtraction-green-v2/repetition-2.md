### 1. Opening paragraph

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Orient the operator to the guide.

**Actual effect:** Delays the procedure without adding product behavior, safety information, or operational context.

**Disposition:** remove.

**Loss if absent:** Nothing identifiable; the heading already states the guide’s purpose.

### 2. Gateway claim

**Passage:** “Relay accepts connections through gateways.”

**Reader problem:** Explain where authentication occurs.

**Actual effect:** Introduces an architectural claim absent from the repository evidence and unnecessary for rotation.

**Disposition:** remove.

**Loss if absent:** Nothing required to rotate or verify the credential.

### 3. Credential lifecycle model

**Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Help a first-time operator predict staging, activation, reconnection, and rollback behavior.

**Actual effect:** Supplies the essential system model, but repeats outcomes later in the procedure.

**Disposition:** compress. Retain all four facts—staging is inactive, activation affects new connections, existing connections retain the old credential until reconnection, and rollback remains available for 30 minutes—while removing duplicated phrasing from either this overview or the steps.

**Loss if absent:** The operator could misunderstand activation scope, omit reconnection testing, or miss the rollback deadline.

### 4. Production prerequisites

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Prevent an unauthorized or poorly scheduled production change.

**Actual effect:** Establishes proportional safeguards for a state-changing production operation and accounts for the documented reconnection behavior.

**Disposition:** keep.

**Loss if absent:** The guide would omit authorization and scheduling prerequisites needed for safe execution.

### 5. Stage operation

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Store the replacement without activating it.

**Actual effect:** Provides the first required operation directly and matches repository evidence.

**Disposition:** keep.

**Loss if absent:** The operator cannot begin the rotation workflow.

### 6. Generic command commentary

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Signal that additional command options exist.

**Actual effect:** Adds vague reference-level commentary without helping the operator complete this rotation.

**Disposition:** remove.

**Loss if absent:** Nothing; the credentials reference link supplies the useful navigation.

### 7. Pending-credential inspection

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Verify that the correct credential was staged before changing production authentication.

**Actual effect:** Pairs the supported inspection command with its observable output and a safety decision.

**Disposition:** keep.

**Loss if absent:** The operator loses the pre-activation verification gate and could activate the wrong or unsuitable credential.

### 8. Activation and controlled verification

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activate the credential and verify new authentication safely.

**Actual effect:** Provides the state-changing command, expected result, and an end-to-end verification, though the new-connection behavior duplicates the lifecycle overview.

**Disposition:** compress. Preserve the command and controlled-client verification; state the new-connection result only once in the guide.

**Loss if absent:** The operator would lack either the activation action or evidence that the replacement works before ending maintenance.

### 9. Rollback and recovery verification

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recover from failed authentication after activation.

**Actual effect:** Supplies the documented rollback condition, command, result, and verification; some lifecycle wording duplicates the overview.

**Disposition:** compress. Preserve the 30-minute constraint through the lifecycle model, plus the rollback command and post-rollback reconnection check.

**Loss if absent:** The operator loses the supported recovery path and the means to verify recovery.

### 10. Aspirational security paragraph

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Encourage broader security governance.

**Actual effect:** Interrupts the production procedure with generic advice and supplies no actionable, repository-backed requirement.

**Disposition:** remove.

**Loss if absent:** Nothing needed for this rotation task.

### 11. Generic authentication explanation

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Define authentication and justify security controls.

**Actual effect:** Repeats obvious background for the stated operator audience and does not explain Relay’s documented authentication architecture.

**Disposition:** remove.

**Loss if absent:** Nothing needed for execution; deeper conceptual context remains discoverable through the authentication link.

### 12. Reference navigation

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios. See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Route operators to complete command syntax and deeper architecture.

**Actual effect:** The two links provide useful navigation, but the enumerated flag categories are unsupported by the supplied evidence and unnecessary in the operational journey.

**Disposition:** compress. Remove the flag enumeration and retain concise links to `docs/reference/credentials.md` for options and `docs/concepts/authentication.md` for architecture.

**Loss if absent:** Removing the whole passage would eliminate navigation for advanced command use and conceptual questions; removing only the enumeration loses no established capability.
