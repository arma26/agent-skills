# Security-Relevant Footguns

## Contents

- Inputs, formats, and parsers
- Filesystem and archives
- Networking and downloads
- Authentication, authorization, and permissions
- Storage and state
- Concurrency, retries, and failure
- Dependencies and external integrations
- Outputs, logs, and errors
- Personal information and developer identity
- Fragility and assumption drift

Use only sections matching observed surface. Report an item only when it has a concrete security consequence or drift mechanism.

## Inputs, Formats, and Parsers

- Multiple decoders or validators for one format create parser differentials and inconsistent acceptance.
- Validation before canonicalization permits alternate encodings, Unicode forms, separators, or duplicate keys to bypass policy.
- Implicit coercion, permissive unknown fields, ambiguous defaults, and fail-open schema evolution expand accepted states.
- Unbounded size, depth, recursion, expansion, regex work, or collection count enables resource exhaustion.
- Type or content sniffing accepts more attack languages than a fixed schema or media type.
- Deserialization that constructs executable or privileged objects crosses a code or authority boundary.

## Filesystem and Archives

- User-controlled paths, filenames, roots, or extensions enable traversal and namespace confusion.
- Checks performed before canonicalization, symlink resolution, or the final open operation create containment gaps and time-of-check/time-of-use races.
- Predictable temporary names, broad permissions, non-atomic replacement, and partial cleanup expose or corrupt data.
- Archive entries can escape extraction roots through traversal, links, device files, or platform-specific path forms.
- Unbounded files, sparse files, nested archives, and decompression ratios exhaust storage or compute.
- Machine-specific absolute paths in tests, snapshots, logs, and docs disclose developer identity and create non-portable assumptions.

## Networking and Downloads

- Caller-selected destinations, schemes, ports, redirects, proxies, or DNS results expand network authority and enable request forgery.
- Redirects can cross host, trust, or credential boundaries after initial validation.
- Public resolution can change before connection; application checks alone may not constrain actual egress.
- Missing limits on headers, body, decompression, redirects, retries, concurrency, or time permit resource exhaustion.
- Generic HTTP clients and reusable fetchers expose capability beyond a fixed provider or operation.
- Downloaded content remains untrusted through format detection, parsing, storage, rendering, and logging.

## Authentication, Authorization, and Permissions

- Authentication without resource-scoped authorization leaves confused-deputy and cross-tenant paths.
- Raw roles, flags, or client claims detached from subject and resource context become forgeable ambient authority.
- Unknown, missing, stale, or failed policy data that defaults to allow is a fail-open decision.
- Compatibility aliases silently broaden privileged input and can outlive their intended migration.
- Permission checks duplicated across handlers, helpers, middleware, and clients drift over time.
- Broad service accounts or filesystem/network permissions turn a narrow defect into a larger blast radius.

## Storage and State

- Persisting data for convenience lengthens exposure and creates deletion, migration, backup, and authorization obligations.
- Shared or global state without multiple justified consumers widens ownership and synchronization boundaries.
- Cache or session data treated as source of truth permits stale authorization and integrity decisions.
- Duplicate stored and derived values need an explicit synchronization invariant; absent one, assumptions drift.
- Secrets, credentials, personal information, and tenant data require explicit owner, consumers, retention, and protection.
- Partial writes and non-atomic updates can leave state that later code interprets as valid.

## Concurrency, Retries, and Failure

- Retrying non-idempotent effects duplicates writes, charges, messages, or authority transitions.
- Replayable requests or events without freshness and identity checks repeat privileged actions.
- Swallowed exceptions, broad catches, fallback success, and partial results conceal failed security controls.
- Cleanup that runs only on success converts temporary sensitive state into retained state.
- Lock scope, cancellation, timeout, and recovery can split validation from the protected effect.
- Shared mutable state can leak data or decisions across requests, users, or tenants.

## Dependencies and External Integrations

- A new dependency expands install-time code, transitive code, update channels, and trusted maintainers.
- Plugins, hooks, subprocesses, and integrations often inherit more filesystem, network, secret, or process authority than required.
- Unpinned or weakly verified artifacts permit substitution and assumption drift across environments.
- External responses, metadata, filenames, redirects, and errors are inputs even when the provider is trusted.
- Integration state belongs at the boundary; leaking it into domain or UI persistence confuses ownership and trust.
- Future reuse is not a current security justification for a generic capability.

## Outputs, Logs, and Errors

- Output encoding or content type that does not match the data permits downstream interpretation as executable content.
- Logs, traces, snapshots, and exceptions can duplicate secrets or personal data into broader retention and access scopes.
- Detailed errors can reveal filesystem layout, identities, policy rules, internal services, or record existence.
- Returning raw dependency or parser output transfers an external trust decision into the caller.
- Debug behavior and verbose logging that differ by environment create unreviewed production surface.

## Personal Information and Developer Identity

- Names, email addresses, usernames, home paths, hostnames, account identifiers, and production-shaped records can leak through generated tests, fixtures, snapshots, examples, docs, errors, and build artifacts.
- Passing tests do not establish safe publication. Generated artifacts are outputs and Git history makes later removal incomplete.
- Secret-shaped values require provenance. If validity cannot be established read-only, report the uncertainty without reproducing the value.
- Prefer content-agnostic fixtures, reserved domains, synthetic identifiers, repository-relative paths, and redaction before serialization.
- Cite the location and category of a sensitive literal; do not copy it into the report.

## Fragility and Assumption Drift

- Parallel implementations of policy, parsing, normalization, serialization, cleanup, or retry logic create multiple sources of truth.
- Dead compatibility paths, fallback modes, and feature flags retain capabilities whose original constraints disappear.
- Broad generic containers and helpers accumulate unrelated authority and consumers.
- Security behavior dependent on call order, undocumented defaults, or implicit environment state is fragile under reuse.
- Tests that target isolated helpers while bypassing the real entry point can preserve unsafe behavior and create false assurance.
- Documentation that describes only one of several live paths causes human decisions based on an incomplete system model.
