---
tags:
  - topic
topics: []
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[Common Go Mistakes - 100 Go Mistakes and How to Avoid Them]]"
source_count: 1
aliases:
  - 100 Go Mistakes
  - Common Go Mistakes
---

# Go Common Mistakes 101

Community-maintained summary of [100 Go Mistakes and How to Avoid Them](https://100go.co/) (Teiva Harsanyi / teivah). Each entry is a numbered mistake with a TL;DR and optional source code on GitHub. The online beta version is enriched beyond the book; some entries are marked obsolete in newer Go releases.

**Scope:** 100 numbered mistakes across eleven technical sections (#1–#100), plus community contributions. Reference: https://100go.co/

**Section map:**

| Section | Mistakes | Wiki concept |
|---------|----------|--------------|
| Code and Project Organization | #1–16 | [Code and project organization](../Concepts/go-mistakes-code-organization.md) |
| Data Types | #17–29 | [Data types](../Concepts/go-mistakes-data-types.md) |
| Control Structures | #30–35 | [Control structures](../Concepts/go-mistakes-control-structures.md) |
| Strings | #36–41 | [Strings](../Concepts/go-mistakes-strings.md) |
| Functions and Methods | #42–47 | [Functions and methods](../Concepts/go-mistakes-functions-methods.md) |
| Error Management | #48–54 | [Error management](../Concepts/go-mistakes-error-management.md) |
| Concurrency: Foundations | #55–60 | [Concurrency foundations](../Concepts/go-mistakes-concurrency-foundations.md) |
| Concurrency: Practice | #61–74 | [Concurrency practice](../Concepts/go-mistakes-concurrency-practice.md) |
| Standard Library | #75–81 | [Standard library](../Concepts/go-mistakes-standard-library.md) |
| Testing | #82–90 | [Testing](../Concepts/go-mistakes-testing.md) |
| Optimizations | #91–100 | [Optimizations](../Concepts/go-mistakes-optimizations.md) |

**Cross-cutting themes:** prefer idiomatic Go over patterns from other languages; discover abstractions at the consumer; early returns and flat control flow; explicit error handling (log *or* return, not both); concurrency structure vs parallelism; benchmark before assuming concurrency helps.
