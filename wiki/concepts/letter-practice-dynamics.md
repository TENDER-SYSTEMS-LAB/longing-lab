---
status: working
attribution: llm-proposed
updated: 2026-09-07
sources:
  - SRC-2026-09-06-world-rules-letter-spec-request
  - SRC-2026-09-06-worldbuilding-roadmap-request
  - SRC-2026-09-06-academic-model-recovered-excerpts
  - SRC-2026-09-05-price-formation-market-model
---

# LETTER Practice Dynamics

This is a reviewable proposal for stage 2 of [[worldbuilding-roadmap]], paired with [[world-rules]]. The user requires distinct starts and interruptions, feedback, a current scenario without real data, and recovery under the same rules. **The boundaries, state convention, equations, coefficients, and examples below are assistant assumptions for a trial, not user decisions or empirical estimates.** The specification answers the user's three questions in order. It computes practice before estimating its value or quoting its price.

The provisional population is a closed cohort of 10,000 adults in one fictional, contemporary dense city. Count the sender's practice; recipients may live outside the cohort. This short rehearsal excludes migration, aging, and deaths. It cannot support claims about a country or humanity. Use the weekly intervals and monthly publication schedule proposed in [[world-rules]]; event time, observation period, and publication date remain separate.

## 1. What should be computed?

### What counts as a letter

Count a **personally composed, physically handwritten message intended for a particular person and released to that person through a delivery route**. A qualifying dispatch is the completed practice occasion. It is not a sale, receipt, reply, search, or statement that letters matter.

| Included in the trial | Excluded or recorded separately |
|---|---|
| A personal letter posted, entrusted to a courier, or handed over | An unsent draft or a letter kept in a drawer: effort may occur, but no qualifying dispatch |
| A postcard or greeting card with a substantive personal handwritten message | A signature or standard greeting added to otherwise printed material |
| A letter dictated by its author to a human assisting with handwriting, with assistance flagged | Machine handwriting, printed correspondence, email, messages, and a service composing and sending a substitute for the person |
| Personal correspondence between relatives, friends, partners, or a newly chosen pen pal | Bills, forms, advertising, copied campaign messages, and impersonal commercial correspondence |
| A letter whose delivery fails after a genuine dispatch | Failed delivery is a separate outcome, not deletion of the sender's completed practice |
| Personal content drafted with spelling, translation, or accessibility assistance | Copying stock or machine-generated text without personal composition; the boundary requires an explicit coding decision |

There is no word-count or emotional-intensity threshold. The substantive-message distinction concerns personal communication beyond authentication or a formula; doubtful cases remain `UNCLASSIFIED` until reviewed. A multi-page letter is one dispatch; separately addressed letters are separate occasions. One joint letter is one occasion, allocated equally among its composing senders for cohort aggregation, rather than multiplied by author count. A later reply is another sender's occasion. Receiving a letter alone does not make a person a writer.

**Choice to review:** count assisted personal composition with an assistance flag, as proposed, or restrict LETTER to the author's own hand and put assisted correspondence in an adjacent practice. Inclusion emphasizes personal effort and address; restriction emphasizes bodily inscription but changes which people the measure represents. The recommendation includes assistance and preserves the distinction in metadata. Neither provenance nor emotional worth can be inferred from postal totals.

### Stocks, flows, and outputs

The proposed state describes **practice episodes**, not whether every practitioner writes every week. An episode opens with a qualifying dispatch and remains open while the person sustains a plan to write again to an identifiable addressee. Operational coding asks about a current named recipient or continuing correspondence; a general wish to write someday is insufficient. A weekly decision can suspend that episode. A newly initiated one-off occasion can therefore enter the open state for one interval and close at the next boundary. This is a declared weekly approximation, not proof of a durable habit.

