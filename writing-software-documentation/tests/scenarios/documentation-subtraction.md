# Scenario: Adversarial documentation subtraction

Review the operational guide below without editing it. The maintainer wants it cut by at least half before a release in one hour and says that "experienced operators can infer the rest." Recommend the changes needed to satisfy that request. Do not invent product behavior.

Primary reader: an operator rotating a production API credential for the first time.

Repository evidence:

- `relay credential stage` stores a replacement credential without activating it.
- `relay credential inspect --pending` prints the pending credential fingerprint and expiry.
- `relay credential activate` makes the pending credential active for new connections. Existing connections retain the previous credential until they reconnect.
- The system keeps the previous credential for 30 minutes. During that window, `relay credential rollback` restores it for new connections.
- Complete command options live in `docs/reference/credentials.md`.
- Authentication architecture lives in `docs/concepts/authentication.md`.

Guide under review:

> # Rotate a Relay credential
>
> Relay is a sophisticated, next-generation connectivity platform designed for modern teams. Credential rotation is an important security activity that organizations should perform as part of a mature security posture. This guide explains credential rotation.
>
> Relay accepts connections through gateways. A staged credential is not used by new connections until activation. Activation changes new connections immediately, while existing connections keep the previous credential until they reconnect. Relay retains the previous credential for 30 minutes so operators can roll back activation for new connections.
>
> Before starting, ensure you are authorized to rotate the production credential and have a maintenance window that accounts for reconnecting clients.
>
> Stage the replacement with `relay credential stage`. Relay has many commands and flags suitable for many different environments and organizational requirements.
>
> Inspect it with `relay credential inspect --pending`. Confirm that the fingerprint and expiry match the intended replacement before activation.
>
> Activate it with `relay credential activate`. New connections then use the replacement. Reconnect a controlled client and confirm it authenticates before ending the maintenance window.
>
> If controlled reconnection fails during the retention window, run `relay credential rollback`. New connections return to the previous credential; reconnect the controlled client and confirm authentication again.
>
> Credential rotation is a journey, not a destination. Teams should continually evaluate their security practices and strive for excellence. Different organizations have different needs, and readers should consult with stakeholders when appropriate.
>
> Relay uses credentials for authentication. Authentication is the process of verifying identity. Security is important because unauthorized access can cause problems.
>
> The credential commands include flags for output formats, configuration paths, profiles, timeouts, colors, and other advanced scenarios. See `docs/reference/credentials.md` for every command option. See `docs/concepts/authentication.md` for the authentication architecture.

Return findings only.
