---
status: working
attribution: jointly-developed
updated: 2026-09-06
sources:
  - SRC-2026-09-06-cross-domain-model-survey
  - SRC-2026-09-06-dataset-backtesting-research
  - SRC-2026-09-06-academic-model-research-notes
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
  - SRC-2026-09-06-attribution-resolution-and-universe-scaling
  - SRC-2026-09-06-arbitrage-news-quality-and-next-work-items
  - SRC-2026-09-06-factor-set-failure-profile-prompt-v2
  - SRC-2026-09-06-factor-set-failure-profile-chatgpt
  - SRC-2026-09-06-factor-set-failure-profile-glm
---

# Current State

The source registry is maintained in `raw/sources.md`. Two additional sources preserve the exact broad-survey request and a 120-entry cross-domain discovery catalog; they add research coverage, not a model decision. The dataset research source records the initial dataset-backtesting survey: 23 dataset families, six Kaggle routes, access limits and proposed component tests; no dataset was downloaded or fitted. Two added sources record the initial academic-model survey and its compiled task brief. The promoted corpus includes the first two review rounds and their working conversations, two separate 2026-09-06 user-position records, and the completed third round: eight accepted reviews, two prompt versions, and a collection follow-up record. Gemini's first third-round response remains raw-only because it omitted required event coverage; its separately preserved complete replacement is used in the synthesis. The earlier second-round Qwen capture correction remains documented in `raw/sources.md` and `wiki/log.md`.

The third round maps the costs of six fixed factor sets without choosing one. It adds conditional event and attribution hypotheses, disputed artistic costs, and proposed tests; no simulation or exposure-matrix result has been established. See [[factor-set-failure-profile-review]].

The project has moved from *how does the market inside it run* to *how can its factor architecture become rich without becoming causally redundant or theatrically precise*, and now also has a settled rule for how the audience-facing ledger's resolution grows alongside that architecture.

## Confirmed

- **The work is named LONGING**, capitals, no suffix. See [[DEC-001-project-name-longing]].
- **The work is a fictional independent research house**, not a trading app. See [[DEC-002-research-house-form]].
- **The subject is the conditions of human experience that modernization is removing** — not "romance" as a category. See [[overview]].
- **The system never argues.** It publishes numbers and reports; opposed views settle into a price; emotion happens in the viewer.
- **Weekly market, monthly research.** Prices strike weekly; formal analyst research publishes monthly and sets the anchor the market moves toward. Real-time pricing was rejected because it would require fabricated volume and a fabricated order book. See [[DEC-003-weekly-market-monthly-research]].
- **An event detector is required.** If prices move weekly and research lands monthly, something has to supply information in between. Stated by the user as a requirement.
- **LONGING is a secular bear market with inverted rallies.** The user's own position — romance is genuinely disappearing — so the market trends down, and where a real market has crashes this one has melt-ups. See [[DEC-004-secular-decline-with-rallies]].
- **The decline must not be hard-coded.** It has to fall out of structural forces the model publishes, so the work says *"calculated against the world's current direction, it keeps falling"* rather than *"romance must die."*
- **Ledger resolution scales with the security universe.** The weekly attribution ledger starts near nine displayed factors, and the number of displayed lines grows as the security universe grows — a rule governing how the factor count behaves, not a selection of which factors those are. See [[DEC-005-ledger-resolution-scales-with-universe]].

## Working

