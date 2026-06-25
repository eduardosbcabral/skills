---
name: codex-report-usage
description: Use when the user asks for Codex usage, token, cost, daily, monthly, session, or historical reports from local Codex JSONL data using the @ccusage/codex CLI.
---
# codex-report-usage

Use the npm library `ccusage-codex` CLI to analyze local Codex usage from JSONL files.

Choose the timezone from the user's request or local environment. If it is unclear, use `<timezone>` as a placeholder and ask only when the exact calendar boundary matters.

## Commands

```bash
npx ccusage-codex daily --timezone <timezone>
npx ccusage-codex monthly --timezone <timezone>
npx ccusage-codex session --timezone <timezone>
```

Use JSON output for summaries or vault reports:

```bash
npx ccusage-codex daily --json --timezone <timezone>
npx ccusage-codex monthly --json --timezone <timezone>
npx ccusage-codex session --json --timezone <timezone>
```

Useful filters:

```bash
npx ccusage-codex daily --since YYYY-MM-DD --until YYYY-MM-DD --timezone <timezone>
npx ccusage-codex monthly --since YYYY-MM-DD --timezone <timezone>
```

## Reporting Rules

- Prefer the user's local timezone unless they ask for another reporting boundary.
- For all-time reports, run daily/monthly/session without date filters and summarize totals, first/last usage dates, and highest-usage days or sessions.
- State clearly that totals depend on the local Codex JSONL files available on this machine.
- Do not mutate Codex logs or archived sessions while reporting usage.
