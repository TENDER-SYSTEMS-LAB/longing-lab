# LONGING — Factor Architecture Review v2

---

## 1. Executive verdict

The v1 critique was correct: Efficiency, Automation, Predictability, Mediation, Immediacy, Digitization, and Optimization are seven names for one thing — the forward march of a particular kind of world. As independent pricing factors they would produce a model in which everything falls together for the same reason, attribution becomes decoration, and the weekly ledger tells one story seven times. The reviewers who proposed collapsing the macro layer to one or three factors were right about the diagnosis and wrong about the cure.

The new principle — *keep as many factors as can explain genuinely different causal stories* — is the right principle. But the candidate set of nine families does not yet satisfy it, because the list conflates three kinds of entities that must live on different layers:

- **World pressures** (macro factors): forces acting on all securities from outside — speed infrastructure, attention capture, substitution capability, and so on.
- **Market regimes** (valuation-state factors): demand-side conditions that determine how the market *rewards or punishes* a given exposure — patience, status, taste. These are not forces on the world; they are forces on the price of the world.
- **Security fundamentals**: attributes and state variables of each practice — its prevalence, its cohort transmission, its habitat assets (labs, record shops, venues), its substitutability, its rarity elasticity.

Scarcity Revaluation, for example, is not a macro factor; it is a valuation response to a fundamental (prevalence) whose decline is *caused by* the macro factors. Pricing it as a parallel factor guarantees double counting: the practice declines because time compression rose, and then "scarcity revaluation" rises because the practice declined — one cause enters the ledger twice with opposite signs. The same category error, in milder form, affects two or three other candidates.

The candidate set is therefore **not too many and not too few — it is misclassified**. Roughly: five or six families are legitimate macro pressures; two (Friction Premium and Social Legibility) are facets of one regime factor that should nonetheless be kept visible as sub-indices; one (Coordination Compression) is an indicator cluster inside a broader force that the candidates entirely miss; and one (Scarcity Revaluation) belongs in the valuation layer.

More importantly, the candidate set is over-focused on **technology**. It models the world as if practices die only because machines replace them. But handwritten letters, unplanned visits, and aimless walking are also being killed by:

- the **economic scarcity of unhurried time** (a labor-and-calendar condition, not a technology);
- the **colonization of attention** (you can have a free Saturday and still never be mentally present);
- the **destruction of the physical and relational substrate** of spontaneous encounter (distance, rent, the death of third places, scheduling norms — this is where Coordination Compression actually lives, and it is where urbanization, trust, and loneliness belong);
- the **demand-side collapse of patience** — a discount rate on slow rewards. This is the closest thing LONGING has to a policy rate, and it is the single most important missing factor, because it is the only mechanism by which the *entire index* can rationally rally for a decade without any technological retreat.

With these additions, and with a disciplined identification rule (each factor must own a class of events that moves no other factor as primary — "identification by event signature"), a set of roughly ten macro factors is defensible and each one earns its place. The model does not need to be simple. It needs to be *identified*. Complexity without identification is the pseudo-quantitative theater the art critic correctly fears; complexity with identification is exactly the aesthetic LONGING wants.

Finally: the architecture as sketched can satisfy the no-hard-coded-decline requirement, but only if the secular drift in the pressure factors is treated as an *editorial prior with uncertainty* rather than a constant, and if the regime factors (patience, status) are genuine stochastic regime processes. Bull markets must be able to arrive through at least four distinct doors: a patience regime shift, an appreciation regime shift, cohort replacement at the security level, and positioning mechanics in thin names. All four exist in the recommended architecture.

---

## 2. Recommended factor architecture

**Design rule (the identification discipline):** every macro factor must own a *signature event class* — a class of modeled or editorial events that moves this factor as primary and no other factor as primary. A factor without a signature class is a renaming and gets merged at quarterly review. A shock is routed to the macro layer only if it changes the world parameter for securities *not directly involved*; otherwise it is a security-level fundamental. (Postal slowdown hurts letters — that is a fundamental. Same-day logistics becoming the national default hurts everyone who lives on latency — that is Time Compression.)

The set: **seven structural pressures, two valuation regimes, one hybrid.**

---

### P1. Time Compression (TC)
- **Definition:** The supply-side removal of latency between desire, action, and outcome by infrastructure and defaults — how fast the world has become, not how fast people want it.
- **Causal mechanism:** Some practices are constituted by temporal space. Waiting for a reply does not get worse when latency falls; it becomes *impossible*. Adjacent practices lose their niche as reply-time norms inflate ("seen" as implicit rejection).
- **Behavior:** Secular, stepwise; can locally reverse (postal degradation).
- **Observable inputs:** OBSERVED: delivery latency distributions, on-demand service penetration. MODELED: reply-latency norms, default settings of communication tools. EDITORIAL: which latencies are now socially mandatory.
- **Correlations:** High with MPD and AC historically; identified by signature events (a new instant-delivery category launches) that move neither.
- **Why separate:** This is the frontier-of-speed factor. Its signature events — infrastructure and default changes — are distinct from preference changes (P9) and from attention changes (P2). A world can get faster with attention untouched.

