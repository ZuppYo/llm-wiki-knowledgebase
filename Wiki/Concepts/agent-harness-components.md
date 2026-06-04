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

# Agent Harness Components

Common harness building blocks (~9 themes in source articles—not a rigid standard, but recurring pain points).

| Area | Examples |
|------|----------|
| **Loop control** | Max retries, error handling, when to exit |
| **Context management** | Long chats, RAM limits, compaction/summary (e.g. Claude context compression) |
| **Tool registry** | Read/write files, bash, built-in ops; how skills attach |
| **Skills vs general tools** | Skills = playbooks; base tools stay general-purpose |
| **Sub-agents** | Spawn/isolate work; grouping policies |
| **Session / persistence** | Thread IDs, resume, fork sessions |
| **Prompt + caching** | System prompt lifecycle, hooks |
| **Pre/post hooks** | Inspect before run; validate after run |
| **Extensibility** | Plugins, custom tools atop vendor harness (e.g. Codex hooks) |
| **Permission & safety** | Ask vs yolo modes, workspace boundaries, approval gates |

**Three pillars (source summary):**

1. **Condition logic** — loops, hooks, when to continue or stop.
2. **Scaling** — sub-agents, memory strategies, context tactics.
3. **Persistence & safety** — sessions, permissions, cycle prevention.

Missing any pillar tends to produce agents that loop badly, leak context, or bypass security.
