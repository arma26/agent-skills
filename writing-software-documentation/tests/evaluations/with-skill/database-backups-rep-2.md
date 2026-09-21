# Back up and restore AcornDB

This guide helps AcornDB operators create, inspect, and safely restore a backup.

AcornDB first records transactions in a journal, then compacts them into immutable segments. A backup captures a consistent snapshot of this storage state while database writes continue.

## Create and inspect a backup

Create a backup file:

```console
acorn backup create --output backups/latest.acorn
```

Inspect it before relying on it:

```console
acorn backup inspect backups/latest.acorn
```

Inspection reports the snapshot time, schema version, and checksum status. Confirm that the snapshot represents the recovery point you need and that its checksum is valid.

## Restore into a new directory

Restore the backup to an empty or nonexistent target:

```console
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB restores the snapshot into `restored-data`. The available documentation does not establish a command for verifying that the restored database is usable, so obtain a repository-backed verification procedure before treating the restore as fully validated.

AcornDB refuses to restore into a non-empty target unless you supply `--replace`. Prefer another target or preserve the existing contents first.

> **Warning:** `--replace` can destroy data already stored in the target directory.

For remote storage configuration and every backup option, see the [backup command reference](docs/reference/backup-commands.md).
