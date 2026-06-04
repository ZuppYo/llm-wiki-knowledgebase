# Naming Conventions

## Raw sources

- Path: `Raw/Sources/<slug>.md`
- Slug: lowercase, hyphen-separated, descriptive (`why-llm-wiki.md`, `llm-wiki-starter-demo.md`)
- `Title` in frontmatter: human-readable title
- `Reference`: stable external id (URL, `owned-demo`, ISBN, etc.)

## Compiled Wiki notes

| Type | Folder | Tag | Example |
|------|--------|-----|---------|
| Topic | `Wiki/Topics/` | `topic` | `llm-wiki-overview.md` |
| Concept | `Wiki/Concepts/` | `concept` | `raw-vs-wiki-layers.md` |
| Entity | `Wiki/Entities/` | `entity` | `obsidian.md` |
| Project | `Wiki/Projects/` | `project` | `llm-wiki-core-setup.md` |
| Log | `Wiki/Logs/` | `log` | `tutorial-05-first-ingest.md` |

- Slug matches filename without extension.
- `aliases` in frontmatter for alternate link targets.
- Link Raw sources in frontmatter `sources` with quoted wikilinks: `- "[[LangGraph 101]]"` (Obsidian Links property; see `.cursor/skills/obsidian-markdown/references/PROPERTIES.md`)
- In note body, use wikilinks or `[[path/note]]` as usual; `wiki_tool.py` still resolves `sources` to `Raw/Sources/*.md` for catalog/lint

## Indexes and artifacts

- `Wiki/catalog.jsonl` — machine-readable catalog (do not hand-edit; use `build`)
- `Wiki/index.md` — human overview (generated)
- `Wiki/<Folder>/index.md` — per-folder listing (generated)
- `Schema/source-manifest.jsonl` — source coverage (updated via `source-scan`)

## Logs

- Session logs: `Wiki/Logs/<event-slug>.md`
- Append-only activity: `Wiki/log.md` via `wiki_tool.py log`
