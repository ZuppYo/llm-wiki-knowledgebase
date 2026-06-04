---
name: llm-wiki-maintain
description: Rebuilds Wiki catalog and indexes, updates source manifest, and keeps Schema artifacts current. Use when rebuilding catalog.jsonl, refreshing indexes, or updating source-manifest.jsonl.
---

# LLM Wiki Maintain

Read [AGENTS.md](../../AGENTS.md) and [Schema/command-reference.md](../../Schema/command-reference.md).

## Rebuild artifacts

```bash
python scripts/wiki_tool.py build
```

Produces `Wiki/catalog.jsonl`, `Wiki/index.md`, and per-folder `index.md` files.

## Source manifest

```bash
python scripts/wiki_tool.py source-scan
python scripts/wiki_tool.py source-scan --update --accept-covered
python scripts/wiki_tool.py source-delta
python scripts/wiki_tool.py source-coverage
```

## Hooks

Install once: `bash scripts/install_hooks.sh` (Git Bash on Windows). Pre-commit runs build, lint, source-lint.

## Commit generated files

After `build` and `source-scan --update`, commit `Wiki/catalog.jsonl`, `Wiki/index.md`, folder indexes, and `Schema/source-manifest.jsonl` when they changed.
