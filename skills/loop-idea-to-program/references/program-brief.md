# Program Brief

Use this for normal or large idea-to-program work.

## Source Separation

Keep source facts separate from interpretation:

```text
Source facts:
Assumptions:
Contradictions:
Unknowns:
Decisions needed:
Execution mode:
Objective verifier:
State location:
Hard stop:
```

## Domain Extraction

```text
Actors:
User workflows:
Domain terms:
Business rules:
Permissions:
Lifecycle states:
Integrations:
Data objects:
Non-functional constraints:
```

## Slice Plan

A good slice is vertical and verifiable. Prefer:

- user-visible or system-verifiable behavior;
- one primary actor/workflow;
- explicit acceptance evidence;
- minimal dependencies on future slices.

Template:

```text
Slice:
User/system outcome:
Rules covered:
Acceptance evidence:
Dependencies:
Risks:
Objective verifier:
```

## First Implementation Goal

Create a Codex goal only when the user explicitly asks for a goal or extended autonomous loop. Otherwise, write a normal phase goal in the response or planning artifact.

Good phase goal:

```text
Outcome:
Scope:
Out of scope:
Verification:
Simplicity gate:
Build/lint gate:
Stop conditions:
Required user decisions:
State location:
Human approval gate:
PR decision:
Post-push CI/CD:
```

## Decision Gates

Stop for user input when the program changes:

- billing, payment, subscriptions, or financial obligations;
- auth, permissions, tenant boundaries, or data ownership;
- legal, compliance, privacy, or retention obligations;
- core workflow semantics where the customer document is ambiguous.
