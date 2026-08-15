---
name: rtk-token-saver
description: "Use when a development task or loop will run noisy shell commands, tests, builds, linters, git diffs, CI checks, logs, or container/cloud commands and should reduce token usage by using RTK when installed. Treat RTK as optional; fall back to normal commands when unavailable or when exact raw output is required."
---

# RTK Token Saver

Use RTK as an optional command-output compressor. It should never change the task goal, verification standard, or safety gate.

## Activate

1. Before a likely noisy shell phase, run `rtk --version` once.
2. If it succeeds, use RTK. If it is unavailable or fails, use raw commands and continue without searching alternate paths, installing, updating, initializing, repairing, or retrying RTK.
3. Run `rtk gain` only when the user asks for savings analytics; it is not an availability check.

## Use RTK For

Prefer explicit RTK commands when the output is large and a compact failure-oriented summary is enough:

- Repo inspection: `rtk git status`, `rtk git diff`, `rtk git log`.
- Search/listing summaries: `rtk ls`, `rtk find`, `rtk grep`.
- Verification summaries: `rtk test <command>` or a supported specialized test, build, lint, or typecheck command.
- CI/log sensors: `rtk gh run list`, `rtk gh pr view`, `rtk docker logs`, `rtk kubectl logs`, `rtk log <file>`.

## Use Raw Commands For

Use raw commands, or `rtk proxy <command>` when an active hook would rewrite them, when full fidelity matters:

- Exact stack traces, compiler diagnostics, snapshots, traces, or generated artifacts.
- Small outputs where compression adds no value.
- Suspected RTK parser/filter issue.
- Mutating operations and final delivery confirmation.
- Security, secrets, compliance, or audit work where hidden detail could be harmful.

## Loop Rules

- Start raw enough to understand context; use RTK for repetitive noisy checks.
- If an RTK wrapper itself fails, run the underlying narrow command raw and keep RTK disabled for the rest of that phase.
- If an RTK summary shows failure, read the full-output path it reports when available. Otherwise rerun only the narrow failing command raw; do not rerun a broad expensive gate merely for verbosity.
- Record verification based on the underlying command, not on RTK itself.
- Never treat token savings as a reason to skip build, lint, tests, CI, logs, or human approval gates.
