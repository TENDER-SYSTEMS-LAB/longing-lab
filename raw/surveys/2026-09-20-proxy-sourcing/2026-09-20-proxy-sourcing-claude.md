I'll verify the main sources before answering, so rows can be marked honestly.# LONGING: Technology Diffusion Proxy Sourcing

**Currency of knowledge.** My training knowledge is reliable to roughly mid-2026. Today is 20 September 2026. Rows marked **[live]** were checked against the web today; everything else is from training memory and not re-verified. I have put almost no historical values in the tables, because I will not reproduce thirty years of figures from memory. URLs are given as domains unless I opened the page today. Licence statements are all `probable`, since I did not open any licence page.

Status legend: `verified` means I am confident the series exists with this name and coverage. `probable` means something of this kind exists but I am unsure of its exact form. `unknown` means I cannot say.

## Section 1: The inventory

### 1.0 International series covering all three countries

These are the only series with harmonised definitions across Japan, Korea and the US.

| technology | series name | publisher | first year | last year | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| Mobile | Mobile-cellular telephone subscriptions per 100 inhabitants (WDI code `IT.CEL.SETS.P2`) | ITU WTID, republished in World Bank WDI | pre-1996 | about 2024 | annual, year-end | Active SIMs including prepaid. M2M is excluded in principle, but this depends on what each country reports. | verified |
| Fixed broadband | Fixed-broadband subscriptions per 100 inhabitants (`IT.NET.BBND.P2`) | ITU / WDI | about 1998–2000 | about 2024 | annual | Wired subscriptions at ≥256 kbit/s download | verified |
| Fixed broadband | Fixed broadband subscriptions per 100 inhabitants, by technology | OECD Broadband Statistics | about 2001–02 | about 2024–25 | semi-annual (June/December) | ≥256 kbit/s advertised download. DSL, cable, fibre and other are split. | verified (start date probable) |
| Mobile broadband | Active mobile-broadband subscriptions per 100 | ITU, and OECD from about 2009 | about 2007 | about 2024 | annual / semi-annual | Data-capable SIMs with actual use | verified |
| Internet, all access modes | Individuals using the Internet, % of population (`IT.NET.USER.ZS`) | ITU / WDI | 1990 | about 2024 | annual | Nominally "used in the last 3 months". In practice each country's own survey is passed through with footnotes. | verified |
| Household ICT | ICT Access and Usage by Households and Individuals | OECD | about 2005 | varies | annual | Korea coverage is good, Japan partial, US sparse | probable |

Publication lag is 12 to 24 months, so there is no official 2025–26 point for these yet. Licence: WDI is CC BY 4.0 and OECD data has been CC BY 4.0 since 2024 (both `probable`). ITU's own database has separate terms (`unknown`).

### 1.1 Japan

| technology | series name | publisher | first year | last year | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| Internet, smartphone, mobile, SNS | 通信利用動向調査 (Communications Usage Trend Survey, CUTS), household edition | MIC (総務省), hosted on e-Stat | 1990 for the survey; individual internet use from 1997; smartphone from 2010 | 2024 survey (reference end of August 2024) **[live]** | annual | Household ownership shares, plus individual shares for ages 6+. Internet use means used in the past 12 months. | verified |
| Mobile (supply side) | 電気通信サービスの契約数及びシェアに関する四半期データ | MIC | about 2004 | 2026 | quarterly | Contracts covering mobile, PHS and BWA. Communication modules are included. | verified (start probable) |
| Mobile (early years) | 携帯電話・PHS契約数 (carrier-level) | TCA (電気通信事業者協会) | before 1996 | ongoing | monthly, later quarterly (about 2014) | Contracts by carrier | probable |
| Fixed broadband | Same MIC quarterly series, plus earlier MIC releases on DSL, FTTH and CATV contracts | MIC | about 2000 | 2026 | quarterly | Contracts defined by technology, with no speed threshold | verified (pre-2004 form probable) |
| Dial-up / BBS | パソコン通信 membership counts (Nifty-Serve, PC-VAN) reported in 通信白書; dial-up ISP subscriber counts | MPT/MIC white papers; New Media Development Association | about 1990 | mid-2000s | annual, irregular | Company-reported membership, not a survey | probable, could not verify |
| Social web, messaging | 情報通信メディアの利用時間と情報行動に関する調査 | MIC Institute for Information and Communications Policy | FY2012 | about FY2024 | annual | Platform-level use rates (LINE, X, Facebook, Instagram and others), ages 13–69 | verified |
| Smartphone (second source) | 消費動向調査, durable-goods penetration | Cabinet Office | smartphone from about 2014 | ongoing | annual (March) | Household penetration | probable |
| Generative AI | Individual gen-AI use experience, from a commissioned web survey in 情報通信白書 | MIC | FY2023 | FY2025 | annual, 3 points | 9.1% → 26.7% → 58.8% **[live]** | verified, but see the break in §3 |

