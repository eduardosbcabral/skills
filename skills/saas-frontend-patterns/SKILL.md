---
name: saas-frontend-patterns
description: Use when maintaining, implementing, reviewing, or refactoring a client-rendered operational SaaS frontend with feature modules, shared API clients, component primitives, i18n, dashboard shell, navigation, styling, and UX patterns.
---

# Dashboard Frontend Patterns

Use this skill to maintain a dashboard-heavy SaaS frontend where correctness, data flow, component structure, styling consistency, and operational UX matter more than marketing composition.

This skill assumes the frontend is client-first. Prefer simple React, a client router, and a separate backend API over server-rendering architecture unless the project explicitly needs SSR, file-based server routing, edge middleware, or server actions.

Treat repository-specific `AGENTS.md`, docs, and local skills as the source of truth; use this skill as stack-level support.

## When Not To Use

Do not use this skill for:

- server-rendered frontend architecture work
- backend-only tasks
- static marketing sites
- purely visual one-off mockups
- framework migrations unless the user explicitly asks
- generic React advice disconnected from an existing codebase

## Report-Only Requests

When the user asks for analysis, review, mapping, or recommendations, do not edit files. Produce the report first and wait for explicit approval before creating or changing artifacts.

## First Pass

Inspect repo guidance and common frontend entrypoints when they exist:

```text
AGENTS.md
frontend/AGENTS.md
frontend/package.json
frontend/vite.config.*
frontend/tsconfig.json
frontend/src/app/
frontend/src/app/routes/
frontend/src/routes/
frontend/src/lib/api.*
frontend/src/services/api/*
frontend/src/features/
frontend/src/hooks/
frontend/src/components/
frontend/src/components/ui/
frontend/src/i18n/
docs/frontend/*.md
```

Map:

- React, router, and build tool versions
- package manager and scripts
- route tree
- dashboard shell
- sidebar and navbar ownership
- API boundary
- auth/session model
- account, organization, workspace, or tenant context
- i18n structure
- UI component system
- styling conventions
- validation commands
- test coverage or lack of it

## Route And Shell Map

Before changes or recommendations, identify:

- route groups and dashboard routes
- root layout and dashboard layout
- auth/public routes
- shell components such as sidebar, header, navbar, banners, context switcher, command palette, and account menu
- source of truth for navigation
- source of truth for route metadata and breadcrumbs
- where loading/error states live

Flag stale starter-template routes, navigation, placeholder data, or duplicate route models.

## Sidebar And Navbar Review

When the app has a sidebar, navbar, or dashboard shell, inspect it as a first-class UX system.

Map:

- sidebar ownership and file location
- navbar/header ownership and file location
- mobile sidebar or drawer behavior
- collapsed and expanded sidebar states
- account, organization, workspace, or tenant switchers
- account menu and logout flow
- notification or announcement areas
- command palette entrypoints
- route active-state logic
- breadcrumbs and page title source
- nav item permissions, feature flags, or context visibility rules
- where nav labels and metadata are translated

Prefer one clear source of truth for route metadata, nav labels, icons, breadcrumbs, and active matching.

When the current app splits these responsibilities, compare all sources together before changing navigation: sidebar item arrays, route dictionaries, metadata helpers, breadcrumb fallback logic, dynamic breadcrumb context, command palette entries, and page headers.

Flag:

- sidebar and navbar using separate duplicated route lists
- stale starter-template nav items
- hardcoded labels that bypass i18n
- active states that fail on nested routes
- nav items visible to users without permission
- mobile nav that hides primary actions or current account context
- shell components that fetch unrelated feature data
- account/logout state split across local storage, cookies, and providers
- duplicated route labels or active-state rules across sidebar, breadcrumbs, metadata, command palette, and page headers

## Shell UX Patterns

For operational SaaS dashboards, the shell should make orientation and repeated work fast.

Check that:

