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

## [2026-09-05] ingest | Pricing Model v2 Factor Architecture Review survey originals

Preserved six independent review responses under `raw/surveys/2026-09-05-pricing-model-v2-factor-review-<model>.md`: Claude, DeepSeek, Gemini, GLM, Grok, and Qwen. Claude's downloaded Markdown was copied byte-for-byte; the other five responses were saved verbatim from each site's response-copy control as UTF-8 Markdown. Registered all six with Git object hashes and `raw-only` status. No review proposal was promoted to a user decision or synthesized into the concept pages.

Capture notes: Qwen's source ends mid-expression (`P_s(t) = P_s(t`); GLM's architecture diagram stops at the valuation-and-belief block but its response continues afterward. These source limitations were preserved without completion or correction. Existing registered source hashes were verified before and after capture.

## [2026-09-05] ingest | Pricing Model v2 factor architecture promoted to the Wiki

Promoted the factor-framework conversation, its registered review prompt, and five hash-verified second-round model reviews — Claude, DeepSeek, Gemini, GLM, and Grok — into the Wiki. Created [[factor-architecture-review-consensus]] to synthesize where the five verified reviews agree and split. Updated [[pricing-model]], [[model-review-consensus]], [[index-architecture]], [[current-state]], [[Q-001-price-formation]], and the index to reflect the new material.

Source verification: all seventeen registered sources were rehashed with `git hash-object` at the start and end of the task and compared against `raw/sources.md`. Sixteen match. `SRC-2026-09-05-pricing-model-v2-factor-review-qwen` does not: registered `59291ecd3ffdb1d45bbcc2ccc3d2403230242f15`, current `07c1fb597b79ee4cdb4dc3fce9d65e201d6911c3`. The change is substantive, not a line-ending artifact — the registered capture ended truncated mid-expression, and the current file ends with a complete closing sentence, so the truncated original was replaced with a finished response after registration. The Qwen review is excluded from all Wiki synthesis. Resolution is left to the user: registering the current file as a separate revision source is the schema's own remedy for this situation, but the originally registered bytes no longer exist on disk, so this needs an explicit decision rather than an automatic fix.

CORRECTION to the preceding entry of the same date: it recorded all six second-round surveys as registered with `raw-only` status. That is no longer accurate. Five were subsequently promoted into the Wiki, and the Qwen row in `raw/sources.md` now reads `REVIEW_REQUIRED — hash mismatch`. The earlier entry stands unedited, since this log is append-only; this entry supersedes it on that point.

Attribution care: the framework is recorded explicitly as a working proposal and the reviews as `llm-proposed`. Nothing was promoted to `user-confirmed`. The final factor set remains open.

Provenance note: unlike the first review round, the second round's review prompt is itself registered (`SRC-2026-09-05-pricing-model-v2-factor-review-prompt`), so the framing of what reviewers were asked is a primary citation here rather than a secondary one. The corollary is recorded on [[factor-architecture-review-consensus]]: because that prompt directed reviewers to hunt for missing causal dimensions and named several by example, the reviews' convergence on a missing demand side is partly prompt-induced rather than fully independent.

Lint performed: wikilinks resolve, no orphan pages besides the index itself, frontmatter complete on all pages, and `git diff --check` clean. One structural repair: a blank line inside the `raw/sources.md` registry table was splitting it into two Markdown tables; removed so all seventeen rows render as one table.

Two attribution errors were found during verification and corrected before promotion. The draft [[factor-architecture-review-consensus]] credited Grok with retaining Coordination Compression and Scarcity Revaluation as factors; GLM retains both and Grok demotes both. It also recorded the 40–60 constituent-expansion proposal as a single-review proposal from Claude, when Grok independently proposes the same target and treats it as equally blocking.

## [2026-09-06] maintenance | Qwen second-round review re-captured and promoted

The Qwen second-round source failed hash verification on 2026-09-05 and was excluded from the Wiki pending review. The user has confirmed the current file is the correct original — the first capture was defective, ending mid-expression partway through the response, and was deleted and re-pasted in full. This is a capture failure, not a change to the evidence.

