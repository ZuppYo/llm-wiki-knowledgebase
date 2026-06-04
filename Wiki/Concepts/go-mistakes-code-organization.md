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

# Go Mistakes: Code and Project Organization

Mistakes #1–16 from [Go Common Mistakes 101](../Topics/go-common-mistakes-101.md). Focus: readability, API design, package layout, and tooling.

| # | Mistake | TL;DR |
|---|---------|-------|
| 1 | Unintended variable shadowing | Shadowed inner variables compile but may assign to the wrong binding; stay cautious even with `err` reuse |
| 2 | Unnecessary nested code | Flatten with early returns; omit `else` after `return`; flip conditions so the happy path stays left-aligned |
| 3 | Misusing init functions | Limited error handling, harder tests, global state; prefer explicit init functions except static config |
| 4 | Overusing getters and setters | Not idiomatic in Go; use exported fields unless encapsulation adds real value |
| 5 | Interface pollution | Discover abstractions at need; don't create interfaces you only foresee needing |
| 6 | Interface on the producer side | Define interfaces on the consumer side; keep producer-side interfaces minimal if unavoidable |
| 7 | Returning interfaces | Return concrete types; accept interfaces as parameters |
| 8 | `any` says nothing | Reserve `any` for truly generic cases (e.g. marshaling); prefer typed APIs |
| 9 | Confused about generics | Use type parameters to remove boilerplate, not prematurely |
| 10 | Type embedding problems | Embedding promotes fields/methods; avoid cosmetic embedding or exposing hidden behavior |
| 11 | Not using functional options | `Option func(*options) error` pattern for configurable constructors |
| 12 | Project misorganization | Consistent layout (by context or layer); right-sized packages; export minimally; see [go.dev/doc/modules/layout](https://go.dev/doc/modules/layout) |
| 13 | Creating utility packages | Avoid `common`/`util`/`shared`; name packages for what they provide |
| 14 | Package name collisions | Unique names or import aliases when variable names clash with package names |
| 15 | Missing code documentation | Document every exported symbol and each package (`// Package …`) |
| 16 | Not using linters | Use `go vet`, specialized linters, formatters, and `golangci-lint` in CI or pre-commit |
