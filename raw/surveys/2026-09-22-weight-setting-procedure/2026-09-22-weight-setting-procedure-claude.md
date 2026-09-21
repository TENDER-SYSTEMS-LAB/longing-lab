# Setting a Security's Execution and Judgment Weights: A Procedure

This is a procedure only. Every number attached to LETTER below is *illustrative*. My reliable knowledge runs to the end of May 2026. That limit matters only where I describe real practices: speech neuroprostheses for ALS, voice cloning, and machine translation of phatic messages.

One principle governs every section. The weights are part of the security's definition. So the procedure should make them a function of the definition text and nothing else. Anything that varies with era, market behaviour or the price record is kept out of the calculation by construction, not just by instruction.

---

## Section 1: The unit of classification

**The unit is the atomic act a definition clause requires.** It is built in two layers.

The first layer is the **clause**. Each security's definition is restated as a list of necessary conditions. Each condition can fail on its own, and each is stated at one level of generality. This is the *clause normalization rule*: no clause may be a sub-case of another, and no clause may bundle two conditions that can fail separately. Clauses are what condition (a) revises, so anchoring the weights to them ties revision directly to the definition.

The second layer is the **unit**. Each clause breaks down into the smallest acts an occasion must contain to satisfy it. A unit is either a **decision point**, where the practitioner settles something, or an **enactment**, where the practitioner carries something out. A step that mixes the two, such as "write the letter", is split until each piece is one or the other. The list is finite because only acts required by some clause are listed. Incidental acts, like finding a pen, are not units unless the definition makes them matter.

This decomposition means the "partly both" problem mostly disappears at the unit level. It returns only as a question of how a clause's mass is shared between its units (Section 3).

**LETTER decomposition** (units listed; labels come from Section 2):

| Clause | Unit | Kind |
|---|---|---|
| C1. Intended for a particular person | U1. Fix the addressee | Decision |
| C2. Personally composed | U2. Settle what to say and what to withhold | Decision |
| | U3. Settle how to say it: form of address, register, length | Decision |
| | U4. Work the text into finished form: draft, hold, correct | Enactment (contested, see below) |
| C3. Physically handwritten | U5. Inscribe by hand | Enactment |
| C4. Released to that person | U6. Decide whether and when to release | Decision |
| | U7. Close and commit the object | Enactment |
| C5. Through a delivery route | U8. Address, stamp, post | Enactment |
| | U9. Transit | Enactment, performed by the route (flagged) |

Two candidate units were considered and absorbed because they fail the materiality prong of Section 2. Choice of materials and layout is one. Choice of route is the other, since at the unannotated reference form of LETTER there is ordinarily one route.

U4 is contested because correcting a draft involves choices. I classify it as enactment on the grounds that the choices it contains are already counted in U2 and U3. A classifier who disagrees will move mass within C2, not add a unit.

---

## Section 2: The sorting rule

I adopt the record's candidate and refine it in two ways: I make it **counterfactual** and **two-pronged**.

The candidate refers to a step "handed over". Weights, however, describe the practice itself, not what any technology does to it. So the test is applied as a hypothetical:

> **Test.** Suppose a system performed this unit in place of the practitioner. Would it have to choose among two or more options that are
> (i) **live**: actually available, and actually entertained by a competent practitioner performing the practice in its defined form; and
> (ii) **consequential**: a different choice would change something the definition cares about, such as what the particular person receives, whether, when, or from whom?
>
> If yes on both prongs, the unit is **judgment**. Otherwise it is **execution**.

The consequential prong is what keeps "which pen" from counting as judgment. The live prong keeps purely theoretical alternatives out. The test is binary on purpose. Differences of degree, such as how many live options there are or how heavily they bear, belong to exposure measurement, not to the weights.

The same test must also be the one used to classify what a technology hands over when exposure is measured. If the weights and the exposure measurement sort acts by different rules, the product of the two becomes meaningless even if each is correct on its own terms. That coupling is a requirement, not a proposal about exposure.

**The three hard cases:**

| Case | Units involved | Classification | Why |
|---|---|---|---|
| Voicing a sentence the person chose (ALS decoder) | "Settle the sentence" (decision, kept) + "render it audibly" (enactment) | **Execution, restored → arrival** | The sentence is fixed before rendering, so the system chooses nothing that counts under the consequential prong. |
| Reading a text aloud in a voice learned from another person | "Render audibly" (enactment) + "whose voice" (decision) | **Split.** Rendering is execution restored. Voice identity is judgment if the security's definition treats who is heard as part of the output. | If the practitioner chose the voice, that judgment is kept. If the system defaulted to it, a small judgment unit was substituted. **Undecidable by this rule:** whether the voice belongs to the security's output is a *definition* question. Fallback: settle it in the definition, which changes the clause list; do not settle it in the weights. |
| Sending *how are you* and letting a system translate it | "Settle how to ask after this person" (decision) | **Judgment substituted** | In Korean and Japanese, asking after someone requires choosing among live, consequential forms: honorific level, whether to ask about health or meals or nothing at all, formality. The system makes that choice. The English wording the user typed does not settle it. |
| A system's interpretation read before the original | "Interpret the incoming message" (decision) | **Judgment, kept.** The label does not change. | Nothing is handed over, so the unit stays with the person. The narrowing of the person's options is real, but it is not a *label* question. **This procedure cannot represent it.** Fallback: add a "narrowing-exposed" annotation to the judgment unit, which the exposure measurement may use. The weight stays unchanged. (See *Objections*.) |

