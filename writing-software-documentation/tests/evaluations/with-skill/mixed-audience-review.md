1. **Unsafe primary operation — “Users can publish an event with `nimbus send`.”**
   The new user receives neither a runnable example nor warning that sending publishes externally. Repository evidence provides a safe evaluation path: `nimbus send order.created --data order.json --dry-run`. Lead with that command, explain that it validates without publishing, and state the expected validation result. Describe removing `--dry-run` as the publishing step with an adjacent risk warning. The evidence does not establish publish verification or recovery, so do not invent either.

2. **The primary task cannot be completed or troubleshot — “Refer to the source for errors.”**
   This gives users no expected result, verification method, likely failure guidance, or actionable recovery path. Document evidence-backed validation outcomes and common recovery steps, or explicitly state that recovery behavior is undocumented and link to an appropriate user-facing troubleshooting reference. Source code is not adequate operational guidance for a new user.

3. **The opening sends users through an unnecessary contributor workflow — “Clone the monorepo, install the compiler toolchain, run the code generator, and execute the internal benchmark suite.”**
   Released binaries are available, so these prerequisites obstruct rather than enable evaluation. Replace this sequence with installation from a released binary and the safe dry-run journey. Move source builds and benchmarks to `CONTRIBUTING.md`.

4. **The system model is unclear and unsupported — “highly extensible event-processing seam leveraging a circuit-breaker architecture” and “acknowledged eventually.”**
   The jargon does not tell a new user what Nimbus does, while the supplied evidence does not establish the queue, broker, circuit-breaker, or eventual-acknowledgment claims. Open with a plain description of the user outcome and retain lifecycle claims only after tracing them to repository evidence. Avoid an acknowledgment guarantee unless its conditions and observable meaning are documented.

5. **Contributor instructions interrupt the user journey — “Contributors must update golden files before merging.”**
   This is irrelevant to the stated primary reader and mixes maintainer obligations into product orientation. Remove it from the README’s main journey and link contributors to `CONTRIBUTING.md`.

6. **Reference detail is summarized without routing readers to its authority — “The command accepts 37 flags…”**
   The count is brittle and does not help a new user choose the few options needed for first success. Show only the flags used by the safe example and link to `docs/reference/send.md` for the complete command reference.
