---
status: working
attribution: llm-synthesis
updated: 2026-09-20
sources:
  - SRC-2026-09-20-factor-identification-prompt
  - SRC-2026-09-20-factor-identification-chatgpt
  - SRC-2026-09-20-factor-identification-claude
  - SRC-2026-09-20-factor-identification-deepseek
  - SRC-2026-09-20-factor-identification-gemini
  - SRC-2026-09-20-factor-identification-glm
  - SRC-2026-09-20-factor-identification-grok
  - SRC-2026-09-20-factor-identification-qwen
  - SRC-2026-09-20-round-decisions-and-deferrals
  - SRC-2026-09-20-identification-experiment
  - SRC-2026-09-20-identification-experiment-findings
---

# Factor Identification Review

Round 4 asks a different question from the first three. Rounds 1 to 3 asked which factors are right and produced one more opinion per round. This round fixes the universe of [[DEC-009-three-markets-and-convergence]] — eleven practices listed in three markets, thirty-three securities, weekly strikes over 1996–2026 — and asks what that universe can **identify**, which is a property of the design rather than of the reviewer. Seven responses were collected: ChatGPT, Claude, DeepSeek, Gemini, GLM, Grok and Qwen. Kimi was not consulted. The prompt forbade recommendations, rankings and preferred sets, and carried the author's two positions from [[DEC-005-ledger-resolution-scales-with-universe]] as fixed context.

The result is a **conditional frontier**, not a factor set. No factor, name, coefficient or count is selected by this page. All reviewer proposals remain `llm-proposed`; this comparison is `llm-synthesis`.

## Evolution

[[factor-set-failure-profile-review]] closed with the objection that eleven constituents cannot distinguish a common shock from a security-specific one. [[DEC-009-three-markets-and-convergence]] tripled the universe partly to answer it, and claimed that three markets make local and common factors structurally separable. This round tests that claim and finds it half-true at every date, in a precise sense set out below. It also gives the first derivation, from the listing rather than from taste, of how many lines the opening ledger can carry — and the derivation does not produce nine.

## Scope and source quality

All seven responses reach Section 8 and answer in the required order. Six are in English; **Gemini's response is in Korean**, and it is the least compliant: it states a convergence threshold (`r ≥ 0.85`), promotion thresholds (`t > 2.58`, `|λ| > 0.35`, `ΔR² ≥ 0.05` over 52 weeks) and a labelled nine-line set with named securities, all of which the prompt forbade inventing. Its content is recorded where it agrees with others and flagged where it stands alone. ChatGPT cites external references inline; the others cite the literature by name. No response ran an estimation; every procedure in Section 7 is proposed, not executed.

**The prompt has one defect the round exposed.** It says the ledger has one line each for numeraire, substitution, positioning, reflexivity and `Unexplained`, plus "one line per priced factor", and then says it "opens near nine factor lines". Five reviewers read *nine priced factors*; GLM read *nine total lines* and answered under that reading, with the alternative given; Qwen and Grok answered both. The two readings give different frontiers — under the total-lines reading GLM's defensible opening count is eight, and under the priced-only reading it is three. Which count the decision in [[DEC-005-ledger-resolution-scales-with-universe]] meant turned out to be the wrong question: asked, the user said the nine was an LLM proposal they had gone along with, not a designed number, and that the factor count may be raised as needed. The ambiguity is closed as moot, and the counts in the table below are read as what the listing supports, not as verdicts on a target.

## Where the round converges

**The listing is a two-way layout, and that fixes what can be named.** Five reviewers (Claude, DeepSeek, GLM, ChatGPT, Qwen) derive the same geometry independently: thirty-three securities decompose into one grand level, ten practice contrasts, two market contrasts and twenty practice × market interaction dimensions. The additive part — `1 + (11 − 1) + (3 − 1) = 13` — is the set of factor directions the listing *names* by construction (GLM cites Heston–Rouwenhorst). The twenty interaction dimensions are where a single security's own noise lives, and nothing supported there can be separated from that noise by estimation. This is the formal form of Round 3's objection: a factor on one practice in one market is that security's residual with a label.

