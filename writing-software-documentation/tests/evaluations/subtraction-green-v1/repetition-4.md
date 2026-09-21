1. **Remove** — “Relay is a sophisticated… This guide explains credential rotation.”

   - Intended problem: Introduce the product and topic.
   - Actual effect: Delays the operation with promotional and generic security language.
   - Evidence: None of these claims support the documented rotation behavior.
   - Correction: Delete the paragraph.
   - Loss if removed: None.

2. **Keep, with light compression** — “Relay accepts connections through gateways… roll back activation for new connections.”

   - Intended problem: Explain staging, activation, connection behavior, and the rollback window.
   - Actual effect: Enables safe decisions during rotation.
   - Evidence: Every behavioral statement matches the supplied repository evidence.
   - Correction: Preserve all four facts, but combine overlapping activation sentences.
   - Loss if removed: The operator could misunderstand when credentials take effect, disrupt existing connections, or miss the 30-minute recovery window.

3. **Keep** — “Before starting, ensure you are authorized… reconnecting clients.”

   - Intended problem: Establish production authorization and operational timing prerequisites.
   - Actual effect: Reduces unauthorized changes and premature maintenance-window closure.
   - Evidence: Existing connections retain the prior credential until reconnection.
   - Correction: Retain; do not assume experienced operators can infer production authorization or reconnection impact.
   - Loss if removed: A safety prerequisite and necessary scheduling constraint.

4. **Compress** — “Stage the replacement with `relay credential stage`. Relay has many commands and flags suitable for many different environments and organizational requirements.”

   - Intended problem: Initiate rotation and acknowledge additional CLI options.
   - Actual effect: The first sentence enables action; the second delays it without identifying a concrete need.
   - Evidence: Staging behavior and the command are established; the generic flags claim is not.
   - Correction: Keep only the staging instruction and route option discovery to the reference link later.
   - Loss if removed entirely: The first required operation.

5. **Keep** — “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”

   - Intended problem: Verify the staged credential before a production change.
   - Actual effect: Provides both a command and an observable acceptance check.
   - Evidence: The command prints the pending fingerprint and expiry.
   - Correction: Retain unchanged.
   - Loss if removed: Pre-activation verification of credential identity and expiry.

6. **Keep, with light compression** — “Activate it with `relay credential activate`… before ending the maintenance window.”

   - Intended problem: Activate the credential and verify authentication through a controlled reconnection.
   - Actual effect: Enables the primary goal and confirms the changed behavior.
   - Evidence: Activation affects new connections; existing connections require reconnection.
   - Correction: Retain the command, new-connection result, and controlled-client verification; tighten wording only.
   - Loss if removed: Completion and verification of the rotation.

7. **Keep** — “If controlled reconnection fails during the retention window, run `relay credential rollback`… confirm authentication again.”

   - Intended problem: Recover from failed authentication.
   - Actual effect: Supplies a time-bounded rollback action and verifies recovery.
   - Evidence: The previous credential remains recoverable for 30 minutes and rollback restores it for new connections.
   - Correction: Retain; optionally replace “retention window” with “30-minute retention window” to keep the deadline visible.
   - Loss if removed: The documented recovery path and its verification.

8. **Remove** — “Credential rotation is a journey, not a destination… consult with stakeholders when appropriate.”

   - Intended problem: Encourage ongoing security governance.
   - Actual effect: Distracts from the time-sensitive production procedure with generic advice.
   - Evidence: No supplied repository evidence establishes these organizational recommendations.
   - Correction: Delete the paragraph.
   - Loss if removed: None relevant to completing or recovering this rotation.

9. **Remove** — “Relay uses credentials for authentication… unauthorized access can cause problems.”

   - Intended problem: Explain basic authentication and security concepts.
   - Actual effect: Repeats obvious background without giving this operator a useful system model.
   - Evidence: The authentication architecture already has an authoritative concept page.
   - Correction: Delete the paragraph and preserve the concept-page link.
   - Loss if removed: No operational capability; deeper understanding remains discoverable through the link.

10. **Compress** — “The credential commands include flags for output formats… See `docs/concepts/authentication.md` for the authentication architecture.”

   - Intended problem: Route readers to exhaustive CLI and architecture material.
   - Actual effect: The links provide useful navigation, but enumerating flag categories interrupts the procedure and is not supported by the supplied evidence.
   - Evidence: Complete options live in `docs/reference/credentials.md`; architecture lives in `docs/concepts/authentication.md`.
   - Correction: Remove the flag enumeration and retain one short references sentence containing both repository-relative links.
   - Loss if removed entirely: Navigation to authoritative command options and the deeper authentication model.

11. **Do not satisfy the “at least half” target by cutting the operational core.**

   - Intended problem: Meet an arbitrary release-time length target.
   - Actual effect: Removing prerequisites, lifecycle behavior, verification, or rollback would create operational risk.
   - Evidence: Those passages directly express every supplied behavior required for a first production rotation.
   - Correction: Achieve as much reduction as possible through findings 1, 4, 8, 9, and 10, plus minor compression of findings 2 and 6. If that does not reach 50%, reject the numeric target rather than deleting safety-critical content.
   - Loss if the remaining material disappeared: Required decisions, verification, recovery, and the minimum system model.
