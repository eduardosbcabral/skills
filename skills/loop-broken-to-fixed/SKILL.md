---
name: loop-broken-to-fixed
description: "Use when the user reports an exception, failed check, broken behavior, production error, performance regression, or another observable symptom and wants diagnosis through a verified cause-specific fix. Do not use for vague discovery or a specified feature with no failure symptom."
---

# Broken To Fixed Loop

Move from an observable failure to a verified root-cause fix.

## State Contract

- **Input:** a symptom plus the expected behavior or an objective way to discover it.
- **Output:** an evidence-backed cause, the smallest safe fix, and regression evidence.
- **Transition:** unclear expected semantics go to `Idea To Build`; a discovered feature or rule change goes to `Change To Done`.
- **Not done:** the named symptom disappeared but the cause, sibling paths, or regression risk remain unexplained.

Conversation and diagnosis do not authorize edits. Implementation, commit, push, PR, deploy, destructive operations, credentials, and external writes require the user's request or approval appropriate to that action.

## Optional Dependency

Before shell-heavy work, load and follow `$rtk-token-saver` when the skill and its external RTK CLI are available. It is an optional operational dependency, not a companion or embedded behavior. Use its current availability, fallback, fidelity, safety, and verification rules as the source of truth. If unavailable, continue with normal commands; do not install or configure RTK without explicit approval.

## Start

1. Capture the exact symptom, expected behavior, environment, trigger, impact, and available artifacts. Preserve exact errors.
2. Read repository guidance, runbooks, nearby code, tests, and deployment/runtime context relevant to the failure.
3. Classify the failure:
   - **tiny:** cause and verifier are obvious and local;
   - **normal:** reproduction or competing hypotheses are needed;
   - **risky:** production, security, auth, money, data, concurrency, performance, migrations, or public contracts are involved.
4. If expected semantics are uncertain, use `references/batch-grill-me.md` or transition to Idea To Build before changing behavior.
5. For normal/risky diagnosis, load `references/diagnosing-bugs.md` and keep `references/diagnosis-ledger.md` compact.

## Built-in Operating Rules

### Ponytail

Understand the real failure path and caller set, then fix the shared root cause once. Prefer existing code, the standard library, the native platform, or an installed dependency before new machinery. Do not choose a tiny diff that leaves sibling paths broken. Never cut trust-boundary validation, security, accessibility, data-loss handling, or necessary diagnostics.

### Ponytail Review

Review the fix only for removable complexity: `delete`, `stdlib`, `native`, `yagni`, or `shrink`. If none applies, record `Lean already. Ship.`

### Caveman

Keep progress and final prose terse: remove filler, hedging, pleasantries, repeated summaries, tool narration, decorative tables, emoji, and long raw logs. Fragments are fine. Preserve the user's language and preserve code, commands, API names, identifiers, and exact errors. Do not invent abbreviations or sacrifice clarity for security warnings, irreversible confirmations, ambiguity, or multi-step instructions.

## Subagents

Delegate bounded diagnosis, evidence, implementation, and review tasks when they improve independence; the parent owns the active hypothesis and synthesis.

- `loop-bug-diagnoser`: independently reproduce or bound normal/risky failures, rank hypotheses, and identify the smallest likely fix area.
- `loop-harness-sensor`: collect focused evidence from tests, CI, browser, logs, traces, or runtime sensors.
- `worker`: implement a clearly owned cause-specific fix when write ownership does not overlap.
- `loop-rule-reviewer`: independently review the fix against the root cause, expected behavior, scope, regression evidence, and risk.

For every normal/risky fix, delegated `loop-rule-reviewer` review is required before Done. For a tiny obvious fix, skip it only with a concrete reason. If a named custom agent is unavailable but subagents are supported, use a built-in `default` or `explorer` agent with the same bounded role and record the fallback. If no subagent facility exists, report the review gap instead of claiming delegated review passed. Do not run parallel writers on the same failure path.

## Loop

1. Build the tightest red-capable verifier: deterministic, fast enough to repeat, and able to fail before the fix. If reproduction is impossible, bound the failure with the best available artifact and name the evidence gap.
2. Minimize the scenario and inspect the smallest relevant execution path and callers.
3. Form ranked, falsifiable hypotheses. Test one variable at a time; discard hypotheses contradicted by evidence.
4. Add tagged temporary instrumentation only when existing sensors are insufficient. Baseline and profile performance failures before optimizing.
5. Add or identify regression evidence at the correct seam before the fix when practical.
6. Apply the smallest cause-specific fix with Ponytail.
7. Rerun the original scenario, focused regression evidence, and relevant build/typecheck/lint or integration checks.
8. Remove temporary logs, probes, flags, and prototypes.
9. Run Ponytail Review, then delegate correctness review according to the Subagents contract. Fix blockers, rerun affected evidence, and re-review affected areas.
10. Commit, push, open a PR, monitor CI, or deploy only when requested. If CI itself is the symptom, its focused rerun is verification, not optional delivery.

## Conditional Mode

Use `references/loop-state-and-stall-guard.md` for resumable diagnosis, external waits, automation, or repeated failed hypotheses. Before a third attempt with the same failure fingerprint, change hypothesis or strategy instead of repeating the action. This is an internal mode, not an installed-skill dependency.

## Done

Done means the cause is evidence-backed or the uncertainty is explicit; the smallest safe fix is applied; the original symptom and regression seam are verified or honest gaps are named; temporary instrumentation is gone; and no blocking simplicity or correctness finding remains. Report cause, fix, evidence, residual risk, and requested delivery status.
