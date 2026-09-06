---
status: working
attribution: llm-proposed
updated: 2026-09-07
sources:
  - SRC-2026-09-06-world-rules-letter-spec-request
  - SRC-2026-09-06-worldbuilding-roadmap-request
  - SRC-2026-09-04-longing-concept-brainstorm
  - SRC-2026-09-05-price-formation-market-model
  - SRC-2026-09-06-arbitrage-news-quality-and-next-work-items
---

# World Rules — Provisional Design

This is the first-stage specification requested in [[worldbuilding-roadmap]], developed alongside [[letter-practice-dynamics]]. **Every new rule and number below is an LLM proposal for review, not a user decision or an empirical description.** The user has selected the design task and its consistency criterion; selecting the task does not select these answers.

## Existing commitments and choices in this draft

The named work, human-practice subject, weekly prices, monthly research, and requirement that decline emerge rather than be imposed are already recorded. The research-house form and stance-only audience encounter were accepted provisionally; the original source explicitly removes the viewer's Buy / Sell buttons. This limits audience interaction, not the possible existence of separate fictional market actors. See [[DEC-002-research-house-form]] and [[DEC-003-weekly-market-monthly-research]]. Separate starts and interruptions, practice feedback, and the current unavailable-real-data scenario are user directions. No particular feedback loop, synthetic generator, unit, valuation bridge, or audience-to-price mechanism has been adopted.

This draft makes the geography, institution, actors, memory, and lifecycle concrete enough to test. The unit remains a consequential choice among three specified branches in [[Q-004-unit-of-account]]. The recommended branch for a world with finite positions is a funded fictional forecast claim; a publication-only quote is a viable smaller rehearsal. Neither changes the viewer into a trader.

## 1. Whose world

**Trial assumption W1:** a fictional dense city district with a fixed cohort of **10,000 adults**, in a technological and social era comparable to 2026. It has apartment mailboxes, a postal network, hand delivery, stationery shops, shared writing rooms, shift work, digital messaging, and reachable contacts outside the district. These are designed institutions with declared conditions, not claims about a named real city's services.

The cohort is the denominator of the first 52-week exercise. A person's qualifying letter belongs to this cohort when its sender belongs to it; its addressee can live elsewhere. A received letter from outside can affect an in-cohort person's behavior without being counted as an in-cohort send. Other practices need equally explicit assignment rules. Two inhabitants can perform several listed practices in the same week: the universe is not a partition of a fixed 100% of human activity.

The closed cohort deliberately omits aging, deaths, migration, and membership turnover during the short exercise. A longer history must either add explicit entry/exit flows or describe a fixed-cohort study whose members age. It cannot quietly refresh the denominator while drawing an uninterrupted prevalence chart. A 1998–2026 price history is not established by this trial; any later back-history needs a separately declared population, method, and simulated-history label.

| Geographic choice | What it enables | Cost / recommendation |
|---|---|---|
| Fictional district, 10,000-adult closed cohort | Exact denominators, traceable local infrastructure, individual starts and restarts, a coherent first slice | Recommended trial. Specify local institutions so that “generic city” does not conceal a universal human claim. Results apply to this designed cohort only. |
| A named contemporary city, with a fictional or observed panel | Cultural and geographical specificity in letters, labor, and postal arrangements | Strong alternative if the place is part of the work's meaning. Requires choosing the city, its inclusion rules, and which claims are fictional versus evidenced. |
| A transnational population | Broad world index and contrasting institutions | Adds incompatible denominators, languages, delivery networks, and observation access before the first practice is specified. Develop after a reason for cross-region comparison emerges. |

## 2. The real–fictional boundary

The artwork and its audience are real. The cohort, its practices, its institutions, its reports, and any market credits are fictional in this scenario. Real technological developments can inform an authored fictional event, but do not automatically become measured changes in this cohort. Record the real reference, the fictional transformation, and the hypothetical effect separately if that route is used.

Methodology identifies the edition as a modeled fictional population; each numerical release carries its universe, period, and source class. A simulated dispatch count is labeled `MODELED`; an audience stance distribution is labeled `AUDIENCE`. A later empirical source may enter a named observation channel with its own scope and limitations. It does not turn an already simulated history into observed history.

There are three separate knowledge levels: **the designed underlying history**, **what a source or observer reports**, and **what the research house and market infer**. The institution does not receive the author's full state table. A false report can change estimates while actual practice remains unchanged. A later correction preserves the earlier report and records when the correction became known. This is a required boundary for the next information design, not an adopted error generator. See [[information-quality]].

## 3. What the institution does and controls

