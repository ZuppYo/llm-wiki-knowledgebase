"""Tests for Raw/Sources subfolder support in wiki_tool.py."""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import wiki_tool as wt  # noqa: E402


class SubfolderSourceTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmpdir = tempfile.mkdtemp()
        self._root = Path(self._tmpdir)
        self._raw = self._root / "Raw" / "Sources"
        self._raw.mkdir(parents=True)
        self._orig_root = wt.ROOT
        self._orig_raw = wt.RAW_SOURCES
        wt.ROOT = self._root
        wt.RAW_SOURCES = self._raw
        wt._invalidate_source_index()

    def tearDown(self) -> None:
        wt.ROOT = self._orig_root
        wt.RAW_SOURCES = self._orig_raw
        wt._invalidate_source_index()
        shutil.rmtree(self._tmpdir, ignore_errors=True)

    def _write_source(self, rel: str, title: str) -> None:
        path = self._raw / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"---\nTitle: {title}\nReference: test\nCreated: 2026-06-04\nProcessed: false\ntags:\n  - source\n---\n\n# {title}\n",
            encoding="utf-8",
        )

    def test_rglob_finds_nested_sources(self) -> None:
        self._write_source("flat.md", "Flat")
        self._write_source("a/nested.md", "Nested")
        paths = [p.name for p in wt.raw_source_paths()]
        self.assertEqual(sorted(paths), ["flat.md", "nested.md"])

    def test_title_wikilink_resolves_nested(self) -> None:
        self._write_source("Knowledge/Ai/foo.md", "Unique Title")
        resolved = wt.resolve_source_ref("[[Unique Title]]")
        self.assertEqual(resolved, "Raw/Sources/Knowledge/Ai/foo.md")

    def test_path_wikilink_resolves_nested(self) -> None:
        self._write_source("Knowledge/Ai/foo.md", "Unique Title")
        resolved = wt.resolve_source_ref("[[Knowledge/Ai/foo]]")
        self.assertEqual(resolved, "Raw/Sources/Knowledge/Ai/foo.md")

    def test_ambiguous_stem_returns_none(self) -> None:
        self._write_source("a/readme.md", "Title A")
        self._write_source("b/readme.md", "Title B")
        resolved, ambiguous = wt.resolve_source_ref_detail("[[readme]]")
        self.assertIsNone(resolved)
        self.assertEqual(len(ambiguous), 2)

    def test_duplicate_stem_errors(self) -> None:
        self._write_source("a/readme.md", "Title A")
        self._write_source("b/readme.md", "Title B")
        index = wt._build_source_index()
        errors = wt._duplicate_source_errors(index)
        self.assertTrue(any("duplicate Raw filename stem 'readme'" in e for e in errors))


if __name__ == "__main__":
    unittest.main()