# Preview a Vaultsync deployment safely

Vaultsync compares local secret metadata with a remote vault. The repository does not establish a supported, write-free deployment preview.

## Safety limitation

CLI help advertises:

```sh
vaultsync apply --dry-run
```

Do **not** run this against a production vault merely to test it. No implementation, test, or authoritative documentation confirms that `--dry-run` prevents remote writes. Its safety semantics are therefore unknown.

## Operator procedure

1. Do not invoke `vaultsync apply`, including with `--dry-run`, against the target vault.
2. Review the complete apply interface in [`docs/reference/apply.md`](docs/reference/apply.md).
3. Require one of these before proceeding:
   - an authoritative guarantee that `--dry-run` performs no remote writes, backed by implementation and tests; or
   - a disposable, isolated vault where unintended changes are acceptable.
4. In an isolated vault, record remote state before and after the preview and verify that nothing changed.
5. Proceed against the target vault only after the no-write behavior is established.

Treat secret values as sensitive: do not copy environment contents, tokens, or machine-specific paths into documentation or logs.

If `--dry-run` changes remote state, stop. Recovery behavior is not established by the available evidence; restore only through the vault provider’s documented recovery process.