### P2. Attention Capture (AC)
- **Definition:** The share of waking human attention that is claimed by engineered engagement streams; the scarcity of *unallocated* mind.
- **Causal mechanism:** Practices die not only when time is scarce but when mind is. Co-presence, waiting, wandering, and solitude require cognitively unclaimed time. A free hour spent inside a feed is unavailable to them even with no change in technology of the practice itself.
- **Behavior:** Secular with saturation dynamics; policy-sensitive.
- **Inputs:** OBSERVED: screen hours, notification counts. MODELED: phone-presence norms in shared space. EDITORIAL: the social permission to be unreachable.
- **Correlations:** Moderate with TC; signature events (engagement-design changes, phone policies) are distinct.
- **Why separate:** Because it is the *primary* enemy of Solitude, Waiting, and co-present practices — securities that TC barely touches. Without AC, the model cannot explain why solitude collapses in leisure-rich societies.

### P3. Discretionary Time Poverty (DTP) — *the hybrid*
- **Definition:** The economic and calendar scarcity of unhurried, uncommitted hours: work intensity, commuting, care burden, precarity.
- **Causal mechanism:** Slow practices are time-intensive *in hours*, not merely in patience. Their habitat is slack. This is an economic condition with technological causes but independent dynamics.
- **Behavior:** Mixed — cyclical (labor market, recessions slow life) over a secular component.
- **Inputs:** OBSERVED: hours worked, commute times, care burdens. MODELED: calendar density. EDITORIAL: the cultural valuation of busyness.
- **Correlations:** Moderate with TC (technology causes both), but divergent scenarios abound: a four-day-week economy, or a post-crash slowdown, enriches time with zero technological change.
- **Why separate:** It is the factor that lets the modeled world *get slower* without any technology retreating — the most plausible engine for a decade-long index rally. Collapsing it into TC would delete that behavior from the model's reachable state space.

### P4. Human Substitution (HS)
- **Definition:** The capability and economic incentive to produce a practice's functional *output* without the human performer.
- **Causal mechanism:** A labor-market mechanism, exactly like automation of skills: where output is fungible and the audience cannot or does not care who performed it, the human performance loses its market. Where the act is the output (presence, liveness), exposure is low or zero.
- **Behavior:** Secular, arriving in capability jumps.
- **Inputs:** OBSERVED: price of synthetic vs. human output. MODELED: output-class substitution capability. EDITORIAL: audience discernment (can recipients tell? do they care?).
- **Correlations:** Moderate with ME and MPD; signature events are AI capability releases, distinct from platform-policy or format events.
- **Why separate:** It is the only factor whose primary target is *who performs the act* — and its exposure profile is sharply non-uniform (devastating for letters, near-zero for visits and walking), which gives the cross-section its texture.

### P5. Mediation & Extraction (ME)
- **Definition:** The presence and intensity of commercial intermediary layers within a practice — ranking, tracking, surveillance, data extraction, asymmetry of information between parties.
- **Causal mechanism:** An intermediary changes the act's texture even when the act survives: the call transcribed and scored is a different practice; the walk quantified and ranked is a different walk; discovery pre-ranked is not discovery. The channel is the *terms of the encounter*, not its speed or substrate.
- **Behavior:** Secular; **non-monotonic** — end-to-end encryption and privacy law can push it down.
- **Inputs:** OBSERVED: platform penetration in a practice's workflow, tracking defaults. MODELED: extraction intensity. EDITORIAL: perceived observation.
- **Correlations:** Moderate with UC and HS; signature events are platform-policy and privacy-regulation changes.
- **Why separate:** Presence-substitution lives in MPD/HS; capability lives in HS; *who stands between and what they take* lives here, and only here.

### P6. Uncertainty Compression (UC)
- **Definition:** The systematic removal of chance, ambiguity, and unsolved search from daily life: prediction, recommendation, reservation, pre-selection — and the saturation of choice spaces that makes unaided discovery impractical even without good prediction.
- **Causal mechanism:** For securities whose value is *constituted* by chance — serendipity, aimlessness, the unplanned — the elimination of randomness is habitat destruction, not convenience.
- **Behavior:** Secular; can locally reverse (prediction scandals, wander-mode features).
- **Inputs:** OBSERVED: recommendation penetration, ETA accuracy, reservation rates, catalog sizes. MODELED: share of outcomes pre-solved. EDITORIAL: ambient expectation of a "right answer."
- **Correlations:** Moderate with ME; signature events are prediction/search-infrastructure changes that occur without commercial extraction changes (e.g., public infrastructure).
- **Why separate:** Its incidence is highly concentrated (SD, AW, UV) while ME's is diffuse — the cross-sectional fingerprints differ, which is exactly what a factor is for.

