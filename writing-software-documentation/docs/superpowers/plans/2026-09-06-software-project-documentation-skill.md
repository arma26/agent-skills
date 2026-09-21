# Software Project Documentation Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and validate a reusable skill that produces user-focused software documentation with clear system models, concise operational examples, and links to complete reference material.

**Architecture:** Keep the executable workflow in a concise root `SKILL.md` and move document patterns and review criteria into two focused references. Test the behavior with repository-local scenario prompts and captured baseline/skill-enabled outputs; use the standard skill validator for structural checks. Record the reader-journey decision in one accepted ADR because it governs future changes to the skill.

**Tech Stack:** Markdown, YAML, Git, Codex skills, repository-local evaluation artifacts

**Spec:** `docs/superpowers/specs/2026-09-06-software-project-documentation-skill-design.md`

**Reasoning map:** `docs/reasoning-maps/software-project-documentation-skill.json`

## Global Constraints

- Default to software users and operators; keep contributor and maintainer material separate.
- Organize guidance around a reader goal and the smallest system model needed to act.
- Pair every meaningful operation with an explanation, concise example, and expected result.
- Put exhaustive commands, fields, options, schemas, and errors in linked reference material.
- Derive technical claims from repository evidence and disclose anything that cannot be verified.
- Do not run destructive or external-state operations solely to verify documentation.
- Use repository-relative paths in committed documentation and examples.
- Add no runtime dependency, documentation framework, or validation script.
- Keep `SKILL.md` concise; place detailed document patterns and review criteria in `references/`.
- Every implementation or review subagent must read the reasoning map and the narrowest task section before acting; evaluation agents must not receive the map because it reveals intended failures.

## Planned File Structure

```text
SKILL.md                                      # Trigger and executable workflow
agents/openai.yaml                            # Skill-list metadata
references/document-patterns.md               # Guidance by document purpose
references/review-rubric.md                   # Create, revise, and review checks
docs/decisions/README.md                      # ADR index and convention
docs/decisions/reader-journey-documentation.md # Accepted architecture decision
docs/reasoning-maps/software-project-documentation-skill.json # Subagent decision context
tests/scenarios/database-backups.md           # Operational lifecycle pressure scenario
tests/scenarios/cli-quick-start.md             # Orientation versus reference scenario
tests/scenarios/api-integration.md             # Evidence, safety, and failure scenario
tests/scenarios/mixed-audience-review.md       # Review-mode audience scenario
tests/evaluations/baseline/*.md                # Unedited outputs without the skill
tests/evaluations/with-skill/*.md              # Unedited outputs using the skill
tests/evaluations/scorecard.md                 # Comparative findings and rationalizations
```

`SKILL.md` is the only mandatory read. Each reference has one responsibility and is linked directly from `SKILL.md`. Evaluation artifacts remain outside the runtime skill surface.

---

### Task 1: Establish RED baseline scenarios

**Files:**

- Create: `tests/scenarios/database-backups.md`
- Create: `tests/scenarios/cli-quick-start.md`
- Create: `tests/scenarios/api-integration.md`
- Create: `tests/scenarios/mixed-audience-review.md`
- Create: `tests/evaluations/baseline/database-backups.md`
- Create: `tests/evaluations/baseline/cli-quick-start.md`
- Create: `tests/evaluations/baseline/api-integration.md`
- Create: `tests/evaluations/baseline/mixed-audience-review.md`
- Create: `tests/evaluations/scorecard.md`

**Interfaces:**

- Consumes: the failure modes and acceptance criteria in the approved specification plus the task boundary in the reasoning map.
- Produces: four stable prompts, four unedited baseline responses, and a scored account of failures that Task 2 must address.

- [x] **Step 1: Write the database lifecycle scenario**

Create `tests/scenarios/database-backups.md` with this exact task evidence:

```markdown
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
```

- [x] **Step 2: Write the CLI quick-start scenario**

Create `tests/scenarios/cli-quick-start.md`:

```markdown
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
```

- [x] **Step 3: Write the API integration scenario**

Create `tests/scenarios/api-integration.md`:

```markdown
# Scenario: API integration

Document how an application submits a payment to the Finch API.

Repository evidence:

- Clients send `POST /v1/payments` with a bearer token and an `Idempotency-Key` header.
- A successful request returns `202 Accepted` and a payment identifier; processing continues asynchronously.
- Clients inspect `GET /v1/payments/{id}` until the status is `settled` or `failed`.
- Repeating a POST with the same idempotency key returns the original payment instead of creating another.
- `429` and `503` responses may be retried with exponential backoff; other `4xx` responses must not be retried automatically.
- The OpenAPI document is authoritative for fields and response schemas.

Primary reader: an application developer making their first production integration.
```

