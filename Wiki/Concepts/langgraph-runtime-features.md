---
tags:
  - concept
topics:
  - langgraph-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[LangGraph 101]]"
source_count: 1
aliases: []
---

# LangGraph Runtime Features

Advanced capabilities covered in LangGraph 101 (per source):

| Feature | Purpose |
|---------|---------|
| **Persistence / checkpoint** | Save **thread** history; continue conversations across runs |
| **Human-in-the-loop** | Pause graph for **approve/reject** before continuing |
| **Long-term memory (Store)** | Remember facts **across threads** |
| **Time travel** | Inspect or **rewind** to past states and branch from there |
| **LangSmith Studio** | Visualize graph structure and debug agent runs locally |

Examples in the source wire nodes to **Gemini** (same API-key pattern as LangChain 101) and build on checkpoint + HITL patterns step by step.