### P7. Encounter Erosion (EE)
- **Definition:** The rising cost of unscheduled human and worldly contact: distance between lives, decline of third places and walkable space, rent pressure on encounter habitats, scheduling norms displacing spontaneity, thinning of relational density and trust. *Absorbs candidate F (Coordination Compression) as its scheduling-norm indicator cluster, and absorbs urbanization, trust, and loneliness questions as indicator clusters.*
- **Causal mechanism:** Unplanned visits, spontaneous calls, aimless wandering through social space, and shelf-browsing discovery all require that unscripted contact be *cheap*. When proximity, venues, availability norms, and trust erode, spontaneity becomes an luxury act — first unusual, then transgressive, then performative.
- **Behavior:** Slow-moving, largely secular; **reversible** (zoning reform, urbanist movements, remote-work migration).
- **Inputs:** OBSERVED: rents, third-place closure rates, walkability indices. MODELED: distance-to-closest-friend, scheduling density (absorbed F), relational contact frequency. EDITORIAL: neighborhood trust, drop-in acceptability norms.
- **Correlations:** Weak-to-moderate with everything; signature events are spatial and normative (zoning, migration, etiquette shifts).
- **Why separate:** No other candidate captures the *spatial-relational substrate*. Without EE, unplanned visits have no factor that prices them, and the model silently implies that suburbs and rents are irrelevant to human contact — false, and artistically impoverished.

### P8. Materiality & Permanence Displacement (MPD)
- **Definition:** The replacement of physical carriers and irreversible artifacts by dematerialized, editable equivalents — including the erosion of the *manufacturing base* for analog inputs.
- **Causal mechanism:** Two channels: (a) the physical substrate is the practice's body — no film, no film photography, regardless of demand; (b) irreversibility is a property of matter — the undeletable photograph, the sent letter, carries commitment weight that the editable file does not. Absorbs the reversibility question as a secondary cluster.
- **Behavior:** Secular with saturation; locally reversible (pressing-plant construction is real).
- **Inputs:** OBSERVED: format shares, analog manufacturing capacity. MODELED: permanence norms. EDITORIAL: the social meaning of the delete key.
- **Correlations:** Moderate with TC; signature events are format shifts and industrial-capacity events.
- **Why separate:** Human Substitution and MPD cross in a 2×2: a voice memo is human-performed but dematerialized; a printed form letter is material but substituted. Neither factor can stand in for the other.

### P9. Patience Regime (PR) — *the LONGING discount rate*
- **Definition:** The demand-side discount rate on slow, delayed, effortful rewards — how much the culture impairs the present value of payoffs that arrive late and ambiguously. Rising PR = impatience.
- **Causal mechanism:** Every LONGING security is a long-duration, low-current-yield asset; most of its value sits in a cultural tail. A rise in societal impatience marks all of them down exactly as rising rates mark down bonds; a fall re-rates all of them up. This is duration, and LONGING is a duration trade.
- **Behavior:** Regime-dependent, long waves, mean-reverting around a slow drift. This is a *valuation regime*, not a world pressure: the frontier (TC) and the preference (PR) are identified separately — TC from infrastructure observables, PR from **revealed choice among coexisting fast and slow options** (the frontier cannot explain people abandoning existing fast options; only preference can).
- **Inputs:** MODELED/EDITORIAL almost entirely: choice shares of slow options conditional on fast availability; savings/patience proxies. This factor will remain mostly editorial, and should say so.
- **Correlations:** Mildly correlated with ASC; signature divergence below (§6).
- **Why separate:** It is the only mechanism that can re-rate the *entire index* upward through demand alone, with zero change in the world's technology. Deleting it hard-codes the secular bear into the model. It must exist, and it must be stochastic.

### P10. Authenticity & Status Cycle (ASC)
- **Definition:** The social-meaning regime: whether effort, rarity, analog-ness, and intimacy currently read as authentic and high-status versus obsolete and affected. Contains the **Effort Premium** sub-index (absorbing candidate G) and a documented **nostalgia-phase** mechanism: each security's ASC beta activates on its own cultural-memory clock (revivals arrive roughly when a form is far enough away to be safe and romantic — a slow, security-specific oscillator *inside* this factor, not a separate factor).
- **Causal mechanism:** Pure demand: practices are re-priced as their social sign flips. The friction premium and the status premium are distinct psychological channels (effort-justification vs. signaling) that can diverge — paying a premium for one-hour film developing is status without patience — so both are kept as observable sub-indices of one latent regime.
- **Behavior:** Cyclical, mean-reverting, long waves; regime-switching (appreciation / neutral / backlash).
- **Inputs:** EDITORIAL: cultural reference tone (an NLP panel over press is legitimate if documented). OBSERVED: premium pricing of analog formats, revival-cohort adoption. MODELED: signaled-identity prevalence.
- **Correlations:** Mildly correlated with PR; identified by the status-without-patience signature.
- **Why separate:** It is the bull engine for individual securities, the carrier of the artwork's quiet bias, and — crucially — a factor the model is allowed to *disagree* with the artist about.

