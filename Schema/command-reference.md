# Command Reference

All commands run from the vault root. Use `python scripts/wiki_tool.py` (or `python3` on Unix).

## wiki_tool.py

| Command | Description |
|---------|-------------|
| `doctor` | Non-mutating health check: folders, Python version, catalog/manifest readability, counts |
| `build` | Generate `Wiki/catalog.jsonl`, `Wiki/index.md`, per-folder `index.md` files |
| `lint` | Validate compiled Wiki frontmatter, tags, sources, `source_count` |
| `source-scan` | List Raw sources; optional manifest update |
| `source-scan --update --accept-covered` | Write `Schema/source-manifest.jsonl` |
| `source-lint` | Validate Raw source frontmatter and processed/coverage rules |
| `source-delta` | Raw sources missing from manifest |
| `source-coverage` | Show Wiki notes covering each Raw source |
| `search-catalog --query "text"` | Search `Wiki/catalog.jsonl` |
| `log --title "title" --details "details"` | Append to `Wiki/log.md` |

## audit_public.py

```bash
python scripts/audit_public.py
```

Fails on private keys, common token patterns, machine-local paths, and committed Obsidian plugin/cache paths.

## install_hooks.sh

```bash
bash scripts/install_hooks.sh
```

Sets `git config core.hooksPath .githooks`. On Windows, use Git Bash.

## Maintenance gate (every meaningful commit)

```bash
python scripts/wiki_tool.py doctor
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-lint
python scripts/audit_public.py
```

## After source ingestion

```bash
python scripts/wiki_tool.py source-scan --update --accept-covered
python scripts/wiki_tool.py source-lint
```
