# Identification experiment — findings v2, on the v4 world, 2026-09-20

**Type:** document (findings)
**Script:** `2026-09-20-identification-experiment-v2.py` (identical to v1 except that the harness path is an argument), run against `2026-09-20-loop-simulation-harness-v4.py`
**Run:** 2026-09-20, five seeds (11–15), harness defaults
**Attribution:** llm-proposed

The same five readings as the first run, on the world with mobile and broadband arrival dates measured from the WDI spine (see `2026-09-20-wave-calibration-from-spine.md`). Five of seven waves are still placeholders, so the *placeholder* qualifier is weakened, not removed.

## First: the harness's own sixteen design tests still pass on v4

| test | v3 | v4 |
|---|---|---|
| index over thirty years | 100 → 16.5 | 100 → 19.4 |
| companion index | 41.3 | 47.3 |
| CALL's fundamental peak | week 365, ×2.05, then ×0.285 | **week 642**, ×2.10, then ×0.487 |
| calls vs defaults | 74% redemption | 75% |
| forced long liquidations / coverings | 80 / 2,278 | 47 / 2,275 |
| advances over +10%, longest | 8, 193 weeks | 10, 123 weeks |
| market correlation early → late | +0.24 → +0.82 | +0.21 → +0.78 |
| weekly sigma, annualised | 2.42%, 17.4% | 2.55%, 18.4% |
| \|return\| autocorrelation | 0.14 | 0.22 |
| largest five-week move | +31.7% at week 926 | +22.2% at week 918 |
| sideways weeks | 286 | 281 |
| measured to | week 1540 | week 1461 |

16/16 in both. The one number that moved by more than noise is the arrival peak of unplanned calls: measured telephony reaches the population later than the placeholder assumed, so the practice it creates peaks at week 642 (2008) instead of 365 (2003), and falls less far by 2026. Everything else stays inside the range the placeholder world produced. The design's shape did not depend on the two dates that were guessed.

## The five readings, v3 against v4

**1. Two-way variance shares of the residual**

| | common | market | practice | interaction |
|---|---|---|---|---|
| v3 early | 0.099 | 0.097 | 0.452 | 0.351 |
| v4 early | 0.093 | 0.101 | 0.468 | 0.337 |
| v3 late | 0.091 | 0.065 | 0.666 | 0.177 |
| v4 late | 0.100 | 0.077 | 0.631 | 0.191 |

Unchanged in shape. The handover still runs through the interaction block, and the two market contrasts are still small at both ends. The measured dates compress the early spread of the two measured waves, and the market block does not shrink for it — because in this world local events, not wave stagger, are what fill the market and interaction blocks.

**2. Recovered factor count (medians)**

| true | v3 early (33 / 11 / dm) | v4 early | v3 late | v4 late |
|---|---|---|---|---|
| 3 | 3 / 8 / 12 | 2 / 7 / 10 | 6 / 4 / 12 | 6 / 4 / 6 |
| 6 | 1 / 7 / 2 | 1 / 8 / 2 | 2 / 8 / 5 | 7 / 8 / 7 |
| 9 | 2 / 7 / 1 | 2 / 8 / 1 | 8 / 9 / 7 | 8 / 9 / 8 |
| 13 | 1 / 1 / 1 | 2 / 7 / 2 | 9 / 8 / 9 | 8 / 7 / 8 |

Early: still one or two directions on the full panel whatever the truth. Late: the full panel now recovers seven of six and eight of nine and thirteen — the saturation near eight or nine holds; **thirteen is again never recovered**. The market-demeaned panel over-counts less on v4 (six for three, not twelve), which suggests part of the v3 over-count was the placeholder stagger putting structure into the demeaned panel.

**3. Promotion gate, calibrated on the null**

| | null median | null 95th | true median | power |
|---|---|---|---|---|
| v3 early | 0.0223 | 0.0382 | 0.0713 | 0.89 |
| v4 early | 0.0218 | 0.0418 | 0.0684 | 0.93 |
| v3 late | 0.0155 | 0.0319 | 0.0641 | 0.98 |
| v4 late | 0.0166 | 0.0333 | 0.0819 | 0.96 |

Same conclusion, same magnitudes: a random direction removes about two percent, the threshold must be calibrated per window, and the gate then has power above 0.9 at both ends.

**4. Leave-one-market-out R²**

| k | v3 early | v4 early | v3 late | v4 late |
|---|---|---|---|---|
| 2 | 0.088 | 0.108 | 0.245 | 0.207 |
| 5 | 0.180 | 0.200 | 0.447 | 0.413 |
| 9 | 0.228 | 0.254 | 0.563 | 0.520 |

Slightly more transportable early, slightly less late. Within seed noise.

**5. Order sensitivity of the schedule line**

| | rms shift / rms | schedule-first bp/wk | factors-first bp/wk |
|---|---|---|---|
| v3 early | 1.450 | −3.67 | −6.94 |
| v4 early | **1.847** | −2.56 | −6.08 |
| v3 late | 0.567 | −10.07 | −11.17 |
| v4 late | 0.567 | −10.95 | −11.92 |

The early sensitivity **rose**. With measured dates the two measured waves arrive later and closer together across markets, so in the early window the declared schedule carries less drift on its own (−2.6 bp/week) and more of what the schedule line ends up claiming depends on whether the factor lines were taken out first. The late number is identical to three decimals. This strengthens the point made for the deferred order decision: in the early history the split is a convention, and the more the waves arrive together, the more it is.

## What this does not establish

Everything the first run did not — no factor names, one estimator, one gate, positioning and reflexive lines not stripped — plus: five of seven waves are still placeholders, and the two that are measured were measured through a logistic fit with one width per wave. The v3 harness and the v1 findings are unchanged and remain the record of the placeholder run.
