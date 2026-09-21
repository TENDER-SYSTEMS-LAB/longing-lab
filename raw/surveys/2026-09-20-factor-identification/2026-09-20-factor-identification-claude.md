# LONGING: Factor Identification Round 4

Assumptions are marked **[A]** and judgements **[J]**. Wherever the specification is silent, I say so rather than fill the gap.

## Section 1 — The identification frontier

There is no single maximum. The number depends on how a factor enters the ledger, and the specification does not say which of three modes applies.

- **Latent factors recovered from covariance alone.** The Ledermann bound limits an exact factor model with diagonal idiosyncratic covariance to K factors where (N−K)² ≥ N+K. At N = 33 this gives K ≤ 25. The bound is an algebraic ceiling, the factors are identified only up to rotation (K² restrictions are needed to name them), and the consistency results for approximate factor models (Chamberlain–Rothschild, Bai–Ng) assume N→∞. At N = 33 only strongly pervasive factors separate from the idiosyncratic eigenvalues.
- **Factor realizations inferred each week from that week's cross-section** (Fama–MacBeth style). Here K ≤ rank(B), where B is the 33×K loading matrix. Pooled with an intercept that is ≤ 32. Within one market it is ≤ 10.
- **Factors as observed, declared series** (wave indices per market). Loadings then come from time-series regression, and K is limited by the collinearity of the factor paths, not by N. The author's first position holds in this mode, and only in this mode.

**By source of variation.** The 33 securities form an 11×3 layout whose weekly degrees of freedom split as follows:

| Component | Degrees of freedom |
|---|---|
| Global mean | 1 |
| Practice effects | 10 |
| Market effects | 2 |
| Practice × market interaction | 20 |

- *Cross-sectional variation within a market* can carry at most 10 dimensions. How many are usable depends on the dispersion of authored loadings across the eleven practices, which is not given, so the usable rank cannot be determined.
- *Cross-market variation in the same practice* gives three observations per practice, hence **two** contrasts. However many "local" factors are declared, they live in a two-dimensional market space crossed with practice loading patterns. The 20 interaction dimensions are where idiosyncratic noise also lives. A factor there is separable from noise only if its loading pattern is specified in advance and persists.
- *Time-series-only variation* covers anything common to all markets and smooth: the numeraire drift, late-wave substitution, float decay, cohort replacement. Merton (1980) shows that finer sampling improves estimates of second moments, while the precision of drift estimates depends on span. For slow factors, 1,565 weeks therefore do not count as 1,565 observations. The effective sample is the number of distinct arrival events, which is at most seven waves × three markets, and fewer once late arrivals coincide.

**The binding constraint is the time-series one.** The drivers of this world are S-curves that share a capability origin. They are nearly collinear in time, and no number of securities fixes that. Cross-market stagger relieves the constraint where stagger exists. The 11-practice cross-section relieves it only where authored loadings differ between waves.

## Section 2 — What the three-market structure buys, exactly

**When the claim holds.** Write r(p,m,t) = β_p·g_t + γ_p·l(m,t) + ε. Global and local factors separate if three conditions hold:

1. A practice's loading on a wave is the same in every market, or differs in a known way.
2. Local realizations are not perfectly correlated across markets.
3. The stagger in arrival dates exceeds the wave's own rise time. A stagger shorter than the S-curve's width identifies nothing.

This is a staggered event-study design, so it also needs no anticipation and parallel paths in the absence of the wave.

**When the claim fails.**

