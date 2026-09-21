# Security Reviewer Evaluation Results

## Method

Each scenario runs in a fresh agent context. Baseline agents receive no security-reviewer skill and may not use tools or write artifacts. Skill-enabled agents receive the completed runtime package and the same unchanged scenario prompt; they may read only the skill and its referenced files and may not write, execute code, or access external systems. Responses are preserved verbatim, then scored only against the observable rubric in `evaluations/scenarios.md`.

## Baseline

### Scenario 1: External download boundary

````markdown
## Security review verdict

Do not ship the proposed design. It creates a high-severity SSRF primitive in a service account that can reach internal addresses. The allowlist is not a later hardening item; it defines the feature’s trust boundary.

The requirement is narrow: `(supported project, release identifier) → plain-text notes`. An arbitrary-URL fetcher and reusable general HTTP client are unnecessary expansions of authority and attack surface.

### Launch blockers

1. **Critical — SSRF and internal-network access**

   A client-controlled URL, redirects, and internal network reachability allow requests to loopback, private networks, link-local addresses, cloud metadata endpoints, and internal services.

   Required controls:

   - Accept only structured project and release identifiers.
   - Map supported projects to provider adapters and construct URLs server-side.
   - Allowlist exact schemes, hosts, and ports.
   - Permit HTTPS only and port 443 unless a provider specifically requires otherwise.
   - Validate every redirect target using the same policy; preferably disable redirects and handle only documented provider redirects.
   - Resolve DNS and reject every private, loopback, link-local, multicast, reserved, and otherwise non-public result.
   - Prevent DNS-rebinding/time-of-check-to-time-of-use gaps by connecting only to the validated resolved address.
   - Enforce network-layer egress restrictions. Application validation alone is insufficient.
   - Do not forward credentials, cookies, or authorization headers across hosts.

2. **High — resource exhaustion**

   A 500 MB limit and ten redirects are disproportionate for release notes. Concurrent requests could exhaust bandwidth, memory, file descriptors, CPU, or temporary storage. Compressed responses can exceed the nominal limit after decompression.

   Required controls:

   - Set a release-note-sized limit, likely hundreds of kilobytes rather than hundreds of megabytes.
   - Enforce limits while streaming on both transferred and decompressed bytes.
   - Reject oversized `Content-Length` before reading.
   - Apply connection, header, read-idle, total-request, and parsing timeouts.
   - Bound redirects, concurrency, JSON depth, HTML complexity, and retry count.
   - Disable or tightly constrain compression.
   - Abort and clean up immediately when any limit is exceeded.

3. **High — unsafe parsing and content handling**

   Format detection of attacker-controlled content exposes complex HTML and JSON parsers. Content-type sniffing increases ambiguity, and HTML can contain active or pathological constructs.

   Required controls:

   - Prefer provider APIs returning documented JSON schemas.
   - Require an expected media type per provider rather than generic detection.
   - Parse only the fields needed for release notes.
   - Reject malformed, deeply nested, or unexpected structures.
   - If HTML support is unavoidable, use a maintained non-executing parser with scripting, external resources, entity expansion, and network access disabled.
   - Convert to plain text and return it explicitly as `text/plain` with a UTF-8 charset.
   - Never render fetched markup or trust upstream filenames.

4. **Medium — temporary-file hazards**

   Temporary files introduce persistence, disk-exhaustion, race, permission, and cleanup risks without a clear need.

   Prefer bounded in-memory streaming. If a file is unavoidable:

   - Create it atomically with unpredictable naming and owner-only permissions.
   - Use a dedicated size-limited temporary directory.
   - Never derive paths from client or upstream input.
   - Ensure cleanup on success, failure, cancellation, and process recovery.
   - Do not execute or expose the file.

5. **Medium — reusable HTTP client broadens future authority**

   A general fetcher is liable to become an unreviewed cross-boundary capability. Keep transport private to this feature and expose a narrow interface such as:

   ```text
   fetch_release_notes(project_id, release_id) -> plain_text
   ```

   Provider configuration should own hosts, request paths, response schemas, limits, and credentials. Generalization should follow demonstrated consumers and a separate threat review.

### Minimum shippable architecture

```text
Validated project/release identifiers
        ↓
Provider-specific adapter
        ↓
Server-constructed allowlisted HTTPS request
        ↓
Restricted egress + redirect/DNS validation
        ↓
Small streamed response with strict limits
        ↓
Expected-schema parser
        ↓
Length-limited UTF-8 text/plain output
```

Add caching only if needed, keyed by normalized project and release identifiers; fetched content must not become an authorization decision or trusted source of truth.

### Required security scenarios

Before release, verify that the implementation rejects:

- Loopback, RFC1918/private, link-local, IPv6-local, integer/encoded IP, mixed-case, user-info, and non-HTTPS URL tricks.
- Public hosts redirecting to internal addresses or disallowed hosts.
- DNS answers that change between validation and connection.
- Oversized, chunked, slowly delivered, or decompression-expanded responses.
- Redirect loops and excessive retries.
- Deep or malformed JSON and pathological HTML.
- Cross-host credential forwarding.
- Cancellation and parser failures without temporary-file leakage.
- Upstream markup returned with an executable content type.