CUTS anchor checked today: individual internet use was 86.2% in 2023. Pages opened: soumu.go.jp/johotsusintokei (white paper) and soumu.go.jp/menu_news/s-news/01tsushin02_02000178.html (2024 CUTS release). Licence: Government of Japan Standard Terms of Use, which is CC BY-compatible (`probable`). I do not know whether CUTS itself now carries an individual gen-AI item.

### 1.2 Korea

| technology | series name | publisher | first year | last year | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| Internet, smartphone, SNS, messenger | 인터넷이용실태조사 (Survey on the Internet Usage), a nationally approved statistic | MSIT / NIA. Earlier publishers were KRNIC, then NIDA, then KISA. | about 1999 | 2025 survey, published 31 March 2026 **[live]** | annual | Individuals aged 3+. Internet use means used within the last month. The 2025 sample was 22,671 households and 50,750 people, and internet use was 95.0%. | verified (early years probable) |
| Mobile (supply side) | 무선통신서비스 가입 현황 (originally 유·무선통신서비스 가입자 현황) | MSIT, and its predecessor ministries | late 1990s | 2026 | monthly | Lines by carrier, generation and MVNO. IoT lines are reported as a separate category. | verified (start probable) |
| Fixed broadband | 초고속인터넷 가입자 현황 | MSIT | about 1999 | 2026 | monthly | Lines defined by technology (xDSL, HFC, LAN, FTTH), with no speed threshold | verified (start probable) |
| Dial-up / PC통신 | Subscriber counts for Chollian, Hitel, Nownuri and Unitel, as cited in 정보화백서 | NCA/NIA white papers; company figures | about 1990 | about 2002 | annual | Company-reported membership | probable, could not verify |
| Smartphone, social, messaging (second source) | 한국미디어패널조사 | KISDI | 2010 | about 2025 | annual panel | Individual device ownership and SNS use | verified |
| Messaging | KakaoTalk domestic MAU | Kakao quarterly IR | about 2013 | 2026 | quarterly | Vendor-defined MAU | probable |
| Generative AI | 생성형 AI 서비스 경험률, an item within 인터넷이용실태조사 | MSIT / NIA | 2023 (from memory about 17.6%, unverified) | 2025 | annual | 33.3% in 2024 → 44.5% in 2025 **[live]**. Paid subscription was 7.9%. | verified for 2024–25, probable for 2023 |
| AI services (broad) | 일상 AI 서비스 경험률 | same | 2021 | 2025 | annual | 32.4% (2021) → 67.0% (2025). This includes smart appliances, so it is not gen AI. | verified **[live]** |

Licence: KOGL / KOSIS terms (`probable`). I do not know whether the base for the gen-AI rate is all persons aged 3+ or internet users only. That needs to be read from the report itself.

### 1.3 United States

