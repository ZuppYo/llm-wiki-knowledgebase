---
tags:
  - "concept"
topics:
  - "langchain-101"
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "Raw/Sources/LangChain 101.md"
source_count: 1
aliases: []
---

# LangChain Framework

**LangChain** is an open-source framework for agent-style apps: it connects LLMs to your application and external tools. It supports Python and TypeScript; Python is the most common choice in AI/data workflows.

**Why it exists (per source):** early LLM apps needed reliable links to external data and tools; LangChain became a standard way to combine models, retrieval, and tool use before composing richer workflows.

**Ecosystem (per source):** **LangGraph** for workflow control (conditions, branching); **LangSmith** for tracing/debugging agent reliability. v1 redesigns APIs toward agent patterns that align with LangGraph.

**Model portability:** one LangChain-style interface can target multiple providers (e.g. Gemini, OpenAI) when a provider integration exists.