**Rank is not identification.** Every reviewer separates three things the prompt's "maximum number of factors" ran together: the rank of the return covariance (at most 33, or 25 under the Ledermann bound Claude and ChatGPT both compute), the number of directions the listing can *name*, and the number of *economic mechanisms* whose weekly contribution can be recovered. Rotation indeterminacy means the data identify a span, not labels; naming requires restrictions the listing supplies or measurements the institute publishes. ChatGPT's formulation: a universe can support nine independent return directions while supporting no unique assignment of nine economic names.

**The author's first position holds in one mode only.** Factors may outnumber securities when they enter as *declared, measured series* — the numeraire revision, a published wave-exposure schedule, flow records — because a measured line consumes no covariance rank. It cannot hold when weekly factor realisations are inferred from the cross-section, where the count is bounded by the rank of the loading matrix. Claude, GLM, Grok and ChatGPT each state this as an interpretation of the position, not a challenge to it.

**Time-series length is estimating power, not identifying power.** Roughly 1,565 weeks estimate a known loading precisely; they do not separate two slow common series with similar loadings. Claude adds the sharpest version: the drivers are S-curves off one capability origin, so for slow factors the effective sample is the number of distinct arrival events — at most seven waves in three markets, fewer once late arrivals coincide — not the number of weeks.

**Convergence destroys local identification and does not destroy common identification.** All seven agree, and four (Claude, DeepSeek, GLM, ChatGPT) give the same arithmetic: under equicorrelation the market block's eigenvalues are `1 + 2ρ` on the common direction and `1 − ρ` on each contrast, so between `ρ = 0.2` and `ρ = 0.9` the contrast variance falls by about a factor of eight while the common direction roughly doubles. All seven decline to date the break: it is set by a rank test on the market-demeaned covariance, window by window, not by a calendar year or a correlation threshold.

**No identification argument produces nine.** Stated in those words by Claude, and by implication in every other response. The counts the seven derive are in the table below.

## The count, by reviewer

Not a ranking. The differences come mostly from the counting convention and from what each reviewer let into the count.

| Reviewer | Reading of "nine" | Opening count | Late count | What the count is made of |
|---|---|---|---|---|
| Claude | priced | at most 8; 6–7 if dial-up and broadband do not separate | about 4 | global common, contact-vs-state, material-vs-rest, arrival lines for staggered waves, two residual market contrasts; labels marked judgement |
| DeepSeek | priced | 13 | 11 | one global, ten practice contrasts, two market contrasts; nine is a subset, not a maximum |
| Gemini | priced | 11–14 | 5–6 | a labelled nine including market-lead and market-lag lines and a reflexive premium — flagged, see above |
| GLM | total lines (A2) | 8, or 9 with a conditional line; 3 under the priced reading | 16, up to 18 | numeraire, substitution, three market lines, positioning, reflexive, `Unexplained`, plus the first practice line to pass promotion |
| Grok | mixed | 8 named lines plus residual; a 9th if the eleven practices present two independent contrasts | loses the local line | numeraire, common substitution, common arrival, one practice-group split, its local residual, positioning, reflexive, `Unexplained` |
| ChatGPT | priced | undetermined; zero certified | undetermined | refuses a count without the exposure matrix; nine is neither excluded nor established |
| Qwen | priced | 9 slots, as a maximum | 9 slots, differently populated | `13 − rank(standing lines) = 13 − 4 = 9`: two country contrasts plus seven residual practice components, unnamed |

Qwen's is the only derivation that lands on nine, and it lands there as a ceiling on *slots* whose economic labels the specification does not determine. Two reviewers (Claude, Grok) arrive at eight by different routes; two (DeepSeek, Qwen) at thirteen named directions as the outer bound.

