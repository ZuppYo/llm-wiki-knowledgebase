---
tags:
  - concept
topics:
  - philips-aut8990-dual-mode-water-filter-101
status: seed
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[Manual/Philips Water AUT8990 - ProblemPPM999]]"
source_count: 1
aliases:
  - AUT8990 TDS 999
  - Philips TDS display stuck at 999
---

# Philips AUT8990 TDS 999 Display Troubleshooting

Compiled from [Philips AUT8990 Dual-Mode Water Filter 101](../Topics/philips-aut8990-dual-mode-water-filter-101.md). Based on Philips AUT8940/AUT8960/AUT8990 user-manual family and field diagnosis from a first-use session.

## What 999 on the faucet means

The smart-faucet TDS readout measures conductivity and shows **ppm**. **999** is often the **display ceiling**, not an exact reading — it means TDS is very high, the RO stage is not performing yet, or the **sensor/display is faulted**.

Normal RO product water is typically **~10–50 ppm** (often under 100 ppm). RO working properly should reject most dissolved solids — filtered TDS is often **~5–10% of tap water** (e.g. tap 200 ppm → RO ~10–20 ppm).

## First-use flush (before blaming the sensor)

Power-on auto-flush is only **~18 seconds** — insufficient alone. Manual first-use sequence per Philips manual:

1. **MF** (green line): run **15 minutes**
2. Faucet **center/off**: wait **10 seconds**
3. **RO** (blue line): run **15 minutes**

Opening **RO only for ~20 minutes** skips MF rinse and may leave high TDS from carbon fines / membrane hydration. See [installation and first use](philips-aut8990-install-first-use.md).

## Common causes while display still shows 999

| Check | Why it matters |
|-------|----------------|
| Faucet on **RO**, not **MF** | MF bypasses RO — TDS stays high |
| **Blue = RO**, **green = MF** at unit and faucet | Swapped lines → RO tap delivers unfiltered water |
| **Gray waste** line flowing when RO runs | No reject flow → membrane not working |
| Inlet pressure **0.1–0.4 MPa** | Below 0.1 MPa may need a booster pump |
| Filter cartridges fully seated, correct order | Bypass or blocked flow raises TDS |
| Quick connectors pushed fully + clips on | Loose collets leak or bypass |

After **full manual flush** and verified plumbing, if **999 persists**, continue diagnosis below.

## Split diagnosis: sensor fault vs RO failure

Use a **handheld TDS meter** on RO water in a cup (best). Without one, compare **taste** to tap water.

| Observation | Likely cause |
|-------------|--------------|
| Handheld **low**, faucet **999** | **Faucet TDS sensor, faucet cable, or display module** |
| Handheld **high**, faucet **999** | **RO not filtering** (membrane, pressure, internal bypass, filters) |
| **999 frozen** (never changes) + waste flowing + taste unlike tap | **Sensor/display fault** while RO likely OK |
| **999 frozen** + taste like tap | RO failure or wrong water path |

### Confirmed pattern: stuck 999 + waste flows + taste differs from tap

When all three hold after full flush and correct tubing:

- **RO membrane process** is probably active (reject water present; water is altered).
- **Faucet TDS readout** is probably **not trustworthy** — treat as hardware/display issue.

Philips support guidance for display mismatch: check wiring; contact service for keypad, main board, or smart-faucet module replacement.

## Self-checks before warranty service

1. Reseat **smart-faucet cable** to the main unit under the sink.
2. **Power cycle:** unplug **1 minute**, replug; run RO 2–3 minutes — if digits never change, sensor fault is likely.
3. Optional handheld TDS test to confirm water quality vs display.
4. Contact **Philips Consumer Care** (2-year warranty on unit) with: full flush done, tubing verified, waste flowing, taste OK, display stuck at 999.

## Filter reset is unrelated

**Do not reset filter life on first use** — reset only **after replacing** cartridges, then repeat the first-use flush. Reset does not fix a stuck TDS display.

## Related

- [Installation and first use](philips-aut8990-install-first-use.md) — flush and filter-reset rules
- [Dual filter paths](philips-aut8990-dual-filter-paths.md) — MF vs RO routing
- [FreshPro Anti-TDS Creep](philips-freshpro-anti-tds-creep.md) — not on AUT8990; manual flush after idle instead
