# LONGING — Pricing Model v2
## Factor Architecture Review

Prepared as a hostile review. Assume the reader is a quant, a behavioral researcher, an index-methodology committee, and an art critic who has seen a lot of fake precision.

---

## 1. Executive verdict

**The new principle is right in spirit and wrong in its test.** "Keep as many factors as can explain genuinely different causal stories" replaces an arbitrary cardinality target with a substantive criterion, which is progress. But *causal story* is the wrong unit of adjudication for a factor model. A factor model is not a taxonomy of the world; it is a basis for a cross-section of returns. Two mechanisms that are metaphysically distinct but always produce the same loading pattern across your constituents are, for pricing purposes, one factor wearing two names — and the attribution ledger will assign their split arbitrarily and pretend it didn't. The correct test is: **does this factor's exposure vector across the constituent list fail to be reproduced as a linear combination of the other exposure vectors?** That is a checkable linear-algebra condition, not a narrative one. Every factor below is justified twice: once by mechanism, once by the shape of its column in the exposure matrix.

**The binding constraint in this model is not the number of factors. It is the number of securities.** Eleven constituents cannot cross-sectionally identify thirteen factors, or nine, or arguably more than four. This is the single most important thing in the review. The prior reviewers who said "collapse to two or three" were reasoning correctly from the wrong premise — they were fitting factors to a universe of eleven. You do not need fewer factors; you need a bigger index. A working rule for a model whose exposures are *assigned* rather than estimated is roughly **K ≤ N/3**: forty-five constituents supports fifteen factors comfortably; eleven supports about four. Expand the constituent list to 40–60 practices before promoting the full factor set to the live model, and run the remainder as declared-but-unpriced research factors in the meantime. That is also what real index providers do, and it gives LONGING an institutionally authentic mechanism — a factor promotion committee — rather than a hack.

**The decline is already hard-coded, and not where §10 is looking for it.** There is no negative drift in the parameters, correct. But every one of the eleven constituents is a practice the artist believes is dying. That is a universe-level bias, and no amount of parameter neutrality survives it: an index composed entirely of declining things will decline, and the "analog revival" will always look like a scripted exception because it *is* one — it is the only kind of upward move the universe permits. The fix is to admit practices that are plausibly *gaining*: amateur choirs, run clubs, home cooking, bathhouse and sauna culture, board game nights, community gardens, book clubs, repair cafés, open-water swimming. These are the same species of security — unoptimized, embodied, socially dense, technologically resistible — and several are in real secular expansion. Their presence is what makes the headline index's decline a *finding* rather than a premise. It also gives you structural winners without special pleading.

**The candidate list is not too many or too few; it is unsorted.** The nine families mix three incompatible object types. Time Compression, Human Substitution, Mediation, Uncertainty Compression, Physicality Displacement and Coordination Compression are candidates for **fair-value drivers**: they change what a practice does for people. Friction Premium and Social Legibility are **multiple drivers**: they change what the market pays per unit of value, and belong on the other side of the FV/price distinction the model already correctly makes in §2.1. Scarcity Revaluation is neither — it is an **endogenous transform of the security's own state**, and treating it as an exogenous macro factor is precisely how you get the double-counting §5H worries about. Sorting these three types into separate blocks resolves most of the apparent redundancy without deleting anything.

**Mediation is not a factor.** It is a delivery mechanism. Every mediation event decomposes into at least one of: it accelerates (latency), it predicts or ranks (pre-selection), it removes the body (dematerialization), it schedules (coordination), or it replaces the human (substitution). I could not construct a mediation event that moves none of those — except one, and that one is worth having: a platform that inserts itself between two parties, changes nothing about speed, prediction, physicality or scheduling, and simply takes rent and sets terms. That residual is **commodification**, and it deserves promotion to a factor precisely because it is the one force in the model that pushes fair value and market price in *opposite* directions.

**The proposal is over-focused on technology, and the gap is the demand side.** All nine candidates model the erosion of the *ability* or *necessity* to perform a practice. None model changes in the *desire or capacity* to perform it. Missing entirely: how much uncommitted attention people have; how far apart they live; how many durable ties they hold; whether the supporting infrastructure still exists. These are not decoration. Time affluence is the mechanism by which recessions produce analog revivals. Spatial structure is why dropping in on people died in North America — suburbanization, not smartphones. Infrastructure viability is why film photography nearly ended and then didn't: not because demand vanished, but because manufacturers left and then partially returned. The technology block explains the trend; the demand block explains the cycle and the reversals, and without it the model cannot generate a genuine bull market from its own state.

**Attention Fragmentation should be merged into Time Affluence, and the reason is instructive.** Both are appealing, and their stories are different: hours available versus hours sustainable. But their exposure vectors across the constituents are approximately negatives of one another — every security that gains from spare time loses from fragmented attention, in roughly proportional magnitude. That is collinearity in the only sense that matters here, and it means the ledger would be splitting a single move by an unidentifiable ratio. They merge into **Attentional Slack**, retaining both indicator families underneath. I include this not because it is important on its own but because it is the discipline the brief asks for, applied to a factor I wanted to keep.

**Nine of the thirteen factors below are things you already proposed.** The review is not a rejection. The changes are: sort into three blocks by what they act on; demote Mediation, Scarcity, Cultural Memory, Reversibility, Synchrony and Choice Abundance to indicators, transforms or security fundamentals; promote Commodification out of Mediation's residual; add four demand-side factors; and add one security-level mechanism (infrastructure viability with threshold effects) that the current architecture cannot express at all and that is responsible for a large share of real-world practice death and revival.

**On subjectivity: the bias belongs in the universe and the language, not in the parameters.** Choosing these eleven securities is already an argument. Writing the research in dry institutional prose is already an argument. Once a security is in the index, the parameters must be capable of humiliating the artist. The mechanism that enforces this is not good intentions; it is a pre-registered exposure matrix with a versioned change log, a published override register with a hard annual cap, and the falsification suite in §10. Without those, "the model can disagree with the artist" is an unfalsifiable claim, which is exactly what the art critic will say.

---

## 2. Recommended factor architecture

Sign convention throughout: **exposure β = ∂log(FairValue)/∂Factor**, unless the factor is marked as a multiple factor, in which case **γ = ∂log(Multiple)/∂Factor**. Factors are normalized to mean 0, unit variance in their long-run distribution, and are defined so that "up" means "more of the named thing."

### Block I — Displacement (fair value; predominantly secular)

These change what a practice *does* for people relative to available alternatives.

---

**F1 — Latency Collapse**

*Definition.* The reduction in the socially normal interval between initiating an exchange and completing it, across the economy of ordinary transactions and communications.

*Mechanism.* Practices whose substance is constituted by an interval — the letter that takes four days, the reply that has not come — lose their substance when the interval is removed. Not their function; their substance. A letter that arrives in an hour is a message.

*Behavior.* Secular, monotone, low volatility. Weekly AR coefficient ~0.99 with positive drift; occasional negative shocks (postal retrenchment, infrastructure failure) are genuine and should be permitted.

*Inputs.* OBSERVED: median postal transit time; median messaging reply latency in modeled cohorts; same-day delivery coverage. MODELED: composite latency index. EDITORIAL: none required.

