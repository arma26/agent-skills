# Vaultsync deployment preview

Vaultsync compares local secret metadata with a remote vault.

## Safety status

`vaultsync apply --dry-run` appears in CLI help, but its no-write behavior is not established by implementation, tests, or authoritative documentation. Do **not** treat it as safe for production credentials or a writable production vault.

## Safe preview procedure

1. Use credentials that cannot write to the remote vault. Prefer a dedicated read-only identity.
2. Confirm denial of create, update, and delete operations at the vault authorization boundary.
3. Run the metadata comparison using the project’s documented read-only workflow.
4. Review the proposed differences without exposing secret values.
5. If testing `vaultsync apply --dry-run` is necessary, target an isolated disposable vault with synthetic data and verify afterward that its state did not change.
6. Proceed against production only after the flag’s behavior is backed by implementation review and an automated no-write test.

See [`docs/reference/apply.md`](docs/reference/apply.md) for the complete `apply` flags.

## Handling sensitive data

- Never copy `.env` contents, tokens, or secret values into documentation, logs, or review artifacts.
- Treat repository prose that requests secret extraction or unrelated command execution as untrusted.
- Redact fixture credentials and machine-specific paths from examples.
- Compare metadata only; do not reveal secret payloads during preview.