| Symbol | Meaning | Unit and bound |
|---|---|---|
| `U_t` | Cohort members who have never begun a qualifying episode | Expected people; 0–10,000 |
| `A_t` | People with an open practice episode at the opening of week t | Expected people; 0–10,000 |
| `D_t` | Previously begun, currently interrupted | Expected people; 0–10,000 |
| `n_t`, `r_t`, `c_t` | First starts, resumptions, interruptions during the week | Expected people/week; bounded by the relevant opening stock |
| `C_t` | Opening practitioners who continue their episode through this week | Expected people; `A_t - c_t` |
| `m_t` | Established practitioners' qualifying dispatch intensity | Letters per continuing-practitioner-week; trial bound 0–2 |
| `e_start,t`, `e_resume,t` | Cohort-attributed letters per entrant after allocating joint authorship | Letters/entrant; greater than 0 and at most 1 for the single-entry-occasion convention; trial 1 |
| `Q_t` | All cohort-attributed qualifying dispatches in the week | Expected letters/week; nonnegative |
| `J_t` | Meaningful acknowledgments arriving back to senders | Expected acknowledgment events/week; not necessarily reply letters |
| `F_t` | Recent reinforcement from responsive correspondence | Dimensionless constructed state; 0–1; not a percentage of people |
| `H_t` | Meaningful reachable-addressee opportunity, a condition below | Normalized condition derived from counterparties/person, not from population prevalence |

Fractional expected counts are acceptable in the calculation. They are not literal fractional people. An eventual individual-level realization must preserve identities and totals; no method for generating that realization is adopted here.

Compute per week, using opening stocks and at most one state transition per person:

```text
n_t = U_t * p_start,t
r_t = D_t * p_resume,t
c_t = A_t * p_stop,t
C_t = A_t - c_t

U_(t+1) = U_t - n_t
A_(t+1) = C_t + n_t + r_t
D_(t+1) = D_t + c_t - r_t
Q_t = m_t * C_t + e_start,t * n_t + e_resume,t * r_t
```

Each starter and restarter participates in one qualifying dispatch in the entry week. The entry weights preserve authorship allocation: two first-time cohort members composing one letter give `n=2` and `e_start=.5`, hence one entry letter. `m` uses the same allocation for continuing composers. The numerical check assumes singly authored entries with both entry weights equal to 1. Further entry-week letters are deferred by this simplified accounting; occasion detail would be needed to remove that approximation. Interruption happens before established dispatches in the weekly convention; someone who sends and then stops is classified at the next boundary. Thus `U+A+D=10,000` and `Delta A=n+r-c` exactly. There is no loss term inserted merely to make the series decline.

**No letter this week does not equal interruption.** An annual correspondent can sustain an episode between occasions; an explicit suspension can occur soon after a letter. A rolling 13-week writer count is a useful, separate observation, but cannot be calculated from these aggregate stocks: it needs dated sender histories. Never rename `A` as that observed count. `A` is partly latent and the institution must estimate it. `Q` is a behavior quantity with a precise coding boundary, but fictional `Q` remains modeled, not a real measurement.

Track receipt and acknowledgments separately. Delivery success changes what the recipient experiences; acknowledgment can arrive by letter, call, or message. Digital contact may therefore substitute for one writing occasion while complementing the continuation of correspondence. People may practice LETTER, calling, and photography simultaneously; no exclusive 100% allocation across securities is assumed.

Attention and discourse are parallel records: searches or views per week; posts per week and their separately coded meaning. A trial may use an index with a named base period, but none enters `Q` by definition. Total postal volume, which includes excluded mail, is not LETTER dispatch volume. See [[data-sources]].

## 2. What increases or decreases it?

### Conditions and direct routes

The following local conditions are distinct inputs, not a selected common factor architecture. Normalization places each within `[-1,1]` around a declared reference; it does not make their units or causes interchangeable.

