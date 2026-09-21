**Training cut-off:** February 2026. Figures or series revisions published after that date are outside what I can attest.

**Summary judgement (Section 7, stated up front):** A defensible thirty-year, three-country diffusion series can be assembled for the earlier waves — mobile telephony, fixed broadband, and internet use — using ITU/OECD administrative data and national household surveys. The social web and smartphone eras are patchier: comparable cross-country series exist for some years but not continuously, and definitions diverge substantially. For generative AI, no continuous industry-wide measured series exists in any of the three countries. A thirty-year series can be built only if the later waves are explicitly marked as constructed from heterogeneous, non-annual, non-harmonised sources, not as a single measured quantity.

---

## Section 1 — The inventory

### 1.1 Japan

| technology | series name | publisher | first year | last year | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| Dial-up / internet use (household) | Communications Usage Trend Survey — household internet penetration | MIC (Ministry of Internal Affairs and Communications) | 1990 (household survey); internet items from mid-1990s | 2025 (latest: 令和7年, published 2026-05-29) | Annual | % of households with internet access; later also % of individuals using internet | `verified` — survey conducted annually since 1990 under Statistics Act; corporate survey added 1993; household member items added 2001 |
| Mobile telephony (subscriptions) | Mobile-cellular subscriptions | ITU (World Telecommunication/ICT Indicators Database); national source: MIC / TCA | 1990 (ITU series starts); national data earlier | 2023 (ITU DataHub); national data to 2025 | Annual | Number of mobile-cellular subscriptions; postpaid and prepaid included; prepaid only if used within a fixed period (e.g. 3 months); data cards and USB modems excluded | `verified` — ITU series name and definition are documented; Japan figures reported in ITU DataHub and MIC White Paper |
| Mobile telephony (penetration) | Mobile-cellular subscriptions per 100 inhabitants | ITU / World Bank | 1990 | 2023 (ITU); 2025 (World Bank estimates) | Annual | Subscriptions per 100 inhabitants; same subscription definition as above | `verified` — World Bank series is derived from ITU; figures for Japan 1996 onward are widely published (e.g. IndexMundi reproduces World Bank data: Japan 21.25 in 1996) |
| Fixed broadband | Fixed-broadband subscriptions | ITU; national source: MIC | 1998 (ITU series) | 2023 (ITU) | Annual | Fixed broadband defined as high-speed connections ≥256 kbps in either direction; includes cable modem, DSL, fibre, satellite, fixed wireless, WiMAX; excludes mobile data contracts | `verified` — ITU definition documented in MIC White Paper; OECD also publishes fixed broadband penetration |
| Fixed broadband (OECD) | Fixed broadband subscriptions per 100 inhabitants | OECD | 2000 (approximate) | 2023 (December) | Annual | OECD definition: fixed broadband subscriptions per 100 inhabitants; includes fibre, DSL, cable, etc.; speed threshold varies by country reporting | `verified` — OECD publishes Japan at 40.8 per 100 in December 2023; OECD broadband portal is the primary source |
| Social web / social media | No single continuous national series | — | — | — | — | — | `unknown` — Japan does not publish a continuous, definitionally stable series for social media usage; MIC surveys include some platform-usage items but not a consistent penetration measure |
| Smartphone | Communications Usage Trend Survey — smartphone ownership rate | MIC | 2012 (approximately) | 2025 | Annual | % of individuals owning a smartphone; survey-based | `probable` — MIC surveys report smartphone ownership rates, but I could not verify a single continuous series name with confirmed first year |
| Messaging platforms | No national continuous series | — | — | — | — | — | `unknown` — LINE usage is reported by the vendor, not as a national statistical series |
| Generative AI | Communications Usage Trend Survey — generative AI usage | MIC | 2023 (first inclusion) | 2025 | Annual (recent) | % of individuals who have used generative AI services; survey-based | `probable` — MIC White Paper 2025 includes figures on generative AI usage by country (Figure 3-71); the series is very short and definitionally loose |

### 1.2 Korea

