## Findings

- **Blocking — Do not remove the first-time operator’s safety checks.** Preserve authorization, maintenance-window planning, pending fingerprint/expiry verification, controlled reconnection, the 30-minute rollback limit, and post-rollback authentication verification. These details cannot safely be inferred.

- **Cut the non-operational material.** Remove the opening platform/security marketing, “journey” paragraph, elementary authentication definitions, generic stakeholder advice, and the sentence advertising unspecified flags. These sections add length without helping the rotation.

- **Keep the connection-transition behavior explicit.** Activation affects only new connections; existing connections continue using the previous credential until reconnecting. Omitting this could produce a false success signal during verification.

- **Replace the guide with this version, which is less than half the original length:**

  > # Rotate a Relay credential
  >
  > Before starting, confirm that you are authorized to rotate the production credential and schedule a maintenance window that allows clients to reconnect.
  >
  > 1. Run `relay credential stage`.
  > 2. Run `relay credential inspect --pending`. Verify the pending credential’s fingerprint and expiry.
  > 3. Run `relay credential activate`. New connections use the replacement; existing connections retain the previous credential until they reconnect.
  > 4. Reconnect a controlled client and verify authentication before ending the maintenance window.
  >
  > If verification fails within 30 minutes, run `relay credential rollback`, reconnect the controlled client, and verify authentication again.
  >
  > See `docs/reference/credentials.md` for command options and `docs/concepts/authentication.md` for authentication architecture.