## What three markets buy, exactly

The round's answer to the claim in [[DEC-009-three-markets-and-convergence]] is more precise than the claim.

**The naming is permanent; the estimation trades off.** GLM's account, consistent with the others and adding one thing they miss: the layout names local versus common at every date, but *estimates* local factors only while markets differ and *estimates* practice factors only while markets align. Early divergence destroys practice identification as thoroughly as late convergence destroys market identification — a practice dying at three speeds in three markets is not one practice factor but three interaction-space effects. The two purchases are never at full strength together, and the **handover** — market lines demoting while practice lines promote — is the structural event of the middle of the history, dated by tests rather than by the specification.

**Early-wave loadings survive convergence; late-wave loadings were never identified.** Claude: if a loading on a staggered wave is time-invariant, the staggered period estimates it and it carries forward. But waves that arrive coincidentally in all three markets — under the stated assumption, smartphones, messaging and AI — have no stagger to identify against, so their loadings are time-series-only from the start and remain so.

**Correlation is not the right observable.** Claude and ChatGPT both note that rising cross-market correlation can mean local shocks shrinking *or* global variance growing, and the two have opposite consequences: in the first case the local line is zero by definition, in the second it is real but unmeasurable. The absolute variance path of the two market contrasts decides, and the specification does not give it.

**The staggered design has known failure modes.** Three units and one arrival ordering per wave means a permutation test on a single wave cannot reach `p < 1/6`; inference pools waves and needs their orderings to differ (Claude). If one market always leads, arrival order is collinear with that market's own trend. Heterogeneous loadings across markets break the two-way design (Claude and ChatGPT cite the staggered difference-in-differences literature). Staggered timing is not an instrument; a causal reading also needs no anticipation and parallel paths (ChatGPT).

## The promotion schedule as a test battery

The promotion criterion left open in [[DEC-005-ledger-resolution-scales-with-universe]] receives, across the seven, a consistent shape: a declared-but-unpriced factor is promoted when every gate in a battery passes on a rolling window, and demoted when the same gates fail. The gates that recur, with the reviewers who state them:

- **Rank increment.** Admitting the candidate raises the rank of the loading matrix, or the number of eigenvalues clearing the idiosyncratic bulk, by one. Kleibergen–Paap (Claude), Onatski or Ahn–Horenstein with a margin because Bai–Ng consistency presumes `N → ∞` (GLM), bootstrap or permutation eigenvalue tests because the cross-section is small and fixed (Qwen). This is the gate that makes the count a function of universe size: rank rises only as listings add rows.
- **Support.** The candidate loads on at least two markets and at least two practices (Claude); a factor supported on one cell is a residual.
- **Useless-factor guard.** The loading vector is rejected as zero before any price is attached (Claude, citing Kan–Zhang).
- **Orthogonality to measured lines.** The candidate's series is not a relabelling of the numeraire, substitution, positioning or reflexive line (Claude, GLM, Qwen).
- **Out-of-sample.** Adding the line lowers the held-out share of `Unexplained` (Claude, DeepSeek, GLM, Qwen).
- **Placebo.** The effect vanishes when arrival-date market labels are permuted (Claude, Qwen).
- **Stability.** Loading signs from one half of the window hold on the other (Claude, Qwen).
- **Replication.** A portfolio of listed securities tracks the candidate's series within tolerance; a factor no listed portfolio can express is not a factor for this ledger (Qwen).
- **Post-publication encompassing.** After the line is added to the published ledger, `Unexplained` does not simply reallocate onto it — required because the reflexive line exists and *publication itself can create a factor* (Grok).
- **Joint testing.** Candidates are tested together, not one at a time against a sparse baseline, or several aliases can be promoted; when subsets are indistinguishable the test returns an equivalence class (ChatGPT).

