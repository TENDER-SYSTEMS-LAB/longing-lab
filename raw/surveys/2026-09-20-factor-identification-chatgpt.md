## Section 1 — The identification frontier

**The specification does not determine a maximum number of separately identifiable economic factors. It determines several conditional dimensional limits. Those limits are not interchangeable.**

The critical distinction is between identifying a **return subspace**, identifying **named economic mechanisms**, and recovering **each mechanism’s contribution in a particular week**. A model can identify the first without identifying the second, and identify a mechanism’s parameters without precisely recovering every realization of its shocks.

I use the following assumptions where necessary: prices are positive, so attribution can be expressed in log returns; the panel is balanced unless otherwise stated; and approximately 1,565 observations means 1,565 potential weekly observations, not 1,565 independent technology shocks. “Priced” means receiving a separately estimated return-attribution line—not demonstrating a nonzero expected risk premium.

### The conditional limits

Write the return vector, after subtracting any **independently known** accounting contributions, as

$$
y_t=Bf_t+\varepsilon_t,
\qquad y_t\in\mathbb R^{33}.
$$

For contemporaneous recovery of unrestricted latent factor realizations, with known loadings and no noise, the condition is

$$
\operatorname{rank}(B)=K.
$$

Consequently, \(K\leq33\). With noise, separating the signal from noise additionally requires restrictions on their distributions or dynamics; full loading rank alone does not accomplish that.

| Source of variation                     |                                                                          Algebraic capacity | What the number does—and does not—establish                                                                                                                                       |
| --------------------------------------- | ------------------------------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Eleven practices within one market      | Eleven return directions; ten relative directions after removing that market’s common level | Eleven distinct loading patterns can fit eleven observations. That does not establish eleven economic causes or distinguish them from eleven security-specific disturbances.      |
| Three markets for one practice          |                             Three return directions; two independent cross-market contrasts | There are two independent ways for that practice to differ between countries. This does not mean that the entire universe supports only two country-sensitive mechanisms.         |
| All thirty-three securities jointly     |      Thirty-three return directions; thirty-two after removing an unrestricted common level | This is the ceiling for unrestricted contemporaneous linear shock recovery through the return vector—not a universal factor-count ceiling.                                        |
| Independently observed factor histories |                                       Limited by the rank of the temporal regression design | More than thirty-three observed drivers can have separately estimated effects if their histories provide independent variation and the regression’s identifying assumptions hold. |

The balanced panel’s geometry is exactly

$$
33
=
1_{\text{grand level}}
+
10_{\text{practice contrasts}}
+
2_{\text{market contrasts}}
+
20_{\text{practice}\times\text{market contrasts}}.
$$

These are dimensions, not economic factors. The within-market and cross-market dimensions overlap; they cannot simply be added as separate identification budgets.

Also, **subtracting a known numeraire contribution does not consume one return dimension**. Projecting out an *unknown* common movement does. “Thirty-three minus the number of existing ledger lines” is therefore not a valid general calculation.

### Why even thirty-three is not a statistical factor-count answer

When both \(B\) and \(f_t\) are unknown,

$$
Bf_t=(BH)(H^{-1}f_t)
$$

for every admissible invertible matrix \(H\). The data may identify the factor space while leaving its economic orientation unidentified. Sign and scale normalizations do not, by themselves, supply names such as “trust” or “attention scarcity.” This is the standard rotational-indeterminacy problem. Bai–Ng’s factor-estimation results concern recovery of the factor space under their large-\(N\), large-\(T\) conditions, not automatic identification of economically named factors. ([Columbia University][1])

Noise restrictions matter just as much. If \(\varepsilon_t\) may contain arbitrary common movements, any proposed factor can be absorbed into it:

$$
Bf_t+\varepsilon_t
=
\varepsilon_t^*.
$$

The number of factors is then unidentified.

A more restrictive model produces a different ceiling. In **static Gaussian covariance-only factor analysis**, with unrestricted loadings, factor covariance normalized to identity, and unknown diagonal idiosyncratic covariance, the Ledermann parameter-count condition is

$$
33K+33-\frac{K(K-1)}2
\leq
\frac{33(34)}2.
$$

The largest integer satisfying it is **25**. This is a model-specific counting bound, not evidence that twenty-five named factors are recoverable here. Restricted loadings, external measurements, or dynamic information change the problem. 

