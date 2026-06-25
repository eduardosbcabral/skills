# AI Agent Skills

Reusable Codex skills and custom agents for development workflows.

## Layout

- `skills/`: installable skill folders. Copy the folders you want into `~/.agents/skills/` for Codex or `~/.claude/skills/` for Claude Code.
- `.codex/agents/`: optional custom Codex agent definitions. Copy the TOML files you want into `~/.codex/agents/`.

## Install in Codex

Codex discovers skills from local skill folders. For a personal install available across your projects, copy skill folders into `~/.agents/skills/`. Codex also supports repo-scoped skills at `.agents/skills/` inside a project.

Install all skills from this repository for your user:

```bash
git clone https://github.com/eduardosbcabral/skills.git /tmp/eduardo-skills
mkdir -p ~/.agents/skills
cp -R /tmp/eduardo-skills/skills/* ~/.agents/skills/
```

Install only one skill:

```bash
mkdir -p ~/.agents/skills
cp -R skills/loop-change-to-done ~/.agents/skills/
```

Install repo-scoped skills instead of user-global skills:

```bash
mkdir -p .agents/skills
cp -R skills/loop-change-to-done .agents/skills/
```

Use a skill explicitly by mentioning it in the prompt, for example `$loop-change-to-done`. Codex may also invoke a skill automatically when the task matches the `description` in `SKILL.md`. If a newly copied skill does not appear, restart Codex.

Custom agents are separate from skills. To install the bundled Codex agents globally:

```bash
mkdir -p ~/.codex/agents
cp .codex/agents/*.toml ~/.codex/agents/
```

## Install in Claude Code

Claude Code discovers skills from `~/.claude/skills/<skill-name>/SKILL.md` for personal skills and `.claude/skills/<skill-name>/SKILL.md` for project-scoped skills. The command name comes from the skill folder name, so `~/.claude/skills/loop-change-to-done/SKILL.md` is invoked as `/loop-change-to-done`.

Install all skills for your user:

```bash
git clone https://github.com/eduardosbcabral/skills.git /tmp/eduardo-skills
mkdir -p ~/.claude/skills
cp -R /tmp/eduardo-skills/skills/* ~/.claude/skills/
```

Install only one skill:

```bash
mkdir -p ~/.claude/skills
cp -R skills/loop-change-to-done ~/.claude/skills/
```

Install repo-scoped skills instead of user-global skills:

```bash
mkdir -p .claude/skills
cp -R skills/loop-change-to-done .claude/skills/
```

Invoke a Claude Code skill directly with `/skill-name`, for example `/loop-change-to-done`. Claude Code can also load skills automatically from their description. Claude Code detects edits under existing watched skill directories, but restart Claude Code if you create a new top-level skills directory and the skill does not appear.

## Privacy

This repository is intended to stay public. Keep personal paths, private hostnames, IP addresses, tokens, customer names, repository names, and environment-specific credentials out of these files. Use placeholders such as `<vault-name>`, `<project>`, `<host-alias>`, and `<timezone>` instead.

## Included Skills

- `azure-cli`
- `azure-devops`
- `loop-broken-to-fixed`
- `codex-report-usage`
- `coolify-cli`
- `loop-idea-to-build`
- `my-vault`
- `loop-change-to-done`
- `saas-backend-patterns`
- `saas-frontend-patterns`
- `saas-project-bootstrap`

## External Companion Skills

Some loop skills can use optional companion skills when they are installed locally. These are referenced by name but are not bundled here.

- `$grill-with-docs`: external third-party companion for grilling unclear requirements and capturing glossary/ADR decisions.
