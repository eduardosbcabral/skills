---
name: loop-change-to-done
description: "Use when the user gives a small or medium scoped change, business rule, feature rule, validation rule, permission rule, UI behavior, or implementation request and wants it implemented with acceptance examples, focused verification, and durable rule capture when needed. Do not use for vague product discovery or for bug reports centered on an exception, failing CI check, or broken runtime symptom."
---

# Change To Done Loop

Turn one desired change into the smallest correct, verified result. Most small changes should finish in one iteration.

## Companion Skills

At start, check whether companion skills are available in the session. If a step would use a missing companion, say `missing companion skill: $name; using inline fallback` once and continue. Treat missing companions as blocking only when no inline/tool fallback can satisfy the step.

- Simplicity: `$ponytail`, `$ponytail-review`.
- Token efficiency: `$rtk-token-saver` (optional; compact noisy shell output when RTK is installed and exact raw output is not required).
- Direction/domain: `$grill-with-docs` (external companion), `$domain-modeling`, `$prototype`.
- Delivery/sensors: `$github:gh-fix-ci`, relevant security skills.
- Planning outputs: `$to-issues`, `$handoff` only when tickets or resumable handoff are actually needed.

## Start

1. Restate the change as actor, trigger, condition, expected outcome, rejected outcome, and edge cases when applicable.
2. Classify: tiny, normal, or large/risky. Use `references/loop-control.md` for non-tiny work, extended loops, automation, subagents, recurring work, or hands-off execution.
3. Run the solution discussion gate before implementing normal/risky changes: use `$grill-with-docs` to challenge direction, domain terms, acceptance examples, risky decisions, and solution shape. For tiny changes, skip this gate unless ambiguity or risk would make the loop encode guesses.
4. In a codebase, read local guidance before editing: `AGENTS.md`, README, docs, architecture notes, scripts, test conventions, and nearby implementations.
5. Load only needed references: `harness-contract.md` for sensors/verification, `change-ledger.md` for normal/risky changes, `loop-prompts.md` for prompts/review gates, and `self-review.md` before final completion.

## Loop

1. Inspect current behavior and nearby patterns.
2. Convert the change into acceptance examples, including negative/edge examples when useful.
3. Record mode, state, objective verifier, hard stop, sensors, and human approval gates.
4. Use `$rtk-token-saver` for noisy repo inspection, tests, lint, build, CI, or logs when available; use raw output when exact diagnostics or full detail matters.
5. Apply the embedded Ponytail gate before coding: reuse existing code, stdlib, native platform, or installed dependency before new code; write the fewest files that satisfy the change. Never cut explicit business rules, trust-boundary validation, security, accessibility, data-loss handling, or required checks.
6. Implement the smallest scoped change at the narrowest correct point.
7. Self-review against the requested change, acceptance examples, scope, edge cases, and project conventions.
8. Verify with the tightest evidence: focused test, typecheck, lint, build, CLI, browser/API check, or CI.
9. Run the build/lint gate for app code when available; record unavailable/too-costly gates and nearest proxy.
10. Run the simplicity review gate: use `$ponytail-review` when available, otherwise inline-check for unnecessary dependency, abstraction, wrapper, dead flexibility, stdlib/native miss, or larger-than-needed diff.
11. Run the correctness review gate: use `loop-rule-reviewer` for normal/risky code or behavior changes; inline fallback only after recording subagent discovery/fallback evidence.
12. Fix blocking review findings, then rerun affected verification and build/lint gates.
13. Ask before opening a PR unless already requested. After push/PR, monitor CI/CD when local pipeline coverage was incomplete and CI/CD exists, or record that CI/CD is unavailable/delegated.
14. Update persistent state only for automated, recurring, multi-thread, or resumable loops.
15. Capture durable rule/change knowledge only when business-significant.
16. End with decision: done, continue, ask, escalate, or stop; include verifier, build/lint, simplicity review, correctness review, PR/CI status, state update, and residual risk.

## Subagents

Use subagents only when they materially improve exploration, implementation, sensor collection, or independent review. Skip for tiny tasks. Preferred agents: `explorer`, `worker`, `loop-harness-sensor`, `loop-rule-reviewer`, and `loop-domain-extractor`. If unavailable, record the blocker and execute the role inline without pretending a separate review happened.

## Done

Done means: acceptance examples satisfied; relevant checks passed or gaps named; change stayed scoped; Ponytail/simplicity gate applied; self-review and review gates have no blocking findings; objective verifier and build/lint gate are recorded; PR/CI decision is handled when relevant; state is updated if resumable; durable docs are added only when useful.
