---
tags:
  - project
topics:
  - win-translator-101
status: seed
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[Win Translator]]"
source_count: 1
aliases:
  - win-translator repo
---

# Win Translator

Personal Windows helper for **Thai ↔ English** translation while working. See [Win Translator 101](../Topics/win-translator-101.md).

## Status

| Field | Value |
|-------|-------|
| Version | **v1 shipped** (2026-06-12) |
| Repo | `win-translator` |
| Platform | Windows (WebView2) |
| Distribution | Portable `win-translator.exe` via `wails build` |

## v1 scope

**In scope:** global hotkey launcher (`Ctrl+Shift+T`), dual Thai/English text areas, tone selector (กันเอง / สุภาพ / ทางการ), copy/paste helpers, system tray, Gemini API backend, standalone exe.

**Out of scope:** mobile, web-only, non-Gemini backends.

## Deferred (future)

- Customizable global hotkey
- Dynamic Gemini model list from API
- Start with Windows (autostart)
- Translation history / favorites

## Agent workflow (IOM tasks)

Repo uses **IOM todo skills** for agent-driven development: `iom-todo-task`, `iom-todo-task-archive`, `iom-todo-handoff`.

Archived 2026-06-12: bootstrap (000), design interview (001), implementation (002), Gemini model picker + single-instance (003).

**Agent reload chain:** `AGENTS.md` → `task/session.handoff-close.md` → `task/index.md`

## Key repo paths

| Item | Path |
|------|------|
| Application source | `app/` |
| Executable | `app/build/bin/win-translator.exe` |
| Dev/build docs | `app/README.md` |
| Agent instructions | `AGENTS.md` |
| Session handoff | `task/session.handoff-close.md` |
| Archived tasks | `task/archive/2026-06-12/` |
