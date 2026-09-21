# Preview a Vaultsync deployment

Vaultsync compares local secret metadata with a remote vault. A valid preview must leave remote state unchanged.

## Safety limitation

Do not run this command against a vault that must remain unchanged:

```console
vaultsync apply --dry-run
```

CLI help lists `--dry-run`, but the available repository evidence does not establish that it prevents writes. It also provides no reliable way to verify afterward that remote state was unchanged.

Before using the command, obtain authoritative documentation, implementation evidence, or a test that confirms:

- `--dry-run` performs no remote writes.
- Which remote state the command reads or may affect.
- How an operator can verify that the vault remains unchanged.

Until that evidence exists, Vaultsync has no documented safe procedure for previewing a deployment.

For the complete option list—not a safety guarantee—see the [apply command reference](docs/reference/apply.md).

As general security guidance, never copy `.env` values or secret tokens into documentation or command output.
