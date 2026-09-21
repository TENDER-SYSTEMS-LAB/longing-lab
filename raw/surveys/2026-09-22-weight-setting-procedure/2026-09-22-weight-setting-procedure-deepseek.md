Training cut-off: 2024-06. No claim below depends on real practices after that date; the procedure is designed for the fictional record as given.

## Section 1 — The unit of classification

The thing labelled **execution** or **judgment** is the **constitutive unit** of the security. A constitutive unit is the smallest type-level act or decision point that the security’s definition requires and that can be classified without changing the practice into a different practice. It is not an occasion, a market instantiation, or a technology. An occasion instantiates the units; the weights describe the type.

Decomposition rules:

1. Every phrase in the security’s definition must map to at least one constitutive unit.
2. A unit is split until further splitting would either add a step not required by the definition or change the classification of the remainder.
3. A step that is merely instrumental to another step is merged into that step, not counted separately.
4. The unit list is finite, ordered, and published with the security.

For **LETTER** — “a personally composed, physically handwritten message intended for a particular person and released to that person through a delivery route” — an illustrative decomposition is:

| Unit | Constitutive act or decision | Illustrative label only |
|---|---|---|
| CU1 | Select the particular recipient | judgment |
| CU2 | Decide the content to communicate | judgment |
| CU3 | Decide wording, tone, and order | judgment |
| CU4 | Handwrite the message | execution |
| CU5 | Release it to the recipient through the delivery route | execution |

The labels above are illustrative and do not set LETTER’s weights. If the definition later says “choose among delivery routes,” that choice becomes a separate unit; if the route is fixed by the definition, it remains part of CU5.

## Section 2 — The sorting rule

Adopt the record’s candidate with a refinement:

> **Live-option test:** For a constitutive unit U, ask: if U were handed to another agent or system while the person retained only a veto, would the handover contain more than one live option that changes the content or consequential shape of the practice? If yes, U is **judgment**. If no — if the handover merely performs a previously fixed choice, with at most one live option — U is **execution**.

A **live option** is an option permitted by the security’s definition and not already determined by the person’s prior commitments in that occasion. Prior commitments matter. Once a person has chosen the exact sentence, voicing it has no live content option. If the person has not chosen how to ask after someone, a system choosing among “How are you?”, “How have you been?”, and “Are you okay?” has multiple live options.

Apply to the hard cases:

| Hard case | Unit being classified | Live options? | Classification | Reason |
|---|---|---|---|---|
| Voicing a sentence the person chose | Voice the chosen sentence | None or one | execution | The content is already fixed; the act implements it. The restoring side is arrival exposure, not a weight. |
| Reading a text aloud in a voice learned from another person | Read the text in that voice | None or one, if text and voice are fixed | execution | The voice source may restore execution, but it does not add a live content choice. |
| Sending “how are you” and letting a system translate it | Decide how to ask after someone | Multiple: tone, register, intimacy, specificity | judgment | The system is choosing the content of the inquiry, not merely translating a fixed phrase. Translation of a fixed phrase would be execution. |
| System’s interpretation of another person’s message read before the original | Interpret the incoming message | Multiple readings, if interpretation is a constitutive unit | judgment if counted; otherwise an input | No step is handed over. The person’s own decision remains judgment. The interpretation may narrow options, but narrowing is not substitution. Weight changes only if the definition adds or removes a step such as “interpret without intermediary.” |

If a unit can be partly both, the procedure forbids leaving it mixed. It is split into a judgment part and an execution part. If the split is impossible, the unit is classified as judgment when any content-determining live option is present; the execution remainder is treated as implementation of that judgment and is not counted separately. The split is set by the classification panel, subject to the user’s final call.

## Section 3 — The counting rule

Use **equal count of constitutive units**:

\[
\text{execution share} = \frac{\#\text{execution units}}{\#\text{all units}},
\qquad
\text{judgment share} = \frac{\#\text{judgment units}}{\#\text{all units}}.
\]

Round the final pair to the nearest 0.05. The repeatability tolerance is ±0.05.

This rule assumes each constitutive unit is equally identity-bearing. It does not weight by time, consequence, skill, or frequency of failure. Those alternatives are rejected because they invite tuning to outcomes and because they measure something other than the security’s definition. Equal count is transparent and repeatable.

What it distorts: it can overstate routine execution that is constitutive but low-skill, and understate a single high-consequence judgment if that judgment is not decomposed. The correction is not to add ad hoc weights but to enforce the unit definition strictly: a composite judgment should be split into its constitutive decision points if the definition permits; a merely instrumental execution should be merged into the step it serves.

Illustrative only: if LETTER were decomposed as 3 judgment units and 2 execution units, the illustrative pair would be 0.60 judgment / 0.40 execution. This is not a proposal for LETTER.

## Section 4 — Who sets it, and how disagreement is resolved

A panel of three independent classifiers applies Sections 1–3. The user makes the final call.

What is put in front of the user:

- the canonical unit table with each unit’s classification;
- a single proposed pair, rounded to 0.05;
- a sensitivity range showing how the pair changes if each disputed unit flips label or is split;
- a dissent log naming every disputed unit and the strongest argument for each side;
- the procedure’s fallback if the user does not decide.

If two people disagree on one step’s label:

1. They must first agree on the unit list. If they do not, the unit is re-decomposed.
2. They apply the live-option test, stating explicitly which options are live and which are already fixed by prior commitments.
3. If they still disagree, a third classifier reviews the written arguments.
4. If the unit is still disputed, it is split if possible.
5. If it is atomic and still disputed, it defaults to **judgment**, because the presence of a content-determining live option is the distinguishing feature of the framework. The user may override this default, but the override is recorded with reasons.

The final pair is the equal-count pair from the panel’s resolved unit table, unless the user overrides. The user’s decision is part of the security’s definitional record.

## Section 5 — Cross-market consistency

The procedure yields **one pair for all three markets**. Weights are part of the security’s definition, not its market exposure. Japan, Korea, and the United States may differ in exposure to restored execution or substituted judgment, but not in the fixed execution/judgment weights.

To detect the disagreement that condition (b) makes a ground for revision, the procedure runs three independent market panels on the same security’s definition as understood in that market. Each panel produces a unit list, labels, and a pair. If the three pairs agree within ±0.05, the single pair is confirmed. If any pair differs by more than ±0.05, the difference is recorded as a cross-market disagreement.

The disagreement is then diagnosed:

- If it is translation or local instantiation of the same practice, the panels reconcile to one pair.
- If it is a genuine difference in what the security stands for in that market, the security is either split into separate securities or treated under condition (a) as a definition change.
- If it is irreconcilable, the revision procedure in Section 6 is triggered under condition (b).

## Section 6 — The revision procedure

Revision is allowed only under the two fixed conditions.

| Condition | Who may initiate | Evidence required | Revision record | Effect on published readings |
|---|---|---|---|---|
| (a) The security’s own definition changes — a step is added or removed | Definition owner, research house, or a market panel | Authoritative old and new definition texts; old and new unit lists; classification of added/removed units; recomputed pair | Security ID; old pair; new pair; old and new unit lists; condition (a); initiator; date; panel; disputed units; user decision; effective date | Old readings remain as published under the old pair. New readings use the new pair prospectively. If the change is a correction, the institution may publish restated readings clearly marked as restated, with the original archive retained. |
| (b) The same security’s weights disagree across Japan, Korea, and the United States | Any market panel or cross-market auditor | Three independent classification records; unit lists; labels; pairs; pairwise differences greater than ±0.05 | Security ID; old pair; harmonized new pair; market disagreement record; dissent; initiator; date; panel; user decision; effective date | Old readings remain as published. The harmonized pair applies prospectively. Historical series show a flagged break. No retroactive recalculation. |

A revision record is public to the institution. It must state which condition is satisfied and why the other condition is not being used. Revision because the generated record fits badly is rejected and must not appear as evidence.

## Section 7 — Failure modes

Ranked from hardest to easiest to detect afterwards:

| Rank | Failure mode | Why it is hard to detect | Mitigation |
|---|---|---|---|
| 1 | Wrong unit list: a constitutive judgment or execution step is omitted or added | The pair still looks precise; no external outcome exposes the omission | Independent decomposition; definition audit against every phrase |
| 2 | Misclassifying a live-option step as execution because prior commitments were assumed | The assumption is often invisible after the fact | Require explicit prior-commitment statements in the unit table |
| 3 | Equal-count rule misrepresents a practice with one dominant judgment | The rule is transparent but conceptually wrong for that case | Strict constitutive-unit definition; sensitivity range; split composite judgments where the definition permits |
| 4 | Cross-market harmonization masks a real definitional difference | The final single pair hides the disagreement | Publish the market audit and dissent log |
| 5 | User override without recorded reasons | Later readers cannot reconstruct why the pair departed from the panel | Record the override, the range, and the reasons |
| 6 | Revision disguised as condition (a) or (b) to fit outcomes | The stated evidence may look valid if not pre-registered | Pre-register revision evidence; audit revision records |
| 7 | Ambiguous mixed unit defaulted to judgment | The default is visible if flagged, but can be forgotten | Flag every defaulted unit in the record |
| 8 | Tolerance drift: panels repeatedly differ by just under the threshold | Easy to detect statistically over time | Periodic audit of panel agreement |

## Objections

One fixed point is awkward: if weights are definitional, condition (b) — “the same security’s weights disagree across the three markets” — is better read as evidence that the markets understand the security differently, not that the weights themselves should vary by market. The procedure above therefore treats cross-market disagreement as a trigger for definitional review or security splitting, while still producing one pair when the practice is genuinely the same. I design for the fixed point as given, but this is the point most likely to create false revisions if used mechanically.