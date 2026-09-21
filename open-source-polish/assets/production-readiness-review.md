# Production readiness review (PRR)

| Field | Value |
| --- | --- |
| Feature | `[TICKET_NUMBER]: Feature name` |
| Authors | `author names` |
| Start date | `YYYY-MM-DD` |
| End date | `YYYY-MM-DD` |
| Review status | `Not started` / `In progress` / `Done` |
| Release decision | `Ready` / `Ready with accepted risks` / `Not ready` |

For each item, add `Pass`, `Fail`, `Blocked`, or `N/A`. Add evidence or an `N/A` reason. A checked box means assessed, not passed.

Write for an operations specialist with no project context or operational
history. Describe the service as a black box. Operation must not require
source-code reading.

Complete each applicable item with this compact response:

`Result — Answer. Source: direct link. Owner: role or team. Last verified: YYYY-MM-DD.`

Answer the concern in the PRR or link directly to the authoritative operational
source. A project homepage, source-code location, or document that requires
another search does not satisfy the one-hop requirement. Do not place credentials
in this review.

## Live operational interfaces

Start here when you need to inspect the running service. Link to the scoped
service or environment view, not the platform homepage. State `N/A` and explain
why when an interface does not exist. Use protected, read-only access where the
platform supports it. Link to the access procedure instead of copying credentials.
Use stable links without embedded credentials or signed access parameters.

| Interface | What an operator can determine | Direct scoped link | Access procedure | Owner | Last verified |
| --- | --- | --- | --- | --- | --- |
| Service health or service-level dashboard | `<health, traffic, errors, latency, saturation, or user outcome>` | `<direct link or N/A with reason>` | `<direct link or N/A with reason>` | `<owner>` | `YYYY-MM-DD` |
| Container, workload, or runtime platform | `<release identity, instances, resource use, restarts, and events>` | `<direct link or N/A with reason>` | `<direct link or N/A with reason>` | `<owner>` | `YYYY-MM-DD` |
| Central log search | `<saved service and environment query, time range, and correlation fields>` | `<direct link or N/A with reason>` | `<direct link or N/A with reason>` | `<owner>` | `YYYY-MM-DD` |
| Database status interface | `<availability, capacity, connections, lag, backups, or maintenance state>` | `<direct link or N/A with reason>` | `<direct link or N/A with reason>` | `<owner>` | `YYYY-MM-DD` |
| Trace or background-work view | `<request path, dependency latency, queue state, or job completion>` | `<direct link or N/A with reason>` | `<direct link or N/A with reason>` | `<owner>` | `YYYY-MM-DD` |
| Deployment, alerting, or dependency status | `<rollout state, active incidents, alerts, or upstream health>` | `<direct link or N/A with reason>` | `<direct link or N/A with reason>` | `<owner>` | `YYYY-MM-DD` |

## Operator quick index

Complete this index after the detailed review. Each source must answer the
concern or enable the next safe action directly.

| Concern | Answer or direct source | Owner | Last verified |
| --- | --- | --- | --- |
| Service outcome, consumers, and supported boundary | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Release artifact, configuration, schema, and runtime identity | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Operator control plane and access procedure | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Start, stop, restart, upgrade, rollback, and verification | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Configuration contract | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Persistent state, backup scope, and safe regeneration | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Health definition and first inspection point | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Background work and completion evidence | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Failure symptoms, containment, recovery, and verification | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |
| Escalation and user communication | `<answer or link>` | `<owner>` | `YYYY-MM-DD` |

## Reviewers

Each reviewer checks the box after completing the review. Use the local role name when titles differ.

### Required

- [ ] Production reliability: `<reviewer name>`
- [ ] Release engineering: `<reviewer name>`
- [ ] Information security: `<reviewer name>`

### Optional

- [ ] Database: `<reviewer name>`
- [ ] Development: `<reviewer name>`

## Architecture

- [ ] What user outcome does the service provide, and who consumes it?
- [ ] Which inputs, outputs, protocols, ports, availability boundaries, and unsupported modes define the service?
- [ ] Do architecture diagrams show interactions with services and features?
- [ ] Do the diagrams identify internal and external dependencies, ports, encryption, protocols, access controls, and security policies?

## Operator controls and lifecycle

- [ ] Which release artifact, configuration generation, schema generation, environment, and runtime instance does this review cover?
- [ ] Where does an operator observe the release and runtime identity?
- [ ] Where does an operator inspect and control the service?
- [ ] Which roles permit inspection, deployment, restart, restore, rotation, and deletion?
- [ ] How does an authorized operator request, verify, and relinquish access?
- [ ] How does an operator start, stop, drain, restart, upgrade, roll back, and observe the result?
- [ ] Which actions are destructive, require approval, or provide a safe preview?
- [ ] Which configuration values does the service require or accept? Link their defaults, source, validation, secret status, and reload behavior.

