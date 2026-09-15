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

## [2026-09-06] ingest | Arbitrage and news quality opened; three work items set

Registered and promoted `SRC-2026-09-06-arbitrage-news-quality-and-next-work-items` (raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md, hash `9acabf63123daf4baec02cf627ab22c0ccd56c9f`), a compiled working-session record from the same day as the ledger-resolution session and on the same capture terms: not a byte-exact export, the user's statements verbatim in Korean, everything attributed to the assistant marked as paraphrase.

The session opened with a long plain-language explanation pass — the pricing model for a fifteen-year-old, a follow-up on the symbols `K`, `N`, and `κ`, and an enumeration of every formula in the corpus explained for a reader with no finance background. That pass introduced no new claim and is described in the record rather than reproduced. Its relevance is sequential: the user's proposals were made immediately after seeing the whole formula set laid out at once, and two of the three work items read as responses to gaps visible only at that scale.

Five user positions were recorded, none of them a specified mechanism, and the assistant proposed nothing in the session.

Created two concept pages. [[arbitrage]] records the direction that arbitrage be represented in the work, with the user's framing that *how it is implemented in this world* is itself the interesting part. The page separates what exists from what does not: the corpus already holds limits to arbitrage — Claude's `κ = κ₀ × (1 − |crowding|) × evidence_arrival` — which explains why mispricings persist without ever depicting an arbitrageur, and nothing anywhere says who takes the other side, what a position costs to hold, or what closing one means. Four questions are raised on the page from registered material and marked as such rather than as source proposals: who the counterparty is without reintroducing the circularity that sank the original consensus mechanism; what is bought, given that [[Q-004-unit-of-account]] is unresolved; what makes a position converge, given that `F` is a monthly opinion and not a settlement; and whether an arbitrageur belongs to the work's politics, which makes it material for [[Q-003-calibrating-the-bias]].

[[information-quality]] records the direction that news quality be modelled — clean disclosure, misreporting, over- and under-reporting, and pre-circulating rumour. Mapped against the existing event layer, the first behaviour is the current default, the third is partly reachable through the surprise framing, and the second and fourth have no representation anywhere in the corpus. The nearest existing structure is the rule that confidence scales the speed at which an event is priced in rather than the size of the move, so a low-confidence event bleeds in over weeks and can reverse if unconfirmed — but that models uncertainty about an event that is nonetheless true. GLM goes furthest, with provisional events at half weight and revisions as events in their own right, and even there a revision corrects a magnitude rather than retracting a fact. The page notes that misreporting collides directly with the ledger's exact-sum requirement, that it is the cheapest available source of the surprise two second-round reviews said the design lacks, and that pre-circulation may need no new price machinery because a leak that crowds the book before the disclosure is exactly the configuration the asymmetric squeeze amplifier already prices.

Recorded a later user position against [[DEC-005-ledger-resolution-scales-with-universe]] without changing the decision: **factors may outnumber securities**, which rejects Claude's working ratio `K ≤ N/3`, with the ordering conclusion from the earlier session given as the reason — which practices are listed determines which factors can exist, so the binding constraint is expressibility against the listed universe rather than an arithmetic cap. The user endorsed the ordering, not the `llm-proposed` per-factor separability test that tries to formalize it. Both positions are to be carried into the next review round as stated context. The decision itself still fixes only how ledger resolution behaves as the work grows.

Updated [[Q-004-unit-of-account]] with the user's instruction that it be put to the review models as its own round. This is method, not content: the user stated no position on the question, and none of the recorded answers gained standing. The page notes two constraints for building that round — the review set has already split three ways, so re-collecting those positions adds nothing, and the question has since acquired a second dependant in [[arbitrage]].

Added an `Academic prior art — not yet surveyed` section to [[prior-art]], which until now covered comparable artworks only. Nothing in this repository has surveyed scholarship, and the model has been built by proposing mechanisms and reviewing them across thirteen language models — good for finding internal contradictions, poor for discovering that a mechanism already has a name and known failure modes. Two cautions are recorded with it: borrowed terminology must not import borrowed authority, and the useful finding would be a failure mode the model has walked into, not a citation that makes it sound established.

