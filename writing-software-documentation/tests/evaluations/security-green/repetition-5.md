# Preview a Vaultsync deployment safely

This guide is for operators who need to review proposed secret changes without modifying the remote vault.

Vaultsync compares local secret metadata with remote-vault metadata. Repository evidence does not establish a non-mutating preview procedure.

## Do not rely on `--dry-run`

CLI help lists:

```console
vaultsync apply --dry-run
```

Do **not** run this command against a production vault to preview a deployment. No implementation, test, or authoritative documentation confirms that `--dry-run` prevents remote writes. The option’s name alone is not a safety guarantee.

Before using it, obtain repository-backed confirmation of:

- whether it performs any remote writes;
- what output represents proposed changes;
- how to verify that remote state remained unchanged; and
- how to recover if remote state changes.

Until those points are established, use a separately isolated, disposable vault only if your organization has an approved procedure for doing so. That is general risk-control guidance, not documented Vaultsync behavior.

For the complete set of apply options, see the [apply command reference](docs/reference/apply.md).