The Qwen row in `raw/sources.md` now carries hash `07c1fb597b79ee4cdb4dc3fce9d65e201d6911c3` with the superseded hash `59291ecd3ffdb1d45bbcc2ccc3d2403230242f15` retained in the row and explained in the note section. It was registered under the same source ID rather than as a separate revision, because no Wiki material had been promoted from the defective capture, and a second row would imply two Qwen reviews exist when there is one. A corresponding rule was added to `raw/README.md` so this case does not need re-deciding.

The substantive consequence: the second review round now has six verified reviews rather than five, and Qwen is the round's clearest dissenter. The framework rejected minimal factor count as a design goal and five reviews support that; Qwen reduces the nine candidates to five core factors — Friction Elimination, Agency Displacement, Material Decoupling, Social Revaluation, Attention Scarcity — and cites parsimony. It is recorded as a minority position, not as a correction of the majority and not smoothed away.

Which unanimity claims changed: Time Compression and Uncertainty Compression are no longer retained by every review, since Qwen merges both into Friction Elimination along with Coordination Compression. Friction / Inconvenience Premium is no longer uniformly preserved as a valuation regime, since Qwen demotes it to a security-level fundamental. Coordination Compression and Scarcity Revaluation move to five of six against retention, with GLM alone retaining each. The demand-side territory list is now recorded as a union across reviews rather than a unanimous set, because Qwen adds only attention scarcity and explicitly rejects institutional trust and demographic shift.

Pages updated: [[factor-architecture-review-consensus]], [[pricing-model]], [[current-state]], [[index-architecture]], [[Q-001-price-formation]], and the index.

Attribution unchanged: all six reviews remain `llm-proposed`, the framework remains a working proposal, and nothing was promoted to a user decision.

## [2026-09-06] lint | Factor attribution errors corrected against the raw surveys

The 2026-09-05 promotion entry recorded that two attribution errors had been found and corrected, crediting GLM with retaining Coordination Compression and Scarcity Revaluation and crediting Claude and Grok jointly with the 40–60 universe proposal. Those corrections were themselves wrong. Verification against the raw surveys shows Grok retains Coordination Formalization as F6 and Scarcity Revaluation as F8, GLM demotes both — Coordination to an indicator cluster inside its Encounter Erosion factor and Scarcity to a security-level Rarity Elasticity of Value — and the 40–60 expansion is proposed by Claude alone, with Grok saying nothing about universe size at all.

Root cause, stated plainly: the earlier corrections rested on a model-generated extraction of the surveys that had transposed GLM and Grok throughout, and that extraction was accepted without checking the claims against the source files. The draft text it replaced had been correct.

A further error found in the same pass, present in the original draft too: Coordination Compression is not deleted by Claude. Claude retains it as F4 but declares it unpriced until the security universe expands, because its support in the eleven-security set is essentially two constituents.

What was done: every model-attributed claim on the affected pages was re-verified directly against the raw surveys and corrected. A `## Correction history` section was added to [[factor-architecture-review-consensus]] so the error is visible on the page itself rather than only in this log.

The standing lesson, phrased as a rule for future work: when an extraction contradicts text already in the Wiki, the source file settles it, not the extraction. Do not overwrite existing content on the strength of a summary that has not been checked against the original.

The earlier log entries stand unedited, as this log is append-only, and this entry supersedes them on these points.

## [2026-09-06] ingest | Third review round opened — failure-profile prompt and first response

Registered three sources and promoted none. The third round changes the question rather than repeating it: instead of asking for a factor set, it presents the six sets from the second round blind, labelled SET A through SET F with model identity removed, and asks only what each set misprices, cannot attribute, cannot identify at eleven securities, double counts, or structurally cannot say. The prompt forbids recommendation, ranking, and new proposals, and puts security-universe expansion explicitly out of scope so that the set question and the universe question stay separable.