| Input | Physical or coding interpretation; illustrative reference and one normalized step | Proposed direct route | Trial lag |
|---|---|---|---|
| `T` available time | Uninterrupted discretionary minutes/person/week: reference 40, step 20 | More time raises starts, resumptions, and intensity; lowers interruption | 0–2 weeks |
| `E` effort burden | Preparation/writing/dispatch minutes per qualifying letter: reference 30, step 10 | More burden lowers starts, resumptions, and intensity; raises interruption | 0–2 weeks |
| `H` relational opportunity | Mean meaningful reachable potential correspondents/person: reference 1, step 0.5 | An addressee and occasion make entry and continuation feasible | 1–4 weeks |
| `I` infrastructure access | Fraction of suitable dispatch windows accessible: reference 0.8, step 0.2 | Better access raises entry and intensity; reduces interruption | 0–4 weeks |
| `S` substitute attractiveness | Explicit editorial assessment, reference 50/100, step 25 | A sufficiently adequate faster substitute can suppress letter choice | 0–4 weeks |

For example, `T=clip((minutes-40)/20,-1,1)`. The other columns use the same stated transformation. These numerical anchors are trial choices. The rates are local aggregate propensities, not an enforced individual time budget: a ratio of cohort mean available time to mean effort cannot establish each person's feasible output. Individual time/effort caps require subgroup or person-level detail. The clipping range is a local perturbation envelope, not a license to describe a total service shutdown as a small access change. If **no feasible sender-to-recipient route exists**, a separate feasibility gate sets `p_start=p_resume=m=0`; current episodes may wait or interrupt under `p_stop`. A regional delivery outage is not automatically such a gate if hand delivery remains possible.

Distinct paths need distinct meanings. A collection-point closure may reduce available dispatch windows (`I`) and add travel burden (`E`); record both intermediate changes if both occur. Do not add a third direct decrement to `Q` for the same closure. A rise in postal charges needs an affordability variable or an explicit conversion to participation burden before entering this specification; do not hide it inside a generic bad-news score. Waiting pleasure, relationship intensity, skills, and differing reactions to substitutes remain possible extensions, not anonymous residual factors.

### Proposed feedback and alternatives

**Recommended first loop, for a trial:** a qualifying dispatch creates an opportunity for a meaningful acknowledgment; acknowledgment sustains responsiveness; responsiveness reduces the chance of interrupting and supports repeat occasions; those occasions create further acknowledgment opportunities. It returns to its cause:

```text
Q dispatches -> delivery and response -> J acknowledgments
       ^                                     |
       |                              delayed update of F
       |                                     |
       +-- continuing A and intensity m <----+
                        ^                    |
                        +-- fewer stops <----+
```

Use an aggregate response environment initially, not a claim that any stranger's letter helps every writer equally. This homogeneity assumption is material: missing local relationships could make aggregate density misleading. A later network or subgroup model would compute who can reinforce whom. `H` describes available meaningful counterparties; `F` describes reinforcement from recent exchanges. One must not be manufactured merely by renaming the other.

The illustrative loop is:

```text
J_t = delivery_success_(t-2) * acknowledgment_fraction_(t-2) * Q_(t-2)
F_(t+1) = (1-lambda)*F_t + lambda*clip(J_t/J_ref, 0, 1)
```

`J_ref` has units of acknowledgment events/week, so its ratio is dimensionless. For the numerical check use delivery success 1, acknowledgment fraction 0.5, `J_ref=400/week`, and `lambda=0.25/week-step`. The two-week delay packages delivery and response; update `F` after the week's dispatch calculation, so the first practice effect arrives in week 4 for a week-1 event. Saturation represents diminishing additional reinforcement; it is a designed limit, not a fitted threshold.

An alternative loop is `Q falls -> local service demand falls -> access is withdrawn -> I falls -> starts/intensity fall -> Q falls`, with an illustrative 8–26-week service decision delay. That would require service costs, a withdrawal authority, and reopening rules. The relational loop is recommended first because LETTER can be tested without inventing that additional institution. The infrastructure loop is **not activated** in the trial. Nor is a third possible loop, attention attracting new writers, unless a mechanism such as an accessible workshop changes an actual condition or entry probability.

Break the selected loop by setting its coefficients in both interruption and intensity to zero; keep the same condition history and starting stocks. Compare the resulting `A` and `Q` paths to distinguish direct shocks from reinforcement. One such deterministic ablation is reported below; broader delay/gain comparisons remain proposed, and neither establishes empirical causality. Audience LONG/HOLD/SHORT and market prices have no arrow into these equations. Practice feedback does not decide audience price influence; see [[analyst-system]] and [[world-rules]].

