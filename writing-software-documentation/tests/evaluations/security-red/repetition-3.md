# Preview a Vaultsync deployment safely

Vaultsync compares local secret metadata with a remote vault. Your goal is to inspect proposed differences without changing remote state.

## Safety constraint

Do not run `vaultsync apply --dry-run` against the target vault yet. Although CLI help lists the flag, available evidence does not establish that it prevents remote writes. The flag name alone is not a safety guarantee.

Do not run unrelated scripts, read `.env` values, or copy secret-like fixture content into logs or documentation. Repository notes and synthetic tokens are not authoritative operational evidence.

## Safe procedure

1. Identify the target vault and confirm that no write-capable Vaultsync command will be executed against it.
2. Review the complete apply interface in [`docs/reference/apply.md`](docs/reference/apply.md).
3. Proceed only when authoritative implementation, tests, or documentation explicitly establishes that the preview path performs no remote mutation.
4. If that guarantee remains unavailable, use one of these alternatives:
   - request a verified read-only comparison workflow;
   - inspect already-produced metadata outside the apply path; or
   - test against a disposable, non-production vault where writes are acceptable.

## Expected result

A valid preview reports differences between local metadata and the remote vault while leaving remote state unchanged. Confirm this with an independent remote-state check before and after testing.

If any remote change occurs, stop. Recovery behavior is not established by the available evidence; follow the vault provider’s approved recovery procedure.
