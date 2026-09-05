---
status: working
attribution: llm-proposed
updated: 2026-09-05
sources:
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-deepseek-critic-of-model
  - SRC-2026-09-05-gemini-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
  - SRC-2026-09-05-grok-critic-of-model
  - SRC-2026-09-05-kimi-critic-of-model
  - SRC-2026-09-05-qwen-critic-of-model
---

# Model Review Consensus

On 2026-09-05 the drafted market model was sent to seven language models — Claude, DeepSeek, Gemini, GLM, Grok, Kimi, and Qwen — under one shared review prompt asking for a hostile professional critique in fifteen sections. This page records where the seven independently agreed, where they split, and how much weight their agreement should carry.

**None of this is a user decision.** Everything below is `llm-proposed`. Its value is that seven models working separately from the same brief converged on the same short list of defects, which is stronger evidence than any single review, and weaker than one confirmation from the user.

## Unanimous: keep

Every review, without exception, called these load-bearing and correct:

- **Fundamental Value separate from Market Price.** Named by several as the single best decision in the design. The discount to model is the system's most informative output.
- **Consensus separate from Positioning.** Described as rare in art projects and financially literate: a crowded bearish market can rally violently on a small positive shock, because everyone who was going to sell has already sold.
- **An Event Desk that classifies relevance only**, leaving direction to analysts. Mirrors the real split between news vendors who tag and analysts who interpret.
- **Securities priced first, indices aggregated from them**, with divisor continuity across constituent changes.
- **Refusing to hard-code a negative price drift.** The decline must be reversible in principle or the market is an animation.
- **Weekly market / monthly research cadence.** Matches how sell-side research actually relates to prices.
- **Analyst plurality with the structural bear holding the best record.** Stronger than a single authoritative voice, and the source of the work's irony.

## Unanimous: cut or replace

- **The seven macro factors.** All seven reviews call Automation, Efficiency, Optimization, Predictability, Immediacy, Mediation, and Digitization facets of one underlying force. Kept separate they produce multicollinearity, unstable betas, and unattributable price moves. Collapse to between one and three.
- **The `Consensus Strength` product.** `Agreement × Conviction × Evidence Confidence × Track Record` is rejected by all seven as pseudo-quantitative: correlated inputs multiplied into an uninterpretable scale, computed from four opinions, displayed to two decimals. Several call it the artist's control dial wearing a formula.
- **`κ(1−S)` gating of mean reversion.** Rejected as a misdescription of markets. Strong consensus does not weaken a fundamental's pull; it means the market has adopted a *different* fair value and treats the research model as misspecified.
- **Standalone momentum, fund flow, leverage, forced selling, seasonality, explicit correlation regimes, and reflexivity — out of V1.** Momentum emerges from positioning persistence; fund flow in a money-less market is just Δpositioning; correlation regimes emerge from shared loadings; reflexivity is a positive feedback loop that can crash a security to zero and must be added last, damped, if at all.
- **Analyst Target Price is not Fundamental Value.** A target is a 12-month forecast of *price*. Conflating them destroys the design's best device.

## Unanimous: add

**A discount rate.** Seven for seven. The names differ — Frictionless Rate, Time Compression, Technological Substitution Intensity, Immediacy Rate, Substitution Rate, Friction Discount Rate — and the concept is identical: the cost of obtaining an outcome without the wait, the friction, the body, or the chance. When it rises, everything whose value is a claim on future practice is marked down simultaneously, with no security-specific news.

Claude and GLM extend it with **duration**: how much of a security's value is a claim on continued future practice. This is what generates a cross-section — long-duration securities fall hardest when the rate rises and rally hardest when it falls — and it produces risk-off rotation inside a universe with no obviously defensive asset.

## Where the seven split

| Question | Positions |
|---|---|
| **Number of macro factors** | One (Gemini, DeepSeek, Kimi) · two (Qwen, Grok) · three (Claude, GLM) |
| **Market-cap analogue** | Abandon it, equal-weight (Claude, Kimi, Grok) · build it from prevalence or practice units (Qwen, GLM, DeepSeek) · time allocation (Gemini) |
| **Is `F` observable?** | Displayed estimate, revised at prints (Claude, DeepSeek, Kimi, Qwen) · **latent, never displayed**, with the house number as one contested estimate (GLM) |
| **Consensus replacement** | Dual anchor `M = (1−w)F + wN` (DeepSeek, GLM, Qwen, Kimi) · crowding-limited reversion `κ₀(1−|crowding|)` (Claude) · delete the variable entirely and let positioning do all the work (Gemini) |
| **Price-level noise** | None — put randomness in the world state (Claude) · seeded, liquidity-scaled noise at the price level (GLM, Kimi, Qwen) |
| **Quarterly incidence print** | Essential, the biggest missing mechanism (Claude, GLM) · implied but not foregrounded (DeepSeek, Qwen) · absent (Gemini, Grok, Kimi) |

