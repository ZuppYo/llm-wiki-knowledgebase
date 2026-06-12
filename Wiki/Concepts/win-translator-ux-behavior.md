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
  - Win Translator UX
---

# Win Translator UX and Behavior

Compiled from [Win Translator 101](../Topics/win-translator-101.md).

## Window and hotkey

| Decision | Value |
|----------|-------|
| Hotkey | `Ctrl+Shift+T` — toggle show/hide |
| On show | Focus last-used field (Thai or English) |
| Tray menu | Open / Settings / Quit |
| Close (X) | Minimize to tray (does not quit) |
| Window position | Remember last position |
| Always on top | On by default; toggle in Settings |
| Single instance | Second launch focuses existing window |

## Translation UX

| Decision | Value |
|----------|-------|
| Trigger | Auto after 500 ms debounce + immediate on paste |
| Source/target | Focused field = source; other = target |
| Empty source | Clear target field |
| Tone change | Re-translate immediately |
| In-flight | Show loading; cancel superseded requests |
| Errors | Show below target field |

**Tone options:** casual (กันเอง) / polite (สุภาพ) / formal (ทางการ).

## Copy and paste

- Per-field **Paste** and **Copy** buttons (Thai and English).
- Paste → insert → focus as source → translate immediately.
- Copy → clipboard + toast “คัดลอกแล้ว”.
- Standard `Ctrl+C` / `Ctrl+V` inside text areas.

## Gemini prompts

- **System prompt:** fixed translator role; output translation only.
- **User prompt:** separate templates for **TH→EN** and **EN→TH**.
- **Tone** embedded in user prompt per selection above.
- **Rules:** natural phrasing; preserve proper nouns, URLs, numbers.

## Settings panel

| Field | Detail |
|-------|--------|
| API key | Masked input; stored encrypted (DPAPI) |
| Gemini model | Dropdown — see models below |
| Always on top | Checkbox |
| Test connection | Calls Gemini with current settings |
| Delete key | Clears stored API key |

**Selectable models:** `gemini-2.5-flash` (default), `gemini-2.5-flash-lite`, `gemini-2.5-pro`.

**Dev fallback:** environment variable `GEMINI_API_KEY`.