| technology | series name | publisher | first year | last year | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| Dial-up / internet use (household) | Survey on the Internet Usage — household internet access rate | MSIT / NIA (National Information Society Agency) | 1999 (household survey); earlier computer survey from 1986 | 2024 (December) | Annual | % of households with internet access; also % of individuals using internet | `verified` — NIA publishes annual survey; OECD metadata notes the survey was called “Survey on the Computer and Internet Usage” before 2009 |
| Mobile telephony (subscriptions) | Mobile cellular telephone subscriptions | MSIT / KCC (Korea Communications Commission); also ITU | 1984 (analogue); digital from 1996 | 2024 (KCC); 2023 (ITU) | Annual | Number of mobile subscriptions; multiple SIMs counted separately; includes M2M? | `verified` — NIA “ICT Statistics at a Glance” cites KCC “Wired and Wireless Communications Service Subscription” as source for mobile cellular telephone subscriptions |
| Mobile telephony (penetration) | Mobile cellular subscriptions per 100 people | ITU / World Bank | 1990 | 2023 (ITU); 2026 (World Bank estimate: 173 per 100) | Annual | Subscriptions per 100 inhabitants | `verified` — ITU/World Bank series for Korea is continuous; IndexBox reports 173 per 100 as of 2026 |
| Fixed broadband | Fixed (wired) broadband subscriptions | KCC; also ITU and OECD | 1998 (ADSL launch); ITU series from 2000 | 2024 (KCC); 2023 (ITU/OECD) | Annual | Number of fixed broadband subscriptions; KCC counts active subscriptions; ITU threshold ≥256 kbps | `verified` — NIA cites KCC “Wired and Wireless Communications Service Subscription”; OECD reports Korea at 46.6–47.3 per 100 in 2023–2024 |
| Fixed broadband (OECD) | Fixed broadband subscriptions per 100 inhabitants | OECD | 2000 (approximate) | 2024 | Annual | OECD harmonised definition | `verified` — OECD broadband portal |
| Social web | No continuous national series | — | — | — | — | — | `unknown` |
| Smartphone | Survey on the Internet Usage — smartphone ownership | MSIT / NIA | 2011 (approximately) | 2024 | Annual | % of individuals owning a smartphone | `probable` — NIA reports household smartphone ownership rates (e.g. 98.3% in 2024) but I could not verify a single continuous series name |
| Messaging platforms | No national continuous series | — | — | — | — | — | `unknown` |
| Generative AI | Survey on the Internet Usage — generative AI usage | MSIT / NIA | 2024 (first inclusion?) | 2024 | Annual (recent) | % of individuals who have used generative AI | `probable` — Google/Ipsos survey (2025) reports 55% of Koreans used generative AI in 2024; NIA may include an item but I could not verify a named series |

### 1.3 United States

| technology | series name | publisher | first year | last year | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| Dial-up / internet use (household) | Current Population Survey — Computer and Internet Use Supplement | U.S. Census Bureau / NTIA | October 1994 (computer use); October 1997 (internet use) | 2023 (most recent supplement) | Irregular (varying months; roughly every 2 years since 2013) | % of households with internet access; later % of individuals; definition of “internet use” has changed over time | `verified` — CPS supplement administered in 1994, 1997, 1998, 2000, 2001, 2003, 2007, 2009, 2010, 2011, 2012, 2013, 2015, 2017, 2019, 2021, 2023 |
| Internet use (adults) | Pew Research Center — Internet/Broadband Fact Sheet | Pew Research Center | 2000 | 2025 | Annual / intermittent | % of U.S. adults who use the internet; based on telephone and online surveys | `verified` — Pew has tracked internet use since 2000; 96% of adults in 2025 |
| Mobile telephony (subscriptions) | Mobile-cellular subscriptions | ITU / World Bank; national source: FCC | 1990 (ITU) | 2023 (ITU) | Annual | Subscriptions per 100 inhabitants; ITU definition as above | `verified` — ITU DataHub series for the U.S. is continuous; FCC also publishes subscriber counts |
| Fixed broadband | Fixed broadband subscriptions | ITU; national source: FCC | 1999 (ITU series) | 2023 (ITU) | Annual | ITU definition ≥256 kbps | `verified` — ITU series; FCC Form 477 data provides more granular but different counts |
| Fixed broadband (household) | NTIA Internet Use Survey — home broadband adoption | NTIA / Census Bureau | 2000 | 2023 | Irregular (aligned with CPS supplement) | % of households with home broadband; definition of “broadband” has changed (speed thresholds, technology) | `verified` — NTIA/Census CPS supplement includes broadband adoption items; Pew reports 3% broadband adoption in 2000 rising to 77% by 2021 |
| Social web | Pew Research — social media use | Pew Research Center | 2005 | 2025 | Annual (most years) | % of U.S. adults who use social media | `verified` — Pew has tracked social media use since 2005; widely cited but survey-based, not administrative |
| Smartphone | Pew Research — smartphone ownership | Pew Research Center | 2011 | 2025 | Annual | % of U.S. adults who own a smartphone | `verified` — Pew smartphone ownership series is continuous from 2011 |
| Messaging platforms | No national continuous series | — | — | — | — | — | `unknown` |
| Generative AI | Pew Research — AI use / ChatGPT use | Pew Research Center | 2023 | 2025 | Annual (recent) | % of U.S. adults who have used ChatGPT or other generative AI | `probable` — Pew has published surveys on ChatGPT use since 2023; OECD also reports U.S. AI use (29% in 2024); no continuous administrative series |

