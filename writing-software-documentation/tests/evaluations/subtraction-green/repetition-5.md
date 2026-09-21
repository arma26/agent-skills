### 1. System model, first sentence

**Passage:** “Relay accepts connections through gateways.”

**Reader problem:** Establish where credential behavior applies.

**Actual effect:** Introduces an unsupported architecture detail that is unnecessary for completing the rotation. Delete the sentence.

**Evidence:** The repository evidence describes new and existing connections but does not establish that Relay accepts them through gateways.

**Disposition:** remove

**Loss if absent:** None; the remaining model explains the connection behavior needed for rotation.

### 2. System model, remaining sentences

**Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Predict how staging, activation, reconnection, and rollback affect production traffic.

**Actual effect:** Provides the essential model, but repeats outcomes stated again in the procedural steps. Consolidate it while preserving all four facts: staging is inactive, activation affects new connections, existing connections retain the old credential until reconnection, and rollback remains available for 30 minutes.

**Evidence:** Every stated behavior is established by the repository evidence for `stage`, `activate`, existing connections, credential retention, and `rollback`.

**Disposition:** compress

**Loss if absent:** The operator could activate or end the maintenance window without understanding which connections use which credential or when rollback expires.

### 3. Prerequisites

**Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Avoid an unauthorized change and reserve time to validate clients affected by reconnection.

**Actual effect:** Establishes necessary operational safeguards, but can be shortened to a direct prerequisite statement covering authorization and a window long enough for controlled reconnection.

**Evidence:** Authorization is labeled general production-safety guidance. The need to account for reconnection follows from the established behavior that existing connections retain the previous credential until they reconnect.

**Disposition:** compress

**Loss if absent:** The operator loses the authorization check and may plan a window that ignores the reconnection boundary.

### 4. Staging operation

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Store the replacement without activating it.

**Actual effect:** Gives the first required operation directly. Retain it.

**Evidence:** Repository evidence establishes that `relay credential stage` stores a replacement credential without activating it.

**Disposition:** keep

**Loss if absent:** The operator cannot begin the documented rotation safely.

### 5. Command-suite filler

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Signal that additional command customization exists.

**Actual effect:** Delays the next required action without identifying a decision or supported behavior. Delete it and rely on the credentials reference link.

**Evidence:** Repository evidence establishes only that complete command options live in `docs/reference/credentials.md`; it does not support the broader claim about environments or organizational requirements.

**Disposition:** remove

**Loss if absent:** None; the verified reference link preserves option discovery.

### 6. Pending-credential inspection

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Prevent activation of the wrong or unsuitable replacement credential.

**Actual effect:** Pairs the inspection command with the exact verification the operator must perform. Retain it.

**Evidence:** Repository evidence establishes that `relay credential inspect --pending` prints the pending credential fingerprint and expiry.

**Disposition:** keep

**Loss if absent:** The operator loses the pre-activation check that distinguishes the intended replacement from an incorrect pending credential.

### 7. Activation and controlled verification

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activate the replacement and verify it works on the connection path affected by activation.

**Actual effect:** Provides the operation, expected result, and a bounded verification before the maintenance window closes. Retain it.

**Evidence:** Repository evidence establishes that activation makes the pending credential active for new connections and that existing connections retain the previous credential until reconnection. Reconnecting a controlled client and confirming authentication is labeled general verification guidance derived from that boundary.

**Disposition:** keep

**Loss if absent:** The operator could activate successfully yet finish without testing authentication on a reconnected client.

### 8. Rollback and recovery verification

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recover when the replacement fails controlled authentication.

**Actual effect:** Supplies a time-bounded recovery action, its effect, and a verification step. Retain it.

**Evidence:** Repository evidence establishes that the previous credential is retained for 30 minutes and that `relay credential rollback` restores it for new connections during that window. Rechecking the controlled client is labeled general recovery-verification guidance.

**Disposition:** keep

**Loss if absent:** The operator loses the documented recovery path and may miss the 30-minute rollback opportunity.

### 9. Promotional introduction

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Orient the reader to the product and topic.

**Actual effect:** Adds promotional and generic security language before the actionable model. The heading already states the task, so delete the paragraph.

**Evidence:** Repository evidence does not support the product-positioning claims, and none of the sentences establishes rotation behavior, prerequisites, verification, or recovery.

**Disposition:** remove

**Loss if absent:** None.

### 10. Motivational aside

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Encourage broader security-program reflection.

**Actual effect:** Interrupts the recovery-to-reference path with generic advice that does not help this operator complete or verify the rotation. Delete it.

**Evidence:** Repository evidence contains no product behavior, required decision, or recovery instruction supporting these statements.

**Disposition:** remove

**Loss if absent:** None for the credential-rotation task.

### 11. Generic authentication explanation

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Explain authentication to an unfamiliar reader.

**Actual effect:** Supplies generic definitions without clarifying Relay’s rotation behavior. Delete it; the existing authentication-architecture link preserves access to the deeper concept.

**Evidence:** Repository evidence identifies `docs/concepts/authentication.md` as the authoritative authentication architecture but does not support these generic statements as necessary product guidance.

**Disposition:** remove

**Loss if absent:** None; the task-specific system model and architecture link remain.

### 12. Unsupported option taxonomy

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Preview available command customization.

**Actual effect:** Duplicates reference-level detail and asserts option categories not established by the supplied evidence. Delete the sentence while retaining the credentials reference link.

**Evidence:** Repository evidence establishes only that complete command options live in `docs/reference/credentials.md`; it does not validate this list of flag categories.

**Disposition:** remove

**Loss if absent:** None; operators can still reach the authoritative option reference.

### 13. Credential-command reference

**Passage:** “See `docs/reference/credentials.md` for every command option.”

**Reader problem:** Find complete syntax and options omitted from the operational guide.

**Actual effect:** Keeps exhaustive command detail out of the primary journey while preserving discovery. Retain it.

**Evidence:** Repository evidence explicitly identifies `docs/reference/credentials.md` as the location of complete command options.

**Disposition:** keep

**Loss if absent:** Operators needing non-default syntax or options lose the verified navigation path.

### 14. Authentication-architecture reference

**Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Reach the deeper authentication model when the operational guide is insufficient.

**Actual effect:** Provides concise optional navigation without interrupting the procedure. Retain it alongside the command reference.

**Evidence:** Repository evidence explicitly identifies `docs/concepts/authentication.md` as the authentication-architecture source.

**Disposition:** keep

**Loss if absent:** Readers with deeper architecture questions lose the verified path to authoritative conceptual material.

### 15. Title

**Passage:** “# Rotate a Relay credential”

**Reader problem:** Identify the operational goal immediately.

**Actual effect:** Names the task directly and should remain unchanged.

**Evidence:** The primary reader’s stated goal is rotating a production API credential.

**Disposition:** keep

**Loss if absent:** The guide loses its immediate task orientation.
