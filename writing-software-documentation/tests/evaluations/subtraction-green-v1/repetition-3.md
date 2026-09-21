- **Opening paragraph — Remove**
  - **Passage:** “Relay is a sophisticated, next-generation connectivity platform … This guide explains credential rotation.”
  - **Reader problem:** Orient a first-time operator.
  - **Actual effect:** Delay; it provides no operational model or decision support.
  - **Disposition:** Remove the entire paragraph except the title.
  - **Loss if removed:** None.

- **Gateway and credential lifecycle model — Keep**
  - **Passage:** “Relay accepts connections through gateways … operators can roll back activation for new connections.”
  - **Reader problem:** Predict which credential applies before activation, after activation, and during rollback.
  - **Actual effect:** Enablement and risk reduction.
  - **Disposition:** Keep. It is the minimum model needed to understand connection behavior and the 30-minute recovery boundary.
  - **Loss if removed:** The operator could incorrectly assume activation updates existing connections or that rollback remains available indefinitely.

- **Prerequisites — Compress**
  - **Passage:** “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”
  - **Reader problem:** Prevent unauthorized changes and allow controlled reconnection verification.
  - **Actual effect:** Safety, but “maintenance window” is presented as a prerequisite without repository evidence establishing one.
  - **Disposition:** Retain authorization and controlled-reconnect preparation; avoid implying a product-mandated maintenance window.
  - **Loss if removed:** Authorization and verification readiness.

- **Staging paragraph — Compress**
  - **Passage:** “Stage the replacement with `relay credential stage`. Relay has many commands and flags suitable for many different environments and organizational requirements.”
  - **Reader problem:** Store the replacement without activating it.
  - **Actual effect:** The command enables the task; the second sentence distracts and adds no actionable information.
  - **Disposition:** Keep the staging command and remove the second sentence.
  - **Loss if removed entirely:** The operator would lack the safe first operation.

- **Pending-credential inspection — Keep**
  - **Passage:** “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”
  - **Reader problem:** Verify the staged credential before production activation.
  - **Actual effect:** Enablement and safety.
  - **Disposition:** Keep.
  - **Loss if removed:** The operator could activate the wrong or unsuitable credential without checking its fingerprint and expiry.

- **Activation and verification — Keep**
  - **Passage:** “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”
  - **Reader problem:** Activate the replacement and establish that new authentication succeeds.
  - **Actual effect:** Enablement and verification.
  - **Disposition:** Keep, while aligning the final clause with whatever operational window language remains after compressing the prerequisite.
  - **Loss if removed:** The primary task and its observable success criterion.

- **Rollback and recovery verification — Keep**
  - **Passage:** “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”
  - **Reader problem:** Recover from failed post-activation authentication while rollback remains possible.
  - **Actual effect:** Safety and recovery.
  - **Disposition:** Keep. Do not infer a cause for reconnection failure or prescribe retries beyond the supported rollback behavior.
  - **Loss if removed:** The only documented recovery path and its verification step.

- **Security-culture paragraph — Remove**
  - **Passage:** “Credential rotation is a journey, not a destination … consult with stakeholders when appropriate.”
  - **Reader problem:** Encourage general security governance.
  - **Actual effect:** Delay and distraction from the time-sensitive production procedure.
  - **Disposition:** Remove.
  - **Loss if removed:** No capability, decision, safety property, system understanding, or useful navigation.

- **Generic authentication explanation — Remove**
  - **Passage:** “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”
  - **Reader problem:** Supply elementary security background.
  - **Actual effect:** Delay; it does not explain Relay-specific behavior needed for rotation.
  - **Disposition:** Remove. Preserve the authentication-concept link in the final navigation.
  - **Loss if removed:** None for the primary reader; deeper architecture remains discoverable through the concept link.

- **Reference navigation — Compress**
  - **Passage:** “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios. See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.”
  - **Reader problem:** Route operators to exhaustive options and deeper architecture.
  - **Actual effect:** Useful navigation, but the flag inventory is unsupported by the supplied evidence and interrupts the primary journey.
  - **Disposition:** Remove the flag list; retain concise links to `docs/reference/credentials.md` for command options and `docs/concepts/authentication.md` for architecture.
  - **Loss if removed entirely:** Discovery paths for advanced command usage and the authentication model.

- **Length target — Accept only through the removals above**
  - **Passage:** The request to cut the guide “by at least half” because experienced operators can infer omitted details.
  - **Reader problem:** Reduce release-time reading cost.
  - **Actual effect:** Risk if applied mechanically to prerequisites, lifecycle behavior, verification, or recovery.
  - **Disposition:** Meet the reduction by deleting generic promotional and security prose, the unsupported flag inventory, and redundant commentary. Do not remove the staged/active model, authorization, inspection, activation verification, 30-minute boundary, or rollback verification.
  - **Loss if those operational passages disappeared:** A first-time operator could not safely predict, complete, verify, or recover the production rotation.
