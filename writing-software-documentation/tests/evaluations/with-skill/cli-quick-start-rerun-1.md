# Preview your first Syncctl synchronization

Syncctl compares a local manifest with a remote workspace. This guide creates a manifest and previews the resulting changes without modifying the remote workspace.

## Prerequisites

- Install a released Syncctl binary.
- Configure authentication using the [Syncctl reference](docs/reference/).

## 1. Create a manifest

Use a new filename so you do not risk replacing an existing file:

```console
syncctl init example.toml
```

Syncctl creates a commented manifest at `example.toml`. Open the file to verify it was created, then configure the desired workspace state. See the [manifest field reference](docs/reference/) for available fields.

## 2. Check the remote state safely

```console
syncctl plan --file example.toml
```

Syncctl compares the manifest with the remote workspace. This command reads remote state but does not change it.

## 3. Preview the changes

```console
syncctl apply --file example.toml --dry-run
```

The dry run shows the changes Syncctl would make without applying them. Review the displayed changes before proceeding.

If a command fails, use the authentication and exit-code guidance in the [Syncctl reference](docs/reference/).

## Apply when ready

Applying a synchronization changes the remote workspace:

```console
syncctl apply --file example.toml
```

Syncctl requires confirmation before making the changes. This quick start does not establish a post-apply verification or recovery procedure, so define those safeguards for your workspace before confirming.

For all commands, options, exit codes, and manifest fields, see the [Syncctl reference](docs/reference/). To build Syncctl from source, see [CONTRIBUTING.md](CONTRIBUTING.md).
