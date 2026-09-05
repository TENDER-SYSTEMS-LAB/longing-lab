---
status: working
attribution: jointly-developed
updated: 2026-09-06
sources:
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-deepseek-critic-of-model
  - SRC-2026-09-05-gemini-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
  - SRC-2026-09-05-grok-critic-of-model
  - SRC-2026-09-05-kimi-critic-of-model
  - SRC-2026-09-05-qwen-critic-of-model
  - SRC-2026-09-05-pricing-model-v2-factor-framework
  - SRC-2026-09-05-pricing-model-v2-factor-review-claude
  - SRC-2026-09-05-pricing-model-v2-factor-review-deepseek
  - SRC-2026-09-05-pricing-model-v2-factor-review-gemini
  - SRC-2026-09-05-pricing-model-v2-factor-review-glm
  - SRC-2026-09-05-pricing-model-v2-factor-review-grok
  - SRC-2026-09-05-pricing-model-v2-factor-review-qwen
---

# Pricing Model

How a LONGING price is produced. This page holds the market architecture that answers [[Q-001-price-formation]]: what a price is a function of, on what schedule it moves, and which parts of the machinery are settled, provisional, or still contested.

The architecture below was developed in the 2026-09-05 conversation and then put through seven independent critical reviews on the same day. Where the conversation's draft and the reviews disagree, both are recorded; the reviews are `llm-proposed` and none of their recommendations has been accepted by the user yet.

## The governing separation

The single decision the whole model rests on is that **value and price are two different numbers, displayed side by side.**

```text
LETTER

Fundamental Value     34.80
Market Price          21.42
Discount to Model    -38.4%
```

Fundamental Value is the research house's estimate of the underlying condition of a practice. Market Price is what the market currently pays. Their gap is not an error to be corrected — it is the most informative object the system produces, and every one of the seven reviews independently identified it as the strongest idea in the design.

Three reviews add a third quantity that the draft conflates with the first: an analyst's **Target Price is a forecast of future market price**, not a claim about value. That distinction buys the work's sharpest dramatic move — an analyst who believes a practice is genuinely valuable *and* forecasts that it will keep falling. Adrian Kessler at a target of 18.50 while the house model reads 34.80 is a coherent position, not a contradiction.

## Time structure

Established by the user: **weekly market, monthly research.** See [[DEC-003-weekly-market-monthly-research]].

```text
CONTINUOUS   Event monitoring — the Event Desk
WEEKLY       Market close, index calculation, Weekly Brief
MONTHLY      Full analyst research: rating, target, conviction, thesis
QUARTERLY    Index constituent review, listing and delisting review
ANNUALLY     THE STATE OF LONGING
```

Weekly closes were chosen over real-time quotes for a stated reason: a price that ticks every second has to be justified with fake volume and a fake order book, whereas `FRIDAY 17:00 UTC` is a research institution reweighing the week. More institutional, less toy.

Monthly research sets the anchor the price moves toward; weekly events move the price around that anchor. Between the two, no human has to re-score anything by hand.

## The macro layer

The user asked for the market equivalent of interest rates, exchange rates, and correlated-asset prices: forces that move a security when nothing about the security itself has changed. The draft answer promotes the [[index-architecture|contrast indicators]] into system-wide macro variables —

```text
EFFICIENCY   AUTOMATION   PREDICTABILITY
MEDIATION    IMMEDIACY    DIGITIZATION   OPTIMIZATION
```

— and gives each security signed exposures to them, so that a week of rising Immediacy drags `LETTER` down with no letter-specific news at all.

**All seven reviews reject this factor set as drafted**, unanimously and on the same ground: the seven series are near-perfectly collinear, so betas become unstable, attribution becomes impossible, and every security ends up moving as one line with decoration. Their consolidations differ in name but not in shape:

| Review | Proposed factor set |
|---|---|
| Gemini | one: `Frictionless Rate` |
| DeepSeek | one: `TIME COMPRESSION` (`MEDIATION` optional second) |
| Kimi | one: `Technological Substitution Intensity` |
| Qwen | two: `Immediacy Rate`, `Mediation / Substitution` |
| Grok | two: `Friction Reduction`, `Uncertainty Compression` |
| Claude | three: `r` Substitution Rate, `q` Friction Premium, `m` Mediation |
| GLM | three: `MEDIATION`, `IMMEDIACY`, `PREDICTABILITY` |

