## Findings

- **Do not remove the operational safety path.** The primary reader is rotating a production credential for the first time, so they cannot safely “infer” activation scope, controlled reconnection, the 30-minute rollback limit, or post-rollback verification.

- **Delete the marketing introduction, the “journey” paragraph, and the elementary authentication/security paragraph.** They add no task-specific information and consume much of the guide.

- **Remove the generic statements about numerous commands, flags, environments, and organizational needs.** Replace them with one direct link to `docs/reference/credentials.md` near the first command. Do not invent missing command arguments.

- **Keep the authorization and maintenance-window prerequisite.** The window must account for reconnecting clients because existing connections retain the previous credential after activation.

- **Preserve the ordered operational core:** stage → inspect fingerprint and expiry → activate → reconnect one controlled client → verify authentication.

- **Preserve recovery as a distinct step:** rollback is available for only 30 minutes, affects new connections, and must be followed by reconnecting and verifying the controlled client.

- **Remove `docs/concepts/authentication.md` from this procedural guide.** Authentication architecture is not needed to complete or recover this rotation; it can remain discoverable from conceptual documentation.

- These removals should comfortably achieve the requested 50% reduction while retaining the minimum safe procedure for the stated reader.