## Operational and scaling risks

- [ ] What scaling issues can occur?
- [ ] Which dependencies are hard or soft? How does each failure affect the service?
- [ ] For each external dependency, where are its owner, status, limits, authentication, and degraded behavior documented?
- [ ] What is the blast radius if the feature fails?
- [ ] Does the design have a single point of failure? If yes, how is it handled?
- [ ] How easily can the service scale?
- [ ] Will the service scale horizontally, vertically, or both?
- [ ] Which scheduled jobs, queues, refreshes, and maintenance tasks run?
- [ ] How does an operator observe, cancel, and safely resume background work?

## SLA, SLO, and SLI

- [ ] Is a service-level agreement (SLA) defined? Which service-level indicators (SLIs) support it?
- [ ] Is the SLA published to its intended audience?
- [ ] Which service-level objectives (SLOs) support the SLA?
- [ ] Which SLIs map to each SLO?
- [ ] Can every SLI be measured?

## CI/CD

- [ ] Does the build produce artifacts?
- [ ] Are artifact definitions version controlled?
- [ ] Is the same artifact promoted through development, staging, and production?
- [ ] Where are artifacts stored? How long are they retained?
- [ ] Is there a continuous integration and deployment process?
- [ ] Does continuous integration include these controls?
  - [ ] Linting
  - [ ] Unit tests
  - [ ] Security tests
  - [ ] Code scanning, such as SonarQube or an equivalent
- [ ] How are artifacts labeled? Which tags does the registry retain, such as `latest` and semantic versions?
- [ ] What is the intended release frequency?
- [ ] Is the release process automated? List each manual step.
- [ ] Does the release cause downtime? If yes, what is the expected duration?
- [ ] How long does rollback take?
- [ ] Which application, schema, worker, or client changes prevent mixed-version operation or rollback?
- [ ] What signal stops a rollout? Link the latest rollback exercise for the release artifact.
- [ ] Which deployment strategy does the service use: blue-green, canary, A/B, recreate, shadow, or another strategy?

## Database

- [ ] Does the service use a database?
- [ ] Which stores hold authoritative, cached, derived, local, or temporary state?
- [ ] What can be regenerated, what must be preserved, and which operation owns each mutation?
- [ ] Has the database owner reviewed the schema?
- [ ] Has the database owner reviewed the queries?
- [ ] What is the expected data growth rate?

## Patching

- [ ] How often is the service patched?
- [ ] Is patching automated? List each manual step.
- [ ] Is there a runbook for patching the service, infrastructure, and applications?
- [ ] Does patching cause downtime? If yes, what is the expected duration?

## Security and compliance

### Design

- [ ] Does the service follow the applicable security policy?
- [ ] Does the service use HTTPS for communication?
- [ ] How are certificates managed? Does renewal occur automatically?

### Infrastructure

- [ ] Does the service add infrastructure resources?
- [ ] Does infrastructure as code create the required resources, with Terraform or an equivalent tool?
  - [ ] Does a security analysis tool check the infrastructure code?
  - [ ] Where is the state file stored? Who can access it?
  - [ ] Is the remote state backed up?
  - [ ] Is state history or versioning enabled?
  - [ ] Does the state contain secrets?
- [ ] Does a configuration management tool, such as Ansible, manage the service?
  - [ ] How are variables and secrets supplied?
- [ ] Do network security policies apply?
  - [ ] Do firewall rules apply least privilege?
  - [ ] Can the service mitigate a distributed denial-of-service attack?
  - [ ] Is the service behind an intrusion detection or prevention system?
  - [ ] Is the service behind a web application firewall?

### Development and operations

- [ ] Does any traffic use unencrypted HTTP?
- [ ] Which TLS version does the service use?
- [ ] Does the pipeline run security scans?
- [ ] Are all secrets encrypted at rest and in transit?
- [ ] Does the service add authentication or authorization?
- [ ] Does the service apply least privilege?
- [ ] Do audit logs record data access?
- [ ] Is the service containerized?
  - [ ] Are container files and images scanned with tools such as Hadolint, KICS, or Checkov?

### Logs

- [ ] Can logs contain secrets?
- [ ] Are logs sanitized to remove sensitive customer information?

### Compliance

- [ ] Which legal or regulatory requirements apply?

