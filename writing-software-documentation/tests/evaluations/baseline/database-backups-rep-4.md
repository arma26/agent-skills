# Back up and restore AcornDB

AcornDB records transactions in a journal and compacts them into immutable segments. A backup captures a consistent snapshot of this storage state while database writes continue.

## Create a backup

```sh
acorn backup create --output backups/latest.acorn
```

This creates `backups/latest.acorn` without stopping writes.

## Inspect the backup

```sh
acorn backup inspect backups/latest.acorn
```

Confirm the reported:

- Snapshot time
- Schema version
- Checksum status

Do not restore a backup whose checksum status indicates a problem.

## Restore safely

Restore into a new directory:

```sh
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB refuses to restore into a non-empty target directory by default.

> **Warning:** `--replace` permits restoring into a non-empty target and can destroy existing data. Verify the target before using it.

For remote storage configuration and all backup options, see [Backup command reference](../../docs/reference/backup-commands.md).
