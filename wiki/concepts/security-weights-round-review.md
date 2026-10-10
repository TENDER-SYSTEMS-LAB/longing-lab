---
status: working
attribution: llm-synthesis
updated: 2026-10-10
sources:
  - SRC-2026-10-10-security-weights-round-decisions
  - SRC-2026-10-10-security-weights-round-prompt-part1
  - SRC-2026-10-10-security-weights-round-prompt-part2
  - SRC-2026-10-10-security-weights-round-chatgpt-part1
  - SRC-2026-10-10-security-weights-round-chatgpt-part2
  - SRC-2026-10-10-security-weights-round-claude-part1
  - SRC-2026-10-10-security-weights-round-claude-part2
  - SRC-2026-10-10-security-weights-round-deepseek-part1
  - SRC-2026-10-10-security-weights-round-deepseek-part2
  - SRC-2026-10-10-security-weights-round-gemini-part1
  - SRC-2026-10-10-security-weights-round-gemini-part2
  - SRC-2026-10-10-security-weights-round-glm-part1
  - SRC-2026-10-10-security-weights-round-glm-part2
  - SRC-2026-10-10-security-weights-round-grok-part1
  - SRC-2026-10-10-security-weights-round-grok-part2
  - SRC-2026-10-10-security-weights-round-qwen-part1
  - SRC-2026-10-10-security-weights-round-qwen-part2
---

# Security Weights Round Review — seven models check the execution/judgment split

The LLM check the author set on 2026-10-01 and arranged on 2026-10-10 ([[SRC-2026-10-10-security-weights-round-setup]]). Seven services answered a two-part prompt in one conversation each: Part 1 gave their own importance for every step without seeing the author's ([[SRC-2026-10-10-security-weights-round-prompt-part1]]); Part 2 showed the author's values and asked about definitions, steps, classes and importance ([[SRC-2026-10-10-security-weights-round-prompt-part2]]). The checked material is on [[security-definitions]].

**Status.** This page is the assistant's synthesis, `llm-synthesis`. Every response is `llm-proposed`; nothing is adopted. Counts show convergence, not correctness. **ChatGPT and DeepSeek gave identical Part 1 values on 78% of steps** (other pairs 21–66%), so they may not be independent; counts below include both.

## 1. The splits: the author against the models' own values

Each model's execution share is computed from its Part 1 importance and the current classes (the narrow rule included).

| Code | Author | Models, median | Models, range | Author − median |
|---|---|---|---|---|
| STRG | 0.47 | 0.26 | 0.22–0.44 | +0.21 |
| INTR | 0.20 | 0.24 | 0.19–0.27 | -0.04 |
| WRIT | 0.11 | 0.10 | 0.06–0.12 | +0.01 |
| RECH | 0.29 | 0.33 | 0.29–0.47 | -0.04 |
| TELL | 0.20 | 0.12 | 0.10–0.26 | +0.08 |
| LSTN | 0.67 | 0.52 | 0.44–0.61 | +0.15 |
| MEND | 0.36 | 0.24 | 0.21–0.36 | +0.12 |
| DEC | 0.33 | 0.24 | 0.17–0.28 | +0.09 |
| CHSE | 0.26 | 0.22 | 0.19–0.26 | +0.04 |
| MAKE | 0.19 | 0.20 | 0.14–0.33 | -0.01 |
| LERN | 0.58 | 0.55 | 0.47–0.71 | +0.03 |
| TCHR | 0.33 | 0.33 | 0.32–0.47 | +0.00 |
| CARE | 0.24 | 0.32 | 0.26–0.42 | -0.08 |
| VGIL | 0.64 | 0.53 | 0.50–0.67 | +0.11 |
| VIST | 0.41 | 0.41 | 0.39–0.53 | +0.00 |
| GTHR | 0.76 | 0.56 | 0.47–0.71 | +0.20 |
| PLAY | 0.59 | 0.50 | 0.47–0.62 | +0.09 |
| ASK | 0.62 | 0.50 | 0.44–0.69 | +0.12 |
| HELP | 0.42 | 0.42 | 0.36–0.54 | +0.00 |
| TRET | 0.50 | 0.38 | 0.33–0.46 | +0.12 |
| LEND | 0.46 | 0.38 | 0.33–0.41 | +0.08 |
| ETRS | 0.35 | 0.30 | 0.22–0.35 | +0.05 |

**One pattern runs through the table.** The author's execution share is above the models' median for 15 of 22 securities, below it for 4 (INTR, RECH, MAKE, CARE) and equal for 3 (TCHR, VIST, HELP). The gap is largest for STRG and GTHR (+0.20), LSTN (+0.14), MEND (+0.13), ASK and TRET (+0.12). Step by step, the author weights the *doing* — saying it, paying, handing over, making time, taking part, accepting help — and the models weight the *choosing and judging* around it.

