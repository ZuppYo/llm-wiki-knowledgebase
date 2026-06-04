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

# Go Mistakes: Functions and Methods

Mistakes #42–47 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: receivers, named results, interfaces, and `defer` evaluation.

| # | Mistake | TL;DR |
|---|---------|-------|
| 42 | Wrong receiver type | Pointer receiver when mutating, containing uncopyable fields, or large; value receiver for immutability, maps/channels/funcs, small value types |
| 43 | Never using named result parameters | Improves readability when multiple same-type returns; initialized to zero values |
| 44 | Side effects with named results | Named results start at zero; naked `return err` may return nil unintentionally |
| 45 | Returning a nil receiver | Typed nil pointer returned as interface is non-nil; return explicit nil interface value |
| 46 | Filename as function input | Prefer `io.Reader` over filenames for reuse and testability |
| 47 | `defer` argument evaluation | Arguments and receivers evaluated immediately; use pointer arg or closure for late binding |
