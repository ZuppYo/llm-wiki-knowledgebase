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

# Go Mistakes: Error Management

Mistakes #48–54 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: panics, wrapping, comparison, and handling discipline.

| # | Mistake | TL;DR |
|---|---------|-------|
| 48 | Panicking | Reserve for programmer errors or fatal missing dependencies; otherwise return errors |
| 49 | When to wrap errors | `%w` adds context and exposes source; use `%v` or custom types to avoid coupling |
| 50 | Comparing error types | With wrapping, use `errors.As` instead of type assertions |
| 51 | Comparing error values | Sentinel errors (`var ErrFoo`); use `errors.Is` with wrapped errors, not `==` |
| 52 | Handling an error twice | Log *or* return, not both; wrapping propagates context |
| 53 | Not handling an error | Use `_` explicitly when ignoring; document why |
| 54 | Not handling defer errors | Handle or propagate defer errors; use `_ = fn()` with comment if intentional |

**Convention from source:** expected errors → sentinel values; unexpected errors → custom types implementing `error`.