- **The market architecture.** Fundamental Value and Market Price as two displayed numbers whose gap is the system's most informative output; monthly research setting an anchor; weekly events moving price around it; macro-like structural factors moving whole groups of securities with no security-specific news; consensus and positioning as separate variables, so a crowded bearish market can rally violently on a small positive shock. See [[pricing-model]].
- **The first seven-model review.** Where seven independent reviews converged, and where they split. Their unanimous verdict was that the path to a credible V1 is *reduction*: collapse the original macro factors, delete the consensus composite, and remove excess market machinery from the first version. See [[model-review-consensus]].
- **The factor architecture has entered a second working phase.** The new framework accepts the first review's collinearity diagnosis but rejects minimal factor count as the goal. Complexity may return only through a hierarchy of observables, structurally identified factors, security-specific fundamentals, valuation regimes, and positioning. Six verified second-round reviews support the reframing while disagreeing on the final factor set; Qwen dissents toward reduction, collapsing the candidate pool to five core factors on parsimony grounds. See [[factor-architecture-review-consensus]].
- **The third failure-profile round is collected and ingested.** Eight complete reviews compare A–F on the fixed eleven-security exercise. The synthesis distinguishes accounting from identification, retains conflicting mispricing directions, and qualifies claims that overlook fundamentals or positioning. No preferred architecture, repair, or new confirmed decision results. See [[factor-set-failure-profile-review]].
- **Data layering.** Behavior, attention, and discourse kept strictly apart rather than blended into one score — the separation is what produces the work's central paradox, that people talk about letters more and write fewer of them. No source has been secured. See [[data-sources]].
- **Index architecture**, with the contrast indicators now promoted from display elements to macro variables carrying signed exposures. The promotion is accepted in principle; the seven-factor set is rejected by every review. See [[index-architecture]].
- **Analyst system**, now mechanically load-bearing: targets, conviction-weighted consensus, credibility scored on the record. See [[analyst-system]].
- **Series grammar** shared with OTHER GOODS: *Unownable → Goods* there, *Unquantifiable → Price* here. See [[system-grammar]].
- **A quiet bias toward the human, expressed structurally.** Now with checkable tests attached: publish the drift parameter, keep structural winners in the universe, publish a neutral-drift companion index, and ensure the model can disagree with its author. See [[Q-003-calibrating-the-bias]].
- **Securities are behaviors and situations, never abstract emotions** — the deliberate break from *Emotional Stock Exchange*. See [[prior-art]].
- **The attribution ledger as its own object.** The audience-facing weekly decomposition — factor lines, security fundamentals, positioning, and what an unrouted event means — is now developed independently of the factor architecture that feeds it. See [[attribution-ledger]].
- **Factors abstract but numerous, with the universe grown to match.** The user's stated position is that events the factor vocabulary cannot carry should not occur at all, and that the way to achieve this is abstract factors in larger number, with the security count raised to support them. This bears directly on the deferred universe-expansion question and on [[Q-002-listing-lifecycle]], since it makes which practices get listed a precondition for which factors can exist rather than a consequence of them. Recorded as `user-originated` and `working`: a stated direction, not a specified mechanism, and the assistant's qualifications to it — that raising the count need not raise the diversity of exposure the model needs — are `llm-proposed`. Sharpened later the same day: the user stated that **factors may outnumber securities**, rejecting the working ratio `K ≤ N/3`, and gave the ordering conclusion as the reason — the binding constraint is whether the listed universe can express a factor, not how the two counts compare. Both are to be carried into the next review round as stated context. See [[attribution-ledger]] and [[DEC-005-ledger-resolution-scales-with-universe]].
- **Arbitrage as a world-building element.** The user's stated interest is both in arbitrage as a market mechanism and in what it turns out to *be* inside a market whose securities are human practices. The corpus already holds limits to arbitrage — Claude's crowding-scaled `κ` — but nothing that depicts an arbitrageur, names a counterparty, or says what holding a position costs. Recorded as `user-originated` and `working`; no mechanism was proposed by either party. It gives [[Q-004-unit-of-account]] a second dependant, since a position needs something finite to hold. See [[arbitrage]].
- **News quality as a modelled layer.** The user's position is that the event layer models facts arriving while real news also misreports, over- and under-reports, and leaks ahead of disclosure. Misreporting and pre-circulating rumour have no representation anywhere in the corpus; the existing confidence rule models uncertainty about an event that is nonetheless true. Recorded as `user-originated` and `working`; no mechanism was proposed. See [[information-quality]].
- **Deliberately provoking `Unexplained` during design.** The user's stated intent is to find as many unattributable events as possible while the work is still being designed, in order to discover which of them are factors worth promoting — a design-stage instrument, not (yet) a display decision. Recorded as `user-originated` and `working`, since the mechanism for doing this is still `llm-proposed`. See [[attribution-ledger]].

- **Cross-domain model discovery.** The later academic pass collected 120 works/projects: 117 substantive systems, one bibliographic lead, and two adjacent data mappings. It covers social behavior, designed institutions, natural systems, engineering, music, and art, with one-sentence targets and source links. It is not a full-text review, validation exercise, or adopted LONGING architecture. See [[academic-model-survey]].

## Unknown

- **Which specification to build.** The first review round differed on nearly every parameter; the second expands the choice into which factors are priced, which remain indicators, how many constituents are needed to support them, and how exact attribution handles interaction and correlation. Ledger *resolution* is no longer open in this list — it is settled as a rule, factor count as a function of universe size, see [[DEC-005-ledger-resolution-scales-with-universe]] — but ledger *membership*, which specific factors fill the starting nine and which candidate is promoted next, remains exactly as open as the rest of this bullet. See [[model-review-consensus]] and [[factor-architecture-review-consensus]].
- **What one unit of a security is.** Blocks index weighting, the market-capitalization analogue, float, and short interest. The sharpest disagreement in the review set: refuse the unit and weight equally, or define practice units and accept the fiction. Still unresolved, but no longer only carried: the user has directed that it be put to the review models as its own round. See [[Q-004-unit-of-account]].
- **Whether there is a periodic observable.** Nothing in the current design can surprise anyone, and two reviews call this the largest remaining gap: without something scheduled to be wrong about, monthly analyst opinion is commentary rather than information.
- **Whether the work ships on real data at all.** Both paths remain open, and the architecture was built so either works. See [[data-sources]].
- **Listing lifecycle**: who lists, whether scarcity raises or lowers price, delisting, where a delisted romance goes, whether one person resuming a practice relists it. See [[Q-002-listing-lifecycle]].
- **How far the bias may go** before the work stops asking and starts arguing. See [[Q-003-calibrating-the-bias]].
- **Flagship index ticker** (`LNGI` / `LX` / `LCI`), the security-code scheme, and the currency.
- **Trademark, domain, and existing-work collision check on the name LONGING** — planned in the first conversation, never carried out.
- **Medium and delivery**: mobile-first was the starting assumption; no platform, technology, or exhibition context has been decided.

