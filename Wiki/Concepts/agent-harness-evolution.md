---
tags:
  - concept
topics:
  - agent-harness-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[Agent Harness]]"
source_count: 1
aliases: []
---

# Agent Harness Evolution

How the industry moved from “model replies only” to explicit harness layers (per source timeline).

| Era | Pattern | Limitation |
|-----|---------|------------|
| Early chat | Model returns text; human executes | No tool control or durable agent state |
| Manual loop | Human pastes tool results back | No coded guardrails; fragile |
| Frameworks (~2023–24) | LangChain, LangGraph—developers wire steps | Heavy implement burden; rigid condition trees |
| AutoGPT-style | Loop until success | Weak security/context rules; runaway loops |
| Modern split | Model decides **which tool**; harness decides **if result is OK / when to stop** | ReAct-like think→act, but termination and safety in **code** |

**Modern division (per source):**

- **Model layer:** reasoning, tool choice (often via system prompt).
- **Harness layer:** deterministic checks—permissions, loop limits, context compaction, session persistence, pre/post hooks.

Harness is largely **code-level** control; system prompt alone cannot replace permission sandboxes or retry policies.
