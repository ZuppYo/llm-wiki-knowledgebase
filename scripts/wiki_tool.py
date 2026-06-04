#!/usr/bin/env python3
"""Deterministic LLM Wiki maintenance tool (stdlib only)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW_SOURCES = ROOT / "Raw" / "Sources"
WIKI = ROOT / "Wiki"
CATALOG_PATH = WIKI / "catalog.jsonl"
MANIFEST_PATH = ROOT / "Schema" / "source-manifest.jsonl"
WIKI_LOG = WIKI / "log.md"

WIKI_SUBDIRS = ("Topics", "Concepts", "Entities", "Projects", "Logs")
ALLOWED_TAGS = frozenset({"topic", "concept", "entity", "project", "log"})
TAG_TO_FOLDER = {
    "topic": "Topics",
    "concept": "Concepts",
    "entity": "Entities",
    "project": "Projects",
    "log": "Logs",
}
SKIP_WIKI_NAMES = frozenset({"index.md", "catalog.jsonl", "log.md"})
REQUIRED_DIRS = [
    RAW_SOURCES,
    ROOT / "Raw" / "Files",
    *(WIKI / d for d in WIKI_SUBDIRS),
    ROOT / "Schema",
    ROOT / "_templates",
    ROOT / ".agents" / "skills",
    ROOT / "scripts",
]


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end].strip()
    body = text[end + 4 :].lstrip("\n")
    return _parse_yaml_block(block), body


def _parse_yaml_block(block: str) -> dict:
    data: dict = {}
    key: str | None = None
    list_key: str | None = None

    for line in block.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and list_key:
            item = stripped[2:].strip().strip("'\"")
            data.setdefault(list_key, []).append(item)
            continue
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        k = k.strip()
        v = v.strip()
        list_key = None
        key = k
        if v == "":
            data[k] = []
            list_key = k
        elif v in ("true", "True"):
            data[k] = True
        elif v in ("false", "False"):
            data[k] = False
        else:
            data[k] = v.strip("'\"")
    return data


def read_note(path: Path) -> tuple[dict, str]:
    return parse_frontmatter(path.read_text(encoding="utf-8"))


def norm_path(p: str) -> str:
    return p.replace("\\", "/")


WIKILINK_RE = re.compile(r"^\[\[([^\]|#^]+)(?:#[^\]]+)?(?:\|[^\]]+)?\]\]$")
BODY_WIKILINK_RE = re.compile(r"\[\[[^\]]+\]\]")


def _wikilink_target(ref: str) -> str | None:
    m = WIKILINK_RE.match(ref.strip())
    return m.group(1).strip() if m else None


def resolve_source_ref(ref: str) -> str | None:
    """Resolve Obsidian wikilink or vault path to Raw/Sources/*.md path."""
    ref = ref.strip().strip("'\"")
    if not ref:
        return None
    if norm_path(ref).startswith("Raw/Sources/"):
        path = ROOT / ref
        if path.is_file():
            return norm_path(str(path.relative_to(ROOT)))
        if not ref.endswith(".md"):
            with_md = ROOT / f"{ref}.md"
            if with_md.is_file():
                return norm_path(str(with_md.relative_to(ROOT)))
        return None
    target = _wikilink_target(ref) or ref
    if not RAW_SOURCES.is_dir():
        return None
    for path in RAW_SOURCES.glob("*.md"):
        meta, body = read_note(path)
        title = str(meta.get("Title") or title_from_note(path, meta, body))
        if path.stem == target or title == target:
            return norm_path(str(path.relative_to(ROOT)))
    return None


def sources_list(meta: dict) -> list[str]:
    """Source refs as written in frontmatter (wikilinks or paths)."""
    raw = meta.get("sources", [])
    if isinstance(raw, list):
        return [str(x).strip().strip("'\"") for x in raw]
    if isinstance(raw, str) and raw:
        return [raw.strip().strip("'\"")]
    return []


def sources_resolved(meta: dict) -> list[str]:
    """Vault paths under Raw/Sources/ for lint and coverage."""
    resolved: list[str] = []
    for ref in sources_list(meta):
        path = resolve_source_ref(ref)
        if path:
            resolved.append(path)
    return resolved


def wiki_note_paths() -> list[Path]:
    paths: list[Path] = []
    for sub in WIKI_SUBDIRS:
        folder = WIKI / sub
        if not folder.is_dir():
            continue
        for p in sorted(folder.glob("*.md")):
            if p.name == "index.md":
                continue
            paths.append(p)
    return paths


def tag_from_meta(meta: dict, path: Path) -> str | None:
    tags = meta.get("tags")
    if isinstance(tags, list):
        for t in tags:
            if t in ALLOWED_TAGS:
                return t
    elif isinstance(tags, str) and tags in ALLOWED_TAGS:
        return tags
    folder = path.parent.name
    for tag, name in TAG_TO_FOLDER.items():
        if name == folder:
            return tag
    return None


def title_from_note(path: Path, meta: dict, body: str) -> str:
    if meta.get("Title"):
        return str(meta["Title"])
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def topics_list(meta: dict) -> list[str]:
    raw = meta.get("topics", [])
    if isinstance(raw, list):
        return [str(x) for x in raw]
    return []


def cmd_doctor(_args: argparse.Namespace) -> int:
    errors: list[str] = []
    if sys.version_info < (3, 9):
        errors.append(f"Python 3.9+ required; got {sys.version}")
    for d in REQUIRED_DIRS:
        if not d.is_dir():
            errors.append(f"Missing directory: {d.relative_to(ROOT)}")
    if CATALOG_PATH.exists():
        try:
            _load_jsonl(CATALOG_PATH)
        except Exception as e:
            errors.append(f"Invalid catalog: {e}")
    if MANIFEST_PATH.exists():
        try:
            _load_jsonl(MANIFEST_PATH)
        except Exception as e:
            errors.append(f"Invalid manifest: {e}")
    wiki_n = len(wiki_note_paths())
    raw_n = len(list(RAW_SOURCES.glob("*.md"))) if RAW_SOURCES.is_dir() else 0
    print(f"Wiki compiled notes: {wiki_n}")
    print(f"Raw sources: {raw_n}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    print("doctor: OK")
    return 0


def cmd_build(_args: argparse.Namespace) -> int:
    records: list[dict] = []
    for path in wiki_note_paths():
        meta, body = read_note(path)
        tag = tag_from_meta(meta, path)
        if not tag:
            continue
        rel = norm_path(str(path.relative_to(ROOT)))
        sources = sources_resolved(meta)
        records.append(
            {
                "path": rel,
                "title": title_from_note(path, meta, body),
                "tag": tag,
                "topics": topics_list(meta),
                "sources": sources,
                "updated": str(meta.get("updated", meta.get("created", date.today().isoformat()))),
            }
        )
    records.sort(key=lambda r: r["path"])
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CATALOG_PATH.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    _write_wiki_index(records)
    for sub in WIKI_SUBDIRS:
        _write_folder_index(sub, records)
    print(f"build: wrote {len(records)} catalog entries")
    return 0


def _index_list_line(record: dict, index_parent: Path) -> str:
    """Markdown list item linking to a note relative to index_parent (clickable in Cursor/Obsidian)."""
    note = ROOT / norm_path(record["path"])
    rel = norm_path(str(note.relative_to(index_parent)))
    return f"- [{record['title']}]({rel})"


def _write_wiki_index(records: list[dict]) -> None:
    lines = ["# Wiki Index", "", f"Generated: {date.today().isoformat()}", ""]
    by_tag: dict[str, list[dict]] = {}
    for r in records:
        by_tag.setdefault(r["tag"], []).append(r)
    for tag in ("topic", "concept", "entity", "project", "log"):
        items = by_tag.get(tag, [])
        if not items:
            continue
        lines.append(f"## {tag.title()}s ({len(items)})")
        lines.append("")
        for r in items:
            lines.append(_index_list_line(r, WIKI))
        lines.append("")
    WIKI.mkdir(parents=True, exist_ok=True)
    (WIKI / "index.md").write_text("\n".join(lines), encoding="utf-8")


def _write_folder_index(sub: str, records: list[dict]) -> None:
    folder_tag = {v: k for k, v in TAG_TO_FOLDER.items()}[sub]
    items = [r for r in records if r["tag"] == folder_tag]
    folder = WIKI / sub
    lines = [f"# {sub} Index", "", f"Generated: {date.today().isoformat()}", ""]
    for r in items:
        lines.append(_index_list_line(r, folder))
    if not items:
        lines.append("_No notes yet._")
    path = WIKI / sub / "index.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def cmd_lint(_args: argparse.Namespace) -> int:
    errors: list[str] = []
    for path in wiki_note_paths():
        meta, body = read_note(path)
        rel = norm_path(str(path.relative_to(ROOT)))
        for wikilink in BODY_WIKILINK_RE.findall(body):
            errors.append(
                f"{rel}: body must use Markdown links, not wikilink {wikilink!r} "
                "(see .agents/skills/llm-wiki-LINKS.md)"
            )
        tag = tag_from_meta(meta, path)
        if tag not in ALLOWED_TAGS:
            errors.append(f"{rel}: missing or invalid tag in {ALLOWED_TAGS}")
            continue
        expected_folder = TAG_TO_FOLDER[tag]
        if path.parent.name != expected_folder:
            errors.append(f"{rel}: tag {tag} should be in Wiki/{expected_folder}/")
        refs = sources_list(meta)
        resolved = sources_resolved(meta)
        count = meta.get("source_count")
        try:
            count_int = int(count) if count is not None else -1
        except (TypeError, ValueError):
            count_int = -1
        if count_int != len(refs):
            errors.append(f"{rel}: source_count ({count}) != len(sources) ({len(refs)})")
        if len(resolved) != len(refs):
            for ref in refs:
                if not resolve_source_ref(ref):
                    errors.append(f"{rel}: source not found: {ref}")
        for src in resolved:
            if not norm_path(src).startswith("Raw/Sources/"):
                errors.append(f"{rel}: source must be under Raw/Sources/: {src}")
        for field in ("created", "updated"):
            if field not in meta:
                errors.append(f"{rel}: missing {field}")
    if errors:
        for e in errors:
            print(f"lint: {e}", file=sys.stderr)
        return 1
    print(f"lint: OK ({len(wiki_note_paths())} notes)")
    return 0


def raw_source_paths() -> list[Path]:
    if not RAW_SOURCES.is_dir():
        return []
    return sorted(RAW_SOURCES.glob("*.md"))


def cmd_source_scan(args: argparse.Namespace) -> int:
    sources = raw_source_paths()
    coverage = _wiki_coverage_map()
    rows: list[dict] = []
    today = date.today().isoformat()
    for path in sources:
        meta, body = read_note(path)
        rel = norm_path(str(path.relative_to(ROOT)))
        title = str(meta.get("Title") or title_from_note(path, meta, body))
        processed = meta.get("Processed") in (True, "true", "True")
        covered_by = sorted(coverage.get(rel, []))
        if covered_by and not processed:
            processed = True
        rows.append(
            {
                "path": rel,
                "title": title,
                "processed": processed,
                "covered_by": covered_by,
                "updated": str(meta.get("Created", today)),
            }
        )
        print(f"{rel}\tprocessed={processed}\tcovered={len(covered_by)}")
    if args.update:
        MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
        with MANIFEST_PATH.open("w", encoding="utf-8") as f:
            for row in rows:
                if args.accept_covered and not row["covered_by"] and not row["processed"]:
                    continue
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"source-scan: updated {MANIFEST_PATH}")
    return 0


def _wiki_coverage_map() -> dict[str, list[str]]:
    m: dict[str, list[str]] = {}
    for path in wiki_note_paths():
        meta, _ = read_note(path)
        rel_wiki = norm_path(str(path.relative_to(ROOT)))
        for src in sources_resolved(meta):
            m.setdefault(src, []).append(rel_wiki)
    return m


def cmd_source_lint(_args: argparse.Namespace) -> int:
    errors: list[str] = []
    coverage = _wiki_coverage_map()
    for path in raw_source_paths():
        meta, _ = read_note(path)
        rel = norm_path(str(path.relative_to(ROOT)))
        for field in ("Title", "Reference", "Created", "Processed", "tags"):
            if field not in meta:
                errors.append(f"{rel}: missing {field}")
        tags = meta.get("tags")
        tag_list = tags if isinstance(tags, list) else ([tags] if tags else [])
        if "source" not in tag_list:
            errors.append(f"{rel}: tags must include 'source'")
        processed = meta.get("Processed") in (True, "true", "True")
        if processed and not coverage.get(rel):
            errors.append(f"{rel}: Processed=true but no Wiki note links this source")
    if errors:
        for e in errors:
            print(f"source-lint: {e}", file=sys.stderr)
        return 1
    print(f"source-lint: OK ({len(raw_source_paths())} sources)")
    return 0


def cmd_source_delta(_args: argparse.Namespace) -> int:
    manifest_paths = {r["path"] for r in _load_jsonl(MANIFEST_PATH)} if MANIFEST_PATH.exists() else set()
    delta = []
    for path in raw_source_paths():
        rel = norm_path(str(path.relative_to(ROOT)))
        if rel not in manifest_paths:
            delta.append(rel)
            print(rel)
    if not delta:
        print("source-delta: none")
    else:
        print(f"source-delta: {len(delta)} not in manifest")
    return 0


def cmd_source_coverage(_args: argparse.Namespace) -> int:
    coverage = _wiki_coverage_map()
    for path in raw_source_paths():
        rel = norm_path(str(path.relative_to(ROOT)))
        covered = coverage.get(rel, [])
        print(f"{rel}: {covered if covered else '(uncovered)'}")
    return 0


def cmd_search_catalog(args: argparse.Namespace) -> int:
    query = (args.query or "").lower()
    if not query:
        print("search-catalog: provide --query", file=sys.stderr)
        return 1
    if not CATALOG_PATH.exists():
        print("search-catalog: run build first", file=sys.stderr)
        return 1
    hits = 0
    for rec in _load_jsonl(CATALOG_PATH):
        hay = " ".join(
            [
                rec.get("path", ""),
                rec.get("title", ""),
                rec.get("tag", ""),
                " ".join(rec.get("topics", [])),
            ]
        ).lower()
        if query in hay:
            hits += 1
            print(json.dumps(rec, ensure_ascii=False))
    if hits == 0:
        print(f"search-catalog: no matches for {query!r}")
    else:
        print(f"search-catalog: {hits} match(es)", file=sys.stderr)
    return 0


def cmd_log(args: argparse.Namespace) -> int:
    title = args.title or "Log entry"
    details = args.details or ""
    stamp = date.today().isoformat()
    entry = f"\n## {title} ({stamp})\n\n{details}\n"
    if WIKI_LOG.exists():
        content = WIKI_LOG.read_text(encoding="utf-8")
    else:
        content = "# Wiki Activity Log\n"
    WIKI.mkdir(parents=True, exist_ok=True)
    WIKI_LOG.write_text(content.rstrip() + entry + "\n", encoding="utf-8")
    print(f"log: appended to {WIKI_LOG.relative_to(ROOT)}")
    return 0


def _load_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="LLM Wiki maintenance tool")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("doctor")
    sub.add_parser("build")
    sub.add_parser("lint")

    p_scan = sub.add_parser("source-scan")
    p_scan.add_argument("--update", action="store_true")
    p_scan.add_argument("--accept-covered", action="store_true")

    sub.add_parser("source-lint")
    sub.add_parser("source-delta")
    sub.add_parser("source-coverage")

    p_search = sub.add_parser("search-catalog")
    p_search.add_argument("--query", required=True)

    p_log = sub.add_parser("log")
    p_log.add_argument("--title", required=True)
    p_log.add_argument("--details", default="")

    args = parser.parse_args()
    handlers = {
        "doctor": cmd_doctor,
        "build": cmd_build,
        "lint": cmd_lint,
        "source-scan": cmd_source_scan,
        "source-lint": cmd_source_lint,
        "source-delta": cmd_source_delta,
        "source-coverage": cmd_source_coverage,
        "search-catalog": cmd_search_catalog,
        "log": cmd_log,
    }
    return handlers[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
