---
status: working
attribution: jointly-developed
updated: 2026-10-10
sources:
  - SRC-2026-10-10-security-weights-decisions
  - SRC-2026-10-10-fund-construction-decisions
  - SRC-2026-10-10-security-legs-and-tickers
  - SRC-2026-10-10-security-families-decisions
  - SRC-2026-10-10-security-universe-round-decisions-5-to-7
  - SRC-2026-10-10-security-universe-round-decisions
  - SRC-2026-10-05-ontology-draft-decisions
  - SRC-2026-10-05-security-universe-method
---

# Security Families — fifty candidates merged into seventeen

The analysis the author asked for on 2026-10-10 ([[SRC-2026-10-10-security-universe-round-decisions-5-to-7]]): analyse the candidates' ontology, abstract them further, merge them, and give the securities simple, ticker-ready names. The input is the thirty candidates on [[security-universe]] as decided earlier that day, plus the twenty added provisionally. The five held candidates are mapped but not counted.

**Status.** The sections after the author's decisions were the assistant's proposal, `llm-proposed`. The author decided on them the same day (next section).

## The author's decisions (2026-10-10)

From the assistant's decision page and follow-up questions ([[SRC-2026-10-10-security-families-decisions]]), `user-confirmed`; the options were the assistant's:

| # | Question | Decision |
|---|---|---|
| 1 | Axis | **Accepted:** practices are grouped by what one person leans on the other for. |
| 2 | Mirror pairs | **Not merged:** decision 3 of 2026-10-10 stands. How the two sides live inside a family is open — see the long/short idea below. |
| 3 | Families | **All seventeen accepted.** KEY is renamed **ENTRUST · 맡김**, so that it differs clearly from IOU: IOU is something owed and paid back later; ENTRUST is something held for another without proof and kept or returned, with nothing paid back. IOU is shown with "(I Owe You)" beside it, `user-originated`. The author asked how PLAY differs from GATHER; the assistant's answer: GATHER is leaning for a place among people, PLAY for someone to do something with for its own sake. |
| 4 | State names | **WAIT** (기다림), **SERENDIPITY** (우연한 만남) and **THINK** (사유), `user-originated`. |
| 5 | Naming | **Ticker + one English word in capitals + Korean name**, `user-originated`. Tickers are four letters by default; three are allowed. |

**The author's idea for the mirror pairs, `user-originated`, not adopted:** borrow long and short positions from futures markets, and the ETFs built from them, since a long and a short exist only together. The assistant's analysis and the codes are proposed below.

## The long/short idea — the assistant's analysis

`llm-proposed`.

**What fits.** In a futures market every long has a matching short; open interest counts contracts that have both. A BEARER BOND is the same: every issue has one who leans and one who is leaned on, and neither side exists alone ([[DEC-008-bearer-bond-is-perpetual]]).

**What does not fit.** A long and a short gain from opposite price moves. The two sides of a bond rise and fall together: more confiding means more listening, and the round found that mirror pairs move together ([[security-universe-round-review]]). Borrowed literally, the listening price would fall whenever confiding rose, which says the wrong thing about the world.

**Only three pairs are two sides of one bond.** 13/14 (learning / teaching), 3/19 (confiding / listening) and 12/27 (asking a favour / helping) are the leaning side and the giving side. 6/26 (a chosen gift / a made gift) and 23/24 (treating / lending) are two forms of the same giving side; the long/short idea does not apply to them.

**A borrowing that fits, proposed:** the two sides are listed as two **legs** of one contract, issued together; the family is a fund holding both legs, the same form as the state-securities; and the futures market's long/short ratio becomes a **lean/give ratio**, an indicator for analysts like the hostility indicator. When many lean and few give — many confide, few listen — the gap is where BLIND TRUST enters.

## Ticker codes — proposed, accepted 2026-10-10 with DEC and ETRS

