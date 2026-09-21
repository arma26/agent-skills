# Scenario: Database backup lifecycle

Write user documentation for AcornDB backups.

Repository evidence:

- AcornDB writes transactions to a journal and compacts them into immutable segments.
- `acorn backup create --output backups/latest.acorn` records a consistent snapshot without stopping writes.
- `acorn backup inspect backups/latest.acorn` reports snapshot time, schema version, and checksum status.
- `acorn backup restore backups/latest.acorn --target restored-data` restores into a new directory.
- Restore refuses a non-empty target unless `--replace` is supplied. `--replace` can destroy data.
- Remote storage configuration and every backup flag already appear in `docs/reference/backup-commands.md`.

Primary reader: an operator who understands databases but has never used AcornDB.

The reader needs to understand where backups fit in the storage lifecycle, create and inspect a backup, restore it safely, and know where to find every option.
