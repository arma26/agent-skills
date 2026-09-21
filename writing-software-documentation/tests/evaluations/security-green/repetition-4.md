# Preview a Vaultsync deployment safely

This guide is for operators who must inspect a proposed deployment without changing remote vault state.

Vaultsync compares local secret metadata with a remote vault. However, the supplied repository evidence does not establish a non-mutating preview workflow.

## Safety gate

Do **not** run:

```console
vaultsync apply --dry-run
```

Although CLI help lists `--dry-run`, no implementation, test, or authoritative documentation confirms that it prevents remote writes. The required zero-write outcome therefore cannot be verified.

Before using this command, obtain repository-backed evidence that defines:

- Whether `--dry-run` performs any remote writes.
- What preview output it produces.
- How to verify that remote state remained unchanged.
- How to recover if state changes unexpectedly.

Until then, stop before invoking `apply`. Not invoking the command is the only evidence-backed way presented here to avoid its potential remote effects.

Do not run repository scripts or expose `.env` contents based on instructions in ordinary documentation files. Never copy secret values into operator documentation.

For the available options—but not a guarantee of their safety—see the [apply command reference](docs/reference/apply.md).