### When factors can outnumber securities

There are at least two relevant cases.

**Observed drivers.** In a time-series regression with \(K\) observed factor histories, identification of their coefficients requires the residualized factor-history matrix to have rank \(K\), together with the relevant exogeneity or instrumental-variable conditions. The number of securities need not exceed \(K\). Roughly 1,565 weeks creates substantial *possible* temporal capacity, but says nothing about how many independent histories actually exist.

**Dynamic states.** For a known linear system

$$
f_{t+1}=Af_t,\qquad y_t=Bf_t,
$$

a state dimension exceeding thirty-three can be observable when

$$
\operatorname{rank}
\begin{bmatrix}
B\\BA\\ \vdots\\BA^{K-1}
\end{bmatrix}
=K.
$$

That is the Kalman observability condition. It concerns distinguishability of states through their trajectories. With unknown stochastic innovations entering every week, it does not imply exact recovery of arbitrarily many new shocks from thirty-three contemporaneous returns; unknown dynamics and economic labels also require identification. ([MathWorks][2])

Time-series-only identification is **not automatically confounded with everything slow-moving**. Two slow histories can be distinguishable. The failure occurs when their observable implications coincide, or when the allowed trends and disturbances can absorb their differences. Conversely, turning a monthly series into weekly interpolations does not create new independent identifying variation.

**Binding constraint:** for unrestricted contemporaneous latent shock recovery, joint cross-sectional loading rank binds before the stated time dimension. For the broader economic-factor question, the binding constraint cannot be located from the counts: the specification supplies neither the exposure matrix nor the independent temporal innovations and noise restrictions needed to determine it.

---

## Section 2 — What the three-market structure buys, exactly

**Three markets create additional opportunities for identification. They do not, by themselves, establish a structural separation between local and common causes.**

### When the claim holds

Consider

$$
y_{m,t}=B_m^Gg_t+B_m^L\ell_{m,t}+\varepsilon_{m,t},
$$

where \(g_t\) is global and \(\ell_{m,t}\) is market-specific.

One sufficient route is that the loadings are independently anchored, the combined loading matrix has the required rank, and the error process is separately characterized. With unknown loadings, further restrictions must identify the global and local blocks and resolve rotations within them.

A covariance-based route illustrates the assumptions involved. If local innovations are mutually uncorrelated across markets, are uncorrelated with global innovations, and cross-market residual covariance is excluded, then

$$
\operatorname{Cov}(y_{m,t},y_{n,t})
=
B_m^G\Sigma_G(B_n^G)',
\qquad m\neq n.
$$

Cross-market covariance then isolates the global component **under those restrictions**. Shared practice-specific shocks must also be represented: a film-photography shock affecting all three listings is cross-market, but not necessarily universe-wide.

Hierarchical factor models make precisely this distinction between within-block and between-block variation. They also show why defining a local component as whatever is orthogonal to the global component is not equivalent to identifying an unrestricted local economic cause. ([뉴욕 연방준비은행][3])

The staggered technology arrivals provide another route. They can distinguish technology exposure from calendar time when the same practice is observed at different adoption stages. A causal interpretation additionally requires an admissible counterfactual: comparable untreated evolution, appropriate treatment of anticipation and spillovers, and separation from other changes coinciding with arrival. Staggered timing alone is not an instrument. These are identification conditions in staggered-adoption difference-in-differences designs, not consequences of having three country labels. ([arXiv][4])

### When the claim fails

**Replicated exposures.** If the additional markets merely repeat the same exposure rows,

$$
B_{\text{three markets}}
=
\mathbf1_3\otimes B_{\text{one market}},
$$

their stacking does not increase loading rank. Independent measurement errors can make estimation more precise, but cannot create a missing exposure contrast. Country-specific factor histories can add temporal information; that is a separate benefit.

**Global–local overlap.** A uniform global loading equals the sum of three uniform country loadings. Four unrestricted weekly contributions with those supports cannot be uniquely recovered from their sum. Restrictions on independent shock distributions might identify four variance components, but that is not the same as recovering four weekly shock realizations.

**Unrestricted correlated local shocks.** A movement common to the countries can be represented as a global shock or as correlated national shocks. Without restrictions or external anchors, these are alternative descriptions of the same observations.

