# LLM Wiki — Agent Rules

This vault separates **source material** from **compiled knowledge**. Follow these rules on every task.

## Layers

| Layer | Path | Purpose |
|-------|------|---------|
| Raw | `Raw/Sources/` | Original captured material. Not compiled notes. Subfolders allowed (e.g. `Raw/Sources/Knowledge/Ai/`). |
| Wiki | `Wiki/` | Concise, reusable, linked knowledge notes. |
| Schema | `Schema/` | Frontmatter rules, lint checklist, manifests, command reference. |

Binary or large attachments go in `Raw/Files/` (gitignored by default; subfolders allowed, e.g. `Raw/Files/<source-id>/`).

## Core rules

1. **Treat `Raw/Sources/` as source material only.** Do not treat Raw notes as finished wiki answers.
2. **Write reusable knowledge only under `Wiki/`.** Use `Wiki/Topics/`, `Concepts/`, `Entities/`, `Projects/`, or `Logs/` as appropriate.
3. **Link every compiled note to one or more Raw sources** in frontmatter `sources` as quoted wikilinks (e.g. `"[[LangGraph 101]]"`) per Obsidian Links properties — not plain `Raw/Sources/...` paths. Keep `source_count` equal to `len(sources)`.
4. **Markdown links:** follow [llm-wiki-LINKS.md](.agents/skills/llm-wiki-LINKS.md) and `.cursor/skills/obsidian-markdown/` ([VAULT-LINKS.md](.cursor/skills/obsidian-markdown/references/VAULT-LINKS.md)). Body = `[Display](relative/path.md)`; frontmatter `sources` = `"[[Raw Title]]"`. No `[[wikilinks]]` in Wiki body.
5. **Search `Wiki/catalog.jsonl` before opening broad Raw context.** Use `python scripts/wiki_tool.py search-catalog --query "..."`. For domain browse or ingest gaps, read the **By Raw domain** section of `Wiki/index.md` (entry points only); use the appendix for flat lookup by note type.
6. **Run maintenance before commits:** `doctor`, `build`, `lint`, `source-lint`, and `scripts/audit_public.py`. After ingestion, also run `source-scan --update --accept-covered`.
7. **Do not invent citations** or add claims without support from linked Raw sources.

## Workflows

- **Ingest:** See `Schema/workflow-examples.md` and skill `.agents/skills/llm-wiki-ingest/`.
- **Query:** Search catalog first; open Raw only when compiled notes are insufficient.
- **Lint:** See `Schema/lint-checklist.md` and `Schema/command-reference.md`.

## Tools

```bash
python scripts/wiki_tool.py doctor
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-scan --update --accept-covered
python scripts/wiki_tool.py source-lint
python scripts/wiki_tool.py search-catalog --query "topic"
python scripts/audit_public.py
```

Templates live in `_templates/`. Do not create a `bonus/` folder unless the user explicitly requests advanced modules.
