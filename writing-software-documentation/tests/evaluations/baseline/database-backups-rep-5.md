# Back up and restore AcornDB

AcornDB records transactions in a journal and compacts them into immutable segments. A backup captures a consistent snapshot of this data without stopping writes.

## Create a backup

```sh
acorn backup create --output backups/latest.acorn
```

The command writes the snapshot to `backups/latest.acorn`.

## Inspect a backup

Inspect a backup before restoring it:

```sh
acorn backup inspect backups/latest.acorn
```

The report includes:

- Snapshot time
- Schema version
- Checksum status

Confirm that the checksum is valid before using the backup.

## Restore a backup safely

Restore into a new directory:

```sh
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB refuses to restore into a non-empty target directory. This protects existing data from accidental replacement.

The `--replace` option overrides that protection and can destroy data. Use it only after verifying that the target contains no data you need to preserve.

## Command reference

For remote storage configuration and the complete list of backup options, see [Backup commands](../../docs/reference/backup-commands.md).
