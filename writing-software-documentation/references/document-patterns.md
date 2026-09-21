# Document Patterns

## Contents

- [Orientation](#orientation)
- [Conceptual explanation](#conceptual-explanation)
- [Operational guidance](#operational-guidance)
- [Reference](#reference)
- [Choose the dominant purpose](#choose-the-dominant-purpose)

## Orientation

Lead with the outcome the software enables and the reader who benefits. Establish the smallest useful model, guide the reader to one safe first success, describe its expected result, and offer clear next destinations.

Keep build-from-source instructions out of orientation for users of released artifacts. Link contributor setup separately unless the source build is itself the reader's goal.

## Conceptual Explanation

Explain the responsibilities and boundaries of relevant components. Show lifecycle or data flow and state the invariants a reader must preserve. Link each concept to the operations it helps the reader understand.

Avoid a source-code walkthrough unless implementation is the subject. Organize around the system model, not file order.

## Operational Guidance

Structure every meaningful operation as:

1. Explain what the operation does and where it fits.
2. State prerequisites, assumptions, and material risks.
3. Show one concise, realistic example.
4. Describe the expected result and how to verify it.
5. Explain likely failure and proportional recovery when consequences matter.
6. Link to relevant concepts and complete reference material.

For a state-changing operation, complete step 4 with either an evidence-backed way to observe the resulting state or an explicit statement that repository evidence does not establish post-operation verification. Put plans and dry runs in step 2 as pre-operation risk controls; keep the step 4 slot focused on the state after the operation.

Repeat the pattern for an extension only when it serves a common reader goal, materially changes behavior or safety, or needs a different mental model. Link minor variations and exhaustive options to reference material.

### AcornDB example

Explain first that AcornDB records transactions in a journal, compacts them into immutable segments, and captures that storage state in a consistent backup while writes continue.

Create and inspect a backup:

```console
acorn backup create --output backups/latest.acorn
acorn backup inspect backups/latest.acorn
```

State the observable result: inspection reports snapshot time, schema version, and checksum status. Tell the reader to confirm the recovery point and a valid checksum before relying on the backup.

Restore safely into a new target:

```console
acorn backup restore backups/latest.acorn --target restored-data
```

State the evidence-backed expected result: AcornDB restores the backup into the new `restored-data` target. The supplied evidence establishes neither exact success output nor a safe command for verifying that the restored data is usable. Disclose that limitation instead of inventing a check, and obtain a repository-backed verification procedure before presenting the restore as fully verified.

Explain that AcornDB refuses a non-empty target by default. Direct the reader to choose another target or preserve existing contents; show `--replace` only with an adjacent warning that it destroys the target's current contents. End with a contextual link copied from verified repository evidence, for example: `For every option, see the [backup command reference](docs/reference/backup-commands.md).` Preserve that supplied repository-relative target instead of recalculating it from the skill's location.

## Reference

Make reference material exhaustive, precise, and predictable. Organize commands, fields, types, defaults, constraints, and errors so readers can retrieve exact facts quickly.

Reference completeness does not justify copying tables into an operational guide. Keep the authoritative detail here and link to it at the point of need.

## Choose the Dominant Purpose

| Reader question | Dominant purpose |
|---|---|
| What is this, what can I do, and where do I begin? | Orientation |
| How does this part work, and why is it shaped this way? | Conceptual explanation |
| How do I accomplish this goal safely? | Operational guidance |
| What exact commands, fields, defaults, constraints, or errors exist? | Reference |
