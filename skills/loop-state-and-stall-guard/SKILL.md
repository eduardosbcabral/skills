---
name: loop-state-and-stall-guard
description: "Use only as an optional companion to an active software-development loop when code, test, build, CI, deployment, runtime, or software-infrastructure work is long, resumable, automated, repeated, or failure-prone and needs durable state or stall detection. Do not use for notes or vault work, documentation-only tasks, research, personal organization, general monitoring, or tiny one-shot development tasks."
metadata:
  short-description: Persist software loop state and detect stalls
---

# Loop State And Stall Guard

Keep long software-development loops from forgetting, restarting, or repeating the same failed approach. It is not a standalone workflow. For non-programming work or tiny one-shot development work, do nothing.

## When To Use

Use this only when a software-development loop is already active and one applies:

- The software task is automated, scheduled, multi-thread, or explicitly resumable.
- The software task spans multiple implementation iterations, PR or CI waits, or external technical sensors.
- A verifier fails repeatedly and the next attempt risks repeating the same approach.
- The user asks to continue the software task later or preserve its loop state.

Do not create `.agent-loop/` for vault organization, note capture, documentation-only edits, research, personal workflows, or general task tracking.

## State Location

Prefer an existing project state location if present. Otherwise use `.agent-loop/` at the repo root.

Files:

- `.agent-loop/state.md`: human-readable current objective, phase, verifier, gates, blockers, and resume point.
- `.agent-loop/journal.jsonl`: append-only attempt records.

Do not create state files for small one-pass work.

## Script

Use the bundled `scripts/loop_state.py` when available. If the script path is unavailable in the runtime, do the same steps inline with markdown state and an append-only JSONL journal.

Common commands:

```bash
python3 scripts/loop_state.py init --objective "..." --mode controlled --verifier "..."
python3 scripts/loop_state.py record --phase implement --action "..." --hypothesis "..." --gate fail --evidence-file /tmp/gate.log
python3 scripts/loop_state.py resume
python3 scripts/loop_state.py stall --threshold 3 --exit-code
```

When the script lives inside a global skill folder, call it by its installed path. Keep state paths relative to the target repo.

## Loop Contract

1. Initialize state before a resumable or automated loop starts.
2. At the start of each resumed turn, read `resume` output before choosing the next action.
3. After every meaningful attempt, record action, hypothesis, gate result, evidence, and next step.
4. Before retrying after a failed gate, run the stall check.
5. If the same failure fingerprint repeats at the threshold, do not retry the same approach. Switch strategy, reduce scope, ask for user input, or escalate.
6. Mark done only with concrete verifier evidence in the same turn.

## Done Evidence

Final output should mention the state location when this skill was used, plus:

- last verifier result;
- whether stall check was clear or triggered;
- resume point if not done;
- open blockers or human gates.
