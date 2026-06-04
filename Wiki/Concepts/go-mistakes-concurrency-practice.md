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

# Go Mistakes: Concurrency Practice

Mistakes #61–74 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: contexts, goroutine lifecycle, channels, sync primitives.

| # | Mistake | TL;DR |
|---|---------|-------|
| 61 | Inappropriate context propagation | HTTP request context cancels after response; use `context.WithoutCancel` (Go 1.21+) for async work |
| 62 | Goroutine without stop plan | Every goroutine needs a shutdown path; block parent until cleanup completes |
| 63 | Goroutines and loop variables | **Obsolete from Go 1.22** (per-iteration loop vars) |
| 64 | Non-deterministic `select` | Multiple ready cases chosen randomly, not by source order |
| 65 | Not using notification channels | Signal without data via `chan struct{}` |
| 66 | Not using nil channels | Nil channel cases removed from `select`; useful for merge patterns |
| 67 | Channel size confusion | Unbuffered = strong sync; default buffered size 1 unless worker pool or rate limit |
| 68 | String formatting side effects | `%v` on types with `String()` can deadlock under locks |
| 69 | Data races with `append` | Concurrent `append` on shared slice with spare capacity races |
| 70 | Mutexes with slices/maps | Assignment copies header, not data; protect iteration or deep-copy |
| 71 | Misusing `sync.WaitGroup` | Call `Add` before starting goroutines, not inside them |
| 72 | Forgetting `sync.Cond` | Broadcast repeated notifications to waiting goroutines |
| 73 | Not using `errgroup` | Coordinate goroutines with shared error and context cancellation |
| 74 | Copying sync types | Never copy `Mutex`, `WaitGroup`, etc. |

Prerequisites: [Concurrency foundations](../Concepts/go-mistakes-concurrency-foundations.md).