**What this means in the world, the assistant's reading.** In [[romance-ontology]] the two shares feed different channels: execution is what a **device** hides, leading to deskilling and the loss of the occasion; judgment is what **substitution** takes, raising calls into BLIND TRUST ([[DEC-014-restoration-is-arrival-and-substitution-is-judgment]]). So the gap does not decide how much a practice declines; it decides **which channel** carries the decline. The author's values route more of it through devices; the models' through AI judgment. A model trained to reason may also overweight deliberation by habit; the round cannot tell that apart from a real difference.

## 2. Steps where nearly all models differ from the author

Steps where at least six of seven models are two or more points from the author's importance:

| Step | | Author | Models, median | Models ≥2 away |
|---|---|---|---|---|
| STRG 2 | Choose whom to address | 1 | 4 | 7/7 |
| STRG 3 | Say it | 4 | 2 | 6/7 |
| STRG 5 | Weigh the answer and act on it | 2 | 5 | 6/7 |
| TELL 2 | Choose whom to tell | 2 | 4 | 6/7 |
| TELL 5 | Weigh the view received | 1 | 4 | 7/7 |
| LSTN 1 | Make time | 5 | 3 | 7/7 |
| LSTN 3 | Understand what is meant | 2 | 5 | 7/7 |
| LSTN 5 | Keep it to oneself | 1 | 3 | 7/7 |
| MEND 3 | Choose what to say or concede | 2 | 4 | 6/7 |
| MEND 4 | Say it | 5 | 2 | 6/7 |
| DEC 4 | Settle on one | 3 | 5 | 6/7 |
| DEC 5 | Carry it out | 4 | 2 | 6/7 |
| TCHR 5 | Let go | 1 | 4 | 7/7 |
| VIST 5 | Spend the time | 2 | 5 | 6/7 |
| GTHR 5 | Take on a role | 1 | 4 | 6/7 |
| TRET 2 | Pay | 5 | 2 | 7/7 |
| TRET 4 | Remember whose turn | 1 | 3 | 6/7 |
| LEND 2 | Hand it over | 5 | 2 | 7/7 |
| LEND 4 | Wait for its return | 1 | 3 | 6/7 |
| ETRS 4 | Refrain from checking | 2 | 5 | 7/7 |

Least credible splits named by the models (three each): **GTHR 7/7**, **LSTN 5/7**, ASK 3/7, STRG 2/7, TRET 2/7, CARE 1/7, WRIT 1/7.

## 3. Definitions

- **Definitions with several branches** whose splits differ: GTHR's civic acts have no boundary (5); RECH mixes "no practical reason" and "on their day", which is calendar-prompted against step 1's "unprompted" (4); MAKE merges making by hand and commissioning (4); VIST holds a visit, a meal and walking home (4); CARE's "body, days or voice" — "voice" unclear to an audience (4); ETRS is defined by a list of objects rather than an act (4); INTR mixes making an introduction and asking for one (3).
- WRIT's "one's own words are words one stands behind" read as circular (4: DeepSeek, Gemini, Grok, Claude by overlap); MEND does not say whose side (2); TRET's "leaving the turn open" may be deliberate or neglect (2); LERN/TCHR mix skill and story (1).
- Overlaps an audience would see (Claude): WRIT with RECH, TELL and MEND; VIST, VGIL and CARE at a deathbed; LEND with ETRS.

## 4. Steps

- **Counted twice:** INTR 1/2 (4); GTHR 2/3/4, attendance at three time scales holding 13 of 17 importance (4); VGIL 2/4 (3); PLAY 3/4 (2); DEC 3/4, CHSE 2/3, RECH 1/2, STRG 1/2 (1 each).
- **A step on the wrong side of the bond:** ETRS 5 is the keeper's act in a security of the one who entrusts (4); MEND 5 bundles offering and accepting forgiveness (4).
- **Missing:** STRG has no step choosing what to say (3); TELL has no step asking for the view, which its definition names (2, and DeepSeek reads step 5 as outside it); RECH 1 is an occurrence, and the choice to act on it is missing (3); LSTN has no decision to listen (1); MAKE's commissioning branch lacks the choice of maker (2); LERN lacks "decide what to learn" against TCHR's "decide what to pass on" (2).
- **Outside the definition:** INTR 5, RECH 5, DEC 5, TELL 5, LSTN 5 add steps the definition does not name (Claude, DeepSeek, ChatGPT).

## 5. Classes