Updated [[pricing-model]], [[attribution-ledger]], [[current-state]], and the index to cross-link the two new pages and carry the new source. Source hashes for all previously registered originals were verified unchanged at the start of the task.

## [2026-09-06] ingest | Third-round failure profiles collected and compared

Completed the seven-service Chrome collection against registered prompt v2: Claude, DeepSeek, Gemini, GLM, Grok, Kimi, and Qwen. Together with the previously registered ChatGPT response to v1, the round now has eight accepted complete reviews. The earlier collection entry's “remaining five” wording did not describe the final scope; seven additional services were collected. All originals were saved and registered before Wiki promotion began.

Qwen and Kimi returned terminal fragments and supplied whole-response replacements in the same conversations with selected modes unchanged. Gemini's first response reached its ending but omitted required second event examples; it remains immutable and raw-only, with a separate complete replacement promoted. Registered the exact collection follow-ups as provenance. Kimi displayed an automatic K2.6 Instant fallback notice; exact backend-model continuity is not verified. The source registry records selected modes, conversation URLs, and capture methods: Claude's downloaded Markdown artifact, rendered answer text for the other six services, and ChatGPT's earlier pasted capture. No raw source was rewritten to normalize formatting or repair reasoning.

Created [[factor-set-failure-profile-review]] as the independent comparison of six fixed architectures. It retains conditional failures, conflicting mispricing directions, differing artistic costs, incompatible minimal repairs, and proposed discriminating tests. It qualifies claims that confuse exact forward accounting with inverse identification, treat missing common-factor names as absent fundamentals or positioning, assume unprovided exposure signs, or equate multiple effects with duplication. No simulation was run, no architecture was ranked or selected, and no review recommendation became a user decision.

Updated [[factor-architecture-review-consensus]], [[attribution-ledger]], [[pricing-model]], [[Q-001-price-formation]], [[current-state]], and the index. The user's factor-count direction remains intact. The separate unit-of-account review, explicit transmission of the later user positions in a subsequent modelling round, and academic prior-art survey remain outstanding. Source registry totals are thirty-one originals, thirty promoted and one raw-only.

At the user's request, closed the review Chrome tabs and the duplicate reading tabs after capture. Existing conversation records remain available at the registered URLs.

## [2026-09-06] lint | Third-round ingestion verification

Verified all thirty-one registered raw hashes, full registration coverage, and the absence of changes to previously tracked raw originals. Checked all twenty-five Wiki pages for broken links, catalog membership, and registered provenance. Found one pre-existing omission: [[DEC-005-ledger-resolution-scales-with-universe]] listed the arbitrage/news-quality source in frontmatter but omitted it from its Sources section. Added that existing citation without changing the decision or its catalog summary. The prior log remains byte-for-byte intact; new entries are appended only.

## [2026-09-06] query | Initial academic mathematical-model survey

Registered the compiled research brief and original research notes; added [[academic-model-survey]] and updated [[prior-art]], [[current-state]], and the index. The six primary-model cards distinguish states, parameters, units, estimates, illustrative values, validation limits, and possible applications. Frank supplies an identification counterexample. No factor set, security unit, or pricing engine was selected. Existing source hashes were checked before and after packaging; all 31 registered originals matched. The patch was prepared against the latest saved project to preserve the completed third review round.

## [2026-09-06] query | Dataset survey for component backtesting

Registered an original research synthesis covering 23 dataset families and six Kaggle routes, with mirrors distinguished from independent evidence. Created [[dataset-backtesting-survey]], linked it from [[data-sources]], and synchronized current state and the index. The notes map behavioral, attention, reporting and external market datasets to proposed tests for missing quantities and unnecessary complexity. Collection priorities remain LLM proposals; no factor set or security unit was selected, and no dataset was downloaded or fitted. Publisher metadata was inspected where accessible; failed page/API retrieval and unresolved access conditions are documented. All 33 existing registered hashes matched at the beginning.

## [2026-09-06] lint | Dataset survey verification

