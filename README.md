# AI Agent Skills

Public, reusable skills and custom agents for software-development workflows.

## Layout

- `skills/`: Codex and cross-tool Agent Skills.
- `.codex/agents/`: Codex custom-agent profiles.
- `.claude/skills/`: Claude Code-specific skills.
- `.claude/agents/`: Claude Code custom subagents.
- `scripts/install.py`: installs Codex skills with mapped custom agents.

## Codex

Install all Codex skills:

```bash
python3 scripts/install.py --all
```

Install the orchestration loop, its agents, and the optional RTK guidance:

```bash
python3 scripts/install.py loop-orchestration
```

Install into one project instead of the user runtime:

```bash
python3 scripts/install.py --project /path/to/workspace loop-orchestration
```

Invoke it explicitly with `$loop-orchestration`, or let Codex load it when the request matches its description. Restart Codex after adding a new top-level skill or custom-agent file.

## Claude Code

Install the Claude-specific loop and its two subagents:

```bash
mkdir -p ~/.claude/skills ~/.claude/agents
cp -R .claude/skills/claude-loop-orchestration ~/.claude/skills/
cp -R skills/rtk-token-saver ~/.claude/skills/
cp .claude/agents/claude-loop-*.md ~/.claude/agents/
```

PowerShell:

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.claude\skills", "$HOME\.claude\agents"
Copy-Item -Recurse -Path ".claude\skills\claude-loop-orchestration", "skills\rtk-token-saver" -Destination "$HOME\.claude\skills\"
Copy-Item -Path ".claude\agents\claude-loop-*.md" -Destination "$HOME\.claude\agents\"
```

Invoke it with `/claude-loop-orchestration`, or let Claude load it from its description. Restart the Claude Code session after adding or editing subagent files.

## Ponytail

Install Ponytail from its official repository as a native plugin instead of copying its skills into this repository.

Codex:

```bash
codex plugin marketplace add DietrichGebert/ponytail
codex plugin add ponytail@ponytail
```

Start a new Codex session, open `/hooks`, and review and trust the Ponytail lifecycle hooks.

Claude Code:

```bash
claude plugin marketplace add DietrichGebert/ponytail
claude plugin install ponytail@ponytail
```

Start a new Claude Code session after installation. Once enabled, Ponytail uses its default `full` mode throughout code-changing work. The loops fold `ponytail-review` into their existing final review only when the change introduces complexity signals; audit, debt, gain, and help stay explicit-only.

## Orchestration

Both variants detect whether work starts as an idea, scoped change, or failure. The primary session remains the parent, substantial bounded work goes to a worker, analytical decisions go to an advisor, verification is proportional, and normal or risky change sets receive a fresh final review.

The Codex profiles pin their native models in `.codex/agents/`. The Claude profiles use Opus for read-only analysis and review, and Sonnet for bounded implementation. Model details stay out of the skills themselves.

`rtk-token-saver` is the loop's only bundled skill dependency. It detects the optional RTK CLI by capability and falls back to raw commands immediately. Installing the skill never installs or configures the CLI. Ponytail remains an external native plugin and follows its official upstream releases.

## Privacy

Keep this repository generic and public. Do not add personal paths, private hostnames, IP addresses, tokens, customer names, repository names, or environment-specific credentials. Use placeholders for examples. Private workflows belong in a private source.

## Included Skills

- `azure-cli`
- `azure-devops`
- `claude-loop-orchestration` (Claude Code)
- `codex-remove-ui-noise`
- `codex-report-usage`
- `coolify-cli`
- `loop-orchestration`
- `rtk-token-saver`
- `saas-backend-patterns`
- `saas-frontend-patterns`
- `saas-project-bootstrap`
