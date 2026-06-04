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

# Go Mistakes: Data Types

Mistakes #17–29 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: numeric literals, slices, maps, and comparisons.

| # | Mistake | TL;DR |
|---|---------|-------|
| 17 | Octal literal confusion | Leading `0` is octal; prefer explicit `0o` prefix |
| 18 | Neglecting integer overflows | Compile-time overflow errors; runtime overflow is silent |
| 19 | Not understanding floating-points | Compare with epsilon; group similar magnitudes; multiply/divide before add/subtract |
| 20 | Slice length vs capacity | Length = available elements; capacity = backing array size |
| 21 | Inefficient slice initialization | Pre-size with `make` length or capacity when size is known |
| 22 | Nil vs empty slice | Both zero-length; only nil needs no allocation; APIs should not distinguish them |
| 23 | Checking slice emptiness | Use `len == 0`, not `== nil` |
| 24 | Slice copy semantics | `copy` copies `min(len(src), len(dst))` elements |
| 25 | `append` side effects | Shared backing arrays mutate; use copy or full slice expression `s[lo:hi:max]` |
| 26 | Slices and memory leaks | Large-slice subslices retain backing array; nil pointer elements after slice |
| 27 | Inefficient map initialization | Provide initial size when element count is known |
| 28 | Maps and memory leaks | Maps grow but never shrink; recreate or use pointers if needed |
| 29 | Comparing values incorrectly | `==` only for comparable types; slices/maps need `reflect.DeepEqual`, custom logic, or stdlib helpers |
