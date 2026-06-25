---
name: saas-project-bootstrap
description: Use when bootstrapping a full-stack multi-tenant SaaS project with a .NET API backend, simple client-rendered React frontend, runtime docs, AI execution skills, Docker local infrastructure, and CI/deploy workflows.
---

# .NET + React SaaS Bootstrap

Use this skill when creating a new full-stack SaaS project with:

- a .NET API backend
- a simple React frontend
- multi-tenant product assumptions
- runtime documentation
- optional AI execution skills

Keep the result practical. Prefer a small explicit structure over a framework-heavy template.

## When Not To Use

Do not use this skill for:

- non-.NET backends
- frontend-only apps
- static marketing sites
- server-rendered frontend architectures
- large platform templates that need many services from day one
- refactoring an existing project unless the user explicitly asks for bootstrap guidance

## Greenfield Or Existing Repo

First decide:

- **Greenfield**: create the minimum viable structure and conventions.
- **Existing repo**: preserve the current stack and add only missing pieces.

Do not replace a working architecture just to match this template.

If an existing repo has local `AGENTS.md` files or `.agents/skills`, treat them as the source of truth. Use this skill only as stack-level support.

## Target Structure

Use a root layout like:

```text
repo/
  AGENTS.md
  README.md
  docs/
    backend/
    frontend/
  .agents/
    skills/
  backend/
    AGENTS.md
    Makefile
    global.json
    nuget.config
    src/
    tests/
  frontend/
    AGENTS.md
    package.json
    src/
```

Use docs for runtime behavior. Use skills for AI execution rules and implementation heuristics.

## Backend Baseline

Use:

- .NET API
- Minimal APIs
- MediatR for request handling
- FluentValidation for request validation
- EF Core with PostgreSQL
- structured `Result<T>` for business outcomes
- Problem Details for HTTP errors
- Docker Compose for local dependencies
- Makefile targets for tests and migrations

Recommended folders:

```text
backend/src/<AppName>.Api/
  Program.cs
  Application/
  Domain/
  External/
  Features/
  Infrastructure/
  Settings/
backend/tests/
  <AppName>.Api.Tests/
  <AppName>.Api.IntegrationTests/
```

Prefer vertical slices in `Features/`: endpoint mapping, request/response types, validators, handlers, and feature-local specifications should be close together.

Use `Application/` only for cross-slice workflows and orchestration with a clear owner.

Use `External/` for provider payloads and low-level contracts.

Use `Infrastructure/` for EF Core, hosting, observability, provider adapters, storage, background workers, and dependency injection.

## Frontend Baseline

Use:

- React
- Vite or an equivalent lightweight build tool
- a client router such as React Router or TanStack Router
- TypeScript
- Tailwind CSS
- shadcn/Radix components
- client-rendered route screens
- client-side API requests through a shared API boundary
- feature modules under `src/features`
- route entries under `src/routes` or the router convention chosen for the app
- explicit i18n structure if multiple languages are needed

Do not use framework-level server rendering, server actions, or server-side API request paths as the default architecture.

Recommended folders:

```text
frontend/src/
  components/
  components/ui/
  features/
  hooks/
  i18n/
  lib/
  routes/
  types/
```

Keep route files thin. They should compose layouts, route shells, and feature components. Data loading should happen through client-side feature hooks or shared client API helpers.

Keep API/auth/error behavior in a client-safe shared API layer such as `src/lib/api.ts`.

## Documentation Baseline

Create only docs that the system needs immediately:

```text
docs/backend/ARCHITECTURE.md
docs/backend/DATA_ACCESS.md
docs/backend/TESTING_GUIDELINES.md
docs/frontend/API_ARCHITECTURE.md
docs/frontend/UX_UI_GUIDELINES.md
docs/frontend/I18N.md
docs/ERROR_CODES.md
```

Do not put AI-only process guidance in docs. Put that in `.agents/skills`.

Do not create release-note style docs during bootstrap.

## Local Tooling

Backend Makefile should expose:

```bash
make dev
make down
make test-unit
make test-integration
make test
make migration-add name=MeaningfulName
make migration-update
make migration-remove
```

Frontend package scripts should expose:

```bash
pnpm dev
pnpm build
pnpm preview
pnpm exec tsc --noEmit
pnpm i18n:check
```

Only add a frontend test runner when there is a real test suite.

## CI And Deployment

Start with separate backend and frontend workflows.

Backend CI should:

- install .NET
- build
- run unit tests
- run integration tests with real Postgres
- run migrations only in deploy workflows

Frontend CI/deploy should:

- install pnpm dependencies with frozen lockfile
- run typecheck and i18n checks
- build the frontend bundle
- package/deploy through the chosen hosting path

Avoid suppressing TypeScript or ESLint build failures unless there is a compensating CI gate.

## Root Agent Instructions

Create a short root `AGENTS.md` that states:

- project structure
- docs versus skills rule
- branching and commit convention
- documentation update rule
- preferred validation commands
- stack-specific library documentation lookup rules when applicable

## Guard Rails

- Keep the first version boring.
- Do not add a generic workflow engine.
- Do not add broad `Manager`, `Processor`, or `Helper` services without a narrow owner.
- Do not create docs that duplicate code or become release notes.
- Keep provider quirks at integration edges.
- Treat tenant calendar dates differently from instants when billing dates matter.
- Keep AI skills short and procedural; keep runtime behavior in docs.

## Completion Checklist

Before calling bootstrap complete, verify:

- root instructions exist
- backend restores and builds
- frontend installs and typechecks
- local dev commands are documented
- docs explain runtime behavior
- skills contain only AI execution guidance
- CI/deploy gates match the chosen stack
- no unnecessary template residue remains
- validation commands actually cover the generated structure

## Output Contract

Return:

- created structure summary
- key files and commands
- conventions established
- validation performed
- known gaps or intentional omissions
- next steps
