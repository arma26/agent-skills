## Review findings

1. **Critical — The onboarding path is incorrect for the primary reader.** The README tells new users to clone the monorepo and install contributor tooling, although released binaries require none of this. Lead with binary installation and move source setup to `CONTRIBUTING.md`.

2. **Critical — The first publish workflow lacks a safe progression.** Show validation first: `nimbus send order.created --data order.json --dry-run`. Then explicitly explain that removing `--dry-run` publishes the event.

3. **High — The introduction obscures the product’s purpose.** Terms such as “event-processing seam” and “circuit-breaker architecture” do not help a new user evaluate Nimbus. Begin with what Nimbus does, who it serves, and its practical benefit.

4. **High — Command documentation overwhelms the evaluation path.** Summarizing 37 flags distracts from the common task. Document the essential arguments and link to `docs/reference/send.md` for the complete reference.

5. **High — Failure behavior is undocumented.** “Refer to the source for errors” is unsuitable for binary users. Describe common errors, exit behavior, troubleshooting steps, and where users can find complete error documentation.

6. **Medium — Delivery semantics are ambiguous.** “Acknowledged eventually” does not establish what acknowledgment means, when it occurs, or what happens after timeouts and retries. State the guarantees and failure boundaries precisely.

7. **Medium — Contributor instructions interrupt user onboarding.** Golden-file and benchmark guidance belongs in `CONTRIBUTING.md`; the README should link there rather than presenting those tasks as setup requirements.
