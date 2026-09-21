### 1

- **Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”
- **Reader problem:** Introduce the task.
- **Actual effect:** Delays the first-time operator with promotional language, generic security advice, and a restatement of the title.
- **Evidence:** No supplied repository evidence supports the promotional characterization or organizational-practice claim.
- **Disposition:** remove
- **Loss if absent:** Nothing; the title already identifies the task.

### 2

- **Passage:** “Relay accepts connections through gateways.”
- **Reader problem:** Explain the connection architecture.
- **Actual effect:** Adds an architectural detail that does not change any rotation decision or action.
- **Evidence:** The supplied evidence does not mention gateways.
- **Disposition:** remove
- **Loss if absent:** Nothing needed to rotate or verify the credential.

### 3

- **Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”
- **Reader problem:** Provide the state-transition and rollback model needed to rotate safely.
- **Actual effect:** Enables the operator to predict staging, activation, reconnect, and rollback behavior, but repeats outcomes later in the procedure.
- **Evidence:** Every behavior is directly established by the supplied repository evidence.
- **Disposition:** compress
- **Loss if absent:** The operator would not understand which connections use which credential or the 30-minute recovery boundary. Retain one concise lifecycle summary and avoid repeating it verbatim in later steps.

### 4

- **Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”
- **Reader problem:** Prevent unauthorized work and allow time to verify reconnect behavior.
- **Actual effect:** Provides useful operational safety guidance, but combines an organization-specific authorization rule with a longer planning instruction.
- **Evidence:** The supplied evidence establishes that existing connections retain the old credential until reconnecting. It does not define authorization policy or require a maintenance window; those are general operational guidance.
- **Disposition:** compress
- **Loss if absent:** The operator could rotate without appropriate local approval or without planning for the reconnect-dependent verification. Retain these as concise, explicitly local prerequisites.

### 5

- **Passage:** “Stage the replacement with `relay credential stage`.”
- **Reader problem:** Store the replacement without activating it.
- **Actual effect:** Gives the first required operation in the safe sequence.
- **Evidence:** The supplied evidence directly establishes that this command stores a replacement without activating it.
- **Disposition:** keep
- **Loss if absent:** The operator could not begin the documented rotation procedure.

### 6

- **Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”
- **Reader problem:** Signal that additional configuration exists.
- **Actual effect:** Interrupts the procedure with vague, non-actionable detail.
- **Evidence:** The evidence establishes only that complete command options are documented elsewhere; it does not support this characterization.
- **Disposition:** remove
- **Loss if absent:** Nothing; the command-reference link provides useful navigation.

### 7

- **Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”
- **Reader problem:** Prevent activation of the wrong or expired replacement.
- **Actual effect:** Supplies both the verification command and the decision criterion before the state change.
- **Evidence:** The supplied evidence establishes that the command prints the pending credential fingerprint and expiry.
- **Disposition:** keep
- **Loss if absent:** The operator loses the only pre-activation check that the staged credential is the intended replacement.

### 8

- **Passage:** “Activate it with `relay credential activate`. New connections then use the replacement.”
- **Reader problem:** Activate the verified replacement and understand its immediate effect.
- **Actual effect:** Gives the state-changing command and its expected result.
- **Evidence:** Both claims are directly established by the supplied repository evidence.
- **Disposition:** keep
- **Loss if absent:** The operator cannot complete activation or know which connections should use the replacement.

### 9

- **Passage:** “Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”
- **Reader problem:** Verify the active credential through a new connection before declaring success.
- **Actual effect:** Provides a bounded production check tied to the documented reconnect behavior.
- **Evidence:** The evidence establishes that existing connections retain the previous credential until reconnecting; using a controlled reconnection as verification is general operational guidance, not explicitly documented product behavior.
- **Disposition:** compress
- **Loss if absent:** The guide would provide no practical verification that a new connection can authenticate with the replacement. Retain the controlled reconnect check while labeling it as the operator’s verification step.

### 10

- **Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”
- **Reader problem:** Recover from a failed post-activation check.
- **Actual effect:** Supplies the time-bounded recovery command, expected state, and verification, though the three instructions can be stated more compactly.
- **Evidence:** The 30-minute retention window, rollback command, and restoration of the previous credential for new connections are directly established. Reconnecting a controlled client is general verification guidance derived from the documented connection behavior.
- **Disposition:** compress
- **Loss if absent:** The operator loses the documented recovery path and confirmation step during the only rollback window.

### 11

- **Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”
- **Reader problem:** Encourage ongoing security governance.
- **Actual effect:** Distracts from an urgent operational procedure with generic advice and clichés.
- **Evidence:** No supplied repository evidence supports these organizational recommendations.
- **Disposition:** remove
- **Loss if absent:** Nothing required to rotate, verify, or recover the credential.

### 12

- **Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”
- **Reader problem:** Explain elementary authentication concepts.
- **Actual effect:** Adds generic background below the completed procedure without improving any operator decision.
- **Evidence:** Only the existence of separate authentication-architecture documentation is established; these statements are not needed for the primary task.
- **Disposition:** remove
- **Loss if absent:** No operational capability or necessary system understanding.

### 13

- **Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”
- **Reader problem:** Preview command-reference contents.
- **Actual effect:** Adds an unsupported option inventory that can drift from the authoritative reference.
- **Evidence:** The supplied evidence says complete options live in `docs/reference/credentials.md` but does not establish any listed option category.
- **Disposition:** remove
- **Loss if absent:** Nothing; operators can consult the authoritative reference.

### 14

- **Passage:** “See `docs/reference/credentials.md` for every command option.”
- **Reader problem:** Find complete syntax without expanding the operational guide.
- **Actual effect:** Preserves useful navigation while keeping exhaustive detail out of the primary journey.
- **Evidence:** The supplied evidence identifies this exact repository-relative destination as the complete command reference.
- **Disposition:** keep
- **Loss if absent:** Operators needing non-default options would lose the authoritative discovery path.

### 15

- **Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”
- **Reader problem:** Support deeper architectural inquiry.
- **Actual effect:** Useful secondary navigation, but unrelated to completing the immediate rotation.
- **Evidence:** The supplied evidence identifies this exact repository-relative destination as the authentication architecture.
- **Disposition:** relocate
- **Loss if absent:** Readers would lose the discovery path to the broader system model. Preserve it in a compact related-documentation section after the operational procedure.

The requested reduction is attainable by removing the unsupported and generic passages, consolidating repeated lifecycle outcomes, and retaining the stage–inspect–activate–verify–rollback path. Cutting safety prerequisites, verification, reconnect semantics, or rollback timing merely because experienced operators might infer them would materially weaken the guide.
