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

# Go Mistakes: Control Structures

Mistakes #30–35 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: `range`, maps, `break`, and `defer` in loops.

| # | Mistake | TL;DR |
|---|---------|-------|
| 30 | Range loop element copies | Value in `range` is a copy; mutate via index or pointer field |
| 31 | Range argument evaluation | Expression evaluated once before loop (array/slice/channel copy semantics) |
| 32 | Pointer elements in range loops | **Obsolete from Go 1.22** (per-loop variable semantics) |
| 33 | Map iteration assumptions | No key order, insertion order, or deterministic iteration; new keys may not appear in current pass |
| 34 | `break` in nested constructs | `break` exits innermost `for`/`switch`/`select`; use labels to break outer loops |
| 35 | `defer` inside a loop | `defer` runs when the surrounding function returns; extract per-iteration function or closure |