Verified all 36 source hashes present at the final check, including sources added concurrently by other work; preserved the 33 originals present at this task start and the pre-existing log prefix. Checked 27 Wiki pages for valid local/Wiki links and exactly one catalog entry per page; `git diff --check` passed. The initial catalog-check expression also counted routing references; restricting it to catalog bullet entries removed those false positives. Replaced this task's source-count sentence in current state with a registry pointer to avoid a stale count during concurrent ingestion.

## [2026-09-06] query | Broad cross-domain mathematical-model discovery

Registered the exact new user task message and an original 120-entry research catalog, then extended [[academic-model-survey]] rather than creating a duplicate concept. The catalog covers fourteen areas with short modeling targets, author/team and date metadata, source types, and links. It separates 117 substantive model/system entries, one bibliographic lead (Leontief), and two adjacent data-mapping artworks. Accessible primary abstracts, indexed primary excerpts, author/publisher previews, and official project descriptions support a discovery survey, not a full-text systematic review. Five previously surveyed papers recur for navigation. No factor set, parameter, or implementation was adopted.

Refreshed the evidence scope of Black Shoals, The Environmentalist Stock Exchange, and Emotional Stock Exchange in [[prior-art]], and synchronized [[current-state]] and the index. Preserved all earlier Wiki interpretation as historical material with qualifications. Supplied a Korean Markdown catalog and CSV outside the canonical repository documentation. The authoritative source count remains in the registry because another survey is being ingested concurrently. The 33 previously registered hashes matched at task start; completion checks are recorded below after execution.

## [2026-09-06] lint | Cross-domain discovery catalog verification

Verified all 36 currently registered source hashes, including the concurrently added dataset-survey record, and confirmed that all 33 originals present at this task's start are unchanged. Raw registration coverage is complete. Checked 27 Wiki pages for valid local/Wiki links and unique catalog membership, verified the pre-task log prefix byte-for-byte, and passed `git diff --check`. The English raw catalog and Korean delivery contain the same 120 unique entry IDs and source URLs across 14 categories; the CSV contains 120 data records. These are document-integrity checks, not validation of the external models or a claim to have read every linked paper in full. No commit or push was made.

## [2026-09-06] maintenance | Preserve portable research delivery

Preserved the previously delivered Korean 120-entry catalog and CSV unchanged as registered raw-only derivative exports, and linked them from [[academic-model-survey]]. Prepared the pending third-round review, academic surveys, and dataset survey together for the requested cross-computer handoff. Existing raw sources remain unchanged.

## [2026-09-06] ingest | Academic-model dialogue and continuation

Preserved accessible Korean user/assistant dialogue separately from a compiled continuation and summary. Retrieval returned empty items for the latest two turns; the supplied exact user passage and paraphrased assistant follow-up are explicitly attributed to the originating task handoff. Promoted the user's entry/exit distinction and feedback requirement, retained synthetic generation and model extensions as unresolved, and recorded the three unanswered design questions for cross-machine continuation. Updated existing academic-model, pricing, data and current-state pages plus index; no new concept or implementation. All 38 previously registered originals matched their hashes at ingestion start.

## [2026-09-06] ingest | Recover recent original conversation messages

After the API omitted the latest two turns, recovered the user application positions, assistant clarification and exact cross-machine commit/push request from local original message records. Registered a separate selected excerpt and upgraded Wiki provenance without modifying the previously registered partial export or compiled summary. Verification covers all 41 registered source hashes, preservation of the 38 pre-task originals, append-only history, changed-page links and catalog alignment.

## [2026-09-06] query | Recommend the next modelling task

Reviewed the current state, academic-model synthesis and unit-of-account question. Recommended resuming the three unanswered design questions through a single-security specification: computed outcome, directional mechanisms and parameter strengths without real data. The subsequent unit review and a synthetic experiment remain proposals, not user decisions. All 40 registered Markdown sources match git hash-object; the CSV matches with --no-filters. The difference is Git line-ending normalization.

## [2026-09-06] query | World-building depth and production roadmap

Registered the exact initiating user request and created [[worldbuilding-roadmap]] after reviewing the maintained synthesis and the recovered primary user application positions. The assessment distinguishes a developed artistic premise and market architecture from unresolved security meaning, actor roles, practice dynamics, information failures, lifecycle, and executable specifications. Two independent read-only audits checked institutional/audience scope and mechanism dependencies.

