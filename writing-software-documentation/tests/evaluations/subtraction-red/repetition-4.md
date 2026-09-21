## Findings

- **Critical — Do not remove the operational safety path.** Retain authorization, maintenance-window planning, pending fingerprint/expiry verification, controlled-client reconnection, and rollback verification. A first-time production operator cannot safely infer these steps.

- **Critical — Preserve connection and rollback semantics.** State that activation affects new connections, existing connections retain the old credential until reconnecting, and rollback is available for only 30 minutes. Removing these facts could cause false validation or missed recovery.

- **Cut the non-operational prose entirely.** Delete the opening marketing paragraph, the “journey” paragraph, the elementary authentication/security paragraph, and the sentence about numerous commands and flags. They add length without helping execute the rotation.

- **Replace duplicated explanation with a compact procedure.** Use four ordered steps: stage; inspect and verify fingerprint/expiry; activate, reconnect one controlled client, and verify authentication; rollback within 30 minutes if verification fails, then reconnect and verify again.

- **Keep reference boundaries concise.** Link `docs/reference/credentials.md` for command options and `docs/concepts/authentication.md` for architecture; do not enumerate flag categories in this task guide.

- **The requested 50% reduction is achievable without deleting safeguards.** Remove generic prose and duplication, not prerequisites, validation criteria, connection behavior, or recovery instructions.
