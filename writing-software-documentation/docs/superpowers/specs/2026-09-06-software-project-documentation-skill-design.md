# Software Project Documentation Skill Design

## Status

Implemented and verified on 2026-09-06. The accepted residual limitation is that the adversarial GREEN execution control passes in 4/5 repetitions; the static-first skill rule remains authoritative.

## Purpose

Create a reusable skill that helps an agent write, revise, and review software project documentation for users and operators.

The skill must optimize for a reader who wants to understand enough of the system to complete a real task. It must not treat documentation as a dump of implementation details, commands, or configuration options.

The design incorporates the useful editorial rules from Andi Miller's article, [LLMs are bad at Technical Writing](https://andimiller.net/posts/2026-09-02-llms-and-technical-writing.html), but uses them as an editing discipline rather than the document's organizing principle.

## Primary Reader

The default reader is a person using or operating the software.

Contributor and maintainer concerns are secondary. Place them in separate documents or clearly separated sections and link to them when relevant. Do not interrupt the primary user journey with build internals, repository conventions, release processes, or implementation details.

If a repository defines a different audience, documentation doctrine, terminology guide, or information architecture, follow that local doctrine after checking that it is internally consistent.

## Goals

The skill must help an agent produce documentation that:

- starts from a concrete reader goal;
- explains the system model needed to understand that goal;
- pairs every meaningful operation with a concise example and expected result;
- covers meaningful extensions without turning the main guide into a reference manual;
- makes failure, safety, and recovery information visible where it matters;
- links to complete reference material for deeper inspection;
- derives technical claims from repository evidence;
- uses direct, concise, consistent, and scannable prose;
- challenges every passage against an identifiable reader capability or understanding before retaining it; and
- updates documentation affected by changes to software behavior.

## Non-goals

The skill will not:

- introduce a documentation framework or dependency into a repository;
- prescribe one universal document layout regardless of reader or task;
- replace complete API, configuration, schema, or command reference material;
- generate screenshots or diagrams by default;
- test destructive operations or modify external systems merely to verify examples;
- invent missing behavior, defaults, guarantees, or outcomes; or
- mix contributor documentation into the main user or operator journey for convenience.

## Supported Actions

### Create

Write new repository-native Markdown documentation using verified repository evidence and the reader-journey structure.

### Revise

Restructure or edit existing documentation while preserving correct information, repository conventions, and intentional scope.

### Review

Assess documentation without changing it. Report findings in priority order and connect each finding to reader impact, technical accuracy, or maintainability.

After accuracy and structure pass, run a separate adversarial subtraction review. Classify challenged passages as keep, compress, relocate, or remove. Require an explicit account of what reader capability, decision, safety property, understanding, or navigation would be lost if the passage disappeared. Do not use a numeric reduction target as a substitute for this judgment.

## Documentation Model

The skill distinguishes four kinds of documentation. A page may link between kinds, but should have one dominant purpose.

### Orientation

Answers: What is this software, what does it enable, and where should I begin?

Orientation establishes the smallest useful system model and directs the reader toward a primary task.

### Conceptual explanation

Answers: How does this part of the system work, and why is it shaped this way?

Conceptual material explains components, responsibilities, boundaries, and lifecycle or data flow. It should include only the detail needed to understand relevant operations.

### Operational guidance

Answers: How do I accomplish a user goal safely?

Every meaningful operation follows this pattern:

1. Explain the operation and where it fits in the system.
2. State prerequisites, assumptions, and material risks.
3. Show one concise, realistic example.
4. Describe the expected result and how to verify it.
5. Explain likely failure and recovery when the consequences matter.
6. Link to relevant concepts and complete reference material.

Meaningful extensions repeat the explanation, example, and expected-result pattern. Include an extension when it represents a common user goal, changes safety or behavior materially, or requires a different mental model. Otherwise, link to reference material.

### Reference

Answers: What are the exact available commands, fields, options, schemas, types, defaults, constraints, or error forms?

Reference material favors completeness, precision, and predictable organization. Operational guides link to it at the point where a reader may need more control; they do not reproduce it wholesale.

## Default Reader Journey

Use this hierarchy as a decision model, not a rigid page template:

```text
User goal
├── What this enables
├── Relevant system model
├── Primary operation
│   ├── Explanation and prerequisites
│   ├── Concise example
│   └── Expected result and verification
├── Meaningful extensions
│   └── Explanation → example → expected result
├── Failure and recovery guidance
└── Links to reference and adjacent concepts
```

Lead with the outcome and the knowledge needed to act. Avoid long product framing, generic benefits, historical narrative, and implementation detail before the first useful path.

## Evidence Workflow

Before writing, revising, or reviewing:

1. Read repository instructions and documentation conventions.
2. Identify the requested reader, goal, and document type.
3. Statically inspect the code, configuration, CLI help, tests, examples, and existing documentation that define the behavior.
4. Map each material claim to a source of truth.
5. Identify related documentation that may become inconsistent.

Prefer primary repository evidence over inference. If sources disagree, report the conflict instead of selecting the most convenient version silently. If evidence is missing, narrow the claim or mark it for confirmation.

Minimize evidence inputs. Avoid known secret-bearing files and full configuration dumps; prefer schemas, examples, or targeted redacted fields.

