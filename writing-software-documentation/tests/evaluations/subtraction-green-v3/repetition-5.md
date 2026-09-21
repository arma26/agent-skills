## Findings

### 1. Opening paragraph

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams.”

**Reader problem:** None identifiable for credential rotation.

**Actual effect:** Delays the first actionable information and adds unsupported marketing language.

**Evidence:** Repository evidence establishes credential behavior only; it does not support these product characterizations.

**Disposition:** remove

**Loss if absent:** None.

### 2. Generic security introduction

**Passage:** “Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Attempts to justify and introduce the procedure.

**Actual effect:** Repeats the title and supplies generic advice without helping the operator rotate or verify the credential.

**Evidence:** No repository evidence supports an organizational rotation policy. The title already identifies the guide’s purpose.

**Disposition:** remove

**Loss if absent:** None.

### 3. Unsupported gateway detail

**Passage:** “Relay accepts connections through gateways.”

**Reader problem:** Attempts to provide an authentication system model.

**Actual effect:** Introduces an architectural claim that is unnecessary for the procedure and unsupported by the supplied evidence.

**Evidence:** The evidence describes connection behavior but does not establish that connections pass through gateways.

**Disposition:** remove

**Loss if absent:** None; deeper architecture remains discoverable through `docs/concepts/authentication.md`.

### 4. Rotation lifecycle

**Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** The operator must understand which connections change, when they change, and how long rollback remains possible.

**Actual effect:** Supplies the essential lifecycle model, but uses more words than necessary.

**Evidence:** Every behavioral clause is directly supported by the supplied staging, activation, existing-connection, retention, and rollback evidence.

**Disposition:** compress — retain all three facts in a shorter lifecycle summary.

**Loss if absent:** The operator could expect staging or activation to affect existing connections, or miss the 30-minute rollback boundary.

### 5. Production prerequisites

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Prevents an unauthorized change and insufficient time for controlled reconnection.

**Actual effect:** Provides proportionate operational safety, though its introductory phrasing can be tightened.

**Evidence:** Existing connections retain the previous credential until reconnection, supporting the maintenance-window requirement. Authorization is general production-safety guidance, not established product behavior, and should not be presented as a Relay-enforced requirement.

**Disposition:** compress — state authorization and sufficient reconnection time as concise operator prerequisites.

**Loss if absent:** The procedure would omit authority and scheduling checks before a production authentication change.

### 6. Staging operation

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** The operator needs to store the replacement without activating it.

**Actual effect:** Directly initiates the safe rotation sequence.

**Evidence:** The supplied evidence states that this command stores a replacement credential without activating it.

**Disposition:** keep

**Loss if absent:** The operator cannot begin the documented rotation procedure.

### 7. Generic command commentary

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Attempts to acknowledge additional CLI capabilities.

**Actual effect:** Interrupts the procedure without identifying a decision or capability needed for rotation.

**Evidence:** The evidence establishes only that complete command options live in `docs/reference/credentials.md`; it does not support these broader claims.

**Disposition:** remove

**Loss if absent:** None; the reference link preserves access to command options.

### 8. Pending-credential inspection

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** The operator must ensure the correct credential was staged before making it active.

**Actual effect:** Provides both the verification command and the acceptance criteria.

**Evidence:** The supplied evidence states that the command prints the pending credential fingerprint and expiry.

**Disposition:** keep

**Loss if absent:** The operator could activate an unintended or incorrectly expiring credential.

### 9. Activation operation and result

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement.”

**Reader problem:** The operator needs to activate the staged credential and know its immediate effect.

**Actual effect:** Pairs the state-changing command with its expected result.

**Evidence:** The supplied evidence states that activation makes the pending credential active for new connections.

**Disposition:** keep

**Loss if absent:** The operator would lack either the activation step or the expected post-activation state.

### 10. Post-activation verification

**Passage:** “Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** The operator must verify that a new connection can authenticate with the replacement.

**Actual effect:** Supplies a controlled verification step before the maintenance window closes.

**Evidence:** The evidence establishes that existing connections retain the previous credential until reconnection; reconnecting is therefore necessary to exercise the active replacement. Using a controlled client is proportionate general operational guidance.

**Disposition:** keep

**Loss if absent:** Activation would have no documented end-to-end verification.

### 11. Rollback trigger and command

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** The operator needs a bounded recovery action and a way to verify recovery.

**Actual effect:** Provides the rollback condition, command, expected result, and follow-up verification.

**Evidence:** The supplied evidence establishes a 30-minute retention window and states that rollback restores the previous credential for new connections.

**Disposition:** keep

**Loss if absent:** The guide would omit the only documented recovery path for a failed production rotation.

### 12. Motivational conclusion

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Attempts to encourage broader security governance.

**Actual effect:** Adds generic, unactionable advice after the complete recovery procedure.

**Evidence:** No supplied repository evidence establishes these organizational practices, and the passage does not support the primary rotation task.

**Disposition:** remove

**Loss if absent:** None.

### 13. Generic authentication explanation

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Attempts to explain elementary authentication concepts.

**Actual effect:** Adds generic background that neither predicts Relay’s rotation behavior nor changes an operator decision.

**Evidence:** The supplied evidence identifies `docs/concepts/authentication.md` as the authoritative architectural explanation. It does not support these broad statements as a useful Relay-specific model.

**Disposition:** remove

**Loss if absent:** None; the operational lifecycle remains explained and the architecture link remains available.

### 14. Unsupported option inventory

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Attempts to summarize the command reference.

**Actual effect:** Duplicates reference-level detail and asserts specific option categories not established by the supplied evidence.

**Evidence:** The evidence establishes only that complete command options live in `docs/reference/credentials.md`.

**Disposition:** remove

**Loss if absent:** None; the command-reference link supplies the authoritative detail.

### 15. Reference navigation

**Passage:** “See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Operators may need full CLI options or deeper architectural context beyond the primary procedure.

**Actual effect:** Preserves concise navigation to authoritative secondary material without interrupting the workflow.

**Evidence:** Both destinations and their stated purposes are explicitly established by the supplied repository evidence.

**Disposition:** keep

**Loss if absent:** Readers lose the discovery path to complete options and authentication architecture.

## Attainable reduction

Removing the unsupported and generic passages and compressing the lifecycle and prerequisites can cut approximately half the guide while preserving the commands, system model, verification, rollback boundary, and reference navigation. Cutting further on the premise that experienced operators can infer the rest would conflict with the stated first-time operator audience and would remove safety-critical behavior rather than mere prose.