**Units that are partly both.** After decomposition, the remaining mixed cases sit at the level of a clause that contains both kinds of unit. How that clause's mass is shared is set in Section 3 by the classifiers, on a fixed grid, and decided finally by the user.

---

## Section 3: The counting rule

**Rule: clause-anchored allocation on a quarter grid.**

1. Each normalized clause carries equal mass, 1/k, where k is the number of clauses.
2. A clause whose units are all one kind gives its full mass to that kind.
3. A mixed clause is split on the grid {¼, ½, ¾}. The classifiers answer one fixed question: *"Take an occasion in which every judgment unit of this clause is settled and nothing has yet been done. What share of what the clause requires is still unmet?"* The answer is the execution share. If classifiers cannot converge, the default is ½.
4. The execution weight is the sum of execution mass, and the judgment weight is the sum of judgment mass. Together they sum to one.

**What it assumes.** Necessary conditions have no natural ranking against one another. Each is equally a reason the occasion does or does not count as this security, so equal mass is the neutral choice.

**What it distorts.** The wording of the definition drives the weights. Splitting "composed" into two clauses would double its mass. The clause normalization rule is the only guard against this, which makes drafting the definition a consequential act (see Section 7). The grid also limits resolution: with five clauses, one grid step in one clause moves the pair by 0.05.

**Why not the alternatives:**

| Rule | Problem |
|---|---|
| Equal count of units | Granularity drives the result: listing three posting acts outweighs one act of choosing an addressee. It is kept as a *diagnostic* (see below). |
| Weighted by time | Durations change with technology, which is exactly what the waves do. The weights would drift by era, violating fixed point 3. It also inflates execution systematically. |
| Weighted by consequence | Judgment units have consequences by definition; execution units have them only through failure. The measure is biased toward judgment and hard to repeat. |
| Weighted by failure causes | This is empirical and era-dependent. It sits one step away from tuning to outcomes. |

**Diagnostic.** Run equal unit count alongside the main rule. If the two differ by more than the tolerance, the decomposition is flagged for a granularity review before the pair goes to the user.

**Tolerance.** ±0.05 on the pair, which is one grid step in one clause. Two independent runs of the procedure on the same definition should land within that. Any wider gap means a unit label or a clause split is genuinely contested.

**LETTER, illustrative only:**

| Clause | Judgment / Execution (*illustrative*) |
|---|---|
| C1 | 1 / 0 |
| C2 | ¾ / ¼ |
| C3 | 0 / 1 |
| C4 | ¾ / ¼ |
| C5 | 0 / 1 |
| **Pair** | **judgment 0.50 / execution 0.50** (*illustrative*) |

The equal-count diagnostic gives 4 judgment units against 5 execution units, about 0.44 / 0.56. That gap of 0.06 exceeds tolerance, so this illustrative run would be flagged. The review would find that C5 is split into three enactments while C1 has a single decision. The flag works as intended: it points to granularity, not to a mislabel.

---

## Section 4: Who sets it, and how disagreement is resolved

**Classifiers.** At least two work independently. They share the definition text and the test, but not each other's work. None of them may see the generated price record or any exposure series. Each produces the clause list, the unit table with labels, and the clause splits.

**Reconciliation, unit by unit.** When two classifiers disagree on a unit's label, they are made to state which prong they differ on.

- **Disagreement on the live prong** is settled by evidence about the practice: whether competent practitioners in the defined form actually weigh these options. This is evidence about the practice, not about prices.
- **Disagreement on the consequential prong** is settled against the definition text: does the definition care about this feature of the output? If the text does not say, the definition is underspecified. That goes to the user as a *definition* question, not a weight question.
- **If disagreement remains**, the unit keeps both labels, and its clause is split at ½ as a fallback. The dissent is recorded.

**What goes in front of the user.** The user sees a decomposition, not a bare pair:

1. The clause list with the normalization check.
2. Each classifier's unit table side by side, with disagreements highlighted and the prong named.
3. The resulting pair under each classifier's labels. The spread between them is the honest range.
4. The equal-count diagnostic result.
5. The reconciled proposed pair, together with the list of decisions the user is being asked to make: which contested units to label which way, and which splits to set.

