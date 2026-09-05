---
status: working
attribution: jointly-developed
updated: 2026-09-05
sources:
  - SRC-2026-09-04-longing-concept-brainstorm
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
  - SRC-2026-09-05-kimi-critic-of-model
  - SRC-2026-09-05-qwen-critic-of-model
---

# Analyst System

The mechanism that turns LONGING from "a fictional market that prices romance" into "a market where incompatible views of what a human being is collide". The premise came from the user: split the analysts, so that the same security — a handwritten letter — draws a LONG report from one and a HOLD or SHORT from another, with the two personas deliberately opposed, because a market is the place where a buyer's and a seller's opposite judgments are expressed as one price.

## Long and short are not good and evil

LONG bets on what is disappearing: letters, waiting, chance, aimless walks, late-night calls, the last train, the interval before film is developed. SHORT bets on what removes it: efficiency, optimization, automation, immediacy, recommendation algorithms, predictability, frictionless experience.

The paradox that makes it work: **in the real market, the SHORT case has the better outlook.** The institution says so coldly, and the work still stands with LONG. The system picks SHORT; the artist picks LONG; neither is announced.

## The analysts

Each analyst is a coherent investment philosophy, which is to say a coherent philosophy of life. The difference between them is not emotion versus reason — it is **what they are willing to count as value**.

### Eleanor Vale — Human Value Research

LONG-biased. Values time, waiting, memory, uncertainty, effort, and physical trace. Inefficiency is not a defect to her; the fact that something took time is itself evidence of value. She argues like an analyst, not a poet: *The market continues to price waiting exclusively as a cost. We disagree.* Her named value factors — scarcity, non-substitutability, the cost of signaling intent, physical persistence — are asserted as real inputs.

Crucially she can also go SHORT: NOSTALGIA, for instance, on the grounds that making the past prettier than it was consumes romance rather than preserving it. That refusal is what keeps her from being a sentimental character.

### Adrian Kessler — Structural Research

SHORT-biased. Values utilization, scalability, substitution, network effects, and time cost. He does not dislike letters; he believes their value cannot be demonstrated. His reports are the most rigorous, his record the best. *Sentimental attachment should not be confused with intrinsic value.* Hard to call wrong, and quietly unbearable.

He can also go LONG — SOLITUDE, for example — but never for romantic reasons: as algorithms occupy every empty interval, being alone becomes a scarce asset. Supply falls, scarcity rises, price rises. He reaches Eleanor's conclusion by a route that has no room for her reasons.

Explicitly not a robot and not a villain: no `A-17` codename, no machine persona. Credentials, photograph, and prose are all entirely normal. What is unsettling is that certain things simply do not exist inside his model. See [[Q-003-calibrating-the-bias]].

### Mina Seo — Behavioral Research

Watches only what people actually do: search volume, records, cultural and generational shifts. Indifferent to both romance and efficiency. On LETTER she publishes HOLD: *Sentiment remains strong while behavioral conversion remains weak.* Put plainly — people say they love handwritten letters, and do not write them.

### Julian Hart — Quantitative Strategy

Almost no prose. Signal, momentum, usage, scarcity, sentiment, replacement risk, a model output, a 12-month target, a confidence figure. Possibly the most accurate long-range judge of romance in the building, which is its own joke.

## The same event, four readings

One event — handwritten correspondence rises 17% — produces four reports: a structural turning point (Eleanor, LONG), a nostalgia-driven rally without fundamentals (Adrian, SHORT), watch whether interest converts into behavior (Mina, HOLD), signal unchanged (Julian, SHORT). And a price: `LETTER 31.82 ▲8.4%`.

**The work never says who was right.** Only the market answers, with a number.

## Analysts argue, politely

Rebuttals stay in research register and never name the opponent. Eleanor writes *the market continues to underestimate the value of waiting*; days later Adrian publishes "Scarcity Is Still Not Value", beginning *recent bullish commentary has framed declining supply as evidence of increasing intrinsic value. We disagree.* A regular reader knows exactly who is being answered. That is the moment the analysts stop being labels and become characters.

The SHORT desk must occasionally be uncomfortably right — on VINYL: *Consumers romanticize behaviors they no longer practice.* That sentence attacks the entire project, which is why it belongs in it. The work begins to doubt itself.

## Track records

Every past report persists, with accuracy and multi-year alpha attached: Adrian ranked first, Eleanor far down the table. The tension this creates is the intended one — the philosophically more beautiful analyst may perform badly, and the analyst nobody wants to agree with may keep being right. Whose judgment does the viewer follow?

## Consensus, and the viewer as the fifth analyst

A security page shows a rating distribution (LONG 5 / HOLD 3 / SHORT 4), a consensus target, high and low targets, and the spread between them. Then it asks: **What's your position?** LONG · HOLD · SHORT.

The response is `Position recorded.` and nothing else. No "you're a romantic ❤️". The register stays clerical to the end.

Aggregate participation is displayed as data (LONG 61.8% / HOLD 24.1% / SHORT 14.1%, 12,481 participants). One rule is explicit: **the vote distribution must not be the price.** Price is set by a separate market mechanism, because a 90% LONG majority can still be outweighed by a small number of far stronger SHORT convictions — conviction moves price, not headcount. The mechanism itself is unresolved: see [[Q-001-price-formation]].

