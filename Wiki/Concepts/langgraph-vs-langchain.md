---
tags:
  - concept
topics:
  - langgraph-101
  - langchain-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[LangGraph 101]]"
source_count: 1
aliases: []
---

# LangGraph vs LangChain

| | LangChain (v1 agent) | LangGraph |
|--|----------------------|-----------|
| **Best for** | One agent + tools, simpler flows | Multi-step **workflows**, branches, deterministic ordering |
| **Control** | Higher-level agent API | **Low-level** graph: you define flow in code (little hidden prompt magic) |
| **Workflow** | Linear/tool loops; limited condition design in-framework | **State + nodes + edges** like a flowchart |
| **Durability** | Memory concepts exist | **Durable execution**: resume/retry from checkpoints after failures |

**Rule of thumb (per source):** stay on LangChain if one agent is enough; adopt LangGraph when you need explicit conditions, multiple sources/steps, or ordered deterministic pipelines. LangGraph is the runtime LangChain agents can run on in the v1 ecosystem.