---

## 3. Factors to merge, demote, or delete

| Candidate | Disposition | Destination | Reason |
|---|---|---|---|
| A. Time Compression | **Kept** | Macro P1 | Distinct frontier-of-speed mechanism; supplies latency-habitat destruction. |
| B. Human Substitution | **Kept** | Macro P4 | Only factor targeting *who performs the act*. |
| C. Mediation | **Kept, narrowed** | Macro P5 | Presence-substitution aspects reassigned to MPD/HS; core narrowed to intermediary extraction and surveillance. |
| D. Uncertainty Compression | **Kept, widened** | Macro P6 | Absorbs choice-abundance as an indicator cluster (same causal outcome: unaided discovery becomes impractical; divergence scenarios were too thin to justify separation). |
| E. Physicality Displacement | **Kept, widened** | Macro P8 | Absorbs reversibility/permanence as secondary cluster; irreversibility is materially grounded. |
| F. Coordination Compression | **Demoted** | Indicator cluster inside EE (P7) | Its mechanism — planning displacing spontaneity — operates through exactly the channel EE prices: the cost of unscheduled contact. Scheduling density is EE's core relational indicator. Divergent-from-TC scenarios exist, but not divergent-from-EE ones. |
| G. Friction/Inconvenience Premium | **Merged** | Sub-index of ASC (P10), with its delay-tolerance component reassigned to PR (P9) | Effort-valuation is a taste regime; delay-tolerance is a discount rate. Split along that seam and both become measurable. |
| H. Scarcity Revaluation | **Demoted** | Security-level valuation fundamental: **Rarity Elasticity of Value**, activating an endogenous Scarcity Premium in the valuation layer when prevalence falls far enough *and* the ASC regime is appreciative | As a macro factor it double counts by construction: it is a *response* to factor-driven prevalence decline. In the valuation layer it is honest: decline (factors) and per-instance rarity premium (valuation) are separately attributable. |
| I. Social Legibility/Status | **Promoted** | Macro regime P10 | Legitimate, necessary; nostalgia handled as a documented phase mechanism inside it, not as its own factor. |

**Also demoted (missing-dimension candidates rejected as macro factors):** bodily effort → security fundamental **Embodied Skill Intensity** (drives loadings on HS and ASC rather than moving itself); commodification → security fundamental **Marketization Degree** with a documented slow feedback into ASC (a practice bought as status slowly loses the authenticity the status was paying for — a built-in mean-reversion the analysts can watch); institutional/regulatory forces → Event Desk inputs, promoted to macro only via the boundary rule in §2; synchronization/asynchrony → covered jointly by TC and EE scheduling norms, no independent behavior purchased.

---

## 4. Missing factors

Four causal dimensions absent from the candidate set are promoted to the architecture (P2, P3, P7, P9 above). In summary, with the questions of §7 answered:

1. **Attention Capture (P2).** The most important omission. The candidate set prices the destruction of practices by machines; it does not price their destruction by *captured minds*. Solitude's primary enemy is not "togetherness technology" — it is the feed in the room.
2. **Discretionary Time Poverty (P3).** Economic time scarcity is separated from technological time compression. They are correlated through productivity, but they answer different questions: TC asks *how fast can the world move*; DTP asks *does anyone have a free afternoon*. A four-day-week economy revives slow practices with no technological change at all — this behavior must be reachable.
3. **Encounter Erosion (P7).** Urbanization, geographic distance, trust, loneliness, and scheduling density are real, distinct causal channels, and they are *non-technological* — the model currently has no factor that a zoning reform or a rent crisis can move. Loneliness as such is not a factor; it is an indicator cluster (relational density, trust) inside P7, plus an ASC narrative driver. This placement answers the "too close to fundamentals?" concern: the *macro* variable is the cost of contact; the loneliness of a specific practice's community is a fundamental.
4. **Patience Regime (P9).** A discount rate on slow rewards. Financially standard (duration), behaviorally documented (time preference), and artistically essential: it is the index-level bull mechanism that keeps the secular bear from being hard-coded.