`llm-proposed`. Four letters by default, three where the word is short. A leg never shares its family's code. `SRD` is avoided because [[index-architecture]] already uses it for the Serendipity Index.

| Ticker | Name | Korean | Legs or forms (decision 3) |
|---|---|---|---|
| STRG | STRANGER | 낯선이 | |
| INTR | INTRO | 소개 | |
| WRIT | WRITE | 글 | |
| RECH | REACH | 안부 | |
| CNFD | CONFIDE | 털어놓기 | legs: TELL confiding / LSTN listening |
| MEND | MEND | 화해 | |
| DEC | DECIDE | 결정 | |
| GIFT | GIFT | 선물 | forms: CHSE choosing / MAKE making |
| TCH | TEACH | 가르침 | legs: LERN learning / TCHR teaching |
| CARE | CARE | 돌봄 | |
| VGIL | VIGIL | 곁 | |
| VIST | VISIT | 방문 | |
| GTHR | GATHER | 모임 | |
| PLAY | PLAY | 놀이 | |
| FAVR | FAVOR | 품앗이 | legs: ASK asking / HELP helping |
| IOU | IOU (I Owe You) | 외상 | forms: TRET treating / LEND lending |
| ETRS | ENTRUST | 맡김 | |
| WAIT | WAIT | 기다림 | state |
| SRDP | SERENDIPITY | 우연한 만남 | state |
| THNK | THINK | 사유 | state |

Open for the author: whether the legs fit the long/short idea; whether 6/26 and 23/24, which are forms rather than sides, stay two securities; and the codes.

## The author's decisions on legs and tickers (2026-10-10, later)

From a second decision page ([[SRC-2026-10-10-security-legs-and-tickers]]), `user-confirmed`; the options were the assistant's:

| # | Question | Decision |
|---|---|---|
| 1 | The long/short idea for the three true pairs | **Two legs, a family fund and a lean/give ratio.** The leaning side and the giving side are two legs of one contract, issued together and listed apart: TELL / LSTN, LERN / TCHR, ASK / HELP. The family is a fund holding both legs, the same form as the state-securities. The futures market's long/short ratio is borrowed as a lean/give ratio, an indicator for analysts; the legs are not priced as opposites. |
| 2 | GIFT and IOU, two forms of one side | **Listed apart**, decision 3 kept: CHSE / MAKE and TRET / LEND. They are forms, not legs, and carry no ratio. |
| 3 | Ticker codes | **Accepted, with two changes by the author, `user-originated`:** DECIDE is **DEC**, ENTRUST is **ETRS**. |

The securities are now seventeen family funds and three states, with ten listed legs and forms beneath five families. Whether a family without legs is a fund of one security or a security of its own is not yet stated; the assistant reads it as a security of its own.

## Fund construction — proposed, decided 2026-10-10

`llm-proposed`, after the decisions above. Two rules already decided bound it: the headline index is equal-weighted so that prevalence does not enter both the fundamental and the weight, and float is outstanding BEARER BONDs, estimated and tagged `MODELED` ([[current-state]], Confirmed). The market's positioning already has real longs and shorts ([[loop-simulation]]), so the legs are named by act, never L and S.

**What a leg measures.** A bond forms only where a leaning act meets a giving person. If the legs counted bonds, both legs of a pair would count the same bonds and always be equal. The assistant therefore proposes: the leaning leg (TELL, LERN, ASK) counts **acts of leaning**, whoever answers; the giving leg (LSTN, TCHR, HELP) counts **giving by people**. Where AI answers, leaning goes on while human giving falls; the difference is reliance that formed no bond, the side of the ledger where BLIND TRUST grows.

