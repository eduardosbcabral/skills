---
name: loop-orchestration
description: "Use for software work that starts as a rough idea, a scoped implementation, or an observable failure and may require code, tests, build or CI behavior, application configuration, or software-infrastructure changes. Automatically choose the path, scale delegation and verification by risk, and drive authorized work to an evidence-backed result. Do not use for notes, research, documentation-only work, personal planning, or skill and prompt maintenance."
---

# Loop Orchestration

Keep the primary session as parent. The model selected by the user remains the coordinator. The parent owns scope, permissions, synthesis, diff inspection, and final acceptance.

## Route

Classify the entry without asking the user to choose a mode:

- **idea:** behavior, architecture, or the first useful slice is unsettled;
- **change:** expected behavior and scope are already settled;
- **failure:** observed software behavior differs from expected behavior.

Classify the task:

- **tiny:** local, mechanical, and unambiguous;
- **normal:** behavior changes within settled boundaries;
- **risky:** auth, money, data, permissions, concurrency, migrations, security, destructive behavior, or public contracts are involved.

Move between entries inside this loop as evidence changes. Do not invoke another loop skill.

## Frame

1. Read repository guidance and inspect the smallest relevant code path, tests, and current behavior.
2. Define the objective, expected and rejected behavior, scope, and cheapest useful verifier. Skip fields that do not help a tiny task.
3. Answer discoverable questions from evidence. Ask the user only for decisions that materially change behavior or risk.
4. Respect current authorization. Analysis does not authorize edits, and local edits do not authorize commit, push, deploy, or external writes.

## Delegate

Delegate only when independence or a fresh context saves meaningful work:

- `loop-advisor`: read-only architecture, difficult decisions, root-cause analysis, and final review;
- `loop-worker`: substantial bounded discovery, evidence collection, implementation, and focused verification.

Spawn a fresh role with no inherited turns. Pass only this packet:

```text
OBJECTIVE
OWNERSHIP
CONSTRAINTS
VERIFICATION
STOP CONDITIONS
```

Require workers to return `STATUS`, `CHANGES`, `EVIDENCE`, and `GAPS`. Advisors follow the verdict contract in their profile. Do not delegate tiny work. Keep at most one writer active. If a role fails to start once, do not retry it; continue in the parent when safe and name the independence gap. Missing independent review blocks Done only for risky work.

## Execute

- For an idea, settle the smallest useful vertical slice before implementation. If implementation was not requested, return the settled contract and stop.
- For a change, implement only the agreed behavior at the narrowest correct shared point.
- For a failure, reproduce or bound it, separate evidence from inference, and fix the root cause rather than the named symptom.

Choose the smallest correct change. Preserve concurrent edits and project conventions. A worker must stop when ownership conflicts, scope expands, or a material decision is missing. Treat worker reports as claims; the parent inspects the actual diff and evidence.

## Verify

- Use the cheapest verifier that proves the changed behavior.
- Run focused evidence during iteration. Run a broad build, lint, typecheck, test, or integration gate once per materially changed candidate, near the end and only when risk or changed surface justifies it.
- Make one safe, reversible attempt to satisfy the evident missing prerequisite. If the harness remains unavailable, record the gap; do not rotate toolchains or mutate project configuration only to make the verifier run.
- Classify a failure as product/code, environment/harness, unrelated/pre-existing, or unknown before acting.
- Repeat an expensive command only after a relevant code, configuration, environment, or hypothesis change.
- After the same result twice, change strategy, change sensor, or report the blocker. Never make a third identical attempt.
- Do not turn unrelated failures into new work. Block Done only when no available evidence proves the requested behavior or an explicit acceptance or delivery gate remains unmet. Otherwise finish with the verification gap named.

## State

Keep normal task state in the parent context. Persist `.agent-loop/state.md` only before a real pause or cross-session resume. Record objective, entry, risk, phase, acceptance, completed evidence, last result, blocker, and next action. Do not create a journal or failure hash. Subagents never own state. Remove transient state at Done only when this loop created it and no project convention owns it.

## Review And Done

After parent verification, use a fresh `loop-advisor` review for normal or risky change sets. Skip it for tiny mechanical work. Require `ship`, `fix-first`, or `rethink`. Any implementation change invalidates the prior verdict; re-review only the affected result.

Done means requested behavior is satisfied, verification passed or honest gaps are named, the diff stayed scoped, and no blocking review finding remains. Perform commit, push, PR, CI monitoring, deploy, or other delivery only when authorized. Report outcome, evidence, residual risk, and delivery status without a process diary.
