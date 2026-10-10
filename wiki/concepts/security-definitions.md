---
status: working
attribution: jointly-developed
updated: 2026-10-10
sources:
  - SRC-2026-10-10-security-weights-round-decisions
  - SRC-2026-10-10-security-weights-round-setup
  - SRC-2026-10-10-security-weights-round-prompt-part1
  - SRC-2026-10-10-security-weights-round-prompt-part2
  - SRC-2026-10-10-classification-rule-decision
  - SRC-2026-10-10-security-weights-decisions
  - SRC-2026-10-10-fund-construction-decisions
  - SRC-2026-10-10-security-legs-and-tickers
  - SRC-2026-10-01-importance-weighting-and-concepts-above-securities
  - SRC-2026-09-21-restoration-is-arrival-and-substitution-is-judgment
---

# Security Definitions — steps for the execution and judgment weights

The task the author set on 2026-10-01 and left until the securities were chosen: each security's steps are counted by importance, the importance is part of its definition, the author sets it, and each setting is checked against as many LLMs as possible ([[DEC-014-restoration-is-arrival-and-substitution-is-judgment]], [[SRC-2026-10-01-importance-weighting-and-concepts-above-securities]]). The securities were chosen on 2026-10-10 ([[security-families]]).

**Status.** The definitions and steps are the assistant's draft, `llm-proposed`; the importance values are the author's, set on 2026-10-10 (next section). The equal-count pairs in the draft are a reference only.

## The author's settings (2026-10-10)

The author set every step's importance on a decision page ([[SRC-2026-10-10-security-weights-decisions]]), `user-confirmed`. Values are in step order; no class was changed. *VIST returned to 0.47 when step 3 went back to execution ([[SRC-2026-10-10-security-weights-round-decisions]]).* *Pairs updated after the narrow rule was adopted later the same day ([[SRC-2026-10-10-classification-rule-decision]]); five securities moved.* Execution share = importance of execution steps ÷ total importance.

| Code | Importance by step | Execution | Judgment |
|---|---|---|---|
| STRG | 5,1,4,3,2 | 0.47 | 0.53 |
| INTR | 5,4,3,2,1 | 0.20 | 0.80 |
| WRIT | 5,5,5,2,2 | 0.11 | 0.89 |
| RECH | 5,4,3,2,3 | 0.29 | 0.71 |
| TELL | 5,2,4,3,1 | 0.20 | 0.80 |
| LSTN | 5,4,2,3,1 | 0.67 | 0.33 |
| MEND | 3,5,2,5,4,3 | 0.36 | 0.64 |
| DEC | 5,2,4,3,4 | 0.33 | 0.67 |
| CHSE | 3,5,5,2,4 | 0.26 | 0.74 |
| MAKE | 5,4,3,4 | 0.19 | 0.81 |
| LERN | 3,1,2,4,2 | 0.58 | 0.42 |
| TCHR | 5,3,2,4,1 | 0.33 | 0.67 |
| CARE | 5,4,3,1,4 | 0.24 | 0.76 |
| VGIL | 3,5,2,4 | 0.64 | 0.36 |
| VIST | 5,3,1,4,2,2 | 0.47 | 0.53 |
| GTHR | 3,4,5,4,1 | 0.76 | 0.24 |
| PLAY | 3,2,5,4,3 | 0.59 | 0.41 |
| ASK | 5,3,4,5,4 | 0.62 | 0.38 |
| HELP | 5,1,4,2 | 0.42 | 0.58 |
| TRET | 2,5,4,1 | 0.50 | 0.50 |
| LEND | 3,5,4,1 | 0.46 | 0.54 |
| ETRS | 5,4,3,2,3 | 0.35 | 0.65 |

**Follow-ups decided or opened in the same exchange:**