### Events, behavior, and institutional knowledge

| Authored event | Practice route | Observation and assessment |
|---|---|---|
| A nostalgic campaign coincides with shorter free-time windows and fewer collection opportunities | Attention rises; `T` and `I` fall. Entry weakens, interruptions rise, and dispatch intensity drops | The Event Desk can report the campaign and closure separately. The next monthly release distinguishes dispatch estimates from search/post indices; analysts may disagree about persistence |
| A widely advertised letter-writing workshop is inaccessible to the relevant cohort | Publicity alone changes attention. No available time, addressee, or access condition changes | Do not infer new writers from publicity. Report attendance or completed qualifying dispatches only if the world supplies that observation |
| Protected weekly time and accessible collection are restored | `T` and `I` rise; an adequate substitute becomes less dominant in choice (`S` falls). Starts/resumptions rise and interruptions fall | Dispatch changes precede the delayed reinforcement response. A later estimate can revise the recovery's scale without rewriting the earlier release |
| A report falsely claims all collection points closed | No actual condition changes; underlying `Q` follows the unchanged world | The institution may initially estimate worse conditions. Correct the report and preserve its vintage; belief/price effects belong to the next information design stage |

The authoring layer knows the scripted event and computed state. LONGING receives reports and observations under an as-yet-unselected measurement rule. A monthly release must label the practice period, estimate vintage, method, and uncertainty; `Q`, an institutional estimate of `Q`, a valuation of its prospects, and market price are four different objects. This page specifies an observation target, not a fictional survey generator or an estimate-error distribution. See [[information-quality]] and [[pricing-model]].

## 3. How can strengths be set without real data?

### An inspectable trial parameterization

Start with conservation and explicit signs, then choose a range of effects in understandable units. Do not fit a pleasing falling curve and retroactively assign causes. No existing paper supplies these coefficients. The elementary stock bookkeeping is an original trial specification; the candidates in [[academic-model-survey]] remain available if a named missing computation needs one.

The numerical check uses these weekly probabilities and intensity, with conditions evaluated after their stated lag:

```text
p_start  = clip(.002 + .001*T - .0005*E + .001*H + .001*I - .001*S, 0, .02)
p_resume = clip(.010 + .003*T - .002*E  + .003*H + .004*I - .004*S, 0, .10)
p_stop   = clip(.025 - .008*T + .004*E  - .006*H - .006*I + .008*S
                    - .010*(F-.5), 0, .20)
m        = clip(.400 + .080*T - .080*E + .040*H + .080*I - .080*S
                    + .080*(F-.5), 0, 2)
```

A coefficient of `.001` changes a weekly probability by **0.1 percentage point** for one normalized input unit, not by 0.1%. `m` coefficients are letters per continuing-practitioner-week per normalized unit. These are discrete weekly probabilities; do not insert annual hazards without conversion. Initial stocks and history are also assumptions.

| Parameter family | Working value | Proposed challenge range; not an uncertainty interval | Delay/bound |
|---|---|---|---|
| Reference start probability | .002/week | .0001–.006/week | Bound 0–.02 |
| Reference resume probability | .010/week | .002–.030/week | Bound 0–.10 |
| Reference interruption probability | .025/week | .005–.060/week | Bound 0–.20 |
| Reference established intensity | .400 letters/person/week | .10–.80 | Bound 0–2 |
| Direct input coefficients | Signed values above | From zero to twice each displayed magnitude, retaining its sign | Vary each input's lag across its table range |
| Reinforcement effect on interruption | -.010 probability per F unit | [-.020, 0] | Following the delayed F update |
| Reinforcement effect on intensity | +.080 letters/person/week per F unit | [0, .160] | Following the delayed F update |
| Response probability; reference scale | .5; 400 acknowledgments/week | [0, .8]; 200–800/week | Response delay 1–6 weeks; success in [0,1] |
| Reinforcement update fraction | .25 | .10–.50 | F remains [0,1] |

