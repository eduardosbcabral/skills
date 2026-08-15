---
name: claude-loop-orchestration
description: "Use in Claude Code for software work that starts as a rough idea, a scoped implementation, or an observable failure. Automatically choose the path, use bounded custom subagents only when worthwhile, verify proportionally, and drive authorized work to an evidence-backed result. Do not use for notes, research, documentation-only work, personal planning, or skill and prompt maintenance."
---

# Claude Loop Orchestration

Keep the primary conversation as parent. The model selected by the user remains the coordinator. The parent owns scope, permissions, synthesis, diff inspection, and final acceptance.

## Route

Classify the entry without asking the user to choose a mode:

- **idea:** behavior, architecture, or the first useful slice is unsettled;
- **change:** expected behavior and scope are already settled;
- **failure:** observed software behavior differs from expected behavior.

Classify the task as **tiny**, **normal**, or **risky**. Risky work includes auth, money, data, permissions, concurrency, migrations, security, destructive behavior, and public contracts. Move between entries inside this loop as evidence changes.

## Frame

1. Read `CLAUDE.md` guidance and inspect the smallest relevant code path, tests, and current behavior.
2. Define the objective, expected and rejected behavior, scope, and cheapest useful verifier. Skip fields that do not help a tiny task.
3. Answer discoverable questions from evidence. Ask the user only for decisions that materially change behavior or risk.
4. Respect current authorization. Analysis does not authorize edits, and local edits do not authorize commit, push, deploy, or external writes.

## Delegate

Use non-fork custom subagents only when independence or a fresh context saves meaningful work:

- `claude-loop-advisor`: read-only architecture, difficult decisions, root-cause analysis, and final review;
- `claude-loop-worker`: substantial bounded discovery, evidence collection, implementation, and focused verification.

Pass only this packet:

```text
OBJECTIVE
OWNERSHIP
CONSTRAINTS
VERIFICATION
STOP CONDITIONS
```

Require workers to return `STATUS`, `CHANGES`, `EVIDENCE`, and `GAPS`. Advisors follow the verdict contract in their profile. Do not delegate tiny work. Keep at most one writer active. If a subagent fails to start once, do not retry it; continue in the parent when safe and name the independence gap. Missing independent review blocks Done only for risky work.

## Execute

- For an idea, settle the smallest useful vertical slice before implementation. If implementation was not requested, return the settled contract and stop.
- For a change, implement only the agreed behavior at the narrowest correct shared point.
- For a failure, reproduce or bound it, separate evidence from inference, and fix the root cause rather than the named symptom.

Choose the smallest correct change. Preserve concurrent edits and project conventions. A worker must stop when ownership conflicts, scope expands, or a material decision is missing. Treat subagent reports as claims; the parent inspects the actual diff and evidence.

## Simplicity

When Ponytail is available, keep its active mode for code-changing work. Fold `/ponytail-review` into the existing final review only when the candidate adds an abstraction, dependency, wrapper, configuration surface, or avoidable file; do not create another stage.

Keep `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, and `/ponytail-help` explicit-only.

## Output Economy

Before a shell-heavy phase, load `/rtk-token-saver` once and probe as it directs. Pass exactly `RTK: enabled` when usable or `RTK: raw` otherwise in worker `CONSTRAINTS`. Continue raw without setup or retries.

RTK may compress command output; it never lowers the required evidence. Use raw output when exact details or delivery truth matter.

## Verify

- Use the cheapest verifier that proves the changed behavior.
- Run focused evidence during iteration. Run a broad build, lint, typecheck, test, or integration gate once per materially changed candidate, near the end and only when risk or changed surface justifies it.
- Make one safe, reversible attempt to satisfy the evident missing prerequisite. If the harness remains unavailable, record the gap; do not rotate toolchains or mutate project configuration only to make the verifier run.
- Classify failures before acting. Repeat an expensive command only after a relevant change.
- After the same result twice, change strategy, change sensor, or report the blocker. Never make a third identical attempt.
- Do not turn unrelated failures into new work. Block Done only when no available evidence proves the requested behavior or an explicit acceptance or delivery gate remains unmet. Otherwise finish with the verification gap named.

## State

Keep normal task state in the parent conversation. Persist `.agent-loop/state.md` only before a real pause or cross-session resume. Record objective, entry, risk, phase, acceptance, completed evidence, last result, blocker, and next action. Do not create a journal or failure hash. Subagents never own state.

## Review And Done

After parent verification, start a fresh `claude-loop-advisor` review for normal or risky change sets. Skip it for tiny mechanical work. Require `ship`, `fix-first`, or `rethink`. Any implementation change invalidates the prior verdict; re-review only the affected result.

Done means requested behavior is satisfied, verification passed or honest gaps are named, the diff stayed scoped, and no blocking review finding remains. Perform delivery only when authorized. Report outcome, evidence, residual risk, and delivery status without a process diary.
