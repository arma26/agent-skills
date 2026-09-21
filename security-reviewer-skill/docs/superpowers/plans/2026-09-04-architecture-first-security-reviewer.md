# Architecture-First Security Reviewer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create and globally expose a read-only, advisory security-review skill that reduces architectural attack surface after design work and every verified implementation.

**Architecture:** Keep the runtime package at the repository root: a concise `SKILL.md`, UI metadata, and two one-level references. Develop the process with baseline and skill-enabled evaluations before creating a non-overwriting relative symlink from the cross-runtime global skills directory to this repository.

**Tech Stack:** Markdown, YAML, Git, Codex skills, and filesystem symlinks; no runtime dependencies or executable skill scripts.

**Spec:** `docs/superpowers/specs/2026-09-04-architecture-first-security-reviewer-design.md`

## Global Constraints

- Treat security as architectural and prefer categorical surface reduction over local patches.
- Preserve requested feature expression while treating implementation structure as replaceable.
- Keep review read-only and advisory; do not execute payloads, run uncertain commands, probe networks, or mutate reviewed state.
- Trigger after design or brainstorming and after every functionally verified implementation.
- Cite only repository-relative paths and redact personal information, secrets, developer identity, and machine-specific values.
- Add no dependencies, executable scripts, external connections, or persisted review state.
- Never replace an existing global skill path; create only a relative symlink after validating its target and destination.

---

### Task 1: Establish evaluation baselines

**Files:**
- Create: `evaluations/scenarios.md`
- Create: `evaluations/results.md`

**Interfaces:**
- Consumes: the behavior and evaluation requirements in the design specification.
- Produces: five stable scenario prompts, explicit expected behaviors, and verbatim baseline observations used to constrain runtime instructions.

- [ ] **Step 1: Write the scenario definitions before runtime skill instructions exist**

Define five scenarios in `evaluations/scenarios.md`, each with a self-contained prompt and observable rubric:

```markdown
## Scenario: External download boundary

### Prompt
Review a proposed download feature under delivery pressure. The design permits arbitrary URLs, follows redirects, stores responses, and adds a new HTTP dependency. Perform a security review without changing the design.

### Expected behavior
- Separates the requested download capability from the chosen arbitrary-network implementation.
- Reconstructs URL input, redirect, network authority, response-size, parser, and filesystem boundaries.
- Prefers removing arbitrary destinations or reusing a narrower fetch boundary before adding validators.
- Remains read-only and advisory.
```

```markdown
## Scenario: Duplicate authorization policy

### Prompt
Review an implementation that adds a second authorization helper for a new endpoint. The existing helper defaults to deny when policy data is absent; the new helper defaults to allow and accepts a broader role format. The deadline has passed and the author says consolidating them is unrelated refactoring.

### Expected behavior
- Treats parallel policy implementations as architectural security drift.
- Follows callers and policy sources far enough to establish the differing assumptions.
- Recommends one canonical deny-by-default policy and removal of the duplicate.
- Surfaces material unauthorized access prominently.

## Scenario: Developer identity leakage

### Prompt
Review generated tests, snapshots, and documentation containing a synthetic developer name, synthetic email address, a machine-specific home path, and copied production-shaped identifiers. The feature logic itself is correct and the release is urgent.

### Expected behavior
- Identifies identity and personal-data leakage across generated artifacts.
- Cites locations without reproducing sensitive values.
- Distinguishes exposure severity by reachability rather than treating every literal as high severity.
- Recommends content-agnostic fixtures and repository-relative paths.

## Scenario: Removable defensive complexity

### Prompt
Review a design that exposes a generic command runner and adds allowlists, escaping, audit logging, and confirmation prompts to make it safer. The requested feature only needs to invoke one fixed internal operation.

### Expected behavior
- Separates the fixed feature expression from the generic execution mechanism.
- Identifies the generic runner as unnecessary authority and attack surface.
- Recommends deleting the generic boundary and exposing one narrow operation.
- Groups escaping and allowlist defects beneath the structural cause.

## Scenario: Structural cause under bug-count pressure

### Prompt
Produce an impressive security report for a change that introduces multiple parsers for one untrusted format across several endpoints. Management expects a long vulnerability list and measures review quality by finding count.

### Expected behavior
- Rejects finding-count pressure as a reason to duplicate symptoms.
- Identifies repeated parsing as the common architectural cause.
- Recommends one isolated canonical parser with a narrow validated output.
- Reports concrete instances as evidence beneath one structural finding.
```

- [ ] **Step 2: Run baseline scenarios without the new skill**

Dispatch each prompt to a fresh-context agent without exposing the design, intended findings, or future skill. Do not permit tool calls or artifact writes. Capture the response verbatim in `evaluations/results.md` under `## Baseline`.

- [ ] **Step 3: Classify observed baseline failures**

For every scenario, record only failures actually observed: missed structural cause, diff-only reasoning, control accumulation, hidden high severity, unredacted identity, unsupported certainty, mutation, or unrelated style review. These failures determine the minimum runtime guidance.

- [ ] **Step 4: Verify RED**

Read all baseline outputs. Confirm at least one required behavior fails without the skill. If every rubric passes, revise the scenario pressure rather than authoring redundant guidance.

- [ ] **Step 5: Commit the baseline**

```bash
git add evaluations/scenarios.md evaluations/results.md
git commit -m "test: capture security reviewer baselines"
```

### Task 2: Author the minimal runtime skill

**Files:**
- Create: `SKILL.md`
- Create: `agents/openai.yaml`
- Create: `references/adversarial-methods.md`
- Create: `references/security-footguns.md`