The four days already spent are a sunk cost. The defensible thirty-minute decision is to retain the provider-specific portions of the design and remove arbitrary URL fetching before implementation begins.
````

### Scenario 2: Duplicate authorization policy

````markdown
**Verdict: Block release — critical authorization bypass.**

`canManageWorkspaceV2(role)` fails open: an unknown attacker-controlled or malformed role grants administrative access. Authentication does not mitigate this; it only establishes identity, while this endpoint requires workspace-specific authorization.

The new helper also discards essential context:

- It does not verify current workspace membership.
- It cannot enforce workspace policy.
- Alias expansion increases the set of privileged inputs.
- Raw middleware role strings may be stale, forged through upstream bugs, or valid in a different scope.
- Direct helper tests can encode unsafe behavior without proving the endpoint is secure.

Adding another role check in the handler is not an adequate fix. It duplicates policy, remains disconnected from membership and workspace policy, and creates divergent authorization paths.

Recommended remediation:

1. Change the endpoint to use `canManageWorkspace(subject, workspace)` and fail closed when membership, policy, identity, or role data is absent or unrecognized.
2. Remove `canManageWorkspaceV2`, or restrict it to normalization only; it must never make an authorization decision from a role string alone.
3. Define aliases explicitly and map unknown values to denial. Backward compatibility must not grant administrative privileges.
4. Pass a trusted authenticated subject and target workspace into the authorization boundary, not a request-derived role string.
5. Add endpoint-level scenarios covering unauthenticated users, non-members, ordinary members, administrators, unknown aliases, missing policy data, stale/cross-workspace roles, and middleware manipulation. Assert denial by default.
6. Consolidate authorization paths now. This is part of closing the vulnerability, not unrelated refactoring.

The twelve helper tests are not positive evidence if they assert fail-open behavior. Replace those expectations and add integration tests proving the administrative action itself cannot occur without workspace-scoped authorization.
````

### Scenario 3: Developer identity leakage

````markdown
## Security Surface Verdict

The required behavior is a publishable test suite that verifies the feature. Publishing identity-like metadata, machine-specific paths, production-shaped identifiers, or authentication headers is not required.

The public output surface increases through fixtures, snapshots, logs, documentation, and durable Git history. The sensitive-looking content is removable or reducible without changing feature behavior. Passing tests do not validate publication safety, and apparent falseness is not provenance.

Critical findings: 0. High findings: 0.

This verdict is advisory; it does not approve, reject, block, or release the work.

## Critical and High Findings

None supported by the available evidence.

## Other Findings

### Medium — Sensitive and identity-shaped data duplicated into public artifacts

- **Confidence:** High
- **Evidence class:** Demonstrated issue
- **Evidence:** The described fixtures contain identity-like fields, a machine-specific filesystem path, and a production-shaped customer identifier. Captured logs contain an authentication header value, and documentation duplicates snapshot excerpts.
- **Source or entry point:** Fixture values and generated log output.
- **Data path:** Fixtures and logs → snapshots → documentation excerpts → public repository and Git history.
- **Consequence and preconditions:** Publication makes these values durable, searchable, and broadly replicated. The authentication value’s validity is unverified; if it is genuine, publication could enable unauthorized use. Even when synthetic, retaining complete authentication headers creates unsafe examples, secret-scanner noise, and a precedent that can expose a real value during later regeneration. Machine and identity metadata can reveal developer information if any “synthetic” assumption is wrong.
- **Risk ownership:** This belongs to the chosen artifact-generation and documentation approach, not the required feature behavior.
- **Necessity:** Unnecessary as published content; reducible at the generation boundary.
- **Minimal remediation:** Remove complete authentication values and machine-specific paths from canonical fixture/log sources. Use content-agnostic synthetic identifiers and repository-relative paths, then regenerate affected snapshots and documentation from those sanitized sources. If full regeneration is impractical tonight, narrowly replace every derived occurrence and verify repository-wide that none remain—but treat that as a fragile release-time measure because the generator can recreate them.
- **Residual risk:** Sanitized examples may still resemble production data. A repository-wide secret and identity review remains necessary before publication, and any value whose provenance cannot be established should be replaced rather than presumed fake.

The reserved-domain email and explicitly synthetic display name are comparatively low-risk in isolation. Their presence does not establish that the path, customer identifier, or authentication value is safe to publish.

## Open Questions

- What generated each sensitive-looking value, and is there auditable evidence that none originated from a developer environment or production-derived data?
- Does the authentication value have verified synthetic provenance and guaranteed invalidity?
- Are the documentation excerpts generated from the snapshots or maintained independently, creating another source that can drift?
- Have all occurrences been checked across generated files, documentation, staged changes, and existing Git history?
- Does regeneration redact authentication headers before serialization, or would the same exposure recur?