- **CARE step 5** is rewritten as a change over time, at the author's choice, because it read the same as step 2: step 2 is the first choice of help, step 5 is "change the care as the need changes". Its importance, 4, was set against the earlier wording and is carried over until the author resets it.
- **The classification rule is put to review**, `user-originated`. The author's memo on RECH asked whether choosing the means is judgment; asked whether to change RECH alone or the rule, the author chose to review the rule itself — that manner (medium, route, handwriting) is never judgment. Until the review ends, every class stays as drafted.
- **TRET's Korean name** "한턱" does not land for the author; opinions are to be gathered before it is changed. The English name and code stay.

Pairs are not final until the rule review and the LLM check are done.

## Review of the classification rule — proposed, decided 2026-10-10

**Decided** ([[SRC-2026-10-10-classification-rule-decision]]), `user-confirmed`: **the narrow rule.** A choice of means is judgment when the other person reads the means as part of the message; other manner stays execution. Five steps change class — WRIT 4, RECH 3, CHSE 5, MAKE 4, VIST 3 — and no importance changed. The medium itself is still not the condition of romance; the choice of it, when read, is judgment, as with chosen friction. The analysis below is kept as the proposal it was.

`llm-proposed`. The author put the rule to review after the memo on RECH ([[SRC-2026-10-10-security-weights-decisions]]).

**Why the review comes first.** The rule decides every step's class, so a change can move all twenty-two pairs. An LLM check run before the review would check classes under a rule that may change.

**The current rule.** A step is judgment only when its options differ in the practice's product or meaning; manner — medium, route, handwriting — is never judgment. This came from the weight round's consensus ([[weight-setting-procedure-review]]) and agrees with the decision that medium, body and place are not the condition of romance ([[SRC-2026-10-04-romance-round-decisions]]).

**What argues against it.** The ontology already holds that *chosen friction* — a slow path chosen for a reason — is romantic, and imposed friction is not ([[romance-ontology]], Layer 1). A chosen path is a choice of manner that carries meaning. A handwritten birthday letter and an auto-sent message can say different things to the one who receives them.

**What a change would do.** Under [[DEC-014-restoration-is-arrival-and-substitution-is-judgment]], only judgment steps are exposed to substitution. If choosing the means becomes judgment, a system that picks the means for a person — a default channel, an auto-sent greeting — counts as substitution and raises calls. Under the current rule it is only the doing handed over.

**Three rules compared, with the author's importance values.** "Narrow" makes a step judgment when it is a choice of means that the other person reads as part of the message; "wide" adds every step of saying, handing over or going.

| Code | Steps that change class | Execution, current | Narrow | Wide |
|---|---|---|---|---|
| STRG | 3 (wide only) | 0.47 | 0.47 | 0.20 |
| INTR | 4 (wide only) | 0.20 | 0.20 | 0.07 |
| WRIT | 4 | 0.21 | 0.11 | 0.11 |
| RECH | 3 | 0.47 | 0.29 | 0.29 |
| TELL | 4 (wide only) | 0.20 | 0.20 | 0.00 |
| CHSE | 5 | 0.47 | 0.26 | 0.26 |
| MAKE | 4 | 0.44 | 0.19 | 0.19 |
| VIST | 3 | 0.47 | 0.41 | 0.41 |
| GTHR | 2 (wide only) | 0.76 | 0.76 | 0.53 |
| ASK | 3 (wide only) | 0.62 | 0.62 | 0.43 |
| ETRS | 3 (wide only) | 0.35 | 0.35 | 0.18 |

The wide rule leaves TELL with no execution at all and moves eleven securities; nearly every practice would become fully exposed to substitution. The narrow rule moves five (RECH, WRIT, CHSE, MAKE, VIST).

**The assistant's reading.** The narrow rule fits the decided ontology best: the medium is still not the condition of romance, but *the choice of it*, when the other person reads it, is judgment — the same reasoning as chosen friction. Which steps fall under it is the author's call.

## Why this is needed

