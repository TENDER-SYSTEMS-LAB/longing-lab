---
status: working
attribution: llm-proposed
updated: 2026-09-19
sources:
  - SRC-2026-09-19-market-texture-session
  - SRC-2026-09-19-market-texture-findings
  - SRC-2026-09-19-loop-simulation-harness-v2
  - SRC-2026-09-16-loop-simulation-session
  - SRC-2026-09-16-loop-simulation-findings
  - SRC-2026-09-16-loop-simulation-harness
---

# Loop Simulation — the first thing in this project that runs

The project has three review rounds, eight accepted model reviews, a 120-entry
cross-domain survey, and a dataset survey. Until 2026-09-16 it had never executed
anything. [[DEC-007-standard-return-numeraire]] closed the loop and reduced the
authored surface to a handful of coefficients, which made the design small enough
to run.

The user chose to run it before selecting a factor set, on the reasoning that
choosing the starting nine before seeing how β and the factors overlap would mean
choosing twice.

## What it is, and what it is not

A stdlib Python file, 2000 weeks, eleven securities, fixed seed. It advances
`A`, `U`, `βᵢ`, `Vᵢ`, `Nᵢ` and quotes weekly, and scores the tests
[[DEC-004-secular-decline-with-rallies]] already wrote down. All nine pass at the
committed defaults.

**It is not a component of the artwork, and nothing in it is a specification.**
It is an instrument for finding out whether DEC-007's mechanism can produce the
shape DEC-004 asks for. Every parameter in it is invented and calibrated against
nothing. Its value is in the four places it found the decision underspecified,
not in the fact that its tests pass.

## What it establishes

**The shape is reachable without a drift constant.** A secular decline, inverted
rallies, a structural winner that falls only because the yardstick grew, a
yardstick that stops, and a peak nobody can see in its own week — all of it from
the mechanism rather than from a coefficient pointing downward. This was the
central claim of DEC-007 and it survives its first contact with arithmetic.

**The tipping point was not designed in.** The backing stock only turns when
`creation·(1−ai_share) < attrition`. Before that week the world's trust is still
growing. The history therefore has two regimes and a phase change between them
that nothing announces — the *invisible peak* [[reserve-instruments]] recorded as
a device, arriving as a mechanical consequence.

**Saturation really does bound the loop.** No gain tested, up to 200× the
default, makes the world diverge. A badly chosen gain ends the work sooner; it
cannot explode it.

## What it found wrong, and what is still open

Four gaps, all in the decision rather than in the run. Detail and tables are in
[[SRC-2026-09-16-loop-simulation-findings]].

- **The loop could not start.** Anxiety was defined on a quantity that turns late,
  so the feedback term was zero at t=0 and stayed there. Fixed below.
- **The requisition rate `s(t)` is unspecified and decisive.** DEC-007 writes
  `dVᵢ/Vᵢ = −βᵢ·s(t)` without saying what `s` is. Above roughly `s = 20·ΔA` the
  model can never disagree with its author at any point in the history, and
  DEC-004's sharpest test fails by construction. Below that, revivals work only
  in the first half. **Open: cap `s`, or state that after the tipping point
  nothing comes back.**
- **The melt-up needs collapses an order of magnitude larger than implied.** At a
  plausible default cluster no squeeze ever fires in 38 years, because an orderly
  float decline takes the short position down with it. Stranding shorts needs a
  week in which roughly a fifth of a practice's relationships end at once.
  **Open: make that claim, or find melt-ups another source.**
- **High-β securities reach numerical zero.** `LTR` ends at ×0.000 with no floor,
  no delisting rule, and no stated meaning for a zero quote. This moves
  [[Q-002-listing-lifecycle]] from a world-building preference to a numerical
  requirement.

## The repair the user adopted

`D` was the rate at which the backing *stock* falls. It is now the trust that
will not come back:

```
D = (rate the backing stock falls) + ai_anx · ai_share · attrition
```

Anxiety is not the pile getting smaller. It is what you gave never returning, and
that starts the moment trust begins reallocating rather than when a total turns.
[[reserve-instruments]] already says trust placed in AI is one-way and returns
nothing; this only makes the existing sentence something a model can read.

The effect is large. The feedback term goes from supplying 69% of capability
growth to **98%**, the exogenous seed drops to a formality, and the reflexive
claim in DEC-007 becomes true rather than aspirational.

It also restores the page's stated cost. With the inert loop, the gain barely
mattered and an earlier version of the findings concluded DEC-007 was wrong to
say one coefficient governs the work's speed. With the loop running, `g = 0.1`
leaves the market at 45 and `g = 0.3` takes it to 6.5. The commitment to publish
the gain is load-bearing after all. That reversal is preserved in the findings
file rather than edited out.

## What it does not establish

Nothing about the world. The universe, hazard rates, creation and attrition
rates, the anxiety coefficient and the revival magnitudes are all invented. The
run is a statement about whether the *document* is complete enough to execute,
and the answer was: not yet, in four specific places, one of which is now closed.

## Second round — does it read as a market? (2026-09-19)

