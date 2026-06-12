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
  - Win Translator config
  - Win Translator DPAPI
---

# Win Translator Config and Security

Compiled from [Win Translator 101](../Topics/win-translator-101.md).

## Config path

`%APPDATA%\WinTranslator\config.json`

## Example structure

```json
{
  "encrypted_api_key": "...",
  "gemini_model": "gemini-2.5-flash",
  "always_on_top": true,
  "window_x": 860,
  "window_y": 512,
  "window_width": 482,
  "window_height": 480,
  "last_field": "thai",
  "tone": "casual"
}
```

## Security rules

| Rule | Detail |
|------|--------|
| API key storage | Encrypted with **Windows DPAPI** |
| API key in code | Never logged or committed to git |
| Dev override | `GEMINI_API_KEY` env var (development only) |

## Model migration

On load, config normalizes Gemini model names:

- **`gemini-2.0-flash` → `gemini-2.5-flash`** automatically (retired model)
- Strips `models/` prefix if present
- Falls back for unknown model strings

See [dev, build, and runtime](win-translator-dev-build.md) for the retired-model error and tray-quit fix.
