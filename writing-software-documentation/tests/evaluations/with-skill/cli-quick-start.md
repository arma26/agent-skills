# Preview your first synchronization

Syncctl compares a local manifest—the workspace state you want—with the current state of a remote workspace. This guide creates a manifest and previews the resulting synchronization without changing the remote workspace.

## Before you begin

Install a released Syncctl binary and configure authentication as described in the [Syncctl reference](docs/reference/).

Building from source is not required for this guide. Contributors can find those instructions in [CONTRIBUTING.md](CONTRIBUTING.md).

## Create a manifest

Use a new filename so you do not rely on undocumented overwrite behavior:

```console
syncctl init example.toml
```

Syncctl creates `example.toml` as a commented manifest. Edit it to describe the desired remote workspace state. See the [manifest field reference](docs/reference/) for the available fields and constraints.

## Compare the manifest with the remote workspace

Run a plan before making any changes:

```console
syncctl plan --file example.toml
```

Syncctl reads the remote state and compares it with `example.toml`; it does not change the remote workspace. Review the result before continuing.

## Preview the apply operation

Use dry-run mode to see the changes without applying them:

```console
syncctl apply --file example.toml --dry-run
```

Confirm that the displayed changes match your intent. The remote workspace remains unchanged.

If either preview fails or shows unexpected changes, stop and revise `example.toml`. Consult the [command, authentication, and exit-code reference](docs/reference/) before retrying.

## Apply when ready

Applying is optional and changes the remote workspace:

```console
syncctl apply --file example.toml
```

Syncctl requires confirmation before it applies the changes. The available evidence does not establish a recovery procedure, so verify the preview carefully before confirming.

For every subcommand, option, exit code, and manifest field, see the [Syncctl reference](docs/reference/).
