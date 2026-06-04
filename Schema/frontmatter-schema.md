# Frontmatter Schema

## Raw source notes (`Raw/Sources/*.md`)

Required fields:

```yaml
---
Title: ""
Author: ""
Reference: ""
ContentType:
  - "markdown"
Created: YYYY-MM-DD
Processed: false
tags:
  - "source"
---
```

- `Processed: true` only after Wiki notes cover the source and `source-lint` passes.
- `Reference` is a stable id (URL slug, owned-demo, etc.).

## Compiled Wiki notes (`Wiki/**/*.md`)

Exclude `Wiki/index.md`, `Wiki/log.md`, and `Wiki/catalog.jsonl` from compiled-note rules.

```yaml
---
tags:
  - "concept"   # exactly one of: topic, concept, entity, project, log
topics: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "Raw/Sources/example.md"
source_count: 1
aliases: []
---
```

| Field | Rule |
|-------|------|
| `tags` | Single allowed tag: `topic`, `concept`, `entity`, `project`, `log` |
| `sources` | Paths to files under `Raw/Sources/` |
| `source_count` | Must equal number of entries in `sources` |
| `topics` | Optional list of related topic slugs or titles |
| `status` | e.g. `seed`, `stable`, `deprecated` |

## Catalog entry (`Wiki/catalog.jsonl`)

One JSON object per line, produced by `wiki_tool.py build`:

```json
{"path":"Wiki/Concepts/example.md","title":"Example","tag":"concept","topics":[],"sources":["Raw/Sources/example.md"],"updated":"YYYY-MM-DD"}
```

## Source manifest (`Schema/source-manifest.jsonl`)

```json
{"path":"Raw/Sources/example.md","title":"Example","processed":true,"covered_by":["Wiki/Concepts/example.md"],"updated":"YYYY-MM-DD"}
```
