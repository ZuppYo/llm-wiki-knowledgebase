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

# Agent Harness Product Patterns (Codex & Claude Code)

Case studies from public write-ups (per source)—illustrate how vendors structure harness loops.

## OpenAI Codex (approximate)

- Client → JSON plan of tool steps → **message processor** routes work (main agent vs sub-agent threads).
- **Thread:** long-lived user↔agent session with history/resume.
- **Turn:** one user command until agent result.
- **Items:** harness-defined steps (e.g. start, streaming, complete)—read file → analyze → diff/apply change → run tests on follow-up turn.
- Same harness backs desktop, TUI, and web runtimes.

## Claude Code (approximate)

- Repeating macro-loop: **get context** (read/search codebase) → **take action** (edit, bash) → **verify** (tests, check output) until done.
- Built-in **operations** are deterministic: file CRUD, grep, bash, tests, LSP intelligence; web search added later as harness tools.
- **Workspace sandbox:** default inside project root; crossing boundaries requires user approval.
- Session features: resume, fork from earlier session, rewind before bad edits; auto-compact and sub-agents for heavy context.

**Takeaway:** both products expose the same model family but encode different philosophies (JSON item pipeline vs context/action/verify loop) and permission models.
