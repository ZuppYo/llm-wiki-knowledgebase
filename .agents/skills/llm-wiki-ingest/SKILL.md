---
name: llm-wiki-ingest
description: Compiles Raw/Sources material into concise Wiki notes with source backlinks. Use when adding sources, ingesting notes, compiling Raw into Wiki, or processing unprocessed sources.
---

# LLM Wiki Ingest

Read [AGENTS.md](../../AGENTS.md) and [llm-wiki-LINKS.md](../llm-wiki-LINKS.md). For Obsidian syntax, follow `.cursor/skills/obsidian-markdown/` — [VAULT-LINKS.md](../../.cursor/skills/obsidian-markdown/references/VAULT-LINKS.md) and [PROPERTIES.md](../../.cursor/skills/obsidian-markdown/references/PROPERTIES.md).

## Steps

1. Confirm source note in `Raw/Sources/` (flat or nested) matches [Schema/frontmatter-schema.md](../../Schema/frontmatter-schema.md).
2. `python scripts/wiki_tool.py search-catalog --query "<keywords>"`
3. Update or create notes in the correct `Wiki/` folder using `_templates/`.
4. **Frontmatter `sources`** — quoted Obsidian **Links** (wikilinks), not plain paths:

   ```yaml
   sources:
     - "[[LangGraph 101]]"
   ```

   Match the Raw note `Title` or filename stem when unique. For nested sources with duplicate stems, use a path wikilink (e.g. `"[[Knowledge/Ai/LLMWiki/llm-wiki-starter-demo]]"`). Keep `source_count` accurate.
5. **Note body** — standard Markdown links only:

   ```markdown
   See [LangGraph 101](../Topics/langgraph-101.md) for prerequisites.
   ```

   From `Wiki/Topics/`, same-folder: `[LangChain 101](langchain-101.md)`. Never `[[slug]]` in body.
6. Set source `Processed: true` when coverage is complete.
7. Run build, lint, source-scan, source-lint (see [Schema/workflow-examples.md](../../Schema/workflow-examples.md)). `build` places the new Topic under the matching **By Raw domain** branch in `Wiki/index.md`.
8. `python scripts/wiki_tool.py log --title "Ingest" --details "..."` if the Wiki changed materially.

## Do not

- Publish long prose only in Raw without compiled Wiki notes
- Invent citations or sources not in `Raw/Sources/`
- Skip `source_count` alignment
- Use wikilinks in Wiki body (lint will fail)
