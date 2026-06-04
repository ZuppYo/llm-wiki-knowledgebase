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

# Claude Code Production Mindset and Tooling

Judgment calls from [Claude Code Paypers Production](../Topics/claude-code-paypers-production.md)—what AI is for vs not for in a shipped product.

## Product vs engineering AI

- AI helps on **logical** sizing questions (market/pain estimates); **feature fit and roadmap** still need human product sense and customer discovery.
- Simple web Q&A to Claude is misleading (wrong > right on the open internet).

## Vibe coding vs production

- Vibe coding is strong for **fast idea validation** (including non-dev prototypes with full UI motion).
- **Production** delay is rarely “hard to code”—it is not breaking thousands of existing users; vibe-coded paths add regressions easily.

## Role of engineers

- Speaker barely hand-codes; **critical thinking** (verify AI output, find loopholes, decide build vs skip) and **problem-finding grit** matter more than typing.
- Card-only implementers are at risk; human touch remains for *what* the app should be and *whom* it serves.

## Adjacent review tools

- **Devin PR review:** very thorough vs Claude-only review; costly (~$3/PR cited)—worth trial when budget allows.
- **CodeRabbit:** seen on OSS (e.g. Bun)—bot review dialog with implementer until aligned; maintainer still owns merge trust.

## Editor integration

- Claude Code in **VS Code** can surface **LSP diagnostics** (red squiggles) while editing—reduces need for separate “code graph” cold-start review in that setup (speaker defers on custom LSP graph projects).