---

## Section 2 — Definitions that do not match

### 2.1 Mobile telephony: subscriptions vs. individuals

All three countries report **subscriptions**, not unique users. The ITU definition counts each active SIM as a subscription; multiple SIMs per person are counted separately. Prepaid SIMs are included only if used within a specified period (typically 3 months). This means mobile “penetration” can exceed 100% — Japan reached ~154 per 100 by 2020, Korea ~173 per 100 by 2026, and the U.S. ~190 per 100 for mobile broadband by 2023. The three countries do not differ substantially in this convention, but the **threshold for “active”** may differ: Korea’s KCC counts subscriptions on a specific reporting date, while ITU harmonises to year-end. M2M SIM cards are counted in some Korean and U.S. figures but excluded from ITU’s mobile-cellular series; this creates a divergence between national and ITU totals for Korea and the U.S.

### 2.2 Fixed broadband: speed threshold and technology inclusion

- **ITU**: threshold is **≥256 kbps** in at least one direction; includes DSL, cable modem, fibre, satellite, fixed wireless, WiMAX; **excludes** mobile data contracts.
- **OECD**: uses a similar technology list but has historically used **different speed thresholds** across countries and reporting years. OECD’s “fixed broadband” includes fibre, DSL, cable, and other fixed technologies; the speed floor is often not explicitly stated in headline tables but is at least 256 kbps.
- **Japan MIC**: aligns with ITU definition in the White Paper.
- **Korea KCC**: counts “wired broadband” subscriptions; the definition includes FTTH, HFC, DSL, etc.; speed threshold may be higher in national reporting.
- **U.S. FCC**: Form 477 data uses a **different threshold** — historically 200 kbps, later 4 Mbps/1 Mbps, now 25 Mbps/3 Mbps — and counts connections by census block, not by household. This makes FCC figures **not directly comparable** to ITU or OECD series.

**Failure mode:** A series titled “fixed broadband subscriptions per 100” from ITU, OECD, and FCC will produce different levels for the same country in the same year because of speed thresholds and whether M2M or business lines are included.

### 2.3 Internet use: household vs. individual; survey vs. administrative

- **Japan MIC**: surveys **households** for internet access and **individuals** for usage rate. The household unit is the dwelling; the individual unit is the person. The two measures are not interchangeable.
- **Korea NIA**: surveys **households** for access and **individuals** for usage. Similar structure to Japan.
- **U.S. Census/NTIA**: CPS supplement collects data at both **household** and **person** level. NTIA reports both; Pew reports **individuals** (adults).
- **Definition of “internet use”** differs: Japan’s individual usage rate asks about use in the past year; Korea’s survey asks about use in the past month (for some items); U.S. CPS asks about use “at home, work, or elsewhere” with varying reference periods. These reference-period differences mean the three countries’ “internet penetration” figures are **not directly comparable** without adjustment.

### 2.4 Base year and population denominator

- **Penetration rates** are calculated as subscriptions (or users) divided by **population**. Japan and Korea use mid-year population estimates from their national statistical offices; the U.S. uses Census Bureau population estimates. Small differences in population base years (e.g. Japan’s census base 2020, Korea’s 2020 census, U.S. 2020 census) can shift penetration rates by a few tenths of a percentage point.
- **Household penetration** uses the number of households as denominator, not population. Japan and Korea report household penetration; the U.S. NTIA reports household broadband adoption. These are comparable in principle but the **survey sampling frames** differ (Japan: approximately 10,000 households; Korea: approximately 10,000 households; U.S. CPS: approximately 50,000 households).

### 2.5 Social web and messaging: no shared definition

There is **no harmonised definition** of “social web” or “messaging platform” usage across the three countries. Japan’s MIC reports usage rates for “social networking services” in some years; Korea’s NIA reports “SNS usage rate”; Pew reports “social media use” for the U.S. The platforms included differ (e.g. Japan may include LINE, Twitter/X, Instagram; Korea may include KakaoTalk, Instagram; the U.S. may include Facebook, Instagram, X). **Cross-country comparison of a “social web” series is invalid** without a stated platform list.

