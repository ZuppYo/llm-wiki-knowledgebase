#!/usr/bin/env python3
"""Fail on obvious secrets and machine-local paths in tracked content."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {
    ".git",
    ".obsidian",
    "Drafts",
    "__pycache__",
}

PATTERNS = [
    (re.compile(r"-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----"), "private key block"),
    (re.compile(r"\bsk-[a-zA-Z0-9]{20,}\b"), "OpenAI-style API key"),
    (re.compile(r"\bghp_[a-zA-Z0-9]{20,}\b"), "GitHub token"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access key id"),
    (re.compile(r"\.obsidian/plugins/"), "obsidian plugins path"),
    (re.compile(r"\.obsidian/cache/"), "obsidian cache path"),
    (re.compile(r"[A-Za-z]:\\Users\\[^\\]+\\"), "Windows user path"),
    (re.compile(r"/home/[^/\s]+/"), "Linux home path"),
]

TEXT_EXTENSIONS = {
    ".md", ".py", ".sh", ".json", ".jsonl", ".yaml", ".yml", ".txt", ".gitignore",
}

# Docs that mention .obsidian ignore rules (not committed plugin state)
SKIP_OBSIDIAN_PATTERN_IN = {".gitignore", "requirement.md", "Schema/command-reference.md"}


def tracked_files() -> list[Path]:
    try:
        out = subprocess.check_output(
            ["git", "ls-files"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        )
        return [ROOT / line.strip() for line in out.splitlines() if line.strip()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in ROOT.rglob("*") if p.is_file() and not _in_skip(p)]


def _in_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def main() -> int:
    errors: list[str] = []
    obsidian_path_patterns = {PATTERNS[4][0], PATTERNS[5][0]}
    for path in tracked_files():
        if path.name == "audit_public.py":
            continue
        if path.suffix.lower() not in TEXT_EXTENSIONS and path.name != ".gitignore":
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        rel = path.relative_to(ROOT)
        for rx, label in PATTERNS:
            if path.name in SKIP_OBSIDIAN_PATTERN_IN and rx in obsidian_path_patterns:
                continue
            if rx.search(text):
                errors.append(f"{rel}: matched {label}")
    if errors:
        for e in errors:
            print(f"audit_public: {e}", file=sys.stderr)
        return 1
    print("audit_public: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
