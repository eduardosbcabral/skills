---
name: loop-broken-to-fixed
description: "Use when the user reports an exception, stack trace, failed CI check, broken behavior, browser failure, production error, performance regression, or other symptom and wants a diagnosis-to-fix loop with reproduction, sensor collection, smallest safe fix, and regression evidence. Do not use for vague product discovery or for a fully specified feature rule with no failure symptom."
---

# Broken To Fixed Loop

Run a controlled diagnosis loop from symptom to verified root-cause fix.

## Companion Skills

At start, check whether companion skills are available in the session. If a step would use a missing companion, say `missing companion skill: $name; using inline fallback` once and continue. Treat missing companions as blocking only when no inline/tool fallback can satisfy the step.

- Simplicity: `$ponytail`, `$ponytail-review`.
- Token efficiency: `$rtk-token-saver` (optional; compact noisy shell output when RTK is installed and exact raw output is not required).
- Diagnosis/direction: `$diagnosing-bugs`, `$grill-with-docs` (external companion), `$prototype`.
- Delivery/sensors: `$github:gh-fix-ci`, relevant security skills.
- Resumption: `$handoff` only when the loop must pause, move, or survive context loss.

## Start

1. Capture the exact symptom: error text, stack trace, failing check, URL/action, timestamp, environment, impact, and expected behavior.
2. Classify: tiny, normal, or large/risky. Use `references/loop-control.md` for non-tiny work, extended loops, automation, subagents, recurring work, or hands-off execution.
3. Schedule the solution discussion gate: reproduce or bound the failure first, then use `$grill-with-docs` before implementation when the fix changes expected behavior, contracts, data, permissions, UX, core rules, or risky direction. For tiny cause-specific fixes with clear expected behavior, skip this gate unless ambiguity or risk would make the loop encode guesses.
4. In a codebase, read local guidance before diagnosis: `AGENTS.md`, README, docs, runbooks, architecture notes, scripts, test conventions, and nearby implementations.
5. Load only needed references: `harness-contract.md` for sensors, `diagnosis-ledger.md` for non-tiny/competing hypotheses, `loop-prompts.md` for prompts/review gates, and `self-review.md` before final completion.

## Loop

1. Reproduce or bound the failure with a local test, command, browser flow, CI log, trace, or artifact.
2. Track one evidence-backed hypothesis at a time and name its falsification step.
3. Use `$rtk-token-saver` for noisy test/log/CI summaries when available; switch to raw output for exact stack traces, compiler diagnostics, snapshots, traces, or security detail.
4. Record mode, state, objective verifier, hard stop, sensors, and human approval gates.
5. Inspect the smallest relevant code path and caller set before editing.
6. Apply the embedded Ponytail gate: fix once at the shared root cause, prefer existing code/stdlib/native/installed dependency, and avoid broad refactors. Never choose a tiny diff that only patches the named symptom while sibling paths remain broken.
7. Patch the smallest cause-specific fix.
8. Self-review against root cause, scope, edge cases, regression evidence, and project conventions.
9. Verify the original symptom is gone and add or identify regression evidence.
10. Run the build/lint gate for app code when available; record unavailable/too-costly gates and nearest proxy.
11. Run the simplicity review gate: use `$ponytail-review` when available, otherwise inline-check for unnecessary dependency, abstraction, wrapper, dead flexibility, stdlib/native miss, or larger-than-needed diff.
12. Run the correctness review gate: use `loop-rule-reviewer` for normal/risky code, data, permission, concurrency, performance, or regression changes; inline fallback only after recording subagent discovery/fallback evidence.
13. Fix blocking review findings, then rerun the original symptom or affected regression/build gates.
14. Ask before opening a PR unless already requested. After push/PR, monitor CI/CD when local pipeline coverage was incomplete and CI/CD exists, or record that CI/CD is unavailable/delegated.
15. Update persistent state only for automated, recurring, multi-thread, or resumable loops.
16. End with decision: done, continue with a new hypothesis, ask, escalate, or stop; include root cause, verifier, build/lint, simplicity review, correctness review, PR/CI status, state update, and residual risk.

## Subagents

Use subagents only when they materially improve diagnosis, sensor collection, implementation, or independent review. Skip for tiny fixes and avoid parallel write-heavy edits. Preferred agents: `loop-bug-diagnoser`, `loop-harness-sensor`, `explorer`, `worker`, and `loop-rule-reviewer`. If unavailable, record the blocker and execute the role inline without pretending a separate review happened.

## Done

Done means: root cause is evidence-backed or uncertainty is explicit; smallest safe fix is applied; symptom or mitigation is verified; regression evidence exists or gap is named; Ponytail/simplicity gate applied; self-review and review gates have no blocking findings; objective verifier and build/lint gate are recorded; PR/CI decision is handled when relevant; state is updated if resumable; risky follow-up is separated from the fix.
