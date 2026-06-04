---
tags:
  - concept
topics:
  - deep-agent-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[Deep Agent]]"
source_count: 1
aliases: []
---

# Deep Agent Framework

**Deep Agents** (LangChain ecosystem) are an **agent harness** framework: pre-built capabilities for building agents that plan, use tools, manage context, and spawn sub-agents—without implementing those layers from scratch on LangGraph.

**Stack (per source):**

| Layer | Role |
|-------|------|
| **Deep Agent** | Harness: planning, virtual FS, sub-agents, built-in middleware tools |
| **LangChain** | Components: chat models, templates, documents, custom tools |
| **LangGraph** | **Runtime**: state, checkpoints, human-in-the-loop, durable execution |

Same community/maintainers as LangChain and LangGraph. Comparable in purpose to other **agent harness** SDKs (source mentions Claude Agent SDK as a parallel idea).

**Look-and-feel (per source):** similar API surface to LangChain agents (`create_deep_agent` vs `create_agent`, then `invoke`); extra behavior comes from harness features you opt into via prompts, backends, and parameters—not a wholly different mental model.