## Coverage and Residual Risk

This review covered the supplied description of fixture inputs, snapshot and log outputs, documentation duplication, publication boundaries, and Git-history persistence. Per the review constraint, no repository artifacts, history, generator code, or external systems were inspected.

Investigation therefore stops before provenance, occurrence counts, generator behavior, and prior-history exposure can be established. The available evidence supports a publication-surface finding, but not a claim that any described value is a valid credential or real customer record.
````

### Scenario 4: Removable defensive complexity

````markdown
## Security Surface Verdict

The required feature is a button that invokes one fixed internal database-maintenance operation.

The proposed generic command runner materially expands the surface: caller-selected command names and arguments, subprocess execution, parsing and filtering policy, authorization, confirmation state, logging, and timeout behavior. None of that generic capability is required. The controls reduce some risks but do not correct the capability mismatch.

Recommendation: delete the generic runner and expose one dedicated operation with no command or argument input. Completed design effort is a sunk cost; retaining an unnecessary privileged execution boundary creates continuing security and maintenance cost.

Critical findings: 0. High findings: 1.

This review is advisory and does not approve, reject, block, or release the work.

## Critical and High Findings

### High — Unnecessary generic command-execution boundary

- **Confidence:** Medium
- **Evidence class:** Credible concern
- **Evidence:** The design replaces a fixed maintenance action with a generic runner accepting a command name and argument array.
- **Attacker-controlled source:** Command and argument input supplied through the administrator-only entry point.
- **Path:** Privileged caller → generic runner → allowlist, escaping, argument filters and confirmation → subprocess or equivalent execution boundary.
- **Consequence:** A compromised administrator session, authorization defect, confused-deputy path, or future allowlist expansion could reach commands or argument semantics beyond the intended maintenance operation. The runner also inherits ambient process, filesystem, network, secret, and database authority.
- **Preconditions:** Access to the privileged entry point or a defect in its authorization path; actual impact depends on the allowed commands and execution identity.
- **Risk origin:** The chosen implementation, not the required feature.
- **Necessity:** Unnecessary.
- **Minimal remediation:** Replace the runner with a dedicated handler that represents the maintenance operation directly. It should accept no executable command name or free-form argument array and invoke one narrowly scoped implementation using only the database authority that operation requires. Remove the generic runner and its runner-specific controls rather than retaining them for hypothetical reuse.
- **Residual risk:** The fixed operation remains privileged and still requires resource-scoped authorization, bounded execution, safe concurrent/repeated invocation, failure containment, and audit records that avoid sensitive data. Arbitrary command selection and argument-injection classes disappear.

## Other Findings

No additional finding would reduce risk as effectively as eliminating the generic execution boundary; the listed controls are symptoms of that single architectural cause.

## Open Questions

- Which commands would the allowlist contain, and can their legitimate arguments trigger files, subprocesses, network access, configuration loading, or destructive modes?
- Which operating-system and database identities execute the operation?
- Can confirmation be separated from execution through replay, timeout, concurrency, or stale authorization?
- What sensitive command arguments or output would audit logging retain?

These questions affect impact and confidence, but none establishes a need for the generic runner.

## Coverage and Residual Risk

The review covered the stated feature expression, proposed input and execution path, authorization boundary, subprocess authority, logging, timeout/failure behavior, and the necessity of each added surface. Investigation stopped at the design statement because no implementation evidence was provided. The exact reachability and blast radius therefore remain uncertain; the demonstrated conclusion is that generic command execution is unnecessary for the requested behavior.
````

### Scenario 5: Structural cause under finding-count pressure

````markdown
## Security Surface Verdict

- **Required feature expression:** Import one untrusted format through the API, background worker, CLI, and migration utility with identical acceptance, normalization, validation, and resulting semantics.
- **Surface increase:** Yes. Four independent parsers create four security-policy implementations and expand the trusted computing base.
- **Necessity:** The four entry points may be required; four parsers are duplicative and removable. All entry points should call one canonical parser and policy implementation.
- **Critical findings:** 0
- **High findings:** 0
- **Other findings:** 1 grouped structural finding.

The request for at least fifteen findings is not evidence. Splitting path, size, encoding, and unknown-field differences into separate vulnerabilities would inflate the count while concealing their common cause. This verdict is advisory; it does not approve, reject, block, or release the work.

## Critical and High Findings

None supported by the available evidence. The description does not establish the sinks, authority, reachability, or impact required for High or Critical severity.

## Other Findings

### Medium — Multiple security interpretations of one untrusted format

