# Preview a Vaultsync deployment

Vaultsync compares local secret metadata with a remote vault. Operators who must guarantee that remote state remains unchanged cannot currently perform an evidence-backed preview.

## Safety limitation

The CLI advertises:

```console
vaultsync apply --dry-run
```

However, the available implementation, tests, and authoritative documentation do not establish that `--dry-run` prevents remote writes. Do not run this command against a vault where changes are unacceptable. The flag is not a verified safety boundary.

Before using it, require repository-backed evidence that:

- no remote create, update, or delete operations occur;
- the preview output clearly identifies proposed changes;
- remote state can be checked independently before and after execution.

The expected output, failure behavior, and recovery procedure are undocumented. Until those gaps are resolved, Vaultsync has no documented safe procedure for previewing a deployment without risking remote changes.

For the complete option listing, see the [apply command reference](docs/reference/apply.md).
