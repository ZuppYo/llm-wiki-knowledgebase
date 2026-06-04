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

# Claude Code Planning and Implementation Workflow

Paypers feature/bug flow on [Claude Code Paypers Production](../Topics/claude-code-paypers-production.md) (Linear + custom skills).

## Intake and tickets

- Customer feature requests arrive via LINE support (not anonymous feedback forms) so the team can ask follow-ups and capture **why** before prioritizing.
- Bugs: humans write reproduction steps; tickets may include customer LINE identifiers so bots can query DB for real receipt/state context.
- Linear is the task board; some PRs are bot-authored with human review only.

## Plan skill (`write plan` pattern)

Custom skill (MCP-connected to Linear) when a card is clear enough:

1. Read and understand the Linear task, then draft a plan.
2. **Spawn two reviewer agents** that read the task + plan and report critical/important gaps; fixes are folded back before coding.
3. Emit plan as **interactive HTML** (not only Markdown): human-readable section (~90% of reviewer attention) with before/after diagrams side-by-side; separate machine-oriented implementation section behind it.

Prompt habit cited: *always create diagram* for current vs proposed state so visual drift is obvious.

## Implementation

- Follow the implementation section of the plan.
- Agent **parallelizes** non-overlapping file edits where possible; a parent reviewer aggregates, runs tests, then runs **reviewer + `/simplify`** in parallel (built-in simplify for cleanup).
- Terminal UX: [Superset](https://superset.sh/) (free, main-repo sessions; Conductor-like but not worktree-only) to see many agent sessions/PR checks at once.

## Plan refinement

- Refine plans by **prompting Claude**, not hand-editing generated HTML files (per Q&A).