**Considered and rejected as factors** (with destinations): trust norms → EE indicator; reversibility → MPD cluster + per-security fundamental; asynchrony → TC + EE; choice abundance → UC cluster; regulation → event layer with boundary rule; commodification → security fundamental + ASC feedback; bodily effort → security fundamental (Embodied Skill Intensity, driving cross-loadings); nostalgia → ASC phase parameter; demographic turnover → security fundamental (**Cohort Transmission**: per-practice cohort adoption, updated monthly, editorially estimated — this is the real-world engine of the film revival and must live at the security level because transmission failures do not co-move across practices).

---

## 5. Exposure matrix

Convention: sign = effect on the security's habitat/value of a **rise** in the factor. `-- `strongly negative, `-` negative, `0` near zero, `+` positive, `++` strongly positive.

| Factor | HL | WR | UPC | UV | AW | FP | PM | SD | HO | LP | SO |
|---|---|---|---|---|---|---|---|---|---|---|---|
| TC — Time Compression | − | −− | − | 0 | 0 | 0 | 0 | − | 0 | 0 | 0 |
| AC — Attention Capture | − | −− | − | − | − | 0 | − | − | 0 | − | −− |
| DTP — Time Poverty | − | − | 0 | − | − | 0 | − | − | − | − | − |
| HS — Human Substitution | −− | − | − | 0 | 0 | −* | 0 | − | − | 0 | 0 |
| ME — Mediation/Extraction | − | − | − | 0 | − | 0 | 0 | −− | 0 | − | − |
| UC — Uncertainty Compression | 0 | 0 | 0 | − | − | 0 | 0 | −− | 0 | 0 | 0 |
| EE — Encounter Erosion | 0 | 0 | − | −− | − | 0 | 0 | −− | − | − | 0** |
| MPD — Materiality Displacement | −− | − | 0 | 0 | 0 | −− | −− | − | − | 0 | 0 |
| PR — Impatience | − | −− | 0 | − | − | − | − | − | − | 0 | − |
| ASC — Authenticity/Status | ++ | + | + | + | + | ++ | ++ | + | ++ | ++ | +*** |

**Surprising exposures, briefly:**

- **Solitude's worst enemy is AC, not any togetherness force.** Its factor profile is nearly empty of technology-pressures and dominated by attention and time — solitude dies of the feed and the full calendar, not of the smartphone per se. This is the kind of finding the terminal should be built to reveal.
- **Unplanned Visit is the model's proof-of-human refuge:** 0 on HS — physical presence cannot be AI-substituted. Its destruction is almost entirely EE.
- **Waiting for a Reply is the highest-duration asset in the model:** −− on both TC and PR. It is the purest bond in LONGING, and the most rate-sensitive.
- **Aimless Walking is hurt more by ME than by TC:** the Strava-ification of the walk changes the practice more than speed does. Quantified walking is a different practice.
- **Film Photography on HS is contested (−\*):** direct output substitution (AI images) is negative, but a proof-of-human channel routes positively through ASC. Analysts must be allowed to split on this sign — it is a designed disagreement point.
- **Live Performance is 0 on HS with a contested positive channel:** synthetic abundance makes liveness scarcer and more precious; the direct substitution exposure is zero.
- **EE on Solitude (0\*\*) is deliberately contested:** forced isolation is not chosen solitude, but scarcity of *true* solitude could raise its rarity value. The analyst panel should carry standing disagreement here; the artwork should not resolve it.

No factor assigns near-uniform signs. TC, UC, and MPD are appropriately selective; DTP and PR are appropriately broad (a bond-like factor and a hours-based factor *should* be broad); ASC is the broad bull factor with differentiated betas.

---

## 6. Independence tests

Mandatory scenarios; each factor moving hard while its nearest neighbor stays still:

1. **TC moves, AC stable:** a national same-day logistics network reaches 80% coverage; screen time and notification load unchanged. (TC ↑, AC flat.)
2. **AC moves, TC stable:** a new short-video format saturates leisure hours; no change in delivery latency, communication speed, or any speed frontier. (AC ↑, TC flat.)
3. **DTP moves, TC stable:** a recession plus four-day-week adoption shortens commutes and thins calendars; every technology unchanged. (DTP ↓ — time enriches — TC flat.)
4. **HS moves, ME stable:** an AI model reaches human-passable personal letters; platforms, tracking, and intermediaries unchanged. (HS ↑, ME flat.)
5. **ME moves, HS stable:** privacy regulation forces tracking off by default; no capability change. (ME ↓, HS flat.)
6. **UC moves, ME stable:** a public, non-commercial planning infrastructure (universal ETAs, reservations, public recommendation) reaches saturation in a low-extraction economy. (UC ↑, ME flat.) Reverse test: a chronological, unranked feed era — ME ↓, UC flat.
7. **EE moves, UC stable:** zoning reform legalizes mixed-use streets and third places multiply; algorithms untouched. (EE ↓ — encounter cheapens — UC flat.)
8. **MPD moves, HS stable:** a format shift completes (streaming displaces the last physical carriers); no AI capability change. (MPD ↑, HS flat.)
9. **PR moves, ASC stable:** a macro scare produces broad savings and delayed gratification — patience rises — while the status of analog formats is unchanged. (PR ↓, ASC flat.)
10. **ASC moves, PR stable:** a celebrity aesthetic moment makes film cameras high-status overnight; premium prices are paid for *one-hour* developing — status rises while revealed willingness to wait does not. (ASC ↑, PR flat. This is the identification signature between the two regime factors.)

