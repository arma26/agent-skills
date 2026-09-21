# Back up and restore AcornDB

AcornDB records transactions in a journal, then compacts them into immutable segments. A backup captures a consistent snapshot of this storage state without stopping writes.

## Create a backup

```sh
acorn backup create --output backups/latest.acorn
```

The destination directory must exist before you run the command.

## Inspect a backup

Inspect a backup before restoring it:

```sh
acorn backup inspect backups/latest.acorn
```

The report includes:

- Snapshot time
- Schema version
- Checksum status

Do not restore a backup whose checksum validation fails.

## Restore a backup safely

Restore into a new directory:

```sh
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB refuses to restore into a non-empty target directory. This protects existing data from accidental overwrite.

The `--replace` option overrides that protection and can destroy data in the target. Use it only after confirming that the existing contents are disposable.

For remote storage configuration and all backup command options, see [Backup command reference](../../docs/reference/backup-commands.md).
