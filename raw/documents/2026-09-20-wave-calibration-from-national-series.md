# Wave calibration from national series — smartphones and the social web, 2026-09-20

**Type:** document (calibration record)
**Input:** the files in `2026-09-20-national-series-retrieval.md`
**Output:** the `smartphone` and `socialweb` rows of `WAVES` in `2026-09-20-loop-simulation-harness-v5.py`
**Attribution:** llm-proposed — the rule extends `2026-09-20-wave-calibration-from-spine.md`; no value here is a user decision

## The rule, extended

Steps 1–5 of the spine rule apply unchanged: year-end (or survey-date) placement in weeks from 1996-01, a three-parameter logistic by least squares, the midpoint as the arrival week, the median fitted scale of the measured markets as the wave's width. Two steps are added because these are share-of-population surveys rather than subscription counts:

6. **A share series' ceiling is at most 100.** If the free fit's ceiling exceeds 100, refit with the ceiling fixed at 100.
7. **A series dates a wave only if it contains the midpoint** — its first observation is below half its ceiling. Otherwise the fitted midpoint is a *bound* on the arrival (at or before the first observation), recorded here and not wired; the market keeps its placeholder.

Where a wave is measured in fewer than three markets, the width is the median of the markets measured, and the unmeasured market keeps its placeholder date. That mix is a known distortion, discussed below.

## The fits

| wave | country | series | window | ceiling `S` | midpoint (week) | midpoint (year) | scale `w` | RMSE | contains midpoint? |
|---|---|---|---|---|---|---|---|---|---|
| smartphone | JPN | MIC household ownership | 2010–2023 | 85.4 | 887 | 2012.0 | 84 | 5.16 | yes (first 9.7) |
| smartphone | USA | Pew adult ownership | 2011–2025 | 91.4 | 868 | 2011.6 | 152 | 2.12 | yes (first 35) |
| smartphone | KOR | — | — | — | — | — | — | — | not obtained |
| social web | USA | Pew, % of internet users | 2005–2015 | 75.1 | 660 | 2007.6 | 78 | 2.53 | yes (first 8) |
| social web | JPN | OECD `D1B_I`, free ceiling | 2012–2024 | 127.4 | 1208 | 2018.1 | 396 | 2.16 | ceiling > 100 → refit |
| social web | JPN | OECD `D1B_I`, ceiling fixed 100 | 2012–2024 | 100 | **1032** | 2014.8 | 285 | 2.53 | yes (first 39.8 < 50) |
| social web | KOR | OECD `D1B_I` | 2005–2024 | 71.9 | 530 | 2005.2 | 311 | 3.18 | **no** (first 37.9 > 35.9) → bound only |

## What was wired

| wave | v4 (KR / JP / US, width) | v5 (KR / JP / US, width) | basis |
|---|---|---|---|
| smartphone | 690 / 700 / 675, spread | **690 / 887 / 868, 118** | KR placeholder; JP, US measured |
| social web | 195 / 450 / 430, spread | **195 / 1032 / 660, 182** | KR placeholder (bound ≤ 530); JP, US measured |
| mobile, broadband | as v4 | as v4 | measured, WDI |
| dial-up, messaging, AI | placeholders | placeholders | no measured series |

## What the measurement moved

Both waves move **later** in the two measured markets, as mobile and broadband did: smartphones by two and a half to three and a half years (Japan 2009.4 → 2012.0, US 2009.0 → 2011.6), the social web by three and a half years in the United States (2004.2 → 2007.6) and by ten in Japan (2004.6 → 2014.8). The Japanese social-web date is the one to treat with most care: the OECD series is MIC's *SNS including LINE* item from 2012, and what it dates is when half of Japanese 16–74-year-olds used a social networking site in the last three months — not when the social web arrived (mixi's rise, 2004–2008, is not in it). It is a measured date for a stated definition, and the definition is late.

Korea's social-web bound — the midpoint is at or before early 2005 — is *earlier* than the measured US and Japanese dates and *later* than its own placeholder (1999.7). The placeholder stands because the rule forbids wiring a bound.

## The distortion this introduces

v5 mixes a placeholder Korean date with measured Japanese and US dates inside the same wave. For the social web that puts Korea at week 195 and Japan at 1032 — a 16-year stagger that no measurement supports on the Japanese side (the definition is late) or the Korean side (the date is a guess). The harness's early history therefore carries an artificial local structure. The identification experiment on v5 shows it: the early market and common blocks rise, the late cross-market correlation falls to +0.70, and the largest five-week move lands at week 138. These are effects of the mix, not findings about the world, and the v5 numbers are read with that in front of them.

## What this does not establish

- Anything about Korean smartphones or the Korean social web beyond the bound.
- That a household rate (Japan) and an adult rate (US) date the same thing; the rule treats them alike and says so.
- That the Japanese social-web date is the arrival of the social web rather than the arrival of the survey's definition.
- One width per wave from two markets.
