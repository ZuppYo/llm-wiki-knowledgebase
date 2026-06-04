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

# Go Mistakes: Testing

Mistakes #82–90 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: test organization, race detection, patterns, and tooling.

| # | Mistake | TL;DR |
|---|---------|-------|
| 82 | Not categorizing tests | Use build tags, env vars, or `-short` to split unit vs integration vs long tests |
| 83 | Not enabling race flag | Run `go test -race` in CI/local; use `//go:build !race` to exclude specific tests |
| 84 | Not using test execution modes | `-parallel` and `-shuffle` expose ordering assumptions |
| 85 | Not using table-driven tests | Reduce duplication; easier to extend cases |
| 86 | Sleeping in unit tests | Prefer synchronization or retry; sleep makes flaky tests |
| 87 | Time API in tests | Inject clocks or hidden time dependencies to avoid flakiness |
| 88 | Not using test utilities | `httptest` for HTTP; `iotest` for reader error tolerance |
| 89 | Inaccurate benchmarks | Preserve timing accuracy; avoid compiler elimination; use `benchstat`; mind observer effect |
| 90 | Missing Go testing features | Coverage (`-coverprofile`); external test package; helper methods on `*testing.T`; setup/teardown |

**Community addition:** fuzzing (native Go fuzzing) for malformed inputs — credited in source to @jeromedoucet.
