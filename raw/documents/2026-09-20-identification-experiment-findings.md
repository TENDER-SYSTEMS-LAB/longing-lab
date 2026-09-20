# Identification experiment — findings, 2026-09-20

**Type:** document (findings)
**Script:** `2026-09-20-identification-experiment.py`, run against `2026-09-20-loop-simulation-harness-v3.py` unmodified
**Run:** 2026-09-20, five seeds (11–15), harness defaults unless stated; total wall time about fifteen seconds
**Attribution:** llm-proposed — the assistant's design and reading of the fourth round's Section 7; no value here is a decision

This is the procedure every fourth-round reviewer proposed and none ran: generate the thirty-three-security panel, remove the lines the institute measures rather than estimates, and ask what the listing can identify — early, late, and against a planted null. It does not select a factor set. The harness's wave dates and every coefficient are placeholders, so every number below is a property of *this* generated world, not of the real one.

## What was done

Weekly log returns of the quote for 3 markets × 11 practices over 1,564 weeks. Two measured lines removed first, in this order: the **numeraire** (exact — the quote is `V·e^z / U`, so adding `Δlog U` back removes it without estimation) and the **declared schedule** (each security regressed on its own market's arrival and substitution increments, which the harness publishes). Everything after that is what an estimator would have to find. Windows: early = weeks 60–460, late = the last 400 weeks, the same windows the harness's own convergence test uses.

Five readings of the residual panel follow.

## 1. The handover is visible, and it runs through the interaction space

Variance shares of the residual, by the two-way blocks the fourth round named:

| window | common (1 dof) | market (2) | practice (10) | interaction (20) |
|---|---|---|---|---|
| early | 0.099 | 0.097 | 0.452 | 0.351 |
| late | 0.091 | 0.065 | 0.666 | 0.177 |

Convergence moves a third of the interaction block into the practice block; the market block shrinks by a third. This is GLM's handover, with one correction to how the round described it: in this world a *local* shock is not a market factor. The harness's early events hit one market with a practice-shaped loading, and that is interaction-space by construction — *a practice dying at three speeds is three cell effects, not one practice factor* — so what drains as the markets converge is the interaction block, not the market block. The two market contrasts were never large.

## 2. The count that can be recovered depends on the window more than on the truth

The harness's own event-factor count was swept as the truth, and an eigenvalue-ratio estimator asked to recover it on three panels: the full 33, the practice-average 11 (the cross-market-uniform part), and the market-demeaned 33.

| true | early: full / avg / demeaned | late: full / avg / demeaned |
|---|---|---|
| 3 | 3 / 8 / 12 | 6 / 4 / 12 |
| 6 | 1 / 7 / 2 | 2 / 8 / 5 |
| 9 | 2 / 7 / 1 | **8** / **9** / 7 |
| 13 | 1 / 1 / 1 | **9** / 8 / 9 |

Medians over five seeds. Early, the full panel collapses to one or two dominant directions whatever the truth — the local events are spread across three market-specific copies, and no copy is strong enough to clear the bulk. Late, the same estimator recovers eight of nine and nine of thirteen. **Thirteen is never recovered**: the late panel saturates near nine, which is the round's *never thirteen at once* in a number. The practice-average panel is the one that names factors late, as the round said it would, and it is the one that is unstable early. The market-demeaned panel over-counts small truths (twelve for three) because with the common direction removed the estimator fastens on noise ratios; that column is a warning about the estimator, not a result about the world.

## 3. A fixed threshold cannot be the promotion gate

The gate tested: does a candidate direction lower held-out unexplained variance beyond three existing principal components? Fit on the first half of the window, scored on the second. Forty random 33-vectors per seed as planted nulls; the harness's nine true loading columns, tiled across markets, as true candidates.

| window | null median | null 95th pct | true median | power at the null's 95th |
|---|---|---|---|---|
| early | 0.0223 | 0.0382 | 0.0713 | 0.89 |
| late | 0.0155 | 0.0319 | 0.0641 | 0.98 |

A random direction removes about two percent of held-out variance by construction — there are thirty-three directions and the residual is spread across them — so any fixed reduction threshold below about four percent would promote most nulls. The threshold has to be calibrated on the null distribution per window, which is what Claude, GLM and ChatGPT said and what this run does. Calibrated that way the gate has power 0.89 early and 0.98 late against the generator's own factors. This is one gate of the battery; rank increment, support, placebo, stability and the post-publication check were not run.

## 4. Two markets predict the third late, and barely early

Factor series fit on two markets' twenty-two securities, loadings fit on the third's, R² on the third:

| k | early | late |
|---|---|---|
| 2 | 0.088 | 0.245 |
| 5 | 0.180 | 0.447 |
| 9 | 0.228 | 0.563 |

Early, two markets explain under a quarter of the third even with nine factors: the third market has its own weather. Late, nine factors explain more than half. The number is the cross-market transportability of the factor structure, and it is the mirror of Section 1.

## 5. The orthogonalisation order moves the schedule line a lot, early

The declared schedule line was estimated twice: before the factor lines (schedule first, then five principal components on the residual) and after them (five components removed first, schedule on what is left).

| window | rms shift / rms of the line | schedule-first mean, bp/week | factors-first mean, bp/week |
|---|---|---|---|
| early | 1.450 | −3.67 | −6.94 |
| late | 0.567 | −10.07 | −11.17 |

Early, swapping the order changes the line's weekly attribution by more than the line's own size and nearly doubles the drift it carries; late, the shift is about half. This is the deferred question about the attribution's order, given a magnitude: in the early history the split between *substitution* and *factor* is mostly a convention, and the published order decides what the institute says caused the decline. Late, the two converge because the substitution drift dominates everything.

## What this does not establish

- No factor names. The estimator recovers a span; the harness's factors have no names either.
- No result about the real world. Wave dates, loadings, event rates and every coefficient are the harness's placeholders. The WDI spine retrieved the same day is not wired into the harness yet.
- Only one gate of the battery, only one estimator, five seeds, two windows. Rank tests, placebo on permuted arrival dates, stability, and the post-publication encompassing check are not run.
- Positioning and reflexive lines are not stripped, because the harness does not expose flows; their content sits inside the residual and inflates the early interaction block by an amount not measured.
- The order experiment swaps two lines. The full six-line ordering has 720 permutations; none beyond these two was tried.