Accumulated positions become the viewer's Portfolio — in effect a portfolio of their own values:

```text
YOUR POSITIONS

LETTER              LONG
WAITING             LONG
SOLITUDE            LONG
NOSTALGIA           SHORT
EFFICIENCY          HOLD
SERENDIPITY         LONG
```

## Publication cadence

The research desk publishes on a schedule, like a real one: a weekly Morning Brief listing LONG and SHORT calls, initiating-coverage notes, and an annual report ("The State of Longing 2026"). Reports carry ratings, targets, risk sections, and investment theses; a LONG note may close on a single line that turns the report into the work — *Some things become valuable precisely because they take time.* SHORT notes stay dry to the last word.

## The analysts became part of the pricing machinery (2026-09-05)

Until 2026-09-05 the analysts were a device for staging disagreement. With the market model they acquire a mechanical role: **monthly research sets the anchor the weekly price moves toward.** See [[DEC-003-weekly-market-monthly-research]] and [[pricing-model]].

Each monthly report now carries a rating, a **target price**, and a **conviction**, and consensus is formed by weighting targets by conviction rather than counting votes — which preserves the existing rule that conviction size moves price and headcount does not:

```text
ELEANOR VALE     LONG    Target 41.00   Conviction 82%
ADRIAN KESSLER   SHORT   Target 18.50   Conviction 94%
MINA SEO         HOLD    Target 28.00   Conviction 61%
JULIAN HART      SHORT   Target 23.80   Conviction 76%
```

Between monthly reports the desk publishes flash notes rather than research — `No rating change. Target unchanged.` or a revised estimate in four lines. That is what a real desk does between coverage updates, and it keeps the weekly cadence affordable.

### A target price is not a valuation

The distinction the reviews insisted on, and the one that most enriches these four characters: a target price is a **forecast of where the market price will be**, not a claim about what something is worth. Kessler can hold that a handwritten letter is fundamentally worth 34.80 and still target 18.50, because he is forecasting that nobody will pay for it. Vale can share his fundamental estimate and target 41.00 because she thinks the market is wrong. Same value, opposite trades — and it stops the analysts from being reducible to optimist and pessimist.

One review assigns each analyst a distinct channel of the model, so that their edge is structural rather than temperamental: Vale trades the valuation multiple, Kessler trades the discount and the factor drift, Seo trades the periodic behavioral print, Hart trades anchor dynamics and positioning squeezes. Their published scorecards then rise and fall as their channel's predictive power waxes and wanes — the regime becomes visible in the analyst league table, which is irony emerging from structure rather than from writing.

### Three warnings from review

- **Circularity.** If analysts set the fundamental, and analyst consensus overrides the fundamental, and analyst track records are scored against price, the system is one opinion split in half fighting itself. The fix is to generate the fundamental by a process the analysts do not control, and let them *estimate* it on the record — which also makes credibility earned rather than stipulated, and turns Kessler being right into something the record shows rather than something the work asserts.
- **Caricature.** If Vale is always LONG and Kessler always SHORT, they become costumes. Recommendations should be functions of price, fundamentals, and the macro state — Kessler should occasionally go LONG when price falls far below even his pessimistic estimate. This is consistent with what the source conversation already established: Vale shorts NOSTALGIA, Kessler goes long SOLITUDE.
- **Operational load.** Four analysts across a large universe every month is roughly two thousand reports a year, and the failure mode is visible: stale, templated research that destroys exactly the credibility the work runs on. The realistic fix is also a realism gain — real sell-side coverage is sparse and uneven. Most securities carry one or two analysts, some carry `NO COVERAGE` with correspondingly wider valuation uncertainty and thinner liquidity, and coverage initiation or a coverage drop becomes an event in itself.

### The viewer's positions

Unchanged in principle — participant votes are displayed, never priced. One review notes the option of treating the aggregate as genuine **retail positioning** if the audience votes, which would be real rather than invented data and would make the audience part of the market's crowding. Recorded as an option, not adopted: it would give viewer behavior an indirect route into price, which the existing rule was written to prevent.

## Related

- [[index-architecture]]
- [[pricing-model]]
- [[model-review-consensus]]
- [[system-grammar]]
- [[DEC-002-research-house-form]]
- [[DEC-003-weekly-market-monthly-research]]

## Sources

- [[SRC-2026-09-04-longing-concept-brainstorm]] — raw/conversations/2026-09-04-longing-concept-brainstorm.md
- [[SRC-2026-09-05-price-formation-market-model]] — raw/conversations/2026-09-05-price-formation-market-model.md
- [[SRC-2026-09-05-claude-critic-of-model]] — raw/surveys/2026-09-05-claude-critic-of-model.md
- [[SRC-2026-09-05-glm-critic-of-model]] — raw/surveys/2026-09-05-glm-critic-of-model.md
- [[SRC-2026-09-05-kimi-critic-of-model]] — raw/surveys/2026-09-05-kimi-critic-of-model.md
- [[SRC-2026-09-05-qwen-critic-of-model]] — raw/surveys/2026-09-05-qwen-critic-of-model.md
