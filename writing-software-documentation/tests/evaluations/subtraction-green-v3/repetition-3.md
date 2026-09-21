### Finding 1

- **Passage:** “# Rotate a Relay credential”
- **Reader problem:** Identifies the production operation covered by the guide.
- **Actual effect:** Provides immediate orientation without distraction.
- **Evidence:** The supplied repository evidence documents the credential rotation sequence.
- **Disposition:** keep
- **Loss if absent:** The guide’s purpose would be less scannable.
- **Correction direction:** Retain unchanged.

### Finding 2

- **Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams.”
- **Reader problem:** Attempts to introduce Relay.
- **Actual effect:** Delays the procedure with unsupported marketing language.
- **Evidence:** No supplied repository evidence supports these characterizations.
- **Disposition:** remove
- **Loss if absent:** Nothing needed for rotation is lost.
- **Correction direction:** Delete the sentence.

### Finding 3

- **Passage:** “Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”
- **Reader problem:** Attempts to justify and introduce the guide.
- **Actual effect:** Repeats the title and adds generic security advice without enabling an operator decision.
- **Evidence:** The evidence defines Relay’s rotation behavior, not organizational security maturity.
- **Disposition:** remove
- **Loss if absent:** Nothing needed to perform or verify the operation is lost.
- **Correction direction:** Delete both sentences.

### Finding 4

- **Passage:** “Relay accepts connections through gateways.”
- **Reader problem:** Attempts to explain where authentication occurs.
- **Actual effect:** Introduces an architectural detail that does not affect this procedure.
- **Evidence:** The supplied evidence does not establish gateway behavior.
- **Disposition:** remove
- **Loss if absent:** No rotation capability, safety property, or necessary understanding disappears.
- **Correction direction:** Delete the sentence.

### Finding 5

- **Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”
- **Reader problem:** Explains the lifecycle and rollback boundary an operator must understand before activation.
- **Actual effect:** Supplies the necessary system model, but repeats effects later beside the corresponding commands.
- **Evidence:** Every behavior is explicitly established by the supplied repository evidence.
- **Disposition:** compress
- **Loss if absent:** The operator could misunderstand staging, existing-connection behavior, or the 30-minute rollback limit.
- **Correction direction:** Retain one concise pre-procedure model; avoid repeating the same activation and rollback effects in full later.

### Finding 6

- **Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”
- **Reader problem:** Prevents an unauthorized or inadequately coordinated production change.
- **Actual effect:** Provides useful safety guidance, although the authorization and maintenance-window requirements are not documented product behavior.
- **Evidence:** Existing connections retain the old credential until reconnection, but the supplied evidence defines neither authorization policy nor a required maintenance window.
- **Disposition:** compress
- **Loss if absent:** The operator loses an important prompt to coordinate authority and client reconnection.
- **Correction direction:** Retain this as concise, explicitly general operational guidance rather than implying Relay enforces these prerequisites.

### Finding 7

- **Passage:** “Stage the replacement with `relay credential stage`.”
- **Reader problem:** Stores the replacement without exposing new connections to it.
- **Actual effect:** Enables the first safe operation in the rotation sequence.
- **Evidence:** The supplied evidence states that this command stores a replacement without activating it.
- **Disposition:** keep
- **Loss if absent:** The operator cannot begin the documented rotation safely.
- **Correction direction:** Retain unchanged.

### Finding 8

- **Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”
- **Reader problem:** Attempts to acknowledge command flexibility.
- **Actual effect:** Adds vague, unsupported detail between staging and verification.
- **Evidence:** The evidence establishes only that complete command options live in `docs/reference/credentials.md`.
- **Disposition:** remove
- **Loss if absent:** Nothing actionable or necessary disappears.
- **Correction direction:** Delete the sentence; the reference link already routes option questions appropriately.

### Finding 9

