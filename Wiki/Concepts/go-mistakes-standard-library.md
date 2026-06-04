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

# Go Mistakes: Standard Library

Mistakes #75–81 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: time, JSON, SQL, HTTP, and resource cleanup.

| # | Mistake | TL;DR |
|---|---------|-------|
| 75 | Wrong time duration | `time.Duration` is nanoseconds; use `time.Second`, not bare integers |
| 76 | `time.After` memory leaks | **Obsolete from Go 1.23** (timer changes) |
| 77 | JSON handling | Watch embedded `time.Time` overriding marshaling; monotonic clock in comparisons; `map[string]any` unmarshals numbers as `float64` |
| 78 | Common SQL mistakes | `sql.Open` doesn't connect; configure pooling; use prepared statements; handle nulls; check `rows.Err()` |
| 79 | Not closing transient resources | Close `io.Closer` types (`HTTP body`, `sql.Rows`, `os.File`) |
| 80 | Missing return after HTTP error | `http.Error` doesn't stop handler; add `return` |
| 81 | Default HTTP client/server | Defaults lack production timeouts; configure explicitly |
