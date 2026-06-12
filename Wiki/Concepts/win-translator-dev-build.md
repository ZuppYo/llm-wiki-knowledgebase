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
  - Win Translator build
---

# Win Translator Dev, Build, and Runtime

Compiled from [Win Translator 101](../Topics/win-translator-101.md).

## Development

```powershell
cd app
$env:Path = "$env:USERPROFILE\go\bin;$env:Path"
$env:GEMINI_API_KEY = "your-key-here"
wails dev
```

## Build portable exe

```powershell
cd app
wails build
# Output: app/build/bin/win-translator.exe
```

## Runtime usage

1. Run exe — app stays in system tray.
2. Press **Ctrl+Shift+T** — show/hide translator.
3. Tray → **Settings** — set API key and Gemini model.
4. Type or paste Thai/English — other field translates automatically.
5. Select tone: กันเอง / สุภาพ / ทางการ.

## After updating the app

1. Tray → **Quit** (required — closing window only minimizes).
2. Launch new `win-translator.exe`.

Only one instance runs; launching again focuses the existing window.

## Lessons learned

| Problem | Cause | Fix |
|---------|-------|-----|
| `gemini-2.0-flash is no longer available` | Google retired the model | Default `gemini-2.5-flash` + Settings model picker |
| Error persists after code fix | Old process still running in tray | Tray → **Quit** all instances before new exe |
| Code update not applied | Close (X) = minimize to tray, not quit | Must use tray **Quit** to reload binary |

See [config and security](win-translator-config-security.md) for model migration on config load.
