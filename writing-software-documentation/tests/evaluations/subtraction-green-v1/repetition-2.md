- **Remove** — “Relay accepts connections through gateways.”  
  **Problem addressed:** system orientation.  
  **Actual effect:** risk; gateway behavior is absent from the supplied evidence.  
  **If removed:** no necessary capability or understanding is lost.  
  **Correction:** delete the unsupported claim.

- **Remove unsupported detail; relocate the links** — “The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios. See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.”  
  **Problem addressed:** deeper command and architecture navigation.  
  **Actual effect:** the unverified flag inventory adds risk and distraction; the links provide useful navigation.  
  **If removed entirely:** readers lose the paths to authoritative options and authentication architecture.  
  **Correction:** remove the flag list, place the command-reference link beside the operational steps, and place the architecture link beside the system model.

- **Keep, but compress duplication** — “A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.”  
  **Problem addressed:** the minimum lifecycle model needed to predict activation and rollback behavior.  
  **Actual effect:** enablement, though later steps repeat parts of it.  
  **If removed:** a first-time operator could misunderstand which connections change and how long rollback remains possible.  
  **Correction:** retain these four facts in a compact pre-procedure model, then trim repeated explanations from later steps.

- **Keep** — “Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.”  
  **Problem addressed:** authority and operational preparation.  
  **Actual effect:** safety.  
  **If removed:** the guide would omit a production-change prerequisite and the reconnect implications established by the evidence.  
  **Correction:** retain; do not sacrifice it to meet the arbitrary reduction target.

- **Compress** — “Stage the replacement with `relay credential stage`. Relay has many commands and flags suitable for many different environments and organizational requirements.”  
  **Problem addressed:** staging the replacement and signaling additional options.  
  **Actual effect:** the command enables action; the second sentence delays it without actionable information.  
  **If removed entirely:** the operator loses the required staging action. Removing only the second sentence loses nothing identifiable.  
  **Correction:** retain the staging command and delete the generic second sentence.

- **Keep** — “Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.”  
  **Problem addressed:** verifying the staged credential before activation.  
  **Actual effect:** enablement and safety.  
  **If removed:** the operator loses the only pre-activation verification step supported by the evidence.  
  **Correction:** retain unchanged or tighten wording without removing either fingerprint or expiry verification.

- **Keep, with minor compression permitted** — “Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.”  
  **Problem addressed:** activation and production verification.  
  **Actual effect:** enablement and safety.  
  **If removed:** the operator cannot complete or verify the primary task.  
  **Correction:** retain the command, new-connection outcome, controlled reconnection, and authentication check; only merge repetitive wording.

- **Keep, with minor compression permitted** — “If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.”  
  **Problem addressed:** bounded recovery from failed activation.  
  **Actual effect:** recovery and safety.  
  **If removed:** the operator loses the documented rollback action, its effect, and post-rollback verification.  
  **Correction:** retain all three elements; explicitly preserve the 30-minute window in either this passage or the preceding system model.

- **Remove** — “Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.”  
  **Problem addressed:** introduction and motivation.  
  **Actual effect:** delay and unsupported promotional background.  
  **If removed:** no action, decision, safety property, system understanding, or navigation is lost.  
  **Correction:** delete the paragraph; the title already states the goal.

- **Remove** — “Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.”  
  **Problem addressed:** broad security encouragement.  
  **Actual effect:** distraction; it supplies no repository-backed operation or decision.  
  **If removed:** nothing identifiable is lost.  
  **Correction:** delete the paragraph.

- **Remove** — “Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.”  
  **Problem addressed:** elementary authentication background.  
  **Actual effect:** delay for the stated operator audience without improving the rotation model.  
  **If removed:** no capability or necessary understanding is lost because the authentication architecture remains discoverable through its reference link.  
  **Correction:** delete the paragraph and preserve the architecture link contextually.

- **Do not delete safety-critical material merely to reach 50%** — “experienced operators can infer the rest.”  
  **Problem addressed:** release-time brevity.  
  **Actual effect:** risk because the primary reader is explicitly rotating a production credential for the first time.  
  **If the operational model, prerequisites, verification, or rollback guidance disappeared:** the reader would lose safe execution and recovery capabilities.  
  **Correction:** achieve the reduction through the removals and compression above; reject any remaining numerical cut that requires deleting those elements.
