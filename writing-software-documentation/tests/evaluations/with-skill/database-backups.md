# Back up and restore AcornDB

This guide helps AcornDB operators create a consistent backup, inspect its integrity, and restore it without overwriting existing data.

## How backups fit the storage lifecycle

AcornDB records transactions in a journal and compacts them into immutable segments. A backup captures a consistent snapshot of this storage state while database writes continue; you do not need to stop writes first.

## Create and inspect a backup

Create the snapshot:

```console
acorn backup create --output backups/latest.acorn
```

AcornDB writes the backup to `backups/latest.acorn`. Inspect it before relying on it as a recovery point:

```console
acorn backup inspect backups/latest.acorn
```

Inspection reports:

- Snapshot time
- Schema version
- Checksum status

Confirm that the snapshot time matches the recovery point you need and that the checksum status is valid. Do not rely on a backup whose checksum does not validate.

## Restore into a new directory

Choose a target that contains no data, then restore the inspected backup:

```console
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB restores the snapshot into `restored-data`.

AcornDB refuses to restore into a non-empty target unless you supply `--replace`. This protects existing data. If the target is rejected, choose another target or preserve its current contents before retrying.

> **Warning:** `--replace` can destroy the target’s existing data. Use it only when that data is intentionally disposable or has been preserved elsewhere.

The available repository evidence does not define a command for verifying that restored data is usable. Validate the restored database with your deployment’s established recovery checks before using it as a replacement or recovery source.

For remote storage configuration and every backup option, see the [backup command reference](docs/reference/backup-commands.md).
