---
status: confirmed
attribution: user-confirmed
updated: 2026-09-20
sources:
  - SRC-2026-09-20-bearer-bond-issuance
  - SRC-2026-09-15-reserve-absorption-and-trust-instruments
---

# DEC-008 — A BEARER BOND is perpetual, and what it measures is attention

## The decision

[[loop-simulation]] made [[Q-002-listing-lifecycle]] urgent: the first build gave
BEARER BOND defaults and no issuance, so float could only fall and a practice
could never be resumed. Asked who issues one, the user rejected every framing on
offer — all of which treated the debt as a discrete obligation, a reply owed —
and supplied a different one:

> 답장을 채무로 보기보다, 한사람이 다른 한사람에게 얼마나 많은 관심을 주는지를
> 채무로 보는게 맞을 것 같다. 요즘 세상이 점점 개인주의화 되면서 점점 남과 관계를
> 맺기보다 스스로 책임지고 스스로 해내는 일이 많아지는 것 같다. 누군가를 믿을 수도
> 있고, 누군가와 같이 무언가를 할 수도 있는것을 나는 이 세계관에서는 서로가 서로에게
> 채권자와 채무자의 관계가 된다고 생각한다.

Three things follow, and each replaces something the assistant had proposed.

**The principal is attention, not an obligation.** What is outstanding between two
people is the amount of reliance one has placed in the other — a quantity, not a
count of unanswered letters. Float is therefore a **balance**, not a number of
relationships. The unit in [[DEC-007-standard-return-numeraire]] changes from
count to amount; the definition of float as outstanding BEARER BONDs is unchanged.

**It runs in both directions, and the two are kept gross.** Each person is
creditor and debtor to the other at once, in amounts that need not match. The
user chose to keep both directions outstanding rather than net them, so float
measures **how much reliance is alive in the world** rather than how lopsided it
is. A mutually deep relationship contributes two large balances; a thin one
contributes two small ones. Netting was rejected because a balanced relationship
would vanish from the ledger, and the ledger would then show individualisation
only when it arrived unevenly.

**Direction of credit.** The one who leans is the debtor and therefore the
**issuer**; the one leaned on has given value now and is the holder. No
institution issues anything: a bearer instrument has no register, and
[[reserve-instruments]] already puts this one beyond any custodian's observation.
The Methodology and Listings Committee in [[Q-002-listing-lifecycle]] lists a
practice for quotation; it does not and cannot issue a bond.

This is consistent with what was already written. *Silence is default* holds: a
person who received another's attention is the debtor, and their silence is their
own default.

## The instrument is perpetual

Asked to confirm a maturity structure, the user rejected it:

> 사람들은 다른 사람과 관계를 맺을 때 영원을 기원하듯이 관계를 맺는다. 즉, 시람과는
> 언제까지만 관계를 맺어야 겠다는 생각은 안한다. 다만, 편지나 문자에 대한 답장 등은
> 심리적인 기한이 있을 수 있다.

So a relationship has no maturity. A reply does. The instrument that matches is
the **perpetual** — a consol, with no maturity, principal never repaid, and only
a coupon running forever. Nothing about a relationship comes due.

The coupon is where the deadline lives. Many real perpetuals carry a **deferrable**
coupon: the issuer may skip a payment without triggering default, and the holder's
forbearance is what makes that survivable. [[reserve-instruments]] had already
written the same sentence — *a late reply is a maturity extension, and it requires
understanding to grant.*

**Deleted by this decision:** per-practice maturity terms, a roll rate, a maturing
principal, and the maturity-wall mechanism built on them. All were assistant
proposals of the preceding turn and none survives a perpetual.

## Three ways a balance leaves

| Path | What happens | What the world reads |
|---|---|---|
| **Coupon** | it is returned — a reply, presence, reciprocation | the relationship is alive |
| **Call** | the issuer redeems early: *I can do this alone now* | individualisation |
| **Write-down** | one side reduces, so the other reduces in response | withdrawal |
| **Default** | silence beyond forbearance | the relationship broke |

**The call is the decline.** A perpetual that is never called runs forever; the
world's move toward self-sufficiency is the issuer exercising an option that was
always theirs. This is not a breach and nobody is owed an apology for it. That
matters more than the arithmetic: [[DEC-004-secular-decline-with-rallies]] forbids
an advocate inside the fiction and [[reserve-instruments]] requires that everyone
who moved was right to move. A decline made of early redemptions satisfies both
without being argued into them, which a decline made of defaults never did.

It also locates AI exactly. **AI is what makes the call possible** — work that
once required asking someone can now be done alone. Using it repays what was owed
to people. The rise of BLIND TRUST is not BEARER BOND defaulting; it is BEARER
BOND being redeemed. [[reserve-instruments]]'s first mechanism — credit creation
stops — becomes arithmetic rather than metaphor.

## The write-down is a response, and its severity is a distribution

> 한쪽이 관계를 서서히 약화시던 급작스럽게 관계를 절단 하던 다른 한쪽도 보통은 관계를
> 서서히 정리한다. 이 정리하는 양은 사람마다 다를 수 있다. 누군가는 실망감에 분노로
> 관계를 완전히 단절할 수 도 있고, 누군가는 그래도 상대방을 빋으면 관계를 서서히
> 낮출수도 있다.

Withdrawal is not an independent event. It answers the counterparty, and the size
of the answer varies by person — one end of the distribution cuts everything at
once in disappointment, the other lowers it slowly and keeps trusting.

**The melt-up mechanism comes from here**, and it is the user's rather than the
assistant's. Because each write-down answers the last one, withdrawal spreads;
where the severe tail of the distribution is involved, the spread is
discontinuous, float drops abruptly, and crowded shorts are stranded. The
inverted rallies [[DEC-004-secular-decline-with-rallies]] requires fall out of
contagion rather than out of a scheduled event.

**Deleted by this decision:** the assistant's `systemic run` — a market-wide
simultaneous withdrawal invented to produce index-level melt-ups — and the
maturity wall that briefly replaced it. Contagion does the work of both and is
explained from inside the world.

## What remains open

- **The severity distribution.** How heavy the total-severance tail is decides how
  often melt-ups happen. Unselected.
- **Forbearance.** How many coupons may be missed before default. Unselected.
- **Call intensity** and how it maps from capability to redemption. Unselected.
- **Asymmetry is not measured.** Gross float distinguishes deep relationships from
  thin ones already; a separate dispersion series for one-sided ones is deferred
  until a surface asks for it.
- **A coupon model.** Reciprocation is currently carried implicitly — a balance
  that is still being serviced is one that has not been called. No separate coupon
  series exists, and none is needed yet.

## Related

- [[reserve-instruments]]
- [[Q-002-listing-lifecycle]]
- [[DEC-007-standard-return-numeraire]]
- [[DEC-004-secular-decline-with-rallies]]
- [[loop-simulation]]

## Sources

- [[SRC-2026-09-20-bearer-bond-issuance]] — [raw/conversations/2026-09-20-bearer-bond-issuance.md](../../raw/conversations/2026-09-20-bearer-bond-issuance.md); registered `user-originated`, because every framing the assistant offered was rejected and the model that replaced it is the user's
- [[SRC-2026-09-15-reserve-absorption-and-trust-instruments]] — [raw/conversations/2026-09-15-reserve-absorption-and-trust-instruments.md](../../raw/conversations/2026-09-15-reserve-absorption-and-trust-instruments.md); the instrument definitions this decision fills in
