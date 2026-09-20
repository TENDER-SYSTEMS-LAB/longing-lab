# Rebuild on DEC-008 / DEC-009 — third simulation round

The first two rounds tested a design that has since been replaced. This round
rebuilds the harness on the decisions as they now stand — a perpetual bond whose
principal is attention, a decline made of calls rather than defaults, technology
waves whose arrival phase leads their substitution phase, thirty years from 1996,
and three markets that start apart and converge.

16 tests pass, half of them new. Five defects were found in the build, one of
them a test that had been passing for the wrong reason.

## What the structure does that the old one could not

**The decline is redemption.** Calls outweigh defaults roughly three to one: 74%
of the balance that leaves does so because someone can now manage alone. Nobody
is betrayed for the total to fall, which is what [[DEC-004-secular-decline-with-rallies]]
requires and what a default-driven model could only be argued into.

**Arrival is visible.** `CALL` — the unplanned telephone call — rises to x1.43 of
its listing fundamental before substitution overtakes it, then falls to x0.30.
Telephony did not remove unplanned calls. It created them, and only later made
them unnecessary.

**A practice can be resumed.** Total outstanding attention rises in 969 of 1565
weeks. The previous build had float that could only fall.

**The markets converge, and nothing declares it.** Mean pairwise return
correlation across the three markets goes from +0.21 early to +0.86 late. It is
not a parameter: early waves land years apart in the three countries and late ones
land in the same season, so the convergence is the arrival dates, which is to say
it is history.

**Market texture holds.** Weekly σ 2.44%, 17.6% annualised, volatility clustering
0.16, largest five-week move +27.3%, 339 weeks inside a flat hundred-week window,
longest advance 167 weeks.

## Five defects

**1. Unnormalised drivers, and magic constants.** The first build carried `*40`,
`*1000` and `-260 * drift` from the single-market model. Scales no longer matched
and the index printed 526× its base. Fixed by normalising both drivers so their
weekly increments sum to one across the run; every coefficient then became an
elasticity and the constants disappeared.

**2. No issuance between waves.** Arrival created reliance and nothing else did,
so in the years between technologies nobody formed a relationship at all. Float
fell from 32,000 to the low hundreds and the loop starved. A baseline issuance
term fixes it: people keep leaning on each other with no new device involved.

**3. Adoption curves narrower than history.** The logistic width was 70 weeks —
about sixteen months — when Korean broadband alone took five years. Multi-year
advances capped at 93 weeks because of it. Widening to 100 weeks produced a
174-week advance. **The threshold was not lowered to pass the test; the curve was
corrected to match the world.**

**4. A test passing for the wrong reason.** *Arrival raises before substitution
takes* was measured on the **quote**, which carries the event premium. Measured on
the fundamental instead, the net drift was negative from week zero onward: the
arrival phase did not exist at all, and `CALL`'s apparent x3.08 peak was entirely
premium. The arrival elasticity was far too small relative to substitution. This
is the round's most useful finding, and it is an argument for writing tests
against the quantity a claim is actually about.

**5. Positioning could only be short.** The target position was clamped
non-negative, so the only force that could lift a price was covering. The user
named this directly: *technology brings romance too, so shorts are not the only
thing that drives a rise.* Positioning is now signed and follows a trend rather
than one week's move. Two things followed. Demand-driven rallies became possible,
and the market acquired a **downside** mechanism it had never had — a crowded long
liquidating when the revival ends.

## What the correction produced

Each wave now carries a `creates` coefficient: how much of its arrival makes new
ways to reach a person rather than new ways to manage without one.

| wave | creates |
|---|---|
| social web — the alumni boom | 1.40 |
| mobile telephony | 1.30 |
| dial-up | 1.00 |
| messaging | 0.90 |
| broadband | 0.85 |
| smartphone | 0.55 |
| **AI** | **0.12** |

AI is the outlier, and that single number is the only claim this work makes about
it: it substitutes heavily and connects almost nobody.

The consequence separates the eras by character rather than by assertion.

| advance | gain | arrival intensity | forced long liquidations |
|---|---|---|---|
| 1996.0–1996.7 | +12.2% | 1.50× | 0 |
| 1997.2–1998.3 | +10.6% | 1.75× | 0 |
| **1998.6–1999.3** | **+19.9%** | **1.90×** | **33** |
| 2015.0–2016.0 | +16.8% | 0.30× | 0 |
| 2017.5–2019.4 | +15.4% | 0.15× | 0 |
| 2023.2–2023.9 | +11.7% | 0.15× | 0 |

**Advances before 2000 are driven by arrival. Every advance after 2010 is short
covering.** The century's turn is the last time buying itself lifted this market,
and the people who bought were carried out when it ended.

## Left unbalanced on purpose

All 33 forced long liquidations fall in one episode. A mass-participation bubble
in these practices recurring several times in thirty years would be less credible
than its happening once, so the asymmetry stands.

## What this does not establish

The wave dates are placeholders, shaped after the real order of arrival in the
three countries. No statistical series has been collected, no normalisation rule
across three national definitions exists, and no proxy has been selected. The
`creates` coefficients are judgements, not measurements. Nothing here is
calibrated against anything, and matching a real index's texture remains a
stylistic calibration to the terminal register of [[DEC-002-research-house-form]].
