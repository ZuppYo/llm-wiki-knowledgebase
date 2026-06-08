---
name: llm-wiki-query
description: Answers questions by searching Wiki/catalog.jsonl and compiled notes before opening Raw sources. Use when answering questions, researching the vault, or querying LLM Wiki knowledge.
---

# LLM Wiki Query

Read [AGENTS.md](../../AGENTS.md) and [llm-wiki-LINKS.md](../llm-wiki-LINKS.md). For Markdown edits, follow `.cursor/skills/obsidian-markdown/`.

## Steps

1. `python scripts/wiki_tool.py search-catalog --query "<user topic>"` — primary lookup for questions.
2. Optional: skim [Wiki/index.md](../../Wiki/index.md) **By Raw domain** to orient by source area, or **Appendix** for recent notes by type.
3. Open the best-matching compiled notes under `Wiki/` (usually via Topic entry points).
4. Open `Raw/Sources/` only if compiled notes lack detail or the user needs source verification.
5. Cite Wiki path and Raw source path for source-dependent claims.

## Links when writing or updating Wiki notes

- **Body:** `[Display](relative/path.md)` only — see [llm-wiki-LINKS.md](../llm-wiki-LINKS.md).
- **Frontmatter `sources`:** quoted wikilinks to Raw titles, e.g. `"[[LangChain 101]]"`.

## Prefer

- Catalog search over reading all of `Raw/Sources/`
- Short compiled notes over full Raw transcripts

## Do not

- Read entire Raw folders when catalog search suffices
- State facts without a linked source when material comes from this Wiki
- Add `[[wikilinks]]` in Wiki body text (use Markdown links)