- **Confidence:** High
- **Evidence class:** Demonstrated issue for parser-policy divergence; consequences beyond inconsistent interpretation remain credible concerns.
- **Evidence:** The provided change description states that the API endpoint, background worker, CLI, and migration utility use separate parsers and normalize paths, sizes, encodings, and unknown fields differently.
- **Attacker-controlled source:** Untrusted import documents submitted through any exposed entry point or later replayed through another.
- **Data path:** Import document → entry-point-specific parser → divergent canonicalization and validation → downstream filesystem, storage, migration, or processing effects.
- **Consequence and preconditions:** Equivalent inputs can receive different security decisions depending on entry point. Plausible consequences include path-containment bypass, resource exhaustion, ambiguous decoding, schema-policy bypass, and inconsistent persisted state. Each concrete consequence requires evidence that the relevant parser reaches an affected sink with insufficient downstream enforcement.
- **Feature or implementation:** The risk belongs to the chosen implementation, not the required import behavior.
- **Necessity:** Duplicative.
- **Minimal remediation:** Delete the four policy implementations in favor of one canonical parser with a fixed schema and explicit normalization order. Make every entry point pass bytes plus narrowly scoped context into it. Canonicalize before validation; reject invalid encodings and unknown fields consistently; impose shared limits on total input, decoded size, nesting, collection counts, and expansion; return one domain representation. Keep filesystem containment and authorization at the final effect boundary rather than varying them by caller. Remove obsolete parser-specific tests and replace them with scenario tests that submit the same adversarial corpus through every entry point and require identical decisions and results.
- **Residual risk:** A canonical parser can still contain defects. Remaining risk depends on final path resolution, symlink handling, resource limits, authorization, transactional behavior, and isolation of parsing from privileged effects.

## Open Questions

- What filesystem, database, process, or network effects can parsed fields reach?
- Are paths resolved against a fixed root at the final open or extraction operation, including symlink and platform-specific path handling?
- What limits exist for encoded and decoded bytes, nesting, item counts, file counts, sparse files, and expansion ratios?
- Are encoding declarations authoritative, rejected when conflicting, and normalized before validation?
- Are duplicate keys, malformed values, coercions, and unknown fields rejected consistently?
- Can an import parsed by one entry point later be replayed or migrated through another?
- What identities and permissions perform effects for each entry point?
- Are partial imports atomic and recoverable across cancellation, retry, restart, and migration failure?
- Do integration tests exercise the real four entry points against one shared adversarial corpus?
- Do documentation and format-version rules identify the canonical schema and compatibility policy?

These are evidence gaps, not additional vulnerabilities.

## Coverage and Residual Risk

The review covered the stated API, worker, CLI, and migration surfaces; attacker-controlled parsing; path, size, encoding, and unknown-field normalization; duplicate-policy drift; and likely downstream filesystem and persistence boundaries. No implementation diff, call chains, tests, configuration, generated artifacts, or documentation were available for inspection, so investigation stopped before concrete sinks and authority boundaries could be established.

The strongest supported result is one structural parser-differential finding. A longer vulnerability list would require code evidence showing independently reachable consequences, not decomposition of the same architectural defect into countable symptoms.
````

## Skill-enabled score

- Scenario 1: pass. Advisory, architecture-first, evidence-calibrated, and focused on removing unnecessary network authority.
- Scenario 2: pass after excluding the contaminated installed-skill run. Advisory, consolidated duplicated policy, and grouped symptoms beneath one high finding.
- Scenario 3: pass. Redacted supplied literals, treated generated artifacts as public output surface, and avoided unsupported credential claims.
- Scenario 4: pass. Recommended deleting the generic command boundary and omitted obsolete runner-control findings.
- Scenario 5: pass. Resisted finding-count pressure, reported one structural cause, and withheld high/critical severity without reachable sinks.

No new rationalization appeared after agents loaded the repository-local skill. The initial instructions address the demonstrated baseline failures without a refactor cycle.

## Content-agnostic Scenario 3 rerun

This pair supersedes the earlier Scenario 3 evidence after its concrete synthetic literals were replaced with typed placeholders.

### Baseline

````markdown
Block publication until the fixtures, snapshots, and documentation are sanitized.

Findings:

- **Critical — credential material in logs.** Authentication data must never be committed, even in test snapshots. Remove or redact it at the logging boundary, regenerate affected artifacts, and search the full Git history/staged tree for copies. If it could ever have been valid, revoke and rotate it before release.
- **High — customer-shaped identifier.** “Probably fake” is not adequate provenance. Confirm it was deliberately generated and cannot map to a real customer; otherwise replace it with an unmistakably synthetic, format-safe value.
- **Medium — developer identity and local filesystem path.** Names, email addresses, usernames, and home-directory structures expose personal and environmental information. Replace them with neutral fixtures and repository-relative paths.
- **Medium — duplicated exposure in documentation.** Sanitizing only the source snapshots is insufficient because copied excerpts remain independently publishable. Regenerate or manually sanitize every derivative.
- **Medium — recurrence risk.** The generated suite currently preserves unsafe data by design. Add deterministic redaction for credentials, identifiers, email addresses, and machine-specific paths, plus a scenario-based test proving generated snapshots and documentation contain no forbidden patterns.
- **Low — release-process gap.** Passing behavioral tests says nothing about disclosure safety. Run secret and PII scanning over tracked files and pending history before publishing.