*Correlations.* High with F2 and F5 in the real world (all downstream of the same modernization). Kept separate because their exposure vectors differ sharply on Waiting for a Reply, Unplanned Visit and Handmade Object.

*Why separate.* It is the only factor that loads heavily on Waiting for a Reply through duration, and it is the only Block I factor that has plausible *negative* real-world realizations (a degrading postal service raises latency), which gives it independent time-series behavior.

---

**F2 — Functional Substitution**

*Definition.* The degree to which a non-human process can produce the recognizable output of a practice at fidelity the recipient accepts.

*Mechanism.* If the artifact can be produced without the act, the artifact stops being evidence of the act. This destroys value in two stages: first the labor becomes optional, then the artifact loses its signal.

*Behavior.* Secular with step changes at capability thresholds. Should be modeled as a jump-diffusion, not a smooth trend — capability releases are discrete.

*Inputs.* OBSERVED: capability benchmarks; adoption rates of generative substitutes. MODELED: substitution fidelity by practice. EDITORIAL: the acceptance threshold — at what fidelity recipients stop distinguishing.

*Correlations.* High with F5; separated by the vinyl/AI-letter test in §6.

*Why separate.* It carries a **documented regime switch**: above a threshold of general synthetic saturation, exposure sign flips positive for practices whose value is indexical rather than aesthetic (film photography, live performance). See §10 Test 1. No other factor in the model has this property, and it is the primary engine of non-scripted bull markets.

---

**F3 — Predictive Pre-selection**

*Definition.* The degree to which outcomes, matches and encounters are forecast, ranked, filtered or pre-selected before they are experienced.

*Mechanism.* Some practices are valuable because of what they *do not* determine in advance. Their value is the variance, not the mean. Removing the variance removes the good, even when the mean outcome improves — indeed especially then.

*Behavior.* Secular with strong recent acceleration; regime-dependent on whether the ranking layer is opt-in.

*Inputs.* OBSERVED: recommendation penetration; share of discovery events originating in a ranked feed; reservation and pre-booking share. MODELED: an effective pre-selection index. EDITORIAL: variance-destruction weight per practice.

*Correlations.* Moderate with F1 (both platform-borne) and F4.

*Why separate.* Its support is almost disjoint from F1 and F2. Aimless Walking and Serendipitous Discovery load `--` here and `0` on F1/F2. Without F3 those two securities have no macro driver at all and become pure idiosyncratic noise — which would be a model failure, since they are among the clearest cases in the brief.

---

**F4 — Coordination Formalization**

*Definition.* The degree to which human contact requires prior mutual scheduling, availability signalling or explicit consent, rather than being initiated unilaterally.

*Mechanism.* Unannounced contact is either normal or rude. Where it is rude, the practice does not merely decline in frequency — it changes valence, and each remaining instance imposes a cost on the recipient.

*Behavior.* Mixed. Technologically driven upward trend, but the *norm* component is cyclical and can reverse quickly (a generational backlash against calendar-mediated friendship is entirely plausible and should be reachable by the model).

*Inputs.* OBSERVED: calendar density; share of social contact preceded by a scheduling exchange; location-sharing penetration. EDITORIAL: the norm state — is dropping in currently coded as warm or as a violation.

*Correlations.* Moderate with F3 (both reduce spontaneity) and F1.

*Why separate — with a caveat.* The independence test is clean (§6), and the loading vectors differ: F3 hits Walking and Serendipity hardest with Visit and Call moderate; F4 inverts that ordering and is near zero for Walking. **But its support in the current eleven-security universe is essentially two securities.** A factor supported on two constituents is not a macro factor; it is a security-specific effect with ambitions. F4 should be promoted to the live model only once the universe includes more coordination-sensitive constituents: the standing appointment, the open house, the corner shop, the walk-in barber, the office drop-by. Until then, run it as an unpriced research factor.

---

**F5 — Dematerialization**

*Definition.* The substitution of a physical carrier or embodied co-presence by a non-physical equivalent that delivers the same informational content.

*Mechanism.* Two channels. The obvious one: the physical version loses share and its supporting economy. The less obvious and more important one: as the material becomes optional, the material becomes *chosen*, and a chosen medium carries different information than a default one.

*Behavior.* Secular, but with a **saturation nonlinearity** — the marginal effect on remaining physical practices turns positive at extreme levels, because scarcity of the material makes materiality itself the signal.

*Inputs.* OBSERVED: physical-format unit share; remote-participation share; paper consumption. MODELED: carrier displacement index. EDITORIAL: saturation threshold per practice.

*Correlations.* High with F2. Separated cleanly: lossless streaming replacing vinyl is pure F5 with zero F2; an AI-written letter on real paper, posted, is pure F2 with zero F5.

*Why separate.* The two channels have different signs on Live Performance and Unplanned Visit, and the saturation nonlinearity is what allows physical media and film to be structural winners.

---

### Block II — Conditions (fair value; mixed secular and cyclical)

These change how much people want, and are able, to perform a practice. This block is absent from the current proposal and is where most of the model's non-scripted upside lives.

---

**F6 — Attentional Slack**

*Definition.* The quantity of uncommitted, non-monetized, sustainably continuous attention available to the median participant. Merges the brief's implicit time-availability channel with attention fragmentation.

*Mechanism.* Nearly every constituent practice is attention-expensive relative to its substitute. When slack contracts, the cheap substitute wins on cost alone, independently of any technological displacement. When slack expands, the expensive practice becomes affordable again.

*Behavior.* **Cyclical and regime-dependent**, mean-reverting with a weekly reversion coefficient around 0.04 and occasional multi-year regimes. This is the model's principal source of durable rallies. It is not a trend.

*Inputs.* OBSERVED: median hours worked; second-job incidence; commute time; unemployment; median session length across attention markets; context-switch frequency. MODELED: composite slack index. EDITORIAL: none.

*Correlations.* Weakly negative with Block I over long horizons; **near zero at business-cycle frequency**, which is the point.

*Why separate.* It is the only factor in the model with predominantly positive loadings and mean-reverting dynamics. It functions as the model's market factor. Its universality would be a defect if there were two of them; there is one, and it is what prevents the index from being a one-directional machine.

*Merge note.* Time affluence and attention fragmentation are held as separate observable indicators beneath F6. If their correlation in the modeled world falls below 0.5 for eight consecutive quarters, split them and re-run the collinearity test. Pre-register this criterion rather than deciding it later.

---

**F7 — Spatial Proximity Structure**

*Definition.* The mean physical distance and access cost between socially connected people, and between people and shared public space.

*Mechanism.* Spontaneous physical contact is a function of distance, not of intention. Nobody drops in on a friend forty minutes away, regardless of how much they like them or how few smartphones exist. Distance also *creates* demand for the mediated substitutes, which is why several exposures here are negative.

*Behavior.* Very slow-moving, regime-like, reversible over decades. Should have the lowest volatility of any factor and the longest impulse response.

*Inputs.* OBSERVED: population density of the modeled cohort; walkability scores; mean distance to three closest strong ties; third-place density per capita; remote-work share. MODELED: composite proximity index. EDITORIAL: none.

