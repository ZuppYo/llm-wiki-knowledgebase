---
name: llm-wiki-query
description: Answers questions by searching Wiki/catalog.jsonl and compiled notes before opening Raw sources. Use when answering questions, researching the vault, or querying LLM Wiki knowledge.
---

# LLM Wiki Query

Read [AGENTS.md](../../AGENTS.md) first.

## Steps

1. Read `Wiki/index.md` for structure.
2. `python scripts/wiki_tool.py search-catalog --query "<user topic>"`
3. Open the best-matching compiled notes under `Wiki/`.
4. Open `Raw/Sources/` only if compiled notes lack detail or the user needs source verification.
5. Cite Wiki path and Raw source path for source-dependent claims.

## Prefer

- Catalog search over reading all of `Raw/Sources/`
- Short compiled notes over full Raw transcripts

## Do not

- Read entire Raw folders when catalog search suffices
- State facts without a linked source when material comes from this Wiki