| # | Question | Options | Assistant's recommendation |
|---|---|---|---|
| 1 | Leg weights in a family fund | equal; follow the smaller leg (only what met); decide later | **Equal**, as the headline index is |
| 2 | Lean/give ratio | leaning acts ÷ human giving acts; price of one leg ÷ the other; bonds issued ÷ leaning acts | **Leaning acts ÷ human giving acts.** Above 1, leaning is unmet by people |
| 3 | When the ratio is published | weekly beside prices; monthly in research | **Monthly in research**, as an analyst indicator like hostility |
| 4 | Families without legs | a security of its own; a fund of one | **A security of its own** |
| 5 | How a state's carrier fund and its own measure combine | fixed split; the measure multiplies the carrier fund; the measure alone moves and carriers set the level | **The measure multiplies the carrier fund.** If waiting vanishes while people still write, the price falls — the risk the round found |
| 6 | Carrier weights in a state fund | equal; by how strongly each carrier makes the state | **Equal** |

These were proposals; the author decided them the same day.

**The author's decisions (2026-10-10)** ([[SRC-2026-10-10-fund-construction-decisions]]), `user-confirmed`; the options were the assistant's:

| # | Decision |
|---|---|
| 1 | **A family fund follows its smaller leg** — only what met. Leaning that no person answers does not raise the fund. Against the assistant's recommendation of equal weights. |
| 2 | **Lean/give ratio = leaning acts ÷ giving acts by people.** Above 1, leaning is unmet by people. |
| 3 | **Published monthly in research**, as an indicator for analysts. |
| 4 | **A family without legs is a security of its own.** "Fund" is used only for a family with legs or forms. |
| 5 | **A state's own measure multiplies its carrier fund**, so a state that vanishes while its carriers hold takes the price down. |
| 6 | **Carriers are equally weighted** in a state fund. |

The assistant's reading, `llm-proposed`: with decision 1 the fund moves with the bonds that actually formed, and the unmet part shows only in the ratio — the fund and the ratio together say what was met and what was not. Whether GIFT and IOU, which have forms rather than legs, follow the smaller form or are equally weighted was decided later the same day: **equally weighted** ([[SRC-2026-10-10-security-weights-decisions]]).

## The axis of abstraction

In [[romance-ontology]], every practice is an **issue**: the one who leans issues a BEARER BOND to the one leaned on, and attention is the principal ([[DEC-008-bearer-bond-is-perpetual]]). The assistant therefore groups practices by **what one person leans on the other for**. Medium, body, place, which side one stands on, and the occasion are attributes of a family, not separate securities — the same move the author made when practices were defined by act.

This axis has one consequence: the two sides of one exchange fall into one family, because they are the two ends of one bond. That merges every mirror pair, which the author kept on both sides on 2026-10-10 ([[SRC-2026-10-10-security-universe-round-decisions]], decision 3). The author's instruction to merge may reopen that decision; this page proposes it and leaves it to the author.

## The seventeen families

Members use the numbers on [[security-universe]] (1–30) and N1–N20 for the twenty added, in the order of [[security-universe-round-review]] section 2. A member marked † is the assistant's least certain placement.

