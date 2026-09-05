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

# Q-001 — How is a price determined?

## The question

LONGING's entire surface rests on numbers: `LETTER 27.43 +0.82%`, `LNGI 42.81 −1.93%`, a consensus target of 29.81. Nothing in the source conversation settles where any of those numbers come from.

Three sub-questions, all open:

1. **Mechanism.** What moves a price? A market simulation, a published formula over real-world indicators, editorial authorship, or viewer participation?
2. **Data basis.** Are the underlying series invented, or derived from real data (search volume, postal statistics, survey figures, usage rates)? Report copy in the source cites concrete-sounding figures — *unplanned visits −8.2% YoY*, *average reply latency −18.1%*, *physical photographs −12.7%* — without saying whether such numbers would be sourced or fabricated.
3. **Unit.** A draft security page reads `27.43 KRW(?)`. The currency, or whether there is one at all, is unresolved.

## What is settled

**Participant votes must not be the price.** Viewer positions are displayed as their own aggregate (LONG 61.8% / HOLD 24.1% / SHORT 14.1%, 12,481 participants), and the price is produced by a separate mechanism. The reason is stated: a 90% LONG majority can be outweighed by a few far stronger SHORT convictions, and if the work borrows the metaphor of a real market it should carry that with it — **conviction size moves price, not headcount.**

**The institution does not explain the price.** It prints 27.43 and says nothing about why. Explanation belongs to the analysts, who disagree. See [[analyst-system]].

## Why it matters

The price is the work's only verdict. Everything else — reports, indices, the archive — is argument arranged around one number. How that number is produced decides whether LONGING is an authored fiction, a data visualization, or a participatory system, and those are three different works.

It also gates the index methodology: [[index-architecture]] cannot publish a composition or a formula for LNGI and its six sub-indices until this is answered.

## Evolution

**Previous state (2026-09-04).** Nothing was settled beyond two negative rules: participant votes are not the price, and the institution does not explain the price. Mechanism, data basis, and unit were all open, and the question was blocking [[index-architecture]].

**Transition (2026-09-05).** A conversation dedicated to this question produced a full market architecture, and that architecture was then reviewed by seven language models on the same day. The mechanism question is now answered in shape if not in parameters; the data question moved from open to *deliberately optional*; the unit question split in two and got worse.

**Current state.** The three sub-questions no longer have equal status.

1. **Mechanism — answered in architecture, open in specification.** A price is produced by a market engine, not by an author and not by a vote. Fundamental Value and Market Price are separate numbers; monthly analyst research sets an anchor; weekly events move price around it; macro-like structural factors push whole groups of securities with no security-specific news; crowded positioning produces asymmetric rallies. See [[pricing-model]]. What remains open is which specification to build: seven reviews agreed on the architecture and differed on nearly every parameter, factor name, and variable count. See [[model-review-consensus]].

2. **Data basis — no longer blocking.** The work can ship either on real-world data or on a published internal valuation model, and the architecture was deliberately designed so that data arriving later slots into factors that already exist. What is settled is the honesty rule rather than the choice: never fabricate a number that looks like a measurement, and tag every displayed value `OBSERVED` / `MODELED` / `EDITORIAL`. See [[data-sources]].

3. **Unit — worse than before, and now its own question.** The original form was about currency (`27.43 KRW(?)`). The reviews reframed it: before asking what the number is denominated in, the work must say what one *unit* of a security is a claim on, because index weighting, market capitalization, float, and short interest all depend on it. That is now [[Q-004-unit-of-account]], and it is the sharpest disagreement in the entire review set.

Also settled here by the user, and recorded as decisions rather than answers to this question: the weekly/monthly cadence ([[DEC-003-weekly-market-monthly-research]]) and the secular decline with inverted rallies ([[DEC-004-secular-decline-with-rallies]]).

**Second round (2026-09-05).** Sub-question 1, Mechanism, is the one that moves again. It stood "answered in architecture, open in specification," where the open part was which of seven reduced V1 specifications to build. The second round changes the shape of that opening rather than closing it. A working framework rejected minimal factor count as the design goal and proposed instead that complexity may return through a hierarchy: observable indicators feed latent structural factors, factors act through security-specific exposures, and price separates structural change from practice fundamentals, narrative, positioning, and event surprise. Six hash-verified reviews — Claude, DeepSeek, Gemini, GLM, Grok, and Qwen — support that reframing, with Qwen dissenting toward reduction: it collapses the candidate pool to five core factors on parsimony grounds rather than adopting classification as the remedy. See [[factor-architecture-review-consensus]]. The specification question is therefore no longer "which reduced V1"; it is which factors are priced and which stay research indicators, how many constituents the exposure matrix needs before a given factor count is identifiable at all, and which exact-attribution method carries interactions and correlations. This is `llm-proposed` and `llm-synthesis` throughout — the framework is a working proposal and the reviews are review material, not a decision.

## What is still unanswered

- Which V1 specification to adopt — the factor set, whether Fundamental Value is displayed or latent, and whether the consensus mechanism is a dual anchor or a crowding-limited reversion. The second round reframes rather than settles this: see [[factor-architecture-review-consensus]].
- Whether there is a quarterly observable for analysts to be wrong about. Two reviews call its absence the largest remaining gap in the design: with nothing scheduled to be surprised by, monthly analyst opinion is commentary rather than information.
- The constituent-count constraint on specification. Two of six verified second-round reviews (Claude and Grok) argue that the eleven-security reference set cannot identify a large factor model and propose expanding the universe to roughly 40–60 practices — including practices in genuine secular expansion — before pricing the full set. This bears on [[Q-002-listing-lifecycle]], since it is a claim about which practices get listed, not only about how many factors can be priced.
- The unit and the currency.
- The flagship index formula, which still waits on [[Q-004-unit-of-account]] rather than on this page.

## Related

- [[pricing-model]]
- [[model-review-consensus]]
- [[data-sources]]
- [[index-architecture]]
- [[analyst-system]]
- [[DEC-003-weekly-market-monthly-research]]
- [[DEC-004-secular-decline-with-rallies]]
- [[Q-002-listing-lifecycle]]
- [[Q-004-unit-of-account]]
- [[factor-architecture-review-consensus]]

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