- **Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”
- **Reader problem:** Prevents activation of the wrong or unsuitable pending credential.
- **Actual effect:** Pairs inspection with a concrete verification criterion.
- **Evidence:** The supplied evidence states that the command prints the pending fingerprint and expiry.
- **Disposition:** keep
- **Loss if absent:** The operator loses the only documented pre-activation verification step.
- **Correction direction:** Retain unchanged.

### Finding 10

- **Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”
- **Reader problem:** Activates the replacement and verifies that production authentication succeeds.
- **Actual effect:** Provides the primary state-changing operation and its essential post-change check, while partly repeating the earlier system model.
- **Evidence:** Activation for new connections and continued use of the old credential by existing connections are established. Controlled-client verification is sensible operational guidance but is not stated as Relay-enforced behavior.
- **Disposition:** compress
- **Loss if absent:** The operator cannot complete or verify rotation.
- **Correction direction:** Keep the activation command and controlled reconnection check; state the new-connection effect only once in the guide and present the check as operator guidance.

### Finding 11

- **Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”
- **Reader problem:** Recovers from failed authentication after activation.
- **Actual effect:** Provides a bounded recovery action and verification, with some duplication of the earlier lifecycle explanation.
- **Evidence:** The supplied evidence establishes the 30-minute retention window and rollback behavior for new connections. Rechecking a controlled client is operational guidance.
- **Disposition:** compress
- **Loss if absent:** The operator loses the documented recovery path and its time boundary.
- **Correction direction:** Preserve the failure condition, rollback command, 30-minute limit, and verification; remove duplicated explanatory wording.

### Finding 12

- **Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”
- **Reader problem:** Attempts to provide broader security-process advice.
- **Actual effect:** Interrupts the recovery-to-reference path with generic, non-actionable prose.
- **Evidence:** None of these claims is grounded in the supplied repository evidence.
- **Disposition:** remove
- **Loss if absent:** No capability, decision, safety property, or product understanding disappears.
- **Correction direction:** Delete the paragraph.

### Finding 13

- **Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”
- **Reader problem:** Attempts to explain elementary authentication concepts.
- **Actual effect:** States generic background that the operator does not need to execute this procedure.
- **Evidence:** Only Relay’s credential behavior and the location of the authentication architecture are supplied.
- **Disposition:** remove
- **Loss if absent:** No procedure-specific understanding disappears; deeper architecture remains discoverable through its link.
- **Correction direction:** Delete the paragraph.

### Finding 14

- **Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”
- **Reader problem:** Attempts to summarize available command options.
- **Actual effect:** Duplicates reference-level detail and asserts a specific option list not established by the supplied evidence.
- **Evidence:** The evidence says only that complete options live in `docs/reference/credentials.md`.
- **Disposition:** remove
- **Loss if absent:** No option discovery is lost because the authoritative reference remains linked.
- **Correction direction:** Delete the sentence.

### Finding 15

- **Passage:** “See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.”
- **Reader problem:** Routes option and architecture questions outside the primary operational journey.
- **Actual effect:** Preserves useful navigation without embedding exhaustive reference or conceptual material.
- **Evidence:** Both destinations and their stated purposes are explicitly established by the supplied evidence.
- **Disposition:** keep
- **Loss if absent:** Operators lose the authoritative paths for complete options and deeper authentication concepts.
- **Correction direction:** Retain both repository-relative links.

### Finding 16

- **Passage:** “The maintainer wants it cut by at least half”
- **Reader problem:** Establishes a release-driven reduction target.
- **Actual effect:** Risks treating word count as more important than the system model, verification, and rollback guidance required for a first production rotation.
- **Evidence:** The review rubric explicitly forbids imposing a percentage target during adversarial subtraction.
- **Disposition:** remove
- **Loss if absent:** No reader capability is lost.
- **Correction direction:** Remove all identified unsupported and generic material, then compress duplicated behavior. Accept only the reduction achievable without deleting prerequisites, verification, recovery, references, or the minimum lifecycle model.
