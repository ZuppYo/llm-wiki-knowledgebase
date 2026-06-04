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

# Agent Harness Definition

An **agent harness** is everything besides the raw LLM that makes agent behavior **systematic, safe, and repeatable** (per source).

**Two parts of “agent” today:**

| Part | Role |
|------|------|
| **Model** | Probabilistic “engine” / brain—produces text and tool-call intents |
| **Harness** | Infrastructure + **rules** for how tools run: staging, feedback, security, loops, permissions |

**Harness = infrastructure + tool governance:** prepared tool surface (sandbox, file ops, AGENTS.md, skills the product already knows) plus policies for when/how to use tools, context limits, retries, and human gates.

**Metaphor (per source):** model = engine; harness = chassis, brakes, and steering—without harness, the engine cannot act in the world.

**Why it matters:** a strong harness can make the **same model** perform better than a weaker harness; agent quality is not only benchmark scores.
