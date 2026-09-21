## Finding 1

**Passage:** “Relay accepts connections through gateways.”

**Reader problem:** Explain where credential behavior applies.

**Actual effect:** Introduces an unsupported architecture detail that is unnecessary for rotation.

**Evidence:** The supplied repository evidence does not mention gateways.

**Disposition:** remove

**Loss if absent:** None.

## Finding 2

**Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios.”

**Reader problem:** Alert operators to additional command options.

**Actual effect:** Adds an unverified option inventory and distracts from the rotation sequence.

**Evidence:** The evidence establishes only that complete command options live in `docs/reference/credentials.md`; it does not establish this list.

**Disposition:** remove

**Loss if absent:** None; the reference link preserves option discovery.

## Finding 3

**Passage:** “Stage the replacement with `relay credential stage`.”

**Reader problem:** Begin the rotation without activating the replacement.

**Actual effect:** Provides the required first operation, but the supplied evidence does not establish how the replacement value is provided. The command-reference link should be placed directly beside this step so the operator can resolve required arguments without guessing.

**Evidence:** Repository evidence states that `relay credential stage` stores a replacement credential without activating it. Complete options live in `docs/reference/credentials.md`.

**Disposition:** keep

**Loss if absent:** The operator loses the first executable step in the rotation.

## Finding 4

**Passage:** “# Rotate a Relay credential”

**Reader problem:** Identify the task and scope.

**Actual effect:** Gives the operator an immediate task-oriented entry point.

**Evidence:** The scenario’s primary goal is rotating a Relay production API credential.

**Disposition:** keep

**Loss if absent:** The page loses its task identity and scan target.

## Finding 5

**Passage:** “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”

**Reader problem:** Understand staging, activation, connection behavior, and the rollback window before acting.

**Actual effect:** Supplies the essential safety model, but repeats outcomes later in the procedural steps. It can be compressed while retaining all four facts.

**Evidence:** Every behavior in the passage is explicitly established by the supplied repository evidence.

**Disposition:** compress

**Loss if absent:** The operator could misunderstand when the credential becomes active, why reconnection matters, or when rollback remains possible.

## Finding 6

**Passage:** “Before starting, ensure you are authorized to rotate the production credential”

**Reader problem:** Prevent an operator from making an unauthorized production change.

**Actual effect:** Preserves an important safety check without burdening the procedure.

**Evidence:** The evidence does not define an authorization mechanism. This is general operational safety guidance, not established Relay behavior, and should remain framed that way.

**Disposition:** keep

**Loss if absent:** The guide loses its explicit authority boundary for a production credential change.

## Finding 7

**Passage:** “and have a maintenance window that accounts for reconnecting clients.”

**Reader problem:** Plan for clients that must reconnect before using the replacement.

**Actual effect:** Connects the procedure to the reconnection consequence, but overstates a maintenance window as a prerequisite not established by the evidence. Compress it into planning guidance for controlled reconnects.

**Evidence:** The evidence establishes that existing connections retain the previous credential until reconnection; it does not require a maintenance window.

**Disposition:** compress

**Loss if absent:** The operator loses advance warning that validation requires reconnection.

## Finding 8

**Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

**Reader problem:** Detect a wrong or expired replacement before production activation.

**Actual effect:** Provides a supported verification gate between staging and activation.

**Evidence:** Repository evidence states that `relay credential inspect --pending` prints the pending fingerprint and expiry.

**Disposition:** keep

**Loss if absent:** The operator loses the only pre-activation check of the staged credential.

## Finding 9

**Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”

**Reader problem:** Activate the credential and verify production authentication safely.

**Actual effect:** Pairs the state-changing operation with its expected result and a controlled verification.

**Evidence:** Repository evidence states that activation makes the pending credential active for new connections and existing connections retain the previous credential until reconnection. Controlled-client verification is general operational guidance consistent with that behavior.

**Disposition:** keep

**Loss if absent:** The operator cannot complete or verify activation.

## Finding 10

**Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”

**Reader problem:** Recover from a failed activation while recovery remains available.

**Actual effect:** Gives the operator a bounded recovery action, expected result, and verification.

**Evidence:** Repository evidence states that the previous credential is retained for 30 minutes and `relay credential rollback` restores it for new connections.

**Disposition:** keep

**Loss if absent:** The operator loses the documented recovery path and its verification step.

## Finding 11

**Passage:** “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”

**Reader problem:** Introduce the product and topic.

**Actual effect:** Delays the procedure with promotional language, generic security advice, and a restatement of the title.

**Evidence:** No supplied evidence supports the promotional characterization, and none of the passage enables rotation.

**Disposition:** remove

**Loss if absent:** None.

## Finding 12

**Passage:** “Relay has many commands and flags suitable for many different environments and organizational requirements.”

**Reader problem:** Signal that additional CLI functionality exists.

**Actual effect:** Adds vague, unsupported commentary between the operator and the required verification step.

**Evidence:** The evidence establishes a complete command reference, not the breadth or suitability claimed here.

**Disposition:** remove

**Loss if absent:** None; the command-reference link preserves useful navigation.

## Finding 13

**Passage:** “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”

**Reader problem:** Encourage broader security-process reflection.

**Actual effect:** Interrupts an urgent operational task with generic advice that supplies no actionable Relay guidance.

**Evidence:** The supplied repository evidence establishes none of these recommendations.

**Disposition:** remove

**Loss if absent:** None for the stated reader goal.

## Finding 14

**Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”

**Reader problem:** Explain elementary authentication and security concepts.

**Actual effect:** Consumes attention without helping an operator predict Relay’s rotation behavior or make a decision.

**Evidence:** The only relevant supplied source is the authentication architecture link; no evidence supports a need for these generic definitions in this operational guide.

**Disposition:** remove

**Loss if absent:** None for an operator rotating a credential.

## Finding 15

**Passage:** “See `docs/reference/credentials.md` for every command option.”

**Reader problem:** Find authoritative command syntax and options.

**Actual effect:** Preserves essential navigation, but its current placement comes after all commands. Move it beside the first command rather than duplicating option detail in the guide.

**Evidence:** Repository evidence explicitly identifies this file as the complete command-options reference.

**Disposition:** relocate

**Loss if absent:** The operator cannot resolve omitted arguments or advanced command requirements without guessing.

## Finding 16

**Passage:** “See `docs/concepts/authentication.md` for the authentication architecture.”

**Reader problem:** Support deeper investigation of Relay’s authentication design.

**Actual effect:** Provides optional navigation without burdening the operational sequence when retained at the end.

**Evidence:** Repository evidence explicitly identifies this file as the authentication-architecture source.

**Disposition:** keep

**Loss if absent:** Readers lose the documented route to the deeper system model.

The requested reduction is attainable by removing the unsupported and generic passages, compressing the supported system model and reconnect-planning clause, and preserving the activation, verification, rollback, and reference-navigation content. Cutting those operational safeguards merely to exceed the length target would impair first-time production use.
