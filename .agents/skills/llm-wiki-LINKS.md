# LLM Wiki — link rules (all llm-wiki skills)

Read with [AGENTS.md](../../AGENTS.md) and `.cursor/skills/obsidian-markdown/references/VAULT-LINKS.md`.

## Two formats

| Location | Syntax | Example |
|----------|--------|---------|
| Frontmatter `sources` | Quoted Obsidian wikilink | `- "[[LangGraph 101]]"` or nested `- "[[Knowledge/Ai/LLMWiki/llm-wiki-starter-demo]]"` |
| Note **body**, generated **indexes** | Standard Markdown | `[LangGraph 101](../Topics/langgraph-101.md)` |

**Why:** `[[wikilinks]]` in body often do not click in Cursor/VS Code. `[text](path.md)` works in Cursor and Obsidian.

## Relative paths (from current file)

| From folder | To same folder | To sibling folder |
|-------------|----------------|-------------------|
| `Wiki/Topics/` | `[B](b.md)` | `[C](../Concepts/c.md)` |
| `Wiki/Concepts/` | `[C](c.md)` | `[T](../Topics/t.md)` |
| `Wiki/Logs/` | `[L](l.md)` | `[T](../Topics/t.md)` |
| `Wiki/index.md` | — | `[T](Topics/t.md)` |

## Nested Raw sources

- Prefer title wikilinks when Raw `Title` is globally unique: `"[[LangGraph 101]]"`
- When filename stems collide across subfolders, use path wikilinks relative to `Raw/Sources/`: `"[[Knowledge/Ai/AgentHarness/Agent Harness]]"`
- `lint` fails on ambiguous wikilinks; `source-lint` fails on duplicate Titles or stems

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