| Name | Korean | Leaning for | Members | Balance | Main channel |
|---|---|---|---|---|---|
| STRANGER | 낯선이 | Help or a word from someone one does not know | 1 way, 22 words in passing, 28 asking people one does not know | belief | − navigation, self-service, AI answers |
| INTRO | 소개 | Being put in touch with a person or a thing by someone who knows both | 2 recommendation, 11 introducing two people | belief, trust | − recommendation and matching |
| WRITE | 글 | Being addressed in words someone stands behind | 4 writing in one's own words | love, understanding | + post, email, messaging; − AI drafting |
| REACH | 안부 | Being thought of across distance | 7 remembering someone's day, 8 reaching out for no reason, 29 friendship at a distance, N18 sending money home† | love, belief | + telephone, mobile, video, remittance; − reminders |
| CONFIDE | 털어놓기 | Being heard | 3 confiding, 19 listening, 10 talking until late†, N20 talking about what is no longer done† | understanding | − AI counsel and companions → BLIND TRUST |
| MEND | 화해 | Repair after harm | 5 apologising, 15 talking a disagreement through, N5 forgiving or reconciling | understanding, trust | − drafted apologies, mediation, feeds |
| DECIDE | 결정 | A judgment made together | 16 deciding together | understanding, belief | − optimisers, AI: substitution of judgment |
| GIFT | 선물 | Something chosen or made for one particular person | 6 choosing a gift, 26 making something for someone, N15 commissioning from its maker† | love | − recommendation, generated content, mass production |
| TEACH | 가르침 | A skill or a memory passed on | 13 learning a craft, 14 teaching by showing, N16 studying together, 20 passing down a family story† | understanding, trust | − tutorials, AI tutors, archives |
| CARE | 돌봄 | Being looked after in need | 18 caring for someone ill, 21 reading aloud, N13 checking on someone alone, N14 restoring conversation | love, belief | − AI care, sensors → BLIND TRUST; + restoration |
| VIGIL | 곁 | Presence when nothing can be fixed | N1 sitting with the grieving, N9 keeping vigil with the dying | love, understanding | − AI companions, monitoring |
| VISIT | 방문 | Bodily company | 9 visiting, 25 sharing a meal arranged together†, N12 walking someone home | love, belief | + transport; − video calls, delivery, ride-hailing |
| GATHER | 모임 | A place among others | 30 joining a gathering, N3 praying with someone | belief | + social web; − personalised feeds |
| PLAY | 놀이 | Doing something for its own sake together | N2 making music, N4 playing a game | belief, trust | + online play and collaboration; − recorded music, AI opponents |
| FAVOR | 품앗이 | Labour or time lent | 12 a neighbour's small favour, 27 helping move, N6 covering for a colleague, N10 minding each other's children, N17 working a neighbour's field in turn | trust, belief | − on-demand services, paid platforms, mechanisation |
| IOU (I Owe You) | 외상 | An account left open | 23 "next time it's on me", 24 lending informally | trust | − split payment, credit services |
| KEY → ENTRUST | 열쇠 → 맡김 | Being trusted with something without proof | 17 meeting on one's word, N7 leaving a key, N8 vouching with one's name†, N11 letting a child go out alone, N19 keeping a secret | trust | − tracking, cameras, smart locks, credit scores |

Fifty candidates, seventeen families: two families have a single member (WRITE, DECIDE). WRITE is kept apart because it carries the origin rule and AI drafting most directly, and is where LETTER now lives as a form. DECIDE is kept apart because it is the clearest case of substitution of judgment ([[DEC-014-restoration-is-arrival-and-substitution-is-judgment]]).

**Held candidates, if released:** bargaining → STRANGER; hosting a traveller → VISIT; interpreting or practising a language → TEACH or CARE; asking someone out or saying "I love you" first → WRITE or a new family; finding others with the same rare condition → GATHER.

## State-securities and their carriers

Decided on 2026-10-10: a state is priced by a fund of its carrying practices plus a measure of the state itself. With families, the carriers become families.

| State | Proposed name | Carriers | Measure of the state |
|---|---|---|---|
| Waiting | WAIT (기다림) | WRITE, REACH, KEY | reply latency |
| Serendipity | CHANCE (우연) | STRANGER, INTRO, GATHER | share of first meetings not arranged by a system |
| Reflection (사유) | open | WRITE, MEND, GIFT, DECIDE | open |

## Coverage check against the three rules