## Performance

- [ ] Can the service affect data-path performance when enabled?
- [ ] Does the service apply throttling, such as rate limiting?
- [ ] What does the customer experience when the service reaches a limit?
- [ ] What warning and failure thresholds apply to memory, CPU, disk, payloads, queues, concurrency, egress, quotas, and cost?
- [ ] Which resource fails first, and does exhaustion preserve authoritative state?
- [ ] Do internal and external dependencies use retry and backoff policies?
- [ ] Can the service operate during a sudden traffic spike?

## Backup and restore

- [ ] Is the service stateful? If yes, what is the source-of-truth data store?
- [ ] Is there a backup process?
- [ ] Are backups full, differential, incremental, or a combination?
- [ ] Where are tier 0, 1, 2, and 3 backups stored? What are their recovery objectives?
- [ ] Are backups monitored? Link the dashboard.
- [ ] What is the backup retention period?
- [ ] Has a restore from backup passed a test?
- [ ] How often are backups created?
- [ ] How much data can be lost after restoration from the latest backup?

## Observability

### Metrics

- [ ] Does the service expose metrics?
- [ ] What does healthy operation look like, and which signal should an operator inspect first?
- [ ] Which ranges, delays, queue depths, and freshness values are normal?
- [ ] Do the metrics support the SLOs?
- [ ] Do the metrics support request rate, error rate, and duration analysis?

### Logs

- [ ] Does the service emit logs?
- [ ] Are logs sent to a central logging system?
- [ ] Can logs expose secrets or personally identifiable information?
- [ ] Which logs use JSON format?
- [ ] Can the observability platform correlate the logs?

### Traces

- [ ] Which platform stores traces?
- [ ] Can traces expose sensitive information?

### Alerts

- [ ] Do alerts trigger when an SLO is not met?
- [ ] Does each alert have a troubleshooting runbook? Link it.
- [ ] Which platform sends alerts?
- [ ] Is alert configuration version controlled?
- [ ] Are alerts routed to the correct platform, channel, and team?
- [ ] Do alert thresholds cover each SLO?
- [ ] Is there a threshold for an official customer outage notification?
- [ ] Do alerts trigger when SLA-related SLIs are not met?

### Dashboards

- [ ] Does a dashboard show service performance? Link it.
- [ ] Are dashboard definitions version controlled?
- [ ] Does a dashboard show request rate, error rate, and duration?

## Responsibility

- [ ] Which team owns production reliability?
- [ ] Who is the service owner?
- [ ] Is there a responsibility assignment matrix? If not, why not?
- [ ] Who are the subject-matter experts?

## On-call and incident response

- [ ] Is someone from the development team on call?
- [ ] What periods does on-call coverage include?
- [ ] Does the rotation use follow-the-sun shifts?
- [ ] Is the on-call rotation adequately staffed?
- [ ] Does each on-call person have training for the relevant alerts?
- [ ] How are incidents escalated? Which channel handles on-call support?
- [ ] Does the service have a private or public status page?
- [ ] Does each expected incident or alert have a runbook?
- [ ] Which communication channel does the service use?
- [ ] Is on-call configuration version controlled?
- [ ] Does the service have prior postmortems? Link them.
- [ ] Which recurring faults, accepted risks, manual controls, temporary exceptions, and untested assumptions matter to an operator?
- [ ] For each credible failure, where is the direct symptom-to-diagnosis, containment, recovery, verification, and escalation procedure?
- [ ] How does an operator detect and reconcile partial success, duplicate work, cancellation, stale completion, or interrupted work?

## User impact and communication

- [ ] How do users distinguish stale, delayed, partial, unavailable, and lost results?
- [ ] What remediation can users perform safely?
- [ ] Which channel communicates incidents, maintenance, recovery, and unresolved data impact?

## Decommissioning

- [ ] How can operators disable and remove the service safely?
- [ ] How are data, credentials, jobs, integrations, storage, alerts, and retained artifacts exported, transferred, deleted, or revoked?

## Testing

- [ ] Did all required tests pass?
- [ ] Did load tests run? Which limits or breaking points did they establish?
- [ ] Were the predicted component failures tested? Include the failure test results.
- [ ] Which tests run in the continuous integration pipeline?

## Feedback

- [ ] Was this checklist useful?
- [ ] What is missing from this checklist?

## Follow-ups

| Result | Item | Owner | Due date | Evidence or accepted-risk record |
| --- | --- | --- | --- | --- |
| `Fail` / `Blocked` | `<item>` | `<owner>` | `YYYY-MM-DD` | `<link>` |