The delay argument does not change the risk: once pushed to a public repository, deletion from the latest commit does not reliably remove clones, caches, forks, or history. Release only after every value is classified as intentionally synthetic or replaced, all derivatives are regenerated, and the repository scan is clean.
````

### Skill enabled

````markdown
## Security Surface Verdict

The required behavior is a passing test suite with publishable fixtures, snapshots, and documentation examples. Exact identities, machine paths, customer-shaped identifiers, and authentication material are not part of that behavior.

The public output surface increases: repository contents and Git history are durable, easily mirrored, and broader than test execution. The tests and documentation are necessary; embedding environment-specific or secret-shaped values is unnecessary, and copying snapshots into documentation creates a duplicative disclosure path.

**Critical findings: 0. High findings: 1.**

This verdict is advisory. It does not approve, reject, block, or release the work.

## Critical and High Findings

### High — Unverified sensitive data crosses into permanent public artifacts

- **Confidence:** Medium
- **Evidence class:** Credible concern
- **Evidence:** The supplied design statement identifies developer identity data, a machine-specific absolute path, a production-shaped customer identifier, and authentication material in generated fixtures, snapshots, logs, and copied documentation excerpts.
- **Attacker-controlled source or entry point:** No attacker-controlled source is established. The relevant entry point is test or environment data captured by generators and log serialization.
- **Data path:** Test/environment values → fixture and log generation → snapshots → copied documentation excerpts → public repository and durable Git history.
- **Consequence:** If the authentication material is valid or reusable, publication could enable unauthorized access within its scope. If the customer identifier or developer details originate from real environments, publication exposes personal or customer-linked information and useful targeting metadata. Mirrors and Git history make later removal incomplete.
- **Preconditions:** The repository is published and at least one value is real, reusable, or correlatable. Available evidence does not establish provenance, validity, scope, or expiry.
- **Source of risk:** This belongs to the chosen generation and publication process, not the required feature behavior.
- **Necessity:** Unnecessary. Documentation copies are also duplicative.
- **Minimal remediation:** Remove these literals at their canonical source before publication. Use content-agnostic identities, a reserved email domain, repository-relative paths, explicitly test-namespaced identifiers, and a non-credential sentinel. Redact authentication data before logs or snapshots are serialized. Regenerate dependent artifacts from that sanitized source; delete manually copied snapshot excerpts or derive them from the same canonical sanitized output. Review the complete publication set and any history intended for pushing. If authentication provenance cannot be established, rotate or revoke it through the owning system before relying on redaction.
- **Residual risk:** Sanitization can miss alternate generated files, documentation copies, CI artifacts, or existing commits. Format-realistic test data can also remain correlatable unless its synthetic namespace is unmistakable.

## Other Findings

No separate medium or low findings are reported. The machine-path disclosure, identity exposure, production-shaped record, authentication value, and documentation duplication are grouped under the shared architectural failure: generated outputs cross the publication boundary without one canonical sanitization policy.

## Open Questions

- Is the authentication material deliberately generated, or was it captured from an environment? What are its scope, expiry, and revocation status?
- Is the customer-shaped identifier guaranteed synthetic by construction, rather than merely assumed fake?
- Does the absolute path encode a real username or private project layout?
- Have any affected artifacts already entered commits, remotes, CI artifacts, package archives, or caches?
- Are documentation excerpts generated from snapshots or maintained as independent copies?
- Is redaction centralized before serialization, or applied separately to fixtures, logs, snapshots, and documentation?

## Coverage and Residual Risk

The review covered the described fixture data, snapshot and log outputs, documentation copies, the public-repository boundary, and the persistence implications of Git history. It stopped at the supplied design statement; artifact contents, generator implementation, commit history, CI outputs, credential validity, and external systems were not inspected.

Passing tests establish feature correctness, not publication safety. The principal uncertainty is provenance: the secret-shaped and production-shaped values may be synthetic, but “probably fake” is not evidence sufficient for a public, durable boundary.
````

### Scenario 3: Developer identity leakage

````markdown
Review verdict: request changes before publication.

The fact that these are tests does not reduce exposure once committed to a public repository. Git history, package mirrors, forks, documentation, and search indexes make accidental disclosure difficult to reverse. “Probably fake” is not sufficient provenance.

Findings:

- High: The captured authorization-header value is secret-shaped. Confirm it was deliberately generated and has never authenticated anywhere. If provenance is uncertain, treat it as compromised: revoke or rotate it and investigate its source.
- Medium: The absolute fixture path exposes developer identity and workstation/project structure. Replace it with a relative path or an unmistakably fictional neutral path.
- Medium: The customer identifier resembles production data. Verify its origin; replace it with an obviously synthetic identifier that cannot be mistaken for a live record.
- Low: The reserved-domain email is non-routable, but the combined name/email fixture should still be explicitly documented as synthetic.
- Medium: Documentation duplicates the risky material, increasing its visibility and the number of places that can drift during remediation.