- the current account, organization, workspace, or tenant context is always visible when relevant
- primary navigation is stable across dashboard routes
- secondary navigation does not fight page tabs
- page title, breadcrumbs, and sidebar active state agree
- global actions live in the navbar/header, not inside unrelated pages
- destructive account actions are not exposed as casual nav clicks
- collapsed sidebars preserve recognizable icons and tooltips
- mobile shell keeps navigation, context, and logout reachable
- loading states do not cause the sidebar/header to jump
- cookie state, context switcher state, banners, reminders, and local-storage dismissal state do not contradict each other

Avoid turning the shell into a marketing surface. Keep it quiet, predictable, and work-focused.

## Architecture Map

Classify code by responsibility:

- `src/app/` or the chosen router convention: route registration, route files, route layouts, redirects, and guards only
- `src/app/routes/` or `src/routes/`: one route-page file per page when the router is not file-system based
- `src/features/`: feature-specific page views, listings, forms, tables, dialogs, hooks, schemas, helpers, and copy
- `src/components/`: reusable UI, shell, layout, and cross-feature components
- `src/components/ui/`: primitive UI wrappers such as shadcn/Radix components when present
- shared API module: client fetch/auth/error/result boundary
- `src/hooks/`: shared client behavior and data loading hooks
- `src/i18n/`: dictionaries, lookup helpers, translation context
- `src/types/`: shared frontend API contracts

Route files should stay thin. Prefer composing client feature modules and layouts. Keep routing, auth guards, query parsing, and loader boundaries explicit and easy to replace.

## Page And Feature File Pattern

Prefer one page or route entry per file. For client-router apps, use a structure like:

```text
src/app/
  AppRoutes.tsx
  route-config.ts
  navigation.ts
  routes/
    <area>/
      <PageName>Page.tsx
src/features/
  <feature>/
    components/
      pages/
        <PageName>PageView.tsx
      <feature-area>/
        <FeaturePart>.tsx
      <feature>-tables/
        index.tsx
        columns.tsx
        cell-action.tsx
    hooks/
    utils/
      form-schema.ts
      filters.ts
    types.ts
```

For file-system routers, the equivalent route file can be `page.tsx`, but keep the same ownership: the route file owns route-level composition and the feature folder owns the screen behavior.

Route page files should be thin wrappers. They may compose layout, guards, route params/query parsing, page header, loading fallback, and one feature-owned page view or listing component. They should not contain table columns, modal workflows, form schemas, mutation bodies, API error parsing, or large screen-specific helper functions.

Feature page views should own the screen-level composition for one page. If a page view starts mixing fetching, derived state, mutations, polling, dialogs, table rendering, forms, and layout, split by concrete responsibility into feature-local components or hooks. Prefer names such as `<Entity>Listing`, `<Entity>Table`, `<Entity>Form`, `<Entity>DetailView`, `<Entity>Filters`, and `<Entity>Dialog` over generic `Manager`, `Panel`, or `Helper` names.

Do not create new pages in legacy `views/` folders when the app has moved to `app/routes`, `routes`, or a similar route-entry convention. Treat legacy view folders as migration targets, not as the place for new screens.

## UX Component Inventory

Before recommending frontend changes, map the screen-level component system:

- shell components: sidebar, header, navbar, context switcher, command palette, banners
- layout components: page headers, filters, tabs, drawers, dialogs, empty states
- data components: tables, cards, status badges, timelines, metric blocks
- form components: field wrappers, validation messages, submit bars, destructive confirmations
- feedback components: loading states, skeletons, toasts, inline errors, retry actions
- navigation components: breadcrumbs, route titles, active states, mobile navigation

Flag duplicated patterns, one-off variants, starter-template leftovers, and components that combine too many responsibilities.

## Component Structure

Prefer:

- one route/page file per page, kept as a thin route-level wrapper
- feature page views that own screen composition without becoming all-in-one workflow files
- feature folders that own page-specific UI, listings, tables, dialogs, hooks, schemas, helpers, and copy
- feature-local components and hooks before global shared abstractions
- shared components only when a pattern is used by multiple features
- primitive UI folders for low-level design-system wrappers
- small composition components over large screen files that do everything

