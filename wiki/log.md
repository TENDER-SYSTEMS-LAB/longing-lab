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

## [2026-09-05] ingest | Market pricing model and seven independent reviews

Registered eight sources. One conversation: `SRC-2026-09-05-price-formation-market-model` (raw/conversations/2026-09-05-price-formation-market-model.md, hash `bb15b180260e26f19a3447d808f8de07fe2c331d`). It arrived as `ChatGPT-conversation-20260905-0244.md` and was renamed to the `YYYY-MM-DD-short-slug.md` form required for registration, following the precedent set at the first ingest; its contents were not altered and the hash is unchanged. It is a Korean-language export and remains in its original language.

Seven surveys: `SRC-2026-09-05-claude-critic-of-model` (`68d0708d`), `-deepseek-` (`6685ee3e`), `-gemini-` (`c77b4442`), `-glm-` (`63edf229`), `-grok-` (`fd5945b2`), `-kimi-` (`50fef85b`), and `-qwen-` (`8839d304`). Each is an independent critical review of the drafted market model by a different language model, responding to one shared review prompt.

This ingest moves the project from concept to mechanism. The first conversation established what LONGING is; this material establishes how the market inside it produces a number.

Promoted as confirmed, both stated directly by the user: the weekly market / monthly research cadence, which overrode a monthly proposal already on the table ([[DEC-003-weekly-market-monthly-research]]), and the secular decline with inverted rallies, together with the constraint that the decline must emerge from published structural forces rather than a hard-coded drift ([[DEC-004-secular-decline-with-rallies]]).

Promoted as working: the market architecture ([[pricing-model]]), the convergence and splits across the seven reviews ([[model-review-consensus]]), and the behavior/attention/discourse data layering with its candidate sources ([[data-sources]]). Updated [[index-architecture]] with an Evolution section recording that the contrast indicators were promoted from display elements to macro variables, [[analyst-system]] with the analysts' new mechanical role and three warnings from review, [[Q-001-price-formation]] with an Evolution section moving it from `unknown` to `working`, and [[Q-003-calibrating-the-bias]] with the concrete tests the reviews supplied for keeping the bias from becoming an argument. Rewrote [[current-state]].

One new question: [[Q-004-unit-of-account]]. It was not raised by the user — it surfaced independently across several reviews and now blocks index weighting, the market-capitalization analogue, float, and short interest. The original currency form of the unit question on [[Q-001-price-formation]] was folded into it.

Attribution care: the entire review corpus is `llm-proposed`, and the surveys converge strongly — seven of seven reject the seven-factor macro set, the `Consensus Strength` product, and the `κ(1−S)` mean-reversion gate, and seven of seven call for a discount-rate analogue. That convergence is recorded as strong evidence about the model and explicitly not as a decision. The user requested the phenomenon those mechanisms were built to produce — a consensus strong enough to override fundamentals — so the phenomenon is recorded as user-originated while the mechanism is recorded as contested. No review recommendation was written as accepted.

Provenance limit: the shared review prompt `LONGING_market_pricing_model_review_prompt.md` is not registered in this repository. Every statement about what the reviews were asked reaches the Wiki only through the surveys themselves and is noted as a secondary citation in `raw/sources.md`, on [[model-review-consensus]], and here. The platform capabilities and public statistics described on [[data-sources]] are likewise secondary: they were cited from web search inside the source conversation and have not been independently verified.

Single-source dependency: eased for the market layer, unchanged elsewhere. [[overview]], [[system-grammar]], [[prior-art]], [[DEC-001-project-name-longing]], and [[DEC-002-research-house-form]] still rest entirely on the 2026-09-04 conversation.
