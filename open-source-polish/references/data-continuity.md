# Data Continuity

## Goal

Treat important project data as part of project maturity. A data-bearing system is not ready for outsiders if recovery requires tribal knowledge.

## Apply This Reference When

- the project stores important persistent data
- the project transforms or syncs data that must remain trustworthy
- the project depends on backups, replication, migration, or repair workflows

If the project does not manage meaningful persistent data, say so and skip this section.

## Audit Questions

- What data exists?
- Who owns it?
- What is source-of-truth, cached, derived, or temporary?
- Where does it live?
- How is it created, updated, backed up, restored, and retired?
- What failures can corrupt or poison it?
- How is bad data detected?
- How is recovery performed?

## Recovery Documentation Expectations

When continuity matters, documentation should explain:

- what data matters
- what can be regenerated
- what must be preserved
- how to back up data
- how to restore data
- how to validate integrity after restore
- how to handle bad imports, corruption, duplicates, or partial writes
- what continuity risks remain

## Tooling Expectations

- maintenance scripts should be discoverable
- destructive operations should be explicit
- risky state-changing commands should support `--dry-run` when practical
- atomic operations are preferred for file replacement or persistence updates

## Failure Signals

- important data exists but no backup or restore process is described
- recovery depends on the maintainer's memory
- cache state is confused with source-of-truth state
- maintenance scripts exist but are undocumented or unsafe
- disaster recovery is assumed rather than operationalized