*Correlations.* Low with everything in Block I. This is the best-conditioned factor in the set.

*Why separate.* Its exposure vector has genuinely mixed signs — `++` for Unplanned Visit, Aimless Walking, Serendipitous Discovery and Live Performance; `-` for Handwritten Letter, Waiting for a Reply, Unplanned Phone Call and Solitude. It is the only factor that is *bad* for correspondence, because correspondence is what distance is for. No linear combination of the other twelve produces that pattern.

---

**F8 — Tie Density**

*Definition.* The number and strength of durable, non-professional, geographically proximate ties held by the median participant. The structural variable, not the emotional outcome.

*Mechanism.* Most constituents are two-person practices requiring a counterparty who will tolerate the imposition. Value scales with the stock of people to whom the practice can be directed.

*Behavior.* Slow secular decline in most modeled scenarios, but explicitly reversible; regime-dependent on household structure and institutional membership.

*Inputs.* OBSERVED: mean confidant count; single-person household share; membership in voluntary associations; residential tenure. MODELED: tie stock. EDITORIAL: strength weighting.

*Correlations.* Moderate with F7 and F9.

*Why separate.* Its divergence from F7 is real in both directions: atomized dense cities, close-knit sparse villages. And its exposure vector inverts F7's on the two most interesting securities — Solitude loads `-` on proximity and `+` on tie density, because solitude requires the *available option* of company. Isolation is not solitude, and the model should be able to tell them apart.

---

**F9 — Generalized Trust** *(conditional promotion)*

*Definition.* The willingness to accept unmonitored exposure to strangers and to unverified contact.

*Mechanism.* Several practices require a stranger-facing risk tolerance that has nothing to do with technology: answering an unknown number, opening the door, talking to someone at the next table, walking at night.

*Behavior.* Cyclical and shock-driven; responds to salient crime, fraud epidemics, and institutional scandal with fast decay and slow recovery — asymmetric, which is a nice modeling detail and matches the empirical literature.

*Inputs.* OBSERVED: fraud incidence; unknown-number answer rate; crime salience in media volume. EDITORIAL: trust regime label.

*Why separate — with a caveat.* Distinct from F8 in support: F9 loads `++` on Serendipitous Discovery and Aimless Walking where F8 is `0`, and F8 loads `++` on Handwritten Letter where F9 is `+`. **This is nonetheless the weakest recommendation in the set** and the pair most likely to fail the collinearity test in §10. Pre-registered merge criterion: if the simulated realizations of F8 and F9 exhibit |ρ| > 0.8 over 5 years, or if F9's exposure vector regresses on the rest with R² > 0.7, merge into a single Social Substrate factor.

---

**F10 — Commodification / Enclosure**

*Definition.* The degree to which a practice is converted into a priced, transacted, platform-intermediated service with a rent-extracting counterparty setting the terms of access.

*Mechanism.* Enclosure does not remove the practice; it changes who controls it and what it is for. A walk sold as a guided mindfulness experience is still a walk, and is worth less as a walk. Meanwhile the enclosed version has capital, distribution and visibility behind it.

*Behavior.* Secular with sector-specific step changes; regime-dependent on capital availability.

*Inputs.* OBSERVED: share of practice instances occurring through a paid intermediary; take rates; resale market share. MODELED: enclosure index. EDITORIAL: the authenticity discount.

*Why separate — and this is the strongest single argument in the review.* **F10 is the only factor whose fair-value exposure and multiple exposure carry opposite signs.** Enclosure lowers what the research institution thinks the practice is worth while raising what the market pays for it, because commodification supplies precisely the things markets reward: liquidity, visibility, measurability and a narrative. This directly exercises the FV/price distinction from §2.1, which is otherwise underused by the factor set. It also produces the model's most interesting single output: a security whose Research Fair Value and Market Price diverge for structural rather than sentimental reasons.

---

### Block III — Valuation regime (multiple; predominantly cyclical)

These change the multiple applied to fair value, not fair value itself. They are the mechanism by which LONGING can be a secular bear market with violent rallies.

---

**F11 — Friction Premium**

*Definition.* The market's current willingness to pay a premium for practices requiring effort, patience, skill, inconvenience or irreversible commitment.

*Mechanism.* Effort is sometimes a cost and sometimes the product. The market's coefficient on effort is not a constant; it is a regime that flips, and its flipping is the best available explanation for analog revivals.

*Behavior.* **Strongly cyclical and regime-switching.** Model as a two-state Markov process, not a mean-reverting diffusion — revivals are regime changes, not oscillations. Expected regime duration 3–8 years.

*Inputs.* OBSERVED: price premia for handmade versus manufactured equivalents; participation in effortful leisure; secondhand analog equipment prices. EDITORIAL: regime label, with the transition probability published.

*Why separate.* Exposure is graded by effort intensity, not uniform: `++` for Handwritten Letter, Film Photography and Handmade Object; `0/+` for Solitude and Unplanned Phone Call. It sits in the multiple block, so it does not compete with F6 in the fair-value equation. **Cascade mechanism:** a friction regime sustained beyond eight quarters feeds slowly into the Cultural Attachment fundamental at a published rate. This is how a multiple-driven rally becomes a fair-value revaluation, and it is how the model produces a multi-year bull market without any scripted exception.

---

**F12 — Status Coding**

*Definition.* How the practice is currently read as a social signal — authentic, tasteful, elite, twee, intrusive, obsolete, performative.

*Mechanism.* Practices are legible. Their legibility is priced independently of their function, and the legibility can invert while the function is unchanged.

*Behavior.* Cyclical, fashion-like, with fast diffusion and slow decay. **Uniquely, its exposures are time-varying by design and can change sign.** Film photography moved from `-` to `++` within a decade with no change in the underlying practice whatsoever.

*Inputs.* OBSERVED: representation frequency in cultural production; demographic skew of new adopters; secondhand price momentum. EDITORIAL: the coding itself, which must remain a scored panel judgment.

*Why separate.* Genuinely mixed signs — `++` for Film Photography and Handmade Object, `--` for Unplanned Visit — and it is the only factor with mutable exposures. That mutability is a serious attribution hazard (§8) and must be handled by fixing exposures within a quarter and booking exposure changes as a separate, labeled ledger line.

---

**F13 — Positioning / Consensus Crowding**

Retained exactly as specified in §2.3 of the brief. It is a price-only, security-level state variable, not a macro factor, and it is deliberately excluded from the exposure matrix. Fast mean reversion, with a convex squeeze response above a crowding percentile threshold. It is the source of the violent upward moves and it must remain incapable of changing fair value — that separation is what makes the short-covering rally legible as a market event rather than a revaluation.

---

### Security-level mechanisms (not factors, but currently missing entirely)

**S1 — Infrastructure Viability, with threshold effects.** Practices do not decline smoothly to zero. They die when the last lab closes, the last manufacturer exits, the last venue loses its licence. This is a step function with hysteresis, and it is responsible for a large share of both real practice deaths and real revivals — film photography's near-death and partial recovery was a supply-side event, not a demand-side one. Model as a per-security state with a viability threshold, a cliff below it, and an asymmetric, slower recovery path. Its absence from the current architecture is the most consequential omission after the demand block.