- **The price model needs the pair.** Under [[DEC-014-restoration-is-arrival-and-substitution-is-judgment]], what raises calls is a system deciding what a person could have decided. A security's judgment share is how much of it AI can take by substitution; its execution share is what can be handed over with the choice kept. Without the pair, no security can be priced through the AI wave.
- **The pair is only as precise as the definition.** The weight round found LETTER's execution share ran from 0.25 to 0.50 because the definition sentence left three choices open ([[weight-setting-procedure-review]]). So the definitions and steps come first, then importance.
- **The author set the order.** Weights were to be set after the securities were chosen ([[SRC-2026-10-01-weights-first-securities-later]]).

## The procedure, as decided

- The unit is a step of the practice, induced from the definition sentence.
- A step is **judgment** when it contains more than one live option that differs in the practice's product or meaning; otherwise it is **execution**. Manner — medium, route, handwriting — is execution, **except a choice of means that the other person reads as part of the message, which is judgment** (narrow rule, decided 2026-10-10, [[SRC-2026-10-10-classification-rule-decision]]).
- Mixed steps are forbidden: every step is one or the other.
- Each step gets an importance set by the author; the execution share is the importance of execution steps over the total.
- Importance is part of the definition, so changing it is a revision under condition (a).

## Which securities need a pair

Twenty-two: the twelve families without legs, the six legs and the four forms. The family funds follow their smaller leg; GIFT and IOU, whose forms are not legs, are open. The three states are priced through carriers and need no pair of their own.

## Draft definitions and steps

### STRG — STRANGER (낯선이)

*Addressing someone one does not know and taking up what they answer.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide to address a stranger rather than look it up | judgment | asking a person or a device changes what is exchanged |
| 2 | Choose whom to address | judgment | a different person gives a different answer |
| 3 | Say it | execution | wording changes little of the meaning |
| 4 | Hear the answer | execution | no live option |
| 5 | Weigh the answer and act on it | judgment | following or not changes the outcome |

Equal-count pair: execution 0.40 / judgment 0.60.

### INTR — INTRO (소개)

*Putting two parties one knows in touch, or asking someone who knows both to do it.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | See that two would suit each other | judgment | the match itself |
| 2 | Choose whom or what to recommend | judgment | a different match |
| 3 | Stand behind the match in words | judgment | staking one's name changes its meaning |
| 4 | Make the contact | execution | manner only |
| 5 | Follow up | execution | no live option |

Equal-count pair: execution 0.40 / judgment 0.60.

### WRIT — WRITE (글)

*Choosing words for one person, sending them and standing behind them; one's own words are words one stands behind.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Choose the recipient | judgment | a different letter |
| 2 | Decide what to say | judgment | the content |
| 3 | Choose the words | judgment | words differing in meaning |
| 4 | Choose the medium the recipient will read (rewritten 2026-10-10; was "Put it into a medium") | judgment | the chosen medium is read by the recipient (narrow rule, 2026-10-10) |
| 5 | Send it | execution | release; the choice to send is in the steps above |

Equal-count pair: execution 0.20 / judgment 0.80 (after the narrow rule).

### RECH — REACH (안부)

*Making contact with someone at a distance with no practical reason, or on their day.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Think of the person unprompted | judgment | whom one thinks of |
| 2 | Choose the moment | judgment | a day remembered or not changes the meaning |
| 3 | Choose a means the other person will read (rewritten 2026-10-10; was "Choose the means") | judgment | the chosen means is read by the other person (narrow rule, 2026-10-10) |
| 4 | Make contact or send | execution | manner only |
| 5 | Keep the thread over time | execution | repetition, no new option |

Equal-count pair: execution 0.40 / judgment 0.60 (after the narrow rule).

### TELL — CONFIDE · leg (털어놓기) · CNFD 기대는 다리

*Telling someone a personal matter and asking for their view.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide to tell someone | judgment | telling a person, a device or no one |
| 2 | Choose whom to tell | judgment | a different listener |
| 3 | Choose what to disclose | judgment | the content |
| 4 | Say it | execution | manner only |
| 5 | Weigh the view received | judgment | what one then does |