Beneath the naming, the same claim appears seven times: **LONGING needs a discount rate.** The price of obtaining an outcome without the wait, the friction, the body, or the chance is the rate; when it rises, everything whose value is a claim on continued future practice is marked down at once, with no news. Claude and GLM add the second-order concept that makes a rate do real work — **duration**. A handwritten letter is long-duration (almost all of its value sits in the future); a physical photograph is shorter (a large stock of prints already exists); solitude is very long-duration but with *positive* rate sensitivity, because the scarcer unmediated experience becomes, the more it is worth.

Claude's separation is worth keeping visible: a **trending** rate carries the secular story, a **mean-reverting** premium carries the cyclical one. That split is what lets multi-year bull markets live inside a multi-decade decline without any special-case logic.

## The belief layer

Two variables, and the reviews are unanimous that they must stay separate:

- **Consensus** — what the market believes.
- **Positioning** — how much of that belief has already been acted on.

A market can be 91% bearish and still have no marginal seller left. That is exactly when a small positive surprise produces a violent rally, and the rally requires no revival of the practice at all: *too many participants had already bet on its death.* Every review named this the most financially literate idea in the design, and the mechanism is cheap — one asymmetric amplifier that is large when a shock opposes crowded positioning and neutral when it agrees with it. Claude adds the part that makes it self-limiting: a squeeze closes positions, so the rally consumes its own fuel and fails without anyone scripting the failure.

### The contested mechanism

The user's own request was for a model in which a strong enough consensus overrides fundamentals: *"이런것들이 설득력있다고 느끼는 컨센서스가 강해지면 펀더멘털이 무시되면서 시장 가격이 낮아지는 경우도 있는 모델을 반영하고 싶어."* The conversation implemented that as a `Consensus Strength` score gating mean reversion —

```text
Fundamental Pull = Base Mean Reversion × (1 − Consensus Strength)
Consensus Strength = Agreement × Conviction × Evidence Confidence × Track Record
```

— and **all seven reviews reject both halves.** The composite is rejected as pseudo-quantitative: four correlated subjective scores multiplied into a number with no interpretable scale, computed from four analysts and displayed to two decimals. The gate is rejected as a misdescription of markets: strong consensus does not make a fundamental less magnetic, it means **the market has adopted a different fair value and believes the research model is wrong.**

The phenomenon the user asked for is not disputed. Only the mechanism is. Two replacements are on offer:

**Dual anchor** (DeepSeek, GLM, Qwen, Kimi in effect):

```text
Market Anchor = (1 − w) × Research Fair Value + w × Narrative Anchor
price reverts toward the Market Anchor, not toward Fair Value
```

where `w` is a credibility weight. GLM makes `w` earned rather than set: it updates on the *lagged* forecast errors of the house model against the narrative, clipped so the market never fully abandons either. Then "the market believes the fundamental estimate is wrong" is literally `w → 0.05`, with the institution on a recorded losing streak. DeepSeek derives `w` more simply, from analyst target dispersion — converging analysts mean a dominant narrative, disagreeing analysts mean the research anchor holds.

**Limits to arbitrage** (Claude): mispricings persist because nobody is left to take the other side, not because belief is intense.

```text
κ = κ₀ × (1 − |crowding|) × evidence_arrival
```

Both produce the same observable — long persistent gaps, then violent snapbacks — without the circularity of the draft, in which analysts set the anchor *and* set the force that overrides the anchor.

## The event layer

The Event Desk classifies **relevance only**: which conditions and which securities an event touches, at what magnitude and confidence. It never publishes a direction. Direction is left to the analysts, who disagree — one AI handwritten-letter service is proof of substitution risk to Adrian Kessler and proof of persistent demand for the form to Eleanor Vale. This separation survived all seven reviews intact, with two refinements:

- **One event writes to exactly one layer.** It moves a factor, or it moves a security's idiosyncratic fundamental — never both, or the same news is counted twice through the betas. If it genuinely does both, it is two events. GLM's variant is a budget rule: an event's total impact is allocated across channels, never summed.
- **Only the surprise moves price.** The anticipated part is already in the fundamental and already in the price. This requires something to be surprised by, which the draft does not have — see below.
- Magnitude belongs in standard deviations of the target factor, never in points. Confidence should scale **the speed at which an event is priced in, not the size of the move**: high confidence prices in within the week, low confidence bleeds in over several weeks and can reverse if unconfirmed.

## The missing mechanism the reviews agree on

Nothing in the drafted system can surprise anyone. Monthly analyst opinion is commentary, not information, and without a scheduled observable there is nothing for an analyst to be *wrong* about — and being wrong is what generates repricing, credibility, capitulation, and irony.

Claude and GLM converge on the same fix from opposite directions: a **quarterly print of realized incidence** per security — letters written, rolls developed, unarranged visits made — reported with noise and later revised. Analysts forecast it beforehand; the gap between forecast and print is the surprise; the surprise drives the fundamental update. This is the earnings analog, and it arrives with earnings season, forecast scorecards, pre-print positioning, post-print repricing, and a precise job for Mina Seo (behavioral nowcasting: sentiment strong, conversion weak, print after print).

It also gives GLM's return decomposition a home. With incidence as earnings, `Multiple = Price ÷ trailing incidence`, and any move splits into a **flow effect** (incidence changed) and a **re-rating effect** (the multiple changed). That is where the work's bias becomes measurable rather than asserted: if multiple compression persistently exceeds what incidence deterioration justifies, the market is charging a despair premium, and the viewer can read it off the attribution table without being told.

## Attribution

Every reviewer treats the weekly attribution ledger as the credibility-critical surface of the whole product:

```text
LTR   W/W  +31.3%

  RATE (Δr)              +4.1%
  PREMIUM (Δq)          +11.7%
  EVENT                  +6.2%
  SHORT COVERING        +11.4%
  MODEL REVERSION        -2.1%
                        -------
                        +31.3%
```

If the terms sum exactly, double counting becomes structurally impossible and the interface gains its strongest institutional artifact. If there are eight loosely-defined additive terms and seven collinear factors, there will be weeks where the true explanation is "several correlated things partially cancelled," the attribution panel starts lying, and the work loses the one thing it was buying with all this machinery.

## Randomness

The conversation's position was to add no noise at all: every price move should have a traceable cause. The reviews consider full determinism a mistake, but agree with the instinct behind it. The recommended placement is **randomness in the world, not in the price** — stochastic innovations on the macro factors, stochastic timing and magnitude of events, stochastic surprise in the quarterly print. Given the realized world state, pricing stays deterministic and fully attributable. Where noise is added at the price level (GLM, Kimi, Qwen), it is liquidity-scaled and seeded, so any week can be replayed exactly: `seed = hash(seed_file ∥ security_id ∥ ISO_week ∥ model_version)`.

## Fallback if no data can be obtained

The user asked what happens if no external data source can be secured at all. The answer developed in the conversation: do not fabricate numbers that look like measurements. Publish an internal valuation model instead, and be cold about its status.

```text
LONGING RESEARCH
MONTHLY FUNDAMENTALS — LETTER

Presence             28
Scarcity             83
Replacement Risk     91
Cultural Attachment  76

Last Review          31 AUG 2026
Next Review          30 SEP 2026
```

The viewer is meant to ask who decided Scarcity was 83 — and the answer is that credit ratings, ESG scores, and target prices work exactly this way. The factors are the institution's periodic assessment, not measured reality. This structure survives data arriving later: each factor becomes a slot that public statistics can be plugged into (`Presence = 60% postal data + 20% survey + 20% editorial model`) without discarding the architecture.

The reviews mostly push past this list: they consider the seven security-level factors as redundant as the seven macro ones, and would collapse them to expected future practice and its decay rate. GLM goes further — the true condition should be **latent**, never displayed, with the house `F` demoted from ground truth to one contested estimate of it, because a market whose fair value is publicly known is not a market having an argument.

## Evolution — from reduction to identified complexity

**Previous state.** The first review round unanimously rejected the original seven near-collinear modernization factors and recommended a reduced first version with one to three macro factors. That remains the finding of [[model-review-consensus]].

