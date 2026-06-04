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

# Deep Agent create_deep_agent API

Primary entry point (per source): **`create_deep_agent`** (parallel to LangChain **`create_agent`**).

**Typical parameters:**

| Parameter | Role |
|-----------|------|
| `model` | LangChain chat model instance (provider-specific package) |
| `tools` | Custom `@tool` functions (same pattern as LangChain 101) |
| `backend` | How filesystem is exposed: default **in-sandbox** vs **`FilesystemBackend`** / **`make_backend`** / **`CompositeBackend`** mapping host paths (e.g. `/` workspace, `/reports` subdir) |
| `system_prompt` | Persona + **critical** step order (source stresses explicit “plan → execute tools → write file → reply” chains) |
| `memory` | Path or folder for AGENTS.md-style shared instructions |
| `skills` | Folder of skill definitions the agent can load on trigger |

**Runtime flow:** build agent → **`agent.invoke`** with user message → stream messages tagged as AI vs tool (debug pattern from LangChain 101).

**LangSmith Studio:** `langgraph.json` points `graphs` at `agent.py:agent`; `langgraph dev` exposes chat UI with harness middleware nodes (todo, filesystem, skill/memory middleware when those params are set).

**Examples in source:**

1. **Basic** — custom weather tool + `FilesystemBackend` writing `resources.md` on disk.
2. **AGENTS.md + skills** — `memory` + `skills` keys; composite backend for `/reports`; SQL optimizer skill writes reports when prompted.
3. **MCP** — Playwright MCP wrapped via `MultiServerMCPClient`, passed as tools.
4. **RAG** — Chroma ingest script + search tools; agent decides when to call retrieval (contrast with deterministic LangGraph RAG graphs).

Install (per demo): `deepagents` library plus provider packages (e.g. `langchain-google-genai`, OpenRouter); optional Tavily only if following upstream samples.
