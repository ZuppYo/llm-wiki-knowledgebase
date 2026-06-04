# Vault links (LLM Wiki)

Use **two link styles** so links work in Cursor/standard Markdown previews **and** in Obsidian.

## Frontmatter `sources` (Raw citations)

Obsidian **Links** property — quoted wikilinks to Raw note titles:

```yaml
sources:
  - "[[LangGraph 101]]"
source_count: 1
```

Match Raw `Title` or filename stem. Do **not** use `Raw/Sources/...` paths here.

## Note body (Wiki ↔ Wiki, indexes)

Use **standard Markdown links** with a **relative path** from the current file:

```markdown
[LangChain 101](langchain-101.md)
[Deep Agent Framework](../Concepts/deep-agent-framework.md)
```

Same pattern as skill cross-references, e.g. [PROPERTIES.md](PROPERTIES.md).

| From | To | Example |
|------|-----|---------|
| `Wiki/Topics/a.md` | topic in same folder | `[B](b.md)` |
| `Wiki/Topics/a.md` | concept | `[C](../Concepts/c.md)` |
| `Wiki/index.md` | any Wiki note | `[T](Topics/t.md)` |
| `Wiki/Topics/index.md` | topic in folder | `[T](t.md)` |

**Do not** use `[[wikilinks]]` in compiled Wiki **body** text — many editors cannot click them. Obsidian still opens `[text](path.md)` normally.

## When wikilinks are OK

- Frontmatter `sources` (required for Properties)
- Raw notes and free-form Obsidian capture (optional)
- Embeds: `![[Note]]` when you intentionally embed content

## Agents

When creating or editing vault Markdown, read `.cursor/skills/obsidian-markdown/SKILL.md` and follow this file for link syntax.