---

## 7. Event classification examples

| # | Event | Primary | Secondary | Notes / double-count flags |
|---|---|---|---|---|
| 1 | AI service writes convincing handwritten-style letters | HS | TC (speed of correspondence) | Contested direction (§2.4): one analyst reads substitution, another reads demand evidence for the form. Contested events move factor *variance*, not forced mean. |
| 2 | End-to-end encryption becomes messenger default | ME ↓ | — | Clean; do **not** also move UC. |
| 3 | Four-day week reaches 20% of employers | DTP ↓ | PR (mild) | Cap secondary at 30% of event magnitude. |
| 4 | Film chemistry plant closes; film prices double | FP fundamental (cost/supply) + Scarcity Premium trigger | MPD only if it signals broader displacement | **Flagged:** classic double-count trap — cost shock must hit fundamentals, not the MPD factor, absent sector-wide evidence. |
| 5 | City converts parking to plazas; center-city rents fall | EE ↓ | — | Clean. |
| 6 | Viral "call your family" moment; major essay on voice intimacy | ASC ↑ (UPC loading) | — | ASC moves only if the market updates its belief about the *regime*, not merely because one security's narrative moved — regime-belief vs. regime-state distinction is mandatory here. |
| 7 | Navigation app adds a randomness "wander mode" | UC (small ↓) | ME (mild ↑: it is mediated chance) | Deliberately ambiguous; analyst split expected and desirable. |
| 8 | Gen Z film-camera sales +40% YoY | FP Cohort Transmission fundamental ↑ | ASC only as *evidence* for regime belief | Flagged: the strongest real-world revival input; must not simultaneously move the ASC factor and FP's fundamentals. |
| 9 | Streaming fragmentation + price rises push users back to discs | PM fundamental (relative price) | MPD (mild local reversal) | Flagged for mild double count; cap secondary. |
| 10 | Workplace AI scheduling assistants become ubiquitous | EE ↑ (scheduling-density cluster) | TC | Former candidate F's home cluster. |
| 11 | Nationwide school phone bans | AC ↓ (long horizon) | ASC (eventually) | Primary AC; recognition lag applies. |
| 12 | Government creates a Ministry of Loneliness Policy | ASC (SO narrative) | EE indicator update | Do not move EE factor unless contact-cost data change. |
| 13 | Postal service cuts to three-day delivery | **HL/WR fundamental**, not TC | — | Boundary-rule demonstration: macro only if securities *not directly involved* are affected. |
| 14 | Generated ambient music floods platforms | HS ↑ | — | Shows factor *non*-incidence: LP ≈ 0, PM ≈ 0. Not everything moves. |

---

## 8. Attribution design

**Requirement:** the weekly ledger sums exactly, always, including interactions — to machine precision, every week, provably.

**Method.** Price change is generated by an additive state-space process, so the ledger is an *identity*, not an estimation:

```text
r_i,w  =  Σ_k β_ik · ΔF_k,w          (factor core, linear)
        + interaction_w,i            (exact cross-term of the Taylor expansion)
        + belief & surprise_i,w      (analyst re-ratings, event surprises)
        + positioning flow_i,w       (flows × impact; short covering lives here)
        + liquidity/noise_i,w
        + residual_i,w               (≈ 0 by construction; publishes actual)
```

- **Interactions:** the linear expansion's exact cross term is published as one `Interaction` line. Factor co-moves are *disciplined at the source* by the event-signature rule (one primary factor per event), so interactions stay small; if the interaction line exceeds ±2% in any week, an automatic collinearity flag opens a review. (Shapley allocation across factor pairs is available as an optional drill-down, never as the headline.)
- **Correlated factor moves:** accepted, not laundered. Correlation is handled by the signature-event identification discipline, not by orthogonalization that would produce uninterpretable rotated factors.
- **Delayed pricing:** shocks enter a per-security *recognition queue* and are released with an exponentially decaying schedule (recognition half-life, typically 2–8 weeks). The ledger shows a `Recognition of prior shock` line; attribution is dated when priced, with the origin event referenced by ID.
- **Confidence:** every line carries the provenance chain of its inputs (OBS/MODELED/EDIT) and a width derived from factor uncertainty and analyst dispersion. The terminal may print point estimates — that is the institution's aesthetic — but the documentation layer carries intervals. The honesty is part of the artwork.