Equal-count pair: execution 0.20 / judgment 0.80.

### LSTN — CONFIDE · leg (들어 주기) · CNFD 주는 다리

*Listening to someone's trouble and answering it.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Make time | execution | no live option once asked |
| 2 | Listen through | execution | no live option |
| 3 | Understand what is meant | judgment | readings differing in meaning |
| 4 | Choose what to say back | judgment | the answer |
| 5 | Keep it to oneself | execution | a duty, no live option |

Equal-count pair: execution 0.60 / judgment 0.40.

### MEND — MEND (화해)

*Repairing a relation after harm, by apology, talk or forgiveness.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Recognise the harm | judgment | what one admits |
| 2 | Decide to repair | judgment | repair or not |
| 3 | Choose what to say or concede | judgment | the content |
| 4 | Say it | execution | manner only |
| 5 | Offer or accept forgiveness | judgment | forgive or not |
| 6 | Keep to the repair | execution | no new option |

Equal-count pair: execution 0.33 / judgment 0.67.

### DEC — DECIDE (결정)

*Reaching one decision with another person.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Frame the question together | judgment | what is being decided |
| 2 | Gather the options | execution | finding, not choosing |
| 3 | Weigh options against each other's wishes | judgment | the trade-off |
| 4 | Settle on one | judgment | the decision |
| 5 | Carry it out | execution | doing |

Equal-count pair: execution 0.40 / judgment 0.60.

### CHSE — GIFT · form (고른 선물) · GIFT 형태

*Choosing a thing for one particular person and giving it.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Notice the occasion | execution | the occasion is given |
| 2 | Consider what they would value | judgment | reading the person |
| 3 | Choose the thing | judgment | a different gift |
| 4 | Obtain it | execution | manner only |
| 5 | Choose how to give it, as the recipient will read it (rewritten 2026-10-10; was "Give it") | judgment | how it is given is read by the receiver (narrow rule, 2026-10-10) |

Equal-count pair: execution 0.40 / judgment 0.60 (after the narrow rule).

### MAKE — GIFT · form (만든 선물) · GIFT 형태

*Making a thing for one particular person and giving it, or having its maker make it for them.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide what to make for them | judgment | a different object |
| 2 | Shape its particular form | judgment | form differing in meaning for that person |
| 3 | Make it | execution | doing |
| 4 | Choose how to give it, as the recipient will read it (rewritten 2026-10-10; was "Give it") | judgment | how it is given is read by the receiver (narrow rule, 2026-10-10) |

Equal-count pair: execution 0.25 / judgment 0.75 (after the narrow rule).

### LERN — TEACH · leg (배우기) · TCH 기대는 다리

*Learning a skill or a story from a person who has it.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Choose whom to learn from | judgment | a different teacher |
| 2 | Ask to be taught | execution | manner only |
| 3 | Watch and copy | execution | doing |
| 4 | Practise under correction | execution | doing |
| 5 | Judge when one has it | judgment | when to stop leaning |

Equal-count pair: execution 0.60 / judgment 0.40.

### TCHR — TEACH · leg (가르치기) · TCH 주는 다리

*Showing someone a skill or passing on a story.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide what to pass on | judgment | the content |
| 2 | Show it | execution | doing |
| 3 | Watch the learner | execution | no live option |
| 4 | Correct | judgment | which fault to correct |
| 5 | Let go | judgment | judging readiness |

Equal-count pair: execution 0.40 / judgment 0.60.

### CARE — CARE (돌봄)

*Looking after a person in need: their body, their days or their voice.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Notice the need | judgment | what is seen as needed |
| 2 | Decide what help to give | judgment | the care itself |
| 3 | Give the help | execution | doing |
| 4 | Check back | execution | routine |
| 5 | Change the care as the need changes (rewritten 2026-10-10; was "Adjust to the person") | judgment | a later choice, apart from the first choice in step 2 |

