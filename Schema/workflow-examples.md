# Workflow Examples

## Ingest a new source

1. Add cleaned Markdown to `Raw/Sources/` using `_templates/source-note.md`.
2. Search existing knowledge:

   ```bash
   python scripts/wiki_tool.py search-catalog --query "related topic"
   ```

3. Open only the most relevant `Wiki/` notes.
4. Create or update focused notes in the correct `Wiki/` subfolder.
5. Set `sources` and `source_count` on each compiled note.
6. Set Raw source `Processed: true` when coverage is complete.
7. Run:

   ```bash
   python scripts/wiki_tool.py build
   python scripts/wiki_tool.py lint
   python scripts/wiki_tool.py source-scan --update --accept-covered
   python scripts/wiki_tool.py source-lint
   ```

8. Optionally log: `python scripts/wiki_tool.py log --title "Ingest" --details "..."`

## Answer a question from the Wiki

1. Read `Wiki/index.md`.
2. `python scripts/wiki_tool.py search-catalog --query "user topic"`
3. Open matching compiled notes.
4. Open `Raw/Sources/` only when compiled notes lack evidence or the user wants verification.
5. Cite both Wiki note path and Raw source when claims depend on source material.

## Pre-commit maintenance

```bash
python scripts/wiki_tool.py doctor
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-lint
python scripts/audit_public.py
```

After ingestion, add `source-scan --update --accept-covered` before `source-lint`.