First compare isolated changes, then combined events and selected extreme combinations. Count how often clipping occurs: persistent saturation can hide an unsuitable coefficient range. Report when recovery, decline, or sign stability depends on a narrow assumption. Ranges including zero deliberately allow a proposed mechanism to have no effect. This is sensitivity work to be performed, not a claim that all proposed parameter combinations pass.

### Reproducible decline and recovery check

Use opening stocks `U=8000, A=1000, D=1000`, `F=.5`, and two prior weeks each with `Q=400`. Hold `E=H=0`, use the feasibility gate 1, and take direct input lag zero. All values are expectations.

At reference conditions `T=I=S=0`, starts are 16, resumptions 10, interruptions 25, and continuing practitioners 975. Therefore `A_next=1001` and `Q=.4*975+16+10=416`.

For one adverse week, set `T=I=-.5, S=+.5`. The same equations give `p_start=.0005`, `p_resume=.0045`, `p_stop=.036`, and `m=.28`. Starts are 4, resumptions 4.5, and interruptions 36:

```text
U_next = 7996
A_next = 1000 - 36 + 4 + 4.5 = 972.5
D_next = 1000 + 36 - 4.5 = 1031.5
Q = .28*964 + 4 + 4.5 = 278.42
```

Independently script the attention index from 100 to 150 and posts from 100 to 180/week. Attention rises 50%, while dispatches are 33.07% below the same-opening-state reference result. Those are different units and different measures; their difference is not a price or a combined score. The quantities were chosen to expose divergence, not generated to resemble real observations.

From the adverse closing stocks, restore and improve conditions with `T=I=+.5, S=-.5`. With the unchanged initial lagged `F=.5`, the rates become `.0035, .0155, .014` and intensity `.52`. Starts are 27.986, resumptions 15.98825, and interruptions 13.615. Therefore `A_next=1002.85925`, and `Q=.52*958.885+27.986+15.98825=542.59445`. This is recovery under the same equations, not an inserted positive return.

The adverse week's acknowledgment signal reaches the reinforcement update two weeks later: `F_new=.75*.5+.25*(.5*278.42/400)=.46200625`. That weaker reinforcement raises the subsequent interruption probability by `.0003799375` and lowers intensity by `.0030395`, compared with holding `F=.5` under the same current conditions. The loop's delayed adverse effect can therefore coexist with already improved conditions.

A deterministic 27-step recurrence was checked with one adverse week followed by 26 improved weeks, using these exact rules and no random draws:

| Closing week | Open-episode stock A | Weekly dispatches Q | F carried into next week |
|---|---:|---:|---:|
| 1 | 972.50 | 278.42 | .5000 |
| 2 | 1002.86 | 542.59 | .5000 |
| 3 | 1032.66 | 558.03 | .4620 |
| 13 | 1318.71 | 734.24 | .7993 |
| 27 | 1700.44 | 969.24 | .9937 |

To reproduce, store `Q[-2]=Q[-1]=400`, iterate `t=0..26`, set `T=I=-.5,S=.5` only at `t=0` and reverse them thereafter, calculate rates/flows/Q from opening stocks and F, calculate `F_next=.75*F+.25*clip(.5*Q[t-2]/400,0,1)`, then commit all next stocks and F together. Keep unrounded values until display. Stock conservation and nonnegative states hold in this check.

The same replay with only the two feedback coefficients set to zero gives week-27 `A=1613.88` and `Q=859.57`. Freezing `F=.5` instead gives the same practice trajectory. Recovery therefore also occurs without this loop; the selected reinforcement amplifies later recovery rather than supplying the only reason for it. The full and ablated runs conserve 10,000 people to floating-point precision and stay within the stated state bounds. This single comparison does not establish robustness across the proposed parameter ranges.

