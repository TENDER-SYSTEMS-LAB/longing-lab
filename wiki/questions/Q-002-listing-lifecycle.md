---
status: working
attribution: jointly-developed
updated: 2026-09-20
sources:
  - SRC-2026-09-19-market-texture-findings
  - SRC-2026-09-06-world-rules-letter-spec-request
  - SRC-2026-09-04-longing-concept-brainstorm
---

# Q-002 — Who lists a romance, and what happens when it dies?

## Issuance is answered (2026-09-20)

**Who issues: the person who leans.** Not the institute, which cannot — a bearer
instrument has no register. The Committee below lists a practice for quotation; it
does not issue anything. See [[DEC-008-bearer-bond-is-perpetual]].

What was *not* answered here, and stays open below: who observes a resumption and
on what evidence, whether a delisted practice can be re-admitted, and what a zero
quote means. The arithmetic now has a birth mechanism; the administrative rules
around it do not exist.

One thing the answer changes about this page's framing. The instrument is
perpetual, so a practice does not lapse by reaching maturity — it is **called**,
redeemed early by the person who no longer needs it. The question *if one person
begins a vanished practice again, has it still vanished?* acquires a mechanical
counterpart: a new issue against a practice with no outstanding balance.

## The arithmetic now needs an answer (2026-09-19)

This page asked who lists a security and whether one person resuming a vanished
practice relists it. Those were world-building questions. [[loop-simulation]]
turned them into numerical requirements.

The first build implemented BEARER BOND defaults and no issuance, although
[[reserve-instruments]] defines the instrument as *bilateral by construction,
issuable, and defaultable*. Three things followed from the missing half. Float
fell from 10,993 to 79 and never recovered. The learning material that feeds the
loop dried up with it, and the loop stalled. And — the one that matters for this
page — **a practice could never be resumed**, so a melt-up could never relapse
and the market had no way to breathe.

The harness now issues new relationships each week, scaled by how alive the
practice still is. That is an arithmetic placeholder, not an answer: it says a
birth rate must exist, and says nothing about **who issues, on what evidence a
resumption is observed, or whether a delisted practice can be relisted at all**.
Those remain exactly as open as below. What has changed is that they can no
longer be deferred as flavour — without a rule, the market does not function.

The related zero-quote problem is unchanged and also numerical: high-β securities
reach numerical zero with no floor and no delisting rule.

## The question

The market metaphor implies a lifecycle, and the source conversation raised it as a set of questions rather than answering any of them:

- Who lists a security?
- If a romance becomes extremely rare, should its price fall or rise?
- Is a practice nobody performs any more delisted?
- Where does a delisted romance go?
- If one person starts doing it again, is it relisted?

The last one is treated as the strongest of them, because it is the theme's original title restated as a market rule:

> If one person begins a vanished romance again, has it still vanished?

## Why it is not merely mechanical

The scarcity question is the same disagreement the research desk exists to stage. Falling supply meets rising scarcity: [[analyst-system]] has Eleanor Vale reading scarcity as value and Adrian Kessler reading it as decline with no catalyst, and Adrian going LONG on SOLITUDE purely because supply is collapsing. A listing rule that resolves the scarcity question one way would settle by fiat an argument the work is built on leaving open.

Delisting is also where the work's quiet bias is placed. In [[system-grammar]], a page whose coverage ends shows `Coverage Discontinued` and, below it, one small trace left by a past user; the Archive is described as holding a disproportionate number of LONG reports on securities that no longer exist. So the delisting mechanism is not backstage plumbing — it is one of the work's most loaded surfaces.

## Evolution — separate practice, evidence, coverage, and listing (2026-09-06)

**Previous state:** the source raised disappearance and one person's return as questions; no operational rule existed. **Transition:** the current user request explicitly asks to distinguish extinction, stopped observation, ended coverage, delisting, and reappearance. **Current state:** the following rules are `llm-proposed` trial specifications alongside [[world-rules]] and [[letter-practice-dynamics]], not institutional policy selected by the user.

One status cannot carry all these meanings. Keep four separate fields and preserve their effective dates and reasons:

| Domain | States / meaning | What must not be inferred |
|---|---|---|
| Underlying practice | Qualifying events occur; no qualifying events in a specified window; operational absence in the bounded cohort; reappearance | A person not dispatching this week has not necessarily interrupted their ongoing episode. Absence now is not proof that future resumption is impossible. |
| Observation | Current, delayed, incomplete, stopped, restored | Zero sampled letters is not zero cohort letters. No observations is not an observed zero. |
| Analyst coverage | Covered by named desks, coverage under review, no current coverage, coverage resumed | The institution can stop research while practitioners continue and a quotation remains possible. |
| Listing / quotation | Candidate, listed/quoted, quotation suspended, delisted/archived, re-admitted | Delisting ends eligibility for a live quote or new issue under its stated terms. It does not erase the practice, old reports, or outstanding obligations. |

### What extinction can mean in this world

**Operational-absence fixture:** the author-known bounded cohort has `A = 0` ongoing episodes at the boundary and no qualifying sends across the preceding 52 weeks. The window is a proposed convention, not an empirical discovery or an irreversible absorbing state. Members of `U` (never begun) and `D` (previously begun/interrupted) remain capable of starting or resuming under the same rules. One dispatch after that boundary disproves continuing absence and creates a reappearance event. It does not by itself establish sustained recovery.

This criterion applies to a finite-person realization or a separately authored absence history, not to rounded expected stocks/flows from the aggregate LETTER equations. Positive expected counts may approach zero without reaching it; an individual realization method remains unselected.

The visible institution cannot read that author-known fact. With the proposed sentinel panel it may publish `No qualifying sends observed in the reporting panel; cohort absence not established`, including response coverage and the time window. A public claim of cohort-wide operational absence requires evidence covering that denominator under an adopted standard. Until such evidence exists, it must not say `EXTINCT` merely because its model estimate rounds to zero. There is no claim of worldwide or permanent extinction from this bounded example.

This supplies distinct answers to the artistic and administrative questions. A practice may cease in the world; the institution may fail to know. The institution may withdraw while the practice persists. A practice may return before its coverage or quotation does. The ordinary research record can expose all three gaps.

### Proposed eligibility and authority

The Methodology and Listings Committee lists a **defined practice/population/method combination**. The initial checklist is a specific inclusion boundary, a non-duplicative coverage purpose, defined state and units, an observation route with declared limitations, a quote meaning, and an archive identifier. It must show which proposed conditions this practice exposes; the listed universe constrains meaningful factors, and there is no factor-to-security ratio cap.

Initial trial admission requires four completed weekly observation releases or a clearly labeled modeled initiating sample of that length. Four weeks test publication completeness, not statistical adequacy, persistence, popularity, or historical prevalence. Rare practices are eligible; a minimum market size or a minimum number of human practitioners is not imposed. If U2/U3 is selected, a valid prospectus, funded obligations, and settlement/redemption procedure are additional gates. A modeled observation sample alone cannot satisfy those financial/service gates.

### Proposed transitions and records

The following periods are deliberate reviewable fixtures, not confirmed thresholds. Administrative reasons are recorded separately from behavioral reasons.

| Trigger | Proposed action | What the audience can still retrieve |
|---|---|---|
| A source misses its scheduled release | Mark observation `DELAYED`; retain the last release with its original as-of date | Prior estimate, missing-release notice, coverage counts. Do not print zero or a freshly dated old count. |
| Two consecutive monthly releases lack an eligible observation source | Mark observation `STOPPED`; require a notice explaining which estimates can still be supported | Last estimate, missingness history, and current quotation status independently. Two misses do not declare extinction. |
| Last analyst ceases current research | Mark `NO CURRENT COVERAGE` at that date; record reason and outstanding forecast horizons | All earlier reports, their matured or pending scores, other source releases, and any separately valid quote. |
| The chosen quote rule cannot produce an eligible weekly close | Mark `QUOTATION SUSPENDED` for that close; explain unavailable input, missing executable counterparty, or methodology failure | Last valid close labeled with date; suspension duration; estimate if still available. A missing close has no invented weekly return. |
| Definition invalidated or duplicate listing found; alternatively quotation remains suspended for 13 weeks with no approved restoration plan | Committee reviews delisting and publishes a reasoned effective date | Permanent archive entry, old definitions, notices, quotes, positions, and any surviving obligations. Low practice volume alone is not this trigger. |
| Qualifying behavior reappears after defined absence | Record `PRACTICE REAPPEARED` with event date and evidence status; update source/estimate when legitimately available | Absence window, initial report, later corroboration, and pre-existing historical identifier. |
| A delisted practice again meets admission conditions, with four valid weekly releases | Committee can re-admit under the same coverage identifier and a new listing episode | The gap remains visible; a new price base/continuity notice is required. A single returning writer is evidence toward revival, not automatic administrative relisting. |

