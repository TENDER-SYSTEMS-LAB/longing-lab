# Identification experiment — findings v4: the rest of the gate battery, on the v4 world, 2026-09-20

**Type:** document (findings)
**Script:** `2026-09-20-identification-experiment-gates.py` against `2026-09-20-loop-simulation-harness-v4.py`, five seeds (11–15), three existing lines assumed, forty planted nulls per seed and window
**Attribution:** llm-proposed

The first run tested one gate — held-out reduction of Unexplained — and found it needs calibration on a planted null, after which its power is above 0.9. This run tests the other gates the fourth round named, each on the same residual (numeraire removed exactly, declared schedule regressed out), each calibrated on a planted null where a threshold is needed. The result is uneven, and the unevenness is the finding: **on this world only two gates carry power.**

## A. Support — works as a floor, not as a test

| candidate | pass rate |
|---|---|
| random 33-vector | 0.98 |
| true generator column, tiled across markets | 0.93 |
| a single cell (one security) | 0.00 |
| a single market (eleven securities, one market) | 0.00 |
| a single practice (three securities, one practice) | 0.00 |

The gate — entries above half the maximum loading must span at least two markets and two practices — turns away exactly what it is for: a cell effect, a market effect, a practice effect. It does not distinguish a true factor from noise, and is not meant to. It is the formal form of *a factor on two constituents is a security-specific effect with ambitions.* The 7% of true columns it rejects are columns whose loading happens to concentrate on one or two practices.

## B. Bulk clearance — half power

Variance along the candidate direction, divided by the median eigenvalue of the residual after three principal components:

| window | null median | null 95th | true median | power |
|---|---|---|---|---|
| early | 2.05 | 3.52 | 3.55 | 0.53 |
| late | 5.92 | 11.44 | 10.80 | 0.49 |

Two things. A random direction sits at twice the bulk, not at one — because with nine pervasive factors in a 33-dimensional space, any direction has a projection on the factor span of order 9/33, so the "bulk" is not noise. And the true median sits at the null's 95th percentile: the generator's nine event factors are of similar strength, three are already absorbed by the existing lines, and of the remaining six about half are too weak, in a 400-week window, to clear the bulk with the calibrated margin. The gate is not wrong; the world has more factors than it can separate at once, which is what the count experiment found from the other side.

## C. Stability — no power on this world

Share of the 33 loading signs, fit on each half of the window against the candidate's own series on the residual after three components, that agree:

| window | null median | null 95th | true median | power |
|---|---|---|---|---|
| early | 0.82 | 0.94 | 0.85 | 0.07 |
| late | 0.88 | 0.97 | 0.91 | 0.00 |

A random direction's loadings are *also* stable, at 82–88% sign agreement, because the residual is dominated by pervasive structure and any direction's projection inherits it. Calibrated on that null the gate has no power. Sign stability, as the round specified it, does not discriminate here; it would need to be stated against something the null lacks, and the run does not supply what that is.

## D. Placebo — the declared schedule is not identified from cross-market timing on v4

R² of each security on its own market's declared arrival and substitution increments, on 26-week block returns, with the true market labels against the five permutations of them:

| window | true R² | permuted median | permuted max | permutations beating the truth |
|---|---|---|---|---|
| early | 0.107 | 0.083 | 0.258 | 0.36 |
| late | 0.035 | 0.033 | 0.049 | 0.40 |
| full | 0.013 | 0.012 | 0.017 | 0.40 |

With five permutations the smallest attainable p-value is one in six, and the truth does not reach even that: more than a third of the permutations explain as much or more. Late this is expected, since the markets' schedules coincide. **Early it is the measured dates doing it**: in v4 Korea and Japan reach mobile in the same season and broadband within two years, so swapping their labels costs little. The three-market stagger that [[DEC-009-three-markets-and-convergence]] relies on for identification is, for the two waves now measured, smaller than the placeholder world had assumed. The declared schedule is still a *measured* line — it does not need to be identified from returns — but the placebo shows that returns alone would not recover which market's schedule is which.

## E. Unexplained monitor — weak late, unreliable early

Eigenvalue-ratio count of factors left in the residual, before and after admitting one more line:

| window | admitted | count |
|---|---|---|
| early | none | 2.80 |
| early | null | 3.18 |
| early | true | 4.47 |
| late | none | 4.60 |
| late | null | 4.70 |
| late | true | 4.00 |

Late, admitting a true line lowers the count and a null does not, by a little. Early, admitting a true line *raises* it: removing a strong direction reshapes the spectrum so that the ratio estimator sees more structure than before. The monitor as GLM specified it — trigger the promotion search while the residual is not near-diagonal — is directionally right late and not usable early with this estimator.

## What the battery is, on this world

| gate | status on v4 | use |
|---|---|---|
| held-out reduction of Unexplained (first run) | power 0.93 early, 0.96 late, once calibrated on the null | the test |
| support | rejects cell, market and practice effects; passes everything else | the floor |
| bulk clearance | power about 0.5 | a second opinion at best; too many factors of similar size |
| stability | no power | not usable as specified |
| placebo on arrival labels | does not reject, early or late | a finding about the measured stagger, not a gate |
| Unexplained monitor | weak late, wrong direction early | a diagnostic, not a trigger |

A promotion rule for this world would rest on the held-out gate and the support floor. The other four are recorded with their failure modes so the next specification of them starts from what did not work.

## What this does not establish

Every gate was run with three existing lines, on residuals that still contain positioning and reflexive content, on placeholder coefficients for five of seven waves. The bulk and stability nulls are random directions in the full space; a null drawn inside the interaction space would be a stricter test and was not run. The placebo has five permutations because there are three markets; it cannot say more than that.