**S2 — Scarcity transform (demoted from candidate factor H).** Not exogenous. Per-instance value as a function of the security's own prevalence, with an **inverted-U**: rising as the practice becomes rare and distinctive, then falling as it becomes illegible. Vinyl is rare and precious; the telegram is rare and dead. Gated by S3.

**S3 — Cultural Memory.** The stock of living practitioners plus representational presence. A state variable, not a factor. It gates both S2 and F12 — a practice nobody remembers cannot be nostalgic, and cannot be status-coded.

**S4 — Replacement Resistance and Reversibility.** Security attributes that determine the *magnitude* of exposure to F2 and F11 respectively. Attributes, not drivers.

---

## 3. Factors to merge, demote, or delete

| Candidate | Disposition | Reason |
|---|---|---|
| **C. Mediation** | **Delete as a factor.** Its components redistribute to F1, F3, F4, F5, F2; its irreducible residual becomes **F10 Commodification**. | Could not construct a mediation event that moves none of the five, except pure rent extraction — which is a different thing and deserves its own name. Mediation is a delivery channel, not a cause. |
| **H. Scarcity Revaluation** | **Demote to endogenous transform (S2).** | It is a function of the security's own state, not an exogenous condition. Keeping it as a factor guarantees the double counting the brief already worried about. As a transform it gains a non-monotonicity it could not have as a factor. |
| **Attention Fragmentation** *(implied)* | **Merge into F6.** Retained as an observable indicator. | Exposure vector is approximately the negative of time affluence's. Collinear in the only sense that matters. Split criterion pre-registered. |
| **Cultural memory / nostalgia** | **Demote to security state variable (S3).** | It is a stock, not a force. It gates other effects rather than producing its own. |
| **Reversibility / commitment** | **Demote to security attribute (S4).** | Determines exposure magnitude to F11. Has no independent time series. |
| **Bodily effort** | **Demote.** | Fully absorbed by F11 exposure grading and F5. |
| **Synchrony vs asynchrony** | **Demote to observable indicator under F1 and F4.** | The one genuine residual — loss of shared simultaneous experience — is absorbed by F6 and F5 with no measurable remainder. |
| **Abundance of choice** | **Demote to observable indicator under F3.** | Instructive: unlimited catalogue *without ranking* would *increase* serendipity. Choice is only corrosive through the ranking layer, which is F3. Making it a factor would get the sign wrong. |
| **Regulation / institutionalization** | **Demote to event class.** | Genuine but low-frequency, and always transmits through F1, F10 or S1. Model as an event that shocks those, not as a standing factor. |
| **Loneliness / social fragmentation** | **Promote, redefined, as F8.** | Correct instinct, wrong variable. Loneliness is an *outcome*; tie density is the structural cause and is what should be priced. Pricing the outcome would double count with the securities themselves. |
| **Trust** | **Promote conditionally as F9.** | Distinct support, weakest case in the set, pre-registered merge criterion with F8. |
| **Commodification** | **Promote to F10.** | Earns its slot on the FV/price sign split alone. |
| **Geographic distance** | **Promote as F7.** | The brief asks whether it matters independently of mediation. It does, and it is one of the largest real drivers of the decline in unplanned contact. |
| **Economic scarcity of time** | **Promote as F6 (merged).** | The brief asks whether this deserves separation from technological time compression. Emphatically yes: they have *opposite signs* on several securities and near-zero correlation at cycle frequency. This is the strongest non-redundancy case in the whole review. |

---

## 4. Missing factors and mechanisms

Beyond those promoted above, four gaps remain worth naming.

**Infrastructure viability with threshold effects (S1).** Discussed above. Its absence means the model cannot express the most common way practices actually die, and cannot express the supply-side revival.

**Demographic composition.** Not a factor in itself, but the exposure matrix should be **age-cohort weighted**, because several exposures differ in sign by cohort. Unplanned phone calls are a violation for one cohort and normal for another; film photography is nostalgia for one and novelty for another. An index whose exposures are cohort-invariant will systematically mis-price generational reversals — which are the main source of revivals. Implement as cohort-weighted exposures rather than as an additional factor.

**Institutional carriers.** Practices survive when an institution maintains them: the postal service, the church choir, the school darkroom, the public library, the licensed venue. This is adjacent to S1 but distinct — S1 is commercial supply, this is institutional maintenance. In the interest of parsimony I would fold it into S1 as a second input rather than a separate mechanism, but flag it explicitly because it is a common real-world cause of both death and preservation and it is entirely absent from the current design.

**Documentation intensity.** The degree to which experience is recorded and shared as a matter of course. Distinct from F5 and F2: it does not dematerialize the practice or replace the human, it changes the practice's relationship to its own audience. Aimless walking that is photographed and posted is a different security. I do **not** recommend promoting this to a factor — its exposure vector is too close to F10's, and it would not survive the collinearity test — but it should exist as an observable indicator feeding F10 and F12, and it is worth revisiting if the universe expands.

---

## 5. Exposure matrix

Split by block for legibility. Sign convention as above; Block III entries are multiple exposures.

### Block I — Displacement (∂log FV)

| Security | F1 Latency | F2 Substitution | F3 Pre-selection | F4 Coordination | F5 Dematerialization |
|---|:--:|:--:|:--:|:--:|:--:|
| Handwritten Letter | `--` | `--` | `0` | `+` | `--` |
| Waiting for a Reply | `--` | `0` | `-` | `0` | `0` |
| Unplanned Phone Call | `-` | `-` | `0` | `--` | `0` |
| Unplanned Visit | `0` | `0` | `-` | `--` | `-` |
| Aimless Walking | `0` | `0` | `--` | `0` | `0` |
| Film Photography | `-` | `--` † | `-` | `0` | `--` † |
| Physical Media | `-` | `-` | `-` | `0` | `--` † |
| Serendipitous Discovery | `0` | `0` | `--` | `-` | `-` |
| Handmade Object | `-` | `--` | `0` | `0` | `--` |
| Live Performance | `0` | `-` † | `-` | `-` | `-` † |
| Solitude | `0` | `0` | `0` | `+` | `0` |

† Documented sign-flip above a pre-registered saturation threshold. See §10 Test 1.

### Block II — Conditions (∂log FV)

| Security | F6 Attentional Slack | F7 Proximity | F8 Tie Density | F9 Trust | F10 Commodification |
|---|:--:|:--:|:--:|:--:|:--:|
| Handwritten Letter | `++` | `-` | `++` | `+` | `-` |
| Waiting for a Reply | `++` | `-` | `+` | `0` | `0` |
| Unplanned Phone Call | `+` | `-` | `++` | `++` | `0` |
| Unplanned Visit | `+` | `++` | `++` | `++` | `0` |
| Aimless Walking | `++` | `++` | `0` | `+` | `-` |
| Film Photography | `+` | `0` | `+` | `0` | `-` |
| Physical Media | `++` | `+` | `+` | `0` | `-` |
| Serendipitous Discovery | `+` | `++` | `0` | `++` | `--` |
| Handmade Object | `++` | `+` | `+` | `+` | `--` |
| Live Performance | `+` | `++` | `+` | `+` | `--` |
| Solitude | `++` | `-` | `+` | `0` | `-` |

