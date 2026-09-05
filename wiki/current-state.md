---
status: working
attribution: jointly-developed
updated: 2026-09-06
sources:
  - SRC-2026-09-04-longing-concept-brainstorm
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-05-claude-critic-of-model
  - SRC-2026-09-05-deepseek-critic-of-model
  - SRC-2026-09-05-gemini-critic-of-model
  - SRC-2026-09-05-glm-critic-of-model
  - SRC-2026-09-05-grok-critic-of-model
  - SRC-2026-09-05-kimi-critic-of-model
  - SRC-2026-09-05-qwen-critic-of-model
  - SRC-2026-09-05-pricing-model-v2-factor-framework
  - SRC-2026-09-05-pricing-model-v2-factor-review-prompt
  - SRC-2026-09-05-pricing-model-v2-factor-review-claude
  - SRC-2026-09-05-pricing-model-v2-factor-review-deepseek
  - SRC-2026-09-05-pricing-model-v2-factor-review-gemini
  - SRC-2026-09-05-pricing-model-v2-factor-review-glm
  - SRC-2026-09-05-pricing-model-v2-factor-review-grok
  - SRC-2026-09-05-pricing-model-v2-factor-review-qwen
---

# Current State

Seventeen sources are registered. The first nine established the concept, built the initial market model, and subjected that model to seven independent reviews. Eight newer files comprise a working factor-framework conversation, its registered review prompt, and six second-round model responses. All six responses are verified and promoted into the Wiki. Qwen's response required a re-capture on 2026-09-06: its first registration was a defective capture that ended mid-expression partway through the response, and the user replaced it with the complete response — a capture correction rather than a change to the evidence, recorded in `raw/sources.md` and in `wiki/log.md`.

The project has moved from *how does the market inside it run* to *how can its factor architecture become rich without becoming causally redundant or theatrically precise*.

## Confirmed

- **The work is named LONGING**, capitals, no suffix. See [[DEC-001-project-name-longing]].
- **The work is a fictional independent research house**, not a trading app. See [[DEC-002-research-house-form]].
- **The subject is the conditions of human experience that modernization is removing** — not "romance" as a category. See [[overview]].
- **The system never argues.** It publishes numbers and reports; opposed views settle into a price; emotion happens in the viewer.
- **Weekly market, monthly research.** Prices strike weekly; formal analyst research publishes monthly and sets the anchor the market moves toward. Real-time pricing was rejected because it would require fabricated volume and a fabricated order book. See [[DEC-003-weekly-market-monthly-research]].
- **An event detector is required.** If prices move weekly and research lands monthly, something has to supply information in between. Stated by the user as a requirement.
- **LONGING is a secular bear market with inverted rallies.** The user's own position — romance is genuinely disappearing — so the market trends down, and where a real market has crashes this one has melt-ups. See [[DEC-004-secular-decline-with-rallies]].
- **The decline must not be hard-coded.** It has to fall out of structural forces the model publishes, so the work says *"calculated against the world's current direction, it keeps falling"* rather than *"romance must die."*

## Working

- **The market architecture.** Fundamental Value and Market Price as two displayed numbers whose gap is the system's most informative output; monthly research setting an anchor; weekly events moving price around it; macro-like structural factors moving whole groups of securities with no security-specific news; consensus and positioning as separate variables, so a crowded bearish market can rally violently on a small positive shock. See [[pricing-model]].
- **The first seven-model review.** Where seven independent reviews converged, and where they split. Their unanimous verdict was that the path to a credible V1 is *reduction*: collapse the original macro factors, delete the consensus composite, and remove excess market machinery from the first version. See [[model-review-consensus]].
- **The factor architecture has entered a second working phase.** The new framework accepts the first review's collinearity diagnosis but rejects minimal factor count as the goal. Complexity may return only through a hierarchy of observables, structurally identified factors, security-specific fundamentals, valuation regimes, and positioning. Six verified second-round reviews support the reframing while disagreeing on the final factor set; Qwen dissents toward reduction, collapsing the candidate pool to five core factors on parsimony grounds. See [[factor-architecture-review-consensus]].
- **Data layering.** Behavior, attention, and discourse kept strictly apart rather than blended into one score — the separation is what produces the work's central paradox, that people talk about letters more and write fewer of them. No source has been secured. See [[data-sources]].
- **Index architecture**, with the contrast indicators now promoted from display elements to macro variables carrying signed exposures. The promotion is accepted in principle; the seven-factor set is rejected by every review. See [[index-architecture]].
- **Analyst system**, now mechanically load-bearing: targets, conviction-weighted consensus, credibility scored on the record. See [[analyst-system]].
- **Series grammar** shared with OTHER GOODS: *Unownable → Goods* there, *Unquantifiable → Price* here. See [[system-grammar]].
- **A quiet bias toward the human, expressed structurally.** Now with checkable tests attached: publish the drift parameter, keep structural winners in the universe, publish a neutral-drift companion index, and ensure the model can disagree with its author. See [[Q-003-calibrating-the-bias]].
- **Securities are behaviors and situations, never abstract emotions** — the deliberate break from *Emotional Stock Exchange*. See [[prior-art]].

## Unknown

