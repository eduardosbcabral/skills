---
name: create-wiki-notes
description: Use when creating a new note, page, project map, operational note, inbox capture, or lightweight documentation entry in Eduardo Wiki.
---

# Create Wiki Notes

## Principle

Create the smallest useful wiki note, place it in the right folder, and sync it.

## Required Sub-Skill

Use `my-wiki` for repository location, naming policy, language policy, and git sync rules.

## Workflow

1. Search first. If an existing note matches, append or update it instead of creating a duplicate.
2. Choose the destination:
   - `inbox/` for quick captures, mobile notes, unclear ideas, or raw input.
   - `wiki/agent-memory/` for reusable agent memory and operating procedures.
   - `wiki/projects/` for agent-facing project maps.
   - `wiki/skills/` for archived or reusable skill notes.
   - `projects/`, `areas/`, or `resources/` for human-facing PARA notes.
3. Use lowercase kebab-case filenames with no accents.
4. Add minimal frontmatter:

```yaml
---
title: Human Readable Title
type: note
status: active
updated: YYYY-MM-DD
tags:
  - wiki
---
```

5. Write concise content. Prefer bullets and commands over long explanation.
6. Update a nearby `index.md` only when the new note is meant to be discoverable later.
7. Run the wiki git sync from `my-wiki`: pull before editing, then status, add only intended files, commit, and push.

## Defaults

- Use English for agent-facing pages under `wiki/`.
- Use the user's natural language for personal or human-facing notes.
- Do not reference local machine paths in wiki content. Use the GitHub repository identity when a portable reference is needed: `git@github.com:eduardosbcabral/notes.git`.
- Keep OpenClaw, Coolify, Telegram, GitHub, and automation procedures in `wiki/agent-memory/` unless the user asks for a project-specific map.

## Common Note Types

| User asks for | Default destination | Type |
| --- | --- | --- |
| "anota isso" | `inbox/` | `capture` |
| "coloca na wiki como fazer X" | `wiki/agent-memory/` | `procedure` |
| "cria mapa desse projeto" | `wiki/projects/` | `project-map` |
| "salva esse artigo" | `resources/articles/` | `source` |
| "documenta essa skill" | `wiki/skills/` | `skill` |
