---
status: working
attribution: jointly-developed
updated: 2026-09-05
sources:
  - SRC-2026-09-04-longing-concept-brainstorm
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
  - SRC-2026-09-05-qwen-critic-of-model
  - SRC-2026-09-05-kimi-critic-of-model
  - SRC-2026-09-05-pricing-model-v2-factor-framework
  - SRC-2026-09-05-pricing-model-v2-factor-review-claude
  - SRC-2026-09-05-pricing-model-v2-factor-review-deepseek
  - SRC-2026-09-05-pricing-model-v2-factor-review-gemini
  - SRC-2026-09-05-pricing-model-v2-factor-review-glm
  - SRC-2026-09-05-pricing-model-v2-factor-review-grok
---

# Index Architecture

The set of indices LONGING publishes, and the reasoning behind how the universe is divided. Accepted by the user as a provisional direction ("일단은 그렇게 가보자"); the tickers and the composition are first-pass proposals, not fixed.

## Governing choice: index by condition, not by sentiment

The universe is not divided into "romantic things". It is divided by **the conditions that make something feel romantic in the first place** — latency, chance, friction, physicality, unstructured time, unmediated contact. This is what keeps the work from being nostalgia art: those conditions are exactly what current technology is removing, so the indices double as a running critique of the present rather than a fondness for the past.

A second, related rule: **index names must not be poetic.** `Lost Romance Index` or `Beautiful Things Index` are out. Names read like real economic indicators.

## Structure

```text
LONGING INDEX
LNGI
│
├── LTY  Latency
├── SRD  Serendipity
├── FRX  Human Friction
├── MAT  Materiality
├── UST  Unstructured Time
└── UMD  Unmediated Interaction
```

### LNGI — LONGING Index

The broad benchmark across the whole covered universe; the S&P-500 role. Described inside the work in deliberately flat language: *broad-market benchmark covering assets classified within the LONGING universe.* Its ticker is unsettled — `LNGI`, `LX`, and `LCI` (Longing Composite Index) were all floated, to be decided once the security taxonomy exists.

### LTY — Latency Index

The value of waiting. Letters, waiting for a reply, film development, waiting for someone, meeting without arrangement, waiting for the next episode, hand delivery. Directly opposed to the defining direction of modern technology, which is to drive latency toward zero. The question the index poses: what is lost as it approaches zero seconds?

### SRD — Serendipity Index

The value of the unpredicted. Getting lost, a shop found by accident, chance meetings, a song discovered without a recommendation, an unplanned trip, a misdialed number. Structurally opposed to recommendation, personalization, prediction, and optimization — a correlation the research desk can cover directly (recommendation accuracy up, serendipity down).

### FRX — Human Friction Index

Everything UX exists to remove: going in person, handing over cash, writing by hand, long conversation, asking directions, mistakes, inconvenience, waiting. The counter-question to *reduce friction*: does anything human survive the removal of all friction? The LONG case in one line — certain forms of friction function as evidence of intent.

### MAT — Materiality Index

What physically remains: letters, printed photographs, tickets, receipts, marginalia, worn objects, albums, CDs and LPs, wrapped gifts. Faces digitization head-on, and carries a built-in disagreement: does shrinking physical volume mean falling value, or does rising scarcity mean the opposite?

### UST — Unstructured Time Index

The value of purposeless time: doing nothing, staring out a window, aimless walking, late-night conversation, a drive with no destination, simply being together, boredom. Opposed by productivity, scheduling, optimization, content consumption, and the quantified self. Named for the concept; the label itself still needs work.

### UMD — Unmediated Interaction Index

Human experience with no system in between: a recommendation from a friend, asking a stranger for directions, an introduction, a chance conversation, calling directly, visiting unannounced. Under pressure from algorithmic recommendation, search, AI assistance, matching, and automated customer experience.

## Contrast indicators

The opposing forces are shown as **contrast indicators on the same dashboard**, not as a separate market: Efficiency, Optimization, Automation, Predictability, Mediation. Displayed as neutral data, paired against their counterparts:

```text
HUMAN FRICTION     38.21   -2.81%
EFFICIENCY         91.42   +1.94%

SERENDIPITY        31.18   -4.20%
PREDICTABILITY     87.21   +2.11%

UNMEDIATED         42.91   -1.72%
AUTOMATION         94.20   +3.14%
```

The system must never characterize efficiency as bad. It reports 5-year returns — Efficiency +184.2%, Serendipity −42.8% — and lets the viewer arrive at the discomfort: *the world really is improving, so why is this chart sad?* That feeling is the intended one.

## Securities and membership

Individual securities are behaviors, situations, and cultural units — never abstract emotions, which is the deliberate break from prior art (see [[prior-art]]). Working examples: `LTR` LETTER, `WTG` WAITING, `SRD` SERENDIPITY, `NTW` NIGHT WALK, `CLL` UNPLANNED CALL, plus proposals such as mixtape-making, an aimless drive, a call from a payphone, and the interval before film is developed.

