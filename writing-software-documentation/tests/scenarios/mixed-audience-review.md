# Scenario: Review mixed-audience documentation

Review the following README without editing it. Report findings in priority order.

> Nimbus is a highly extensible event-processing seam leveraging a circuit-breaker architecture. Clone the monorepo, install the compiler toolchain, run the code generator, and execute the internal benchmark suite. Users can publish an event with `nimbus send`. The command accepts 37 flags covering serialization, batching, credentials, timeouts, retries, and output. Contributors must update golden files before merging. Events enter a local queue, are sent to the configured broker, and are acknowledged eventually. Refer to the source for errors.

Repository evidence:

- Released binaries are available; users do not need the source toolchain.
- `nimbus send order.created --data order.json --dry-run` validates an event without publishing it.
- Removing `--dry-run` publishes the event.
- Complete flags live in `docs/reference/send.md`.
- Contributor checks live in `CONTRIBUTING.md`.

Primary reader: a new user evaluating Nimbus.