Every reviewer but Gemini refuses to set the thresholds. They are institutional constants, fixed ex ante and calibrated by the Monte Carlo in the section after next. GLM states the **count law** the schedule implies: for `I` practices in `C` markets the named capacity is `1 + (I − 1) + (C − 1)` plus whatever the declared schedule anchors, and the realised line count is the number of those passing the battery on the date in question.

## What this universe cannot identify

The prompt called this the most important section, as the direct consequence of the author's second position. The reviewers' lists overlap heavily; the recurring items, the confound, and the listing change each says would separate it:

| Cannot separate | Confounded with | Listing change that would separate it | Stated by |
|---|---|---|---|
| The AI wave from the numeraire | The unit itself — AI defines it, arrives everywhere at once, touches every practice | A listed practice whose fundamental is AI-insensitive or that AI's arrival phase *raises*; or the basket's constituents, or AI-complementary claims, listed with opposite exposure | Claude, DeepSeek, Qwen, Gemini |
| Smartphones, messaging and the social web from each other | Coincident arrival, same exposed practices | A practice exposed to exactly one of the three | Claude |
| A wave's arrival phase from its substitution phase | Each other, when the lag between them is uniform; possibly one impulse response rather than two factors | Practices whose lag demonstrably differs | Claude, DeepSeek, ChatGPT |
| Cohort replacement from technological substitution | Both slow, monotone, common | Float tranches by birth cohort within each practice-market | Claude, DeepSeek, GLM, Grok, Qwen |
| Country-level slow trends — density, urban form, working hours, local price of time | The two market contrasts, which any slow national variable is collinear with | More markets, or urban and provincial tranches, or local numeraires | Claude, GLM, Qwen |
| A practice × market specific — film in Japan, messaging timing in Korea | That single security's idiosyncratic residual | Replicate the cell: sub-practices or regional variants in the same market | Claude, DeepSeek, GLM, Qwen |
| Style clusters — analog, asynchronous | *Exactly* the practice lines: a cross-market-uniform style is a linear combination of them | None. No practices-only listing separates a style from the practice lines; only a rotation choice does, and rotations are not data | GLM |
| Where redeemed attention goes | The substitution line's residual and `Unexplained`; substitution is visible only from the victim's side | List the replacing acts as securities | GLM, Grok |
| Within-practice heterogeneity — letters between intimates and letters between institutions | The single listed name's residual | Split the name | Grok, DeepSeek |
| Desire for a practice from the capability to do without it | Positioning and the reflexive line; float is attention *placed*, not attention *wanted* | A second published quantity per security that is neither float nor price — a listing of a new object, not a new factor | Grok, Qwen |
| A revival or scarcity premium from the material contrast | Revivals occur only in the three material practices | A non-material practice with a revival, or a material one without | Claude, ChatGPT |
| The 2020 shock from a late-wave acceleration | One coincident global event | None: it is an event, not a factor, under any listing | Claude |

Two reframings deserve to stand apart from the table.

**ChatGPT: exclusions are exposure equivalences, not a semantic blacklist.** A factor is unidentifiable on this universe exactly when a nonzero perturbation of its history lies in the nullspace of the observation map — produces the same observations. A listing change helps only if its added rows take that perturbation out of the nullspace; more securities that observe the same directions add nothing. And there are failures no listing repairs: an unanchored numeraire (scaling every fundamental and the unit together leaves every quote unchanged), gross issuance versus gross redemption from a balance alone (`Q_t − Q_{t−1} = I_t − R_t` does not identify the two flows; flow records do), and a factor whose full signature an unrestricted disturbance may reproduce. The second position is therefore made precise rather than confirmed: the listing determines what can be *expressed*, and the observation system and disturbance model determine what can be *distinguished*.

**GLM: the second position has a boundary.** Because a practices-only listing spans every cross-market-uniform loading vector, it decides that styles do not exist as separate lines — only as alternative names for the same span. That is the author's position reached from the estimation side, and its limit.

