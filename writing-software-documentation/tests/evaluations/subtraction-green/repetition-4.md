### 1. Unsupported maintenance-window prerequisite

- **Passage:** “and have a maintenance window that accounts for reconnecting clients.”
- **Reader problem:** Prepare for the effect on existing connections.
- **Actual effect:** Introduces an operational requirement the evidence does not establish.
- **Evidence:** The scenario confirms existing connections retain the previous credential until reconnecting, but provides no maintenance-window requirement.
- **Disposition:** remove; rely on the later controlled-client reconnection and verification instructions.
- **Loss if absent:** No evidence-backed capability or safety property is lost.

### 2. Unsupported command-option inventory

- **Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”
- **Reader problem:** Discover advanced command configuration.
- **Actual effect:** Adds an unverified option list and distracts from the first rotation.
- **Evidence:** The scenario establishes only that complete command options live in `docs/reference/credentials.md`; it does not verify these individual option categories.
- **Disposition:** remove; retain the reference link.
- **Loss if absent:** None; option discovery remains available through the reference.

### 3. Unsupported gateway detail

- **Passage:** “Relay accepts connections through gateways.”
- **Reader problem:** Understand where authentication occurs.
- **Actual effect:** Adds architecture detail that does not help complete the rotation and is not established by the supplied evidence.
- **Evidence:** The scenario describes connection behavior but does not mention gateways.
- **Disposition:** remove.
- **Loss if absent:** No operational capability or necessary system understanding is lost.

### 4. Production authorization safeguard

- **Passage:** “Before starting, ensure you are authorized to rotate the production credential”
- **Reader problem:** Prevent an operator from changing a production credential without organizational authority.
- **Actual effect:** Supplies a concise, consequence-proportional safety check.
- **Evidence:** This is general operational guidance rather than established Relay behavior; the scenario identifies the target as a production credential.
- **Disposition:** keep, but present it explicitly as an organizational prerequisite rather than product behavior.
- **Loss if absent:** The guide loses its only explicit authority check before a production change.

### 5. Essential connection and rollback model

- **Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”
- **Reader problem:** Predict which credential each connection will use and when rollback remains possible.
- **Actual effect:** Provides the necessary mental model, but repeats effects later beside the activation and rollback commands.
- **Evidence:** Every clause is directly supported by the scenario’s staging, activation, existing-connection, retention, and rollback evidence.
- **Disposition:** compress; retain the staged-versus-active distinction, existing-connection behavior, and 30-minute rollback window once in a concise pre-operation model.
- **Loss if absent:** Operators could activate without understanding connection scope or the rollback deadline.

### 6. Staging operation

- **Passage:** “Stage the replacement with `relay credential stage`.”
- **Reader problem:** Store the replacement without activating it.
- **Actual effect:** Enables the first operation in the rotation.
- **Evidence:** The scenario states that `relay credential stage` stores a replacement credential without activating it.
- **Disposition:** keep.
- **Loss if absent:** The operator cannot begin the documented rotation safely.

### 7. Pending-credential verification

- **Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”
- **Reader problem:** Detect a mistaken pending credential before it affects new connections.
- **Actual effect:** Pairs inspection with an explicit expected result and decision gate.
- **Evidence:** The scenario states that the command prints the pending credential fingerprint and expiry.
- **Disposition:** keep.
- **Loss if absent:** The operator loses the pre-activation verification step.

### 8. Activation and controlled validation

- **Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”
- **Reader problem:** Activate the pending credential and verify it works on a new connection.
- **Actual effect:** Enables the state change and supplies an observable validation.
- **Evidence:** The scenario confirms activation affects new connections and existing connections retain the old credential until reconnecting. Controlled-client verification is proportional general operational guidance.
- **Disposition:** keep, but remove the unsupported “before ending the maintenance window” wording.
- **Loss if absent:** The operator cannot activate or verify the replacement credential.

### 9. Rollback and recovery verification

- **Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”
- **Reader problem:** Recover when the activated credential fails validation.
- **Actual effect:** Supplies a bounded rollback trigger, expected result, and recovery verification.
- **Evidence:** The scenario confirms a 30-minute retention window and that rollback restores the previous credential for new connections.
- **Disposition:** keep.
- **Loss if absent:** The guide loses its only documented recovery path.

### 10. Credential reference navigation

- **Passage:** “See `docs/reference/credentials.md` for every command option.”
- **Reader problem:** Find exhaustive command syntax without burdening the operational guide.
- **Actual effect:** Routes advanced questions to the authoritative reference.
- **Evidence:** The scenario identifies this file as the location of complete command options.
- **Disposition:** keep.
- **Loss if absent:** Operators lose the discovery path for required environment-specific options.

### 11. Authentication architecture navigation

- **Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”
- **Reader problem:** Investigate the deeper authentication model when needed.
- **Actual effect:** Provides optional conceptual navigation at the end without interrupting the rotation.
- **Evidence:** The scenario identifies this file as the authentication architecture source.
- **Disposition:** keep.
- **Loss if absent:** Readers lose the verified route to deeper architectural context.

### 12. Marketing introduction

- **Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”
- **Reader problem:** Orient the reader to the guide.
- **Actual effect:** Delays the operation with marketing, generic security advice, and a restatement of the title.
- **Evidence:** No scenario evidence supports the marketing characterization; the title and stated audience already establish the task.
- **Disposition:** remove.
- **Loss if absent:** None.

### 13. Generic command commentary

- **Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”
- **Reader problem:** Signal that advanced configuration exists.
- **Actual effect:** Adds vague commentary without enabling a decision or action.
- **Evidence:** The scenario supports linking to the complete command reference, not this generic characterization.
- **Disposition:** remove.
- **Loss if absent:** None; the retained reference link preserves discovery.

### 14. Motivational security commentary

- **Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”
- **Reader problem:** Encourage broader security-program reflection.
- **Actual effect:** Interrupts recovery guidance with generic, non-actionable advice for a secondary organizational concern.
- **Evidence:** The scenario provides no repository-specific support for these statements.
- **Disposition:** remove.
- **Loss if absent:** No capability, decision, safety property, or useful navigation disappears.

### 15. Generic authentication explanation

- **Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”
- **Reader problem:** Explain basic authentication terminology.
- **Actual effect:** Repeats elementary background without improving the operator’s ability to rotate or recover.
- **Evidence:** The scenario provides a dedicated authentication architecture link but does not establish a need for this generic explanation.
- **Disposition:** remove.
- **Loss if absent:** None; deeper explanation remains discoverable through the concept link.

### Reduction finding

Removing findings 1, 2, 3, 12, 13, 14, and 15, then compressing finding 5 and trimming finding 8, can meet the requested reduction of at least half while preserving the complete first-rotation path: stage, inspect, activate, verify, rollback, and verify recovery.
