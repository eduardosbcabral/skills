#!/usr/bin/env python3
"""Persistent loop state and stall detection for AI engineering loops."""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path


DEFAULT_STATE_DIR = ".agent-loop"
DEFAULT_THRESHOLD = 3

SIGNAL_RE = re.compile(
    r"(error|fail|failed|assert|assertion|exception|traceback|panic|fatal|"
    r"undefined|not found|cannot|unexpected|timeout|refused|denied)",
    re.I,
)

NORMALIZERS = [
    (re.compile(r"0x[0-9a-fA-F]+"), "0xADDR"),
    (re.compile(r"\b[0-9a-f]{7,40}\b"), "HEX"),
    (re.compile(r"\d{4}-\d{2}-\d{2}[t ]\d{2}:\d{2}:\d{2}\S*", re.I), "TS"),
    (re.compile(r"(:|line )\s*\d+(:\d+)?"), r"\1N"),
    (re.compile(r"[/\\][\w./\\-]+/([\w.-]+)"), r"PATH/\1"),
    (re.compile(r"\b\d+(\.\d+)?\s*(ms|s|sec|seconds)\b", re.I), "DUR"),
    (re.compile(r"\b\d+\b"), "N"),
    (re.compile(r"\s+"), " "),
]


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def git_head():
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return result.stdout.strip() if result.returncode == 0 else ""
    except FileNotFoundError:
        return ""


def read_text(value, file_path):
    if file_path:
        try:
            return Path(file_path).read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""
    return value or ""


def fingerprint(text):
    if not text or not text.strip():
        return ""
    lines = [line.strip() for line in text.splitlines() if SIGNAL_RE.search(line)]
    if not lines:
        lines = [line.strip() for line in text.splitlines() if line.strip()][-8:]
    blob = "\n".join(lines[:30]).lower()
    for rx, repl in NORMALIZERS:
        blob = rx.sub(repl, blob)
    blob = blob.strip()
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12] if blob else ""


def paths(args):
    root = Path(args.state_dir)
    return root, root / "state.md", root / "journal.jsonl"


def load_journal(path):
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except ValueError:
            continue
    return rows


def analyze(rows, threshold):
    if not rows:
        return {
            "verdict": "progress",
            "streak": 0,
            "fingerprint": "",
            "recommendation": "continue",
            "reason": "no attempts recorded",
            "dead_end_actions": [],
        }

    last = rows[-1]
    fp = last.get("fingerprint", "")
    if last.get("gate") == "pass" or not fp:
        return {
            "verdict": "progress",
            "streak": 0,
            "fingerprint": fp,
            "recommendation": "continue",
            "reason": "last attempt passed or had no stable failure fingerprint",
            "dead_end_actions": [],
        }

    streak = 0
    for row in reversed(rows):
        if row.get("gate") != "pass" and row.get("fingerprint") == fp:
            streak += 1
        else:
            break

    counts = {}
    for row in rows:
        action = (row.get("action") or "").strip()
        if action and row.get("fingerprint") == fp and row.get("gate") != "pass":
            counts[action] = counts.get(action, 0) + 1
    dead_ends = sorted(action for action, count in counts.items() if count > 1)

    if streak >= threshold:
        return {
            "verdict": "stalled",
            "streak": streak,
            "fingerprint": fp,
            "recommendation": "switch-strategy" if streak == threshold else "escalate",
            "reason": f"{streak} consecutive failed attempts share fingerprint {fp}",
            "dead_end_actions": dead_ends,
        }

    return {
        "verdict": "progress",
        "streak": streak,
        "fingerprint": fp,
        "recommendation": "continue",
        "reason": f"failing but under threshold ({streak}/{threshold})",
        "dead_end_actions": dead_ends,
    }


def cmd_init(args):
    root, state_file, journal_file = paths(args)
    root.mkdir(parents=True, exist_ok=True)
    if not journal_file.exists():
        journal_file.write_text("", encoding="utf-8")
    if not state_file.exists() or args.force:
        state_file.write_text(
            "\n".join(
                [
                    "# Loop State",
                    "",
                    f"- Objective: {args.objective}",
                    f"- Mode: {args.mode}",
                    f"- Phase: {args.phase}",
                    f"- Verifier: {args.verifier}",
                    f"- Hard stop: {args.hard_stop}",
                    f"- State created: {now()}",
                    "- Last result: not started",
                    "- Resume point: start",
                    "- Blockers: none",
                    "",
                ]
            ),
            encoding="utf-8",
        )
    print(f"state: {state_file}")
    print(f"journal: {journal_file}")


