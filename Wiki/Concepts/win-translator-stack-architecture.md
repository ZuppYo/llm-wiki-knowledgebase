---
tags:
  - concept
topics:
  - win-translator-101
status: seed
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[Win Translator]]"
source_count: 1
aliases:
  - Win Translator architecture
---

# Win Translator Stack and Architecture

Compiled from [Win Translator 101](../Topics/win-translator-101.md).

## Tech stack

| Layer | Choice | Rationale |
|-------|--------|-----------|
| Framework | **Wails 2** | Go backend + web UI; small exe; WebView2 on Windows |
| Backend | **Go 1.23+** | Hotkey, tray, config, Gemini client |
| Frontend | **Vanilla JS + Vite** | Simple UI without heavy framework |
| Translation | **Gemini REST API** | `generateContent` over HTTP |
| Default model | **`gemini-2.5-flash`** | Replaces retired `gemini-2.0-flash` |
| Config | `%APPDATA%\WinTranslator\config.json` | API key encrypted with **Windows DPAPI** |
| Tray | `github.com/getlantern/systray` | Open / Settings / Quit |
| Hotkey | `golang.design/x/hotkey` | `Ctrl+Shift+T` |

**Prerequisites:** Go 1.23+, Node.js 18+, Wails CLI, WebView2 Runtime (built into Windows 11).

**Distribution:** dev via `wails dev` (optional `GEMINI_API_KEY` env); release via `wails build` → `app/build/bin/win-translator.exe`.

## Folder layout

```
app/
├── main.go              # Wails entry, single-instance lock
├── app.go               # Bindings: Translate, Settings, window control
├── tray.go              # System tray menu
├── hotkey_windows.go    # Ctrl+Shift+T
├── internal/
│   ├── config/          # Load/save config, model migration
│   ├── dpapi/           # Encrypt/decrypt API key (Windows)
│   └── gemini/          # Gemini HTTP client + prompts
└── frontend/
    ├── index.html       # Main + Settings views
    └── src/main.js      # Debounce, paste/copy, tone UI
```

## Translation flow

1. User types or pastes in focused field (source).
2. Frontend debounces **500 ms** (paste = immediate).
3. Go builds system + user prompt with tone (TH→EN or EN→TH).
4. Gemini `generateContent` returns translation.
5. Result written to opposite field (target).
6. In-flight request **cancelled** if input changes before response.

See [UX and behavior](win-translator-ux-behavior.md) for window/tray rules and [config and security](win-translator-config-security.md) for stored settings.
