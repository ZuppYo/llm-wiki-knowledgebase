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

# Go Mistakes: Optimizations

Mistakes #91–100 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: CPU caches, memory, GC, and profiling.

| # | Mistake | TL;DR |
|---|---------|-------|
| 91 | Not understanding CPU caches | L1 ~50–100× RAM; 64-byte cache lines; spatial locality; struct field ordering |
| 92 | False sharing | Pad or separate counters updated by different cores |
| 93 | Instruction-level parallelism | Reduce data hazards; enable parallel CPU instruction execution |
| 94 | Data alignment | Reorder struct fields by size descending for compact layout |
| 95 | Stack vs heap | Stack allocation is cheap; heap triggers GC cost |
| 96 | Reducing allocations | API design, compiler escape analysis, `sync.Pool` |
| 97 | Not relying on inlining | Fast-path inlining reduces call overhead |
| 98 | Not using diagnostics | `pprof` and execution tracer to find hot paths |
| 99 | Not understanding GC | Tune GC for load spikes (e.g. `GOGC`, memory limit) |
| 100 | Go in Docker/Kubernetes | **Obsolete from Go 1.25** (container-aware `GOMAXPROCS`) |

These build on [Data types](../Concepts/go-mistakes-data-types.md) slice/map behavior and [Concurrency foundations](../Concepts/go-mistakes-concurrency-foundations.md) workload sizing.
