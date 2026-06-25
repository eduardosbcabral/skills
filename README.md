# AI Agent Skills

Reusable Codex skills and custom agents for development workflows.

## Layout

- `skills/`: installable skill folders. Copy the folders you want into `~/.codex/skills/` or another Codex skill root.
- `.codex/agents/`: optional custom Codex agent definitions. Copy the TOML files you want into `~/.codex/agents/`.

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
