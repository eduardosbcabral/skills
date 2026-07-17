---
name: my-skills
description: "Use when Eduardo asks about my skills, my skills repository, the canonical source of a personal skill, or wants to find, inspect, create, update, install, synchronize, commit, or publish skills from his own repository. Provides the canonical remote, checkout conventions, source/install boundaries, and safe sync workflow."
---

# My Skills

Use this repository as the canonical source for Eduardo's personal skills.

## Repository

- Remote: `https://github.com/eduardosbcabral/skills.git`
- Expected local checkout: `~/dev/github/skills`
- Skill sources: `~/dev/github/skills/skills/<skill-name>/`
- Codex installation: `~/.codex/skills/<skill-name>/` or another discovered active skill root.

Verify the checkout with `git -C ~/dev/github/skills remote get-url origin`. If it is missing or points elsewhere, search for a matching checkout before cloning. Clone only when the requested task requires a local checkout.

## Source And Installation

Treat the repository copy as source and the installed copy as runtime by default.

- For normal authoring: edit `skills/<skill-name>/`, validate it, then install the validated folder.
- When the user explicitly says the installed version is authoritative: compare it with the repository, copy only the requested skill, then validate again.
- Never bulk-copy every installed skill into the repository.
- Preserve unrelated work in both locations.

## Workflow

1. Inspect repository guidance, branch, remote, and working-tree status.
2. Locate the requested skill in the repository and active installation roots.
3. Compare before writing; state which copy is authoritative for this task.
4. Make the smallest scoped change.
5. Validate each changed skill with the available `skill-creator` validator.
6. Run `git diff --check` and inspect the final repository diff.
7. Install or synchronize only when requested or clearly part of the user's requested workflow.
8. Commit, push, open a PR, or publish only when explicitly requested.

Do not discard unrelated dirty-worktree changes. Do not expose secrets or add private customer/project data to this public repository.