A security can belong to several indices at once — LETTER sits in Latency, Human Friction, and Materiality — which is a large part of what makes the structure read as a real market.

Prices are shown across long horizons rather than as a single day's quote: current price, values at 1998 / 2008 / 2018 / 2026, 52-week and all-time highs. That moves the work's subject from measuring emotion to **recording disappearance**.

Four of the six sub-indices — Latency, Serendipity, Human Friction, Unstructured Time — were judged the likeliest core vocabulary of the work.

## Evolution — the contrast indicators became the macro layer (2026-09-05)

**Previous state.** Efficiency, Optimization, Automation, Predictability, and Mediation were display elements: neutral series shown beside their counterparts so the viewer could feel the discomfort of a world that is genuinely improving.

**Transition.** The user asked for the market equivalent of interest rates and exchange rates — forces that move a security when nothing about the security has changed. The contrast indicators were promoted from display to mechanism: each becomes a system-wide variable, each security carries a signed exposure to it, and a week of rising Immediacy pushes `LETTER` down with no letter-specific news.

**Current state.** The promotion is accepted in principle and the *set* is not. The first seven reviews rejected seven near-collinear factors and would collapse them to between one and three, with a discount-rate role at the centre. A subsequent working framework accepts the diagnosis but proposes restoring complexity through a hierarchy of observables, identified latent factors, security exposures, valuation regimes, and positioning. Five verified second-round reviews support that reframing while leaving factor membership open. See [[pricing-model]], [[model-review-consensus]], and [[factor-architecture-review-consensus]].

This changes the indices too. Three families now exist rather than one: the **asset indices** on this page, the **system indicators** acting as macro variables, and **market indicators** describing the market's own state — consensus strength, dispersion, long/short breadth, discount to fundamental, realized volatility.

```text
LONGING MARKET OVERVIEW

LNGI                    38.42   -1.82%

SYSTEM INDICATORS
AUTOMATION              94.18   +2.4%
IMMEDIACY               96.82   +1.7%
MEDIATION               91.34   +3.1%

MARKET
LONG BREADTH             32.8%
SHORT BREADTH            51.4%
CONSENSUS STRENGTH       78.2
FUNDAMENTAL DISCOUNT    -18.4%
```

One caution carried over from review: a constructed indicator must be published as an index level with a base date and a construction rule, never as a measurement of the world. `Immediacy 138.4` is defensible as the former and indefensible as the latter.

## Weighting — unresolved, and now the blocking question

Index composition cannot be published until the work says what one unit of a security is. That has become its own question — see [[Q-004-unit-of-account]] — and the reviews divide sharply: equal weighting with a stated institutional position (*a research house that declines to rank human experiences by importance*), against practice-capitalization or footprint weighting that gives the indices a real size measure at the cost of inventing one.

What is agreed across all reviews: build securities first and aggregate upward, use divisor continuity across every constituent change, borrow the published-methodology and rebalance-calendar discipline of real index providers, and reject free-float adjustment, liquidity screens, and investability rules, which exist only because real money tracks real indices.

## Open

- The methodology and formula behind every number: see [[Q-001-price-formation]] and [[pricing-model]].
- Index weighting and the unit of account: see [[Q-004-unit-of-account]].
- Which macro factor set replaces the seven contrast indicators.
- Listing, delisting, and relisting rules: see [[Q-002-listing-lifecycle]]. Reviews add that delisting needs defining now even if it never fires, and that an index which continually removes its worst constituents understates the decline — so a survivorship-adjusted companion index may be the most eloquent number the system can print.
- The flagship index ticker (`LNGI` / `LX` / `LCI`) and the security-code scheme.
- The unit of price. A draft screen shows `27.43 KRW(?)` — the currency question is unanswered in the source.

## Related

- [[DEC-002-research-house-form]]
- [[pricing-model]]
- [[model-review-consensus]]
- [[factor-architecture-review-consensus]]
- [[analyst-system]]
- [[Q-004-unit-of-account]]

## Sources

- [[SRC-2026-09-04-longing-concept-brainstorm]] — raw/conversations/2026-09-04-longing-concept-brainstorm.md
- [[SRC-2026-09-05-price-formation-market-model]] — raw/conversations/2026-09-05-price-formation-market-model.md
- [[SRC-2026-09-05-claude-critic-of-model]] — raw/surveys/2026-09-05-claude-critic-of-model.md
- [[SRC-2026-09-05-glm-critic-of-model]] — raw/surveys/2026-09-05-glm-critic-of-model.md
- [[SRC-2026-09-05-qwen-critic-of-model]] — raw/surveys/2026-09-05-qwen-critic-of-model.md
- [[SRC-2026-09-05-kimi-critic-of-model]] — raw/surveys/2026-09-05-kimi-critic-of-model.md
- [[SRC-2026-09-05-pricing-model-v2-factor-framework]] — raw/conversations/2026-09-05-pricing-model-v2-factor-framework.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-claude]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-claude.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-deepseek]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-deepseek.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-gemini]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-gemini.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-glm]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-glm.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-grok]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-grok.md
