# Academic mathematical models: verified research notes

Date: 2026-09-06. Attribution: llm-synthesis. This is an original research record, not a reproduction of the papers. Primary PDFs and relevant equation/table pages were inspected; no author code was executed or model fitted. LONGING applications and algebraic deductions below are proposals, not author findings or user decisions. Six deliberately selected models constitute a first survey, not a systematic review. Selection emphasizes explicit mathematics, identifiable quantities, and useful failure modes rather than journal prestige.

## 1. Adoption and saturation — Bass (1969)

*A New Product Growth Model for Consumer Durables*, Management Science 15, 215–227. [DOI](https://doi.org/10.1287/mnsc.15.5.215); [primary scan](https://pdodds.w3.uvm.edu/files/papers/others/1969/bass1969a.pdf), pp. 217–222.

State Y is cumulative first buyers; flow S=dY/dt is buyers/year. Fixed market potential m is buyers; innovation p and imitation q are year⁻¹. No explicit external driver enters.

`dY/dt = [p + qY/m](m−Y)`

Annual regression uses `S_t=a+bY_(t−1)+cY_(t−1)²`, with `a=pm`, `b=q−p`, `c=−q/m`. Eleven durable-product series were chosen partly to limit replacement purchases. Table 1 home freezers (1946–1961): p=.018119, q=.17110, m=21,973 thousand units, R²=.742. Table 3's .473 curve r² is a different statistic, not held-out validation. Early estimates and market-potential inference are sensitive to limited observations. Retrospective fit does not identify causal imitation.

**LONGING deduction/proposal:** distinguish first adoption, active participation, and repeat occasions. A falling S can coexist with rising Y; this equation cannot measure abandonment. Add independently observed exits only in a separately specified model. Test against simple trend and cohort baselines on future periods; do not call q a measured social-pressure factor.

## 2. Competing practices — Abrams and Strogatz (2003)

*Modelling the dynamics of language death*, Nature 424, 900. [DOI](https://doi.org/10.1038/424900a); [author PDF](https://dmabrams.esam.northwestern.edu/pubs/Abrams%20and%20Strogatz%20-%20Modelling%20the%20dynamics%20of%20language%20death%20-%20Nature%202003.pdf), Eq. 1 and Fig. 1.

State x is one language's speaker fraction; 1−x is the other. Constant s∈[0,1] is relative status, a dimensionless response exponent, c a time⁻¹ transition scale, x₀ an initial condition.

`dx/dt = c[s(1−x)x^a − (1−s)x(1−x)^a]`

Historical fits across 42 regions used least-absolute-value regression; a averaged 1.31 (SD .25, not a standard error). The short paper does not tabulate every fitted c and x₀. Calendar-year observations include proxies and age-based historical reconstruction. Fits are retrospective. The model assumes exclusive, monolingual, well-mixed groups and fixed status; bilingualism and spatial networks are absent.

**Own derivation:** for 0<s<1, a≠1, the interior equilibrium obeys `x/(1−x)=[(1−s)/s]^(1/(a−1))`. It is unstable for a>1, stable for 0<a<1. At a=1, `dx/dt=c(2s−1)x(1−x)`. Extinction is not a conclusion for every parameter regime.

**LONGING proposal:** use only where practices genuinely compete. Measure switching and dual use before treating participation as a zero-sum share; status is not automatically technological convenience.

## 3. Persistence and feedback — Rinaldi (1996 working paper)

*Love Dynamics: The Case of Linear Couples*, IIASA WP-96-068. [Repository](https://pure.iiasa.ac.at/id/eprint/4959/); [verified working paper](https://pure.iiasa.ac.at/id/eprint/4959/7/WP-96-068.pdf), printed pp. 3–6, Eqs. 1–3. This card describes that version, not an independently checked final journal article.

`dx₁/dt=−α₁x₁+β₁x₂+γ₁A₂`

`dx₂/dt=−α₂x₂+β₂x₁+γ₂A₁`

States xᵢ are signed affection; fixed Aᵢ represent appeal. Positive αᵢ, βᵢ, γᵢ represent forgetting, response to affection, and response to appeal. Time may be months or years; affection has no operational measurement scale. Stability requires `β₁β₂<α₁α₂`. The paper provides no estimated coefficients or empirical validation and defers identification. Fixed positive feedback can produce unbounded states outside the stable region.

**Own dimensional reading:** with common affection units, α and β are time⁻¹; γ has affection/(appeal·time). Isolated decay has half-life `ln(2)/α` only after removing both input terms, including appeal.

**LONGING proposal:** retain as a transparent feedback analogy, not an empirical forgetting law. This model's dyadic affection is narrower than LONGING's waiting, chance, memory, and practices. A candidate measurement would require repeated personal reports and independently observed inputs; public attention data cannot calibrate it.

## 4. Waiting and anticipatory utility — Loewenstein (1987)

*Anticipation and the Valuation of Delayed Consumption*, Economic Journal 97, 666–684. [DOI](https://doi.org/10.2307/2232929); [author PDF](https://www.cmu.edu/dietrich/sds/docs/loewenstein/AnticipationDelayed.pdf), pp. 669–671, Eqs. 1–5, 8.

This is scheduled utility, not an autonomous state equation. Outcome x supplies flow U(x) during [T,T+L). T is waiting duration, L consumption duration, r discount rate, δ>r anticipation attenuation, α vividness intensity.

Before T: `U_a(t)=α U(x)e^(−δ(T−t))(1−e^(−δL))/δ`.

At time zero:

`U(Y)=U(x){α(e^(−rT)−e^(−δT))(1−e^(−δL))/[δ(δ−r)] + e^(−rT)(1−e^(−rL))/r}`.

Y is a money equivalent, not a traded quote. Under flow units, r, δ, α are time⁻¹. For positive U(x), initially delaying consumption is beneficial when `α(1−e^(−δL))/δ > 1−e^(−rL)`. A hypothetical willingness-to-pay survey of 30 undergraduates motivates the model; α, δ, r are not structurally estimated. No universal waiting premium is established.

**LONGING proposal:** observe actual delay separately from anticipation preferences. Test repeated valuations across controlled delays, including dread and uncertainty. An illustrative α=.2/day, δ=.5/day, r=.05/day, L=1 day satisfies the inequality; α=.01/day reverses it. These are assumed values, not estimates.

## 5. Collective attention — Candia et al. (2019; online 2018)

*The universal decay of collective memory and attention*, Nature Human Behaviour 3, 82–91. [DOI](https://doi.org/10.1038/s41562-018-0474-5); [paper](https://barabasi.com/media/pub_imports/files/995.pdf), Eqs. 1–6, 24; [supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41562-018-0474-5/MediaObjects/41562_2018_474_MOESM1_ESM.pdf), printed p. 26, Tables 1–2.

Latent communicative and recorded attention u,v sum to S. Initially u=N,v=0; p is disappearance, r transfer, q recorded decay (year⁻¹ in age-year fits).

`du/dt=−(p+r)u; dv/dt=ru−qv`

`S=N[(p−q)e^(−(p+r)t)+r e^(−qt)]/(p+r−q)`

Log-response fitting uses citation histories and cultural-goods popularity against age. Spotify estimates (SE): p=.4685 (.0516), q=.0324 (.0004), r=.2197 (.0164), N=8.4335 (.5019); pseudo-R²=.3966. N is response amplitude, not a population count. Supplement Table 1 gives Cat5 1990(1) lognormal AICc −103.2909 versus biexponential −94.3849: the latter does not win every comparison. Cultural-goods cross-sections cannot directly identify individual forgetting.

**Own deduction/proposal:** `dS/dt=−pu−qv≤0`; transfer cancels. Revival requires new inputs. Distinguish attention proxies from performed practices and personal recollection. Fit alternative curves and inspect held-out errors before interpreting the latent compartments.

## Mechanism-identification counterexample — Frank (2019)

*How to Understand Behavioral Patterns in Big Data: The Case of Human Collective Memory*, Behavioral Sciences 9, 40. [DOI and primary article](https://doi.org/10.3390/bs9040040), Eq. 1 and sections 3–5.

`m(t)=[e^(−at)+c e^(−bt)]/(1+c)` reproduces the normalized Candia curve with `a=p+r`, `b=q`, `c=r/(p−q)` where that parameterization is valid. Independent pools and a cascade can generate the same aggregate curve. Aggregate goodness of fit therefore cannot choose the causal mechanism. This is a mathematical identification critique, not a new empirical refutation of Candia's data. Frank proposes interventions that disrupt a pathway to distinguish mechanisms.

**LONGING implication (LLM proposal):** an exactly reconstructed ledger is not evidence that its factors are independently identified. Require observations or interventions capable of separating explanations; preserve unresolved alternatives.

## 6. Network viability — Rohlfs (1974)

*A Theory of Interdependent Demand for a Communications Service*, Bell Journal of Economics and Management Science 5, 16–37. [DOI](https://doi.org/10.2307/3003090); [primary reprint](https://competitionpolicyinternational.com/assets/0d358061e11f2708ad9d62634c6c40ad/SchmalenseeRohlfswithCover.pdf). Rohlfs begins PDF p.14; the preceding Schmalensee introduction is separate. Reprint pp. 323–326, Eqs. 11–19; p.332, Eq.20.

Binary states qᵢ indicate subscribers. With fixed outside budgets/prices and money-normalized contact values wᵢⱼ:

`qᵢᴰ=1 iff Σ_(j≠i) wᵢⱼqⱼ ≥ p`; equilibrium requires `qᵢ=qᵢᴰ`.

p is a recurring service fee, not an asset price. Uniform calling reduces the condition to `fwᵢ≥p`, with f the user fraction. An assumed uniform w∈[0,100] yields `p=100f(1−f)` for nonzero equilibria. The maximum 25 is illustrative, not estimated. Zero adoption also persists for p>0. Adjustment has no calibrated annual speed. Costs enter a viability condition but are not empirically fitted. Group composition matters; headcount alone is generally insufficient.

**Own example/proposal:** fee16 gives fractions .2 and .8; under the example's adjustment assumptions the lower threshold is unstable. Measure contact-network membership, operating costs, and participation before borrowing this threshold. Network demand is not itself a model of physical infrastructure depreciation. Positive network benefits omit congestion and unwanted contacts.

## Scope and evidence boundary

The six cards cover named mechanisms, not an exhaustive theory of romance. Cultural transmission across generations, technological substitution with active-user exits, chance encounters, physical infrastructure retirement, contested value, and index measurement remain open. Henrich's cultural-loss model and subsequent demographic critiques are leads deferred from this bounded deliverable. No factor universe, factor-to-security count ratio, security unit, pricing law, or engine has been selected. A practice's declining prevalence does not imply declining personal value or a uniquely determined price.
