---
tags:
  - concept
topics:
  - agent-harness-101
  - langgraph-101
  - deep-agent-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[Agent Harness]]"
source_count: 1
aliases: []
---

# Agent Harness Implementation Levels

Ways to work with harnesses (per source), from least to most control:

| Level | Examples | What you customize |
|-------|----------|-------------------|
| **1 — Product harness** | Cursor, Codex, Claude Code, Gemini CLI | Mostly **prompts**, skills, AGENTS.md—cannot rewrite core tool implementations |
| **2 — Harness SDK** | Claude Agent SDK, [Deep Agent 101](../Topics/deep-agent-101.md) | Parameters + prompts on a pre-built harness |
| **3 — Graph / agent frameworks** | [LangGraph 101](../Topics/langgraph-101.md), LangChain agents | Define flows, tools, checkpoints in code |
| **4 — Raw API loop** | Vendor SDK + your `run_loop` | Full control: tool-use blocks, token limits, context strategy |

**Harness engineering:** designing and implementing these layers (loops, tools, permissions)—not only prompting.

**Source note:** stronger frontier models need less hand-holding in tool docs, but **code-level** harness (permissions, deterministic tools) remains the last line of defense against hallucinated actions.