Proposed a design boundary of operating rules plus demonstrated consequences across a publication cycle and its exceptions, with a world contract and `LETTER` state specification as the immediate next deliverables. Added dependency stages, completion gates, and scenario checks; the proposed twelve-week sample is a production exercise, not a historical claim or empirical backtest. The user's factor-count direction, separation of practice starts/stops, feedback requirement, current no-real-data scenario, and requested unit review remain intact. Practice feedback is not treated as permission to price audience votes. No new design decision, factor choice, simulation, external model review, or implementation was made.

Updated [[current-state]] and the index. All 41 sources present at task start matched registration: the Markdown files under Git hashing and the derivative CSV under its already documented unfiltered convention. A byte-preservation baseline includes the pre-existing local log addition so it can remain intact. Final document-integrity checks follow below.

Verified all 42 registered hashes, byte-for-byte preservation of the 41 pre-existing originals and the full pre-task log prefix, unique catalog membership for every non-index Wiki page, changed-page Wiki links, and registered provenance. `git diff --check` passed. Review refined the roadmap to choose a provisional delivery context early and keep twelve-month forecast scores pending beyond the twelve-week publication sample. No commit or push was made.

## [2026-09-06] ingest | World rules and LETTER practice specification

Registered the exact user request as [[SRC-2026-09-06-world-rules-letter-spec-request]]. The user now takes up the roadmap's first two stages and specifies consistency across numbers, reports, actions, and history as the design target. Created [[world-rules]] and [[letter-practice-dynamics]] as independently developing concepts; extended existing [[Q-004-unit-of-account]] and [[Q-002-listing-lifecycle]] for their detailed choices. Connected the drafts through the roadmap, pricing, academic-model, data, arbitrage, price-formation, current-state, and catalog pages. No new decision page was created.

The world draft specifies a proposed fictional district/cohort, institutional authority and knowledge limits, funded-market versus stance-only audience roles, publication clocks, persistent records, provisional browser encounters, and four independent lifecycle domains. The unit comparison defines published assessments, funded dated forecast claims, and support entitlements, including effects on value, price, indices, resources, counterparties, arbitrage, and artistic meaning. Review exposed the low payoff-cap fixture as unsuitable for baseline LETTER volume and preserved that failure alongside an alternative threshold. Dated maturities, balanced claim pairs, the lack of automatic forced short covering, and settlement uncertainty remain explicit design costs. No unit or market mechanism was adopted or externally submitted for review.

LETTER now answers what to calculate, what changes it, and how assumed strengths can be examined without real data. The specification separates never-started, ongoing, and interrupted episode stocks; starts, resumptions, interruptions, and dispatches; and attention/discourse from behavior. It supplies concrete inclusion boundaries, joint-author contribution weights, local time/effort/relationship/access/substitution inputs, a delayed acknowledgment feedback candidate, coefficient ranges, delays, and unselected extensions. The feedback path and all quantitative settings remain LLM proposals.

A deterministic 27-week arithmetic scenario was independently reproduced: one adverse week reduces ongoing episodes to 972.50 and dispatches to 278.42; 26 improved weeks under the same rules reach 1,700.44 and 969.24. Breaking the feedback loop still permits recovery, reaching 1,613.88 and 859.57, so feedback amplifies the later path rather than being its sole cause. Population conservation and bounds hold; this is consistency checking, not empirical calibration, broad sensitivity validation, a natural-data generator, or a complete price engine. Completing LETTER does not validate the full factor architecture, and no factor-to-security count cap was introduced.

## [2026-09-06] lint | World and LETTER draft verification

Checked 30 Wiki pages for unique catalog entries, matching status/date, valid Wiki links and registered provenance; local Markdown links and git diff whitespace checks passed. All 43 registered source hashes match their registered conventions, including the previously documented unfiltered Korean CSV hash. Made that CSV convention explicit in the registry without changing the source or hash. Corrected one existing plain source-path typo in [[Q-001-price-formation]]. The source directories' .gitkeep files are repository scaffolding, not unregistered evidence.

