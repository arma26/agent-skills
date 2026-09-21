### Finding 1

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Orient the operator to the task.

**Actual effect:** Delays the procedure with promotional, generic, and self-descriptive prose. None of it helps execute or verify the rotation.

**Disposition:** remove

**Loss if absent:** Nothing identifiable; the title already establishes the task.

### Finding 2

**Passage:** “Relay accepts connections through gateways.”

**Reader problem:** Explain where authentication occurs.

**Actual effect:** Introduces an unsupported architectural claim that is unnecessary for rotation.

**Disposition:** remove

**Loss if absent:** Nothing needed to rotate the credential safely.

### Finding 3

**Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Provide the lifecycle model needed to predict activation and rollback behavior.

**Actual effect:** Enables safe timing, reconnection, and rollback decisions, but repeats details also stated in the activation and rollback steps. State the model once compactly, then avoid repeating it below.

**Disposition:** compress

**Loss if absent:** The operator could incorrectly expect activation or rollback to change existing connections and could miss the 30-minute recovery boundary.

### Finding 4

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Establish production authority and timing prerequisites.

**Actual effect:** Prevents an unauthorized change and accounts for the documented requirement that existing connections must reconnect before using the replacement.

**Disposition:** keep

**Loss if absent:** The authorization check and reconnect-aware maintenance planning would disappear.

### Finding 5

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Store the replacement without activating it.

**Actual effect:** Starts the safe staged workflow defined by repository evidence.

**Disposition:** keep

**Loss if absent:** The operator would lack the first required action.

### Finding 6

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Signal that additional CLI options exist.

**Actual effect:** Adds vague reference-level commentary without helping the primary operation; the later reference link already provides navigation.

**Disposition:** remove

**Loss if absent:** Nothing; option discovery remains available through the credential reference.

### Finding 7

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Verify that the intended credential was staged before making it active.

**Actual effect:** Supplies both the verification command and the evidence the operator must compare.

**Disposition:** keep

**Loss if absent:** The operator could activate the wrong or unsuitable pending credential without verification.

### Finding 8

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activate the credential and verify production authentication safely.

**Actual effect:** Provides the activation action, immediate result, and controlled verification. The new-connection behavior duplicates the earlier lifecycle explanation and can be stated only once.

**Disposition:** compress

**Loss if absent:** The operator would lose the activation command and the controlled post-activation authentication check.

### Finding 9

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recover from failed authentication while the previous credential remains available.

**Actual effect:** Gives a condition, recovery command, expected result, and verification. “During the retention window” should remain explicitly tied to the documented 30-minute limit.

**Disposition:** keep

**Loss if absent:** The operator would lose the documented recovery path and its verification step.

### Finding 10

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Encourage broader security governance.

**Actual effect:** Distracts from the time-sensitive operational sequence with generic advice that establishes no product behavior or concrete decision.

**Disposition:** remove

**Loss if absent:** Nothing required for this rotation task.

### Finding 11

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Explain elementary authentication concepts.

**Actual effect:** Adds generic background without supplying the specific authentication model needed for rotation. Deeper architecture is already linked.

**Disposition:** remove

**Loss if absent:** Nothing needed by the stated operator; authentication architecture remains discoverable through the concept link.

### Finding 12

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Advertise advanced command options.

**Actual effect:** Interrupts completion with an incomplete option inventory and duplicates the authoritative reference’s purpose.

**Disposition:** remove

**Loss if absent:** No operational capability; the complete option reference remains linked.

### Finding 13

**Passage:** “See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Route operators to exhaustive CLI details and deeper architecture without embedding them in the procedure.

**Actual effect:** Preserves useful navigation while keeping reference and conceptual detail outside the primary journey.

**Disposition:** keep

**Loss if absent:** Operators would lose the documented paths to complete command options and the authentication model.