## Verification and Safety

Default to static inspection. Do not execute repository-owned code solely for documentation verification. A `--dry-run` name, test target, local destination, disposable fixture, or repository script is not evidence of safety.

Execute only after independently establishing that the exact command and its transitive hooks are non-mutating, removing network and credential access, containing execution in a disposable environment, and retaining all surrounding authorization requirements. Verification should establish that commands are syntactically valid, examples use current interfaces, and described results match observable behavior.

Clearly identify anything that could not be verified and why. Never transform an assumption into an asserted fact during editing.

Examples must:

- avoid machine-specific absolute paths, identities, secrets, and unexplained identifiers;
- use repository-relative paths when describing repository content;
- use placeholders only when their required replacement is obvious;
- show safe defaults where alternatives differ in risk; and
- remain concise enough that the operation is visible at a glance.

## Editorial Pass

After structure and accuracy are sound, apply these constraints:

- Prefer familiar, specific words over decorative jargon.
- Define necessary specialist terms at first use or link to their definition.
- Prefer direct sentences and active voice when they make responsibility clearer.
- Replace a paragraph with a sentence when no meaning is lost.
- Use headings, lists, tables, and diagrams only when they improve navigation or comprehension.
- Keep terminology, capitalization, spelling convention, and command names consistent.
- Remove throat-clearing, repeated conclusions, generic claims, and details that do not help the reader complete or understand the task.
- Preserve prerequisites, rationale, constraints, and safety information even when removing them would make the page shorter.

Conciseness is subordinate to understanding and safe action.

The subtraction pass should be independent of the drafting rationale when a fresh reviewer is available. It remains review-only unless revision is separately authorized. Valuable secondary material should move behind a contextual link rather than lose its discovery path.

## Skill Components

The initial skill should remain small and repository-native:

- `SKILL.md`: triggers, core workflow, document classification, safety rules, and completion checklist.
- `references/document-patterns.md`: detailed guidance for orientation, conceptual, operational, and reference documents.
- `references/review-rubric.md`: criteria for create, revise, and review modes.
- `agents/openai.yaml`: generated user-facing skill metadata.

Do not add scripts until repeated use demonstrates a mechanical check that is both reliable and valuable. Judgment about audience, hierarchy, meaningful operations, and sufficient explanation belongs in the skill rather than a brittle linter.

## Error Handling

Use explicit guard clauses in the workflow:

- If the reader or goal is unclear and different answers would materially change the document, ask one focused question before drafting.
- If repository instructions conflict with the requested document, surface the conflict and request a decision.
- If technical evidence is missing, do not draft the disputed claim as fact.
- If safe execution cannot be independently established, do not execute the example; use static inspection and disclose the limitation.
- If no reference material exists, provide the necessary minimum detail and identify the missing reference rather than creating an unexplained link target.
- If the requested page combines incompatible purposes, propose a split and preserve one primary reader journey per page.

## Validation Strategy

Skill validation follows a documentation-specific red, green, and refactor cycle.

### Baseline scenarios

Run agents without the skill against at least these tasks:

1. Explain a database lifecycle and document backup and restore operations.
2. Write a CLI quick start for a project with extensive command reference.
3. Document an API integration with authentication, retries, and failure behavior.
4. Review an existing guide that mixes user, operator, and contributor concerns.
5. Review an operational guide under deadline and arbitrary length pressure, with both low-value prose and safety-critical context.

Record whether baseline outputs:

- begin with implementation or reference detail instead of a reader goal;
- omit the system model;
- describe operations without examples or expected results;
- reproduce exhaustive options in the main guide;
- mix audiences;
- assert behavior without evidence;
- omit safety, verification, or recovery guidance; or
- use jargon, repetition, inconsistent terminology, or dense prose.

### Skill-enabled scenarios

Run comparable tasks with the skill and confirm that the output corrects the observed baseline failures without becoming formulaic or verbose.

### Acceptance criteria

For each scenario, an independent reviewer should be able to answer:

- Who is the primary reader?
- What goal can the reader accomplish?
- What system model does the page establish?
- Does every meaningful operation have a concise example and expected result?
- Are meaningful extensions explained and demonstrated?
- Are safety, failure, and recovery proportional to the operation's risk?
- Is exhaustive detail placed in or linked to reference material?
- Can every material technical claim be traced to evidence or an explicit limitation?
- Does the page remain easy to scan without fragmenting the explanation?
- Can every retained passage be tied to a reader capability, decision, safety property, understanding, or navigation need?
- Does every proposed removal state what would be lost and preserve useful secondary material through relocation?

Validation should use fresh contexts and should not reveal the intended diagnosis to evaluators.

## Documentation Maintenance

When software behavior changes, inspect every document that describes the affected interface, lifecycle, configuration, example, failure mode, or result. Update connected pages in the same change or state why no update is necessary.

Avoid duplicated facts without an ownership rule. Prefer one authoritative reference location with contextual links from operational and conceptual guides.

## Deferred Decisions

- Whether repeated validation needs a deterministic documentation fixture or test harness.
- Whether diagrams should receive a separate reference guide after real usage demonstrates recurring patterns.
- Whether project-specific terminology files need explicit support beyond following repository conventions.