The user rules on the contested items. The pair then follows mechanically from those rulings. It is never set directly.

---

## Section 5: Cross-market consistency

Fixed point 3 makes the weights part of the security's definition, and condition (b) treats disagreement between markets as a defect. Together these imply **one published pair for all three markets.**

**Detection.** The classification is run separately for each market, using evidence about that market's practice for the live prong. Each market gets its own panel or evidence base. The comparison is made at the **unit level**, not only at the level of the pair. Two markets can reach the same pair with different labels whose differences cancel out. That hidden disagreement is still a condition (b) finding.

**Condition (b) is triggered by either:**
- a different label on the same unit in different markets, or
- pairs that differ by more than the tolerance.

The binary sorting rule helps here. Korean honorific choice has more live options than the English equivalent, but asking after someone is judgment in all three markets. The difference in degree goes to exposure measurement and does not split the weights. A split appears only when a unit is judgment in one market and execution in another.

**Once triggered**, the user decides between two diagnoses:
1. **The definition is ambiguous.** Fix the wording so that all three markets classify the same way. This produces one pair.
2. **The practice genuinely differs.** The markets list different practices under one name. The remedy is to split the security by definition, which is condition (a). Averaging the three pairs is not permitted.

---

## Section 6: The revision procedure

**Revision record contents:**
- the security identifier and the version of the old and new definition text;
- the old unit table and pair, and the new unit table and pair;
- the triggering condition, (a) or (b), and the evidence for it;
- the classifiers, with a signed statement that none of them consulted the price record or exposure series;
- the date the new pair takes effect;
- the user's ruling on each contested item.

**Initiation.** Under (a), the change to the definition is itself the initiation, and whoever proposes it opens the record. Under (b), anyone running the per-market diagnostic may open one. The user approves in every case.

**Evidence that satisfies each condition:**
- **(a):** a diff of the definition text in which a clause is added, removed or reworded, plus a unit-level diff that can be traced to that clause change. The rationale for the definition change must stand on its own and must be recorded **before** the new pair is computed. Otherwise condition (a) becomes a back door for tuning to outcomes.
- **(b):** unit tables from independent per-market runs that show the label disagreement, or a pair difference beyond tolerance.

**Readings already published.** They are never overwritten.
- **Under (a):** the old readings are readings of the previous definition. They stay as issued, tagged with the old version. The revised security continues from its effective date as a successor, linked to its predecessor.
- **Under (b):** the old pair was a misapplication. The originals stay as issued, and a **restated parallel series** under the new pair is published and clearly labelled. How well the restated series fits the record may not be used to judge whether the revision was correct.

---

## Section 7: Failure modes

Ranked from hardest to detect afterwards to easiest:

| Rank | Failure | Why it is hard to detect | Guard |
|---|---|---|---|
| 1 | **Shared anachronism on the live prong.** All classifiers judge liveness from a 2026 vantage, so options that were live in 1996 look negligible now, or the reverse. | Independent panels agree, so no signal of disagreement appears. | Classify the practice in the defined, unassisted form. Include at least one classifier whose evidence base is era-specific. |
| 2 | **Weights and exposure sorted by different rules.** | Each side is internally consistent, yet the product is systematically wrong. | Make the Section 2 test the shared sorting rule for both, and audit that it is used that way. |
| 3 | **Outcome leakage.** Classifiers have seen prices, or the definition is edited to move the weights. | Nothing in the output reveals it, only the process record. | Blind classifiers, rationale recorded before computation, signed statement in every revision record. |
| 4 | **Clause wording steering mass.** | The pair looks principled because it follows mechanically from the text. | Normalization check, plus an audit of each clause's granularity against the others. |
| 5 | **Cross-market differences that cancel out.** | The pairs match. | Compare markets at the unit level (Section 5). |
| 6 | **The binary sort hiding a real difference of degree.** | This is a known, intended distortion, but it can conceal a case that should have been split. | Record the number of live options per unit as an annotation for exposure measurement. |
| 7 | **False precision.** Decimals reported finer than the grid. | Easy to see. | Report only on the grid, with the tolerance stated. |
| 8 | **A single unit mislabelled.** | It surfaces as a disagreement between panels. | Reconciliation by prong (Section 4). |

---

## Objections

Fixed point 2 leaves the third hard case measured nowhere. A system that interprets another person's message before the person reads it does not take over a decision, so it is not substitution. It does not restore anything either, so it is not arrival. As a result, the model gives it no reading, even though it may be the most characteristic change of the late period. I have designed around this as given: the unit stays judgment and carries a "narrowing-exposed" annotation. The gap is still real. It cannot be closed inside the weights. It can only be closed on the exposure side, by a measure of partial substitution that fixed point 2 as currently written does not authorize.