**Phase–country confounding.** Different arrival dates do not isolate arrival effects if each arrival coincides with unrestricted country-specific changes. Allowing arbitrary country-by-week effects can absorb the entire proposed adoption signal.

### What convergence does

The supplied correlations, approximately \(+0.2\) early and \(+0.9\) late, do not determine an identification cutoff.

For illustration only, if the three standardized market returns have equal pairwise correlation \(\rho\), their correlation matrix has eigenvalues

$$
1+2\rho,\qquad 1-\rho,\qquad 1-\rho.
$$

At \(0.9\), it remains full rank. At \(1\), the two relative directions disappear. This is a statement about that hypothetical correlation matrix—not a measured factor count.

Even increasing correlation need not reduce the absolute information in country differences. Under

$$
y_{m,t}=g_t+\ell_{m,t},
$$

increasing the variance of \(g_t\), while holding local variation fixed, raises correlation without reducing the variance of \(y_{m,t}-y_{n,t}\). The shared numeraire can also raise quoted-return correlation without eliminating local fundamental variation.

**Convergence destroys contemporaneous or local-window identification when the relevant residualized exposure or event-history columns become exactly dependent.** Near-dependence produces weak identification rather than an exact algebraic failure. If different practices retain distinct exposures, synchronized arrival dates need not eliminate identification.

Nor does convergence erase earlier information about genuinely stable parameters. For a fixed-parameter linear model,

$$
D_{\text{full}}'D_{\text{full}}
=
D_{\text{early}}'D_{\text{early}}
+
D_{\text{late}}'D_{\text{late}}.
$$

Adding late observations cannot destroy rank already present in the early design. But applying early estimates to late, drifting exposures is an invariance assumption—not fresh late-period identification.

**No calendar date for loss of identification follows from the specification.** It would be determined by the relevant rank and signal-to-noise diagnostics, not by crossing a universal correlation threshold.

---

## Section 3 — The nine lines

**The supplied specification certifies zero additional named, separately identified economic factor lines. It does not establish that the true factor count is zero. The empirically defensible number remains undetermined.**

Nine is neither excluded by the universe’s dimensions nor established by them.

### What is already mechanically distinguishable

If \(N_t\), the STANDARD RETURN unit’s value against the frozen yardstick, is independently known, then

$$
P_{i,t}=\frac{V_{i,t}}{N_t}
\quad\Longrightarrow\quad
\Delta\log P_{i,t}
=
\Delta\log V_{i,t}-\Delta\log N_t.
$$

The numeraire line therefore has an exact loading of **\(-1\) on all thirty-three securities**. Its distinguishing observable is the independently maintained \(N_t\), not a common component estimated from those securities’ returns.

It becomes inseparable from a uniform numerator movement if that independent numeraire measurement is absent. A companion index constructed from the same prices is not automatically an independent measurement; its construction must actually anchor the conversion.

This is an existing accounting line, not one of the additional nine.

### What the panel supplies for testing additional lines

Let \(u\) be a zero-sum practice contrast and \(v\) a zero-sum market contrast. Using fixed orthogonal contrast bases, the panel supplies the following complete reporting geometry:

| Reporting component          | Independent dimensions | Observable that isolates the coordinate             | Loadings and signs                                                                      |
| ---------------------------- | ---------------------: | --------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Grand movement               |                      1 | Average return across all securities                | Same positive loading on all thirty-three                                               |
| Practice contrasts           |                     10 | Differences between three-market practice averages  | Loading \(u_p\), identical across the three listings of practice \(p\)                  |
| Market contrasts             |                      2 | Differences between eleven-practice market averages | Loading \(v_m\), identical across the eleven listings in market \(m\)                   |
| Practice–market interactions |                     20 | Double-centered practice-by-market returns          | Loading \(u_pv_m\); positive where the contrast signs agree, negative where they differ |

These coordinates distinguish **where** a movement occurs. They do not distinguish **why** it occurs. A saturated thirty-three-coordinate decomposition also reproduces noise.

For a coordinate to become an economic factor line, an observable or identifying restriction must distinguish its cause from every alternative cause permitted to have the same pattern.

The arrival–substitution narrative does not yet supply that distinction. It specifies a qualitative sequence, but not independent phase measurements, practice-level exposure magnitudes, or a rule separating direct price effects from float-mediated effects. A positive arrival phase and a negative substitution phase can be parts of one impulse response rather than two independent factors.