- [x] **Step 4: Write the mixed-audience review scenario**

Create `tests/scenarios/mixed-audience-review.md`:

```markdown
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
```

- [x] **Step 5: Run all four scenarios without the skill**

Dispatch each scenario in a fresh context without exposing the design specification, reasoning map, scorecard, or expected failure modes. Request Markdown output only and prohibit file changes. Save each unedited response under the matching path in `tests/evaluations/baseline/`.

Expected RED result: at least one response omits a necessary system model, lacks an example or expected result, mixes audiences, duplicates reference detail, asserts unsupported behavior, or buries safety and recovery guidance. If none fails, strengthen the scenario pressure before implementing the skill.

- [x] **Step 6: Score and record the baseline failures**

Create `tests/evaluations/scorecard.md` with one row per scenario and these columns:

```markdown
| Scenario | Reader goal first | System model | Operation + example + result | Reference separated | Evidence bounded | Safety/recovery | Audience separated | Editorial clarity |
|---|---|---|---|---|---|---|---|---|
```

Score each cell `pass` or `fail`. Below the table, quote the specific baseline sentence or omission that justifies every failure and record any agent rationalization verbatim. Do not add the desired rewritten answer.

- [x] **Step 7: Commit the RED artifacts**

```bash
git add tests/scenarios tests/evaluations
git commit -m "Add baseline documentation skill scenarios" -m "- Define lifecycle, quick-start, API, and review prompts
- Capture unedited no-skill responses
- Score observed reader-journey and evidence failures"
```

---

### Task 2: Implement the skill and architecture record

**Files:**

- Create: `SKILL.md`
- Create: `agents/openai.yaml`
- Create: `references/document-patterns.md`
- Create: `references/review-rubric.md`
- Create: `docs/decisions/README.md`
- Create: `docs/decisions/reader-journey-documentation.md`

**Interfaces:**

- Consumes: the exact failures recorded in `tests/evaluations/scorecard.md`, the approved specification, and the accepted decisions and constraints in the reasoning map.
- Produces: `$writing-software-documentation`, two directly linked references, discoverable UI metadata, and the accepted decision governing all four files.

- [x] **Step 1: Initialize the skill scaffold without nesting the deliverable**

Confirm that `SKILL.md`, `agents/`, and `references/` do not exist at the repository root. If any exists, stop and inspect it instead of overwriting it.

Run the `init_skill.py` command supplied by `skill-creator` with these arguments:

```text
writing-software-documentation --path .skill-scaffold --resources references
--interface display_name="Software Documentation Writer"
--interface short_description="Write usable, evidence-based software documentation"
--interface default_prompt="Use $writing-software-documentation to create or revise user-focused software documentation with clear concepts, examples, and reference links."
```

Move the generated `SKILL.md`, `agents/`, and `references/` from `.skill-scaffold/writing-software-documentation/` to the repository root. Remove only the now-empty scaffold directories with `rmdir`; do not use recursive deletion. This satisfies the required initializer while keeping the repository root itself as the installable skill directory.

- [x] **Step 2: Record the accepted architecture decision**

Create `docs/decisions/README.md` with the directory purpose, statuses (`proposed`, `accepted`, `rejected`, `deprecated`, `superseded`), and a link to `reader-journey-documentation.md` marked `accepted`.

Create `docs/decisions/reader-journey-documentation.md` using the simple ADR form with these substantive sections:

- **Status:** Accepted on 2026-09-06.
- **Context:** unconstrained LLM documentation tends to lead with detail, mix audiences, omit usable examples, and optimize prose without fixing information architecture.
- **Decision:** organize the skill around user/operator journeys; require the smallest useful system model; pair meaningful operations with examples and expected results; keep exhaustive material in linked references; use the article's rules as a final editorial pass.
- **Alternatives:** rigid templates were rejected as formulaic; an editorial-only pass was rejected because it cannot repair the wrong reader journey.
- **Consequences:** the skill needs evidence inspection, safety boundaries, separate document-pattern guidance, behavioral scenarios, and maintenance checks; some pages may need splitting.
- **Non-goals:** no documentation framework, runtime dependency, screenshots by default, or deterministic prose linter.
- **Implementation plan:** name the six files in this task and the scenario/evaluation paths in Task 1.
- **Verification:** repeat the acceptance questions from the specification as checkboxes and require standard skill validation.

- [x] **Step 3: Write the minimal executable workflow**