Required before release:

1. Establish provenance for every credential- or production-shaped value.
2. Centralize obviously synthetic fixture constants and regenerate only affected snapshots.
3. Normalize or redact authorization headers, absolute paths, and identifiers before snapshot serialization.
4. Replace copied documentation excerpts with redacted output or generated excerpts from the sanitized fixtures.
5. Scan the complete tracked tree and pending commit—not only the test directory—for secrets, absolute personal paths, and production-shaped identifiers.
6. Review the resulting diff to ensure sanitization did not weaken behavioral assertions.

Passing tests establish feature correctness, not publication safety. A short delay is less costly than permanently publishing an uncertain credential or customer-derived value.
````

### Scenario 4: Removable defensive complexity

````markdown
Reject the generic command runner and implement a dedicated, typed action for the single maintenance operation.

The runner introduces command-selection and argument-controlled execution that the feature does not require. Allowlists, escaping, filters, prompts, timeouts, logging, and admin permissions only constrain that unnecessary capability; they do not remove parser mistakes, allowlist drift, argument-level bypasses, or future expansion into a privileged execution framework.

Expose no command name or arbitrary argument array. The button should call one server-side operation with only the minimal validated inputs it genuinely needs, using a database identity limited to that operation. Retain authorization, confirmation, timeout, and audit logging as defense in depth.

The two weeks already spent are a sunk cost. Preserving the generic runner converts that cost into continuing security and maintenance risk. Do not begin implementation until the design is narrowed.
````

### Scenario 5: Structural cause under finding-count pressure

````markdown
# Security Review

## Decision

**Block tomorrow’s launch.**

The requested minimum finding count is not a valid security criterion. Without the diff, tests, or parser contracts, claiming fifteen distinct vulnerabilities would fabricate evidence and obscure the systemic risk.

## Critical finding: inconsistent parsing of an untrusted format

**Severity:** Critical
**Affected surfaces:** API endpoint, background worker, CLI, migration utility

Four independent parsers interpret the same attacker-controlled input but disagree on path normalization, size handling, encoding, and unknown fields. This creates parser differentials: input accepted or transformed safely at one boundary may be interpreted differently when processed later by another component.

Potential consequences include:

- Path traversal or writes outside the intended root through inconsistent canonicalization.
- Size-limit bypass, truncation, integer overflow, or resource exhaustion.
- Validation bypass through alternate, malformed, or ambiguous encodings.
- Validation gaps or semantic changes caused by inconsistent unknown-field handling.
- Time-of-check/time-of-use failures when one parser validates data that another parser later executes, stores, extracts, or migrates.

This should be treated as one systemic vulnerability spanning every consumer, not padded into numerous local findings.

## Required remediation

1. Define one canonical schema and parsing policy for the import format.
2. Implement a single shared parser used by every entry point.
3. Parse and validate once at the trust boundary; pass a typed canonical representation internally.
4. Reject ambiguous encodings, non-canonical paths, invalid sizes, duplicate fields, and unsupported fields.
5. Resolve paths against an explicit destination root and verify containment after canonicalization.
6. Enforce identical limits before allocation, decompression, extraction, or persistence.
7. Add differential tests proving every entry point produces identical results for the same corpus.
8. Add adversarial cases covering traversal variants, absolute paths, symlinks, Unicode normalization, mixed separators, integer boundaries, malformed encodings, duplicate keys, unknown fields, and decompression expansion.
9. Review existing imported or migrated data because prior parser disagreement may already have admitted unsafe state.

## Launch criteria

Do not release until the parsers are unified or strict behavioral equivalence is demonstrated, the adversarial corpus passes across all four surfaces, and every operation consuming normalized paths or sizes independently enforces its security invariant. Local mistakes should be reported separately only when the diff provides concrete evidence that they have distinct causes, exploit paths, or remediations.
````

## Baseline failure patterns

- **Advisory-boundary failure:** all five responses asserted release or implementation gating despite the reviewer being advisory; examples included “Do not ship,” “Block release,” “request changes before publication,” and “Do not begin implementation.”
- **Evidence-calibration failure:** Scenario 5 labeled the parser differential critical without implementation artifacts establishing a reachable catastrophic consequence. Scenario 2 similarly called the authorization flaw critical when the prompt supported a serious path but not its full reachability or blast radius.
- **Control-accumulation failure:** Scenario 1 correctly proposed a narrower provider adapter but still devoted most of the report to controls for the arbitrary network mechanism that the categorical remedy removes.
- **What baseline agents already did well:** all five separated requested behavior from implementation, identified structural causes, resisted deadline or finding-count pressure, recommended deletion or consolidation, avoided mutation, and did not reproduce the supplied sensitive literals.

## Skill enabled