Likewise, practice names do not determine signs. Film photography may respond differently to technical substitution, scarcity, and preservation demand. Assigning those responses requires a valuation mapping or evidence.

Accordingly:

* **Opening-period additional factor count:** undetermined; none is individually certified by the brief.
* **Late-period additional factor count:** undetermined; none is individually certified by the brief.
* **Early-to-late change date:** undetermined.

A further distinction matters: a retrospective 1996 attribution estimated using the full thirty-year history is not an attribution identifiable with information available in 1996. The opening ledger’s information set must be specified.

---

## Section 4 — The promotion schedule

A runnable promotion rule needs two gates: **structural distinguishability** and **adequate estimation precision**. Statistical significance alone is not the first gate.

### Structural gate

Each declared factor needs a registered measurement definition, exposure specification, admissible dynamics, noise assumptions, and a statement of whether it represents a primitive shock or a downstream pathway.

For an anchored linear attribution model, let \(d_j\) be the stacked security-by-week contribution regressor for candidate \(j\). Let \(D_{-j}\) contain all competing factor regressors and unknown nuisance contributions. After whitening by the stipulated error covariance, define

$$
I_{j\mid -j}
=
d_j'
\left(I-P_{D_{-j}}\right)
d_j.
$$

Here \(P_{D_{-j}}\) is projection onto the competitors’ span.

If \(I_{j\mid -j}=0\), the candidate is exactly aliased and cannot receive a separately estimated coefficient. If it is positive but very small, the coefficient is weakly distinguished.

This uses the **entire security-by-time signature**, not merely correlations between factor time series. It therefore permits identification through exposure differences, temporal differences, or both.

For latent or nonlinear models, the corresponding test examines the normalized observable-distribution mapping: local rank conditions, parameter profiles, and searches for distinct parameterizations yielding the same observable law. Local identification is not sufficient to rule out distant equivalent solutions.

### Precision and pricing gate

Conditional on structural identification, promotion passes only when all registered tests pass:

1. The conditional contribution is distinguishable from zero at the institution’s declared error-control level.
2. The contribution’s uncertainty interval is narrower than the declared attribution tolerance.
3. Simulations show adequate power to recover a contribution of the declared minimum economically reportable size.
4. The result survives the registered nuisance models, dependence structure, and chronological validation procedure.

Those tolerances are institutional decision parameters, not facts derivable from thirty-three securities. Once fixed, the rule is mechanical. Without them, “strong enough to price” remains undefined.

The tests must be **joint**. Testing candidates one at a time against a sparse baseline can promote several aliases. If different candidate subsets produce indistinguishable named allocations, the test returns an equivalence class rather than selecting whichever entered first.

For a fixed anchored linear design, the available number of additional independent contribution directions is

$$
r_{\mathrm{additional}}
=
\operatorname{rank}[C,D]
-
\operatorname{rank}(C),
$$

where \(C\) contains unknown existing contributions and nuisance terms. This counts distinguishable combinations, not necessarily individually named factors.

**A listing triggers promotion only when its new observable signature breaks an existing ambiguity or supplies enough independent precision to pass the gate.** A duplicated exposure row need not add rank. Consequently, the schedule depends on listing composition, realized variation, and the observation system—not on security count alone. Current-window qualification can also disappear without any delisting.

---

## Section 5 — What this universe cannot identify

**The permanent exclusions are exposure equivalences, not a list of evocative factor names.**

The eleven practice labels do not establish the exposure equalities needed to declare a particular economic concept permanently unidentifiable. Nor do they establish that the equalities are absent.

### The exact listing test

Suppose \(H_U\) maps candidate factor histories into all permitted observations for the listed universe \(U\), including any independently observed fundamentals and floats.

If an admissible nonzero perturbation \(a\) satisfies

$$
H_Ua=0,
$$

then two factor histories separated by \(a\) produce the same observations. They cannot be distinguished by estimation on this observation system.

For unrestricted contemporaneous factor histories, this reduces to the familiar loading nullspace. With dynamic restrictions, the relevant operator includes the observable lag responses and the set of admissible histories.

A listing change breaks that particular ambiguity only when its added measurement rows satisfy

$$
H_{\mathrm{new}}a\neq0.
$$

**More securities help only insofar as they observe a direction currently hidden.** To resolve several ambiguities, the added rows must eliminate the relevant nullspace, not merely increase the row count.

