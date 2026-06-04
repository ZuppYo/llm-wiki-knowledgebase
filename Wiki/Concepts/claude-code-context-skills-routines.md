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

# Claude Code Context, Skills, and Routines

Operational patterns from [Claude Code Paypers Production](../Topics/claude-code-paypers-production.md).

## Skills

- Author with **skill-creator**; trim output—target ~**1,500 tokens** per skill (not too short/long).
- Repo-hosted skills + cheat sheet so dev and non-dev roles share the same commands (e.g. `/export-line-broadcast` with **schema hints** embedded for SQL).
- Personal vs team skills: planning/bug-fix automation vs org-wide MCP helpers.

## Context cost

- Baseline: `/compact` (assumed known).
- **[Caveman prompting](https://github.com/JuliusBrussee/caveman):** ultra-short utterances to shrink context while staying readable.
- **[RTK](https://github.com/rtk-ai/rtk):** claimed token reduction on verbose tool output (e.g. tests, infra/git commands, server logs)—speaker validates more for ops than app dev; verify with RTK’s own stats if skeptical.
- **Codebase graph tool** (unnamed in talk): invoke via skill/prompt instead of full-file scans when checking if a symbol exists—install deliberately; don’t stack unvetted plugins blindly.

## CLAUDE.md and agents

- ~200-line root `CLAUDE.md` mostly **links** to per-domain agent briefs (frontend, API, etc.) so context loads on demand.
- Prefer adding rules under **`.claude/rules`** (built-in discovery) over growing `CLAUDE.md` for every new case.

## Scheduled automation (routines vs loop)

- **Routines** (not `loop`) for hourly cloud **bug fixer**: pick Linear cards tagged `bug` that need no human choice, no DB schema changes; local routines exist for other jobs.
- Other bots (examples): validate suspected bugs from product; daily **Sentry** digest with auto-PR when confident; **Stripe churn** report with customer links/phone for sales follow-up.

## Learning the harness

- Study Claude Code **anatomy** (skills, routines, connectors, cowork) and match tool to problem—avoid bolting every new hype tool into all processes.
- **[cc-changelog / cc-prompt](https://github.com/mackgreg/claude-code)** (reverse-engineered internals): align prompts/skills with actual built-in tools (e.g. cron) for faster, correct tool use.