| technology | series name | publisher | first year | last year | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| Internet, devices | Internet Use Survey (CPS Computer and Internet Use Supplement), NTIA Data Explorer | NTIA / Census | 1994 | 2023 | irregular, roughly biennial | Households and persons aged 3+. "Uses the Internet from any location." Household proxy respondent. | verified (exact wave list probable) |
| Internet, broadband, smartphone, social | Fact sheets: Internet/Broadband; Mobile; Social Media | Pew Research Center | 2000; smartphone 2011; social 2005 | about 2024–25 | roughly annual | Adults 18+, self-report | verified |
| Household internet | ACS table S2801 (computer and internet use) | Census Bureau | 2013 | 2024 | annual; 2020 was experimental only | Households with a broadband subscription, broken down by type | verified |
| Fixed broadband (supply side) | High-Speed Services for Internet Access, later renamed Internet Access Services reports (Form 477) | FCC | December 1999 | about 2021–22 | semi-annual | Connections over 200 kbps in at least one direction, residential plus business | verified |
| Fixed broadband (successor) | Broadband Data Collection (BDC) | FCC | June 2022 | 2026 | semi-annual | Primarily a measure of availability rather than subscriptions | verified |
| Mobile | Annual Wireless Industry Survey | CTIA | 1985 | about 2025 | semi-annual, then annual | "Connections", which includes tablets and IoT devices | verified (only the toplines are free) |
| Dial-up | Home dial-up versus broadband share (Pew, 2000 onward); CPS 2000–03 connection-type item; AOL subscriber counts in 10-K filings | Pew / NTIA / SEC filings | 2000 | about 2015–2019 | mixed | Survey shares, plus one company's count | probable |
| BBS | none | none | none | none | none | No measured series exists. Trade-magazine estimates only. | unknown / does not exist |
| Messaging | Messaging-app items in Pew surveys; NTIA online-activities item | Pew / NTIA | about 2013–15 | about 2023 | irregular | Adults or persons who use messaging | probable |
| Generative AI (ChatGPT) | "Ever use ChatGPT", from the American Trends Panel | Pew | 2023 | 2026 | annual, 4 points | Adults 18+: 18% → 23% → 34% → 44% **[live]** | verified |
| Generative AI (any tool) | Real-Time Population Survey gen-AI module (Bick, Blandin, Deming) | St. Louis Fed / NBER authors | August 2024 | 2025 | several waves | Ages 18–64. 54.6% by August 2025. | probable |
| Generative AI (firms) | Business Trends and Outlook Survey, AI-use item | Census Bureau | September 2023 | 2026 | biweekly | Share of *firms* using AI. Not comparable to the person-level rows above. | verified (from memory) |

Licence: federal series are public domain. Pew requires attribution under its terms of use. CTIA is proprietary.

## Section 2: Definitions that do not match

- **Mobile.**
  - All three supply-side series count subscriptions, not people. Japan's contract counts include embedded communication modules and, historically, PHS. Korea reports IoT lines separately from handsets. CTIA's "connections" include all data devices. So the national headline figures are inflated in different ways, and only ITU/OECD attempt to strip out M2M lines.
  - Prepaid is negligible in Japan and Korea and substantial in the US. This makes ITU's rule of "active within 3 months" matter mostly for the US figure.
  - On the survey side, Japan reports household ownership plus individuals aged 6+, Korea reports individuals aged 3+, and Pew reports adults aged 18+.
- **Internet use.**
  - Japan counts anyone who used the internet in the past 12 months, aged 6+.
  - Korea counts use in the past month, aged 3+.
  - NTIA counts current use, aged 3+, reported by a household proxy.
  - Pew counts "at least occasionally", aged 18+.
  - ITU's nominal 3-month window matches none of these.
- **Fixed broadband.**
  - ITU and OECD use ≥256 kbit/s per 100 inhabitants.
  - Japan and Korea define broadband by technology, with no speed floor.
  - The FCC used more than 200 kbps in one direction and has raised the "broadband" benchmark repeatedly (4/1, 25/3 and 100/20 Mbps). Pew and ACS measure households that self-report having a subscription.
  - Per-inhabitant and per-household denominators diverge as household size changes, and Korea's household size fell sharply over the period.
- **Social web.** Japan's CUTS category is "SNS including free-call functions", at 81.9%, which means LINE is counted as social media. Korea separates messenger use from SNS, and its SNS category has at times included minihompy and blog services. Pew's "any social media" figure depends on a platform list that changes over time.
- **Smartphones.** The same three-way mismatch between household, individual and adult bases applies. The age floors are 6+, 3+ and 18+.
- **Generative AI.**
  - Japan: the measure is ever-use, from a commissioned web panel.
  - Korea: the measure is "experienced", from a face-to-face household survey of people aged 3+.
  - US: Pew's measure is product-specific (ChatGPT), from a probability panel of adults 18+.
  - MIC's own US comparator (68.8%) is far above Pew's figure for the same period. That gap shows how much the survey mode and the question wording matter.

## Section 3: Breaks, revisions and discontinuities

