---
name: llm-wiki-lint
description: Runs LLM Wiki maintenance gates (doctor, build, lint, source-lint, audit_public) before commits. Use before committing, after edits, or when validating vault health.
---

# LLM Wiki Lint

Read [AGENTS.md](../../AGENTS.md), [llm-wiki-LINKS.md](../llm-wiki-LINKS.md), and [Schema/lint-checklist.md](../../Schema/lint-checklist.md).

## Maintenance gate

```bash
python scripts/wiki_tool.py doctor
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-lint
python scripts/audit_public.py
```

## After ingestion

Add before `source-lint`:

```bash
python scripts/wiki_tool.py source-scan --update --accept-covered
```

## Link checks (`lint`)

- `source_count` matches `sources`; each `sources` wikilink resolves under `Raw/Sources/`
- **No `[[wikilinks]]` in Wiki note body** — use `[Label](relative/path.md)` per [llm-wiki-LINKS.md](../llm-wiki-LINKS.md)
- `build` regenerates `Wiki/index.md` and folder indexes as Markdown links

## On failure

- Fix frontmatter per [Schema/frontmatter-schema.md](../../Schema/frontmatter-schema.md)
- Convert body wikilinks to Markdown links (see [VAULT-LINKS.md](../../.cursor/skills/obsidian-markdown/references/VAULT-LINKS.md))
- Re-run `build` then `lint` and `source-lint`
- Do not commit until all commands exit 0
