---
status: working
attribution: llm-synthesis
updated: 2026-09-07
sources: []
---

# LONGING Wiki Index

This is the Wiki's working content catalog. Excluding the index itself, every Wiki page appears exactly once under its type using `link + one-line summary + status, when present + updated date`. Do not remove an entry unless its page is deleted. When a page's summary, status, or updated date changes, update this catalog in the same task.

## Routing

| Information to organize | Read or update first |
|---|---|
| Overall definition and central principles of the project | [[overview]] |
| Latest snapshot of decisions, current scope, and priorities | [[current-state]] |
| Design readiness, target world-building depth, and proposed work sequence | [[worldbuilding-roadmap]] |
| Provisional jurisdiction, institutional powers, actors, audience memory, and unit branches | [[world-rules]] |
| LETTER practice boundary, starts/stops, feedback, and no-data effect assumptions | [[letter-practice-dynamics]] |
| An idea that develops across several areas | Relevant `wiki/concepts/` page |
| A choice explicitly decided by the user and its rationale | Relevant `wiki/decisions/` page |
| An unanswered question that remains under review | Relevant `wiki/questions/` page |
| Chronological record of ingestion, queries, linting, and operational changes | Append to [[log]] |
| A new original and its hash or ingestion status | [Raw Source Index](../raw/sources.md) |

Before creating a page, check this catalog to see whether an existing page can be extended. Never classify `llm-proposed` material as a decision without explicit user confirmation.

## Core

- [[overview]] — LONGING as a fictional research house tracking the conditions of human experience modernization is removing · `working` (2026-09-07)
- [[current-state]] — Snapshot of decisions, the world/LETTER drafts, unselected assumptions, and gates before information and price design · `working` (2026-09-07)

## Concepts

- [[worldbuilding-roadmap]] — Design-readiness assessment, handoff provenance, stage 1–2 draft checkpoint, and proposed later dependencies and release gates · `working` (2026-09-07)
- [[world-rules]] — Proposed city/cohort, institutional authority, unit branches, actor knowledge, publication memory, and audience encounter · `working` (2026-09-07)
- [[letter-practice-dynamics]] — Proposed LETTER boundary, episode stocks and send flows, causal conditions, feedback, assumed strengths, and scenario checks · `working` (2026-09-07)

- [[dataset-backtesting-survey]] — 23 dataset families and Kaggle routes mapped to behavior, observation and mechanism tests, with access limits and unconfirmed priorities · `working` (2026-09-07)

- [[academic-model-survey]] — Six model cards, 120-entry discovery map, user directions, and the separate unadopted LETTER application draft · `working` (2026-09-07)

- [[index-architecture]] — LNGI and six condition-based sub-indices, the contrast indicators now promoted to macro variables, and how securities are listed across them · `working` (2026-09-07)
- [[pricing-model]] — Price architecture and failure reviews, now connected to the proposed LETTER state specification and unit-dependent price bridge · `working` (2026-09-07)
- [[model-review-consensus]] — What the first seven independent model reviews agreed to keep, cut, and add, and where they split · `working` (2026-09-07)
- [[factor-architecture-review-consensus]] — What the six verified second-round reviews agree must make a richer factor architecture identifiable, auditable, and falsifiable, where Qwen dissents toward reduction, and the transition to fixed-set failure review · `working` (2026-09-07)
- [[factor-set-failure-profile-review]] — Eight third-round reviews of six fixed sets: conditional failure costs, disagreements, source limitations, and tests proposed but not run · `working` (2026-09-07)
- [[attribution-ledger]] — The weekly decomposition, its three layers, unrouted events, and the distinction between exact accounting and causal recovery · `working` (2026-09-07)
- [[arbitrage]] — Arbitrage as a world-building question, with proposed unit-dependent holdings and the distinction between risky convergence and executable payout discrepancies · `working` (2026-09-07)
- [[information-quality]] — News as reports about events rather than events: misreporting, over- and under-reporting, and rumour ahead of disclosure · `working` (2026-09-07)
- [[data-sources]] — Behavior/attention/discourse separation, candidate sources, and modeled-versus-observed boundaries in the world/LETTER trial · `working` (2026-09-07)
- [[analyst-system]] — Opposed analysts publishing LONG/HOLD/SHORT with targets and conviction, consensus, track records, and the viewer as fifth analyst · `working` (2026-09-07)
- [[system-grammar]] — The series rule shared with OTHER GOODS: human things processed by systems never made for them · `working` (2026-09-07)
- [[prior-art]] — Artistic precedents, three official-page refreshes, and evolution through two academic surveys · `working` (2026-09-07)