### Block III — Valuation regime (∂log Multiple)

| Security | F11 Friction Premium | F12 Status Coding | F10 (multiple leg) |
|---|:--:|:--:|:--:|
| Handwritten Letter | `++` | `+` | `+` |
| Waiting for a Reply | `+` | `0` | `0` |
| Unplanned Phone Call | `+` | `-` | `0` |
| Unplanned Visit | `+` | `--` | `0` |
| Aimless Walking | `+` | `+` | `+` |
| Film Photography | `++` | `++` | `+` |
| Physical Media | `+` | `++` | `+` |
| Serendipitous Discovery | `+` | `+` | `+` |
| Handmade Object | `++` | `++` | `++` |
| Live Performance | `+` | `+` | `++` |
| Solitude | `0/+` | `+` | `+` |

### Surprising exposures, explained

**Handwritten Letter is `+` on Coordination Formalization.** As spontaneous contact becomes socially costly, asynchronous unsolicited contact that imposes no scheduling obligation becomes one of the few remaining permitted forms. Formalization kills the phone call and partially rescues the letter. This is the exposure I would most want a hostile reviewer to attack, and it is also the one that best demonstrates the factor is doing real work rather than applying a uniform modernization discount.

**Handwritten Letter, Waiting for a Reply and Unplanned Phone Call are `-` on Spatial Proximity.** Correspondence is what distance is *for*. Densification reduces the need for it. This is the clearest case in the model of a factor that is good for the index overall and bad for specific constituents, and it is why F7 is the best-conditioned column in the matrix.

**Solitude is `+` on Tie Density and `-` on Spatial Proximity.** Solitude is the chosen absence of company, which requires company to be available and requires physical room to withdraw into. Isolation in a crowded city with no ties is not solitude; it is a different and worse thing, and the model should price it as such. If your matrix cannot distinguish solitude from isolation, it is not modeling solitude.

**Solitude is `+` on Coordination Formalization.** A fully scheduled social life makes unscheduled time reliably one's own. This is a small positive and it is the kind of second-order exposure that should be flagged as low-confidence in the ledger rather than asserted at full magnitude.

**Waiting for a Reply is `-` on Predictive Pre-selection, not only on Latency.** Read receipts, typing indicators and delivery confirmations do not shorten the wait; they *resolve* it. The security's substance is uncertainty as much as duration, and it therefore loads on two Block I factors through two different channels. That double loading is legitimate and must be booked as two separate ledger lines, not one.

**Unplanned Visit is `--` on Status Coding.** In the current regime, arriving unannounced is read as a boundary violation rather than as warmth. This exposure is time-varying and has been positive within living memory, which is exactly the property that makes F12 valuable and dangerous.

### Matrix condition — honest assessment

Three columns have low cross-sectional dispersion: **F6** (all positive), **F10 fair-value leg** (all negative or zero) and **F11** (all positive). They are distinguished from each other only by magnitude gradient and by block membership, not by sign pattern. In an eleven-security universe they will fail a strict collinearity test. They are separable in principle — F6 is a fair-value factor with mean-reverting dynamics, F11 is a multiple factor with regime-switching dynamics, F10 has opposite signs across the FV/price boundary — but "separable in principle" is exactly the claim that pseudo-quantitative models make. **Do not present all three as independent priced factors on a universe of eleven.** Expand the universe first, then test.

---

## 6. Independence tests

Mandatory section. Each test isolates one factor while a named neighbour stays still.

**F1 vs F2.** A national postal service restores next-day delivery on all domestic mail; generative writing capability is unchanged. Latency Collapse rises sharply; Functional Substitution does not move at all. Conversely: a handwriting-robot service launches that produces genuinely indistinguishable ink-on-paper letters, posted through the same unchanged mail system. F2 jumps; F1 is flat. Both directions clean.

**F2 vs F5.** A streaming service ships bit-perfect lossless audio with spatial mixing, and vinyl pressing capacity is unchanged. Dematerialization rises; Functional Substitution is flat — the same humans made the same music. Conversely: fully synthetic performers top the charts on physical vinyl releases. F2 jumps; F5 is flat.

**F3 vs F4.** A dating platform removes browsing entirely and serves one algorithmically selected match per day. Predictive Pre-selection rises; Coordination Formalization is unchanged — meeting still requires the same scheduling. Conversely: a norm emerges among a cohort that calling without texting first is rude, with no new technology deployed and no ranking layer involved. F4 rises; F3 is flat. This second case is the important one, because it shows F4 has a purely normative channel that F3 cannot reach.

**F5 vs F7.** Remote work becomes permanent at large employers and households disperse to lower-density areas. Spatial Proximity falls sharply. Dematerialization rises only modestly — the tools were already deployed. The magnitudes are what separate them; the transmission chain must be booked explicitly (see §7, event 11).

**F6 vs F1.** A large economy legislates a four-day week. Attentional Slack rises substantially. Latency Collapse does not move — delivery is not slower, replies are not later. This is the cleanest independence test in the model and the reason time affluence must not be folded into time compression. Conversely: same-day delivery reaches universal coverage while median hours worked rise. F1 up, F6 down. **Opposite signs on the same week.** Any architecture that merges these produces zero net move and explains nothing.

**F7 vs F8.** A dense city experiences high residential turnover: proximity unchanged, mean tie tenure collapses. F8 falls, F7 flat. Conversely: a stable rural community disperses geographically while maintaining contact. F7 falls, F8 roughly flat.

**F8 vs F9.** A widely reported phone-fraud epidemic targets a demographic cohort. Generalized Trust drops sharply; tie structure is completely unchanged — the same people know the same people. Unplanned Phone Call falls hard through F9 alone. This is the test that justifies F9's conditional promotion, and if the modeled world cannot generate this scenario, merge F9 into F8.

**F10 vs F5.** A ticketing platform introduces universal dynamic pricing and consolidates resale. Commodification rises; nothing is dematerialized — the concerts are identical, in the same rooms, with the same bodies. Fair value falls, market price rises. No other factor produces that combination.

**F11 vs F12.** A cohort-wide backlash against "authenticity performance" makes visible effort read as pretentious, while willingness to *undertake* effort in private stays high. Status Coding falls; Friction Premium is flat. Conversely: a deep recession makes effortful home production broadly attractive without any change in what it signals. F11 rises; F12 flat.

**F11 vs F6.** A friction-premium regime switch occurs during a period of contracting attentional slack — the market rewards effort at precisely the moment people have less capacity for it. Multiples expand while fair values contract, and price goes sideways with a large, fully attributable offsetting ledger. That decomposition is the single best demonstration that the two blocks are doing different work.

**F3 vs F6.** Route optimization reaches universal adoption during a period of expanding leisure time. F3 up, F6 up. Aimless Walking's fair value moves by the net of a `--` and a `++` exposure. If the model cannot produce sideways-with-large-offsetting-attribution here, the blocks have collapsed into one.