Avoid:

- generic shared abstractions for one feature
- multiple unrelated pages in one file
- new screens in legacy view folders when route-entry folders exist
- colocating fetch, mutation, polling, modal state, table rendering, form schema, form rendering, and layout in one component
- creating new primitives when local conventions already cover the need
- framework-level server rendering for screen composition or data loading

## API Boundary

Prefer:

- one shared client HTTP layer for base URL, auth headers, account/context headers, Problem Details parsing, result shaping, and `204` handling
- client-side feature hooks for data loading and revalidation
- client fetches for initial screen state, interaction, polling, and post-render refresh
- no duplicated auth/error handling inside feature components

Do not introduce server actions, backend-for-frontend routes, or server-side API request paths by default. Use the separate backend API through the shared client API layer.

Check whether the implementation returns result objects or throws exceptions. Docs and code should agree.

For mutations in client forms, preserve the shared API result contract and route form/server errors through the existing form error helper.

## Auth And Context

Trace:

- where auth tokens are stored
- how client-side calls read auth state
- how account, organization, workspace, or tenant context is represented
- how delegated administration or impersonation is represented when present
- how logout clears mounted UI state
- how user/context data refreshes after switching context
- how middleware, cookies, local storage, and client providers interact

Flag split-brain states where middleware, cookies, local storage, and mounted dashboard components can disagree.

Context switching often spans cookies, local storage, auth claims, mounted user-data providers, and API headers. Trace all of them before changing switching, impersonation, or logout behavior.

## i18n Review

Prefer:

- typed dictionaries in source
- locale key parity
- route copy as metadata and breadcrumb source
- lookup helpers for runtime enum/status values
- no hardcoded user-facing strings in feature UI

Common namespaces:

- `ui` for shared primitives
- `lookups` for code-driven labels
- `features` for feature/page/component copy
- `public` for unauthenticated flows
- `routes` for metadata and breadcrumbs

Run or recommend the project i18n validation command when copy changes.

For forms, check both translated field labels and validation schema messages. If the project still has raw validation strings, avoid adding more drift.

## Operational UX Patterns

For dashboard-heavy SaaS screens, review whether the UI supports repeated work:

- lists should be scannable and sortable/filterable when the data volume requires it
- page headers should expose the primary action and current context
- status labels should be visually distinct and semantically consistent
- destructive or externally visible actions should require confirmation
- empty states should provide the next useful action, not marketing copy
- loading and error states should preserve layout stability
- forms should group related fields and show validation near the field
- mobile layouts should keep core actions reachable without hiding critical state

Do not turn operational screens into landing pages or decorative card stacks.

## Table Patterns

When the app uses TanStack Table or similar:

- preserve the shared table wrapper, toolbar, pagination, column header, filter, view-options, and skeleton components
- keep table implementations in feature-local table folders such as `<entity>-tables/` when that pattern exists
- keep `index.tsx`, `columns.tsx`, row/cell action files, and table-specific filters separate when the table has non-trivial behavior
- keep table state in the existing URL/query-state mechanism when present
- use translated column keys or labels consistently
- keep filter metadata on column definitions when that is the established pattern
- preserve horizontal overflow, sticky headers, pinned-column styling, and empty/loading states

Do not create a one-off table implementation for ordinary CRUD lists. Do not bury table columns and row actions inside the route page or page view when they can be named as feature-local table parts.

## Form Patterns

When the app uses React Hook Form, Zod, or similar form/schema tooling:

- keep feature-owned schemas, inferred value types, defaults, option lists, and form helpers under the feature, usually in `utils/form-schema.ts` or a similarly specific file
- keep form rendering in a feature-owned form component such as `<Entity>Form.tsx`
- use shared form field wrappers for inputs, selects, switches, dates, currency, files, and phone fields
- route API errors through the shared form error handler
- keep submit/cancel actions in the page header or form action area consistently
- keep destructive mutations behind dialogs or alert dialogs

Do not duplicate form control styling or validation plumbing inside feature components. Do not define large schemas, default-value builders, or mutation error mapping inside route page files.