**Transition.** The subsequent Pricing Model v2 framework accepts the collinearity diagnosis and rejects factor count as the design objective. It proposes a large candidate pool and a hierarchy in which visible indicators feed latent factors, factors act through security-specific exposures, and price separates structural change from fundamentals, narrative, positioning, and surprise. A factor survives only when it buys a distinct causal story, cross-sectional loading pattern, event class, time behavior, and attribution line.

Six hash-verified second-round reviews — Claude, DeepSeek, Gemini, GLM, Grok, and Qwen — support that direction and add two constraints, with Qwen dissenting toward reduction rather than classification (see [[factor-architecture-review-consensus]]). First, the candidate pool still mixes structural pressures, valuation regimes, and security-level responses; those layers must be separated before selecting names. Second, the pool is too technology-centric and needs demand-side causes such as available time and attention, spatial and relational conditions, practice infrastructure, cohort transmission, patience, and status.

**Current state.** Complexity is allowed as a working direction, not yet adopted as a specification. Human Substitution and some form of Physicality Displacement survive all six verified reviews, under Qwen's renamings Agency Displacement and Material Decoupling. Time Compression and Uncertainty Compression survive as distinct factors in five of six; Qwen merges both into a single Friction Elimination factor along with Coordination Compression. Mediation remains contested across four positions, including Qwen's, which dissolves it entirely. Coordination is merged, demoted, or delayed by five of six, with only GLM retaining it as a factor. Scarcity is treated as a nonlinear security-level response or absorbed elsewhere by five of six, with only GLM retaining it as a market-wide factor. Exact attribution, pre-registered exposures, and falsification are requirements, but the mathematical method and initial factor count remain open.

## What is settled, what is not

Settled by the user: the weekly/monthly cadence, the need for an event detector, the requirement that consensus be able to override fundamentals, and the secular-decline shape (see [[DEC-004-secular-decline-with-rallies]]).

Not settled: the factor set and its names, which candidates are priced versus displayed only as indicators, how large the security universe must be to support the model, whether `F` is observable or latent, whether the consensus mechanism is a dual anchor or a crowding-limited reversion, whether there is a quarterly print, what a unit of a security is ([[Q-004-unit-of-account]]), and which attribution method to build. See [[model-review-consensus]] and [[factor-architecture-review-consensus]] for the two successive review rounds.

## Related

- [[model-review-consensus]]
- [[factor-architecture-review-consensus]]
- [[data-sources]]
- [[index-architecture]]
- [[analyst-system]]
- [[DEC-003-weekly-market-monthly-research]]
- [[DEC-004-secular-decline-with-rallies]]
- [[Q-001-price-formation]]
- [[Q-004-unit-of-account]]

## Sources

- [[SRC-2026-09-05-price-formation-market-model]] — raw/conversations/2026-09-05-price-formation-market-model.md
- [[SRC-2026-09-05-claude-critic-of-model]] — raw/surveys/2026-09-05-claude-critic-of-model.md
- [[SRC-2026-09-05-deepseek-critic-of-model]] — raw/surveys/2026-09-05-deepseek-critic-of-model.md
- [[SRC-2026-09-05-gemini-critic-of-model]] — raw/surveys/2026-09-05-gemini-critic-of-model.md
- [[SRC-2026-09-05-glm-critic-of-model]] — raw/surveys/2026-09-05-glm-critic-of-model.md
- [[SRC-2026-09-05-grok-critic-of-model]] — raw/surveys/2026-09-05-grok-critic-of-model.md
- [[SRC-2026-09-05-kimi-critic-of-model]] — raw/surveys/2026-09-05-kimi-critic-of-model.md
- [[SRC-2026-09-05-qwen-critic-of-model]] — raw/surveys/2026-09-05-qwen-critic-of-model.md
- [[SRC-2026-09-05-pricing-model-v2-factor-framework]] — raw/conversations/2026-09-05-pricing-model-v2-factor-framework.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-claude]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-claude.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-deepseek]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-deepseek.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-gemini]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-gemini.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-glm]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-glm.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-grok]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-grok.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-qwen]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-qwen.md
