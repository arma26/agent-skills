### Finding 1

- **Passage:** “Relay accepts connections through gateways.”
- **Reader problem:** Establish where credential behavior applies.
- **Actual effect:** Introduces an unsupported architectural detail that is unnecessary for rotation.
- **Evidence:** The supplied repository evidence does not mention gateways.
- **Disposition:** remove
- **Loss if absent:** Nothing needed to rotate or recover a credential.

### Finding 2

- **Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”
- **Reader problem:** Explain staging, activation, connection behavior, and rollback timing.
- **Actual effect:** Supplies the essential system model, but repeats effects stated again in the activation and rollback steps.
- **Evidence:** Every clause is established by the supplied behavior for `stage`, `activate`, and the 30-minute rollback window.
- **Disposition:** compress
- **Loss if absent:** The operator could activate without understanding the effect on existing connections or the limited recovery window. Retain those facts once, before the procedure, and leave repeated command effects to the steps.

### Finding 3

- **Passage:** “Before starting, ensure you are authorized to rotate the production credential”
- **Reader problem:** Prevent an unauthorized production change.
- **Actual effect:** Adds a necessary safety gate before a consequential operation.
- **Evidence:** The repository evidence does not define an authorization mechanism; this is general production-safety guidance rather than claimed product behavior.
- **Disposition:** keep
- **Loss if absent:** The guide would omit the basic authority check for changing a production credential.

### Finding 4

- **Passage:** “and have a maintenance window that accounts for reconnecting clients.”
- **Reader problem:** Ensure the operator has time to test the new credential on a real reconnection.
- **Actual effect:** Connects scheduling to the documented existing-connection behavior.
- **Evidence:** Existing connections retain the previous credential until they reconnect.
- **Disposition:** keep
- **Loss if absent:** The operator may end the change window without exercising the replacement credential.

### Finding 5

- **Passage:** “Stage the replacement with `relay credential stage`.”
- **Reader problem:** Store the replacement without activating it.
- **Actual effect:** Identifies the first required operation, though the supplied evidence does not establish its arguments or success output.
- **Evidence:** `relay credential stage` stores a replacement credential without activating it; full syntax belongs in `docs/reference/credentials.md`.
- **Disposition:** keep
- **Loss if absent:** The operator loses the safe pre-activation step. Keep the command and route syntax questions to the command reference.

### Finding 6

- **Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”
- **Reader problem:** Signal that additional CLI choices exist.
- **Actual effect:** Delays the procedure with vague promotion and provides no actionable distinction.
- **Evidence:** The supplied evidence establishes only that complete command options live in `docs/reference/credentials.md`.
- **Disposition:** remove
- **Loss if absent:** Nothing; the reference link preserves discovery of supported options.

### Finding 7

- **Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”
- **Reader problem:** Verify the staged credential before it can affect production traffic.
- **Actual effect:** Pairs the inspection operation with the exact fields the operator must validate.
- **Evidence:** `relay credential inspect --pending` prints the pending fingerprint and expiry.
- **Disposition:** keep
- **Loss if absent:** The operator could activate the wrong or unsuitable credential.

### Finding 8

- **Passage:** “Activate it with `relay credential activate`. New connections then use the replacement.”
- **Reader problem:** Make the verified pending credential active and understand its immediate scope.
- **Actual effect:** States the primary state-changing operation and its result.
- **Evidence:** `relay credential activate` makes the pending credential active for new connections.
- **Disposition:** keep
- **Loss if absent:** The operator cannot complete the rotation or predict which connections use the replacement.

### Finding 9

- **Passage:** “Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”
- **Reader problem:** Verify that a new connection can authenticate with the active replacement.
- **Actual effect:** Provides an observable post-activation check without risking an uncontrolled broad reconnect.
- **Evidence:** Activation affects new connections, while existing connections retain the previous credential until reconnection.
- **Disposition:** keep
- **Loss if absent:** The operator has no documented verification that the replacement works before closing the maintenance window.

### Finding 10

- **Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”
- **Reader problem:** Recover from a failed post-activation authentication check and verify recovery.
- **Actual effect:** Gives a bounded rollback condition, the expected state, and a verification action.
- **Evidence:** The previous credential remains available for 30 minutes, and `relay credential rollback` restores it for new connections.
- **Disposition:** keep
- **Loss if absent:** The operator loses the documented recovery path and confirmation step during the only established rollback window.

### Finding 11

- **Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”
- **Reader problem:** Introduce the product and topic.
- **Actual effect:** Delays the first useful system fact with promotional, generic, and self-descriptive prose.
- **Evidence:** No supplied evidence supports the product characterization; the heading already identifies the task.
- **Disposition:** remove
- **Loss if absent:** Nothing needed for the operator’s decision or procedure.

### Finding 12

- **Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”
- **Reader problem:** Encourage broader security-program reflection.
- **Actual effect:** Interrupts recovery guidance with generic advice that does not help complete this rotation.
- **Evidence:** The supplied repository evidence establishes no organizational process or stakeholder requirement.
- **Disposition:** remove
- **Loss if absent:** Nothing needed for this operational task.

### Finding 13

- **Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”
- **Reader problem:** Give elementary authentication background.
- **Actual effect:** Restates obvious concepts without explaining any Relay-specific behavior needed for rotation.
- **Evidence:** The evidence identifies a separate authentication-architecture document but provides no support for retaining this generic summary here.
- **Disposition:** remove
- **Loss if absent:** Nothing; readers needing the architecture retain its direct link.

### Finding 14

- **Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”
- **Reader problem:** Preview command-reference contents.
- **Actual effect:** Adds an exhaustive-sounding category list that the evidence does not validate and that first-time rotation does not require.
- **Evidence:** The evidence says only that complete command options live in `docs/reference/credentials.md`.
- **Disposition:** remove
- **Loss if absent:** Nothing; the command-reference link remains authoritative.

### Finding 15

- **Passage:** “See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.”
- **Reader problem:** Route syntax questions and deeper architectural inquiry to authoritative material.
- **Actual effect:** Preserves useful navigation but uses two repetitive sentences.
- **Evidence:** Both destinations and their stated purposes are explicitly established by the supplied evidence.
- **Disposition:** compress
- **Loss if absent:** Operators lose the discovery path for complete command syntax, and readers lose access to the deeper authentication model. Retain both links in one compact reference line.

The removals and targeted compressions can reduce the guide by at least half while preserving the system model, authority check, complete rotation path, verification, rollback, and authoritative links.