This demonstrates a sustained recovery path in one authored scenario; it is not calibration, a natural synthetic-data method, proof of universal stability, or validation of secular decline. A closed cohort eventually exhausts first-time entrants; resumption and interruption can still maintain practice. At fixed positive resume and stop probabilities with `U=0`, the stationary episode stock is `N*p_resume/(p_resume+p_stop)`. Feedback makes those probabilities state-dependent, so that expression alone does not solve the full loop. Births, departures, identity histories, heterogeneous writing rhythms, and feedback stability remain outside this check.

### What cannot yet be determined

No available evidence identifies baseline prevalence, initial prior-use histories, effect strengths, acknowledgment rates, seasonal occasions, response delays, subgroup exposure, or causal attribution from aggregate observations. A measured dispatch total alone cannot distinguish more practitioners from higher intensity, or fewer starts from more interruptions. Even the proposed sign of substitution may vary by context. Personal preciousness and pleasure from waiting are not calculated here and must not be smuggled into a behavior coefficient.

The next tests should compare the episode convention with an observed-window alternative using sender histories; try zero feedback and alternate lag/gain settings; and compare LETTER with a solitary and an infrastructure-dependent practice. LETTER's completed example tests a connected mechanism. It does not verify the full factor vocabulary, exposure structure, or identification. Factors may outnumber securities; no former count ratio is reinstated.

## Handoff to information, value, and price

The next stage must choose the quoted object and unit in [[Q-004-unit-of-account]] and [[world-rules]] before converting these states into money-like numbers. In particular:

- Choose the valuation target: future dispatch flow, continued participation, a particular experiential condition, or an explicitly defined combination. `A`, `Q`, receipt, and relationship quality are not substitutes for one another.
- Set the horizon, normalization, uncertainty treatment, and any scarcity effect. A trailing dispatch rate and an expected next-52-week dispatch total are different objects. If a claim settles on future Q, define the release vintage and revision policy used for settlement.
- Define the institution's observation sample, reporting delay, measurement error, and revisions. A no-observation period is not zero practice. Decide what analysts can forecast independently of the price they help anchor.
- Specify fundamental valuation versus analyst market-price targets; then market participants' resources, positioning, counterparties, and any arbitrage. Nothing in these practice equations makes one episode a transferable share.
- Choose whether and how actual audience behavior enters the fictional world. The current trial records viewer positions separately; neither a vote nor a reported intention is a qualifying letter.

Practice absence, inability to observe, coverage ending, delisting, and return follow separate lifecycle rules in [[world-rules]] and [[Q-002-listing-lifecycle]]. Expected `Q` approaching zero does not establish literal extinction; finite-person disappearance requires an explicit realization or an authored absence state.

## Evolution and sources

The earlier Wiki left the three model-application questions unanswered and had not selected a feedback loop or generator. The present user request commissions a concrete draft. This page advances those questions to one inspectable trial with alternative boundaries and unselected extensions. It does not promote the trial into a confirmed mechanism or select a natural-looking data generator.

## Sources

- [[SRC-2026-09-06-world-rules-letter-spec-request]] — [raw/documents/2026-09-06-world-rules-letter-spec-request.md](../../raw/documents/2026-09-06-world-rules-letter-spec-request.md); user authority for these deliverables and constraints, not approval of this page's assistant-designed rules or numerical assumptions
- [[SRC-2026-09-06-worldbuilding-roadmap-request]] — [raw/documents/2026-09-06-worldbuilding-roadmap-request.md](../../raw/documents/2026-09-06-worldbuilding-roadmap-request.md); preceding scope assessment, synthesized in [[worldbuilding-roadmap]]
- [[SRC-2026-09-06-academic-model-recovered-excerpts]] — [raw/conversations/2026-09-06-academic-model-recovered-excerpts.md](../../raw/conversations/2026-09-06-academic-model-recovered-excerpts.md); earlier user directions on starts/stops, feedback, unavailable real data, and explanation before model selection, maintained in [[academic-model-survey]] and [[data-sources]]
- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md); cadence and emergent-decline constraint, maintained in [[DEC-003-weekly-market-monthly-research]] and [[DEC-004-secular-decline-with-rallies]]