Equal-count pair: execution 0.40 / judgment 0.60.

### VGIL — VIGIL (곁)

*Staying with someone in grief or at the end, when nothing can be fixed.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide to come | judgment | come or not |
| 2 | Be there | execution | presence, no live option |
| 3 | Choose whether and what to say | judgment | silence or words |
| 4 | Stay through | execution | no new option |

Equal-count pair: execution 0.50 / judgment 0.50.

### VIST — VISIT (방문)

*Going to be with someone in body: a visit, a meal arranged together, walking them home.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide to go | judgment | go or call |
| 2 | Arrange the time | execution | scheduling |
| 3 | Travel | execution | returned to execution 2026-10-10: the choice between going and calling is already step 1 |
| 4 | Choose what to do together | judgment | the time's content |
| 5 | Spend the time | execution | presence |
| 6 | See them back | execution | doing |

Equal-count pair: execution 0.67 / judgment 0.33 (VIST 3 returned to execution).

### GTHR — GATHER (모임)

*Joining others who share a purpose and keeping a place among them; civic acts enter here.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Choose the group | judgment | a different place among people |
| 2 | Go and join | execution | doing |
| 3 | Take part | execution | doing |
| 4 | Keep coming | execution | repetition |
| 5 | Take on a role | judgment | what one becomes in the group |

Equal-count pair: execution 0.60 / judgment 0.40.

### PLAY — PLAY (놀이)

*Doing something for its own sake with others: a game, music.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Choose what to play and with whom | judgment | a different game |
| 2 | Set it up | execution | manner |
| 3 | Play | execution | doing |
| 4 | Respond to the others | judgment | moves differing in outcome |
| 5 | Finish or agree to play again | execution | no new option |

Equal-count pair: execution 0.60 / judgment 0.40.

### ASK — FAVOR · leg (부탁하기) · FAVR 기대는 다리

*Asking someone near for help with labour or time.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide not to do it alone or buy it | judgment | a person, a service or oneself |
| 2 | Choose whom to ask | judgment | a different helper |
| 3 | Ask | execution | manner |
| 4 | Accept the help | execution | doing |
| 5 | Keep the debt in mind | execution | no live option |

Equal-count pair: execution 0.60 / judgment 0.40.

### HELP — FAVOR · leg (도와주기) · FAVR 주는 다리

*Giving someone near labour or time they asked for.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide to help | judgment | help or not |
| 2 | Arrange the time | execution | scheduling |
| 3 | Do the work | execution | doing |
| 4 | See what is needed beyond the ask | judgment | what more is given |

Equal-count pair: execution 0.50 / judgment 0.50.

### TRET — IOU · form (한턱) · IOU 형태

*Paying for someone now and leaving the turn open.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide to pay for them | judgment | pay, split or not |
| 2 | Pay | execution | doing |
| 3 | Leave the account unsettled | judgment | settling or not changes the meaning |
| 4 | Remember whose turn | execution | no live option |

Equal-count pair: execution 0.50 / judgment 0.50.

### LEND — IOU · form (빌려주기) · IOU 형태

*Lending to someone without a contract.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide to lend and how much | judgment | the loan |
| 2 | Hand it over | execution | doing |
| 3 | Set no terms | judgment | terms or not changes the meaning |
| 4 | Wait for its return | execution | no live option |

Equal-count pair: execution 0.50 / judgment 0.50.

### ETRS — ENTRUST (맡김)

*Trusting someone with something of one's own — a key, a secret, a child, one's name, a time — without proof.*

| # | Step | Class | Why |
|---|---|---|---|
| 1 | Decide to entrust | judgment | entrust or not |
| 2 | Choose to whom | judgment | a different keeper |
| 3 | Hand it over or say it | execution | manner |
| 4 | Refrain from checking | judgment | tracking or not changes the meaning |
| 5 | Keep it or give it back | execution | the keeper's doing |