**Trial assumption W2:** LONGING is an independent research publisher with a Methodology and Listings Committee, a Measurement Desk, an Event Desk, and the four analyst philosophies already proposed in [[analyst-system]]. These are roles; a complete organizational history or biography is unnecessary for the first slice.

| Function | Permitted claims and acts | Limit |
|---|---|---|
| Measurement Desk | Publish qualifying-send observations, panel coverage, response counts, uncertainty, and revisions; estimate active episodes and starts/stops from the evidence available | A postal total alone cannot identify handwritten personal letters; a missed response is missing, not zero. Latent ongoing intention is not directly measured by envelope counts. |
| Event Desk | Register underlying-event references and incoming reports, timestamps, affected conditions, magnitude claims, and confidence; issue corrections | Relevance is distinct from a LONG/SHORT judgment. It cannot create an actual practice change by declaring one. |
| Analysts | Publish estimates of state, an institutional-value argument, price forecasts at stated horizons, ratings, and conviction; change their views on record | They do not rewrite a realized count, settle a contract by opinion, or erase a losing forecast. Price-forecast performance is separate from practice-forecast performance. |
| Methodology and Listings Committee | Define eligible practice boundaries, denominators, listing identifiers, observation standards, quote rules, index methods, and prospective changes; initiate/suspend/end quotations with reasons | It controls coverage and publication, not whether an inhabitant writes a letter. Low prevalence is not automatically a delisting reason. |
| Publication and archive | Release weekly closes, monthly research, notices, corrections, and versioned methods; preserve dates and prior versions | A corrected current estimate must not replace what visitors or analysts actually saw earlier. |

**Observation fixture for review:** start with a fictional 500-person sentinel panel drawn from the 10,000-person cohort. Collect qualifying sends, recipient acknowledgement, episode starts/restarts/interruptions, and time/access conditions. Show attempted and responding panel counts separately; no response-rate, representativeness, or precision is assumed. The sampling procedure, reporting bias, reporting lag, and conversion into cohort estimates are next-stage decisions. The fixture defines a source of imperfect institutional knowledge, not a finished estimator. A designed underlying count can be retained privately to test errors.

For the lifecycle rehearsal, propose provisional weekly observation releases and a monthly consolidated statement that can revise them. This gives the four-week admission fixture and the two-missed-monthly-release observation-stop fixture in [[Q-002-listing-lifecycle]] different, explicit clocks. A provisional release may report missingness instead of a fresh count; the method must specify when it qualifies for admission or quotation. This additional observation cadence is a trial choice, separate from the confirmed weekly-price/monthly-research cadence.

If funded claims are selected, a **separate fictional clearing trust** holds participant collateral and follows the prospectus's settlement rule. The house does not spend that collateral or trade against its own valuation. Defining the settlement publisher, eligible release vintage, correction deadline, and unavailable-data procedure remains a gate before any contract series can operate. The finite budgets and escrow are fictional resources; the user is never asked to provide money.

## 4. What is listed and what one unit means

The listed object is a **specified practice in a specified population and observation convention**, not an emotion, every physical object associated with it, or ownership of practitioners. `LETTER` is the continuing coverage identifier. Its specification excludes unsent drafts and machine-produced letters and counts a qualifying personal handwritten physical message when released to a particular addressee; [[letter-practice-dynamics]] owns the detailed boundary.

Three genuinely different meanings remain open:

| Branch | One unit and quote | Consequence |
|---|---|---|
| U1 — Published assessment | There is no issued share. One quotation refers to the cohort's next 52 weeks of LETTER practice; the level is normalized to 100 at the reference date. One point is one hundredth of that initial assessment, not a letter or a credit. The assessment functional must be chosen before numerical publication. | Fits a research-only rehearsal. No asset float, funded SHORT, squeeze, or realizable arbitrage exists. Recorded opinion breadth can exist, but cannot be called short interest. |
| U2 — Funded forecast claim | One dated claim pays `100 × min(L_T / K, 1)` fictional credits after a fixed 52-week period, where `L_T` is the prospectus-defined qualifying-send total and `K` is a frozen threshold. The weekly price is credits paid for that contingent payout. | Recommended if actual in-world positioning and counterparties are important. Each paired LONG and complementary claim is fully funded by 100 credits. The price expresses a forecast of a specified outcome; it does not exhaust the letter's human value. |
| U3 — Conserved support entitlement | One dated certificate entitles its holder to one person-hour in a defined writing facility, materials, and one dispatch within the stated service period. The quote is credits per entitlement. | Gives holding and redemption physical consequences. It prices enabling capacity, not directly practice survival, and introduces resource allocation and a market-to-practice feedback that must be designed separately. |

