---
name: saas-backend-patterns
description: Use when maintaining, implementing, reviewing, or refactoring a .NET vertical-slice SaaS API while preserving Minimal API, MediatR, FluentValidation, EF Core, PostgreSQL, provider integration, background worker, and risk-based testing patterns.
---

# .NET Vertical-Slice Backend Patterns

Use this skill to maintain a .NET backend shaped around feature slices, application workflows, domain entities, infrastructure adapters, and external providers.

The goal is to preserve clear ownership and current architectural patterns before changing behavior.

## When Not To Use

Do not use this skill for:

- frontend-only tasks
- non-.NET backends
- purely cosmetic docs edits
- one-line mechanical changes that do not affect ownership, behavior, tests, or architecture
- broad security reviews that need a dedicated security workflow

## Report-Only Requests

When the user asks for analysis, review, mapping, or recommendations, do not edit files.

Produce the report first and wait for explicit approval before creating or changing artifacts.

## First Pass

Inspect these files first when they exist:

```text
AGENTS.md
backend/AGENTS.md
docs/backend/ARCHITECTURE.md
docs/backend/DATA_ACCESS.md
docs/backend/TESTING_GUIDELINES.md
docs/ERROR_CODES.md
backend/Makefile
backend/src/*/Program.cs
```

If the repo has local `AGENTS.md` files or `.agents/skills`, treat them as the source of truth and use this skill only as stack-level support.

Then map:

- framework and package versions
- request pipeline
- feature/module folders
- persistence pattern
- error model
- auth/tenant model
- background jobs
- provider boundaries
- test projects and commands
- repo-specific file-ordering rules

## Owner Map

Before changes or recommendations, identify the current owner for each relevant behavior:

- HTTP endpoint slice
- handler or application workflow
- domain entity or aggregate method
- specification/query owner
- provider adapter or webhook edge
- background worker
- test suite
- documentation file

If ownership is unclear, report that as a finding before proposing a design.

## Architecture Map

Classify code by responsibility:

- `Features/`: HTTP-facing slices, endpoint groups, request/response types, validators, handlers, feature-local specifications
- `Application/`: cross-slice workflows, billing/notification/orchestration services, event handlers
- `Domain/`: entities, enums, domain events, state transitions, aggregate behavior
- `Infrastructure/`: EF Core, migrations, DI, hosted workers, observability, storage, provider adapters
- `External/`: provider payloads, Refit clients, webhook contracts, low-level API models

Most changes should stay in one feature slice plus its tests. Move into `Application/` only when the workflow truly crosses feature ownership.

Use action-named feature files inside each feature folder. A route aggregator such as `SuperAdminEndpoints.cs` may own the shared route group, tags, authorization policy, and route-to-handler mapping, but it should not contain feature logic. Each actual feature should live in a file named after the action, such as `CreateTenantUser.cs`, `ListTenants.cs`, `GetAdminDashboard.cs`, or `UpdatePlatformSettings.cs`.

Each action-named feature file should keep its own `Request`, `Response`, validation metadata or validator, and `HandleAsync` handler together. Do not collect request/response contracts in broad `*Contracts.cs` files, `Program.cs`, or a large endpoint file. Do not group multiple features inside broad endpoint files such as catalog, admin, CRM, settings, or similarly generic catch-alls.

Preserve repo-specific ordering rules, especially implementation-first ordering when it is documented.

## Request Flow

Look for this pattern:

1. endpoint group maps route
2. endpoint creates or forwards a MediatR request
3. FluentValidation validates the request
4. handler loads state and applies business rules
5. handler returns `Result<T>`
6. result maps to HTTP response and Problem Details

Keep HTTP formatting out of handlers. Keep business failures structured with error codes.

Endpoint groups may also own route/body/form composition, simple parse guards, access profiles, and route names. Preserve local authorization helpers such as authenticated-user, tenant-manager, public-token, webhook, or provider-callback access profiles when they exist.

Map route groups through extension methods on `IEndpointRouteBuilder`; do not bury endpoint registration inside handlers or infrastructure services.

## Validation And Entitlements

Prefer slice-local FluentValidation validators for request shape and business input rules.

If the project uses MediatR behaviors for validation, entitlements, limits, or module gates, keep that behavior centralized. Do not recreate entitlement checks as ad hoc endpoint filters or duplicated handler branches unless the local pattern already requires it.

When request records carry attributes for module or usage limits, preserve that attribute-driven flow and add tests at the handler/behavior layer.

## Data Access Review

