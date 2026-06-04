---
tags:
  - "concept"
topics:
  - "langchain-101"
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "Raw/Sources/LangChain 101.md"
source_count: 1
aliases: []
---

# LangChain Four Core Components (v1)

The tutorial groups LangChain v1 into four building blocks:

| Component | Role |
|-----------|------|
| **Model** | Init chat model, `model.invoke(prompt)`; API keys via env (e.g. `GOOGLE_API_KEY`) |
| **Message** | `system`, `human`, `AI`, `tool` roles; multimodal content (text + base64 image); optional chat prompt templates |
| **Agent + tools** | `create_agent` + `@tool` functions; model decides tool calls, observes results, returns final answer; **system prompt** often required so the model uses tool output in the final reply |
| **Structured output** | `with_structured_output` or agent `response_format` — Pydantic/dataclass/JSON schema for downstream apps |

**Agent loop (conceptual):** user input → model may call tools → tool results → model produces output (optionally structured).
