# Wave calibration from the WDI spine — 2026-09-20

**Type:** document (calibration record)
**Input:** `2026-09-20-wdi-spine.csv` (vintage 2026-07-13, retrieved 2026-09-20T08:07:50Z)
**Output:** the `mobile` and `broadband` rows of `WAVES` and `MEASURED_UNTIL` in `2026-09-20-loop-simulation-harness-v4.py`
**Attribution:** llm-proposed — the rule is the assistant's, chosen so that someone else applying it to the same file gets the same numbers; no value here is a user decision

## The rule

For each country and each spine series:

1. Place each annual value at its **year end**, in weeks from 1996-01: `week = (year − 1996 + 1) × 52.18`.
2. Fit a three-parameter logistic `S / (1 + exp(−(t − t0) / w))` by least squares to the annual points from 1990 to the last available year.
3. **Mobile subscriptions only**: fit on the window from 1990 up to and including the first year at or above 100 per 100. Growth past one subscription per inhabitant is lines per person — multi-SIM, machine lines, data devices, as the sourcing round set out — not people reached, and a logistic on the full series drifts to a late, wide, badly fitting curve (Japan: midpoint 2008.8, scale 367 weeks, RMSE 8.6). Broadband and internet use are fit on their full windows.
4. The wave's **arrival week** in a market is the fitted midpoint `t0`. The wave's **width**, common to the three markets, is the median of the three fitted scales `w`.
5. `MEASURED_UNTIL` is the year end of the last year in which every spine series is complete: 2023, week 1461.

Nothing is interpolated, smoothed or capped. The fit is a summary of the annual points, and the annual points are the spine as retrieved.

## The fits

| series | country | window | ceiling `S` | midpoint `t0` (week) | midpoint (year) | scale `w` (weeks) | RMSE |
|---|---|---|---|---|---|---|---|
| mobile `IT.CEL.SETS.P2` | KOR | 1990–2010 | 94.92 | 250 | 1999.8 | 113 | 5.52 |
| | JPN | 1990–2011 | 94.73 | 255 | 1999.9 | 153 | 4.86 |
| | USA | 1990–2015 | 103.28 | 376 | 2002.2 | 191 | 1.15 |
| broadband `IT.NET.BBND.P2` | KOR | 1998–2024 | 42.97 | 458 | 2003.8 | 184 | 3.23 |
| | JPN | 1998–2023 | 33.84 | 548 | 2005.5 | 154 | 2.26 |
| | USA | 1998–2024 | 35.13 | 564 | 2005.8 | 159 | 1.97 |
| internet use `IT.NET.USER.ZS` | KOR | 1990–2024 | 90.51 | 311 | 2001.0 | 106 | 5.70 |
| | JPN | 1990–2024 | 87.29 | 369 | 2002.1 | 139 | 3.39 |
| | USA | 1990–2024 | 84.26 | 279 | 2000.4 | 172 | 6.01 |

## What was wired in, and what was not

| wave | v3 placeholder (KR / JP / US, width) | v4 (KR / JP / US, width) | basis |
|---|---|---|---|
| mobile | 150 / 50 / 240, 100 | **250 / 255 / 376, 153** | measured |
| broadband | 205 / 350 / 380, 100 | **458 / 548 / 564, 159** | measured |
| dial-up | 10 / −40 / −80, 100 | unchanged | placeholder — no measured series exists |
| social web, smartphone, messaging, AI | unchanged | unchanged | placeholders — no measured three-country series |
| `MEASURED_UNTIL` | 1540 | **1461** | end of 2023 |

**Internet use was fitted and not wired.** It is not a dial-up series: the sourcing round's finding that *general Internet penetration is not a measured dial-up/BBS series* holds, and its midpoints (2000–2002) sit between the mobile and broadband midpoints rather than before them. It is kept here as a check series. Its three midpoints fall within 1.7 years of each other, which is the cross-market timing comparison the sourcing round said the spine supports.

## What the measurement moved

Against the placeholders, the measured dates are **later in every market for both waves**, and the order of arrival changes. In v3 Japan led mobile by two years; measured, Korea and Japan reach the midpoint in the same season (1999.8, 1999.9) and the United States two and a half years later. In v3 broadband's spread across the three markets was 175 weeks; measured, it is 106, with Korea leading by a year and a half and Japan and the United States arriving together. The measured widths are half again as wide as the placeholder.

## What this does not establish

- Whether the logistic is the right functional form; it is a summary, and the harness's own adoption curve is logistic, so the two match by construction.
- Anything about the five unmeasured waves. Their dates are still judgements shaped after the order of arrival.
- Whether one width per wave is right. The three fitted scales differ by up to 70% within a wave; the median discards that.
- Whether `MEASURED_UNTIL` should be one number. The boundary is one per series and was deferred; 1461 is the earliest of them.
- The mobile truncation at 100 per 100 is a declared rule, not a measured fact about when telephony reached the population.