The v1 example, in v2 form:

```text
LTR — WEEKLY RETURN                                  +13.84%

FACTOR CORE (linear)
  Human Substitution                       −1.44%
  Attention Capture                        −1.10%
  Time Compression                         −0.61%
  Patience Regime (impatience)             −0.57%
  Discretionary Time Poverty               −0.31%
  Mediation & Extraction                   −0.22%
  Uncertainty Compression                  −0.09%
  Authenticity & Status Cycle              +2.86%
  Others                                   0.00%
  Factor core subtotal                     −1.48%
Cross-factor interaction                   +0.42%
Belief revision & surprise                 +4.55%
Positioning flows (short covering)         +9.72%
Liquidity / impact residual                +0.63%
                                          --------
TOTAL                                      +13.84%   (exact)
```

Note the v1 draft's `Human Substitution −3.11%` alongside `Time Compression −1.82%` and a huge narrative block is exactly the double-counting shape the reviewers feared; under the signature-event discipline, the event's magnitude is assigned once, at its primary, and the remaining move is honestly labeled as belief and flow.

---

## 9. Complexity risks — where earned complexity becomes theater

**Warning signs (any one triggers review):**

1. **Precision beyond inputs.** Printing two decimals of a factor whose inputs are 60% EDITORIAL, without intervals. Internal representations must be distributions; the point estimate is a display convention, and the docs must say so.
2. **Dead factors.** A factor that was primary in fewer than ~5% of weeks over a 20-year simulated history, or whose signature-event purity test (§10) fails 70%. It is decoration and gets merged or demoted at the quarterly review — the factor set subjects itself to the same §2.3 committee that reviews constituents.
3. **Attribution dust.** Ledger lines smaller than their confidence widths. If `Uncertainty Compression −0.09%` carries ±0.4%, the line is noise dressed as knowledge; aggregate it into a band.
4. **Universal loading.** Every event mapping to 4+ factors means the taxonomy has failed and the event-signature rule has decayed. Attribution becomes noise with excellent formatting.
5. **Renamed duplicates.** Two factors whose indicator sets correlate above ~0.9 *in simulated history* *and* which lack divergent scenarios. Correlation alone does not merge factors; correlation plus no divergence mechanism does.
6. **False objectification.** Converting inherently judgmental quantities into "measurements" with no provenance. `Cultural Attachment = 76.4` is legitimate *only* with a visible derivation trail. Some things must remain editorially declared — PR is the clearest case — and declaring them is a strength, not a confession.
7. **Narrative-fitting.** Any parameter tuned to make the index decline. The secular bear must be a *prior*, contested in the documentation, revisable at annual review, and capable of being wrong inside the model.

---

## 10. Falsification tests

1. **Film-revival transplant test.** Feed the model's input history a synthetic analogue of the real 2010s film revival (cohort adoption, ASC indicators, lab closures, premium pricing). **Pass:** FP makes new multi-year price highs with zero parameter changes and no special-case rules. **Fail = the model is rigged.**
2. **Structural-winner Monte Carlo.** Run 1,000 thirty-year world paths with the drift priors set *bearish*. **Pass:** in a meaningful fraction of paths (target ≥15%), at least one security shows a positive total return while the index is negative, via any of the four bull doors (patience regime, appreciation regime, cohort transmission, positioning squeeze). **Fail if all securities decline in all paths — decline is hard-coded.**
3. **Collinearity / purity test.** Inject each factor's signature event in isolation (50 draws each). **Pass:** ≥70% of the attributed move lands on the intended factor; rolling-window betas do not flip sign from co-movement alone. Also replay v1's seven-factor set on the same events as a control — it should fail this test, demonstrating the fix.
4. **Attribution integrity test.** Across 10,000 simulated weeks, ledger sums to returns within 1e−10 relative error, including interaction and residual lines. Differential check: perturb one factor shock, verify the ledger's delta matches the sensitivity matrix. **Fail = the ledger is narrative, not accounting.**
5. **Model-versus-artist disagreement test.** Construct 20 adversarial events with a clear artist prior (e.g., a genuinely beautiful AI letter service — the artist wants it to be bearish for HL). **Pass:** the model's market reaction diverges from the artist's prior in ≥20% of cases, and the analyst panel shows internal disagreement in ≥30%. **Fail if the model poetically confirms the artist every time.**
6. **Counter-secular decade test** (bonus). Synthesize a decade of reversed pressures (DTP enriching, PR patient, ASC appreciative, EE improving) with no technology retreat. **Pass:** the index is capable of a positive decade. This is the no-hard-coded-decline requirement, tested directly.
7. **Squeeze realism test** (bonus). With short interest >80% of modeled float and a modest positive surprise, the weekly return distribution must exhibit fat right tails. Thin names must be capable of violence; a dampened response means the microstructure layer is decorative.

