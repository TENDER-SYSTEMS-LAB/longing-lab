---
status: working
attribution: llm-synthesis
updated: 2026-09-06
sources: []
---

# LONGING Wiki Index

This is the Wiki's working content catalog. Excluding the index itself, every Wiki page appears exactly once under its type using `link + one-line summary + status, when present + updated date`. Do not remove an entry unless its page is deleted. When a page's summary, status, or updated date changes, update this catalog in the same task.

## Routing

| Information to organize | Read or update first |
|---|---|
| Overall definition and central principles of the project | [[overview]] |
| Latest snapshot of decisions, current scope, and priorities | [[current-state]] |
| An idea that develops across several areas | Relevant `wiki/concepts/` page |
| A choice explicitly decided by the user and its rationale | Relevant `wiki/decisions/` page |
| An unanswered question that remains under review | Relevant `wiki/questions/` page |
| Chronological record of ingestion, queries, linting, and operational changes | Append to [[log]] |
| A new original and its hash or ingestion status | [Raw Source Index](../raw/sources.md) |

Before creating a page, check this catalog to see whether an existing page can be extended. Never classify `llm-proposed` material as a decision without explicit user confirmation.

## Core

- [[overview]] — LONGING as a fictional research house tracking the conditions of human experience modernization is removing · `working` (2026-09-04)
- [[current-state]] — Snapshot of confirmed, working, and unresolved project state after two pricing-model review rounds · `working` (2026-09-06)

## Concepts

- [[index-architecture]] — LNGI and six condition-based sub-indices, the contrast indicators now promoted to macro variables, and how securities are listed across them · `working` (2026-09-06)
- [[pricing-model]] — How a price is produced, including the evolution from a reduced macro layer toward hierarchical, identified complexity · `working` (2026-09-06)
- [[model-review-consensus]] — What the first seven independent model reviews agreed to keep, cut, and add, and where they split · `working` (2026-09-05)
- [[factor-architecture-review-consensus]] — What the six verified second-round reviews agree must make a richer factor architecture identifiable, auditable, and falsifiable, and where Qwen dissents toward reduction · `working` (2026-09-06)
- [[attribution-ledger]] — The weekly published decomposition itself: the worked ledger, its three layers, and what an unrouted event means · `working` (2026-09-06)
- [[data-sources]] — Behavior, attention, and discourse kept apart; candidate real-world sources and the honesty rules that govern them · `working` (2026-09-05)
- [[analyst-system]] — Opposed analysts publishing LONG/HOLD/SHORT with targets and conviction, consensus, track records, and the viewer as fifth analyst · `working` (2026-09-05)
- [[system-grammar]] — The series rule shared with OTHER GOODS: human things processed by systems never made for them · `working` (2026-09-04)
- [[prior-art]] — Comparable works from Benayoun onward and the two rules that keep LONGING distinct · `working` (2026-09-04)

## Decisions

- [[DEC-001-project-name-longing]] — The work is titled LONGING with no suffix; rejected name candidates and the outstanding collision check · `confirmed` (2026-09-04)
- [[DEC-002-research-house-form]] — The form is a research house in a terminal register, not a trading app; seven sibling formats deferred · `working` (2026-09-04)
- [[DEC-003-weekly-market-monthly-research]] — Prices strike weekly, formal research publishes monthly and sets the anchor; real-time pricing rejected · `confirmed` (2026-09-05)
- [[DEC-004-secular-decline-with-rallies]] — The market trends down and rallies where a real market crashes; the decline must emerge, never be hard-coded · `confirmed` (2026-09-05)
- [[DEC-005-ledger-resolution-scales-with-universe]] — The weekly ledger starts near nine displayed factors and grows as the security universe grows; a rule, not a set selection · `confirmed` (2026-09-06)

## Open Questions

- [[Q-001-price-formation]] — Where every price and index value comes from: mechanism now answered in architecture, specification and unit still open · `working` (2026-09-06)
- [[Q-002-listing-lifecycle]] — Who lists a romance, whether scarcity raises or lowers price, and what delisting and relisting mean · `unknown` (2026-09-04)
- [[Q-003-calibrating-the-bias]] — How far the tilt toward the human can go before the work stops asking and starts arguing · `working` (2026-09-05)
- [[Q-004-unit-of-account]] — What one unit of a security is a claim on, and what replaces market capitalization · `unknown` (2026-09-05)

## Activity

- [[log]] — Append-only history of ingestion, queries, linting, decisions, and maintenance (2026-09-06)

## Repository Control

- [README](../README.md) — Entry point describing the project and the repository (2026-09-04)
- [AGENTS](../AGENTS.md) — Reading, language, ingestion, verification, and institutional Git identity rules for agents (2026-09-04)
- [Schema](../schema.md) — Page taxonomy, status, attribution, provenance, language, and maintenance rules (2026-09-04)
- [Raw README](../raw/README.md) — How to add and preserve original source material (2026-09-06)
- [Raw Source Index](../raw/sources.md) — IDs, paths, hashes, and ingestion status for every raw source (2026-09-06)

## Page Creation Gates

- Create a concept, decision, or question page only when registered source material supports it.
- Do not duplicate a per-source raw catalog here. Use the [Raw Source Index](../raw/sources.md) as the single registry.
- Several pages still rest on a single source. [[overview]], [[system-grammar]], [[prior-art]], [[DEC-001-project-name-longing]], and [[DEC-002-research-house-form]] depend entirely on the 2026-09-04 concept conversation.
- The seven `critic-of-model` surveys are `llm-proposed` throughout. Their agreement is evidence about the model, never a user decision — do not promote a converged recommendation to `confirmed` without the user. The six second-round Pricing Model v2 factor reviews are `llm-proposed` on the same terms; all six (Claude, DeepSeek, Gemini, GLM, Grok, Qwen) are hash-verified and synthesized in [[factor-architecture-review-consensus]]. Qwen's source was re-registered on 2026-09-06 after its first capture was found defective — it ended mid-expression partway through the response — and is now verified under the same source ID.
