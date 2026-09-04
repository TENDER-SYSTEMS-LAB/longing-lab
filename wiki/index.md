---
status: working
attribution: llm-synthesis
updated: 2026-09-04
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
- [[current-state]] — Snapshot of what is confirmed, working, and unknown after the first concept conversation · `working` (2026-09-04)

## Concepts

- [[index-architecture]] — LNGI and six condition-based sub-indices, contrast indicators, and how securities are listed across them · `working` (2026-09-04)
- [[analyst-system]] — Opposed analysts publishing LONG/HOLD/SHORT, consensus, track records, and the viewer as fifth analyst · `working` (2026-09-04)
- [[system-grammar]] — The series rule shared with OTHER GOODS: human things processed by systems never made for them · `working` (2026-09-04)
- [[prior-art]] — Comparable works from Benayoun onward and the two rules that keep LONGING distinct · `working` (2026-09-04)

## Decisions

- [[DEC-001-project-name-longing]] — The work is titled LONGING with no suffix; rejected name candidates and the outstanding collision check · `confirmed` (2026-09-04)
- [[DEC-002-research-house-form]] — The form is a research house in a terminal register, not a trading app; seven sibling formats deferred · `working` (2026-09-04)

## Open Questions

- [[Q-001-price-formation]] — Where every price and index value comes from: mechanism, data basis, unit · `unknown` (2026-09-04)
- [[Q-002-listing-lifecycle]] — Who lists a romance, whether scarcity raises or lowers price, and what delisting and relisting mean · `unknown` (2026-09-04)
- [[Q-003-calibrating-the-bias]] — How far the tilt toward the human can go before the work stops asking and starts arguing · `working` (2026-09-04)

## Activity

- [[log]] — Append-only history of ingestion, queries, linting, decisions, and maintenance (2026-09-04)

## Repository Control

- [README](../README.md) — Entry point describing the project and the repository (2026-09-04)
- [AGENTS](../AGENTS.md) — Reading, language, ingestion, verification, and institutional Git identity rules for agents (2026-09-04)
- [Schema](../schema.md) — Page taxonomy, status, attribution, provenance, language, and maintenance rules (2026-09-04)
- [Raw README](../raw/README.md) — How to add and preserve original source material (2026-09-04)
- [Raw Source Index](../raw/sources.md) — IDs, paths, hashes, and ingestion status for every raw source (2026-09-04)

## Page Creation Gates

- Create a concept, decision, or question page only when registered source material supports it.
- Do not duplicate a per-source raw catalog here. Use the [Raw Source Index](../raw/sources.md) as the single registry.
- Every page currently in this catalog rests on a single source. Watch for that dependency when new material arrives.