| year | series | what changed | confidence |
|---|---|---|---|
| 2001; 2004 | Japan, all series | Publisher changed from MPT to MPHPT in 2001. The English name became MIC in 2004. | verified |
| about 2013–15 | Japan mobile contracts | Separate module reporting began. Counts were adjusted for intra-group MVNO transactions. | probable |
| about 2014 | TCA | Carrier reporting moved from monthly to quarterly. | probable |
| 2019 | CUTS | A change in survey design produced an anomalous jump in internet use. MIC advises caution when comparing across this year. | probable |
| 2021–23 | Japan PHS | The service was wound down and drops out of the counts. | verified |
| 2026 | MIC white paper gen-AI item | 15–19-year-olds were added to the sample. The rate for ages 20+ is 52.2%, against a headline of 58.8%. **[live]** | verified |
| about 2002–06 | Korea internet survey | The age floor moved from 7+ to 6+ to 3+. Mobile internet was folded into "use". | probable |
| 2004; 2009; about 2019 | Korea internet survey | Publisher changed from KRNIC to NIDA, then KISA, then NIA. | probable |
| 2008; 2013; 2017 | Korea subscriber statistics | The responsible ministry changed from MIC to KCC, then MSIP, then MSIT. | verified |
| about 2014 and later | Korea mobile lines | IoT and device lines were split out from handsets. | probable |
| 2005; 2008; 2014 | FCC Form 477 | 2005: the reporting threshold was removed. 2008: tract-level reporting, speed tiers and mobile broadband were added. 2014: further revision. | verified (details probable) |
| 2010; 2015; 2024 | FCC | Changes to the broadband speed benchmark. | verified |
| 2022 | FCC | Form 477 was replaced by BDC. Subscription counting is de-emphasised. | verified |
| about 2015 | NTIA CPS supplement | The questionnaire was redesigned. Wave intervals remain irregular throughout. | probable |
| 2020 | ACS | No standard 1-year release. | verified |
| about 2021–23 | Pew | Moved from telephone surveys to NPORS (web and mail). Pew flags this as a mode break. | verified |
| ongoing | ITU / WDI | History is silently revised whenever countries resubmit. Record the download date. | verified |
| 2025–26 | Microsoft AI Diffusion | Moved from half-yearly to quarterly reports (H1 2025, H2 2025, Q1 2026). **[live]** | verified |

## Section 4: The gap after the last measurement

I cannot find a continuous, industry-wide series of generative-AI usage volumes for any of the three countries. The following is what is published.

- **Official annual survey points (3 or 4 per country).** These are the Japan, Korea and US rows in §1. They are not mutually comparable, for the reasons in §2.
- **One cross-country series: Microsoft AI Economy Institute, AI Diffusion Report.**
  - It reports the share of the population aged 15–64 using gen-AI tools. It is derived from Microsoft telemetry and adjusted for device share and internet penetration. It is a modelled estimate, not a measurement.
  - South Korea went from 25.9% to 30.7%, and the US from 26.3% to 28.3%, between H1 and H2 2025.
  - The US figure for Q1 2026 is 31.3%.
  - The methodology paper is arXiv 2511.02781. The authors concede that the underlying data come from PC and tablet usage.
  - A Japan figure exists in the reports. I did not retrieve it and will not guess it.
  - Limitations: a single vendor, only three time points, a phone-blind base, and an opaque adjustment.
- **Point-in-time vendor disclosures.**
  - OpenAI publishes occasional global weekly-active-user announcements (over 900 million weekly, February 2026). They are global and irregular, with no country split. The figures come from press events, not from a published series.
  - The usage paper by OpenAI and academic co-authors (2025) is a snapshot.
  - The Anthropic Economic Index gives per-country *relative* usage indices. These are not volumes and cover one vendor only.
- **Commercial panels.**
  - Similarweb and Sensor Tower cover all three countries. Korea also has Mobile Index and WiseApp, and Japan has ICT総研 and the NTT Docomo institute.
  - These are paywalled and panel-based, and their definitions are unstable.
  - I can verify that they exist but not their series. `probable`.
- **Firm-level data.** Census BTOS is the only high-frequency official AI series anywhere in the three countries. It is biweekly, US-only, and measures firms, not people.

The closest honest proxy is each country's own official annual survey point, used within that country only. The Microsoft series is the sole cross-country check. The last measured points as of today are as follows:

- **Japan:** the FY2025 survey, published 24 July 2026.
- **Korea:** the 2025 survey, published 31 March 2026.
- **US:** the Pew early-2026 wave, published 17 June 2026.
- **Microsoft:** Q1 2026.

Anything later is extrapolation.

## Section 5: A normalisation proposal

**Rule ("own-ceiling timing scale").** Apply this per country *c* and technology *k*:

