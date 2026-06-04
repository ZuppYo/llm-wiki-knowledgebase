---
tags:
  - concept
topics:
  - go-common-mistakes-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[Common Go Mistakes - 100 Go Mistakes and How to Avoid Them]]"
source_count: 1
aliases: []
---

# Go Mistakes: Strings

Mistakes #36–41 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: runes, iteration, concatenation, and memory.

| # | Mistake | TL;DR |
|---|---------|-------|
| 36 | Not understanding runes | Rune = Unicode code point; `len(string)` counts bytes, not runes |
| 37 | Inaccurate string iteration | `range` yields rune + byte index; use value element or `[]rune(s)` for rune index |
| 38 | Misusing trim functions | `TrimLeft`/`TrimRight` trim *sets* of runes; `TrimPrefix`/`TrimSuffix` trim exact affixes |
| 39 | Under-optimized concatenation | Use `strings.Builder`; preallocate with `Grow` for known total length |
| 40 | Useless string conversions | Prefer `bytes` package when working with `[]byte` to avoid string↔byte churn |
| 41 | Substring memory leaks | Substrings share backing array; copy when retaining a small part of a large string |
