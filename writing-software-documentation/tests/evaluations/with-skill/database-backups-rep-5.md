# Back up and restore AcornDB

AcornDB records transactions in a journal and compacts them into immutable segments. A backup captures a consistent snapshot of this storage state while writes continue.

## Create and inspect a backup

Create a backup:

```console
acorn backup create --output backups/latest.acorn
```

Inspect the resulting backup before relying on it:

```console
acorn backup inspect backups/latest.acorn
```

Inspection reports the snapshot time, schema version, and checksum status. Confirm that the recovery point and schema version are appropriate and that the checksum status is valid.

The available evidence does not specify failure output or whether creating a backup can replace an existing file. As a precaution, preserve an existing backup or choose a distinct output path.

## Restore safely

Restore into a new directory:

```console
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB restores the snapshot into `restored-data`. The available evidence does not define exact success output or a procedure for verifying that the restored database is usable. Validate it with your deployment’s established checks before using it as a recovery source.

AcornDB refuses to restore into a non-empty target unless `--replace` is supplied. Prefer another target directory when existing data must be preserved. The `--replace` option can destroy the target’s current contents and should be used only when that data is intentionally disposable or has been preserved elsewhere.

For remote storage configuration and every backup option, see the [backup command reference](docs/reference/backup-commands.md).
