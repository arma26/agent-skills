### Title

**Passage:** “# Rotate a Relay credential”

**Reader problem:** Identifies the production task.

**Actual effect:** Provides immediate orientation without distraction.

**Disposition:** keep.

**Loss if absent:** The operator loses the guide’s scope and goal.

### Opening paragraph

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Attempts to establish context and importance.

**Actual effect:** Delays the procedure with marketing, generic advice, and a repetition of the title. The repository evidence does not support the product characterization.

**Disposition:** remove.

**Loss if absent:** Nothing needed to rotate or verify the credential.

### System model

**Passage:** “Relay accepts connections through gateways. A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Explains staging, activation scope, connection behavior, and rollback limits.

**Actual effect:** Supplies the essential mental model, but later procedural paragraphs repeat most of it. Compress it to the staging boundary, existing-connection behavior, and 30-minute rollback window; let the steps describe their immediate results.

**Disposition:** compress.

**Loss if absent:** The operator cannot predict which connections use which credential or how long rollback remains possible.

### Prerequisites

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Prevents an unauthorized or operationally disruptive production change.

**Actual effect:** Establishes necessary safety conditions. Authorization is general operational guidance rather than evidenced product enforcement; keep that distinction while tightening the sentence.

**Disposition:** compress.

**Loss if absent:** The operator may rotate without authority or sufficient time to verify reconnecting clients.

### Staging command

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Stores the replacement without activating it.

**Actual effect:** Enables the first required operation directly and matches repository evidence.

**Disposition:** keep.

**Loss if absent:** The operator lacks the command needed to stage the replacement.

### Command-suite aside

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Attempts to acknowledge configuration flexibility.

**Actual effect:** Interrupts the procedure without enabling a decision. The supplied evidence establishes only that complete options live in the credential reference.

**Disposition:** remove.

**Loss if absent:** Nothing; the reference link preserves discovery of command options.

### Pending-credential verification

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Prevents activation of the wrong or unsuitable credential.

**Actual effect:** Provides the evidenced inspection command and a concrete pre-activation verification.

**Disposition:** keep.

**Loss if absent:** The operator cannot verify the pending credential before production activation.

### Activation and controlled verification

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activates the replacement and verifies it safely.

**Actual effect:** Contains the required command, result, and verification, but repeats behavior already established by the system model. Compress the repeated result while retaining activation and controlled reconnection.

**Disposition:** compress.

**Loss if absent:** The operator loses both the activation step and evidence that the replacement works for a new connection.

### Rollback and recovery verification

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recovers from failed post-activation authentication.

**Actual effect:** Provides the evidenced rollback action, expected result, and recovery verification. It can be tightened without removing any of those elements.

**Disposition:** compress.

**Loss if absent:** The operator loses the documented recovery path and confirmation that rollback restored authentication.

### Security aphorisms

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Attempts to encourage broader security governance.

**Actual effect:** Adds generic advice without helping the operator complete, verify, or recover this rotation.

**Disposition:** remove.

**Loss if absent:** Nothing relevant to the primary task.

### Authentication definitions

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Attempts to explain authentication to a novice.

**Actual effect:** States generic background that is too shallow to improve the operator’s system model and duplicates the linked architecture topic.

**Disposition:** remove.

**Loss if absent:** Nothing needed for rotation; deeper understanding remains discoverable through the authentication architecture link.

### Unsupported option inventory

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Attempts to summarize available command customization.

**Actual effect:** Adds reference detail and claims specific option categories not established by the supplied evidence. Direct readers to the authoritative reference instead.

**Disposition:** remove.

**Loss if absent:** Nothing; the following reference link covers complete command options.

### Command reference link

**Passage:** “See `docs/reference/credentials.md` for every command option.”

**Reader problem:** Routes operators who need complete CLI details to the authoritative source.

**Actual effect:** Preserves useful navigation without burdening the operational flow.

**Disposition:** keep.

**Loss if absent:** Operators lose the documented path to complete command options.

### Authentication architecture link

**Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Supports deeper conceptual inquiry beyond the immediate rotation.

**Actual effect:** Useful secondary navigation, but not part of the primary procedure. Place it in a compact related-documentation section after the recovery step.

**Disposition:** relocate.

**Loss if absent:** Readers lose the discovery path to the broader authentication model.