Prefer:

- repository plus specification pattern
- feature-local specifications for feature-owned reads
- application specifications for reusable workflow reads
- EF migrations for schema changes

Flag:

- direct ad hoc EF queries inside handlers when the project convention forbids them
- oversized catch-all specifications
- query logic inside endpoint mapping
- bypassing repository conventions for ordinary feature work
- schema changes without docs and tests

Direct `DbContext` use is not automatically wrong, but it must match the project's conventions and have a clear owner.

Allow direct `DbContext` only for explicit exceptions such as infrastructure polling or atomic claims, auth/security lookups, seeding, health checks, integration-test setup/assertions, stale-tracking refreshes, or rich include cases that are already documented by nearby code. Ordinary feature reads should use repository/specification conventions.

Specifications should encode tenant predicates and includes close to the feature that owns the read.

## Tenant And Access Context

Tenant context is usually claim or middleware based, but handlers still need to validate access to loaded tenant-owned resources.

When a project supports a master tenant, impersonation header, or tenant switcher flow, treat it as a first-class access mode. Preserve the distinction between the actor tenant and the effective tenant for queries, logs, and authorization.

## Provider Boundaries

For Stripe, payment gateways, WhatsApp, email, storage, AI, or similar providers:

- keep provider payload names near the edge
- normalize into internal models before workflow logic
- keep compatibility fallbacks narrow and evidence-based
- use deterministic fakes in automated tests
- avoid real external calls in local unit/integration tests

Webhook entrypoints should parse, verify, normalize, and delegate. Core workflows should not become provider-payload parsers.

Provider webhook and callback endpoints should own provider authentication, raw payload names, compatibility parsing, correlation extraction, logging, and HTTP status mapping. Normalize into internal identifiers or events before invoking billing or application workflows.

## Background Jobs

Identify whether jobs are:

- queue-backed
- database-polling
- provider-polling
- event-triggered

Prefer feature-owned polling when the durable row already contains scheduling/retry state. Do not add a generic queue unless it removes real complexity.

Hosted workers should claim due work, reload current state, run a narrow workflow, and persist status/retry changes.

When batch claiming or skip-locked style concurrency is needed, direct persistence APIs can be appropriate in infrastructure workers. Keep that exception contained and test the claim/retry behavior.

## Complexity Hotspot Score

Score risky areas by looking for:

- high line count
- many injected dependencies
- provider calls plus persistence in the same class
- retries, locks, state transitions, and policy selection in one place
- generic names like `Manager`, `Processor`, `Dispatcher`, `Resolver`, or `Orchestrator`
- hidden state or date/time assumptions
- weak or missing focused tests

Classify findings as:

- `Architecture`
- `Data Access`
- `Workflow`
- `Provider Edge`
- `Tests`
- `Docs`

Prefer deleting branches, narrowing owners, and renaming around business behavior before adding abstractions.

## Testing Expectations

Find the project-approved commands before running tests. Prefer Makefile or repo scripts over raw `dotnet test` when documented.

If Makefile targets are documented as canonical, use them instead of raw `dotnet test`.

Typical layers:

- unit tests for entities, validators, handlers, application services, event handlers
- integration tests for HTTP, real persistence, auth/tenant behavior, critical billing/payment flows
- deterministic provider doubles for external integrations
- integration tests with migrations, real persistence, reset isolation, disabled hosted services, fake auth, and deterministic fakes when the project has that harness

For risky changes, identify which behavior is protected by which test. Passing tests are not enough if they do not cover the changed workflow.

## Documentation Rule

Runtime behavior belongs in docs.

AI execution guidance, refactor heuristics, and process rules belong in skills or agent instructions.

If behavior changes, inspect the relevant existing docs and update them only after implementation is approved.

## Completion Checklist

Before calling backend pattern work complete, verify:

- owner map is present
- architecture shape is grounded in files
- package/runtime stack is identified
- data-access conventions are checked
- endpoint access profiles and route naming conventions are checked
- validation and entitlement behaviors are checked
- tenant/master-tenant/impersonation behavior is checked when relevant
- provider boundaries are mapped
- background jobs are mapped when relevant
- tests and commands are identified
- risks are backed by concrete evidence
- recommendations preserve current conventions unless a change is justified

## Output Contract

Return:

- concise architecture summary
- owner map
- evidence-backed file references
- current conventions to preserve
- risks or drift from those conventions
- recommended next actions
- validation commands that actually cover the task

Do not claim completion from broad tests or build success unless they cover the specific requirement.