**F12 exposure mutability test.** Film photography's status coding moves from `-` to `++` over five modeled years with no change in F12's *level* — the factor is flat, the exposure rotated. This must appear in the ledger as an "Exposure Revision" line, never as a factor return. If it appears as a factor return, the attribution is lying.

---

## 7. Event classification examples

Twelve events, with double-counting flags.

**1. A national postal service cuts delivery to three days per week.**
F1 **down** (latency increases — bullish for Handwritten Letter and Waiting for a Reply on substance). S1 Infrastructure Viability **down** (bearish for the same securities on practicality).
⚠️ *Two-sided.* The Event Desk's default instinct will be to book this once as bearish. It is not one event; it is two effects with opposite signs and different half-lives. Require both legs, booked separately, with the net left to the model.

**2. An AI service launches producing indistinguishable ink-on-paper handwritten letters, physically posted.**
F2 **up** only.
⚠️ Do **not** book F5 — nothing was dematerialized. Do **not** book F1 — delivery is unchanged. This event exists in the test suite specifically to catch Desks that book all modernization events across all modernization factors.

**3. A streaming service ships lossless audio; vinyl pressing capacity unchanged.**
F5 **up** only. F2 flat.

**4. A major city adopts fifteen-minute-city zoning across its core.**
F7 **up** only.
⚠️ No technology factor moves. If the Desk books anything in Block I here, the classification rubric has failed.

**5. A large economy legislates a four-day working week.**
F6 **up** only.
⚠️ Do **not** book F11. Friction Premium is what the market *pays* for effort; this event changes what people *can afford* to do. Confusing the two collapses Blocks II and III.

**6. A dating platform removes browsing and serves one algorithmic match per day.**
F3 **up** (large). F4 **up** (small).
⚠️ Moderate double-count risk with F2 — the algorithm is not producing the human, only ranking them. Do not book F2.

**7. A viral trend makes disposable film cameras fashionable among a teenage cohort.**
F12 exposure revision for Film Photography **up**. **No macro factor moves.**
⚠️ *Highest-frequency double-count risk in the model.* The Desk will want to book Friction Premium. **A single-security cultural event cannot move a macro factor.** F11 is an economy-wide revaluation of effort; one practice going viral is a security-level narrative state change. Rule: a Block III factor move requires evidence of co-movement across at least three constituents in different Block I exposure profiles. This rule alone prevents most of the attribution corruption I would expect this model to suffer.

**8. A manufacturer discontinues its last colour reversal film stock.**
S1 Infrastructure Viability **down**, crossing a threshold. S2 Scarcity transform activates.
⚠️ Do **not** book F5 — this is a supply-side exit, not a dematerialization event. Do **not** book F2. If threshold is crossed, expect a discontinuous fair-value move and a possible positioning squeeze; both must be labeled as such in the ledger.

**9. A reported fraud epidemic targets an elderly cohort by telephone.**
F9 **down** only. F8 flat.
Unplanned Phone Call falls hard through a single channel. Clean single-factor event; useful as a ledger integrity check.

**10. A ticketing platform introduces universal dynamic pricing and consolidates the resale market.**
F10 **up**. Live Performance fair value **down**, market price **up**.
The canonical FV/price divergence event. Publish both legs on the same ledger page.

**11. Remote work becomes permanent policy at large employers.**
F7 **down**. F6 **up**. F8 **down**.
⚠️ *Highest overall double-count risk.* Three factors, one press release. Require the Desk to write out the transmission chain explicitly — dispersal → distance; commute recovery → slack; residential churn → tie erosion — and to assign three independent magnitudes with three independent confidences. If the Desk cannot articulate the chains separately, it should book only F7 and let the others arrive through observed indicators later.

**12. A national census reports single-person households passing forty percent.**
F8 **down**.
⚠️ Do **not** book Solitude as a beneficiary. Solitude loads `+` on tie density; this event is *bearish* for Solitude's fair value even though it superficially describes more people being alone. This is the model's best single illustration of why structural variables must be priced rather than outcomes, and it should be in the Event Desk's training set.

---

## 8. Attribution design

### The decomposition

Work in logs and split at the FV/price boundary, which the architecture already provides:

```
Δ log P_i,t  =  Δ log FV_i,t  +  Δ log M_i,t  +  Δ log Q_i,t

Δ log FV_i,t =  Σ_k β_ik ΔF_k,t          (Blocks I and II)
             +  ΔS2_i,t                   (scarcity transform)
             +  ΔS1_i,t                   (infrastructure)
             +  ε_i,t                     (idiosyncratic fundamental)

Δ log M_i,t  =  Σ_j γ_ij ΔF_j,t          (Block III)
             +  Δ narrative_i,t

Δ log Q_i,t  =  positioning / crowding adjustment (F13)
```

### Exactness

A first-order sum will not be exact, because exposures are state-dependent, several have documented thresholds, and the multiple compounds with fair value. **Use a Shapley decomposition over the factor set for the published ledger.** It is exact by the efficiency axiom, it is order-independent — which matters, because a sequential decomposition lets whoever picks the ordering pick the story — and it is defensible to a methodology committee, which a hand-assigned interaction line is not. At K ≈ 13 the exact computation is 8,192 evaluations per security per week, which is trivial; above K = 20, switch to sampled Shapley with published standard errors.

Consequence: **the "Interaction / Residual" line in the brief's example ledger becomes structurally zero and should be removed.** Interactions are distributed into the factor lines by construction. Keeping an interaction line while using Shapley would be double reporting.

### Correlated factor moves

Shapley solves exactness but not interpretability: when F1, F2 and F5 all move together, the ledger will show three large lines that a reader will misread as three findings. Publish the ledger in **two bases**:

```
LTR — WEEKLY RETURN                              +13.84%

  COMMON MODERNIZATION (PC1)                      -4.90%
  ORTHOGONALIZED FACTOR CONTRIBUTIONS
    Latency Collapse        (resid)               -0.31%
    Functional Substitution (resid)               -1.12%
    Predictive Pre-selection(resid)               +0.08%
    Coordination Formaliz.  (resid)               +0.44%
    Dematerialization       (resid)               -0.19%
    Attentional Slack                             +1.21%
    Spatial Proximity                             -0.06%
    Tie Density                                   -0.22%
    Generalized Trust                              0.00%
    Commodification         (FV leg)              -0.38%
  ─────────────────────────────────────────────
  FAIR VALUE CHANGE                               -5.45%

    Friction Premium                              +3.10%
    Status Coding                                 +1.21%
    Commodification         (multiple leg)        +0.19%
    Narrative state                               +4.31%
  ─────────────────────────────────────────────
  MULTIPLE CHANGE                                 +8.81%

    Positioning / short covering                  +9.72%
  ─────────────────────────────────────────────
  PRICE-ONLY CHANGE                               +9.72%

    Unattributed                                  +0.76%
  ─────────────────────────────────────────────
  TOTAL                                          +13.84%
```

Block I factors are reported orthogonalized against their first principal component, with that component published as its own line. This concedes the original reviewers' point exactly where it is true — the Block I factors *are* highly correlated — while preserving them as distinct causal objects, because a factor's causal identity does not require its realization to be orthogonal. **Keep the factors in the causal layer; report attribution in the orthogonalized basis.** Publish the rotation matrix quarterly so the transformation is auditable.

