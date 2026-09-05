# LONGING — Pricing Model v2 Factor Architecture Review

## 1. Executive Verdict

The new principle—"Do not choose the number of factors in advance; keep as many factors as can explain genuinely different causal stories"—is fundamentally correct. The previous seven-factor set failed because it was essentially one modernization factor wearing seven different hats. The new candidate set of nine families is an improvement, but it still contains significant conceptual redundancy that must be resolved before implementation.

The deepest conceptual problem is not the number of factors but the absence of a clear taxonomy of what a "factor" is doing in this model. Some candidate factors describe *technological processes* (automation, digitization), others describe *human experience* (uncertainty, friction), and others describe *social interpretation* (legibility, status). These are not different magnitudes of the same thing; they are different ontological categories. The model needs factors that operate at different levels of causation: some as slow-moving structural forces, some as cyclical market sentiments, some as security-level fundamental drivers, and some as pure belief or narrative states that can decouple from fundamentals entirely.

The current nine candidates are simultaneously too many and too few. Too many because several are causally redundant given adequate specification: Coordination Compression is largely a subset of Time Compression plus Mediation; Physicality Displacement overlaps heavily with both Human Substitution and Mediation; Scarcity Revaluation is not a macro force but a security-level valuation response function. Too few because the set remains almost exclusively technology-centric, missing economic, demographic, and social-psychological dimensions that would move prices in genuinely different ways.

What is right: the hierarchy of observable indicators feeding latent factors is sound; the distinction between fundamental revision, narrative re-rating, and positioning effects is essential; the requirement that factors be independently movable is the correct test; the willingness to retain complexity when it buys distinct behavior is appropriate for this artistic-financial hybrid.

What remains wrong: the factors have not been asked to answer different *questions* about why a practice changes value. A good factor architecture should partition the space of causes: (1) Can the practice still be done? (2) Does anyone still want to do it? (3) What does it cost to do it? (4) What does society think of those who do it? (5) How do market participants feel about all of the above? The candidate set answers mostly question one, occasionally question four, and almost never questions two, three, and five as distinct forces.

I will recommend a final set of approximately eight latent factors, organized into three layers: structural (slow secular forces), experiential (medium-speed cultural-economic forces), and reflexive (market belief and positioning forces). This is not because eight is the right number, but because eight is the number of genuinely distinct causal stories that survive hostile review after merging redundancies and adding missing dimensions.

---

## 2. Recommended Factor Architecture

### Layer 1: Structural Factors (secular, slow-moving, long half-life)

---

**Factor S1: Time Compression**

**Definition:** The degree to which the latency between human intention and outcome is eliminated across the social environment, measured as the expected wait time for a representative set of human practices and transactions.

**Causal mechanism:** When waiting itself becomes culturally unfamiliar, practices that require or presuppose waiting lose their intelligibility and their practitioners lose the patience infrastructure that made the practice sustainable. This is distinct from mere impatience: it is the erosion of the *capacity to occupy waiting* as a meaningful state.

**Secular/cyclical/regime behavior:** Secular trending, with occasional plateau regimes during cultural backlash.

**Observable inputs:** OBSERVED: average message response latency, delivery time distributions, service wait times, attention interval measurements. MODELED: composite latency index across 20 practice domains. EDITORIAL: analyst assessment of whether latency reduction is accelerating or saturating.

**Likely correlations:** Correlated with Human Substitution (S2) and Mediation (S3) over long windows, but diverges during periods when automation reduces latency without replacing the human act (e.g., faster postal service helps handwritten letters) or when mediation adds friction (e.g., platform interfaces that slow down spontaneous contact).