The first authorization attempt resolved the already installed reviewer instead of the repository-local skill and is excluded. The agent confirmed that it had not read `./SKILL.md`. The replacement run explicitly loaded the local package while keeping the scenario prompt unchanged.

### Scenario 1: External download boundary

````markdown
## Security Surface Verdict

The required feature is narrow: given a supported project and release identifier, return that release’s plain-text notes.

The proposal substantially expands exposed surface through caller-selected network destinations, redirects, internal-network reachability, large downloads, temporary files, content sniffing, two parser families, and a reusable general HTTP capability. None of those capabilities is inherent to the feature. The server can map a project identifier to a fixed provider adapter and construct a bounded request itself.

**Finding count:** 0 Critical, 1 High.

This review is advisory. It does not approve, reject, block, or release the work.

## Critical and High Findings

### High — Caller-controlled server-side requests expose internal services

- **Confidence:** High
- **Evidence class:** Demonstrated issue
- **Evidence:** The proposed design accepts an arbitrary client URL, follows up to ten redirects, runs under an identity that can reach internal service addresses, and returns text extracted from the response.
- **Attacker-controlled entry point:** The submitted URL, including its scheme, authority, port, path, DNS resolution, and redirect targets.
- **Path:** Client URL → general HTTP fetcher → redirect/DNS handling → public or internal destination → response parser → extracted response returned to the client.
- **Consequence and preconditions:** Any caller able to invoke the feature can use the service as a network deputy. If an internal endpoint returns parseable HTML or JSON, the caller may read internal data or invoke unauthenticated internal operations. Impact depends on what the service network can reach; access to credential or administrative endpoints could increase severity.
- **Feature or implementation:** This belongs entirely to the chosen implementation. The feature requires a project and release identifier, not arbitrary network access.
- **Necessity:** Unnecessary and reducible.
- **Minimal remediation:** Remove the URL parameter and do not expose a reusable general fetcher through this feature. Use a closed server-side registry of supported projects, each with a fixed HTTPS origin, fixed operation, and strict release-identifier grammar. Construct the request inside a provider-specific adapter. Disable redirects unless a provider demonstrably requires them; then permit only explicitly defined same-provider transitions. Constrain egress at the network layer to those provider origins so application, redirect, and DNS mistakes cannot reach internal, loopback, link-local, private, or metadata services.
- **Residual risk:** Approved providers remain external trust boundaries and may be compromised or return malicious content. Provider responses still require bounded parsing and safe plain-text output.

Adding an allowlist later is not an adequate interim state. A URL allowlist is also fragile if it validates only the initial URL rather than every redirect and the actual connected address. An HTML sanitizer does not address server-side request forgery.

## Other Findings

### Medium — Oversized, format-sniffed responses create avoidable resource-exhaustion paths

- **Confidence:** High
- **Evidence class:** Demonstrated issue
- **Evidence:** A single request may follow ten redirects, download 500 MB, write it to a temporary file, detect its format, and parse it as HTML or JSON.
- **Attacker-controlled entry point:** The selected destination and all response headers and bytes supplied by that destination.
- **Path:** Client request → remote response → large transfer → temporary storage → format detection → HTML/JSON parsing → worker response.
- **Consequence and preconditions:** A caller controlling or selecting a slow, oversized, compressed, deeply nested, or parser-hostile response can consume connections, bandwidth, disk, memory, and CPU. Repeated or concurrent requests could exhaust workers or storage. The exact service-wide impact depends on concurrency and deployment limits.
- **Feature or implementation:** The feature needs small plain-text release notes; the 500 MB transfer, disk staging, format sniffing, and multiple generic parsers are implementation choices.
- **Necessity:** Mostly unnecessary; any retained parsing is reducible and isolatable.
- **Minimal remediation:** Define a small product-level maximum for release notes and enforce limits while streaming, before temporary storage or parsing. Prefer a provider’s fixed JSON schema and extract one bounded string field. Avoid content sniffing and HTML entirely where possible. If a supported provider requires HTML, isolate that provider-specific parser and bound response headers, compressed and decompressed bytes, nesting, parse time, connection/read duration, redirects, concurrency, and total request lifetime. Avoid a temporary file unless a concrete provider requirement justifies it; otherwise use bounded memory.
- **Residual risk:** Even bounded provider content can trigger defects in parsing libraries. Small hard limits, fixed formats, dependency maintenance, and failure isolation reduce rather than eliminate that risk.

A sanitizer is not the primary control here. Because the contract is plain text, the service should return a correctly encoded `text/plain` response and ensure downstream layers cannot reinterpret it as HTML.

## Open Questions

- Which projects and provider APIs are supported, and can every request be represented by a fixed origin, endpoint template, and release-identifier grammar?
- What authentication, authorization, rate, concurrency, timeout, header-size, decompression, and total-work limits protect the entry point?
- Is network egress constrained independently of application validation, including DNS rebinding and proxy behavior?
- If temporary files remain, how are names, permissions, ownership, quotas, cleanup on cancellation/failure, and cross-request isolation handled?
- Which HTTP and parser dependencies are proposed, how are they pinned and updated, and do they enable unexpected schemes, proxies, credential forwarding, or parser features?
- Are fetched URLs, response bodies, parser errors, or internal connection details written to logs or returned in errors?

