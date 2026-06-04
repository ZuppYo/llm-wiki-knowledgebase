---
tags:
  - concept
topics:
  - agent-harness-101
  - deep-agent-101
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[Agent Harness]]"
source_count: 1
aliases: []
---

# Agent Harness vs MCP and Skills

| | **MCP** | **Skills** | **Harness** |
|--|---------|------------|-------------|
| **What** | Wire protocol / tool transport | Task-specific instructions (playbook) | Full runtime around the model |
| **Loop** | Fire tool → done | May or may not apply each turn | Owns agent loop, state, retries |
| **Security** | Not built-in | Guidance only | Permissions, sandbox, approvals |
| **Determinism** | Depends on caller | Output can vary | Tool implementations run **deterministically** (read file always reads) |

**MCP through harness (per source):** MCP alone is “plug and protocol”; harness validates results, blocks unsafe paths, and decides whether to continue the agent loop.

**Skills through harness:** skills steer *when* and *how* to approach a task; harness still enforces tool behavior and workspace rules.

See also [Deep Agent Harness Capabilities](deep-agent-harness-capabilities.md) and [Deep Agent 101](../Topics/deep-agent-101.md) for a framework that bundles many harness features.