An observation gap does not mechanically imply quote suspension: U1 might still publish a visibly stale-evidence assessment under a declared policy; U2 participants might quote a still-valid claim with increased settlement uncertainty. The selected price rule must state when the available evidence is inadequate. No standing permission to manufacture a fresh quote follows from this exception.

If the committee changes the definition so that the new object is substantively different, create a new practice identifier linked as a successor rather than hiding the break inside the old series. A normal return under the same definition keeps the original identifier. A population or denominator change is also a methodology event, not a silently extended chart.

### What delisting does to a held claim

Under U1, there is no monetary claim to cancel. A visitor's stance and the last valid quote persist, and an unavailable current quote is not a total loss calculation.

Under U2, the continuing `LETTER` page and each dated claim are different objects. Ending new listing or research coverage does not confiscate escrow, cancel a holder's contingent payout, change its cap, or declare a settlement of zero. Existing claims retain their prospectus terms and settlement record, even if secondary quotes cease. Ordinary maturity is not practice extinction or delisting: the claim settles and expires while the coverage page may issue a new vintage. Unavailable observations must follow a predeclared settlement-failure procedure; choosing that procedure remains a gate in [[Q-004-unit-of-account]].

Under U3, stopping quotation does not erase committed service capacity or an entitlement's redemption/refund terms. Service expiry, failed service provision, ended coverage, and practice cessation are distinct events.

### Scarcity, indices, and the archive

Lifecycle policy must not settle the research argument that scarcity is or is not valuable. A rare practice can have a low future-output claim price under U2, a high service-entitlement price under U3, or contested assessment under U1. Falling participant count and rising price can coexist only through the chosen valuation/contract rules; the committee does not mandate that combination.

Publish effective index membership changes separately from behavioral returns. The main index cannot silently discard a suspended or delisted constituent and present the surviving set as the same historical population. A frozen-cohort companion should preserve the original member list, removal reasons, and coverage loss. Whether it carries the last valid price, displays unavailable levels, or uses a contractual terminal payout is a methodology choice tied to the selected unit; **do not automatically assign zero to an unobserved or delisted practice**. A divisor adjustment may preserve arithmetic continuity but cannot by itself explain the changed meaning of membership.

The archive retains discontinued LONG and SHORT research without rewriting their chronology. The earlier proposed trace from a past audience member is still an experience option, not authority to publish private text. A private stance can persist locally under [[world-rules]]; a public trace requires a separately specified contribution mechanism.

### Example with independently changing states

1. A panel stops reporting in month 2. The last observed LETTER count is retained as old; no claim of disappearance follows.
2. The final analyst leaves coverage in month 3. The practice page now says `NO CURRENT COVERAGE`; a funded dated claim may still have a valid quote and obligation.
3. Later the chosen quote rule cannot produce closes. Suspension begins; after the proposed review window the committee ends live listing. The archive and any outstanding claim terms survive.
4. A resident who had stopped sends a qualifying letter. The underlying state records a restart and one dispatch. A source may report it late or fail to see it; the institution changes its record only when evidence arrives.
5. Four valid releases and a valid quote/prospectus route support re-admission. One person's act preceded administrative return and remains visible in the dated record. This is a return of evidence and eligibility, not an assertion that the practice has recovered to its former scale.

## Related

- [[world-rules]]
- [[letter-practice-dynamics]]
- [[Q-004-unit-of-account]]
- [[Q-001-price-formation]]
- [[analyst-system]]
- [[system-grammar]]
- [[index-architecture]]

## Sources

- [[SRC-2026-09-06-world-rules-letter-spec-request]] — [raw/documents/2026-09-06-world-rules-letter-spec-request.md](../../raw/documents/2026-09-06-world-rules-letter-spec-request.md); exact request for concrete lifecycle distinctions; thresholds and authority rules above are unconfirmed task proposals
- [[SRC-2026-09-04-longing-concept-brainstorm]] — [raw/conversations/2026-09-04-longing-concept-brainstorm.md](../../raw/conversations/2026-09-04-longing-concept-brainstorm.md)
