---
tags:
  - concept
topics:
  - philips-aut8990-dual-mode-water-filter-101
  - philips-aut8940-ro-water-filter-101
status: seed
created: 2026-06-12
updated: 2026-06-12
sources:
  - "[[Manual/Philips Water AUT8990 - ProblemPPM999]]"
source_count: 1
aliases:
  - FreshPro
  - Anti-TDS Creep
---

# Philips FreshPro Anti-TDS Creep

**FreshPro™** (full name **FreshPro Anti-TDS Creep**) is Philips marketing for **automatic RO membrane flushing during standby** so the first glass after idle time stays low-TDS.

## TDS creep (the problem)

When an RO system sits **idle**, pressure on the membrane drops. Dissolved solids can **diffuse slowly** to the product side. The **first draw** after idle may show **temporarily higher TDS** until stale water is flushed out.

Typical user mitigation without FreshPro: run the RO faucet **several minutes** (or at least 30 s–5 min per manual) before drinking after long idle.

## What FreshPro does

The controller **flushes the RO path with purified water automatically**, including when the unit is not actively dispensing — reducing creep so **first and later glasses stay closer in quality**.

Philips positions this on newer/higher-tier under-sink models (e.g. **AUT9028DG**, **AUT7063R23**, **AUT6104** per product pages).

## AUT8990 vs FreshPro

The **AUT8990** user-manual family (**AUT8940/AUT8960/AUT8990**) does **not** document FreshPro by name. Available flush behavior on AUT8990:

| Mechanism | Behavior |
|-----------|----------|
| Power-on auto-flush | ~**18 s** |
| Panel flush button | Long-press **3 s** until cycle completes |
| After **2+ days** idle | Run **RO ≥ 5 minutes** before use (manual) |

So AUT8990 relies on **manual flush after idle**, not standby FreshPro auto-flush.

## Not the same as a stuck TDS display

FreshPro addresses **gradual TDS rise after idle**. A faucet stuck at **999** with unchanged digits is a separate issue — see [AUT8990 TDS 999 troubleshooting](philips-aut8990-tds-999-troubleshooting.md).

## Related

- [Philips AUT8940 installation and first use](philips-aut8940-install-first-use.md) — FreshPro toggle on AUT8940 panel (hold droplet **5 s**)
- [Philips AUT8990 installation and first use](philips-aut8990-install-first-use.md) — manual idle flush without FreshPro