## Double counting

The three capability-derived objects — numeraire, substitution, float — were the prompt's stated concern, and the round agrees on the discipline:

- **At most two orthogonal components from one driver** (GLM): the unit-valuation component, measured by the companion index, and the exposure-weighted flow component residualised against it. A third capability-derived line double counts by construction. Claude's check is exact and weekly: headline index minus companion index must equal the numeraire line.
- **The common direction is the average of the three market lines.** Carrying a world line *and* three unconstrained market lines is linear dependence (GLM, ChatGPT, Claude). Carry a block's lines or its common line plus contrasts, never both.
- **Float is substitution's balance-sheet shadow.** Redemption *is* the substitution mechanism; float updates the fundamental and never enters the attribution as its own line (Claude, DeepSeek, GLM, Grok, Qwen). ChatGPT adds that the float is an attention balance, not a share count, so no `1/Q` price formula and no universally positive scarcity loading follow from its definition.
- **Arrival is not one minus substitution.** Code arrival only in the window between a wave's arrival and the start of its substitution phase (Grok).
- **Positioning and reflexivity are separated by the lag the institute inserts.** Positioning is contemporaneous; reflexivity is the coefficient on the *lagged published* attribution (Grok), estimated on residuals so it does not absorb slow-factor persistence (Claude). Whether positioning and float are the same balance is not stated in the specification and cannot be determined (Claude).
- **The attribution is a recursive orthogonalisation in a declared order** — numeraire, substitution, priced factors, positioning, reflexive, `Unexplained` — and the order has the status of a Cholesky ordering: it determines the split, it is untestable from returns, and it **must be published** (GLM, Claude citing Frisch–Waugh–Lovell). `Unexplained` is the monitor: if its cross-sectional covariance is not near-diagonal, a line is missing and the promotion search is triggered.
- **A shared driver is not itself a double count** (ChatGPT). The error is reporting a total effect and then adding effects already inside it. Exact weekly sums in a nonlinear model need a stated finite-change allocation rule, which can make the arithmetic exact without making the causal allocation unique. This keeps the distinction [[attribution-ledger]] already draws between exact accounting and causal recovery.

## What would settle it — a procedure that can be run

All seven propose the same experiment and note that it is runnable because the world is generated. Combined:

1. **Declare the generating process in full**, including every candidate factor from the earlier rounds' sets at once, with variance shares swept from negligible to dominant, and the correlation path produced by distinct mechanisms — growing global variance, shrinking local variance, synchronised exposures, growing numeraire variance — since these share a headline correlation but differ in what they destroy (ChatGPT).
2. **Simulate the 33 × 1,565 panel** under each candidate as truth, and fit every candidate to every panel. Report the confusion matrix `P(select j | truth i)` separately for the early and late windows; off-diagonal mass is a direct measure of what the universe cannot tell apart (Claude).
3. **Plant controls**: a null factor with zero loadings, to measure the false-promotion rate of the gate battery, and leave-one-market-out prediction of the third market's attribution (Claude, Grok, ChatGPT).
4. **Calibrate the thresholds** the battery leaves unset — variance-share floors, window lengths — from the simulated size and power (GLM). Block-bootstrap the rank tests to preserve serial correlation.
5. **Apply to the actual history, rolling**, to obtain the dated sequence of promotions and demotions: the early count, the handover, the late count.
6. **State the limit.** The procedure discriminates *identifiability classes*, not sets within a class. Two passing sets that are rotations of each other generate the same return distribution, and no data this universe produces separates them; the tie is settled by the listing's exclusion structure (GLM, ChatGPT).

The output is a frontier: for each line, the parameter region in which it is recoverable. [[loop-simulation]] already generates the panel this procedure needs; nothing in it has been run.

## Framing objections, recorded

The prompt permitted framing objections in Section 8 only. Those raised:

