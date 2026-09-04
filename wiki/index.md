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

- [[overview]] — Definition, identity, and central question of the project; not yet established · `unknown` (2026-09-04)
- [[current-state]] — Snapshot of what is confirmed, in progress, and unknown; currently empty · `unknown` (2026-09-04)

## Concepts

No pages yet.

## Decisions

No pages yet.

## Open Questions

No pages yet.

## Activity

- [[log]] — Append-only history of ingestion, queries, linting, decisions, and maintenance (2026-09-04)

## Repository Control

- [README](../README.md) — Entry point describing the project and the repository (2026-09-04)
- [AGENTS](../AGENTS.md) — Reading, language, ingestion, verification, and institutional Git identity rules for agents (2026-09-04)
- [Schema](../schema.md) — Page taxonomy, status, attribution, provenance, language, and maintenance rules (2026-09-04)
- [Raw README](../raw/README.md) — How to add and preserve original source material (2026-09-04)
- [Raw Source Index](../raw/sources.md) — IDs, paths, hashes, and ingestion status for every raw source (2026-09-04)

## Page Creation Gates

- Do not create concept, decision, or question pages until real source material exists to support them.
- Do not duplicate a per-source raw catalog here. Use the [Raw Source Index](../raw/sources.md) as the single registry.