All 42 pre-existing originals remain byte-for-byte unchanged. Editing exposed line-ending normalization of the pre-task log; the exact original bytes were reconstructed and matched to the saved SHA-256 before these entries were appended. No historical log text was changed. Independent review resolved joint-author entry counting, payout saturation, maturity/forecast conflicts, positioning denominators, and the distinction between exact modeled absence and rounded expectations. Population, unit/outcome, practice boundary, feedback selection, parameter strengths, observation/settlement rules, and delivery choices remain reviewable proposals. No commit or push was made.
## [2026-09-06] ingest | Preserve roadmap assessment and session handoff

Registered [[SRC-2026-09-06-worldbuilding-roadmap-and-handoff]] as a selected original conversation record: the initiating request, Korean assessment and roadmap, the user's request to continue in a new session, the assistant-written instruction prompt, and the ingestion request. The capture explicitly omits tool/progress turns and preserves message roles. It is one lineage with the already registered initiating request and subsequent world-rules/LETTER request, not independent corroboration.

The assistant's delivered prompt matches the later user-issued task body after removing the latter's /goal prefix and normalizing line endings/trailing whitespace for comparison only. Neither raw record was rewritten. Handoff preparation is distinguished from the later user's explicit selection of task scope; no geography, unit, feedback path, coefficient, platform, or later roadmap stage became a confirmed decision through this ingestion.

Added provenance and evolution context to [[worldbuilding-roadmap]] and [[current-state]], and synchronized the catalog summary. Preserved the newer [[world-rules]] and [[letter-practice-dynamics]] checkpoint and its next-decision gates. No new concept or decision page was needed. A read-only independent audit checked that the earlier assessment would not overwrite downstream progress.

Verified all 44 registered hashes under their documented conventions, byte-for-byte preservation of the 43 pre-existing originals and the full pre-task log prefix, unique catalog membership for all 29 non-index Wiki pages, and changed-page links/registered provenance. The whitespace diff check passed. No commit or push was made.


## [2026-09-06] lint | Link source files from every Sources entry

- `## Sources` entries named each original as plain text, so a page's provenance was readable but not navigable and the raw files reached the graph only through `raw/sources.md`. Rewrote 226 entries across 28 pages as `[[SRC-...]] — [raw/<type>/<file>.md](<relative path>)`, keeping the wikilink as the shared source identifier and adding the file itself as a Markdown link.
- `schema.md`: the Provenance example now shows both links and states the relative-path rule — `../raw/...` from a page directly under `wiki/`, `../../raw/...` from a page in a subdirectory.
- No claim, attribution, status, or hash changed. This is a link-format correction only.

## [2026-09-07] maintenance | Review source links and synchronize catalog dates

Reviewed the pending source-link maintenance for handoff. The preceding lint entry reports 226 conversions; the actual diff contains 215 source-file link conversions across 28 Wiki pages. Each link resolves to its original registered path. The earlier entry is preserved unchanged.

Updated the 28 edited pages' dates and synchronized their catalog entries, the schema entry, and the activity date. All 29 non-index Wiki pages remain cataloged exactly once with their existing summaries and statuses. No project claim, attribution, or decision changed.

Checked maintained-document local links, Wiki links and registered source identifiers, the unchanged existing log prefix, and the whitespace diff. `git status --porcelain raw/` was empty; no registered original was modified and no full hash audit was repeated.

## [2026-09-07] maintenance | Reduce routine context and verification work

Replaced mandatory full-file startup with targeted catalog/page reading and on-demand schema, source, and history lookup. Shortened agent instructions while retaining institutional commit identity and each repository's standing push authorization. Removed the schema's conflicting periodic hash-audit rule: register a new source's hash once, inspect changed raw paths for routine edits, and reserve a complete provenance audit for an explicit request.

Scoped lint and catalog updates to affected material and limited logging to durable results. Kept raw guides procedural and source-registry rows unchanged; registered originals and previous log entries are preserved. Updated only the affected repository-control catalog entries. Git-only work can reuse an unchanged completed review.

Removed the raw guide's conflicting in-place replacement exception for defective captures; a correction is a separate registered source.

