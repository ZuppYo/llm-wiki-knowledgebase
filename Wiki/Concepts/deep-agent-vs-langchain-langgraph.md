---
tags:
  - concept
topics:
  - deep-agent-101
  - langchain-101
  - langgraph-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[Deep Agent]]"
source_count: 1
aliases: []
---

# Deep Agent vs LangChain and LangGraph

**LangChain** supplies base components (models, tools, prompts). **LangGraph** supplies low-level **runtime** control (state, checkpoints, HITL). **Deep Agent** sits on top and **uses both**, adding harness-level features you would otherwise implement yourself.

**Add-ons Deep Agent ships with (per source):**

- **Planning / task breakdown** (e.g. todo lists) before execution
- **Context via virtual filesystem** (read/write/edit; default sandbox or mapped workspace)
- **Sub-agents** spawned when the main agent decides a subtask needs isolation
- **Long-term memory** (LangGraph memory store patterns still apply)
- **Skills** and **AGENTS.md**-style project memory
- **MCP** tool integration
- **Shell execution** in sandbox backends; file permissions and HITL-style gates

**When to use Deep Agent (per source):** you want those harness behaviors **built in**—especially planning, filesystem workflows, and “one `create_deep_agent` + system prompt” agents. Plain LangChain agents can cover simple tool loops; many transcript examples could be done with LangChain alone, but you would re-implement todo planning, file middleware, etc.

**When LangGraph alone may win (per source):** highly **deterministic** pipelines (e.g. strict RAG: retrieve first, then answer) where you want explicit graph ordering rather than the agent choosing tools step-by-step.