Create `SKILL.md` with this frontmatter:

```yaml
---
name: writing-software-documentation
description: Use when creating, revising, or reviewing repository documentation for software users and operators, especially README files, quick starts, conceptual guides, operational procedures, troubleshooting pages, and linked reference material.
---
```

Keep the body under 500 lines and write instructions in imperative form. Include:

1. A two-sentence overview stating that reader understanding and safe action outrank completeness in the main journey.
2. Guard clauses for unclear audience/goal, conflicting evidence, unsafe verification, and mixed page purposes.
3. The workflow: establish reader and goal; gather evidence; classify the dominant document purpose; build the reader journey; write concepts before mechanics; pair meaningful operations with examples and results; verify safely; edit; inspect connected docs.
4. The operation pattern `explanation → prerequisites/risks → concise example → expected result/verification → failure/recovery → reference links`.
5. Direct instructions to read `references/document-patterns.md` when choosing or structuring a document and `references/review-rubric.md` before finalizing or reviewing one.
6. A compact completion checklist covering audience, system model, examples, evidence, safety, reference separation, terminology, and connected documentation.
7. A red-flags list addressing the exact baseline failures from Task 1.

Do not add a generic “When to use” body section; discovery information belongs in the description.

- [x] **Step 4: Write document-pattern guidance**

Create `references/document-patterns.md` with a table of contents and four sections:

- **Orientation:** outcome, smallest useful model, safe first success, expected result, next destinations. Exclude build-from-source instructions for users of released artifacts.
- **Conceptual explanation:** responsibilities, boundaries, lifecycle/data flow, invariants, and links to operations. Avoid source walkthroughs unless implementation is the subject.
- **Operational guidance:** the required operation pattern, criteria for meaningful extensions, proportional failure/recovery guidance, and an AcornDB example showing create, inspect, safe restore, and a link to command reference.
- **Reference:** exhaustive and predictably structured commands, fields, types, defaults, constraints, and errors. State that reference completeness does not justify copying tables into operational guides.

End with a short decision table mapping reader questions to the dominant document purpose.

- [x] **Step 5: Write the review rubric**

Create `references/review-rubric.md` with separate `Create`, `Revise`, and `Review` sections plus a common evidence checklist.

Require review findings to be ordered by reader harm:

1. unsafe or technically false instructions;
2. inability to complete or verify the primary task;
3. missing system model or prerequisites;
4. audience mixing and misplaced reference detail;
5. terminology, scanning, and prose defects.

For every finding, require the location, reader impact, supporting evidence, and a concrete direction. Require revision mode to preserve correct content while changing hierarchy. Require create mode to name the intended reference destinations before duplicating detail.

- [x] **Step 6: Confirm skill metadata**

Confirm that the initializer generated `agents/openai.yaml` with exactly these values; regenerate it through the `skill-creator` metadata generator if the file differs:

```yaml
interface:
  display_name: "Software Documentation Writer"
  short_description: "Write usable, evidence-based software documentation"
  default_prompt: "Use $writing-software-documentation to create or revise user-focused software documentation with clear concepts, examples, and reference links."
```

Do not add icons, colors, dependencies, or invocation policy.

- [x] **Step 7: Validate structure and links**

Run the `quick_validate.py` command supplied by `skill-creator` with `.` as the target. Expected: validation succeeds.

Run:

```bash
rg -n 'TB[D]|TO[D]O|FIXM[E]|file:/{2}' SKILL.md agents references docs/decisions
```

Expected: no matches.

Inspect every Markdown link in `SKILL.md`, `references/`, and `docs/decisions/`; confirm each repository-relative target exists and each external link uses HTTPS.

- [x] **Step 8: Commit the GREEN implementation**

```bash
git add SKILL.md agents references docs/decisions
git commit -m "Add the software documentation writing skill" -m "- Center user and operator journeys
- Pair meaningful operations with verified examples
- Separate conceptual, operational, and reference guidance
- Record the governing architecture decision"
```

---

### Task 3: Forward-test and close behavioral gaps

**Files:**

- Create: `tests/evaluations/with-skill/database-backups.md`
- Create: `tests/evaluations/with-skill/cli-quick-start.md`
- Create: `tests/evaluations/with-skill/api-integration.md`
- Create: `tests/evaluations/with-skill/mixed-audience-review.md`
- Modify: `tests/evaluations/scorecard.md`
- Modify if required by observed failures: `SKILL.md`
- Modify if required by observed failures: `references/document-patterns.md`
- Modify if required by observed failures: `references/review-rubric.md`

**Interfaces:**

