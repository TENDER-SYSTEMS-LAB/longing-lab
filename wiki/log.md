# Activity Log

This log is append-only. Add new entries after all existing ones using `## [YYYY-MM-DD] <type> | <title>`. Prefer `ingest`, `query`, `decision`, `lint`, or `maintenance` as the type.

## [2026-09-04] maintenance | Repository initialized

Created the repository structure following the convention established in `other-goods-lab`: a `raw/` source layer, a `wiki/` synthesis layer, and an operating layer of `schema.md` and `AGENTS.md`. No project material was ingested and no project facts were recorded. The `wiki/collections/` type was intentionally not created, since no material requires it.

## [2026-09-04] maintenance | Institutional Git identity policy

Added a repository-wide rule requiring new commits to use the repository-local TENDER SYSTEMS identity and requiring commit identity to be verified separately from GitHub push authentication. The rule prohibits personal author or committer fallback, guessed institutional email addresses, secret disclosure, and history rewriting. A dedicated push identity remains preferred; personal push authentication is permitted only with explicit user authorization and acknowledgment that non-commit audit or activity records may retain the push actor. No project knowledge or raw source material changed.