### Residual

In a simulated world, the residual is a design choice, not a measurement error. If the model generates the world and then explains it, the residual is exactly zero — and a ledger that explains 100% of its own returns every week is the purest form of the pseudo-quantitative theater §9 warns about. **Deliberately inject an idiosyncratic fundamental shock ε and let it print as "Unattributed."** Target: unattributed variance between 5% and 15% of total return variance, monitored quarterly. Below 5%, the model is a tautology. Above 25%, the factors are not doing the work.

### Delayed pricing

Factor moves should not price instantaneously. Maintain a **pending-impulse pipeline**: each factor shock is distributed over a security-specific impulse response (typically 2–12 weeks, longer for F7, immediate for F13). The ledger then reads a current-week slice of past events, and the pipeline itself is published:

```
Functional Substitution     -1.12%
  of which 2026-W31 event   -0.71%  (week 3 of 8)
  of which 2026-W34 event   -0.41%  (week 1 of 6)
```

This is unusual for a research terminal and would be genuinely rigorous. It also makes the model auditable in the strongest sense: a reader can verify that no event was booked twice.

### Confidence

Each event carries a confidence. Confidence enters as a **shrinkage on immediate price impact and an increase in the residual variance of the pending impulse**, not as a footnote. Low-confidence events price at a fraction of their magnitude and resolve later. When they resolve, the correction prints on its own line:

```
Confidence Revision (2026-W29 event, conf 0.35 → 0.80)   -0.44%
```

### Exposure revisions

Because F12's exposures are mutable by design and cohort weighting will drift, exposure changes must never appear as factor returns. Freeze exposures within a quarter; book changes on the quarterly review date as a separate, labeled line with a link to the methodology change log. A model that silently rotates its exposures is unfalsifiable.

---

## 9. Complexity risks — where this becomes theater

Explicit warning signs, each with a monitored threshold.

**A factor's exposure vector regresses on the others with R² > 0.7.** It is a linear combination wearing a name. On the current eleven-security universe, F6, F10-FV and F11 will likely trip this. Merge or expand the universe.

**A factor's attribution line is below the unattributed line in more than 80% of weeks.** It is decoration. It has never changed a decision and never will.

**A factor has never printed with the opposite sign to PC1.** If a factor has never once disagreed with general modernization, it has no independent existence. This is the sharpest single diagnostic and the one that would have caught the original seven variables immediately.

**More factors than N/3 constituents.** Currently 13 factors on 11 securities. This is the model's present state and it is not defensible. It is a universe problem, not a factor problem, but it must not ship.

**Exposures edited after a price move.** The single most corrosive failure mode, because it is undetectable from outside without a change log. Require a versioned, timestamped exposure matrix, quarterly-only revision, and a published diff. Any intra-quarter revision requires a written justification in the Override Register.

**Displayed precision exceeding input resolution.** `Cultural Attachment 76.4` derived from a five-point analyst panel is theater. The correct fix is *not* to round to 76 — false precision is part of the artistic surface and should stay. The fix is to publish the input resolution and the inter-rater dispersion beside the number: `76.4 (panel n=5, σ 8.2, scale 1–100 anchored)`. **Publish the dispersion, not just the consensus.** Real research does this and it is the single cheapest thing LONGING can do to survive the art critic. The dry institutional surface becomes more convincing, not less, when it admits its own error bars.

**Editorial inputs that never contradict the artist.** If every editorial judgment ever entered has moved prices in the direction the artist expected, the editorial layer is not an input, it is a signature.

**The seven-variables failure returning under new names.** Run the PC1 test annually. If the first principal component of factor realizations exceeds 75% of variance, the model has silently collapsed back to one factor regardless of how many are printed.

**Threshold and regime-switch exposures added after the fact.** The sign flips marked † in §5 are the model's most powerful device and its most abusable one. They must be pre-registered with their thresholds *before* the path that triggers them is run. A threshold discovered because it was needed to explain a move is a fitted parameter pretending to be a mechanism.

---

## 10. Falsification tests

**Test 1 — Film photography revival.** Run the model over a modeled 2005–2026 with historically plausible factor inputs. Required: a trough followed by a genuine multi-year rally with a positive cumulative return over the last decade of the window, and a decomposition in which the rally is driven by the F2 sign flip (synthetic saturation restoring indexical value), F12 status rotation, S2 scarcity and F11 regime, *not* by an idiosyncratic term. **Fails if:** film can only decline, or if the rally is more than 40% unattributed, or if it requires a manual override.

**Test 2 — Structural winner.** Run 500 simulated 10-year paths with parameters drawn from their prior distributions and no path-specific tuning. Required: in at least 60% of paths, at least one constituent finishes above +50% cumulative; across all paths, at least four distinct constituents achieve this in some path. **Fails if:** the winners are always the same one or two securities (the model has a favourite, not a mechanism), or if zero paths produce a winner (drift is hard-coded somewhere, most likely in the universe).

**Test 3 — Collinearity.** Three parts. (a) Condition number of the exposure matrix < 20. (b) Each factor's exposure vector regressed on all others: R² < 0.7. (c) PCA of simulated factor *realizations*: PC1 < 75% of cross-sectional return variance. **Fails if:** any part trips. Expected current result: fails (b) on F6/F10/F11 and possibly F8/F9, and fails (a) on eleven securities. The prescribed response is to expand the universe and retest, not to delete factors.

**Test 4 — Attribution integrity.** Four parts. (a) Shapley lines sum to the weekly return to machine precision. (b) Reconstruct 52 weeks of price from the ledger alone; must match the simulated path exactly. (c) Leave-one-factor-out: removing any factor must measurably degrade cross-sectional explanatory power; if removing a factor changes nothing, delete it. (d) Replay the event log against the pending-impulse pipeline and confirm no event contributes twice. **Fails if:** any part fails.

**Test 5 — Model versus artist.** Pre-register, before any simulation, the artist's ranked ordering of the eleven securities by expected 5-year performance, sealed. Run the model. Required: Spearman correlation between model output and the sealed prior **below 0.8**, and at least two documented cases where the model produced a result the artist disliked and it was not overridden. Maintain an **Override Register** with a hard cap of two overrides per year, each requiring a written dissent published in the methodology appendix. **Fails if:** correlation exceeds 0.8, or the override cap is exceeded, or the register is empty after two years — an institution that has never disagreed with itself is not an institution.

**Test 6 — Exposure shuffle.** Randomly permute the exposure matrix rows across securities and re-run. Show the resulting price paths and ledgers to a naive reader alongside the real ones. **Fails if:** the reader cannot distinguish them at better than chance. If the exposures do not produce recognizably different behavior per security, they are ornament.