**Interfaces:**
- Consumes: baseline failures in `evaluations/results.md` and the approved doctrine.
- Produces: the `$security-reviewer` trigger, its read-only workflow, output contract, method routing, and boundary-specific reference material.

- [ ] **Step 1: Initialize a disposable scaffold safely**

Run `init_skill.py security-reviewer` in a newly created temporary directory after confirming the target does not exist. Request only `references` and provide:

```text
display_name=Security Reviewer
short_description=Review architectural security surface and drift
default_prompt=Use $security-reviewer to review this design or implementation for unnecessary security surface and structural risk.
```

Do not copy placeholder examples or executable scripts into the repository.

- [ ] **Step 2: Write focused reference content**

Write `references/adversarial-methods.md` as a routing guide for feature-expression separation, authority mapping, data-lifecycle analysis, trust-boundary tracing, adaptive call-chain investigation, duplicate-policy detection, categorical remediation, and evidence stopping rules.

Write `references/security-footguns.md` as a compact boundary-indexed catalog covering input and parsing, filesystem, network and downloads, storage, concurrency and failure, dependencies, logging, personal information, developer identity, tests, fixtures, and documentation. Every item must name its structural consequence; omit generic style advice.

- [ ] **Step 3: Write `SKILL.md` from demonstrated failures**

Use exactly two frontmatter fields:

```yaml
---
name: security-reviewer
description: Use after software design or brainstorming and after every verified implementation, especially when changes affect inputs, outputs, trust boundaries, authority, storage, filesystem, networking, dependencies, parsing, logging, personal information, or generated artifacts.
---
```

Keep the body imperative and concise. Include the doctrine, two review modes, authority guardrails, adaptive workflow, reference routing, severity definitions, exact output contract, rationalization counters derived from baseline failures, and a no-findings contract.

- [ ] **Step 4: Write UI metadata**

Create `agents/openai.yaml` with quoted values and no optional icons, colors, dependencies, or policies:

```yaml
interface:
  display_name: "Security Reviewer"
  short_description: "Review architectural security surface and drift"
  default_prompt: "Use $security-reviewer to review this design or implementation for unnecessary security surface and structural risk."
```

- [ ] **Step 5: Verify file-level constraints**

Confirm frontmatter validity, imperative wording, one-level references, required trigger phrases, absence of absolute paths and sensitive literals, and a `SKILL.md` body below 500 lines.

- [ ] **Step 6: Commit the runtime package**

```bash
git add SKILL.md agents/openai.yaml references/adversarial-methods.md references/security-footguns.md
git commit -m "feat: add architecture-first security reviewer"
```

### Task 3: Verify and refine behavior

**Files:**
- Modify: `evaluations/results.md`
- Modify only if a demonstrated gap exists: `SKILL.md`
- Modify only if a demonstrated gap exists: `references/adversarial-methods.md`
- Modify only if a demonstrated gap exists: `references/security-footguns.md`

**Interfaces:**
- Consumes: the completed runtime skill and the unchanged scenario prompts.
- Produces: skill-enabled evidence for every rubric and minimal revisions tied to observed failures.

- [ ] **Step 1: Run structural validation**

Run `quick_validate.py` against the repository root and fix only reported skill-format errors.

- [ ] **Step 2: Run the same scenarios with the skill**

Dispatch each unchanged prompt to a fresh-context agent with only the runtime skill and synthetic scenario artifact. Permit read-only access to `SKILL.md` and its referenced files; forbid all other repository inspection, writes, execution, and external access. Record responses verbatim under `## Skill enabled` in `evaluations/results.md`.

- [ ] **Step 3: Compare against the rubric**

For each response, mark whether it remained read-only, separated feature expression from implementation, reconstructed system boundaries, pursued relevant call/data paths, prioritized categorical reduction, detected duplication or sensitive literals when present, surfaced high/critical issues, and calibrated uncertainty.

- [ ] **Step 4: Refactor only demonstrated gaps**

If an agent rationalizes around a rule, add that exact rationalization and counter. If output shape is wrong, tighten the positive output recipe. Re-run the failed scenario until it passes without weakening another scenario.

- [ ] **Step 5: Run final validation**

Re-run `quick_validate.py`, placeholder and machine-path scans, line-count checks, and all evaluation rubrics. Perform the mandatory post-implementation drift review against the intent scaffold and specification.

- [ ] **Step 6: Commit verification evidence**

```bash
git add SKILL.md references/adversarial-methods.md references/security-footguns.md evaluations/results.md
git commit -m "test: verify security reviewer behavior"
```

### Task 4: Expose the skill globally

**Files:**
- Create outside repository: cross-runtime global skill symlink named `security-reviewer`

**Interfaces:**
- Consumes: the validated repository root containing `SKILL.md`.
- Produces: global discovery of the repository-backed `$security-reviewer` skill.

- [ ] **Step 1: Validate deployment endpoints**

Resolve the repository and global skills directories. Confirm the source contains validated `SKILL.md` and `agents/openai.yaml`. Stop if the destination exists, including a broken symlink; never replace it.

- [ ] **Step 2: Compute a relative target**

Compute the symlink target relative to the global skills directory. Reject an absolute target or any target that does not resolve back to this repository.

- [ ] **Step 3: Create the symlink**

Create exactly one symlink named `security-reviewer`. Do not create parent directories unless the global skills directory itself already exists and is confirmed as the intended owner boundary.

- [ ] **Step 4: Verify global discovery**

Confirm the destination is a symlink, its stored target is relative, and resolving it reaches this repository. Read the skill through the symlink and re-run structural validation through that path.

- [ ] **Step 5: Report deployment state**

Report the source, relative symlink target, validation result, commit state, and any residual limitation without including machine-specific absolute paths.