1. **Pick one spine series by a fixed priority.** First, the ITU/WDI or OECD series where one exists (mobile, fixed broadband, internet use). Otherwise, the national official household survey (Japan CUTS, the Korea Internet Usage Survey, US NTIA). Otherwise, Pew. Never splice two sources within one spine. Second sources are reported alongside and are not blended in.
2. **Date every observation at its true reference date.** That is year-end for ITU, end of August for CUTS, the fieldwork midpoint for Korea and for Pew, and the supplement month for the CPS. Do not use the label year.
3. **Bounded share series (% of a population).** *D* = *x*/100. Record the base (age floor, household or individual, recall window) as metadata. Do not rescale.
4. **Unbounded series (subscriptions per 100).**
   - Define the ceiling *S* as the mean of the first three consecutive annual observations whose year-on-year change is under 2% in relative terms.
   - Then *D* = min(1, *x*/*S*).
   - If no such plateau exists, leave the series un-normalised and flag it.
5. **Technologies in decline (dial-up).** *D* = *x* / max(*x*).
6. **Interpolation.** Do not interpolate inside the rule. Any value at a frequency finer than annual is a constructed value and must be flagged as such. The real points are the dated observations from step 2 and nothing else.

**What the rule assumes.**
- Definitional inflation (multi-SIM, modules, business lines) is a constant multiplicative factor within a country over time.
- The plateau represents true saturation.

**What the rule distorts.**
- The first assumption is false for mobile, because the share of multi-SIM and IoT lines grows late in the series. That bias pushes *S* upward, which makes early diffusion look slower than it was.
- Step 4 discards all cross-country level information by construction.
- Step 3 leaves the gaps in age base and recall window uncorrected. Korea's 1-month window, Japan's 12-month window, and the 3+/6+/18+ age floors all remain in the data.

**What is valid after applying the rule.**
- Within-country comparisons across time.
- Cross-country comparisons of *timing*: the dates at which a country crossed 10%, 50% and 90%, and the time it took to go from 10% to 90%.

**What is still invalid.**
- Cross-country levels at a point in time.
- Any cross-country comparison of social, messaging or gen-AI series.
- Any comparison of one technology's level against another's.
- Anything involving gen AI beyond the ordering of points within one country. With three or four observations and no plateau, there is no usable ceiling.

## Section 6: What cannot be sourced

- **BBS users, US.** Does not exist as a measured quantity.
- **PC-communication membership, Japan and Korea.** Published historically as company counts in print-era white papers. Not accessible to me, and not survey-based.
- **A continuous series of dial-up subscribers.** Partly published, in fragments from the FCC, MIC and company filings. No harmonised series exists.
- **The social web before about 2005, and before about 2011 in Japan and Korea.** Essentially unmeasured by official statistics. Platform MAUs by country are mostly unpublished. Meta reports the US and Canada combined, and X stopped reporting after 2022.
- **US messaging.** No official series.
- **Gen-AI usage volumes by country (sessions, tokens, MAU).** Held by vendors and unpublished.
- **Anything at weekly frequency for persons.** Does not exist in official statistics.
- **Not checked today.** Exact start years, licences and last-revision dates for most rows, the wave lists for CUTS, KOSIS and NTIA, and the Japan value in Microsoft's reports. These are published but were not checked.

## Section 7: Refusals and confidence

**What I declined to do.**
- I did not reproduce historical values from memory.
- I did not assess the premise or say what the index should do with the series.
- I did not state licences as fact or give last-revision dates, because I could not verify either.
- I did not estimate the missing Japan figure in Microsoft's reports or the unverified Korea 2023 gen-AI figure.

**Judgement.** A single thirty-year series does not exist. A defensible thirty-year *chain* can be assembled.

- **Mobile, internet use and fixed broadband.** These can be built on the ITU/WDI and OECD spine. It is harmonised, runs from 1996 to about 2024, and is revisable.
- **Smartphones.** From about 2010–11, from national surveys only. Bases are mismatched, so the series are good for timing and not for levels.
- **The social web.** From about 2005 in the US and about 2011 in Japan and Korea, under the same limits as smartphones.
- **Dial-up and BBS.** Cannot be carried as measured three-country series.
- **Generative AI.** This is three or four non-comparable annual points per country, and the last are dated between March and July 2026.
- **The measurement boundary.** It can be stated honestly, but it is a different date for each technology and country. It is not one week.

I can also put this into a document or spreadsheet if that is more useful for the project.