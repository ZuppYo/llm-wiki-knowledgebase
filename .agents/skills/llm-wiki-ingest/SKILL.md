---
name: llm-wiki-ingest
description: Compiles Raw/Sources material into concise Wiki notes with source backlinks. Use when adding sources, ingesting notes, compiling Raw into Wiki, or processing unprocessed sources.
---

# LLM Wiki Ingest

Read [AGENTS.md](../../AGENTS.md) first. For Obsidian frontmatter and links, also follow `.cursor/skills/obsidian-markdown/` (especially Properties → **Links** type).

## Steps

1. Confirm source note in `Raw/Sources/` matches [Schema/frontmatter-schema.md](../../Schema/frontmatter-schema.md).
2. `python scripts/wiki_tool.py search-catalog --query "<keywords>"`
3. Update or create notes in the correct `Wiki/` folder using `_templates/`.
4. Set `sources` as quoted Obsidian **Links** (wikilinks), not plain paths:

   ```yaml
   sources:
     - "[[LangGraph 101]]"
   ```

   Match the Raw note `Title` or filename stem (e.g. `LangChain 101`, `llm-wiki-starter-demo`). Do **not** use `Raw/Sources/...` in frontmatter — Properties will not click. Keep `source_count` accurate.
5. Set source `Processed: true` when coverage is complete.
6. Run build, lint, source-scan, source-lint (see [Schema/workflow-examples.md](../../Schema/workflow-examples.md)).
7. `python scripts/wiki_tool.py log --title "Ingest" --details "..."` if the Wiki changed materially.

## Do not

- Publish long prose only in Raw without compiled Wiki notes
- Invent citations or sources not in `Raw/Sources/`
- Skip `source_count` alignment
