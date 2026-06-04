# LLM Wiki — link rules (all llm-wiki skills)

Read with [AGENTS.md](../../AGENTS.md) and `.cursor/skills/obsidian-markdown/references/VAULT-LINKS.md`.

## Two formats

| Location | Syntax | Example |
|----------|--------|---------|
| Frontmatter `sources` | Quoted Obsidian wikilink | `- "[[LangGraph 101]]"` |
| Note **body**, generated **indexes** | Standard Markdown | `[LangGraph 101](../Topics/langgraph-101.md)` |

**Why:** `[[wikilinks]]` in body often do not click in Cursor/VS Code. `[text](path.md)` works in Cursor and Obsidian.

## Relative paths (from current file)

| From folder | To same folder | To sibling folder |
|-------------|----------------|-------------------|
| `Wiki/Topics/` | `[B](b.md)` | `[C](../Concepts/c.md)` |
| `Wiki/Concepts/` | `[C](c.md)` | `[T](../Topics/t.md)` |
| `Wiki/Logs/` | `[L](l.md)` | `[T](../Topics/t.md)` |
| `Wiki/index.md` | — | `[T](Topics/t.md)` |

## Do not

- Put `[[slug]]` or `[[Wiki/...|label]]` in Wiki **body** prose
- Put `Raw/Sources/...` paths in frontmatter `sources` (use wikilink to Raw `Title`)

## Lint

`python scripts/wiki_tool.py lint` fails if a compiled Wiki note body contains `[[...]]`.

## Skills

- **ingest** — set frontmatter wikilinks; write body with Markdown links
- **query** — cite paths; when editing answers into Wiki, use Markdown links
- **maintain** — `build` writes indexes as Markdown links
- **lint** — includes body wikilink check