**Test 7 — Zero-information.** Replace every EDITORIAL input with its unconditional mean and re-run. Required: a substantial but not total drop in explained variance — roughly 25–50%. **Fails if:** almost nothing changes (the editorial layer is theater) or almost everything changes (the model is the artist's opinion with extra arithmetic, and the observable layer is theater instead).

**Test 8 — Opposite-sign week.** Construct the F6-up / F1-up scenario from §6 and verify that at least three securities print near-zero returns with large offsetting ledger lines. **Fails if:** the offsetting behavior cannot be produced, which would indicate Blocks I and II have collapsed.

---

## 11. Proposed v2 specification

### Pipeline

```
L0  OBSERVABLE INDICATORS                    weekly / monthly, tagged O | M | E
      postal transit · reply latency · same-day coverage
      capability benchmarks · substitute adoption
      recommendation penetration · pre-booking share · catalogue size
      calendar density · location sharing · scheduling norm state (E)
      physical format share · remote participation share
      hours worked · unemployment · session length · context switches
      density · walkability · third places · distance to ties · remote share
      confidant count · household composition · association membership
      fraud incidence · unknown-number answer rate
      intermediary share · take rates · resale share
      craft price premia · effortful-leisure participation
      representation frequency · adopter age skew · secondhand momentum
                                    ↓
L1  LATENT FACTORS                           F1–F12 state processes, weekly
      Block I  F1 F2 F3 F4 F5     secular    φ≈0.99, μ>0, F2 jump-diffusion
      Block II F6 F7 F8 F9 F10    mixed      F6 φ=0.96 μ=0; F7 φ=0.998
      Block III F11 F12           cyclical   F11 two-state Markov; F12 fashion
      + common innovation: ε_k,t = λ_k u_t + ν_k,t   (λ high for Block I)
                                    ↓
L2  EXPOSURE MATRIX  B (N×12), Γ (N×3)       versioned, quarterly revision only
      cohort-weighted; documented threshold flips; frozen intra-quarter
                                    ↓
L3  SECURITY FUNDAMENTALS                    monthly research cycle
      prevalence · S1 infrastructure viability (threshold, hysteresis)
      S3 cultural memory · S4 replacement resistance / reversibility
      cultural attachment (E, panel-scored, dispersion published)
                                    ↓
L4  RESEARCH FAIR VALUE                      monthly, with weekly marks
                                    ↓
L5  NARRATIVE / MULTIPLE                     weekly
                                    ↓
L6  POSITIONING / CROWDING  F13              weekly, fast reversion, convex squeeze
                                    ↓
L7  WEEKLY PRICE + SHAPLEY LEDGER            weekly close
      two-basis reporting · pending-impulse pipeline · unattributed 5–15%
```

### Core equations

**Factor dynamics.**
```
F_k,t = F_k,t-1 + μ_k + φ_k(F̄_k − F_k,t-1) + σ_k(λ_k u_t + ν_k,t) + Σ_e shock_k,e,t
```
Secular factors: φ_k ∈ [0, 0.01], μ_k > 0. Cyclical: μ_k = 0, φ_k ∈ [0.02, 0.10]. F7: φ = 0.002, σ smallest in the set. F11 replaces this with a two-state Markov switch, transition probabilities published.

**Prevalence.**
```
log Prev_i,t = log Prev_i,t-1 − Σ_k θ_ik ΔF_k,t + η_i,t
```
θ ≠ β. Prevalence responds to displacement; value does not respond identically, and the gap between them *is* the scarcity mechanism.

**Scarcity transform (inverted-U, memory-gated).**
```
S2_i,t = a_i · Memory_i,t · Prev_i,t^α · exp(−Prev_i,t / p*_i)
```
Rises as prevalence falls toward p*, then collapses as Memory decays. This is what distinguishes vinyl from the telegram, and it is the single most important non-monotonicity in the model.

**Infrastructure viability (threshold with hysteresis).**
```
S1_i,t = 1                          if V_i,t > v_high
       = (V_i,t / v_low)^κ          if V_i,t < v_low        [cliff, κ > 1]
       = previous state             otherwise                [hysteresis band]
```
Recovery path slower than decline path by a published asymmetry factor. Threshold crossings print as discrete ledger events.

**Fair value.**
```
log FV_i,t = c_i + Σ_k β_ik(cohort, regime) F_k,t
                 + s_i S2_i,t + w_i log S1_i,t + Attach_i,t + ε_i,t
```

**Multiple.**
```
log M_i,t = m_i + Σ_j γ_ij F_j,t + Narr_i,t
```

**Price.**
```
log P_i,t = log FV_i,t + log M_i,t + q(Crowd_i,t)
q convex above the squeeze threshold; q is mean-zero over long horizons by construction
```

**Cascade.** If F11 remains in the high-friction state for more than 8 quarters, `Attach_i` accrues at a published rate ρ per quarter, weighted by γ_i,F11. This converts a sustained multiple regime into a fair-value revaluation and is the model's licensed path to a multi-year bull market.

### What must remain subjective, and how it is disciplined

Four things should stay editorial and should be visibly labeled as such: **the exposure matrix** (versioned, diffed, frozen intra-quarter); **Cultural Attachment** (panel-scored against a published anchored rubric, with n and σ printed beside every value); **Status Coding** (panel, with the current coding and its history published, since the exposure is mutable); and **event direction** (the Desk classifies relevance, magnitude and confidence; analysts assign direction and may dissent on the record, per §2.4). Everything else should be observed or modeled. The discipline is not that these become objective — they cannot — but that they are reproducible, dated, dispersed and overridable only on the record.

### Structural winners the architecture can produce

**Live Performance.** Loads `++` on Spatial Proximity and `+` on Attentional Slack in Block II; benefits from the F2 and F5 sign flips as synthetic and streamed substitutes saturate (the value of the non-reproducible rises as the reproducible becomes free); gains from S2 as recorded music becomes unlimited. Its only strong negative is F10, and F10's multiple leg is `++`. A decade in which cities densify, a friction regime is on, and synthetic media saturates produces a sustained bull market in Live Performance *while the headline index falls*, entirely from factor states.

**Film Photography.** Above the synthetic-saturation threshold, F2 flips positive — when any image can be generated, a chemical image becomes evidence in a way a digital file is not. Combine with the F5 saturation flip, an S2 scarcity premium in the rising region of the inverted-U (prevalence low, memory still high), a `++` status coding, and `++` friction exposure. The rally is model-generated, not scripted, and Test 1 verifies it.

**Solitude** is the third candidate: near-zero Block I exposures, `++` on Attentional Slack, positive on tie density and status. In an attention-backlash regime it can be the index's best performer for years.

That three of eleven securities can win is adequate. But the universe expansion in §1 is what makes this credible rather than convenient: with rising practices in the index, an upward move is a finding rather than a rescue.

### Build order

1. **Expand the constituent universe to 40–60 practices, including practices in genuine secular expansion.** Nothing else in this specification is defensible until this is done.
2. Implement Blocks I and III plus F6 and F13 — nine priced factors, which a 45-security universe supports comfortably. Run F4, F7, F8, F9, F10 as declared, published, *unpriced* research factors with a documented promotion committee and criteria.
3. Implement S1, S2, S3 with pre-registered thresholds.
4. Build the Shapley ledger with the two-basis presentation and the pending-impulse pipeline before running any long simulation, so that the first path you look at is already auditable.
5. Run the falsification suite. Publish the results, including the failures, as the first State of LONGING. An institution whose founding document reports its own model's failed tests is more convincing than one that does not — and it is the only version of this project the art critic cannot dismiss.
