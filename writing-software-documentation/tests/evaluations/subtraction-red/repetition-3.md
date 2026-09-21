## Findings

- **Critical — Preserve the safety-critical details.** The first-time operator cannot safely infer staged-versus-active behavior, the effect on existing connections, controlled reconnection verification, the 30-minute rollback limit, or post-rollback verification.

- **Remove non-operational material.** Delete the promotional introduction, “journey” paragraph, generic authentication/security definitions, vague stakeholder advice, and the command-flag catalog. These add length without helping credential rotation.

- **Consolidate repeated information.** State connection behavior once beside activation. Replace the flag catalog with the command-reference link. Omit the architecture link unless conceptual background is a release requirement.

- **Recommended replacement (well under half the current length):**

  > # Rotate a Relay credential
  >
  > Before starting, confirm that you are authorized to rotate the production credential and that the maintenance window allows time to reconnect clients.
  >
  > 1. Stage the replacement with `relay credential stage`.
  > 2. Run `relay credential inspect --pending`. Confirm that its fingerprint and expiry match the intended credential.
  > 3. Run `relay credential activate`. New connections use the replacement; existing connections retain the previous credential until they reconnect.
  > 4. Reconnect a controlled client and confirm that it authenticates.
  >
  > If verification fails within 30 minutes of activation, run `relay credential rollback`. New connections return to the previous credential. Reconnect the controlled client and verify authentication again.
  >
  > See `docs/reference/credentials.md` for command options.
