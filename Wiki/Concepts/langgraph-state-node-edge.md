---
tags:
  - concept
topics:
  - langgraph-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - Raw/Sources/LangGraph 101
source_count: 1
aliases: []
---

# LangGraph State, Node, and Edge

Core graph model (per source):

- **State** — shared data passed through the run (conversation + workflow fields).
- **Node** — a step/function (e.g. call an LLM, run logic); nodes read/update state.
- **Edge** — connections that define **order** and branching between nodes.

Design feels like a **flowchart**: start → steps → end, with visible control flow in code. LangSmith Studio can visualize and debug the graph locally.

**Durable execution:** graph runs can **resume** from saved state after errors instead of restarting from scratch.
