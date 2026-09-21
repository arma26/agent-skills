### 1

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Orient the operator to the procedure.

**Actual effect:** Delays the procedure with promotional language, generic security advice, and a restatement of the title. Delete the paragraph.

**Disposition:** remove

**Loss if absent:** Nothing; the title and operational content already establish the subject.

### 2

**Passage:** “Relay accepts connections through gateways. A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Explain the credential lifecycle and which connections activation and rollback affect.

**Actual effect:** Provides the minimum system model needed to predict production behavior. Every behavioral claim is supported by the supplied repository evidence. Retain it.

**Disposition:** keep

**Loss if absent:** The operator could mistake staging for activation, expect existing connections to switch immediately, or miss the 30-minute rollback boundary.

### 3

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Prevent an unauthorized or operationally incomplete production change.

**Actual effect:** Establishes proportionate safety prerequisites. The need to accommodate reconnects follows from the documented behavior of existing connections. Retain it as operational guidance rather than product behavior.

**Disposition:** keep

**Loss if absent:** The operator loses the authorization check and may end the maintenance window before validating a reconnected client.

### 4

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Store the replacement without activating it.

**Actual effect:** Identifies the correct first operation, supported by repository evidence, but does not contain enough syntax to show how the credential is supplied. Retain the sentence and place the existing command-reference link immediately after it; do not invent missing options.

**Disposition:** keep

**Loss if absent:** The operator loses the required separation between storing and activating the replacement.

### 5

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Signal that additional command options exist.

**Actual effect:** Adds vague detail without helping the operator choose or execute anything. The command reference provides the useful navigation. Delete the sentence.

**Disposition:** remove

**Loss if absent:** Nothing identifiable.

### 6

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Verify that the intended credential was staged before changing production behavior.

**Actual effect:** Pairs an evidence-backed command with its observable output and a clear verification decision. Retain it.

**Disposition:** keep

**Loss if absent:** The operator could activate the wrong credential or one with an unintended expiry.

### 7

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activate the pending credential and verify production authentication safely.

**Actual effect:** States the supported connection behavior and supplies a bounded verification step. Retain it.

**Disposition:** keep

**Loss if absent:** The operator loses both the activation action and the test that determines whether the rotation succeeded.

### 8

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recover from failed authentication while the previous credential remains available.

**Actual effect:** Gives an evidence-backed recovery action, its scope, and post-recovery verification. Retain it.

**Disposition:** keep

**Loss if absent:** The operator loses the documented recovery path and may miss the 30-minute opportunity to restore service for new connections.

### 9

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Encourage broader security-program reflection.

**Actual effect:** Interrupts the production procedure with generic advice that enables no concrete decision or action. Delete the paragraph.

**Disposition:** remove

**Loss if absent:** Nothing needed for this rotation task.

### 10

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Explain basic authentication terminology.

**Actual effect:** Repeats concepts already implicit in the task at a level too generic for the stated operator. It neither explains Relay’s architecture nor changes the procedure. Delete the paragraph.

**Disposition:** remove

**Loss if absent:** Nothing needed to perform, verify, or recover the rotation.

### 11

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Summarize the scope of command options.

**Actual effect:** Duplicates reference-level categories without helping the primary journey and may become stale. Delete the enumeration and rely on the authoritative reference link.

**Disposition:** remove

**Loss if absent:** No operational capability; the linked reference remains the authoritative destination.

### 12

**Passage:** “See `docs/reference/credentials.md` for every command option.”

**Reader problem:** Let the operator obtain the invocation details omitted from the guide.

**Actual effect:** Provides necessary navigation, but appears after every operation instead of where the missing syntax first blocks progress. Move it directly after the staging instruction and preserve the repository-relative target.

**Disposition:** relocate

**Loss if absent:** The operator may be unable to construct the staging command without unsupported guesswork.

### 13

**Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Route readers with deeper architectural questions to authoritative conceptual material.

**Actual effect:** Supplies useful optional navigation without duplicating architecture in the operational journey. Retain it at the end.

**Disposition:** keep

**Loss if absent:** Readers lose the discovery path for understanding Relay’s broader authentication architecture.