### Named mechanisms and the precise equivalences that would exclude them

The following are conditional exclusion diagnoses, not assertions that the missing exposure equalities have already been measured. The listing changes describe the contrasts required to break each equivalence; they do not alter the fixed universe used elsewhere in this answer.

| Plausible mechanisms                                                | Exact condition under which this universe cannot separate them                                                                                                                                                  | Listing contrast that would break that equivalence                                                                                                                                                                                               |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Time scarcity versus effort/friction valuation**                  | Their exposure vectors are proportional across all thirty-three listings, and no independent measurements or distinguishable dynamics identify the two histories. Only their combined contribution is observed. | Exposure to duration must vary independently of exposure to effort—for example, contrasting long passive involvement with brief effort-intensive involvement, with the other relevant attributes controlled.                                     |
| **Mediation versus human substitution**                             | Every observable increase in mediation is bundled with the same proportional reduction in the need for another person, so both channels have the same observable signature.                                     | A contrast in mediation while the continued necessity of another person is held fixed, or the converse.                                                                                                                                          |
| **Generalized trust versus social contact opportunity**             | Letters, calls, visits, and other affected practices carry indistinguishable exposures to willingness to trust and opportunity to interact; the available observations record only their joint effect.          | Listings separating the availability of contact from willingness to accept vulnerability within available contact.                                                                                                                               |
| **Scarcity revaluation versus cultural attachment or nostalgia**    | On the affected listings, both are assigned the same exposure pattern and temporal driver—for example, the same decline in outstanding attention—with no independent identifying variation.                     | A contrast where scarcity differs at comparable attachment, or attachment differs at comparable scarcity. Merely adding another jointly scarce-and-cherished listing does not help.                                                              |
| **Public legibility/status versus private attachment**              | Each practice listing aggregates public and private enactments in a way that permits both explanations to generate the same observed price and fundamental history.                                             | Matched public-versus-private exposure within otherwise comparable enactments, with observable distinctions in the loading definitions.                                                                                                          |
| **Infrastructure viability versus a practice-specific disturbance** | The infrastructure factor affects exactly one practice’s three country listings, and the residual model permits an unrestricted shared shock to that practice.                                                  | A loading pattern that crosses practice identity: infrastructure exposure shared across distinct practices, or differing infrastructure exposure within a practice, so that infrastructure and practice shocks no longer have identical support. |

Several existing practices might already supply some of these contrasts. Unplanned calls retain another person while being technologically mediated. Physical media and unarranged visits do not have identical material and interpersonal characteristics. Private reflection potentially differs from publicly displayed practices.

But **a descriptive difference is not an established zero loading**. These observations identify places to examine the exposure map; they do not settle its rank or the signs of its entries.

Replication across countries cannot repair a proportionality that remains proportional in every country. It can repair the ambiguity when the country dimension actually changes the relevant exposure ratios or provides independently anchored temporal variation.

### Three failures that cannot honestly be assigned a listing-only remedy

**An unanchored numeraire.** If only relative prices \(P_i=V_i/N\) are observed, the transformation

$$
V_i^*=cV_i,\qquad N^*=cN
$$

leaves every quoted price unchanged. More listings in the same unanchored unit do not resolve this. The remedy is an independent anchor. The stipulated frozen yardstick can provide one only insofar as its measurement genuinely supplies that anchor.

**Issuance versus redemption from float balances alone.** The identity

$$
Q_t-Q_{t-1}=I_t-R_t
$$

does not identify the two gross flows. Replacing \((I_t,R_t)\) with \((I_t+h_t,R_t+h_t)\) preserves the balance. Additional balance-only listings do not identify the original listing’s gross flows without further cross-equation restrictions. Flow observations, not merely another security, distinguish them.

**A factor versus an unrestricted disturbance with the same observable effects.** If the residual class may reproduce the candidate’s full cross-sectional and temporal signature, adding listings while allowing the same unrestricted residual freedom does not identify the factor. Restrictions or independent measurements are required.

These distinctions matter because there are two different statements:

> “The current listing does not expose this difference.”

and

> “The observation and disturbance definitions do not distinguish this difference.”

The first can be resolved by an appropriate listing contrast. The second is not necessarily resolved by listing changes at all.