- Consumes: `$writing-software-documentation`, the unchanged scenario prompts from Task 1, and the evaluation-isolation constraint from the reasoning map.
- Produces: unedited skill-enabled outputs, comparative scores, and minimal wording changes tied to observed failures.

- [x] **Step 1: Run the same scenarios with the skill**

Dispatch each scenario in a fresh context. Instruct the agent to use `$writing-software-documentation` from the repository root, output Markdown only, and make no file changes. Do not reveal the reasoning map, scorecard, or intended answer. Save each unedited response under the matching path in `tests/evaluations/with-skill/`.

- [x] **Step 2: Score the skill-enabled outputs**

Add a second table to `tests/evaluations/scorecard.md` using the same columns and scoring rules as the baseline. Cite specific output evidence for every result.

Expected GREEN result: all safety, evidence, audience, example, and expected-result cells pass; each system-model and reference-separation cell passes without the output becoming an exhaustive manual.

- [x] **Step 3: Refactor only observed gaps**

For each failed cell, identify the agent's wording or rationale, make the smallest corresponding change to `SKILL.md` or one reference, and rerun only the affected scenario in a fresh context. Append the replacement unedited output and rescore it. Do not add hypothetical rules unsupported by a scenario failure.

- [x] **Step 4: Record rationalizations and red flags**

Update the scorecard with a table containing `Observed rationalization`, `Why it harms the reader`, and `Skill counter`. Ensure each remaining rationalization appears in `SKILL.md` as a concise red flag or explicit guard clause.

- [x] **Step 5: Re-run structural validation**

Run the `quick_validate.py` command supplied by `skill-creator` against `.`. Recheck repository-relative links and rerun the forbidden-path scan from Task 2.

- [x] **Step 6: Commit verified behavioral changes**

```bash
git add SKILL.md references tests/evaluations
git commit -m "Validate the documentation skill behavior" -m "- Compare baseline and skill-enabled scenario outputs
- Close observed reader-journey and safety gaps
- Record evaluation evidence and rationalizations"
```

---

### Task 4: Final documentation, security, and repository verification

**Files:**

- Modify: `docs/decisions/reader-journey-documentation.md`
- Modify if findings require it: `SKILL.md`
- Modify if findings require it: `references/document-patterns.md`
- Modify if findings require it: `references/review-rubric.md`

**Interfaces:**

- Consumes: the validated skill, evaluation evidence, specification, plan, reasoning map, and accepted ADR.
- Produces: a security-reviewed, structurally valid, internally consistent repository with verification recorded in the ADR.

- [x] **Step 1: Review specification coverage**

Walk every goal, non-goal, workflow requirement, safety rule, error guard, maintenance rule, and acceptance criterion in the specification. Record the implementing file and section. Fix any uncovered requirement before continuing.

- [x] **Step 2: Run the required security review**

Use `security-reviewer` against the verified skill and evaluation diff. Focus on unsafe example execution, destructive commands, secret or identity leakage, machine-specific paths, unsupported claims, prompt injection from repository content, external-state mutation, and ambiguity around dry-run behavior. Fix confirmed findings and rerun affected scenarios.

- [x] **Step 3: Run the required code and documentation review**

Use `superpowers:requesting-code-review` to compare the implementation with the approved specification and repository instructions. Include `SKILL.md`, both references, the ADR, and evaluation artifacts. Fix confirmed findings and repeat validation after every material change.

- [x] **Step 4: Record verification in the ADR**

Add a dated `More Information` entry to `docs/decisions/reader-journey-documentation.md` naming:

- the standard validator result;
- the baseline and skill-enabled scenario result counts;
- any accepted limitations;
- the commit that contains the final implementation.

Do not rewrite the original decision or consequences.

- [x] **Step 5: Run final verification**

Run the standard skill validator against `.` and confirm success. Then run:

```bash
git diff --check
rg -n 'TB[D]|TO[D]O|FIXM[E]|file:/{2}' SKILL.md agents references docs tests
git status --short
```

Expected: `git diff --check` exits zero; the scan returns no matches; status lists only the intended ADR verification or review fixes.

- [x] **Step 6: Commit the final verification record**

```bash
git add SKILL.md references docs/decisions tests/evaluations
git commit -m "Complete documentation skill verification" -m "- Resolve security and specification review findings
- Record final scenario and validator evidence
- Confirm documentation and ADR consistency"
```

- [x] **Step 7: Verify the committed repository**

Run:

```bash
git status --short
git log -5 --oneline
```

Expected: working tree output is empty and recent history contains the baseline, implementation, behavioral validation, and final verification commits.