[[Q-004-unit-of-account]] defines quote, payout, resources, counterparties, indices, positioning, arbitrage limits, and artistic costs for every branch. No branch is implemented. In U2 an illustrative `K = 10,000 sends` makes 4,000 eligible annual sends settle at 40 credits per claim; 12,000 sends settle at 100, not 120. **That threshold fails against the companion LETTER fixture:** its initial flow is about 416 sends/week, or 21,632 sends over 52 unchanged weeks, so 10,000 would be reached around week 25. Once reached, later disappearance cannot reduce this cumulative claim's payout. A higher trial threshold such as 40,000 postpones saturation but does not remove the design cost; no threshold is selected. Counting cumulative letters also rewards intensity concentrated among a few writers; mean active practitioners or qualifying practitioner-weeks would answer a different question and need a different prospectus. A dated contract's tendency toward a realized payout must not be mistaken for the long-run trend of a continuing practice index; repeated issuance needs a declared roll rule.

The original proposed “Fundamental Value” and “Market Price” can remain separate under all branches, but cannot retain the same meaning without qualification. U1 needs a declared appraisal functional; U2's fundamental is the house's expected contractual payout, while disagreement over human worth also appears in the research; U3's fundamental estimates a support entitlement's value. The name alone must not hide this choice. [[Q-001-price-formation]] and [[pricing-model]] own the next valuation and price rules.

## 5. Who knows and does what

| Actor | Information available | Actions and finite constraints |
|---|---|---|
| Practising person | Their own time, effort, contacts, deliveries, habits, and local news; incomplete knowledge of everyone else | Begin, continue, pause, stop, resume, reply, choose another medium; limited time, energy, contact access, and infrastructure. No duty to write because somebody bought LETTER. |
| Research institution | Submitted observations and reports with missingness and delay; its own declared model | Publish estimates, methods, eligibility and coverage notices; cannot decree universal extinction or compel behavior. |
| Analyst | Common public releases plus any separately specified, timestamped research channel; no omniscient latent state | Publish and revise a dated thesis, forecast, horizon, and conviction; credibility is earned through matured outcomes. A twelve-month forecast remains pending for twelve months. |
| Fictional market participant | Public information and, only if specified later, uneven private signals; other participants' public quotes or positions | In U1: publish a view under a finite research-attention budget. In U2: commit finite credits, hold, transfer, or close matched claims. In U3: acquire, transfer, redeem, or allow entitlements to expire. Exact participant counts and budget distribution remain unselected. |
| Audience member | Published records and their saved stance; no hidden world state | Read, compare, record LONG/HOLD/SHORT, revise a stance, and revisit its original evidence. No money, order entry, control over the cohort, or automatic price channel. |

Analyst forecasts may inform the monthly anchor as already directed, but settlement observations must remain separate from their forecast. Under U2 the next-stage mechanism must explain how finite participants respond to that anchor and arrive at a weekly quote. “Price converges to value” alone does not supply a buyer, seller, budget, or information event. The U2 rehearsal keeps market actors separate from the practitioner cohort and gives them no channel to commission, finance, or direct qualifying dispatches; allowing those roles to overlap would add an incentive or manipulation loop that needs its own design. This separation is a trial boundary, not a conclusion that financial incentives can never change practice.

## 6. Time and institutional memory

**Trial assumption W3:** the world uses UTC+9. Practice weeks run Monday 00:00 to the next Monday 00:00. The weekly close is Monday 17:00, using reports received by Monday 12:00 and clearly identifying the latest completed practice week. Formal research appears at 14:00 on the first Monday of each calendar month, before that close, with an explicit observation cutoff. This supplies one concrete clock without treating an earlier Friday example as a confirmed weekday. Publication days and starting date remain selectable.

The monthly report may describe an older observation period because source collection is delayed; weekly price changes use the information actually available, not the already-known-to-the-author full history. Events, dispatch weeks, observation windows, report releases, and claim maturities therefore have separate dates. Under U2 a generic new twelve-month price target soon falls after an existing 52-week claim matures. Reports must instead identify a maturity-compatible horizon or explicitly target a later vintage/constant-maturity series, and scoring must use that same object. This is a next-stage change to the existing analyst-target convention, not a completed performance record.

Every released artifact retains: the practice and population definition version, relevant period, information cutoff, publication time, source class, and release identifier. Corrections link old and new releases with a reason. This is a design requirement for the visible archive, not permission to mutate repository raw sources.

**Audience record fixture:** a browser-local record stores security, stance, timestamp, quote identifier, and the research releases available when recorded. A new stance appends a change rather than erasing the original. The return visit can show `LONG recorded 6 weeks ago`, the original and latest quote, intervening research, and a later correction. A stance without a target and horizon is a value position; its price movement can be shown but is not labeled forecast accuracy.

