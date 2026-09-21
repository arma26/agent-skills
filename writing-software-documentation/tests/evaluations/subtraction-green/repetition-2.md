### Finding 1

**Passage:** “Relay accepts connections through gateways.”

**Reader problem:** Establish where credential behavior applies.

**Actual effect:** Introduces an unsupported architectural claim without helping the rotation task.

**Evidence:** The supplied repository evidence describes connection behavior but does not mention gateways.

**Disposition:** remove

**Loss if absent:** None.

**Correction direction:** Delete the sentence.

### Finding 2

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Signal that additional command options exist.

**Actual effect:** Adds an unverified option inventory and delays the authoritative reference.

**Evidence:** The evidence establishes only that complete command options live in `docs/reference/credentials.md`; it does not establish these option categories.

**Disposition:** remove

**Loss if absent:** None; the reference link provides authoritative discovery.

**Correction direction:** Delete the inventory and retain the reference link.

### Finding 3

**Passage:** “See `docs/reference/credentials.md` for every command option.”

**Reader problem:** Find the syntax and options needed to supply and manage the replacement credential.

**Actual effect:** Enables task completion, but appears only after every command has already been presented.

**Evidence:** The repository evidence identifies this page as the complete command-option reference.

**Disposition:** relocate

**Loss if absent:** Operators lose the documented route to complete command syntax.

**Correction direction:** Place the link immediately before the staging step or beside the first command.

### Finding 4

**Passage:** “# Rotate a Relay credential”

**Reader problem:** Identify the guide’s operational goal.

**Actual effect:** Provides a direct, scannable task heading.

**Evidence:** The documented commands and lifecycle all concern credential rotation.

**Disposition:** keep

**Loss if absent:** The page loses its immediate task identity.

**Correction direction:** Retain unchanged.

### Finding 5

**Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Understand activation scope, connection lifecycle, and the rollback window before changing production state.

**Actual effect:** Supplies the minimum system model needed to predict rotation behavior and avoid ending the maintenance window prematurely.

**Evidence:** Every clause is directly established by the supplied repository evidence.

**Disposition:** keep

**Loss if absent:** Operators cannot predict which credential new and existing connections use or when rollback remains available.

**Correction direction:** Retain as the conceptual introduction.

### Finding 6

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Avoid an unauthorized production change and reserve time to verify reconnection behavior.

**Actual effect:** Establishes concise safety prerequisites before state-changing commands.

**Evidence:** Authorization and maintenance-window selection are general operational guidance; the need to account for reconnection follows from the evidenced behavior that existing connections retain the previous credential until reconnecting.

**Disposition:** keep

**Loss if absent:** The guide loses its authorization warning and preparation for connection-specific activation behavior.

**Correction direction:** Retain, while treating authorization and scheduling as general operational guidance rather than product-enforced behavior.

### Finding 7

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Store the replacement without activating it.

**Actual effect:** Starts the safe rotation sequence with a reversible, non-activating operation.

**Evidence:** The repository evidence states that this command stores a replacement credential without activating it.

**Disposition:** keep

**Loss if absent:** The operator loses the first required rotation action.

**Correction direction:** Retain after moving the command-reference link nearby.

### Finding 8

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Indicate that broader CLI functionality exists.

**Actual effect:** Adds vague, non-actionable promotion between the staging and inspection steps.

**Evidence:** No supplied evidence establishes this characterization; authoritative command details already have a reference destination.

**Disposition:** remove

**Loss if absent:** None.

**Correction direction:** Delete the sentence.

### Finding 9

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Prevent activation of the wrong or unexpectedly expiring credential.

**Actual effect:** Pairs the inspection command with the exact fields the operator must verify.

**Evidence:** The repository evidence states that the command prints the pending credential fingerprint and expiry.

**Disposition:** keep

**Loss if absent:** The operator loses the pre-activation verification gate.

**Correction direction:** Retain unchanged.

### Finding 10

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activate the pending credential and verify production authentication safely.

**Actual effect:** Gives the state-changing command, expected result, and controlled verification.

**Evidence:** The evidence establishes that activation makes the pending credential active for new connections while existing connections retain the previous credential until reconnecting. Controlled-client verification is proportional general operational guidance.

**Disposition:** keep

**Loss if absent:** The operator loses activation, its expected effect, or the first-success check.

**Correction direction:** Retain unchanged.

### Finding 11

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recover from failed authentication after activation.

**Actual effect:** Provides a time-bounded recovery command, expected state, and post-recovery verification.

**Evidence:** The repository evidence states that the previous credential is retained for 30 minutes and that rollback restores it for new connections.

**Disposition:** keep

**Loss if absent:** The operator loses the documented recovery path and verification step.

**Correction direction:** Retain unchanged.

### Finding 12

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Orient the reader to the product and topic.

**Actual effect:** Delays the operational model with promotional language, generic security advice, and a restatement of the heading.

**Evidence:** The evidence does not support the promotional characterization, and none of these sentences adds product behavior needed for rotation.

**Disposition:** remove

**Loss if absent:** None.

**Correction direction:** Delete the paragraph and begin with the system model.

### Finding 13

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Encourage broader security governance.

**Actual effect:** Interrupts the recovery-to-reference path with generic advice that supplies no concrete decision or action.

**Evidence:** No supplied repository evidence supports product-specific guidance in this paragraph.

**Disposition:** remove

**Loss if absent:** None for the first-time rotation task.

**Correction direction:** Delete the paragraph.

### Finding 14

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Explain authentication at a basic level.

**Actual effect:** Repeats obvious background without clarifying Relay’s credential lifecycle or enabling an operation.

**Evidence:** Only the first sentence is broadly consistent with the authentication context; the paragraph adds no evidenced behavior beyond the operational model and linked architecture page.

**Disposition:** remove

**Loss if absent:** None for the stated reader and goal.

**Correction direction:** Delete the paragraph and preserve navigation to the authentication concept page.

### Finding 15

**Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Support deeper investigation of Relay’s authentication design.

**Actual effect:** Provides useful secondary navigation, but it is not part of the first rotation journey.

**Evidence:** The repository evidence identifies this page as the authentication architecture source.

**Disposition:** relocate

**Loss if absent:** Readers lose the discovery path to the authoritative conceptual explanation.

**Correction direction:** Preserve it in a short “Related” section after the operational procedure.

The removals eliminate slightly more than half of the guide’s prose while preserving the system model, prerequisites, complete operation sequence, verification, rollback, and authoritative navigation.