- *Heterogeneous loadings across markets.* With three units, the staggered two-way design does not identify a common effect (the Goodman-Bacon and de Chaisemartin–D'Haultfœuille results on heterogeneous treatment effects).
- *Three clusters.* Each wave has one arrival ordering out of 3! = 6, so a permutation test on a single wave cannot produce p < 1/6. Inference comes only from pooling waves, and only if the orderings differ between waves. **[A]** The specification does not give the orderings. If one market always leads, arrival order is collinear with that market's own slow trends and nothing is identified.
- *Convergence.* For three equicorrelated, equal-variance series the eigenvalues are 1+2ρ (common) and 1−ρ (twice). At ρ = 0.2 these are 1.4, 0.8, 0.8, so the contrasts carry 53% of the variance. At ρ = 0.9 they are 2.8, 0.1, 0.1, so the contrasts carry 6.7%. The local signal falls eightfold in variance terms.

**Stated plainly, convergence destroys two things and spares one.**

- It spares loadings on early waves. If they are time-invariant, the staggered period estimates them and they carry forward.
- It destroys the week-by-week estimation of late local realizations.
- It destroys, entirely, the identification of loadings on waves that arrive coincidentally (smartphones, messaging and AI, under **[A]**). Those waves were never staggered, so their loadings are time-series-only.

**When.** The break is the last wave whose stagger exceeds its rise time, which cannot be dated from the specification. It also cannot be determined whether ρ = 0.9 reflects local shocks shrinking in absolute terms or global variance growing. In the first case the local line is zero by definition. In the second case the local factor is real but unmeasurable. The absolute variance path of the two market contrasts would decide between them.

## Section 3 — The nine lines

The lines below are derived by identification source, and the labels are **[J]**. The practice grouping is **[J]**: contact (letters, unplanned calls, unarranged visits, waiting), state (solitude, boredom, night walks, private reflection), material (film, physical media, handmade). It can be replaced by the leading principal components of within-market demeaned returns, which are identified only up to rotation. All lines are defined on frozen-yardstick returns.

| # | Line | Distinguishing observable | Loadings | Becomes unidentifiable when |
|---|---|---|---|---|
| 1 | Global common | The equal-weight mean of all 33, net of numeraire | All securities, + | It is defined on headline returns, where it duplicates the numeraire line |
| 2 | Contact vs state | A cross-sectional contrast present in every market | Contact 12 +, state 12 − | The two groups' loadings on all waves coincide |
| 3 | Material vs rest | The same, for the material group | Material 9 +, other 24 − | It is inseparable from a revival effect (see Section 5) |
| 4–6 | Arrival lines for staggered waves **[A: dial-up, mobile, broadband]** | Market-specific arrival dates | Differ by practice **[A]**: mobile raises unplanned calls and lowers waiting and unarranged visits | Stagger is shorter than rise time, or two waves share both practices and ordering (a risk for dial-up and broadband) |
| 7–8 | Residual market contrasts | Market means after lines 4–6 | All 11 practices in a market, contrast-coded | ρ is high, or a third contrast is declared (only two exist) |

A ninth line would have to come from the practice × market interaction, where each candidate rests on three or four securities and meets Round 3's two-constituent objection in only slightly weaker form.

**Early in the history** the defensible count is at most eight. It falls to six or seven if dial-up and broadband do not separate.

**Late in the history** lines 1–3 survive cleanly. One composite late-wave line can be added, identified only by time series and carrying a permanent confound flag, which gives four. Lines 7–8 survive only if their absolute variance clears the idiosyncratic variance, and that cannot be determined from the specification.

The count changes at the break defined in Section 2. It is a window, not a date, and the demotion test in Section 4 detects it.

No identification argument produces the number nine.

## Section 4 — The promotion schedule

A declared factor with loading column b and path f is promoted when every test below passes on a rolling window. The thresholds are fixed before estimation, and their values are **[J]**.

1. **Rank.** A Kleibergen–Paap rank test rejects rank([B b]) = rank(B). The ledger's line count equals the numerical rank of B, and rank rises only as new listings add rows. That is what makes the count a function of universe size.
2. **Support.** The nonzero entries of b span at least two markets and at least two practices. If they do not, b is a market effect, a practice effect, or a single security.
3. **Useless-factor guard** (Kan–Zhang). A joint Wald test rejects b = 0 before any price is attached.
4. **Path distinctness.** The partial R² of f on all existing line paths, including the numeraire and substitution lines, is below threshold.
5. **Out-of-sample.** Adding the line lowers the variance share of `Unexplained` on held-out weeks.
6. **Placebo.** The effect disappears when arrival-date market labels are permuted.
7. **Stability.** Loading signs estimated on one half of the window hold on the other half.

Demotion uses the same tests in reverse.

## Section 5 — What this universe cannot identify

1. **AI wave vs numeraire.** AI defines the unit, arrives coincidentally everywhere, and touches every practice. Separating it needs a listed practice whose fundamental is AI-insensitive, or one that AI's arrival phase raises.
2. **Smartphone vs messaging vs social web.** Arrival is coincident and the exposed practices are the same. Separating them needs a practice exposed to exactly one of the three.
3. **Arrival vs substitution within a late wave.** If the lag between the two phases is the same everywhere, the two phases trace one shape. Separating them needs practices whose lag demonstrably differs.
4. **Cohort replacement vs technological substitution.** Both are slow and monotone. Separating them needs a practice bound to age but neutral to technology, or the same practice listed by cohort.
5. **Country-level slow trends** (household structure, working hours, urban form) **vs market contrasts.** With three markets, any slow national variable is collinear with a market trend. Separating them needs more markets or sub-market listings.
6. **Practice × market specifics.** Each rests on one security and is indistinguishable from idiosyncratic noise. Separating it needs a second practice in the same market that shares the mechanism.
7. **Revival or scarcity premium vs the material contrast and the reflexive line.** Revivals occur only in the three material practices. Separating them needs a non-material practice with a revival, or a material one without.
8. **The 2020 shock.** It is one coincident global event and cannot be distinguished from a late-wave acceleration. It is an event, not a factor, under any listing.

## Section 6 — Double counting

- **Numeraire vs global or AI line.** The numeraire line has zero cross-sectional dispersion by construction. Any other line with zero dispersion duplicates it. The check: headline index minus companion index must equal the numeraire line exactly, every week.
- **Substitution line vs wave lines.** If wave lines include the substitution phase, the same movement is counted twice. Either wave lines carry the arrival phase only, or they are a sub-ledger that decomposes the substitution line and is not added to it.
- **Float vs substitution.** Redemption is the substitution mechanism. A float line may carry only issuance that is not driven by capability.
- **Positioning vs float.** The specification does not say whether these are the same balance. This cannot be determined.
- **Reflexive line vs persistent factors.** If the reflexive line is estimated on raw lagged returns, it absorbs slow-factor persistence. It should be estimated on residuals only.
- **Early wave lines vs market contrasts.** The same movement appears in both. Prevent this by sequential orthogonalization (Frisch–Waugh–Lovell) in a fixed, published order. The order is **[J]**, and because the attribution of shared variance depends on it, it should be disclosed and not hidden.

## Section 7 — What would settle it

Because the world is generated, the following can actually be run.

1. For each candidate set i, simulate the 33 × 1,565 panel with set i as the true process, imposing the stated correlation path.
2. Fit every candidate set j to each panel and select by held-out `Unexplained` share or a Bai–Ng criterion.
3. Report the confusion matrix P(select j | truth i), separately for the early window and the late window. Off-diagonal mass directly measures what the universe cannot tell apart.
4. Add two controls. One is a planted null factor with zero loadings, which gives the false-promotion rate of Section 4. The other is leave-one-market-out prediction of the third market's attribution.
5. Treat unspecified quantities (idiosyncratic volatility, stagger length, loading dispersion) as sweep parameters. The output is then a frontier: for each line, the parameter region in which it is recoverable.

## Section 8 — Refusals

**Declined**

- A single maximum factor count.
- A date for the convergence break.
- Numerical thresholds.
- Wave orderings by market.

Each of these depends on quantities the specification does not contain.

**Framing**

1. The world is authored, so the institute knows its own process. Identification here means whether a reader could recover or falsify the published ledger. It does not mean discovery.
2. The author's first position holds only when factors are declared series. It cannot hold if weekly factor realizations are inferred from the cross-section.
3. Section 3 asks for a set while the brief forbids proposing one. I resolved this by deriving identification classes and marking the labels as judgement.
4. Section 5 asks for listing changes while the brief forbids new securities. I named properties a listing would need, not securities.
5. Nothing in the identification analysis produces nine.