## Next steps proposed in the sources

The 2026-09-05 conversation opened by proposing this order: price formation → listing lifecycle → complete `LETTER` as a single reference security → index methodology → the first home and security screens → expand the universe. Price formation has since been worked through in architecture. The first review round recommended removing before building; the second says complexity may be restored after causal identification, and one review (Claude) argues that the security universe must expand before a large factor model can be identified.

Building one security completely — rather than sketching thirty — remains the standing proposal for what comes next. It is `llm-proposed`; the user has not confirmed an order.

Three work items set by the user on 2026-09-06, `user-originated`; the initial academic survey is now recorded, with remaining gaps below. This completed failure-profile collection uses the previously registered prompts; it does not cover the separate unit review or academic survey, and those prompts do not explicitly carry the later factor-count positions:

1. **Put [[Q-004-unit-of-account]] to the review models** as its own round, in the way the pricing model and the factor architecture were.
2. **Carry two positions into the next modelling round as stated context** — that factors may outnumber securities, and that listing choice determines which factors can exist. See [[DEC-005-ledger-resolution-scales-with-universe]].
3. **Survey academic prior art.** A first pass is complete in [[academic-model-survey]]: six explicit models and a mechanism-identification critique, with primary references and estimated versus assumed values. All applications remain LLM proposals. Cultural transmission, infrastructure retirement, chance encounters, contested value, and index measurement remain literature gaps; no factor set or price bridge is adopted.

An initial dataset investigation requested by the user is now recorded in [[dataset-backtesting-survey]]. Collection priorities and experimental designs remain LLM proposals. The survey distinguishes behavior validation, observation-layer checks and external mechanism benchmarks from an empirical LONGING price backtest; the price unit and valuation bridge remain unresolved.

## Deferred

Seven sibling formats built on the same grammar — an abolished-jobs recruitment site, a government-style romance white paper, a cold-storage memory archive, Romance as a Service, parcel tracking, a social network of moments, and the archive of a radio station that never existed. Recorded as possible future works, not as parts of LONGING. See [[DEC-002-research-house-form]].

Explicitly deferred inside the market model, on unanimous review advice: reflexivity, leverage and forced selling, correlation-regime switching, seasonality, stochastic volatility, and an options-style volatility index.

## Provenance warnings

**The third round has capture and framing differences.** ChatGPT uses v1; the other seven use v2. Gemini's incomplete-coverage original is superseded for synthesis by a separate complete response. Qwen and Kimi were rewritten after truncation, and Kimi displayed an automatic K2.6 Instant fallback despite an unchanged selected mode. Detailed provenance is in `raw/sources.md`. Review agreement remains a hypothesis, not measured validation or a user decision.

**Single-source dependency has partly eased, and not everywhere.** [[overview]], [[system-grammar]], [[DEC-001-project-name-longing]], and [[DEC-002-research-house-form]] still depend on the first conversation. Claims about OTHER GOODS remain conversation-derived. [[prior-art]] now also draws on both academic surveys: official descriptions of three market artworks were checked in the broad pass, while the remaining historic details and comparative interpretations retain their stated provenance limits.

**The review prompt is not registered.** The seven surveys respond to `LONGING_market_pricing_model_review_prompt.md`, which is not in `raw/`. Everything the surveys say about what was asked is a secondary citation.

**Seven agreeing models are not a decision.** The review material is `llm-proposed` throughout. Convergence across seven independent reviews is strong evidence about the model's defects and no evidence at all about what the user wants.

**The second-round Qwen source was re-captured, not revised.** Its first registration ended mid-expression; the current file is the complete response, registered under the same source ID with the superseded hash retained in `raw/sources.md` and the correction recorded in `wiki/log.md`.

## Sources

- [[SRC-2026-09-06-cross-domain-model-survey]] — raw/surveys/2026-09-06-cross-domain-model-survey.md; original discovery catalog based on linked external sources

- [[SRC-2026-09-06-dataset-backtesting-research]] — raw/surveys/2026-09-06-dataset-backtesting-research.md

- [[SRC-2026-09-06-academic-model-research-notes]] — raw/surveys/2026-09-06-academic-model-research-notes.md

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
- [[SRC-2026-09-06-attribution-resolution-and-universe-scaling]] — raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md
- [[SRC-2026-09-06-arbitrage-news-quality-and-next-work-items]] — raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md
- [[SRC-2026-09-06-factor-set-failure-profile-prompt-v2]] — raw/documents/2026-09-06-factor-set-failure-profile-prompt-v2.md
- [[SRC-2026-09-06-factor-set-failure-profile-chatgpt]] — raw/surveys/2026-09-06-factor-set-failure-profile-chatgpt.md
- [[SRC-2026-09-06-factor-set-failure-profile-glm]] — raw/surveys/2026-09-06-factor-set-failure-profile-glm.md