### 2.6 Generative AI: no shared definition

The Google/Ipsos survey (2025) asks whether respondents have “used generative AI in the past year” — a **past-year** reference period. The OECD’s 2025 survey asks about **experience with new technologies**, with different wording. MIC’s White Paper reports “generative AI service usage” by country, but the question wording and reference period are not harmonised with Korea or the U.S. **No common definitional basis exists.**

---

## Section 3 — Breaks, revisions and discontinuities

| year | country | series | what changed |
|---|---|---|---|
| 1997 | U.S. | CPS Computer and Internet Use Supplement | Internet use questions added; earlier supplements collected computer use only |
| 2000 | U.S. | CPS supplement | Reference period and question wording on internet use changed; broadband questions added |
| 2001 | Japan | MIC Communications Usage Trend Survey | Household member items added (individual-level usage questions) |
| 2003 | U.S. | CPS supplement | Broadband adoption questions expanded |
| 2007 | U.S. | CPS supplement | Survey moved from October to different months; sampling frame updated |
| 2009 | Korea | Survey on the Internet Usage | Survey renamed from “Survey on the Computer and Internet Usage” to “Survey on the Internet Usage” |
| 2010 | Japan | MIC survey | Web questionnaire survey introduced for some components; sample design changed |
| 2011 | U.S. | CPS supplement | Survey became annual from 2011; definition of “broadband” updated to include mobile broadband in some items |
| 2012 | Japan | MIC survey | Smartphone ownership questions added |
| 2013 | U.S. | CPS supplement | Survey moved to every-other-year schedule; broadband definition updated to 4 Mbps/1 Mbps |
| 2015 | U.S. | CPS supplement | Broadband definition updated; mobile broadband questions added |
| 2016 | Korea | Online shopping statistics | Sample revision implemented; time series prior to 2016 isolated from later data (not directly diffusion, but indicates revision practice) |
| 2018 | U.S. | CPS supplement | Broadband definition updated to 25 Mbps/3 Mbps |
| 2020 | Japan | MIC survey | Survey operations changed due to COVID-19; some response rates affected |
| 2023 | U.S. | CPS supplement | Most recent supplement; some questions on generative AI added or modified |
| 2024 | Korea | NIA survey | Generative AI usage items added or expanded |
| 2025 | Japan | MIC survey | Generative AI usage items included in White Paper analysis |

**Note:** The U.S. CPS supplement is the most fragmented series: the definition of “broadband” has changed at least four times (200 kbps → 4 Mbps/1 Mbps → 25 Mbps/3 Mbps → current), and the survey has not been conducted annually since 2013. Any U.S. broadband series spanning 1996–2026 must document these breaks or use FCC Form 477 data, which has its own definitional history.

---

## Section 4 — The gap after the last measurement: generative AI

**No continuous, industry-wide, nationally representative series of generative AI usage exists for Japan, Korea, or the United States.** What is published falls into four categories:

### 4.1 Vendor disclosures (point-in-time)

- **OpenAI / ChatGPT**: user numbers reported periodically by the company (e.g. weekly active users); not disaggregated by country in a consistent series.
- **Google / Gemini**: usage reported in earnings calls and blog posts; not a continuous country-level series.
- **Anthropic / Claude**: usage trends published in blog posts (e.g. “Claude.ai use by country”); not a national statistical series.
- **Similarweb**: publishes **monthly website visits** for generative AI tools by country; Japan +126.8%, Korea +85.6% from 2024 to 2025. This is a **traffic proxy**, not a usage measure; it counts visits, not unique users, and is affected by bot traffic and multiple devices.

### 4.2 Survey-based point estimates (not continuous)

| source | countries | year | question | result |
|---|---|---|---|---|
| Google/Ipsos (2025) | 21 countries incl. JP, KR, US | 2024 | Used generative AI in past year | Korea 55%, US 29%, Japan 28% |
| OECD (2025) | OECD countries | 2025 | Experience with new technologies / generative AI | Japan, Korea, Mexico included; no single penetration figure |
| MIC White Paper (2025) | JP, US, KR, etc. | 2024 | Generative AI service usage | Figures reported by country (Figure 3-71) but not as a continuous series |
| Pew Research (2023–2025) | US | 2023–2025 | Used ChatGPT / generative AI | US-only; no Japan or Korea counterpart in same survey |
| Sensor Tower (2026) | Global | 2025–2026 | In-app revenue from generative AI | US ~38% share; Japan 5%, Korea 5% — revenue, not usage |

