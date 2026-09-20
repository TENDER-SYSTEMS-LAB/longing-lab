# Identification experiment — findings v3, on the v5 world, 2026-09-20

**Type:** document (findings)
**Script:** `2026-09-20-identification-experiment-v2.py` against `2026-09-20-loop-simulation-harness-v5.py`, five seeds
**Attribution:** llm-proposed

The same five readings on the world with four waves partly measured: mobile and broadband in all three markets, smartphones and the social web in Japan and the United States with Korea on placeholders. Read with `2026-09-20-wave-calibration-from-national-series.md` in front: the Korea–Japan social-web stagger in v5 is an artefact of mixing a placeholder with a late-defined measurement.

## Design tests, v4 against v5

16/16 pass on both. What moved:

| test | v4 | v5 |
|---|---|---|
| index over thirty years | 100 → 19.4 | 100 → 19.6 |
| CALL's fundamental peak | week 642, ×2.10 → ×0.487 | week 638, ×1.73 → ×0.383 |
| calls vs defaults | 75% | 76% |
| forced long liquidations / coverings | 47 / 2,275 | 29 / 2,141 |
| advances over +10%, longest | 10, 123 weeks | 5, 138 weeks |
| market correlation early → late | +0.21 → +0.78 | +0.25 → **+0.70** |
| weekly sigma | 2.55% | 2.50% |
| \|return\| autocorrelation | 0.22 | 0.24 |
| largest five-week move | +22.2% at week 918 | **+36.0% at week 138** |
| sideways weeks | 281 | 277 |

Late convergence weakens and the biggest melt-up moves from 2013 to 1998. Both follow from the social-web row: Korea's placeholder at week 195 now sits alone sixteen years before Japan's measured 1032, so the early history has a large local arrival nothing else shares, and the late history has one fewer coincident wave to converge on.

## The five readings, v4 against v5

**1. Variance shares** — early: common 0.093 → **0.158**, market 0.101 → **0.143**, practice 0.468 → 0.409, interaction 0.337 → 0.291; late: common 0.100 → 0.114, market 0.077 → 0.094, practice 0.631 → 0.586, interaction 0.191 → 0.207. The early market and common blocks grow. This is the first run in which the market block is not small early, and it is the artificial stagger doing it.

**2. Recovered count** — early: still one direction for truths 6, 9 and 13 on the full panel, but **twelve for a truth of three**, where v4 gave two; late: 6 / 1 / 8 / 8 for truths 3 / 6 / 9 / 13 against v4's 6 / 7 / 8 / 8. The saturation near eight holds; thirteen is again never recovered; the estimator is less stable at low truths, which the early stagger explains.

**3. Gate** — early null 95th 0.0446, true median 0.0699, power 0.93; late 0.0330 / 0.0778 / 0.96. Unchanged in conclusion.

**4. Leave-one-market-out** — k=9: early 0.254 → **0.305**, late 0.520 → **0.466**. More transportable early, less late: the same stagger, seen from the other side.

**5. Order sensitivity** — early 1.847 → **1.879**, late 0.567 → 0.508; schedule-first drift −2.56 → −3.10 bp/week early, factors-first −6.08 → −6.77. The early split remains a convention.

## What this does not establish

Everything the first two runs did not, plus: two of the four newly dated markets are measured against definitions that date late (Japan's SNS-including-LINE item) or early (a US internet-user base), Korea is a placeholder in both new waves, and the v5 world's early structure is partly the mix. The honest comparison for design purposes remains v4; v5 is what the record looks like when the measured and the guessed are wired side by side.