- **Which specification to build.** The first review round differed on nearly every parameter; the second expands the choice into which factors are priced, which remain indicators, how many constituents are needed to support them, and how exact attribution handles interaction and correlation. See [[model-review-consensus]] and [[factor-architecture-review-consensus]].
- **What one unit of a security is.** Blocks index weighting, the market-capitalization analogue, float, and short interest. The sharpest disagreement in the review set: refuse the unit and weight equally, or define practice units and accept the fiction. See [[Q-004-unit-of-account]].
- **Whether there is a periodic observable.** Nothing in the current design can surprise anyone, and two reviews call this the largest remaining gap: without something scheduled to be wrong about, monthly analyst opinion is commentary rather than information.
- **Whether the work ships on real data at all.** Both paths remain open, and the architecture was built so either works. See [[data-sources]].
- **Listing lifecycle**: who lists, whether scarcity raises or lowers price, delisting, where a delisted romance goes, whether one person resuming a practice relists it. See [[Q-002-listing-lifecycle]].
- **How far the bias may go** before the work stops asking and starts arguing. See [[Q-003-calibrating-the-bias]].
- **Flagship index ticker** (`LNGI` / `LX` / `LCI`), the security-code scheme, and the currency.
- **Trademark, domain, and existing-work collision check on the name LONGING** — planned in the first conversation, never carried out.
- **Medium and delivery**: mobile-first was the starting assumption; no platform, technology, or exhibition context has been decided.

## Next steps proposed in the sources

The 2026-09-05 conversation opened by proposing this order: price formation → listing lifecycle → complete `LETTER` as a single reference security → index methodology → the first home and security screens → expand the universe. Price formation has since been worked through in architecture. The first review round recommended removing before building; the second says complexity may be restored after causal identification, and two reviews argue that the security universe must expand before a large factor model can be identified.

Building one security completely — rather than sketching thirty — remains the standing proposal for what comes next. It is `llm-proposed`; the user has not confirmed an order.

## Deferred

Seven sibling formats built on the same grammar — an abolished-jobs recruitment site, a government-style romance white paper, a cold-storage memory archive, Romance as a Service, parcel tracking, a social network of moments, and the archive of a radio station that never existed. Recorded as possible future works, not as parts of LONGING. See [[DEC-002-research-house-form]].

Explicitly deferred inside the market model, on unanimous review advice: reflexivity, leverage and forced selling, correlation-regime switching, seasonality, stochastic volatility, and an options-style volatility index.

## Provenance warnings

**Single-source dependency has partly eased, and not everywhere.** [[overview]], [[system-grammar]], [[prior-art]], [[DEC-001-project-name-longing]], and [[DEC-002-research-house-form]] still rest entirely on the first conversation. All claims about OTHER GOODS and every comparable work in [[prior-art]] reach this repository only through it and remain unverified here.

**The review prompt is not registered.** The seven surveys respond to `LONGING_market_pricing_model_review_prompt.md`, which is not in `raw/`. Everything the surveys say about what was asked is a secondary citation.

**Seven agreeing models are not a decision.** The review material is `llm-proposed` throughout. Convergence across seven independent reviews is strong evidence about the model's defects and no evidence at all about what the user wants.

**The second-round Qwen source was re-captured, not revised.** Its first registration ended mid-expression; the current file is the complete response, registered under the same source ID with the superseded hash retained in `raw/sources.md` and the correction recorded in `wiki/log.md`.

## Sources

- [[SRC-2026-09-04-longing-concept-brainstorm]] — raw/conversations/2026-09-04-longing-concept-brainstorm.md
- [[SRC-2026-09-05-price-formation-market-model]] — raw/conversations/2026-09-05-price-formation-market-model.md
- [[SRC-2026-09-05-claude-critic-of-model]] — raw/surveys/2026-09-05-claude-critic-of-model.md
- [[SRC-2026-09-05-deepseek-critic-of-model]] — raw/surveys/2026-09-05-deepseek-critic-of-model.md
- [[SRC-2026-09-05-gemini-critic-of-model]] — raw/surveys/2026-09-05-gemini-critic-of-model.md
- [[SRC-2026-09-05-glm-critic-of-model]] — raw/surveys/2026-09-05-glm-critic-of-model.md
- [[SRC-2026-09-05-grok-critic-of-model]] — raw/surveys/2026-09-05-grok-critic-of-model.md
- [[SRC-2026-09-05-kimi-critic-of-model]] — raw/surveys/2026-09-05-kimi-critic-of-model.md
- [[SRC-2026-09-05-qwen-critic-of-model]] — raw/surveys/2026-09-05-qwen-critic-of-model.md
- [[SRC-2026-09-05-pricing-model-v2-factor-framework]] — raw/conversations/2026-09-05-pricing-model-v2-factor-framework.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-prompt]] — raw/documents/2026-09-05-pricing-model-v2-factor-review-prompt.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-claude]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-claude.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-deepseek]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-deepseek.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-gemini]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-gemini.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-glm]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-glm.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-grok]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-grok.md
- [[SRC-2026-09-05-pricing-model-v2-factor-review-qwen]] — raw/surveys/2026-09-05-pricing-model-v2-factor-review-qwen.md