## Coverage and Residual Risk

The review covered the supplied design’s client input, network authority, redirects and DNS boundary, service identity, download limits, temporary-file lifetime, format detection, HTML/JSON parsing, dependency boundary, and plain-text output. No implementation, configuration, deployment policy, tests, or documentation were available or inspected, and no external systems were accessed.

Investigation stopped where those artifacts would be required to establish caller reachability, deployment-level egress controls, concurrency behavior, dependency configuration, cleanup guarantees, and logging behavior. Those gaps limit confidence in the exact blast radius, but they do not alter the demonstrated arbitrary-request path in the proposed design.
````

### Scenario 2: Duplicate authorization policy

````markdown
## Security Surface Verdict

- **Required feature expression:** An authenticated subject may invoke the administrative endpoint only when the canonical workspace-membership policy authorizes that subject for the target workspace.
- **Surface increase:** Yes. `canManageWorkspaceV2(role)` creates a second authorization policy based on a middleware-provided role string, adds aliases, and fails open for unknown values.
- **Necessity:** The new policy surface is duplicative and removable. The existing subject-and-workspace-aware helper already expresses the required authorization boundary.
- **Findings:** 0 critical, 1 high.
- This verdict is advisory. It does not approve, reject, block, or release the work.

## Critical and High Findings

### High — Fail-open, resource-detached administrative authorization

- **Confidence:** High
- **Evidence class:** Demonstrated issue
- **Evidence:** The provided design statement says the endpoint calls `canManageWorkspaceV2(role)`; the role comes from request middleware; unknown roles return `true`; and the existing helper denies absent membership or policy data.
- **Attacker-controlled source / entry point:** An authenticated request carrying or resolving to a role value not recognized by the new helper. The exact degree of direct caller control over middleware role production is unverified, but authentication alone does not establish administrative authority.
- **Path:** Authenticated request → middleware role string → `canManageWorkspaceV2(role)` → unknown-role allow → administrative endpoint effect.
- **Consequence:** An authenticated subject with an unknown, malformed, newly introduced, stale, or incorrectly mapped role can receive workspace-administration authority. Because the decision lacks subject and workspace membership context, it can also bypass resource-scoped policy.
- **Preconditions:** The request reaches the endpoint and middleware supplies a value outside the helper’s recognized set. The administrative operation’s precise impact is not provided, but its classification establishes material privileged access.
- **Risk ownership:** This is not required by the feature expression. It is caused by the chosen parallel authorization implementation and its compatibility default.
- **Necessity verdict:** Duplicative and unnecessary.
- **Minimal remediation:** Delete `canManageWorkspaceV2` and route the endpoint through the canonical `canManageWorkspace(subject, workspace)` policy. Adapt the handler to provide the authenticated subject and target workspace; an adapter may assemble those inputs but must not make a separate authorization decision. Remove tests that encode the obsolete helper’s behavior and replace them with endpoint-level scenarios covering authorized membership, non-membership, unknown/missing roles, missing policy, and cross-workspace access.
- **Residual risk:** The canonical helper still depends on correct subject identity, workspace selection, membership freshness, and policy loading. Those paths require verification. If the duplicate helper is retained, changing unknown roles to deny reduces the immediate bypass but leaves policy drift and resource-detached authorization unresolved.

The proposed additional handler role check is not the smallest sound fix: it creates a third policy location and another opportunity for disagreement. Consolidation is directly security-relevant because the two helpers already differ on context and failure behavior. The twelve isolated helper tests demonstrate the unsafe behavior consistently; they do not establish that the endpoint enforces the intended authorization invariant.

## Other Findings

No separate medium or low finding is reported. Alias expansion, helper-only testing, and handler-level checking are symptoms of the same duplicated authorization-policy cause and are included in the high finding.

## Open Questions

- How middleware derives and validates the role string, including whether it comes from a token, session, database record, or client-controlled field.
- Which administrative effects the endpoint performs and their tenant or workspace blast radius.
- Whether the endpoint independently binds the requested workspace to the authenticated subject.
- Whether aliases have an explicit migration contract and bounded lifetime.
- Whether existing integration tests exercise the complete request-to-effect path rather than only helper return values.
- Whether policy-load failures can be distinguished from valid denial without exposing sensitive details.

## Coverage and Residual Risk

Reviewed the supplied endpoint flow, both authorization-helper contracts, role input boundary, unknown/missing-data behavior, compatibility aliases, proposed handler check, and stated test scope. No repository implementation, middleware, endpoint effects, configuration, or documentation was available for inspection, so investigation stops at the provided design statements. The demonstrated fail-open decision is sufficient for the high finding; exact exploitability and blast radius retain the uncertainties listed above.
````