### 4.3 Closest available proxies and limitations

1. **Google Trends / search volume** for “ChatGPT” or “generative AI” by country. Limitation: search interest ≠ usage; affected by media coverage.
2. **Similarweb website visits** to generative AI domains by country. Limitation: visits, not users; bot traffic; multiple domains per user.
3. **App download and revenue data** (Sensor Tower, data.ai). Limitation: revenue and downloads ≠ active usage; paid vs. free users not distinguished.
4. **National survey items** (MIC, NIA, Pew). Limitation: not harmonised, different reference periods, different question wording, not continuous for long enough to build a 30-year series.

**Conclusion:** Generative AI usage **cannot be measured as a continuous series** from 1996 to 2026. It can be **proxied** from 2023 onward using survey point estimates and traffic/revenue proxies, but these must be labelled as such. The series would have a **gap from 1996 to 2022** (no measurement of generative AI, because the technology did not exist in consumer form) and a **fragmented series from 2023 onward** (different sources, different definitions, no harmonisation).

---

## Section 5 — A normalisation proposal

Given the definitional differences in Section 2, a single comparable scale across all three countries and all technologies is not achievable without severe distortion. The following rule is proposed as the **least-bad** option for a cross-time, within-country series, with explicit limitations for cross-country comparison.

### Rule

**Step 1 — Choose one primary source per technology per country.** Prefer the longest continuous series from a single publisher. For mobile telephony and fixed broadband, use **ITU** as the primary source for all three countries. For internet use, use **national household surveys** (MIC for Japan, NIA for Korea, CPS/NTIA for the U.S.) as the primary source.

**Step 2 — Convert all series to a common unit: penetration per 100 inhabitants (or per 100 households).**
- For subscription-based series (mobile, fixed broadband): divide subscriptions by mid-year population × 100.
- For survey-based series (internet use, smartphone, social media): use the reported penetration rate directly if the survey reports % of population; if it reports % of households, convert to % of population using average household size from the same national source.

**Step 3 — Mark interpolated years.** Where a series is not annual (e.g. U.S. CPS supplement), interpolate linearly between survey years and **mark interpolated years in the series metadata**. Do not smooth across definitional breaks.

**Step 4 — Apply a break-adjustment factor where a definitional change is known and quantified.** For example, if the U.S. broadband definition changed from 200 kbps to 4 Mbps in 2013, and the number of subscribers under the old definition is known, calculate the ratio of new-definition to old-definition subscribers in the overlap year and apply it retrospectively. **Where no overlap exists, leave the break unadjusted and mark the series as discontinuous.**

**Step 5 — For cross-country comparison at a point in time, use the same year and the same source.** Compare Japan, Korea, and the U.S. in 2023 using ITU mobile subscriptions for all three; do not compare Japan’s MIC figure to Korea’s NIA figure for the same year unless the definitions have been checked and harmonised.

### What the rule assumes

- Population denominators are accurate and comparable across countries.
- Survey penetration rates are unbiased estimates of the true population parameter.
- Interpolation between survey years is acceptable for trend visualisation but not for precise year-on-year comparisons.
- ITU’s harmonised definitions are the closest available to a common standard.

### What the rule distorts

- **Cross-country comparison of survey-based series** (internet use, smartphone, social media, generative AI) remains invalid at a point in time because reference periods, question wording, and platform lists differ.
- **Mobile penetration** is inflated by multiple SIMs; the rule cannot correct for this without individual-level data.
- **Fixed broadband** is distorted by different speed thresholds; ITU’s 256 kbps floor is lower than current U.S. definitions, so U.S. figures under ITU will be higher than under FCC definitions.
- **Interpolated years** may mask turning points if the underlying trend is non-linear.

### Comparisons that remain invalid after the rule

- Comparing U.S. fixed broadband (FCC, 25 Mbps threshold) to Japan fixed broadband (ITU, 256 kbps threshold) in the same year.
- Comparing Korea’s NIA “internet usage rate” (past month) to Japan’s MIC “internet usage rate” (past year) without adjusting for reference period.
- Comparing social media penetration across the three countries without stating the platform list.
- Comparing generative AI usage across the three countries using any single survey, because the surveys were not harmonised.

### If a single comparable scale is required