The first round asked whether the mechanism produces the right shape. The user
then asked for LTR as a candle chart, and the candles answered a different
question badly: the price was a smooth glide, the bodies were hairlines, and a
viewer would read the curve as drawn rather than traded. Shown a real weekly
index chart, the user set the target directly — **the LONGING market is that
chart inverted**, carrying genuine sharp moves, long advances, sideways
stretches and high-volatility regimes.

It now sits where it was asked to: weekly σ 2.54% against a real index's ~2.2%,
18.3% annualised against ~16%, volatility clustering 0.35 against ~0.25, and a
largest five-week move of **+32%** where the 2020 crash was −32%. The sign is
inverted and the magnitudes are in the same place. 15/15 tests pass, the six new
ones scoring texture rather than shape.

### What the first build was missing

**The event layer.** [[DEC-003-weekly-market-monthly-research]] makes an event
detector a requirement and the first round simply had none, which is why there
was no texture. Events now arrive weekly, mostly macro and routed through nine
factor loadings; **only 40% are true of the practice**, and the rest move the
quote and decay — the distinction [[information-quality]] asks for. Monthly
research pulls the premium back toward the fundamental, and the sawtooth between
push and pull is the weekly texture.

**Clusters that follow the dying, not the dead.** With uniform cluster
probability, LTR's forced-covering weeks all landed after it had already reached
the floor — squeezes on a corpse. Tying cluster probability to a security's own
rate of decline moved them from weeks 1144–1793 to 311–807, while the practice is
still being abandoned.

**Systemic weeks as runs.** Independent per-security clusters cancel at the index,
so no index-level melt-up was possible. A systemic week now withdraws float
market-wide at once. [[reserve-instruments]] already ends the story in
insolvency; a run is what insolvency looks like from inside one week.

**Regimes, one revival era, and cascades.** Three regimes with long dwell times
supply the quiet, choppy and violent stretches. One era of revival is
**scheduled** rather than drawn each week — a small weekly probability either
never fires or fires twice, and the history needs exactly one long uptrend to be
a history rather than a slope. Forced covering resolves over months rather than
inside a week, which is what lets a melt-up last long enough to be named.

### Three defects in the first build

- **Quotes could go negative.** The premium was additive, `P = (V/U)(1 + prem)`,
  with nothing bounding it below −1, so prices crossed zero and the index changed
  sign. A measured σ of 33% was entirely this. It is now a **log premium**.
- **BEARER BOND had no issuance.** [[reserve-instruments]] defines it as
  "bilateral by construction, issuable, and defaultable" and only the defaults
  were built. Float fell 10,993 → 79 and never recovered, the learning material
  feeding the loop dried with it, and **a practice could never be resumed**, so a
  melt-up could never relapse. See the evolution note on
  [[Q-002-listing-lifecycle]].
- **This world cannot draw a weekly candle.** The week is the tick, so there is
  no intra-week high or low. The smallest honest candle is the **month**.

### One methodological limit

The model is chaotic in its parameters: changing any coefficient re-rolls the
whole sample path, so single-seed statistics move for reasons unrelated to the
change. Every figure above is a median across seeds or a structural count, never
one path read as a result.

### The boundary on all of it

Matching a real index's statistics is a **stylistic calibration to the terminal
register of [[DEC-002-research-house-form]]**. It answers whether the surface
reads as traded rather than drawn. It is not evidence about human practice, and
nothing becomes selected by having produced a convincing chart.

## Related

- [[DEC-007-standard-return-numeraire]]
- [[DEC-004-secular-decline-with-rallies]]
- [[reserve-instruments]]
- [[Q-002-listing-lifecycle]]
- [[Q-003-calibrating-the-bias]]
- [[DEC-003-weekly-market-monthly-research]]
- [[information-quality]]

## Sources

- [[SRC-2026-09-19-market-texture-session]] — [raw/conversations/2026-09-19-market-texture-session.md](../../raw/conversations/2026-09-19-market-texture-session.md); the requirement that the market read as a real index inverted
- [[SRC-2026-09-19-market-texture-findings]] — [raw/documents/2026-09-19-market-texture-findings.md](../../raw/documents/2026-09-19-market-texture-findings.md); six mechanisms, three defects, and the calibration boundary
- [[SRC-2026-09-19-loop-simulation-harness-v2]] — [raw/documents/2026-09-19-loop-simulation-harness-v2.py](../../raw/documents/2026-09-19-loop-simulation-harness-v2.py); the current instrument, superseding the 2026-09-16 harness
- [[SRC-2026-09-16-loop-simulation-session]] — [raw/conversations/2026-09-16-loop-simulation-session.md](../../raw/conversations/2026-09-16-loop-simulation-session.md); the user decisions to simulate first and to adopt the redefined anxiety term
- [[SRC-2026-09-16-loop-simulation-findings]] — [raw/documents/2026-09-16-loop-simulation-findings.md](../../raw/documents/2026-09-16-loop-simulation-findings.md); assistant-authored results from an assistant-authored model, uncalibrated
- [[SRC-2026-09-16-loop-simulation-harness]] — [raw/documents/2026-09-16-loop-simulation-harness.py](../../raw/documents/2026-09-16-loop-simulation-harness.py); the instrument, registered so the findings can be reproduced or refuted
