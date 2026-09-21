# Back up and restore AcornDB

AcornDB records transactions in a journal, then compacts them into immutable segments. A backup captures a consistent snapshot of this storage state while the database continues accepting writes.

## Create a backup

```sh
acorn backup create --output backups/latest.acorn
```

Store the resulting backup separately from the database it protects.

## Inspect a backup

Before restoring, inspect the backup:

```sh
acorn backup inspect backups/latest.acorn
```

The report includes:

- Snapshot time
- Schema version
- Checksum status

Do not restore a backup whose checksum validation fails.

## Restore safely

Restore into a new directory:

```sh
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB refuses to restore into a non-empty target directory. This protects existing data from accidental replacement.

To replace a non-empty target, you must explicitly supply `--replace`. This operation can destroy data; verify the target directory and preserve anything needed before proceeding.

## Command reference

For remote storage configuration and the complete set of backup options, see [Backup commands](../docs/reference/backup-commands.md).
