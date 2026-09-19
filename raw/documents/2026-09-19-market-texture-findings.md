# Market texture — second simulation round

Follows `SRC-2026-09-16-loop-simulation-findings`, which established that the
shape DEC-004 asks for is reachable from DEC-007's mechanism. This round asks a
different question, set by the user against a real weekly index chart: **does it
read as a market?**

The answer at the end of the first round was no. The line was smooth, the candles
were hairlines, and a viewer would read the curve as drawn rather than traded.
Six mechanisms were added and three defects were found. 15/15 tests pass.

## Where it landed

| | LONGING | real weekly index |
|---|---|---|
| weekly σ | 2.54% | ~2.2% |
| annualised | 18.3% | ~16% |
| volatility clustering (\|return\| autocorrelation) | 0.35 | ~0.25 |
| largest 5-week move | **+32%** | −32% (2020) |
| longest advance inside the trend | 202 weeks, +11% | multi-year |
| weeks inside a flat 100-week window | 320 | — |

The sign is inverted and the magnitudes sit in the same place.

## What was added

**An event layer.** DEC-003 makes the event detector a requirement and the first
round simply did not have one — which is why the market had no texture. Events
arrive weekly, 62% of them macro and routed through one of nine factor loadings,
the rest single-name. **Only 40% are true of the practice**; the rest move the
quote and decay, which is the distinction [[information-quality]] asks for.
Monthly research pulls the premium back toward the fundamental. Events push, the
anchor pulls, and the sawtooth between them is the weekly texture.

**Default clusters follow the dying, not the dead.** Cluster probability was
uniform, so LTR's forced-covering weeks all landed after the security had already
reached the floor — squeezes on a corpse. Tying cluster probability to a
security's own rate of decline moved LTR's squeezes from weeks 1144–1793 to
311–807, while the practice is still being abandoned.

**Systemic weeks are runs, not higher hazards.** Independent per-security
clusters cancel at the index, so no index-level melt-up could occur. A systemic
week withdraws float market-wide at once. [[reserve-instruments]] already ends
the story in insolvency; a run is what insolvency looks like from inside one week.

**Regimes.** Three states — quiet, choppy, stressed — with mean dwell times of
150, 90 and 35 weeks, scaling volatility, event arrival and run probability. A
real index is not one process, and it stays in each of its processes for a long
time.

**One scheduled revival era.** DEC-004 requires that changed conditions permit
recovery. A per-week coin flip with a small probability either never fires or
fires twice, so the era is scheduled: exactly one in the history, ~250 weeks. It
produces the multi-year advance the chart needs to be a history rather than a
slope.

**Covering cascades over months.** Forced covering was resolved inside one week,
which produced spikes rather than rallies. Only 26% of a stranded position is
covered per week, the price impact strands more shorts, and shorts rebuild slowly
afterwards. That is what makes a melt-up last long enough to be named.

## Three defects, all in the first round's build

**1. Quotes could go negative.** The premium was an additive multiplier,
`P = (V/U)·(1 + prem)`. Nothing bounded `prem` below −1, so prices crossed zero
and the index changed sign, printing weekly moves of +789%. The measured σ of
33% in the first texture attempt was entirely this. Fixed by making it a **log
premium**, `P = (V/U)·exp(z)`, which cannot cross zero.

**2. BEARER BOND had no issuance.** [[reserve-instruments]] defines it as
"bilateral by construction, issuable, and defaultable" and the build implemented
only the defaults. Float fell from 10,993 to 79 and never recovered, the learning
material that feeds the loop dried with it, and the loop stalled. Worse for the
work: **a practice could never be resumed**, so a melt-up could never relapse and
the market had no way to breathe. Adding issuance — new relationships per week,
scaled by how alive the practice still is — restores both. **Who issues is
[[Q-002-listing-lifecycle]]'s question and it is now a numerical requirement, not
a preference.**

**3. This world cannot draw a weekly candle.** DEC-003 makes the week the tick, so
there is no intra-week high or low to draw. A weekly candle would require
inventing data the world does not have. The smallest honest candle is the
**month** — four weekly strikes — and moving averages are therefore in months.
The first index chart in this round synthesised a weekly range before this was
noticed; it was removed.

## The boundary

Matching a real index's statistics is a **stylistic calibration to DEC-002's
terminal register**, not evidence about the world. It answers "does this read as
traded rather than drawn", which is a question about the surface. Nothing here
calibrates a parameter against any measurement of human practice, and no factor,
coefficient, basket, or historical span becomes selected by having produced a
convincing chart.

The tuning also exposed a methodological limit worth recording: the model is
chaotic in its parameters. Changing any coefficient re-rolls the whole sample
path, so single-seed statistics move a lot for reasons that have nothing to do
with the change. Every figure above is either a median across seeds or a
structural count, never a single path read as a result.