The only defensible single scale is a **z-score or percentile rank within each country over time**, then plot the three countries’ trajectories. This preserves **cross-time comparability within a country** and allows **visual comparison of the shape of diffusion curves** across countries, but it **does not** permit statements like “Japan was at 50% and Korea at 60% in 2010.” The rule is:

1. For each country and each technology, compute the series’ mean and standard deviation over the full period.
2. Convert each year’s value to \( z = (x - \mu) / \sigma \).
3. Plot \( z \) over time for each country.
4. Label the y-axis as “standard deviations from country mean” and state explicitly that levels are not comparable across countries.

---

## Section 6 — What cannot be sourced

| item | assessment |
|---|---|
| Continuous social web penetration series (Japan, Korea, U.S., 1996–2026) | **Does not exist as a measured quantity.** National surveys ask about “SNS” or “social media” with different platform lists and different reference periods; no international body harmonises a continuous series. |
| Continuous messaging platform usage series (LINE, KakaoTalk, WhatsApp, etc.) | **Does not exist as a measured quantity.** Vendor-reported user numbers are point-in-time and not disaggregated by country in a consistent series. |
| Continuous generative AI usage series (any country) | **Does not exist as a measured quantity.** Survey point estimates exist from 2023 onward; no continuous series. |
| Comparable smartphone ownership series across all three countries for 1996–2026 | **Published but not harmonised.** Japan MIC, Korea NIA, and U.S. Pew all report smartphone ownership, but the questions and reference periods differ; no international body publishes a harmonised series. |
| U.S. fixed broadband series on a consistent definition, 1996–2026 | **Published but discontinuous.** FCC Form 477 data is available but the speed threshold has changed multiple times; CPS/NTIA data is irregular. No single consistent series exists. |
| Japan mobile subscriptions prior to 1990 | **Not published in ITU database.** ITU series starts 1990; earlier national data may exist in MIC archives but I could not verify. |
| Korea mobile subscriptions prior to 1984 | **Not published in ITU database.** Analogue mobile launched in 1984; ITU series starts 1990. |
| Cross-country comparable “internet user” series for 1996–2000 | **Published but sparse.** ITU/World Bank internet user series for Japan, Korea, and the U.S. exists from the mid-1990s, but early years are estimates based on different national sources. |

**Note on accessibility:** I was able to verify the existence and definition of ITU, OECD, MIC, NIA, and CPS series through published documentation. I could not access the full ITU DataHub time-series database directly (subscription required) and therefore cannot attest to every individual year’s figure. Figures cited here are from secondary sources that reproduce ITU or national data, and I have marked them accordingly.

---

## Section 7 — Refusals and confidence

### Refusals

I declined to:

- **Estimate any figure I could not source.** No invented numbers appear in this inventory.
- **Propose how the index should use the series.** That is outside the scope of this task.
- **Assess the artistic premise.** Not relevant to sourcing.
- **Smooth or backfill silently.** Where interpolation is proposed, it is marked as such.

### Overall judgement

**Can a defensible thirty-year, three-country diffusion series be assembled?**

**Partially — with caveats.**

A defensible series **can** be assembled for:

- **Mobile telephony** (1996–2023): ITU mobile-cellular subscriptions per 100 inhabitants. Continuous, definitionally stable, available for all three countries. Caveat: counts subscriptions, not users; multiple SIMs inflate penetration.
- **Fixed broadband** (1998–2023): ITU fixed-broadband subscriptions per 100 inhabitants. Continuous, but definitional threshold (256 kbps) is outdated and may not match national definitions.
- **Internet use** (1997–2023): national household surveys. Available for all three countries but **not harmonised**; reference periods and units differ.
- **Smartphone ownership** (2011–2025): national surveys. Available but not harmonised across countries.

A defensible series **cannot** be assembled for:

- **Social web** (1996–2026): no continuous, comparable series.
- **Messaging platforms**: no continuous, comparable series.
- **Generative AI** (1996–2026): no continuous series; only point estimates from 2023 onward.

**The caveat that matters most:** The series for the later waves (social web, messaging, generative AI) would be **constructed**, not **measured**. If the institution publishes a single “technology diffusion” series that spans 1996–2026, it must either (a) use different technologies at different times and mark the transitions explicitly, or (b) restrict the series to the technologies for which continuous measurement exists (mobile, fixed broadband, internet use) and treat the later waves as a separate, non-comparable extension. A single continuous series across all seven waves would be **dishonest** unless every splice point and definitional change is documented and every gap is marked.