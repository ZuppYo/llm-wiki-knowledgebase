"""Tests for Wiki/index.md tree generation in wiki_tool.py."""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wiki_tool as wt  # noqa: E402


class WikiIndexTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmpdir = tempfile.mkdtemp()
        self._root = Path(self._tmpdir)
        self._raw = self._root / "Raw" / "Sources"
        self._wiki = self._root / "Wiki"
        self._raw.mkdir(parents=True)
        for sub in wt.WIKI_SUBDIRS:
            (self._wiki / sub).mkdir(parents=True)
        self._orig_root = wt.ROOT
        self._orig_raw = wt.RAW_SOURCES
        self._orig_wiki = wt.WIKI
        self._orig_catalog = wt.CATALOG_PATH
        wt.ROOT = self._root
        wt.RAW_SOURCES = self._raw
        wt.WIKI = self._wiki
        wt.CATALOG_PATH = self._wiki / "catalog.jsonl"
        wt._invalidate_source_index()

    def tearDown(self) -> None:
        wt.ROOT = self._orig_root
        wt.RAW_SOURCES = self._orig_raw
        wt.WIKI = self._orig_wiki
        wt.CATALOG_PATH = self._orig_catalog
        wt._invalidate_source_index()
        shutil.rmtree(self._tmpdir, ignore_errors=True)

    def _write_source(self, rel: str, title: str, *, processed: bool = False) -> None:
        path = self._raw / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"---\nTitle: {title}\nReference: test\nCreated: 2026-06-04\n"
            f"Processed: {'true' if processed else 'false'}\ntags:\n  - source\n---\n\n# {title}\n",
            encoding="utf-8",
        )

    def _write_wiki(
        self,
        folder: str,
        slug: str,
        *,
        tag: str,
        title: str,
        source_title: str,
        updated: str,
    ) -> None:
        path = self._wiki / folder / f"{slug}.md"
        path.write_text(
            f"---\ntags:\n  - {tag}\nstatus: seed\ncreated: 2026-06-01\n"
            f"updated: {updated}\nsources:\n  - \"[[{source_title}]]\"\n"
            f"source_count: 1\naliases: []\n---\n\n# {title}\n",
            encoding="utf-8",
        )

    def test_tree_shows_topic_entry_only(self) -> None:
        self._write_source("Knowledge/Ai/demo.md", "Demo Source", processed=True)
        self._write_wiki("Topics", "demo-101", tag="topic", title="Demo 101", source_title="Demo Source", updated="2026-06-08")
        self._write_wiki(
            "Concepts",
            "demo-detail",
            tag="concept",
            title="Demo Detail",
            source_title="Demo Source",
            updated="2026-06-07",
        )
        wt.cmd_build(wt.argparse.Namespace())
        index = (self._wiki / "index.md").read_text(encoding="utf-8")
        self.assertIn("## By Raw domain", index)
        self.assertIn("### Knowledge / Ai", index)
        self.assertIn("[Demo 101](Topics/demo-101.md)", index)
        self.assertNotIn("[Demo Detail](Concepts/demo-detail.md)", index.split("## Appendix")[0])

    def test_unprocessed_source_in_tree(self) -> None:
        self._write_source("pending.md", "Pending Source", processed=False)
        wt.cmd_build(wt.argparse.Namespace())
        index = (self._wiki / "index.md").read_text(encoding="utf-8")
        self.assertIn("· unprocessed", index)
        self.assertIn("#### Pending Source", index)

    def test_appendix_sorted_by_updated_desc(self) -> None:
        self._write_source("a.md", "Source A", processed=True)
        self._write_wiki("Topics", "older", tag="topic", title="Older Topic", source_title="Source A", updated="2026-06-01")
        self._write_wiki("Topics", "newer", tag="topic", title="Newer Topic", source_title="Source A", updated="2026-06-09")
        wt.cmd_build(wt.argparse.Namespace())
        index = (self._wiki / "index.md").read_text(encoding="utf-8")
        appendix = index.split("## Appendix")[1]
        self.assertLess(appendix.index("Newer Topic"), appendix.index("Older Topic"))

    def test_pick_entry_point_prefers_topic_over_concept(self) -> None:
        records = [
            {"path": "Wiki/Concepts/x.md", "tag": "concept", "title": "X"},
            {"path": "Wiki/Topics/y.md", "tag": "topic", "title": "Y"},
        ]
        by_path = wt._records_by_path(records)
        entry = wt._pick_entry_point(["Wiki/Concepts/x.md", "Wiki/Topics/y.md"], by_path)
        self.assertEqual(entry["path"], "Wiki/Topics/y.md")


if __name__ == "__main__":
    unittest.main()
