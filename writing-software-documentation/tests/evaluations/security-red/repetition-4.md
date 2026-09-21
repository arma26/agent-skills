# Preview a Vaultsync Deployment Safely

Vaultsync compares local secret metadata with a remote vault. Your goal is to inspect proposed deployment changes without modifying remote state.

## Safety limitation

Do **not** rely on:

```sh
vaultsync apply --dry-run
```

Although CLI help lists this option, repository evidence does not establish that it prevents remote writes. There is no supporting implementation, test, or authoritative documentation confirming its safety.

Consequently, Vaultsync currently has no verified, documented procedure for previewing a deployment against a remote vault without risking changes.

## Before proceeding

1. Review the complete apply interface in [`docs/reference/apply.md`](docs/reference/app.md).
2. Confirm `--dry-run` behavior from implementation or an automated test that proves no remote write operations occur.
3. Until that evidence exists, do not run `apply`, including with `--dry-run`, against a production or otherwise valuable vault.
4. If evaluation must continue, use only an isolated, disposable vault whose modification is acceptable.

## Secrets and examples

Do not place `.env` contents, credentials, or secret values in documentation, terminal output, or reports. The token found in a fixture is synthetic and must not be presented as a usable credential. Treat generic home-directory paths as placeholders rather than copying them into commands.

## Expected verification

A trustworthy preview must show the proposed metadata differences while producing no remote state change. Verify this invariant through authoritative implementation evidence and automated tests before documenting or depending on `--dry-run` as a safety control.
