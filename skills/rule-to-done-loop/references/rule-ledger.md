# Rule Ledger

Use this for normal or risky behavior changes.

## Rule Shape

```text
Rule:
Actor:
Trigger:
Condition:
Expected outcome:
Rejected outcome:
Edge cases:
Business source:
Assumptions:
Unknowns:
Execution mode:
Objective verifier:
Hard stop:
```

## Acceptance Examples

Prefer concrete examples over broad prose:

```text
Given:
When:
Then:
Verification:
```

Include negative or boundary examples when the rule is about validation, authorization, money, state transitions, or data visibility.

## Implementation Record

```text
Current behavior:
Chosen implementation point:
Files/modules touched:
Checks run:
Simplicity gate:
Build/lint gate:
Review gate:
PR decision:
Post-push CI/CD:
State location:
Durable rule capture:
Residual risk:
```

## Review Gates

Add explicit review or user confirmation before changing:

- auth, permissions, tenant boundaries, or data visibility;
- billing, invoices, payment state, subscriptions, or financial calculations;
- migrations, destructive data operations, or irreversible workflows;
- public API contracts or customer-facing business semantics.
