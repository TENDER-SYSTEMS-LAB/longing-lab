# Activity Log

This log is append-only. Add new entries after all existing ones using `## [YYYY-MM-DD] <type> | <title>`. Prefer `ingest`, `query`, `decision`, `lint`, or `maintenance` as the type.

## [2026-09-04] maintenance | Repository initialized

Created the repository structure following the convention established in `other-goods-lab`: a `raw/` source layer, a `wiki/` synthesis layer, and an operating layer of `schema.md` and `AGENTS.md`. No project material was ingested and no project facts were recorded. The `wiki/collections/` type was intentionally not created, since no material requires it.

## [2026-09-04] maintenance | Institutional Git identity policy

Added a repository-wide rule requiring new commits to use the repository-local TENDER SYSTEMS identity and requiring commit identity to be verified separately from GitHub push authentication. The rule prohibits personal author or committer fallback, guessed institutional email addresses, secret disclosure, and history rewriting. A dedicated push identity remains preferred; personal push authentication is permitted only with explicit user authorization and acknowledgment that non-commit audit or activity records may retain the push actor. No project knowledge or raw source material changed.

## [2026-09-04] ingest | First concept conversation — LONGING established

Registered `SRC-2026-09-04-longing-concept-brainstorm` (raw/conversations/2026-09-04-longing-concept-brainstorm.md, hash `d387cd37602638d884491cbea9291b3ef63ee7f2`). The file arrived as `conversation-20260904-2249` and was renamed to the `YYYY-MM-DD-short-slug.md` form required for registration; its contents were not altered and the hash is unchanged. The source is a Korean-language conversation export and remains in its original language.

This is the repository's first project material. It moved the Wiki from empty placeholders to a working model of the work.

Promoted as confirmed: the title `LONGING` ([[DEC-001-project-name-longing]]) and the choice of a research-house form in a financial-terminal register rather than a trading app ([[DEC-002-research-house-form]]). Both were stated by the user directly, the second with an explicit provisional framing.

Promoted as working: the index architecture ([[index-architecture]]), the opposed-analyst system ([[analyst-system]]), the series grammar shared with OTHER GOODS ([[system-grammar]]), and the comparable-works survey with its two differentiation rules ([[prior-art]]). Rewrote [[overview]] and [[current-state]] from the source.

Three open questions recorded: price and index formation ([[Q-001-price-formation]]), listing lifecycle ([[Q-002-listing-lifecycle]]), and how far the work's tilt toward the human may go ([[Q-003-calibrating-the-bias]]).

Attribution care: the user asked for a faint bias toward romance and proposed characterizing SHORT analysts as machine-like or villainous. The LLM set that persona approach aside and proposed structural asymmetry instead; the user replied only "좋은 정리 감사해". That is acknowledgment, not a decision, so the approach is recorded as `working` and `jointly-developed`, not `user-confirmed`. Seven alternative work formats generated in the conversation were recorded as `deferred` rather than dropped, and rejected name candidates were preserved with reasons.

Single-source dependency: every Wiki page now depends on this one conversation. All statements about OTHER GOODS and every comparable artwork cited in [[prior-art]] reach the repository only through it and are secondary citations, unverified here.
