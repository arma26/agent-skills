# Back up and restore AcornDB

AcornDB records transactions in a journal and compacts them into immutable segments. A backup captures a consistent snapshot of this storage state while writes continue.

## Create and inspect a backup

```console
acorn backup create --output backups/latest.acorn
acorn backup inspect backups/latest.acorn
```

Inspection reports the snapshot time, schema version, and checksum status. Before relying on the backup, confirm that the snapshot time matches the intended recovery point and that the checksum is valid.

## Restore a backup safely

Restore into a new, empty directory:

```console
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB restores the snapshot into `restored-data`. The available documentation does not establish a command for verifying that the restored database is usable; obtain a repository-backed verification procedure before treating the restore as fully tested.

AcornDB refuses to restore into a non-empty target unless you supply `--replace`. Because `--replace` can destroy the target’s existing data, prefer a new target directory or preserve the current contents before using it.

For remote storage configuration and every backup option, see the [backup command reference](docs/reference/backup-commands.md).
