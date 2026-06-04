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

# Go Mistakes: Concurrency Foundations

Mistakes #55–60 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: concurrency vs parallelism, races, workloads, and contexts.

| # | Mistake | TL;DR |
|---|---------|-------|
| 55 | Concurrency vs parallelism | Concurrency = structure; parallelism = execution; concurrency enables parallelism |
| 56 | Concurrency always faster | Small workloads may be slower concurrently; benchmark to validate |
| 57 | Channels vs mutexes | Parallel goroutines → mutexes for shared state; concurrent goroutines → channels for coordination |
| 58 | Data races vs race conditions | Data race = concurrent write + access; race-free ≠ deterministic; race condition = timing-dependent behavior |
| 59 | Workload type impacts | CPU-bound → ~`GOMAXPROCS` goroutines; I/O-bound → depends on external latency |
| 60 | Misunderstanding contexts | Deadlines, cancellation signals, and values; `Done()` closes on cancel/deadline; pass context to blocking calls |

See also [Concurrency practice](../Concepts/go-mistakes-concurrency-practice.md) for applied patterns (#61–74).