## Styling And Design System Review

Inspect styling conventions before adding UI:

- Tailwind utility patterns when present
- CSS variables and theme tokens
- primitive/component-library usage
- icon library conventions
- spacing, radius, border, shadow, and density patterns
- dark/light mode behavior when present
- responsive breakpoints and container widths

Preserve the existing visual language unless the task is explicitly a redesign.

Flag:

- inconsistent spacing scales
- hardcoded colors that bypass tokens
- excessive shadows or card nesting
- oversized typography inside compact tools
- unreadable contrast
- text overflow on mobile
- layout shifts caused by dynamic labels, badges, or buttons
- duplicated custom variants of existing primitives

## Date And Money Semantics

For products with billing, scheduling, renewals, or financial values:

- treat business calendar dates as `yyyy-MM-dd` calendar values
- do not let browser timezone conversion shift due dates, start dates, renewal dates, or scheduled business dates
- format true instants, such as sent/scheduled timestamps, in the active account timezone when available
- compare "today" using the business timezone when overdue/due-today labels matter
- centralize currency and date formatting helpers

## UI Component Rules

Prefer existing primitives and local feature components before adding new shared abstractions.

Use:

- established primitive UI components for dialogs, menus, forms, tables, tooltips, and sidebars
- Tailwind utility classes and CSS variables for theme consistency when that is the local convention
- existing form wrappers and schemas for repeat form patterns
- icon libraries already installed in the project

Avoid:

- generic shared components for one feature-specific case
- hardcoded strings
- duplicated table implementations
- component files that combine fetching, polling, dialogs, mutations, and layout without a clear split
- framework-level server rendering for data loading
- new or expanded server-side request handlers for routine API calls

## Visual Validation

For UI or layout changes, validate the rendered screen when feasible.

Check:

- desktop and mobile viewport behavior
- no overlapping text or controls
- loading, empty, error, and success states
- dialogs, drawers, menus, and command palette interactions
- table overflow and sticky/fixed shell behavior
- translated copy length if i18n is present

## Validation

Find the project-approved validation set. Typical commands:

```bash
pnpm exec tsc --noEmit
pnpm i18n:check
pnpm build
pnpm lint
```

Prefer typecheck plus i18n check as the fast default when that is the documented workflow. Reserve full build for routing, config, production-only behavior, or explicit release checks.

If the build config suppresses TypeScript or ESLint failures, call out the compensating validation gate that must exist.

For visual/layout changes, run a browser smoke test against the rendered UI when feasible.

## Completion Checklist

Before calling frontend pattern work complete, verify:

- route and shell map is present
- page/file ownership is mapped, including route wrappers, feature page views, listings, tables, forms, schemas, hooks, and API boundary
- sidebar and navbar ownership are mapped when present
- route metadata, breadcrumbs, and active nav logic are checked
- sidebar, command palette, metadata helpers, breadcrumb fallback, and page headers are checked together when navigation changes
- mobile shell behavior is reviewed
- duplicated or stale navigation sources are called out if present
- API boundary is identified
- auth and context state sources are identified
- i18n conventions are checked
- component and styling conventions are checked against existing code
- table and form conventions are checked for CRUD/list/form work
- no server-side data path is introduced without an explicit project requirement
- UX conventions are checked against the actual screen type
- date/time/money semantics are checked when relevant
- validation commands are identified
- starter-template residue or stale navigation is called out if present
- risks are backed by concrete evidence

## Documentation Rule

Runtime behavior belongs in docs.

AI execution guidance, refactor heuristics, and process rules belong in skills or agent instructions.

If behavior changes, inspect the relevant existing docs and update them only after implementation is approved.

## Output Contract

Return:

- concise frontend architecture summary
- route, shell, sidebar, and navbar map
- UX component inventory when relevant
- evidence-backed file references
- current conventions to preserve
- risks or drift from those conventions
- recommended next actions
- validation commands that actually cover the task

Do not claim completion from broad tests or build success unless they cover the specific requirement.
