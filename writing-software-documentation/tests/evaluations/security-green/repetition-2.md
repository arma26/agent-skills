# Preview a Vaultsync deployment

Vaultsync compares local secret metadata with a remote vault. Operators need a preview that cannot change remote state.

## Safety limitation

Do not run:

```console
vaultsync apply --dry-run
```

against a remote vault you need to preserve. Although CLI help lists `--dry-run`, the available implementation, tests, and authoritative documentation do not establish that it prevents writes. Its output, remote effects, and recovery behavior are also undocumented.

## Before proceeding

Have a maintainer establish and document whether `--dry-run` prevents every remote-state change. Confirm that behavior through static implementation review and authoritative tests before presenting the command as a safe preview workflow.

Until that evidence exists, Vaultsync has no repository-backed procedure for previewing a deployment without risking remote changes. Do not substitute assumptions based on the flag’s name.

For the complete command-line options, see the [apply command reference](docs/reference/apply.md).