Therefore, no unconditional semantic blacklist—“trust cannot exist,” “scarcity cannot exist,” or “mediation cannot exist”—follows from the fixed universe. What can be established is the nullspace of its registered observable signatures. That is the precise boundary implied by listing-dependent factor availability.

---

## Section 6 — Double counting

**A shared capability series does not itself imply double counting. Counting the same price pathway more than once does.**

For illustration, let capability be \(C\), substitution \(S=S(C)\), float \(Q=q(S,C)\), and log numerator value \(v=v(C,S,Q)\). Then

$$
\frac{d\log P}{dC}
=
-\frac{dn}{dC}
+
\frac{\partial v}{\partial C}
+
\frac{\partial v}{\partial S}\frac{dS}{dC}
+
\frac{\partial v}{\partial Q}
\left(
\frac{\partial q}{\partial C}
+
\frac{\partial q}{\partial S}\frac{dS}{dC}
\right).
$$

The same capability innovation can legitimately affect all these paths. The error is to report its total effect and then add effects already included inside that total. This is the distinction between total, direct, and mediated effects; causal interpretation of the separated paths requires additional identification assumptions beyond an accounting decomposition. 

The identifiable collision points are:

| Collision                                                            | How double counting arises                                                                                                                                                   | Condition that prevents it                                                                                                                     |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Numeraire revision versus efficiency/time-compression factors**    | A broad technology factor is fitted to quoted returns and absorbs denominator appreciation, while the denominator effect is also printed separately.                         | The exact denominator contribution is removed once. Any additional factor represents a separately identified numerator pathway.                |
| **Substitution versus float-mediated scarcity or withdrawal**        | The substitution line measures the total effect of substitution, including redemption and float consequences, while a float-related factor adds the same consequences again. | Substitution is explicitly direct-only, or its mediated effects are nested within its total rather than added alongside it.                    |
| **Float change versus a fundamental already constructed from float** | Float enters the fundamental valuation, then the same float-driven valuation change receives another factor attribution.                                                     | Every valuation input and transformation has one place in the additive accounting map.                                                         |
| **Technology-wave totals versus their channels**                     | Smartphone, messaging, or AI lines contain the same effects already attributed to arrival, substitution, numeraire, or float.                                                | Wave labels identify sources, while channel allocations partition their consequences; source totals and channel totals are not added together. |
| **Global factors versus national versions of the same movement**     | A national total includes the global movement, and both are added.                                                                                                           | The national contribution is explicitly incremental to the global contribution under a stated decomposition.                                   |
| **Positioning versus reflexive amplification**                       | Positioning is measured as its full price effect including feedback, while reflexivity adds that feedback again.                                                             | Initial impact and incremental feedback are separately defined in the dynamic structural accounting.                                           |
| **Float-driven index-weight changes versus security returns**        | An index composition effect is attributed as though it were another movement in the constituent’s own price.                                                                 | Constituent-price attribution and index-weight/rebalancing attribution remain separate accounting objects.                                     |

Two qualifications are essential.

First, the float is an attention balance. The specification does **not** establish that it is a share count dividing total value. Neither a \(1/Q\) price formula nor a universally positive scarcity loading follows from its definition.

Second, a first-order derivative decomposition need not sum exactly over a finite weekly change in a nonlinear model. Exact reconciliation requires a stated finite-change allocation rule, including interaction effects. Such a rule can make the arithmetic exact without making the causal allocation uniquely identified.

`Unexplained` therefore cannot automatically be interpreted as pure idiosyncratic noise. It may include measurement error, omitted mechanisms, unidentified shared movements, and unallocated nonlinear terms.

---

## Section 7 — What would settle it

A runnable procedure is an **identification-and-recovery experiment**, followed by estimation on the actual generated observation panel. Its output is a set of identified distinctions and unresolved equivalences, not a preference ranking.

### Establish the actual observation boundary

The input manifest records which quantities are genuinely available to the estimator: weekly quotes, numeraire vintages, float balances, gross flows where logged, independent fundamental measurements, technology-arrival and substitution measurements, and positioning or feedback observations.

A variable being stored inside the generator does not make it an observed variable. Generator truth can be retained for scoring while withheld from estimation.

Publication frequency and measurement frequency are recorded separately. A weekly strike calculated from unchanged monthly inputs is not treated as new independent evidence about those inputs.

### Compile each candidate into observable restrictions

