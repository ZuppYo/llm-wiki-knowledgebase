---
tags:
  - concept
topics:
  - claude-code-paypers-production
status: seed
created: 2026-06-04
updated: 2026-06-04
sources:
  - "[[ใช้ Claude Code ยังไง ให้ปังแบบ Paypers by Wasin Watthanasrisong]]"
source_count: 1
aliases: []
---

# Claude Code Team MCP and Data Access

How Paypers spreads Claude Code beyond a single CTO on [Claude Code Paypers Production](../Topics/claude-code-paypers-production.md).

## Repo as the skill hub

- Everyone clones the company GitHub repo and works there so **MCP configs and skills** are shared—not ad-hoc personal setups.
- Example MCP: **Google Cloud Logging** from the repo—e.g. “how many 403s in the last day?” or correlate a bug with logs without paging devs.

## Product and business users

- **Read-only MCP** to production database for the product team (conversion, daily metrics, etc.) so they query in Claude instead of interrupting engineering.
- Accuracy depends on **explicit schema/table vocabulary** in prompts and especially inside skills; vague “give me insights” prompts fail; skills encode how to ask (like delegating to a colleague).

## Example skill outcome

- `/export-line-broadcast`: skill documents schema → Claude builds optimized SQL → exports CSV segment for LINE broadcast targeting (e.g. users who joined today and have not converted).

## Hiring signal (small team ~7)

- With more code written by agents, prioritize engineers who **spot problems** and persist on fixes—not ticket executors only; bots/automation often come from pain points engineers hit daily (worktrees for parallel experiments).