- **In an authored world, identification is audit, not discovery** (Claude, GLM). The institute knows its own process; the question is whether a reader could recover or falsify the published ledger from what is published.
- **The information set of the opening ledger must be specified** (ChatGPT). A 1996 attribution estimated with thirty years of hindsight is not an attribution identifiable with what was available in 1996.
- **The second position is a premise, not an identification result** (DeepSeek): the analysis can say what a listing separates, not what should be listed.
- **The round asked for scalars where the objects are indexed by epoch and rotation** (GLM); a single number would smuggle in the preference the round forbade.

## Evolution — the procedure was run

On the user's instruction the Section 7 procedure was run on 2026-09-20 against the v3 harness, five seeds, with the numeraire and the declared schedule stripped first — [[identification-experiment]]. What it returned, all `llm-proposed` and all on placeholder coefficients: the handover is visible and runs through the interaction block rather than the market contrasts; an eigenvalue-ratio estimator recovers one or two directions early whatever the truth and eight of nine or nine of thirteen late, never thirteen; a fixed promotion threshold promotes most planted nulls and the gate must be calibrated on the null per window, after which its power is 0.89 early and 0.98 late; two markets explain 23% of the third early and 56% late; and swapping the orthogonalisation order of the schedule and factor lines shifts the schedule line by 1.45 times its own size early. No factor is named and nothing is calibrated against the spine.

## Related

- [[DEC-005-ledger-resolution-scales-with-universe]]
- [[identification-experiment]]
- [[DEC-009-three-markets-and-convergence]]
- [[DEC-007-standard-return-numeraire]]
- [[attribution-ledger]]
- [[factor-set-failure-profile-review]]
- [[factor-architecture-review-consensus]]
- [[loop-simulation]]
- [[technology-waves]]
- [[Q-002-listing-lifecycle]]

## Sources

- [[SRC-2026-09-20-factor-identification-prompt]] — [raw/documents/2026-09-20-factor-identification-prompt.md](../../raw/documents/2026-09-20-factor-identification-prompt.md)
- [[SRC-2026-09-20-factor-identification-chatgpt]] — [raw/surveys/2026-09-20-factor-identification-chatgpt.md](../../raw/surveys/2026-09-20-factor-identification-chatgpt.md)
- [[SRC-2026-09-20-factor-identification-claude]] — [raw/surveys/2026-09-20-factor-identification-claude.md](../../raw/surveys/2026-09-20-factor-identification-claude.md)
- [[SRC-2026-09-20-factor-identification-deepseek]] — [raw/surveys/2026-09-20-factor-identification-deepseek.md](../../raw/surveys/2026-09-20-factor-identification-deepseek.md)
- [[SRC-2026-09-20-factor-identification-gemini]] — [raw/surveys/2026-09-20-factor-identification-gemini.md](../../raw/surveys/2026-09-20-factor-identification-gemini.md)
- [[SRC-2026-09-20-factor-identification-glm]] — [raw/surveys/2026-09-20-factor-identification-glm.md](../../raw/surveys/2026-09-20-factor-identification-glm.md)
- [[SRC-2026-09-20-factor-identification-grok]] — [raw/surveys/2026-09-20-factor-identification-grok.md](../../raw/surveys/2026-09-20-factor-identification-grok.md)
- [[SRC-2026-09-20-factor-identification-qwen]] — [raw/surveys/2026-09-20-factor-identification-qwen.md](../../raw/surveys/2026-09-20-factor-identification-qwen.md)
- [[SRC-2026-09-20-round-decisions-and-deferrals]] — [raw/conversations/2026-09-20-round-decisions-and-deferrals.md](../../raw/conversations/2026-09-20-round-decisions-and-deferrals.md); the user's answer on the counting convention
- [[SRC-2026-09-20-identification-experiment-findings]] — [raw/documents/2026-09-20-identification-experiment-findings.md](../../raw/documents/2026-09-20-identification-experiment-findings.md); the Section 7 procedure, run