## Decisions

- [[DEC-001-project-name-longing]] — The work is titled LONGING with no suffix; rejected name candidates and the outstanding collision check · `confirmed` (2026-09-07)
- [[DEC-002-research-house-form]] — The form is a research house in a terminal register, not a trading app; seven sibling formats deferred · `working` (2026-09-07)
- [[DEC-003-weekly-market-monthly-research]] — Prices strike weekly, formal research publishes monthly and sets the anchor; real-time pricing rejected · `confirmed` (2026-09-07)
- [[DEC-004-secular-decline-with-rallies]] — The market trends down and rallies where a real market crashes; the decline must emerge, never be hard-coded · `confirmed` (2026-09-07)
- [[DEC-005-ledger-resolution-scales-with-universe]] — The weekly ledger starts near nine displayed factors and grows as the security universe grows; a rule, not a set selection, now carrying the user's later position that factors may outnumber securities · `confirmed` (2026-09-07)

## Open Questions

- [[Q-001-price-formation]] — Price architecture with unresolved unit, observation, valuation, and market rules after the world/LETTER draft · `working` (2026-09-07)
- [[Q-002-listing-lifecycle]] — Proposed independent practice, observation, coverage, and listing states, including absence, delisting, and return · `working` (2026-09-07)
- [[Q-003-calibrating-the-bias]] — How far the tilt toward the human can go before the work stops asking and starts arguing · `working` (2026-09-07)
- [[Q-004-unit-of-account]] — Concrete quotation, forecast-claim, and support-entitlement alternatives with price, index, positioning, arbitrage, and artistic consequences · `working` (2026-09-07)

## Activity

- [[log]] — Append-only history of ingestion, queries, linting, decisions, and maintenance (2026-09-07)

## Repository Control

- [README](../README.md) — Entry point describing the project and the repository (2026-09-04)
- [AGENTS](../AGENTS.md) — Task-sized reading, scoped verification, source preservation, institutional Git identity, and standing push authorization (2026-09-07)
- [Schema](../schema.md) — On-demand page structure, attribution, provenance, catalog, and maintenance reference (2026-09-07)
- [Raw README](../raw/README.md) — New-source registration, immutable originals, and targeted lookup guidance (2026-09-07)
- [Raw Source Index](../raw/sources.md) — Source IDs, paths, hashes, ingestion status, and targeted registration/lookup rules (2026-09-07)

## Page Creation Gates

- Create a concept, decision, or question page only when registered source material supports it.
- Do not duplicate a per-source raw catalog here. Use the [Raw Source Index](../raw/sources.md) as the single registry.
- Several pages still rest on a single source. [[overview]], [[system-grammar]], [[prior-art]], [[DEC-001-project-name-longing]], and [[DEC-002-research-house-form]] depend entirely on the 2026-09-04 concept conversation.
- The seven `critic-of-model` surveys are `llm-proposed` throughout. Their agreement is evidence about the model, never a user decision — do not promote a converged recommendation to `confirmed` without the user. The six second-round Pricing Model v2 factor reviews are `llm-proposed` on the same terms; all six (Claude, DeepSeek, Gemini, GLM, Grok, Qwen) are hash-verified and synthesized in [[factor-architecture-review-consensus]]. Qwen's source was re-registered on 2026-09-06 after its first capture was found defective — it ended mid-expression partway through the response — and is now verified under the same source ID.

The eight accepted third-round reviews are synthesized in [[factor-set-failure-profile-review]] with the same `llm-proposed` boundary. No factor set or repair has been selected; initial Gemini coverage was superseded by a separate complete response, and all capture differences are recorded in the raw registry.
