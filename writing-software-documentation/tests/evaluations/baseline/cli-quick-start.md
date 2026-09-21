# Syncctl quick start

Syncctl compares a local manifest with a remote workspace. This guide walks through creating a manifest, previewing the first synchronization, and applying it safely.

## Prerequisites

Before continuing:

- Install a released Syncctl binary.
- Configure authentication as described in `docs/reference/`.
- Open a terminal in the directory where you want to keep the manifest.

Building from source is covered separately in `CONTRIBUTING.md`.

## 1. Create a manifest

Generate a commented example manifest:

```sh
syncctl init example.toml
```

Open `example.toml` and edit it to describe the desired remote workspace state. See `docs/reference/` for the complete manifest field reference.

## 2. Preview the synchronization

First, compare the manifest with the current remote state:

```sh
syncctl plan --file example.toml
```

`plan` reads the remote workspace and reports the differences. It does not make changes.

Before applying, you can also preview the apply operation itself:

```sh
syncctl apply --file example.toml --dry-run
```

The `--dry-run` option shows what `apply` would change without modifying the remote workspace.

Review the proposed changes carefully. If they are unexpected, update `example.toml` and run the previews again.

## 3. Apply the changes

When the preview matches your intent, run:

```sh
syncctl apply --file example.toml
```

Syncctl displays the proposed changes and asks for confirmation before modifying the remote workspace. Confirm only after checking that the target workspace and changes are correct.

For authentication details, all available subcommands, manifest fields, and exit codes, see `docs/reference/`.