**Why separate:** Time Compression attacks the *temporal texture* of practices. It can move independently of substitution because a practice can survive automation of its delivery (digital photo sharing does not replace film's aesthetic role even though it compresses time) while another practice can be destroyed by latency reduction without any substitution (unplanned visits become socially impossible when everyone expects real-time availability awareness).

---

**Factor S2: Human Substitution**

**Definition:** The degree to which the expressive or performative content of a human act can be reproduced by non-human means while preserving its functional output sufficiently to satisfy the recipient.

**Causal mechanism:** When the functional payoff of a practice is preserved but the human element is removed, the practice loses its *economic reason to exist* in its original form; simultaneously, the human element may acquire premium status as a luxury or authenticity signal, creating divergent valuation effects across different securities.

**Secular/cyclical/regime behavior:** Secular trending, with cyclical authenticity premiums emerging during periods of rapid substitution.

**Observable inputs:** OBSERVED: AI adoption rates in communication, automation penetration in relevant service domains, synthetic media quality benchmarks. MODELED: substitution feasibility scores per security domain. EDITORIAL: analyst judgment on whether substitution is perceived as adequate by recipients.

**Likely correlations:** Correlated with Time Compression and Mediation, but diverges when substitution occurs without latency reduction (e.g., a handwritten letter generated by AI and sent via slow postal mail) or when latency reduction occurs without substitution (e.g., faster delivery of physical handmade goods).

**Why separate:** Human Substitution attacks the *identity of the actor*. This is the factor that distinguishes "a human did this" from "this was produced." It can move sharply while Time Compression stays stable during, for example, a breakthrough in AI-generated personalized handwriting that does not change postal delivery speeds. This is the factor that makes Handmade Object and AI-Generated Handwritten Letter move in opposite directions even when both involve physical delivery.

---

**Factor S3: Mediation**

**Definition:** The degree to which human-to-human or human-to-world contact is intermediated by a third-party system that controls access, discovery, routing, or representation.

**Causal mechanism:** Mediation changes the *social architecture* of a practice. When contact is mediated, the spontaneous, reciprocal, and contextual dimensions of the practice are partially replaced by algorithmic logic, interface constraints, and platform incentives. This alters who practices, how they practice, and what the practice means.

**Secular/cyclical/regime behavior:** Secular trending, with cyclical platform disintermediation movements.

**Observable inputs:** OBSERVED: platform penetration rates for communication and discovery, percentage of social contact initiated through apps, discovery path analyses. MODELED: mediation index per practice domain. EDITORIAL: analyst assessment of whether platform incentives align with practice preservation.

**Likely correlations:** Correlated with Time Compression and Uncertainty Compression, but diverges when platforms add friction (e.g., dating apps that make spontaneous meetings harder while making planned meetings faster) or when uncertainty is compressed without mediation (e.g., personal navigation systems that optimize walking routes but do not mediate the walking itself).

**Why separate:** Mediation attacks the *relational structure* of practices. It can move independently when a new platform emerges that intermediates a previously direct practice without changing its speed or substituting its human content. Example: a social network for "spontaneous meeting" that actually makes meetings less spontaneous by creating an algorithmic marketplace for serendipity. Time Compression stays flat, Human Substitution stays flat, but Mediation rises and Serendipitous Discovery's fundamental value drops.

---

**Factor S4: Uncertainty Compression**

**Definition:** The degree to which outcomes, encounters, and discoveries are pre-determined, predicted, or optimized before the human act occurs, reducing the role of chance, failure, and surprise.

**Causal mechanism:** Practices whose value depends on the *possibility space remaining open*—serendipity, discovery, the unplanned, the unrepeatable—lose value when the possibility space is closed before the practice begins. This is not about time or substitution; it is about whether the practice can still produce the unexpected.

**Secular/cyclical/regime behavior:** Secular trending, with cyclical movements when recommendation systems become so complete that they trigger cultural backlash and deliberately random practices.

**Observable inputs:** OBSERVED: recommendation penetration rates, prediction accuracy benchmarks, route optimization adoption, reservation system coverage. MODELED: uncertainty elimination index per practice domain. EDITORIAL: analyst judgment on whether prediction is reducing the expected value of unplanned outcomes.

**Likely correlations:** Correlated with Mediation (platforms often predict and optimize), but diverges when prediction occurs without mediation (personal AI assistants that optimize your walking route without routing your social contact through a platform) or when mediation increases uncertainty (platform marketplaces that create unpredictable peer-to-peer encounters).

**Why separate:** Uncertainty Compression attacks the *possibility structure* of practices. This is the factor that explains why Aimless Walking and Serendipitous Discovery can decline even when no one is replacing humans, no time is being saved, and no platform is mediating the act. A city government that installs "optimal walking route" signage everywhere compresses uncertainty without any of the other three structural factors moving.

---

### Layer 2: Experiential Factors (medium-speed, cultural-economic)

---

**Factor E1: Friction Premium**

**Definition:** The market's current willingness to reward or penalize practices that require effort, skill, patience, inconvenience, or commitment, measured as the valuation spread between high-friction and low-friction equivalents.

**Causal mechanism:** Friction is not inherently good or bad; its valuation is cyclical. In periods of cultural reaction against convenience, friction becomes a *signal of investment and authenticity*: the fact that a practice is difficult becomes evidence that the practitioner cares. In periods of convenience dominance, friction is penalized as inefficiency. This is a market sentiment factor that moves independently of the actual level of friction in the environment.

**Secular/cyclical/regime behavior:** Strongly cyclical, with regime lengths of 3-7 years.

**Observable inputs:** OBSERVED: price spreads between analog and digital equivalents, sales data for high-effort goods, cultural media sentiment. MODELED: friction preference index from market behavior. EDITORIAL: analyst assessment of current cultural mood regarding effort and convenience.

**Likely correlations:** Low correlation with structural factors over short windows. Can move sharply while all four structural factors trend in the same direction.

**Why separate:** This factor explains why film photography, vinyl, and handmade objects can enter multi-year bull markets even while digitization, automation, and optimization continue to advance. It is the market's changing *interpretation* of friction, not the changing level of friction itself. Without this factor, the model cannot produce analog revivals without inventing contrived technology reversals.

---

**Factor E2: Physicality Premium**

**Definition:** The market's current valuation of embodied, material, and physically present experience relative to dematerialized or remote equivalents, independent of any functional differences.

**Causal mechanism:** Physical presence carries costs (travel, material, space) and benefits (tactile richness, co-presence, irreversibility) that cannot be fully replicated remotely. The market's relative valuation of these costs and benefits shifts cyclically as cultural norms, health events, and urban conditions change. This is distinct from friction premium because physicality can be low-friction (a cheap print) or high-friction (a live performance); the relevant dimension is embodiment, not effort.

**Secular/cyclical/regime behavior:** Cyclical, with long secular decline in physical share of total experience but cyclical revaluation of physical premium.

**Observable inputs:** OBSERVED: price premiums for physical media over digital, attendance at live events, physical goods sales trends, spatial presence data. MODELED: physicality premium index. EDITORIAL: analyst assessment of whether physical presence is becoming more or less valued per unit of experience.

**Likely correlations:** Correlated with Friction Premium (many physical practices are also high-friction), but diverges when physical practices become convenient (instant photo printing) or digital practices become high-friction (long-form digital detox).

**Why separate:** Physicality Premium explains why Live Performance can rally while Handmade Object stays flat: both are high-friction, but only one is embodied presence. It also explains why Physical Media can rally while Film Photography declines: both are physical, but one is a carrier of content and the other is a production process. The physical carrier question is distinct from the effort question.

---

**Factor E3: Social Legibility**

**Definition:** The degree to which a practice confers positive or negative social interpretation—status, authenticity, taste, virtue, or belonging—on its practitioner, relative to the social interpretation of not practicing.

**Causal mechanism:** Humans practice things partly because of what the practice signals to others. When a practice becomes legible as "authentic," "elite," "romantic," or "nostalgic," demand rises independently of functional utility. When it becomes legible as "outdated," "inefficient," or "pretentious," demand falls. This factor captures the social-semiotic dimension of practice valuation.

**Secular/cyclical/regime behavior:** Cyclical and regime-dependent; can shift rapidly with cultural moments (a film, a celebrity adoption, a backlash).

**Observable inputs:** OBSERVED: social media sentiment, media coverage tone, cultural criticism, adoption patterns among status groups. MODELED: legibility index per practice. EDITORIAL: analyst assessment of how the practice is currently read socially.

**Likely correlations:** Correlated with Friction Premium (friction often signals authenticity), but diverges when high-friction practices become socially legible as pretentious (e.g., vinyl collecting during a period of mockery) or when low-friction practices become status symbols (e.g., minimalist digital living).

**Why separate:** Social Legibility can move sharply and independently of all structural and other experiential factors. A single influential cultural artifact (a film, a novel, a celebrity endorsement) can change how millions of people interpret a practice without changing the technology, the time, the substitution risk, or the uncertainty environment. This is the factor that makes the model cultural rather than merely technological.

---

### Layer 3: Reflexive Factor (market-internal force)

---

**Factor R1: Positioning / Crowding**

**Definition:** The degree to which market participants are already positioned for a particular outcome in a practice's valuation, creating potential for violent reversals when outcomes differ from expectations.

**Causal mechanism:** When the market is unanimously bearish on a practice, bearishness becomes the crowded trade. Any positive surprise—a cultural moment, a technological reversal, a demographic shift—forces short covering, which amplifies the positive move far beyond what the fundamental change would justify. Conversely, when the market is unanimously bullish, disappointment is amplified. This is a pure market-structure factor that operates independently of all fundamental and experiential factors.

**Secular/cyclical/regime behavior:** Mean-reverting with short half-life (weeks to months), but can create multi-quarter momentum when combined with a genuine fundamental shift.

**Observable inputs:** OBSERVED: market positioning data (long/short ratios, consensus ratings, flow data), volatility of positioning changes. MODELED: crowding index per security. EDITORIAL: analyst assessment of whether the market is too one-sided.

**Likely correlations:** Uncorrelated with structural factors. Negatively correlated with future returns when crowding is extreme.

**Why separate:** This is the factor that makes the market capable of violent, audit-attributable rallies in a secular bear market. Without it, the model cannot generate the "short covering" attribution line that was identified as essential in the original brief. It is not a fundamental factor at all; it is a market-internal force, and conflating it with fundamentals would make the attribution ledger meaningless.

---

## 3. Factors to Merge, Demote, or Delete

### Delete: Coordination Compression (Candidate F)

**Action:** Demote to observable indicator within Time Compression and Mediation.

**Reason:** Coordination Compression is causally reducible. The claim that "spontaneous contact is replaced by scheduling" is composed of: (1) time latency reduction (you know when someone is free without asking), which is Time Compression; and (2) intermediation of contact through scheduling platforms or norms, which is Mediation. There is no scenario where Coordination Compression moves while both Time Compression and Mediation stay flat: if scheduling becomes more prevalent, either the time cost of coordinating drops (Time Compression) or the coordination is intermediated by a system (Mediation), usually both. It does not buy a distinct causal story.

**Fate:** Keep "scheduling density" and "reservation penetration" as observable indicators that load on both Time Compression and Mediation. This preserves the observability without the false factor distinction.

---

### Delete: Scarcity Revaluation (Candidate H)

**Action:** Move to security-level fundamental variable, not a macro factor.

**Reason:** Scarcity Revaluation is a *response function* of individual securities to their own prevalence declines, not a macro force that moves all securities. The fact that "as a practice becomes rarer, each remaining instance is valued more" is a property of the security (and its collector market, its cultural position, its irreplaceability), not a property of the macro environment. If scarcity revaluation were a macro factor, every declining practice would simultaneously gain scarcity premium, which is not how rarity works. Rarity value is conditional on the practice's cultural legibility: a rare practice that is considered outdated gets no scarcity premium; a rare practice that is considered romantic does.

**Fate:** Model as a security-level valuation function: Scarcity Premium = f(prevalence decline rate, social legibility, irreplaceability). This is a fundamental input to Research Fair Value, not a weekly price factor.

---

### Merge: Physicality Displacement (Candidate E) → Physicality Premium (E2) + Human Substitution (S2)

**Action:** Split into two components and merge each into the appropriate factor.

**Reason:** Physicality Displacement as originally proposed conflates two different causal questions: (1) "Is the physical carrier being replaced by a digital equivalent?" which is about Human Substitution (the function is preserved without the physical form), and (2) "How much does the market value physical embodiment per se?" which is the experiential Physicality Premium. The first is a structural trend; the second is a cyclical valuation. A streaming service replacing vinyl is Human Substitution; the market suddenly deciding that vinyl sounds better than streaming is Physicality Premium.

**Fate:** Dematerialization rate becomes an observable indicator loading on Human Substitution. Physicality Premium survives as E2.

---

### Demote: Friction / Inconvenience Premium (Candidate G) → Friction Premium (E1)

**Action:** Survives, but renamed and redefined as a market valuation factor rather than a structural property.

**Reason:** The original framing was ambiguous about whether this was "the level of friction in the environment" (which would be structural and correlated with everything) or "the market's valuation of friction" (which is cyclical and can move independently). The latter is the only version that buys distinct behavior.

**Fate:** Survives as E1 with clarified definition.

---

### Survives: Social Legibility / Status (Candidate I) → Social Legibility (E3)

**Action:** Survives largely as proposed.

**Reason:** This is the only candidate factor that captures the social-semiotic dimension of practice valuation. It is genuinely independent: it can move sharply without any change in technology, time, substitution, mediation, or uncertainty. The objection that it is "psychological rather than technological" is not a problem; real markets price social meaning, and LONGING's whole premise is that social meaning is priced.

---

### Survives but Reclassified: Time Compression (Candidate A), Human Substitution (Candidate B), Mediation (Candidate C), Uncertainty Compression (Candidate D)

**Action:** All four survive as structural factors (S1-S4).

**Reason:** Each has passed the independent movement test. The key insight is that they represent genuinely different causal channels: Time Compression attacks temporal texture, Human Substitution attacks actor identity, Mediation attacks relational architecture, Uncertainty Compression attacks possibility structure. They can move independently in specific scenarios, as documented in Section 6.

---

## 4. Missing Factors

### Missing Factor 1: Economic Time Scarcity

**Definition:** The degree to which people experience their available discretionary time as insufficient, driven by labor market conditions, care obligations, commuting burdens, and economic precarity—distinct from technological time compression.

**Causal mechanism:** Practices that require time investment (waiting for a reply, film photography, handmade objects, live performance) lose value not because technology makes them faster, but because people genuinely have less uncommitted time due to economic conditions. This is a labor-market force, not a technology force. It can move independently: a society with high economic time scarcity can adopt slow technology (e.g., no same-day delivery) but people still lack time for slow practices because they are working two jobs.

**Secular/cyclical/regime behavior:** Cyclical with long secular trends in labor participation and work hours.

**Observable inputs:** OBSERVED: labor force participation rates, average work hours, commute times, childcare costs, leisure time surveys. MODELED: discretionary time availability index. EDITORIAL: analyst assessment of whether economic conditions are squeezing leisure time.

**Why separate from Time Compression:** Time Compression is about the *latency of outcomes* (how long between wanting and getting); Economic Time Scarcity is about the *quantity of uncommitted time* people have. A society can have instant delivery but zero free time, or slow delivery and abundant leisure. These are different causal channels.

**Exposure pattern:** Negative for all time-intensive practices (Handwritten Letter, Film Photography, Handmade Object, Live Performance); near zero for practices that require little time (Waiting for a Reply, which is about attention, not time).

**Double-counting risk:** Correlates with Time Compression over long windows but diverges in specific regimes (e.g., a society that adopts convenience technology while also reducing work hours).

---

### Missing Factor 2: Demographic Cohort Replacement

**Definition:** The degree to which younger cohorts entering the culture have different baseline relationships to practices than older cohorts departing, causing valuation shifts independent of any individual's changing behavior.

**Causal mechanism:** Practices are valued by cohorts, not by a timeless population. When a cohort that values handwritten letters ages out of the market, the practice loses value even if every individual who currently values it continues to do so. This is a demographic force, not a technological or cultural one. It is particularly important for practices whose value is tied to a specific generational experience (e.g., film photography's value to Generation X versus Generation Z).

**Secular/cyclical/regime behavior:** Secular with predictable cohort timing; can produce surprising reversals when younger cohorts rediscover practices (the vinyl revival is partly a cohort effect: younger buyers adopted vinyl without having abandoned it).

**Observable inputs:** OBSERVED: age-stratified adoption and valuation data, cohort size distributions, intergenerational cultural transmission rates. MODELED: cohort replacement index per security. EDITORIAL: analyst judgment on whether a practice is being transmitted across cohorts or dying with its cohort.

**Why separate from Social Legibility:** Social Legibility is about what a practice *signals* in the current cultural moment; Demographic Cohort Replacement is about *who is present* to value it. A practice can be highly legible as authentic but still decline because its valuing cohort is shrinking (e.g., a practice valued intensely by a small elderly cohort).

**Double-counting risk:** Correlates with Social Legibility in some periods, but diverges when a practice becomes newly legible to younger cohorts (revival) or loses legibility among its core cohort (intra-cohort fashion shift).

---

### Missing Factor 3: Attention Scarcity

**Definition:** The degree to which human attention—the capacity to notice, dwell, and attend to a single thing—is fragmented by competing demands, measured as the average duration of uninterrupted attention across the population.

**Causal mechanism:** Practices that require sustained attention (waiting, aimless walking, live performance, solitude, serendipitous discovery) lose value when the population's attentional infrastructure erodes. This is distinct from time scarcity (people may have free time but no attention capacity) and from uncertainty compression (attention can be fragmented even in high-uncertainty environments). It is also distinct from mediation (attention fragmentation can occur without platforms, e.g., through generalized anxiety or ambient media).

**Secular/cyclical/regime behavior:** Secular trending, with cyclical attention-restoration movements.

**Observable inputs:** OBSERVED: attention span measurements, media multitasking data, mindfulness practice adoption rates, reading time surveys. MODELED: attention fragmentation index. EDITORIAL: analyst assessment of whether attention is becoming scarcer or more available.

**Why separate from Economic Time Scarcity:** Time and attention are different resources. A person with abundant free time can still lack the attention to wait for a reply or notice a serendipitous discovery. A person with no free time can still have deep attention capacity for the few practices they do engage in.

**Double-counting risk:** Correlates with Uncertainty Compression (prediction systems often compete for attention) but diverges when attention fragmentation is driven by non-technological causes (e.g., economic anxiety, social fragmentation).

---

### Missing Factor 4: Institutional Trust / Social Capital

**Definition:** The degree to which people trust strangers, institutions, and the social environment sufficiently to engage in practices that require vulnerability, spontaneity, or exposure to unmediated others.

**Causal mechanism:** Unplanned visits, unplanned phone calls, serendipitous encounters with strangers, and live performance all require a baseline level of trust that the unplanned will not be dangerous or unpleasant. When social trust declines, these practices lose value because the expected cost of spontaneity rises. When trust rises, they gain value because spontaneity becomes pleasurable rather than threatening. This is a social capital force, not a technological one.

**Secular/cyclical/regime behavior:** Cyclical with long secular trends in social trust metrics; can shift rapidly during crisis periods.

**Observable inputs:** OBSERVED: generalized trust surveys, crime rates, stranger interaction data, hospitality trends. MODELED: social trust index. EDITORIAL: analyst assessment of whether the current social environment rewards or punishes vulnerability.

**Why separate from Mediation:** Mediation is about whether contact is intermediated; Institutional Trust is about whether unmediated contact is *safe and rewarding*. A society with no mediation but low trust would see unplanned visits decline anyway. A society with high mediation but high trust might see resistance to mediation because people want direct contact.

**Double-counting risk:** Correlates with Mediation in some periods (platforms often emerge in response to trust deficits) but diverges when trust improves without platform adoption declining.

---

## 5. Exposure Matrix

| Security | S1 Time Comp | S2 Human Subst | S3 Mediation | S4 Uncertainty Comp | E1 Friction Prem | E2 Physicality Prem | E3 Social Legibility | E4 Econ Time Scarcity | E5 Demo Cohort | E6 Attention Scarcity | E7 Social Trust | R1 Positioning |
|----------|-------------|---------------|--------------|---------------------|------------------|---------------------|----------------------|----------------------|----------------|----------------------|----------------|----------------|
| Handwritten Letter | -- | -- | - | - | + | + | ++ | -- | -- | - | 0 | varies |
| Waiting for a Reply | -- | - | - | 0 | ++ | 0 | + | - | - | -- | 0 | varies |
| Unplanned Phone Call | -- | - | -- | - | + | - | - | - | - | - | -- | varies |
| Unplanned Visit | -- | 0 | -- | -- | ++ | ++ | + | -- | - | - | -- | varies |
| Aimless Walking | - | 0 | - | -- | + | + | + | -- | - | -- | - | varies |
| Film Photography | - | -- | 0 | 0 | ++ | ++ | ++ | - | -- | - | 0 | varies |
| Physical Media | - | -- | - | 0 | + | ++ | + | - | - | 0 | 0 | varies |
| Serendipitous Discovery | - | - | -- | -- | + | + | + | - | - | -- | -- | varies |
| Handmade Object | - | -- | - | 0 | ++ | ++ | ++ | -- | - | - | 0 | varies |
| Live Performance | - | -- | - | - | ++ | ++ | ++ | -- | - | -- | + | varies |
| Solitude | + | + | + | + | ++ | 0 | + | + | + | ++ | + | varies |

**Notes on surprising exposures:**

- **Solitude** is the only security with positive exposure to structural factors. Time Compression, Human Substitution, Mediation, and Uncertainty Compression all make solitude more valuable by making it scarcer and more legible as a deliberate choice rather than a default state. This is the model's structural winner.

- **Waiting for a Reply** has near-zero exposure to Uncertainty Compression because the wait itself is the practice; the uncertainty is the point. It has strongly positive Friction Premium because the willingness to wait becomes a status signal.

- **Unplanned Visit** has very strong negative Social Trust exposure: this practice requires the most trust, and trust declines hit it hardest.

- **Film Photography** has positive Social Legibility exposure that is currently outweighing its structural negatives—this is what makes a multi-year bull market possible within the model.

- **Aimless Walking** has a surprising negative Attention Scarcity exposure: aimless walking requires the *capacity to be aimless*, which requires sustained attention to one's own wandering. A fragmented attention environment makes aimless walking feel like failure rather than freedom.

---

## 6. Independence Tests

**S1 Time Compression vs. S2 Human Substitution:**

Scenario: A global movement for "slow communication" emerges. People begin deliberately delaying their responses to messages and choosing postal mail for important correspondence. Delivery systems remain equally fast, but people choose to use them more slowly. Time Compression stays flat (the latency infrastructure is unchanged), but Human Substitution rises (people explicitly reject AI-generated or instant communication in favor of human-authored, delayed communication). Result: Waiting for a Reply rises on S2 while staying flat on S1.

**S2 Human Substitution vs. S3 Mediation:**

Scenario: A breakthrough in on-device AI allows people to generate highly personalized handwritten letters, voice messages, and other communication *without using any platform*. The AI runs locally. Human Substitution rises sharply (AI can now replicate human expression convincingly), but Mediation stays flat (no platform is involved; the substitution is a tool, not an intermediary). Result: Handwritten Letter drops on S2 while Mediation-sensitive securities stay flat.

**S3 Mediation vs. S4 Uncertainty Compression:**

Scenario: A new social platform emerges that is explicitly designed for serendipity—it randomly connects strangers for unplanned encounters. The platform increases Mediation (all encounters are intermediated) but decreases Uncertainty Compression (the platform deliberately introduces randomness). Result: Serendipitous Discovery falls on S3 but rises on S4; the net effect is ambiguous and can be attributed separately.

**E1 Friction Premium vs. E2 Physicality Premium:**

Scenario: The cultural moment shifts toward "effortless elegance." High-effort practices are seen as try-hard and pretentious, but physical presence remains valued. People stop making handmade objects (high friction, low status) but continue attending live performances (high friction, high physicality, high status). Friction Premium falls, Physicality Premium stays flat. Result: Handmade Object declines on E1 while Live Performance holds.

**E2 Physicality Premium vs. E3 Social Legibility:**

Scenario: A viral cultural artifact romanticizes digital detox and slow living, but specifically valorizes digital minimalism rather than physical objects. Physical media become legible as clutter rather than authenticity; physical presence becomes legible as meaningful. Physicality Premium holds, Social Legibility shifts. Result: Physical Media declines on E3 while Live Performance holds on E2.

**E4 Economic Time Scarcity vs. E6 Attention Scarcity:**

Scenario: A society adopts a four-day work week, dramatically increasing leisure time. However, attention remains fragmented by ambient media and anxiety. Economic Time Scarcity falls, Attention Scarcity stays high. Result: Handmade Object rises on E4 (people have time), but remains flat on E6 (people lack attention for sustained craft).

**E5 Demographic Cohort Replacement vs. E3 Social Legibility:**

Scenario: A practice is heavily valued by an aging cohort but is not being adopted by younger cohorts. Social Legibility remains high (the practice is widely respected and considered authentic), but Demographic Cohort Replacement trends negative (the valuing population is shrinking). Result: A security can decline on E5 while holding on E3.

**E7 Social Trust vs. E3 Social Legibility:**

Scenario: A well-publicized crime involving a stranger encounter makes unplanned interactions feel dangerous. Social Trust falls sharply. However, the practice of unplanned visits remains socially legible as authentic and neighborly (no one thinks it's pretentious; they just think it's risky). Result: Unplanned Visit falls on E7 while holding on E3.

**R1 Positioning vs. All Fundamental Factors:**

Scenario: All fundamental factors stay flat, but the market has become extremely short a particular security because of a long period of negative sentiment. A minor positive event (a celebrity mentions the practice favorably) triggers a violent short-covering rally. No fundamental factor moves; R1 alone explains the price action.

---

## 7. Event Classification Examples

1. **A major AI company launches a service that generates personalized handwritten letters at scale.**
   - Primary: S2 Human Substitution (+)
   - Secondary: E3 Social Legibility (uncertain—could make handwritten letters feel more authentic or more fake)
   - Risk: Double-counting with S1 if the service also delivers faster than postal mail. Flag: ensure the event is scored separately on S2 (substitution) and S1 (time compression) with different magnitudes if delivery speed is unaffected.

2. **A city government removes all algorithmic route optimization from its public navigation system, reverting to static maps.**
   - Primary: S4 Uncertainty Compression (−)
   - Secondary: S3 Mediation (−, if navigation is less intermediated)
   - Risk: None—these are clearly distinct channels.

3. **A viral essay celebrates the virtue of waiting and delayed gratification.**
   - Primary: E1 Friction Premium (+)
   - Secondary: E3 Social Legibility (+ for waiting-related practices)
   - Risk: Double-counting between E1 and E3. Flag: if the essay changes the *status* of waiting, it's E3; if it changes the *valuation of effort*, it's E1. Score separately with analyst justification.

4. **A major employer introduces a four-day work week.**
   - Primary: E4 Economic Time Scarcity (−)
   - Secondary: E6 Attention Scarcity (uncertain—more time could mean more attention or more fragmentation)
   - Risk: None—these are distinct resources.

5. **A new social platform launches that randomly connects strangers for unplanned in-person encounters.**
   - Primary: S3 Mediation (+)
   - Secondary: S4 Uncertainty Compression (−, because the platform introduces randomness)
   - Secondary: E7 Social Trust (uncertain—could increase trust through positive encounters or decrease it through negative ones)
   - Risk: None, provided the analyst scores each channel separately rather than assuming a net effect.

6. **Film photography is prominently featured in a critically acclaimed film.**
   - Primary: E3 Social Legibility (+)
   - Secondary: E1 Friction Premium (+ if the film valorizes effort; − if it makes film seem effortless)
   - Risk: Double-counting with E1. Flag: the analyst must specify whether the film changes status, effort valuation, or both.

7. **A major city experiences a well-publicized crime wave involving stranger encounters.**
   - Primary: E7 Social Trust (−)
   - Secondary: E3 Social Legibility (− if unplanned contact becomes legible as dangerous)
   - Risk: Double-counting if the analyst conflates "trust" (E7) with "legibility" (E3). Flag: trust is about safety expectations; legibility is about social meaning.

8. **A study shows that average message response latency has dropped from 2 hours to 8 minutes over the past decade.**
   - Primary: S1 Time Compression (+)
   - Secondary: E6 Attention Scarcity (+ if faster response means more fragmentation)
   - Risk: None—these are distinct channels.

9. **A cultural movement emerges around digital minimalism, explicitly rejecting physical clutter.**
   - Primary: E2 Physicality Premium (−)
   - Secondary: E3 Social Legibility (− for physical media, + for digital minimalism)
   - Risk: None—physicality and legibility are distinct dimensions.

10. **A major retailer discontinues physical media entirely, shifting to streaming-only distribution.**
    - Primary: S2 Human Substitution (+) if streaming is perceived as replacing the physical object
    - Secondary: E2 Physicality Premium (−, because physical availability declines)
    - Secondary: E1 Friction Premium (−, because the low-friction option becomes the only option)
    - Risk: Triple-counting risk. Flag: the analyst must specify the magnitudes carefully. S2 captures the replacement of the physical object; E2 captures the market's changing valuation of physicality; E1 captures the changing valuation of friction. These are distinct but require careful scoring.

---

## 8. Attribution Design

The weekly price attribution must be mathematically exact (summing to the total price change) while remaining interpretable. Given the complexity of the factor set, a standard linear factor decomposition is appropriate but must be augmented with interaction handling.

### Proposed Format

```text
SECURITY: HANDWRITTEN LETTER (LTR)
WEEKLY RETURN: +13.84%

COMPONENT ATTRIBUTION:

Structural Factors:
  Time Compression (S1)                    -1.82%
  Human Substitution (S2)                  -3.11%
  Mediation (S3)                           -0.94%
  Uncertainty Compression (S4)             -0.46%
  
Experiential Factors:
  Friction Premium (E1)                    +2.87%
  Physicality Premium (E2)                 +1.23%
  Social Legibility (E3)                   +3.15%
  Economic Time Scarcity (E4)              -0.78%
  Demographic Cohort (E5)                  -0.34%
  Attention Scarcity (E6)                  -0.52%
  Social Trust (E7)                        +0.11%

Reflexive Factor:
  Positioning / Short Covering (R1)        +9.72%

Residual / Interaction                     +2.14%
                                          -------
TOTAL                                      +13.84%
```

### Handling Interaction Effects

The linear decomposition assumes each factor contributes independently. In practice, factors interact (e.g., Time Compression and Human Substitution jointly amplify each other's effect on Waiting for a Reply). Two approaches:

**Approach A: Shapley-style attribution.** Compute the marginal contribution of each factor by evaluating the model with and without that factor, averaging over all possible orderings. This is computationally expensive but mathematically exact and defensible.

**Approach B: Explicit interaction term.** Estimate pairwise interaction coefficients for known causally linked factor pairs (e.g., S1×S2, S3×S4, E1×E3, E2×E7). The interaction term appears as a separate line in the attribution. This is more transparent but requires the interaction coefficients to be estimated or modeled.

**Recommendation:** Use Approach B for known interactions (documented in the factor specification) and fold remaining unexplained variance into the residual line. The residual should not be called "noise" but "unmodeled interaction / other," acknowledging that the model is incomplete.

### Handling Correlated Factor Moves

When factors are correlated in a given week (e.g., S1 and S2 both move together), the attribution should flag this explicitly:

```text
NOTE: S1 and S2 moved together this week (correlation +0.87).
Total structural effect: -6.33% (of which -2.11% is shared variance).
```

This prevents the misleading impression that each factor's contribution is independent when it is not.

### Handling Delayed Pricing

Some events (e.g., a cultural artifact that changes Social Legibility) may not be fully priced in the same week they occur. The attribution should include a line for delayed pricing:

```text
Delayed Pricing (prior week's E3 shock now being priced)  +0.61%
```

This acknowledges that the market is not perfectly efficient and that information filters in over time.

### Confidence Intervals

Each attribution line should carry a confidence interval, reflecting the uncertainty in factor exposure estimates:

```text
Social Legibility (E3)    +3.15%  (± 1.42%)
```

This prevents false precision and communicates that attribution is an estimate, not a fact.

### Full Weekly Ledger

```text
SECURITY: [TICKER]
WEEKLY RETURN: [±X.XX%]

STRUCTURAL FACTORS:
  S1 Time Compression       [±X.XX%] (± CI)
  S2 Human Substitution     [±X.XX%] (± CI)
  S3 Mediation              [±X.XX%] (± CI)
  S4 Uncertainty Compression [±X.XX%] (± CI)

EXPERIENTIAL FACTORS:
  E1 Friction Premium       [±X.XX%] (± CI)
  E2 Physicality Premium    [±X.XX%] (± CI)
  E3 Social Legibility      [±X.XX%] (± CI)
  E4 Economic Time Scarcity [±X.XX%] (± CI)
  E5 Demographic Cohort     [±X.XX%] (± CI)
  E6 Attention Scarcity     [±X.XX%] (± CI)
  E7 Social Trust           [±X.XX%] (± CI)

REFLEXIVE FACTOR:
  R1 Positioning            [±X.XX%] (± CI)

INTERACTION TERMS (if any):
  [S1×S2, S3×S4, E1×E3, etc.]  [±X.XX%]

DELAYED PRICING:
  [Prior period shocks]     [±X.XX%]

RESIDUAL:
  [Unexplained]             [±X.XX%]

TOTAL:                      [±X.XX%]
```

---

## 9. Complexity Risks

### Crossing the Line from Earned Complexity to Pseudo-Quantitative Theater

**Warning Sign 1: Factor count exceeds explanatory power.**
If the model has 12 factors and a typical weekly return is ±5%, the average factor contribution is ±0.4%, which is within noise. The model crosses into theater when individual factor lines are smaller than the residual line on average. Rule: if the residual is consistently larger than most factor contributions, the factors are not doing real work.

**Warning Sign 2: Factors are estimated but never updated.**
If the factor exposures (betas) are set once and never revised based on market data, they are not factors; they are fixed parameters. The model crosses into theater when the exposures are "editorial" but the editorial process is not documented or revisable.

**Warning Sign 3: Every factor moves together every week.**
If the factor correlation matrix shows all factors moving together (average pairwise correlation > 0.7), the factors are redundant. The model crosses into theater when the attribution ledger shows many lines but they all sum to the same thing as one line.

**Warning Sign 4: Attribution is unfalsifiable.**
If every weekly return can be attributed post hoc without any way to test whether the attribution was correct, the model is theater. The model crosses into theater when the attribution cannot be audited by an independent observer using the documented methodology.

**Warning Sign 5: Subjective inputs are not tagged.**
If editorial estimates (e.g., Social Legibility = 76.4) are mixed indistinguishably from observed data (e.g., response latency = 2.1 hours), the model is theater. The model crosses into theater when a reader cannot tell which numbers are measured, which are modeled, and which are judgments.

**Warning Sign 6: Precision without uncertainty.**
If the model reports factor contributions to two decimal places but has no confidence intervals, it is theater. Real factor models have wide uncertainty. The model crosses into theater when +3.15% is reported without ± 1.42%.

**Warning Sign 7: The model always agrees with the artist's thesis.**
If the LONGING index always trends downward and the "structural winners" never actually win, the model is rigged. The model crosses into theater when film photography cannot enter a multi-year bull market even when the modeled world supports it.

---

## 10. Falsification Tests

### Test 1: Film Photography Revival Test

**What it tests:** Whether the model allows analog revivals without hard-coded exceptions.

**Method:** Simulate a 5-year scenario where: (1) a major cultural event (film, celebrity adoption) makes film photography socially legible as highly authentic; (2) E1 Friction Premium rises; (3) E2 Physicality Premium rises; (4) E3 Social Legibility rises sharply; (5) all structural factors continue trending in their secular directions. Run the model with no manual intervention. Verify: can film photography produce a positive 5-year cumulative return exceeding +50%? Can it outperform the LONGING index by more than 80 percentage points?

**Failure condition:** Film photography cannot rally above +20% cumulative over 5 years, or the rally requires manual intervention (e.g., an analyst overriding the model).

**Why this matters:** If the model cannot produce an analog revival organically, it is hard-coded for decline and the artistic thesis (secular bear market with occasional dramatic rallies) is not being modeled but scripted.

---

### Test 2: Structural Winner Test

**What it tests:** Whether the model allows any security to rise secularly.

**Method:** Identify the security with the most favorable structural exposure profile (likely Solitude). Simulate a 10-year scenario with all structural factors trending in their expected directions and all experiential factors neutral. Verify: does Solitude produce a positive 10-year cumulative return exceeding +100%?

**Failure condition:** No security can produce a positive 10-year return under neutral experiential conditions. The model has hard-coded decline.

**Why this matters:** The artist's thesis is that the LONGING world is broadly declining but contains structural winners. If no structural winners exist, the model is rigged.

---

### Test 3: Collinearity Test

**What it tests:** Whether the factors are causally distinct or merely statistically correlated.

**Method:** For each pair of factors, construct a scenario (as in Section 6) where one factor moves strongly while the other stays flat. Then verify: (1) can the scenario be expressed as a series of observable indicator changes? (2) Does the model's factor estimation procedure actually produce divergent factor movements in response to these scenarios? (3) Do the security price effects differ depending on which factor moved?

**Failure condition:** For any pair of factors, no scenario can be constructed where they move independently, or the model's estimation procedure always moves them together regardless of scenario.

**Why this matters:** If factors cannot move independently in practice, they are redundant regardless of their conceptual distinction.

---

### Test 4: Attribution Integrity Test

**What it tests:** Whether the weekly attribution is mathematically exact and auditable.

**Method:** Take 20 consecutive weekly returns for a security. For each week, reproduce the attribution ledger using only: (1) the documented factor estimation procedure; (2) the documented observable indicators; (3) the documented editorial judgments; (4) the documented interaction coefficients. Verify: does the sum of all attribution lines equal the total return to within ±0.01% in all 20 weeks? Can an independent analyst reproduce the attribution using only the documentation?

**Failure condition:** The attribution fails to sum to the total, or the attribution requires undocumented judgments to reproduce.

**Why this matters:** If the attribution is not reproducible, it is not auditable, and the "attribution" is theater.

---

### Test 5: Model-Versus-Artist Disagreement Test

**What it tests:** Whether the model can produce outcomes that contradict the artist's presumed preferences.

**Method:** Construct a scenario where: (1) a practice that the artist presumably values (e.g., Handwritten Letter) becomes highly socially legible as pretentious and outdated (E3 falls sharply); (2) a practice that the artist presumably does not value (e.g., algorithmic optimization of social contact) becomes highly socially legible as authentic and efficient (E3 rises sharply); (3) all other factors stay neutral. Run the model. Verify: does the model produce a bear market for Handwritten Letter and a bull market for the optimization practice, despite the artist's quiet bias toward the human?

**Failure condition:** The model's valuation always aligns with the artist's presumed preferences regardless of the modeled scenario.

**Why this matters:** The brief explicitly states that "the market model must remain capable of disagreeing with the artist." If the model cannot produce an outcome where the artist's preferred practice declines while a "cold" practice rises, the model is propaganda, not research.

---

## 11. Proposed v2 Specification

### Hierarchy

```text
OBSERVABLE INDICATORS (measured monthly, tagged OBSERVED)
        ↓
LATENT FACTORS (8 factors, estimated quarterly, tagged MODELED)
        ↓
SECURITY EXPOSURES (betas, estimated annually, tagged MODELED)
        ↓
FUNDAMENTAL LAYER (Research Fair Value, updated monthly, tagged EDITORIAL)
        ↓
NARRATIVE LAYER (Social Legibility adjustment, updated weekly, tagged EDITORIAL)
        ↓
POSITIONING LAYER (Short covering / crowding, updated weekly, tagged MODELED)
        ↓
WEEKLY MARKET PRICE
```

### Observable Indicators (Monthly, OBSERVED)

The following indicators are collected monthly from real-world and fictional sources:

**Time Compression Indicators:**
- Average message response latency (hours)
- Same-day delivery penetration (% of retail)
- On-demand service availability index
- Real-time availability awareness penetration

**Human Substitution Indicators:**
- AI-generated communication penetration (% of messages)
- Synthetic media quality benchmark
- Automation penetration in relevant service domains
- Substitution feasibility index per security domain

**Mediation Indicators:**
- Platform-mediated social contact penetration (% of interactions)
- Discovery path analysis (platform vs. direct)
- App-mediated communication share
- Intermediary fee extraction rate

**Uncertainty Compression Indicators:**
- Recommendation system penetration (% of choices)
- Prediction accuracy benchmark
- Route optimization adoption rate
- Reservation system coverage (% of venues)

**Economic Time Scarcity Indicators:**
- Average work hours
- Commute time
- Care obligation burden
- Leisure time survey data

**Attention Scarcity Indicators:**
- Average uninterrupted attention duration
- Media multitasking rate
- Mindfulness practice adoption
- Reading time survey data

**Social Trust Indicators:**
- Generalized trust survey
- Stranger interaction rate
- Crime rate
- Hospitality trends

**Demographic Indicators:**
- Age-stratified adoption data per security
- Cohort size distributions
- Intergenerational transmission rates

### Latent Factor Estimation (Quarterly, MODELED)

Each latent factor is estimated as a weighted combination of its observable indicators, with weights estimated via a documented procedure (e.g., principal component analysis, confirmatory factor analysis, or expert-weighted index). The estimation procedure is documented and revisable.

**Factor Specification:**

| Factor | Type | Persistence | Observable Indicators |
|--------|------|-------------|----------------------|
| S1 Time Compression | Structural | High (annual half-life) | Response latency, delivery speed, on-demand index |
| S2 Human Substitution | Structural | High | AI penetration, automation, substitution feasibility |
| S3 Mediation | Structural | High | Platform penetration, discovery path, intermediary fee |
| S4 Uncertainty Compression | Structural | High | Recommendation penetration, prediction accuracy, optimization |
| E1 Friction Premium | Experiential | Medium (quarterly half-life) | Analog-digital price spread, high-effort goods sales, cultural sentiment |
| E2 Physicality Premium | Experiential | Medium | Physical media price premium, event attendance, physical goods sales |
| E3 Social Legibility | Experiential | Low (weekly half-life) | Social media sentiment, media coverage, cultural criticism |
| E4 Economic Time Scarcity | Experiential | Medium | Work hours, commute, care burden, leisure time |
| E5 Demographic Cohort | Experiential | High (annual half-life) | Age-stratified adoption, cohort size, transmission rates |
| E6 Attention Scarcity | Experiential | Medium | Attention duration, multitasking, mindfulness, reading time |
| E7 Social Trust | Experiential | Medium | Trust surveys, stranger interaction, crime, hospitality |
| R1 Positioning | Reflexive | Low (weekly half-life) | Market positioning data, consensus ratings, flow data |

**Note:** This is 12 factors, not 8. The four structural factors (S1-S4), seven experiential factors (E1-E7), and one reflexive factor (R1). I have added E4-E7 from the missing factors section. This is justified because each has passed the independent movement test and adds a genuinely distinct causal story.

### Security Exposure Estimation (Annual, MODELED)

Each security has a beta for each factor, estimated annually based on:
- Historical price sensitivity to factor movements
- Analyst judgment on structural exposure
- Cross-sectional comparison with similar securities

Exposures are tagged as MODELED and documented with estimation methodology.

### Fundamental Layer: Research Fair Value (Monthly, EDITORIAL)

Research Fair Value is the analyst team's estimate of underlying value, computed as:

```text
Research Fair Value = f(
  Prevalence Trend,
  Cultural Attachment,
  Replacement Resistance,
  Expected 5Y Persistence,
  Scarcity Premium,
  Irreplaceability Index
)
```

These inputs are EDITORIAL: they are analyst judgments, documented and reproducible, but not directly observed. The function is a documented valuation model (e.g., discounted future practice value).

### Narrative Layer: Social Legibility Adjustment (Weekly, EDITORIAL)

The Social Legibility factor (E3) is estimated weekly based on:
- Social media sentiment tracking
- Media coverage analysis
- Cultural criticism monitoring
- Analyst judgment on shifts in social meaning

This is the fastest-moving fundamental factor and is tagged EDITORIAL because it requires interpretation of cultural signals.

### Positioning Layer: Short Covering (Weekly, MODELED)

The positioning factor (R1) is modeled based on:
- Market positioning data (long/short ratios)
- Consensus ratings
- Flow data
- Historical positioning-return relationships

This is MODELED because it can be quantified from market data, but the model specification requires judgment.

### Weekly Price Formation

The weekly price change is decomposed as:

```text
ΔPrice = Σ(β_i × ΔFactor_i) + Interaction Terms + Delayed Pricing + Residual
```

Where:
- β_i are security exposures (estimated annually)
- ΔFactor_i are factor changes (estimated weekly for E3 and R1, monthly for others, with interpolation)
- Interaction terms are estimated for known causally linked factor pairs
- Delayed pricing captures shocks from prior periods that are being priced in the current week
- Residual is the unexplained component, always reported with the attribution

### Documentation Requirements

Every number in the model must be tagged:

- **OBSERVED:** From a real or fictional data source, with source documented
- **MODELED:** Produced by a documented estimation procedure
- **EDITORIAL:** An analyst judgment, with justification documented

No number may appear without a tag. This is the core anti-theater rule.

### Model Governance

- **Monthly:** Analyst team reviews factor estimates, updates Research Fair Value, publishes attribution
- **Quarterly:** Methodology review, factor exposure re-estimation, constituent review
- **Annually:** Full model review, factor architecture review, falsification tests

The model is designed to be complex, documented, and auditable—while acknowledging that some inputs are subjective. The subjectivity is not hidden; it is tagged, justified, and revisable.

---

**End of v2 Specification**