def cmd_record(args):
    root, state_file, journal_file = paths(args)
    root.mkdir(parents=True, exist_ok=True)
    evidence = read_text(args.evidence, args.evidence_file)
    gate = args.gate
    fp = "" if gate == "pass" else fingerprint(evidence)
    row = {
        "ts": now(),
        "phase": args.phase,
        "action": args.action,
        "hypothesis": args.hypothesis,
        "gate": gate,
        "fingerprint": fp,
        "evidence": args.evidence_summary or first_signal(evidence),
        "next": args.next,
        "commit": git_head(),
    }
    with journal_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    update_state(state_file, row)
    print(f"recorded: gate={gate} fp={fp or '-'}")


def first_signal(text):
    for line in (text or "").splitlines():
        if SIGNAL_RE.search(line):
            return line.strip()[:240]
    for line in (text or "").splitlines():
        if line.strip():
            return line.strip()[:240]
    return ""


def update_state(state_file, row):
    if state_file.exists():
        base = state_file.read_text(encoding="utf-8", errors="replace").rstrip()
    else:
        base = "# Loop State"
    summary = [
        "",
        "## Last Attempt",
        "",
        f"- Time: {row['ts']}",
        f"- Phase: {row['phase']}",
        f"- Action: {row['action']}",
        f"- Gate: {row['gate']}",
        f"- Fingerprint: {row['fingerprint'] or '-'}",
        f"- Evidence: {row['evidence'] or '-'}",
        f"- Resume point: {row['next'] or '-'}",
        "",
    ]
    marker = "\n## Last Attempt\n"
    if marker in base:
        base = base.split(marker, 1)[0].rstrip()
    state_file.write_text(base + "\n" + "\n".join(summary), encoding="utf-8")


def cmd_resume(args):
    _root, state_file, journal_file = paths(args)
    if state_file.exists():
        print(state_file.read_text(encoding="utf-8", errors="replace").rstrip())
    else:
        print("state: none")
    rows = load_journal(journal_file)
    result = analyze(rows, args.threshold)
    print("")
    print(
        f"journal: {len(rows)} attempts; stall={result['verdict']} "
        f"streak={result['streak']} fp={result['fingerprint'] or '-'}"
    )
    for row in rows[-8:]:
        action = (row.get("action") or "")[:100]
        print(f"- {row.get('gate')} {row.get('phase')}: {action}")
    if result["dead_end_actions"]:
        print("avoid:")
        for action in result["dead_end_actions"]:
            print(f"- {action}")


def cmd_stall(args):
    _root, _state_file, journal_file = paths(args)
    result = analyze(load_journal(journal_file), args.threshold)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(result["verdict"])
        print(result["reason"])
        print(f"recommendation: {result['recommendation']}")
        if result["dead_end_actions"]:
            print("dead-end actions:")
            for action in result["dead_end_actions"]:
                print(f"- {action}")
    if args.exit_code and result["verdict"] == "stalled":
        sys.exit(10)


def cmd_fingerprint(args):
    print(fingerprint(read_text(args.evidence, args.evidence_file)) or "(no-failure)")


def build_parser():
    parser = argparse.ArgumentParser(description="Persist loop state and detect repeated stalls.")
    parser.add_argument("--state-dir", default=DEFAULT_STATE_DIR)
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--objective", required=True)
    init.add_argument("--mode", default="controlled")
    init.add_argument("--phase", default="intake")
    init.add_argument("--verifier", default="not set")
    init.add_argument("--hard-stop", default="not set")
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=cmd_init)

    record = sub.add_parser("record")
    record.add_argument("--phase", required=True)
    record.add_argument("--action", required=True)
    record.add_argument("--hypothesis", default="")
    record.add_argument("--gate", choices=["pass", "fail", "blocked"], required=True)
    record.add_argument("--evidence", default="")
    record.add_argument("--evidence-file")
    record.add_argument("--evidence-summary", default="")
    record.add_argument("--next", default="")
    record.set_defaults(func=cmd_record)

    resume = sub.add_parser("resume")
    resume.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    resume.set_defaults(func=cmd_resume)

    stall = sub.add_parser("stall")
    stall.add_argument("--threshold", type=int, default=DEFAULT_THRESHOLD)
    stall.add_argument("--exit-code", action="store_true")
    stall.add_argument("--json", action="store_true")
    stall.set_defaults(func=cmd_stall)

    fp = sub.add_parser("fingerprint")
    fp.add_argument("--evidence", default="")
    fp.add_argument("--evidence-file")
    fp.set_defaults(func=cmd_fingerprint)

    return parser


def main():
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
