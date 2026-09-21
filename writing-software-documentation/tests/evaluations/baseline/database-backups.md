# Back up and restore AcornDB

AcornDB records transactions in a journal and compacts them into immutable segments. A backup captures a consistent snapshot of this storage state while the database continues accepting writes.

Use backups to preserve a recoverable point in time independently of the active journal and segments.

## Create a backup

Choose an output path and run:

```console
acorn backup create --output backups/latest.acorn
```

The command creates a consistent snapshot without stopping writes.

Store the resulting backup somewhere appropriate for your recovery requirements. Remote storage configuration is covered in the [backup command reference](docs/reference/backup-commands.md).

## Inspect a backup

Inspect a backup before relying on or restoring it:

```console
acorn backup inspect backups/latest.acorn
```

The inspection reports:

- Snapshot time
- Schema version
- Checksum status

Confirm that the snapshot time is the recovery point you expect and that the checksum status is valid before proceeding.

## Restore a backup safely

Restore into a new directory:

```console
acorn backup restore backups/latest.acorn --target restored-data
```

AcornDB refuses to restore into a non-empty target directory by default. This protects existing data from accidental replacement.

If the target contains data, choose a different target or move the existing data to a safe location. Use `--replace` only when you deliberately intend to destroy and replace the target’s current contents:

```console
acorn backup restore backups/latest.acorn --target restored-data --replace
```

> **Warning:** `--replace` can destroy data in the target directory. Verify the target path and preserve any needed contents before using it.

For all backup and restore flags, see the [backup command reference](docs/reference/backup-commands.md).