The prompt is registered in two versions because the round spans both. Version 1 headed SET B `12 priced factors` while noting that two of the twelve run unpriced initially. Version 2 rewrites the heading and states the execution rule. The ChatGPT response was produced against version 1 and documents its own resolution of that tension in its Refusals section; the remaining five reviews are being collected against version 2. Registering both keeps each response traceable to the exact stimulus that produced it.

Capture note: the ChatGPT original was captured from the response as pasted into the working conversation, not from a direct export. That is a weaker capture path than the second round used, and it is recorded in `raw/sources.md` so a later direct export can be compared against it.

Nothing from this response has entered the Wiki. Its most consequential claims — that few factors produce semantic compression while many produce collinearity, these being two forms of one information limit at eleven securities; that an exactly summing ledger does not imply exact causality; and that statistical cost and artistic cost diverge, so a statistically better simplification can be an artistically worse resolution — are `llm-proposed` from a single model and will be synthesized only after the round completes and the responses can be compared.

## [2026-09-06] ingest | Ledger resolution decided as a rule; attribution-ledger page created

Registered and promoted `SRC-2026-09-06-attribution-resolution-and-universe-scaling` (raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md, hash `f369932d9135eeb1a15d22e256bc34748fd9cc28`), a compiled record of a working session held while the third review round was being collected. Unlike the surrounding material, this session did not review any model output; it worked on the weekly attribution ledger the audience actually reads — what it prints, how it decomposes a price move, and what an unrouted event means — and on what that implies for how factor count and security count relate.

The user's resolution decision was recorded as a rule rather than a set selection: the weekly ledger starts near nine displayed factors, and the number of ledger lines grows as the security universe grows, making factor count a function of universe size instead of a constant. This is `user-confirmed` and is recorded in the new [[DEC-005-ledger-resolution-scales-with-universe]]. Two further positions stated by the user in the same session — that unattributable events should not occur at all, and that factors should be abstract but numerous with the security count growing to match — are recorded as `user-originated` and `working`, not folded into the decision, because they are stated directions rather than specified mechanisms; the session record itself distinguishes them from the resolution rule on exactly this ground.

Created [[attribution-ledger]] as a new concept page, since the weekly ledger now has enough material to develop independently of the factor architecture that feeds it. It reproduces the worked `LETTER` example verbatim and records, explicitly marked as `llm-proposed` and not confirmed by the user: the three-layer allocation rule for routing an event to the factor layer, the security-fundamentals layer, or the positioning layer; a per-factor separability test proposed to replace the earlier working ratio of roughly one factor per three securities; the treatment of `Unexplained` as a rarely firing design instrument rather than a display element; and the proposal to write thirty to fifty events before fixing either the factor set or the security list.

A clarification carried onto the new page: because a LONGING price is generated by the model rather than observed from the world, residual is structurally zero in the statistical sense, and `Unexplained` does not mean noise the model failed to explain — it means an authored event with no word in the current factor vocabulary. The session's own worked example for this — the closure of the last large film-processing chain, offered as a case with no macro-factor coverage — was corrected within the same session: infrastructure viability loads on only three of eleven constituents (Film Photography, Physical Media, Live Performance) and is near zero elsewhere, which makes it a security-level mechanism, not a macro factor, so the event belongs in the ledger's existing security-fundamentals layer from the start. The option first presented as the lesser choice was the architecturally correct one. This correction is preserved on [[attribution-ledger]] rather than smoothed away, since it is a concrete instance of exactly the mis-routing risk the page is about.

Updated [[pricing-model]], [[current-state]], [[Q-001-price-formation]], and the index to cross-link the new pages, added the new source to each page's frontmatter and Sources section, and noted on each that ledger *resolution* is now settled as a rule while ledger *membership* — which factors fill the starting nine, and the criterion for promoting the next one — remains open.

Capture limitation, carried from `raw/sources.md`: the source is a compiled working-session record, not a byte-exact export; repository mechanics from the same session were omitted, and the user's own statements are reproduced verbatim in Korean and marked as such. The record itself closes with an explicit split between what the user decided and what the assistant proposed without confirmation, and that split is what this entry and the two new pages follow.
