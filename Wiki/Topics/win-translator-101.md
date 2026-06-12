---
tags:
  - topic
topics: []
status: seed
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[Win Translator]]"
source_count: 1
aliases:
  - Win Translator
  - Thai English desktop translator
---

# Win Translator 101

**Win Translator** is a personal Windows desktop app for fast **Thai ↔ English** translation via Google Gemini. v1 shipped 2026-06-12; repo `win-translator`.

**Compiled notes:**

- [Project status and scope](../Projects/win-translator.md) — v1 goals, out-of-scope items, IOM task history
- [Stack and architecture](../Concepts/win-translator-stack-architecture.md) — Wails 2, Go, Gemini client, folder layout, translation flow
- [UX and behavior](../Concepts/win-translator-ux-behavior.md) — hotkey, tray, debounce, tone, prompts, copy/paste
- [Config and security](../Concepts/win-translator-config-security.md) — `%APPDATA%` config, DPAPI, model migration
- [Dev, build, and runtime](../Concepts/win-translator-dev-build.md) — commands, tray quit rule, lessons learned
