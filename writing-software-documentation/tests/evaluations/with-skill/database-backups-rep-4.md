# Back up and restore AcornDB

AcornDB writes transactions to a journal and compacts them into immutable segments. A backup captures a consistent snapshot of this storage state without stopping writes.

## Create and inspect a backup

Create the backup, then inspect it before relying on it:

```console
acorn backup create --output backups/latest.acorn
acorn backup inspect backups/latest.acorn
```

Inspection reports the snapshot time, schema version, and checksum status. Confirm that the recovery point is appropriate and review the checksum status before storing or restoring the backup.

The available repository evidence does not define recovery behavior for a failed creation or inspection. Do not treat the backup as usable until inspection succeeds.

## Restore into a new directory

Restore the backup to a new, empty target:

```console
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB restores the snapshot into `restored-data`. It refuses a non-empty target by default; choose another target or preserve the existing contents elsewhere.

The `--replace` option overrides this protection and can destroy the target’s current data. Avoid it unless that destruction is intentional and the existing data is recoverable.

The available evidence does not define a command for verifying the restored database’s usability. Complete your repository-backed validation procedure before considering recovery finished.

For remote storage configuration and every available option, see the [backup command reference](docs/reference/backup-commands.md).
