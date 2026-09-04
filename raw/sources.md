# Raw Source Index

This document is the registry for every raw source. It tracks each source's ID, path, hash, and ingestion status. Any Wiki content followed back through its provenance must ultimately lead to an original through this table.

## Registration

When adding a source, append one row to the table below and record the result of `git hash-object <path>` in the `Hash` column. If a later hash differs from the registered value, the original has changed. Do not update the Wiki automatically. Mark the pages that rely on the source `REVIEW_REQUIRED` so that a person can review them again.

## Source List

| Source ID | Path | Type | Date | Attribution | Hash | Ingested | Wiki Status |
|---|---|---|---|---|---|---|---|
| `SRC-2026-09-04-longing-concept-brainstorm` | [raw/conversations/2026-09-04-longing-concept-brainstorm.md](conversations/2026-09-04-longing-concept-brainstorm.md) | conversation | 2026-09-04 | jointly-developed | `d387cd37602638d884491cbea9291b3ef63ee7f2` | 2026-09-04 | promoted |