Browser-local persistence is sufficient for a first rehearsal and does not imply cross-device recovery. A real audience percentage requires a later shared record service with a defined unique-participant and revision-counting rule; until then there is no invented global total. Public traces or free-text testimony are a separate choice from storing a private stance. Neither individual nor aggregate stances change practice, institutional estimates, or price in this trial. Practice feedback in [[letter-practice-dynamics]] is a separate causal design.

## 7. Disappearance and return

Keep four independent statuses: **underlying practice state**, **observation availability**, **research coverage**, and **quotation/listing**. The detailed proposed rules are in [[Q-002-listing-lifecycle]]. A zero observed count is not proof of extinction; an interrupted practitioner is not erased; ended analyst coverage is not delisting; and a missing price is not a zero price.

A first return after operational absence creates a practice event. It does not automatically create a new contract, a revived index constituent, or a completed recovery. The same coverage identifier retains the old reports and new evidence. Dated contracts, if selected, have their own identifiers and mature independently of the continuing practice page.

## 8. Provisional delivery and encounter

**Trial assumption W4:** a browser publication designed first for a laptop reading session, with a readable narrow layout for return visits. Home shows the latest dated index/quote, coverage status, movers, and research. A visitor opens LETTER, sees behavior beside attention and discourse, reads opposed research, and records a stance with `Position recorded.` The interface remains in the ordinary institutional register. This is a medium for testing, not a committed platform or exhibition format.

At the next visit, the visitor's previous position, the original report, the new weekly quote, and any correction are still available. An ended-coverage page retains its last dated estimate and archive rather than manufacturing a live close. A paper or linked-document rehearsal can test this sequence before a website is built; a persistent audience record requires an interactive medium for the full return-visit test.

## Choices needed before the information and price stage

| Choice | Recommendation and reason | What remains possible before selection |
|---|---|---|
| World W1 | Fictional bounded district first; a named city only if geographical specificity matters to the work | Specify and challenge LETTER flows using the trial denominator. |
| Unit U1/U2/U3 | U2 for a full world with funded positions; U1 for a publication-only rehearsal; U3 if allocation of support is itself the subject | Compare state measures, reports, lifecycle, and encounter without fabricating a quote. |
| U2 outcome and settlement, if selected | Start review with 52-week qualifying sends, then compare practitioner breadth; freeze thresholds, release vintage, and failure procedure before quoting | Demonstrate how concentrated output and broad participation diverge; no settlement series yet. |
| Observation scope | Trial sentinel panel plus separately retained underlying history | Develop count/estimate/attention distinctions and information-error cases; no claimed precision. |
| Audience consequence | Persistent private stance and later disclosed aggregate, with no price route in the trial | Review first/return visit and archival behavior. Any vote-to-price rule needs its own decision. |
| Lifecycle windows and medium | Use the working rules and browser encounter below as fixtures | Test exceptions on paper; thresholds and delivery technology remain revisable. |

Next-stage gates are the observation and revision process; choice of a value/contract outcome and its mapping; a finite participant and weekly quotation rule if U2/U3 is selected; forecast scoring; and index roll/membership treatment. These gates do not select a factor set. Completing LETTER tests connected operation, not whether the entire factor architecture is sufficient or identifiable. Factors may outnumber securities.

## Sources

- [[SRC-2026-09-06-world-rules-letter-spec-request]] — [raw/documents/2026-09-06-world-rules-letter-spec-request.md](../../raw/documents/2026-09-06-world-rules-letter-spec-request.md); exact current design request and constraints; new rules here are this task's unconfirmed proposals
- [[SRC-2026-09-06-worldbuilding-roadmap-request]] — [raw/documents/2026-09-06-worldbuilding-roadmap-request.md](../../raw/documents/2026-09-06-worldbuilding-roadmap-request.md); target-depth and roadmap request
- [[SRC-2026-09-04-longing-concept-brainstorm]] — [raw/conversations/2026-09-04-longing-concept-brainstorm.md](../../raw/conversations/2026-09-04-longing-concept-brainstorm.md); research-house and stance encounter; the original no-Buy/Sell and provisional acceptance passages were checked for the distinction between viewer interaction and fictional market actors
- [[SRC-2026-09-05-price-formation-market-model]] — [raw/conversations/2026-09-05-price-formation-market-model.md](../../raw/conversations/2026-09-05-price-formation-market-model.md); cadence and working anchor/price architecture, read through maintained synthesis for this task
- [[SRC-2026-09-06-arbitrage-news-quality-and-next-work-items]] — [raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md](../../raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md); user directions on arbitrage, imperfect reporting, and the unit review, read through maintained synthesis