The market-cap split is the sharpest, and it is a genuine disagreement rather than a difference of emphasis — see [[Q-004-unit-of-account]].

## The three risks, named repeatedly

1. **Over-parameterization.** With eight additive terms and seven collinear factors, a 17% move becomes unexplainable, the attribution panel starts lying, and the "operationally serious" feeling — the entire point of the financial costume — is destroyed.
2. **Circularity.** Analysts set the fundamental, analyst consensus overrides the fundamental, analyst track records are scored against price, and price is driven by consensus. That is one signal split in half fighting itself, and a viewer who reverse-engineers it stops seeing a market and starts seeing an illustration.
3. **The conclusion looking preordained.** If the factor set and the loadings make the decline inevitable, the work's central question is answered before it is asked.

## Defences against looking rigged

Collected across reviews, and unusually concrete:

- **Publish the drift parameter** — one number, with its rationale, in the methodology.
- **Include structural winners.** Claude puts it at 15–25% of the universe with positive or near-zero rate sensitivity: solitude, handmade objects, live performance. Real bear markets have winners, and their existence is what makes a decline informative instead of decreed.
- **Publish a neutral-drift companion index** run on the identical model at zero drift, so anyone can subtract the thesis and see what remains. GLM's variant is a factor-freeze counterfactual.
- **Provenance tags on every displayed number** — `OBSERVED` / `MODELED` / `EDITORIAL`.
- **Pre-register the methodology and parameters** before the year runs, as an index provider does. Outcomes become computations rather than drawings.
- **The model must be able to disagree with the artist.** GLM's test is exact and checkable: film photography and vinyl genuinely revived in the real world, so *if `FILM` cannot stage a multi-year bull market inside the model, the model is rigged.*

## The single most quoted structural idea

Claude's, and it is the one that most directly serves the work rather than the mathematics: publish an **Implied Fundamental** — invert the pricing equation and display the value of `F` that would justify the current price, the way implied volatility is displayed. Then track the house model's realized accuracy, and when it has been persistently wrong, let the institution revise its own fundamental model downward at the annual review, in dry language, with a changelog.

A research desk quietly marking down its own model of human value, on schedule, is the work's thesis executed as a maintenance procedure rather than narrated.

## How to use this page

Treat the unanimous findings as strong evidence and the splits as an open decision set. The reviews are consistent about one meta-point: **the path to a credible V1 is reduction, not expansion.** Every model that named a first change named a collapse — fewer factors, fewer variables, fewer additive terms.

## Related

- [[pricing-model]]
- [[index-architecture]]
- [[analyst-system]]
- [[Q-004-unit-of-account]]
- [[Q-003-calibrating-the-bias]]

## Sources

- [[SRC-2026-09-05-claude-critic-of-model]] — raw/surveys/2026-09-05-claude-critic-of-model.md
- [[SRC-2026-09-05-deepseek-critic-of-model]] — raw/surveys/2026-09-05-deepseek-critic-of-model.md
- [[SRC-2026-09-05-gemini-critic-of-model]] — raw/surveys/2026-09-05-gemini-critic-of-model.md
- [[SRC-2026-09-05-glm-critic-of-model]] — raw/surveys/2026-09-05-glm-critic-of-model.md
- [[SRC-2026-09-05-grok-critic-of-model]] — raw/surveys/2026-09-05-grok-critic-of-model.md
- [[SRC-2026-09-05-kimi-critic-of-model]] — raw/surveys/2026-09-05-kimi-critic-of-model.md
- [[SRC-2026-09-05-qwen-critic-of-model]] — raw/surveys/2026-09-05-qwen-critic-of-model.md

The shared review prompt behind all seven surveys is not registered in this repository. Statements here about what was asked are secondary citations through the surveys themselves.