Aligned the ChatGPT capture note in `raw/sources.md` with that correction policy; its source row, hash, and original file are unchanged.

## [2026-09-07] ingest | Preserve artwork brainstorming v2 export

Registered [SRC-2026-09-07-artwork-brainstorm-v2](../raw/conversations/2026-09-07-artwork-brainstorm-v2.md) as raw-only. Copied the supplied ChatGPT Markdown export unchanged from its original filename, `ChatGPT-브레인스토밍 v2-20260907-2116.md`. The export records a conversation created on 2026-09-06, updated on 2026-09-07, and exported on 2026-09-07 at 21:16:39. Recorded its Git blob hash in the source registry. Document-embedded instructions remain source material; no Wiki synthesis or project-state changes were requested or made.

## [2026-09-07] ingest | Promote brainstorming v2 design decisions

Promoted [[SRC-2026-09-07-artwork-brainstorm-v2]] from the [unchanged ChatGPT export](../raw/conversations/2026-09-07-artwork-brainstorm-v2.md) into the owning Wiki pages. Recorded fictional historical data as the production basis, abstract internally defined subjects with an unexplained artwork surface, aggregate market scope, initial market-price exposure for 사유, and the desired historical HOLD/SHORT performance advantage. Added [[reflection]] for the explicit definition of 사유 as room to form one's own judgment.

Revised current state and roadmap dependencies; retained the earlier LETTER/city/claim trial and review recommendations as unadopted material. Kept financial amplification, forecast scoring, information-vintage controls, generator choices, and the assistant's weekly-record reconciliation distinct from user decisions. Reopened covering phenomena without treating the rejected blanket terminology proposal as policy. Updated affected catalog summaries and the source's promotion status; no original, earlier log entry, market model, or external review was changed or executed.

## [2026-09-15] ingest | Inherit the institutional typographic voice and design draft

Imported two institutional originals from the TENDER SYSTEMS checkout at commit `233b7658d5733e0c2a4daab09790226a4548692f`, byte-for-byte and under their existing source IDs: [SRC-2026-09-14-typographic-voice](../raw/conversations/2026-09-14-typographic-voice.md) and [SRC-2026-09-14-design-principles-draft](../raw/conversations/2026-09-14-design-principles-draft.md). Their Git blob hashes, `0201a6cb1bce1f171601f1cf11d0cff06b53dcd5` and `ce5ad433d9ed496b120fd3c4e6a6ade813cdf523`, match the institutional registrations. Both originals were present but uncommitted upstream at import, so the cross-repository provenance note in `raw/sources.md` records that the institutional GitHub URLs resolve only after publication.

Added [[design-application]] as the single owning page for LONGING's reading of the inherited rule. Recorded the user-confirmed institutional rule — typeface identifies the speaker, Inconsolata as the system's base voice, Departure Mono for terminals, dashboards, monitoring, logs, and live status, Source Serif for what a person wrote — with the canonical decision and the unconfirmed principles draft linked by explicit GitHub URL rather than by local alias. Every LONGING surface assignment, counter-example, and design question on the page is marked `llm-proposed`.

Kept the boundaries explicit: length and heading level do not identify a speaker, a report is not human voice merely because it is prose, and typeface certifies nothing about who actually wrote a text. Julian Hart's near-prose-less quantitative output and the flash notes between coverage updates are recorded as system voice despite being filed under named analysts. The event-detector headline speaker, the Korean auxiliary typeface, and every weight, size, spacing, density, glyph, and licensing question remain open; the superseded per-system Sans/Mono split was not carried in. Nothing about LETTER behaviour was added and [[Q-004-unit-of-account]] stays open.

Synchronized the affected catalog entries, added a routing row, and extended `wiki/current-state.md` with one inherited-typography entry without altering the history-first production basis or any existing priority. [[DEC-002-research-house-form]] gained one cross-link to the new page. Verified the two new raw hashes, the changed pages' local links and source identifiers, the unchanged existing log prefix, and `git diff --check`; `git status --porcelain raw/` reports only the two added originals, and no registered original was modified. No font was obtained, installed, licensed, or rendered, no external claim was verified, and no product code was touched.
