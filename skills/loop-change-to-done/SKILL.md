---
name: loop-change-to-done
description: "Use when the user gives an already-scoped change, business rule, validation, permission, UI behavior, or implementation request and wants the smallest correct implementation with focused verification. Do not use for vague discovery or a task centered on a concrete failure symptom."
---

# Change To Done Loop

Move from a specified change to a verified result.

## State Contract

- **Input:** a scoped request or an Idea To Build transition contract.
- **Output:** the smallest correct implementation plus focused evidence.
- **Transition:** unclear product semantics go to `Idea To Build`; a failing verifier with an unknown cause goes to `Broken To Fixed`.
- **Not done:** code exists but acceptance behavior or verification is unclear.

Conversation and analysis do not authorize edits. Implementation, commit, push, PR, deploy, destructive operations, credentials, and external writes require the user's request or approval appropriate to that action.

## Optional Dependency

Before shell-heavy work, load and follow `$rtk-token-saver` when the skill and its external RTK CLI are available. It is an optional operational dependency, not a companion or embedded behavior. Use its current availability, fallback, fidelity, safety, and verification rules as the source of truth. If unavailable, continue with normal commands; do not install or configure RTK without explicit approval.

## Start

1. Restate the change as actor, trigger, expected behavior, rejected behavior, edge cases, and verifier. Skip fields that genuinely do not apply to a tiny mechanical edit.
2. Read repository guidance and inspect the current behavior, nearest implementation, tests, and conventions before editing.
3. Classify the change:
   - **tiny:** mechanical, local, and unambiguous;
   - **normal:** behavior changes but the rule is settled;
   - **risky:** auth, money, data, concurrency, migrations, destructive behavior, security, public contracts, or broad UX is involved.
4. If product semantics are not settled, transition to Idea To Build. If only a few independent decisions block the change, use `references/batch-grill-me.md`.
5. For normal/risky changes, keep the compact record in `references/change-ledger.md`.

## Built-in Operating Rules

### Ponytail

Understand the real flow, then choose the first option that works: delete the need, reuse existing code, use the standard library, use the native platform, use an installed dependency, solve it in one line, or write the minimum new code. Apply the change at the narrowest correct shared point. Do not cut explicit rules, trust-boundary validation, security, accessibility, data-loss handling, or required evidence.

### Ponytail Review

Use after implementation when the diff adds abstraction, spans several files, or feels larger than the behavior. Tag only removable complexity: `delete`, `stdlib`, `native`, `yagni`, or `shrink`. If none applies, record `Lean already. Ship.`

### Caveman

Keep progress and final prose terse: remove filler, hedging, pleasantries, repeated summaries, tool narration, decorative tables, emoji, and long raw logs. Fragments are fine. Preserve the user's language and preserve code, commands, API names, identifiers, and exact errors. Do not invent abbreviations or sacrifice clarity for security warnings, irreversible confirmations, ambiguity, or multi-step instructions.

## Loop

1. Convert the request into concrete positive, negative, and boundary acceptance examples where useful.
2. Choose the smallest viable implementation point with Ponytail. Avoid speculative refactors and future-proofing.
3. Implement only the scoped behavior, following nearby project patterns.
4. Self-review the diff for requested behavior, rejected behavior, edge cases, security boundaries, accidental scope, and project conventions.
5. Run the tightest verifier first. Then run relevant test, typecheck, lint, build, CLI, API, or browser evidence in proportion to risk.
6. If a verifier fails for an unknown reason, transition to Broken To Fixed. If the implementation was wrong, correct it here and rerun only affected evidence.
7. Run Ponytail Review when complexity warrants it and correctness review for normal/risky behavior. Fix blocking findings, then rerun affected verification.
8. Capture durable rule documentation only when the behavior is business-significant and the repository has a clear home for it.
9. Commit, push, open a PR, monitor CI, or deploy only when requested. A PR is an optional delivery action, not part of the definition of done.

## Conditional Mode

Use `references/loop-state-and-stall-guard.md` only for resumable, automated, multi-session, external-wait, or repeated-failure work. It is an internal mode, not an installed-skill dependency.

## Done

Done means acceptance behavior is satisfied, relevant verification passed or honest gaps are named, the diff stayed scoped, and no blocking simplicity or correctness finding remains. Report outcome, evidence, files or behavior changed, residual risk, and any requested delivery status.