- **The narrow rule as applied.** Six models say VIST 3 should be execution because travel is not read as a message unless the step says so; only Grok supports judgment. WRIT 4, RECH 3, CHSE 5 and MAKE 4 are challenged by three to four on the same ground: the step does not state that the other person reads the means. Grok calls all of them correct. Claude adds that MAKE 3, making by hand, is the rule's own paradigm case and should be judgment. The assistant checked VIST: step 1, "decide to go", already holds the choice between going and calling, so VIST 3 as judgment counts that choice twice.
- **Execution steps holding a live choice:** ETRS 5 (4), LSTN 1 "make time" (3), ASK 4 "accept the help" (3), GTHR 3 "take part" (3), LSTN 5 "keep it to oneself" (2), DEC 2 "gather the options" (2), PLAY 3 (2), ASK 5 (1). Mixed steps are forbidden, so each would need a class or a split into two steps.
- **Inconsistencies inside the list** (Claude, GLM): CARE 4 "check back" is execution while ETRS 4 "refrain from checking" is judgment; CHSE 1 noticing is execution while RECH 1 and CARE 1 are judgment; "keeping" steps (RECH 5, MEND 6, GTHR 4, VGIL 4 against TRET 4, LEND 4, ASK 5) need one rule.
- Judgment steps read as execution: ASK 1 (Gemini), TRET 3 (Qwen), RECH 1 (ChatGPT).

## 6. Decisions for the author — answered 2026-10-10

*The author decided ([[SRC-2026-10-10-security-weights-round-decisions]]), `user-confirmed`: (4) multi-branch definitions are **split into forms**, against the assistant's recommendation to narrow them; (2) the assistant writes revised step lists for review; (3) WRIT 4, RECH 3, CHSE 5 and MAKE 4 are rewritten to state the reading condition and stay judgment, and **VIST 3 returns to execution**; (5) the assistant proposes a rule for "keeping" steps and the fixes; (1) importance is revisited **only on the steps six or seven models disputed**, after the steps are revised.*


1. **The direction of the gap.** Keep the author's weighting of the doing, adopt the models' weighting of the choosing, or adjust only the steps in section 2. This decides whether decline runs more through devices or through AI judgment.
2. **Structural fixes** in section 4 — merge double-counted steps, move or drop the side-switching steps, add the missing ones. Each changes the step list and therefore needs importance again.
3. **The narrow rule's five steps.** Reword each so that it states the reading condition, or return the ones the author does not see as read (VIST 3 most contested).
4. **Multi-branch definitions** in section 3 — narrow each to one act, or split into forms.
5. **Class consistency** in section 5, including a single rule for "keeping" steps.

## Related

- [[security-definitions]]
- [[security-families]]
- [[DEC-014-restoration-is-arrival-and-substitution-is-judgment]]
- [[weight-setting-procedure-review]]
- [[romance-ontology]]

## Sources

- [[SRC-2026-10-10-security-weights-round-decisions]] — [raw/conversations/2026-10-10-security-weights-round-decisions.md](../../raw/conversations/2026-10-10-security-weights-round-decisions.md); the author's five decisions
- [[SRC-2026-10-10-security-weights-round-prompt-part1]] — [raw/documents/2026-10-10-security-weights-round-prompt-part1.md](../../raw/documents/2026-10-10-security-weights-round-prompt-part1.md)
- [[SRC-2026-10-10-security-weights-round-prompt-part2]] — [raw/documents/2026-10-10-security-weights-round-prompt-part2.md](../../raw/documents/2026-10-10-security-weights-round-prompt-part2.md)
- [[SRC-2026-10-10-security-weights-round-chatgpt-part1]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-chatgpt-part1.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-chatgpt-part1.md)
- [[SRC-2026-10-10-security-weights-round-chatgpt-part2]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-chatgpt-part2.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-chatgpt-part2.md)
- [[SRC-2026-10-10-security-weights-round-claude-part1]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-claude-part1.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-claude-part1.md)
- [[SRC-2026-10-10-security-weights-round-claude-part2]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-claude-part2.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-claude-part2.md)
- [[SRC-2026-10-10-security-weights-round-deepseek-part1]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-deepseek-part1.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-deepseek-part1.md)
- [[SRC-2026-10-10-security-weights-round-deepseek-part2]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-deepseek-part2.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-deepseek-part2.md)
- [[SRC-2026-10-10-security-weights-round-gemini-part1]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-gemini-part1.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-gemini-part1.md)
- [[SRC-2026-10-10-security-weights-round-gemini-part2]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-gemini-part2.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-gemini-part2.md)
- [[SRC-2026-10-10-security-weights-round-glm-part1]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-glm-part1.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-glm-part1.md)
- [[SRC-2026-10-10-security-weights-round-glm-part2]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-glm-part2.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-glm-part2.md)
- [[SRC-2026-10-10-security-weights-round-grok-part1]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-grok-part1.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-grok-part1.md)
- [[SRC-2026-10-10-security-weights-round-grok-part2]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-grok-part2.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-grok-part2.md)
- [[SRC-2026-10-10-security-weights-round-qwen-part1]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-qwen-part1.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-qwen-part1.md)
- [[SRC-2026-10-10-security-weights-round-qwen-part2]] — [raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-qwen-part2.md](../../raw/surveys/2026-10-10-security-weights-round/2026-10-10-security-weights-round-qwen-part2.md)