Each candidate architecture supplies its measurement equations, exposure restrictions, allowed dynamics, admissible residual covariance, and attribution ownership rules.

The experiment first searches for exact equivalences: duplicate signatures, loading nullspaces, unobservable dynamic directions, and alternative parameterizations producing the same observable distribution. An exact equivalence cannot be repaired by a favorable fit statistic.

### Run recovery experiments across admissible worlds

All simulations retain the fixed eleven practices, three markets, and 1996–2026 span.

Unspecified quantities—shock strengths, measurement errors, persistence, and exposure drift—are explicit simulation inputs swept over ranges, not presented as measurements. Histories include cases with additional factors absent, present and distinguishable, aliased, or hidden inside shared practice disturbances.

Convergence is generated through distinct mechanisms: growing global variation, shrinking local variation, synchronized exposures, and increasing shared numeraire variation. These can have similar headline correlations but different identification consequences.

Every candidate is fitted to histories generated under alternative candidate structures as well as its own. Recovering a model from data generated only by itself tests implementation, not discrimination.

### Validate in time and across the panel

Estimation uses chronological training and validation windows. Entire event episodes remain intact rather than being randomly divided across training and testing. Leave-one-market or leave-one-practice exercises test transportability of the registered exposure restrictions.

Where staggered events are used causally, the estimand and comparison groups are explicit. Ordinary two-way fixed-effects event studies can mix heterogeneous cohort effects; Sun–Abraham establish that this contamination occurs under staggered timing with heterogeneous treatment effects. A fitted lead or lag is not automatically the mechanism it is labeled to represent. ([arXiv][5])

### Produce an identification report

For each candidate line and each historical window, the report contains its conditional rank contribution, weakest identified direction, uncertainty in its weekly attribution, false-promotion rate, recovery power, and sensitivity to the registered nuisance alternatives.

It also reports whether indistinguishable candidate architectures disagree on named contributions despite agreeing on total returns. That is direct evidence against separate named identification.

Factor-number criteria can contribute a statistical dimension diagnostic. Bai–Ng consistency, however, relies on their large-panel assumptions and specified factor/error conditions; it is not a finite-sample certificate for nine economic names in a thirty-three-security panel. ([Columbia University][1])

The decisive outcomes are **distinguished**, **weakly distinguished**, **observationally equivalent**, or **not exposed by the current observation system**. Multiple largest surviving architectures may remain, with the same identifiable combinations but different labels.

No such estimation has been run here: the prompt supplies a design and qualitative histories, not the observation panel or executable measurement specification. The procedure above would determine the missing count and the historical intervals over which it is supportable.

---

## Section 8 — Refusals

I declined to supply nine named factors, a smaller asserted “correct” set, numerical loading signs unsupported by a valuation rule, or a calendar date at which convergence removes factors. Those quantities do not follow from the information supplied. The dimensional limits and conditional identification failures do.

I also declined to declare particular semantic concepts unidentifiable under **every** possible model. Independent measurements, valid identifying restrictions, or distinguishable dynamics can change that conclusion without changing the securities. Where listing changes alone cannot resolve a failure, Section 5 states that explicitly.

There are two framing issues.

First, identification is a property of **the listed exposures, the observation system, and the admissible structural and disturbance models together**. The listing is a precondition for expressing a priced effect, but the number and names of listings do not fully specify the identification design.

Second, the largest identifiable subspace need not have a uniquely identifiable economic basis. A universe can support nine independent return directions while supporting no unique assignment of nine economic names.

**The result of this round is therefore a conditional frontier: thirty-three contemporaneous return dimensions; additional identification potentially available through anchored temporal information; no established count of named additional factors; and a precise nullspace-and-recovery test for determining which distinctions the fixed universe can sustain.**

[1]: https://www.columbia.edu/~sn2294/pub/ecta02.pdf "FRANJBLACKECTA8-1ECTA358"
[2]: https://www.mathworks.com/help/control/ref/statespacemodel.obsv.html "obsv - Observability of state-space model - MATLAB"
[3]: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr412.pdf "Dynamic Hierarchical Factor Models"
[4]: https://arxiv.org/abs/1803.09015 "[1803.09015] Difference-in-Differences with Multiple Time Periods"
[5]: https://arxiv.org/abs/1804.05785?utm_source=chatgpt.com "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects"