Equal-count pair: execution 0.40 / judgment 0.60.

## Questions for the author — answered 2026-10-10, except the LLM check

1. **GIFT and IOU funds** — *equal weights, decided.* Do they follow the smaller form, as the leg families follow the smaller leg, or weight their two forms equally?
2. **Definitions and classes.** Accept, reword, or change the class of any step.
3. **Importance.** Set each step's importance, on a 1–5 scale proposed by the assistant.
4. **The LLM check** — *set up 2026-10-10 ([[SRC-2026-10-10-security-weights-round-setup]]): two parts, Part 1 blind ([[SRC-2026-10-10-security-weights-round-prompt-part1]]) and Part 2 with the author's values ([[SRC-2026-10-10-security-weights-round-prompt-part2]]), sections A–D, sent to seven services; TRET's Korean name is not asked and stays open.* After the importance is set, the assistant drafts a round prompt so that each setting is checked against as many LLMs as possible, as decided on 2026-10-01.

## Related

- [[security-weights-round-review]]
- [[security-families]]
- [[DEC-014-restoration-is-arrival-and-substitution-is-judgment]]
- [[weight-setting-procedure-review]]
- [[letter-practice-dynamics]]
- [[current-state]]

## Sources

- [[SRC-2026-10-10-security-weights-round-decisions]] — [raw/conversations/2026-10-10-security-weights-round-decisions.md](../../raw/conversations/2026-10-10-security-weights-round-decisions.md); four narrow-rule steps rewritten, VIST 3 returned, forms to be split
- [[SRC-2026-10-10-security-weights-round-setup]] — [raw/conversations/2026-10-10-security-weights-round-setup.md](../../raw/conversations/2026-10-10-security-weights-round-setup.md); the round set up
- [[SRC-2026-10-10-security-weights-round-prompt-part1]] — [raw/documents/2026-10-10-security-weights-round-prompt-part1.md](../../raw/documents/2026-10-10-security-weights-round-prompt-part1.md); round prompt, Part 1
- [[SRC-2026-10-10-security-weights-round-prompt-part2]] — [raw/documents/2026-10-10-security-weights-round-prompt-part2.md](../../raw/documents/2026-10-10-security-weights-round-prompt-part2.md); round prompt, Part 2
- [[SRC-2026-10-10-classification-rule-decision]] — [raw/conversations/2026-10-10-classification-rule-decision.md](../../raw/conversations/2026-10-10-classification-rule-decision.md); the narrow rule adopted
- [[SRC-2026-10-10-security-weights-decisions]] — [raw/conversations/2026-10-10-security-weights-decisions.md](../../raw/conversations/2026-10-10-security-weights-decisions.md); importance set; CARE step 5; the rule review; TRET's Korean name
- [[SRC-2026-10-10-fund-construction-decisions]] — [raw/conversations/2026-10-10-fund-construction-decisions.md](../../raw/conversations/2026-10-10-fund-construction-decisions.md); funds follow the smaller leg; families without legs are securities
- [[SRC-2026-10-10-security-legs-and-tickers]] — [raw/conversations/2026-10-10-security-legs-and-tickers.md](../../raw/conversations/2026-10-10-security-legs-and-tickers.md); legs, forms and ticker codes
- [[SRC-2026-10-01-importance-weighting-and-concepts-above-securities]] — [raw/conversations/2026-10-01-importance-weighting-and-concepts-above-securities.md](../../raw/conversations/2026-10-01-importance-weighting-and-concepts-above-securities.md); importance weighting, importance in the definition, mixed steps forbidden
- [[SRC-2026-09-21-restoration-is-arrival-and-substitution-is-judgment]] — [raw/conversations/2026-09-21-restoration-is-arrival-and-substitution-is-judgment.md](../../raw/conversations/2026-09-21-restoration-is-arrival-and-substitution-is-judgment.md); substitution counts judgment
