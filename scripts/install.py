#!/usr/bin/env python3
"""Install repository skills together with their Codex custom agents."""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SKILLS = ROOT / "skills"
SOURCE_AGENTS = ROOT / ".codex" / "agents"
NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")

LOOP_AGENTS = {
    "loop-idea-to-build": (
        "loop-domain-extractor",
        "loop-harness-sensor",
        "loop-slice-planner",
        "loop-rule-reviewer",
    ),
    "loop-change-to-done": (
        "loop-harness-sensor",
        "loop-rule-reviewer",
    ),
    "loop-broken-to-fixed": (
        "loop-bug-diagnoser",
        "loop-harness-sensor",
        "loop-rule-reviewer",
    ),
}


def replace_tree(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.is_symlink() or target.is_file():
        target.unlink()
    elif target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)


def available_skills() -> list[str]:
    return sorted(
        path.name
        for path in SOURCE_SKILLS.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def destinations(args: argparse.Namespace) -> tuple[Path, Path]:
    if args.project:
        project = args.project.expanduser().resolve()
        return project / ".agents" / "skills", project / ".codex" / "agents"

    codex_home = args.codex_home or Path(
        os.environ.get("CODEX_HOME", Path.home() / ".codex")
    )
    codex_home = codex_home.expanduser().resolve()
    return codex_home / "skills", codex_home / "agents"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install skills and mapped Codex custom agents from this checkout."
    )
    parser.add_argument("skills", nargs="*", help="Skill folder names to install")
    parser.add_argument("--all", action="store_true", help="Install every repository skill")
    scope = parser.add_mutually_exclusive_group()
    scope.add_argument("--project", type=Path, help="Install into a project workspace")
    scope.add_argument("--codex-home", type=Path, help="Override the user Codex home")
    args = parser.parse_args()
    if args.all and args.skills:
        parser.error("use --all or explicit skill names, not both")
    if not args.all and not args.skills:
        parser.error("provide at least one skill name or --all")
    return args


def main() -> None:
    args = parse_args()
    requested = available_skills() if args.all else args.skills
    invalid = [name for name in requested if not NAME_PATTERN.fullmatch(name)]
    if invalid:
        raise SystemExit(f"invalid skill name: {invalid[0]}")

    missing = [
        name for name in requested if not (SOURCE_SKILLS / name / "SKILL.md").is_file()
    ]
    if missing:
        raise SystemExit(f"unknown skill: {missing[0]}")

    install_names = list(dict.fromkeys(requested))
    if any(name in LOOP_AGENTS for name in requested) and "rtk-token-saver" not in install_names:
        install_names.append("rtk-token-saver")

    agent_names = sorted(
        {agent for name in requested for agent in LOOP_AGENTS.get(name, ())}
    )
    missing_dependencies = [
        name for name in install_names if not (SOURCE_SKILLS / name / "SKILL.md").is_file()
    ]
    if missing_dependencies:
        raise SystemExit(f"missing skill dependency: {missing_dependencies[0]}")
    missing_agents = [
        name for name in agent_names if not (SOURCE_AGENTS / f"{name}.toml").is_file()
    ]
    if missing_agents:
        raise SystemExit(f"missing agent definition: {missing_agents[0]}")

    skill_root, agent_root = destinations(args)
    for name in install_names:
        replace_tree(SOURCE_SKILLS / name, skill_root / name)
        print(f"installed skill: {name}")

    agent_root.mkdir(parents=True, exist_ok=True)
    for name in agent_names:
        source = SOURCE_AGENTS / f"{name}.toml"
        shutil.copy2(source, agent_root / source.name)
        print(f"installed agent: {name}")


if __name__ == "__main__":
    main()
