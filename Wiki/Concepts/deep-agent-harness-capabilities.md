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

# Deep Agent Harness Capabilities

Built-in harness tools (per source overview) can be triggered via **commands** or **prompt** keywords—e.g. mention `todo`, `read file`, `edit file` in the system prompt so the agent invokes middleware without you importing each tool.

| Capability | Notes from source |
|------------|-------------------|
| **Planning / todo** | Plan steps before executing tools; visible step-by-step in LangSmith chat view |
| **Filesystem** | List/read/write/edit; default writes stay in **sandbox** unless a **filesystem backend** maps host paths (`virtual_mode` restricts paths) |
| **Shell** | Run commands in sandbox backend |
| **Sub-agents** | `create_deep_agent` can spawn sub-agents for isolated subtasks |
| **Memory** | LangGraph-style memory store; can persist via files (e.g. `AGENTS.md`) and update memory on disk |
| **Skills** | Load `SKILL.md` folders; agent reads skill when trigger matches |
| **MCP** | Wrap MCP clients (e.g. `MultiServerMCPClient`) and pass as tools—same config idea as MCP elsewhere |
| **Providers** | Multi-vendor models via existing LangChain integrations (OpenRouter, Google GenAI, etc.) |
| **Human-in-the-loop** | Similar patterns to LangGraph interrupt/approve flows |
| **Permissions** | Gate read/write paths; optional human approval before continuing |

**Agent harness goal (per source):** provide a **tool base** plus a way to **define step order** via system prompts—custom tools still plug in like LangChain `tools=[...]`.
