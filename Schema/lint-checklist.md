# Lint Checklist

Run `python scripts/wiki_tool.py lint` and `source-lint` before every meaningful commit.

## Compiled Wiki notes (`lint`)

- [ ] File is under `Wiki/Topics|Concepts|Entities|Projects|Logs/`
- [ ] Frontmatter present with closing `---`
- [ ] Exactly one allowed tag: `topic`, `concept`, `entity`, `project`, `log`
- [ ] `source_count` equals length of `sources` list
- [ ] Every path in `sources` exists under `Raw/Sources/` (including nested subfolders)
- [ ] No ambiguous source wikilinks (duplicate Title or stem across Raw sources without path wikilink)
- [ ] `updated` and `created` are present (YYYY-MM-DD)
- [ ] Note body has no `[[wikilinks]]` (use `[Label](relative/path.md)` per `.agents/skills/llm-wiki-LINKS.md`)

## Raw sources (`source-lint`)

- [ ] `Title`, `Reference`, `Created`, `Processed`, and `tags` (including `source`) present
- [ ] If `Processed: true`, at least one Wiki note lists this file in `sources`
- [ ] No duplicate `Title` or filename stem across Raw sources (unless only one is linked via path wikilink)
- [ ] Manifest row exists after `source-scan --update --accept-covered`

## Catalog and indexes (`build`)

- [ ] `Wiki/catalog.jsonl` regenerated
- [ ] `Wiki/index.md` and per-folder `index.md` files updated

## Public audit (`audit_public.py`)

- [ ] No private keys, tokens, or obvious secrets in tracked files
- [ ] No machine-local paths leaked into committed content
- [ ] No `.obsidian/plugins` or cache paths committed

## Doctor (`doctor`)

- [ ] Required folders exist
- [ ] Python 3.9+
- [ ] Catalog readable if present
