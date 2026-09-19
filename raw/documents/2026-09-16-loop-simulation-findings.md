# DEC-007 loop — simulation findings

`sim.py`, stdlib only, 2000 weeks (~38 years), 11 securities, fixed seed.
`python3 sim.py` runs it and scores DEC-004's own tests. 9/9 pass at the
committed defaults.

The passes matter less than the seven findings. Four are gaps in DEC-007; one is
a correction to DEC-007's stated cost; one reverses a claim made earlier in this
report; and one is a repair the user adopted.

## 1. The loop as written has no ignition.

`A(t+1) = A(t) + g·D(t)·L(t)`, with `D` defined as the rate at which the backing
stock falls. At t=0 the backing is *growing*: bilateral creation exceeds
attrition, so `D = 0`, so `A` never moves, so AI share never rises, so creation
never stops. The world sits still forever.

The first run produced a flat market, and `g` had no effect at any value from
0.1 to 20.

**Consequence.** DEC-007 says authored content "shrinks to one gain
coefficient." As originally written it is two — an ignition and a gain — and the
page needs correcting. Finding 7 reduces the ignition to a formality but does
not remove it.

## 2. There is a tipping point, and it was not designed in.

The backing only turns when `creation·(1−ai_share) < attrition`, which at the
trial rates is `ai_share > 0.35`. Before that week the world's stock of trust is
still growing.

The backing peaks at week 613 of 2000 and falls for the remaining 1387. Nothing
announces the crossing. It is legible only afterwards, as the week the pile
stopped growing — which is the *invisible peak* [[reserve-instruments]] recorded
as a device and DEC-007 promised the mechanics would produce. It does, and it was
not put in by hand.

## 3. The requisition rate is unspecified, and it alone decides whether the work can argue with itself.

DEC-007 writes `dVᵢ/Vᵢ = −βᵢ·s(t)` and never says what `s` is. The simulation has
to pick one: `s = req_k · ΔA`. That choice decides DEC-004's sharpest test —
whether a genuine revival can stage a bull market against the author's thesis.

| `req_k` | FILM revival at week 300 | at 700 | at 1200 | at 1500 |
|---|---|---|---|---|
| 4  | ×2.57 | ×2.15 | — | — |
| 8  | ×1.90 | ×1.45 | — | — |
| 16 | ×1.28 | ×1.30 | — | — |
| 20+ | — | — | — | — |

Above roughly `req_k = 20` the model can **never** disagree with its author, at
any point in the history: the design is rigged and DEC-004's test fails by
construction. Below that, dissent is possible only in the first half, because
substitution drag scales with `ΔA` and `ΔA` is largest exactly when the loop runs
hottest.

**Still open.** Either `s` is capped so late revivals stay possible, or the work
accepts that after the tipping point nothing can come back — a strong claim it
has not made.

## 4. The melt-up mechanism needs relationship collapses far larger than DEC-007 implies.

DEC-007 says a cluster of BEARER BOND defaults removes float abruptly and strands
the shorts. At a plausible cluster — 14× baseline hazard, about 1.4% of a
practice's relationships ending in one week — **no squeeze ever fires**, in 2000
weeks, across all 11 securities. Shorts scale with float when float declines in
an orderly way; only a discontinuity strands them.

| cluster size | squeezes in 38 years |
|---|---|
| 14× (1.4% of float) | 0 |
| 60× | 28 |
| 120× (18% of float in one week) | 39 |

At 120× the cadence is roughly one a year, matching the named-rally texture
DEC-004 wants. But it means the world contains weeks in which **nearly a fifth of
the relationships sustaining a practice end at once.** That is a world-building
claim DEC-007 does not make. Either it gets made, or melt-ups need another source.

## 5. The loop gain governs the work — but only once the loop actually runs. (Reversed)

An earlier version of this report said the opposite. With the inert loop of
finding 1, `g` moved the ending from 5.4 to 2.4 across a 200× change and
everything above `g = 1` was indistinguishable, so the report concluded DEC-007's
stated cost — "one coefficient governs the speed of the entire work" — was wrong.

It was wrong about an inert loop. With the repair in finding 7:

| `g` | 0.1 | 0.3 | 0.55 | 1.0 | 2.0 | 20.0 |
|---|---|---|---|---|---|---|
| final index | 45.6 | 6.5 | 2.5 | 2.4 | 2.4 | 2.4 |

`g = 0.1` leaves the market at 45 and `g = 0.3` takes it to 6.5. The page's stated
cost is accurate, and the commitment to publish `g` is load-bearing. Saturation
still bounds the loop at every gain tested, so the stability claim holds too.

## 6. High-beta securities reach zero, and delisting stops being optional.

`LTR` ends at ×0.000 of its listing price — numerically zero, not merely cheap.
The design has no floor, no delisting rule, and no statement of what a zero quote
means. [[Q-002-listing-lifecycle]] was already open; this makes it a numerical
requirement rather than a world-building preference. A market cannot print zero
every week for two hundred weeks and stay legible.

## 7. Anxiety was defined on the wrong quantity. Redefining it makes the loop self-starting. (Adopted)

`D` was the rate at which the backing *stock* falls. That quantity turns late, so
the loop could not start (finding 1) and, once started, supplied only 69% of
capability growth while the exogenous seed did the rest.

The repair, chosen by the user: anxiety is not the pile getting smaller, it is
**what you gave never coming back.** That begins the moment trust starts
reallocating, long before any total turns.

```
D = (rate the backing stock falls) + ai_anx · ai_share · attrition
```

It is not a new idea. [[reserve-instruments]] already states that trust placed in
AI is one-way and returns nothing; this only makes the existing sentence
something the model can read.

| | tipping point | loop share of growth | final index |
|---|---|---|---|
| stock-only (as written) | week 746 | 69% | 2.7 |
| slow the ignition instead | never reached | 0% | 43.2 |
| weaken requisition instead | week 746 | 69% | 3.0 |
| **redefine anxiety (adopted)** | week 613 | **98%** | 2.5 |

The exogenous seed drops to 1.6% of capability growth — present, because a
reinforcing loop still needs something to start it, but no longer the thing
driving the work.

## What was NOT fixed, and should not be

An earlier version of this report flagged that 88% of the index decline happens
before the tipping point, and called it a defect. It is not, and no configuration
changes it: the market tracks the capability curve while the tipping point tracks
an adoption share, and the two run on different clocks.

DEC-004 already requires the peak to be "invisible in its own moment and legible
only later on a chart." A peak that coincided with the market's dramatic turn
would not be invisible. It has to pass while nobody is looking, and it does.

## What this does not establish

No parameter here is calibrated against anything. The universe, the hazard rates,
the creation and attrition rates, the anxiety coefficient and the revival
magnitudes are all invented to exercise the structure. The run shows that the
**shape** DEC-004 asks for is reachable from DEC-007's mechanism without a drift
constant, and it locates where the mechanism is underspecified. It does not show
that any of these numbers are the right ones.
