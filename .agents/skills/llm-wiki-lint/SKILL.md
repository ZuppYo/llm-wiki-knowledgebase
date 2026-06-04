---
name: llm-wiki-lint
description: Runs LLM Wiki maintenance gates (doctor, build, lint, source-lint, audit_public) before commits. Use before committing, after edits, or when validating vault health.
---

# LLM Wiki Lint

Read [AGENTS.md](../../AGENTS.md) and [Schema/lint-checklist.md](../../Schema/lint-checklist.md).

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

## On failure

- Fix frontmatter per `Schema/frontmatter-schema.md`
- Re-run `build` then `lint` and `source-lint`
- Do not commit until all commands exit 0
