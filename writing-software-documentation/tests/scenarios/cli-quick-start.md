# Scenario: CLI quick start

Write the first-use guide for Syncctl.

Repository evidence:

- Syncctl compares a local manifest with a remote workspace.
- `syncctl init example.toml` creates a commented manifest.
- `syncctl plan --file example.toml` reads remote state but changes nothing.
- `syncctl apply --file example.toml` changes the remote workspace and requires confirmation.
- `syncctl apply --file example.toml --dry-run` shows the changes without applying them.
- Authentication, all subcommands, exit codes, and manifest fields are complete in `docs/reference/`.
- Building Syncctl from source is documented in `CONTRIBUTING.md`.

Primary reader: a user installing a released binary who wants to preview their first synchronization safely.