- **Every balance is fed.** Love (6): WRITE, REACH, GIFT, CARE, VIGIL, VISIT. Understanding (6): WRITE, CONFIDE, MEND, DECIDE, TEACH, VIGIL. Trust (7): INTRO, MEND, TEACH, PLAY, FAVOR, IOU, KEY. Belief (9): STRANGER, INTRO, REACH, DECIDE, CARE, VISIT, GATHER, PLAY, FAVOR.
- **Every channel is present.** Device: STRANGER, KEY, FAVOR, REACH. Substitution of judgment: WRITE, CONFIDE, DECIDE, INTRO, MEND. Restoration: CARE, REACH. Arrival: WRITE, REACH, GATHER, PLAY, VISIT. The non-technological channel added on 2026-10-10 most plausibly reaches CARE and VIGIL (longer lives), FAVOR (smaller families, shorter hours) and REACH (love marriage) — the assistant's reading.
- **Not only declining practices.** Risers: REACH, WRITE, GATHER, PLAY. Trust still has few risers (PLAY, and REACH through remittance); the round's warning that trust is fed mostly by declining practices is reduced, not removed.

## Naming

The proposal follows the names the work already uses — LETTER, BLIND TRUST — rather than short codes: one English word in capitals, shown as the ticker, with a Korean label beside it. A name is an act or its object, never a balance (LOVE, TRUST) or an emotion, which keeps the rejected `LOVE ▲2.4%` out ([[prior-art]]). The security-code scheme remains open ([[index-architecture]]); the naming round's rule that every purely alphabetic three- or four-letter code should be assumed occupied ([[institution-naming-review]]) bears on any short code, not on the display name.

## Questions for the author — answered 2026-10-10

1. **Axis.** Group by what one leans on the other for?
2. **Mirror pairs.** Merge both sides into one family, reopening decision 3 of 2026-10-10?
3. **Families.** Accept, split or rename each of the seventeen, especially the members marked †.
4. **Naming rule.** One English word in capitals with a Korean label, never a balance or an emotion?
5. **State names.** WAIT, CHANCE, and a name for reflection.

## Related

- [[security-definitions]]
- [[loop-simulation]]
- [[security-universe]]
- [[security-universe-round-review]]
- [[romance-ontology]]
- [[DEC-016-securities-chosen-top-down]]
- [[reflection]]
- [[index-architecture]]
- [[current-state]]

## Sources

- [[SRC-2026-10-10-security-weights-decisions]] — [raw/conversations/2026-10-10-security-weights-decisions.md](../../raw/conversations/2026-10-10-security-weights-decisions.md); GIFT and IOU forms equally weighted; TRET's Korean name reopened
- [[SRC-2026-10-10-fund-construction-decisions]] — [raw/conversations/2026-10-10-fund-construction-decisions.md](../../raw/conversations/2026-10-10-fund-construction-decisions.md); fund construction decided
- [[SRC-2026-10-10-security-legs-and-tickers]] — [raw/conversations/2026-10-10-security-legs-and-tickers.md](../../raw/conversations/2026-10-10-security-legs-and-tickers.md); legs, family funds, the lean/give ratio, ticker codes
- [[SRC-2026-10-10-security-families-decisions]] — [raw/conversations/2026-10-10-security-families-decisions.md](../../raw/conversations/2026-10-10-security-families-decisions.md); the families accepted, names and tickers, the long/short idea
- [[SRC-2026-10-10-security-universe-round-decisions-5-to-7]] — [raw/conversations/2026-10-10-security-universe-round-decisions-5-to-7.md](../../raw/conversations/2026-10-10-security-universe-round-decisions-5-to-7.md); the twenty provisional candidates and the instruction to abstract, merge and name
- [[SRC-2026-10-10-security-universe-round-decisions]] — [raw/conversations/2026-10-10-security-universe-round-decisions.md](../../raw/conversations/2026-10-10-security-universe-round-decisions.md); recasts; mirror pairs and 29 kept
- [[SRC-2026-10-05-ontology-draft-decisions]] — [raw/conversations/2026-10-05-ontology-draft-decisions.md](../../raw/conversations/2026-10-05-ontology-draft-decisions.md); securities are practices
- [[SRC-2026-10-05-security-universe-method]] — [raw/conversations/2026-10-05-security-universe-method.md](../../raw/conversations/2026-10-05-security-universe-method.md); selection tests, coverage rules, definition by act, the author's naming condition