---

## 11. Proposed v2 specification — LMC-2 ("LONGING Macro Complex, v2")

```text
┌──────────────────────────────────────────────────────────────────┐
│ OBSERVABLE INDICATORS (~24 series, each tagged OBS/MODELED/EDIT) │
│  delivery latency · reply-latency norms · on-demand penetration  │
│  screen hours · notification load · presence norms               │
│  hours worked · commute · calendar density                       │
│  synthetic-output prices · substitution capability indices       │
│  platform penetration · tracking defaults · extraction intensity │
│  recsys penetration · ETA accuracy · reservation rate · catalogs │
│  rents · third-place count · walkability · scheduling density    │
│  relational contact frequency · trust readings                   │
│  format shares · analog manufacturing capacity · permanence norm │
│  slow-option choice shares (conditional on fast availability)    │
│  analog premia · revival-cohort adoption · cultural tone (NLP)   │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│ LATENT FACTORS (10) — weekly update as distributions             │
│  P1 TC   P2 AC   P3 DTP   P4 HS   P5 ME   P6 UC   P7 EE   P8 MPD │
│  Regimes:      P9 PR (patience/impatience)                       │
│                P10 ASC (appreciation/neutral/backlash)           │
│  Pressures: Σ(signature events) + EW indicator drift             │
│  Regimes: 3-state Markov + editorial priors + nostalgia phases   │
│  Contested events → variance ↑, mean contested by analyst panel  │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│ SECURITY LAYER (per security, quarterly review)                  │
│  Exposures β (11×10, editorial, documented, ±1-band uncertainty) │
│  Fundamentals: prevalence · cohort transmission · habitat assets │
│   (labs/shops/venues) · embodied skill intensity · cost structure│
│   output substitutability · reversibility · marketization degree │
│   rarity elasticity of value (κ_i)                               │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│ VALUATION & BELIEF                                               │
│  Cultural cash flow C_i = prevalence_i × per-instance value_i    │
│  Discount: r = 4% + 3%·z(PR) + idio premium (fragility 0–6%)     │
│  Scarcity premium = κ_i · rarity shortfall · 1{ASC appreciative} │
│  → Research Fair Value_i (distribution)                          │
│  Analyst panel (5 schools: Substitutionist · Materialist ·       │
│   Formalist · Ecologist · Sentimentalist) contest directions;    │
│   consensus = weighted median; dispersion → uncertainty & vol    │
│  → Analyst Target Prices (12M, per analyst + consensus)          │
└──────────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────────┐
│ MARKET MICROSTRUCTURE                                            │
│  Float · short interest · depth (∝ float) · impact k/√depth      │
│  Weekly flows: belief updates + surprise + rebalancing           │
│  Squeeze channel: surprise⁺ × short interest × urgency           │
│  → WEEKLY PRICE   (with the §8 exact attribution ledger)         │
└──────────────────────────────────────────────────────────────────┘
```

**Initial parameters (starting points, all revisable):** EW drift weight α = 0.05/week on indicator z-scores; event magnitudes m ∈ [−3, +3] with confidence c ∈ [0,1], single primary assignment, secondaries capped at 30%; recognition half-lives 2–8 weeks by security liquidity; PR and ASC transition matrices at quarterly scale with editorial priors; exposure review annual; factor self-review quarterly (signature-purity and dead-factor tests); drift priors on pressures documented as *beliefs with uncertainty*, subject to annual State of LONGING review. Cadence unchanged from §2.2.

**Why this build satisfies §10 without hard-coding:** the seven pressures carry bearish *priors*, not bearish *laws*; PR and ASC are stochastic regimes capable of years-long appreciative phases; cohort transmission can flip any security's fundamentals; and the microstructure layer makes thin, heavily-shorted names violently responsive to good news. Concretely:

- **Film Photography** bulls through the real-world chain: cohort transmission ↑ (new practitioners) + ASC appreciation regime + lab closures triggering κ-scaled scarcity premia on remaining capacity — a multi-year bull inside a falling index, emergent, no exceptions scripted.
- **Live Performance** bulls through a different door entirely: HS floods the world with synthetic recorded output → the proof-of-human premium (ASC-liveness sub-channel) compounds with AC making shared embodied attention scarce. Liveness becomes the one thing that cannot be generated.
- **Unplanned Phone Call** is the episodic candidate: an E2E-encryption wave (ME ↓) plus a voice-intimacy status turn (ASC ↑) can produce a sharp re-rating — the model's version of a short squeeze on a practice everyone had already written off.

The architecture's promise to the artwork: an institution that computes with visible, documented, partly subjective conviction — rigorous enough to be trusted, honest enough to be watched disagreeing with the people who built it.