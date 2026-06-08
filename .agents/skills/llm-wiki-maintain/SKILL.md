---
name: llm-wiki-maintain
description: Rebuilds Wiki catalog and indexes, updates source manifest, and keeps Schema artifacts current. Use when rebuilding catalog.jsonl, refreshing indexes, or updating source-manifest.jsonl.
---

# LLM Wiki Maintain

Read [AGENTS.md](../../AGENTS.md), [llm-wiki-LINKS.md](../llm-wiki-LINKS.md), and [Schema/command-reference.md](../../Schema/command-reference.md).

## Rebuild artifacts

```bash
python scripts/wiki_tool.py build
```

Produces `Wiki/catalog.jsonl`, `Wiki/index.md`, and per-folder `index.md` files. Catalog `sources` arrays store full vault paths (may include nested subpaths under `Raw/Sources/`).

**`Wiki/index.md` layout:**

- **By Raw domain** — tree mirroring `Raw/Sources/`; one Topic (entry point) per source; `processed` / `unprocessed` badge; link to Raw file.
- **Appendix — by note type** — flat Topics/Concepts/… lists sorted by `updated` (newest first).

Wiki note files remain in `Wiki/Topics/`, `Concepts/`, etc. Only the index view is tree-shaped.

**Indexes:** `build` emits **Markdown links** (`[Title](Topics/foo.md)`), not wikilinks — so index pages stay clickable in Cursor and Obsidian.

## Source manifest

```bash
python scripts/wiki_tool.py source-scan
python scripts/wiki_tool.py source-scan --update --accept-covered
python scripts/wiki_tool.py source-delta
python scripts/wiki_tool.py source-coverage
```

## Migrating old body wikilinks

1. Replace `[[slug]]` with `[Title](../Folder/slug.md)` using paths from [llm-wiki-LINKS.md](../llm-wiki-LINKS.md).
2. Keep frontmatter `sources` as `"[[Raw Title]]"`.
3. Run `build` and `lint`.

## Hooks

Install once: `bash scripts/install_hooks.sh` (Git Bash on Windows). Pre-commit runs build, lint, source-lint.

## Commit generated files

After `build` and `source-scan --update`, commit `Wiki/catalog.jsonl`, `Wiki/index.md`, folder indexes, and `Schema/source-manifest.jsonl` when they changed.
