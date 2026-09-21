**LONGING — Round 1: Sourcing inventory (draft for verification)**

**Attestation before anything else.** I performed no live lookups in this session. Everything below comes from training knowledge, which ends in early 2025 (conservatively: February 2025). Nothing published after that date can be attested here, and 2025–2026 figures are outside my knowledge entirely. Given that, I use the status labels as follows:

- `verified` — I am confident the series exists with approximately this name, publisher and coverage, from repeated exposure in training data. This is **not** live verification.
- `probable` — something of this kind exists, but exact name, start year, age band or discontinuation date needs checking.
- `unknown` — I cannot attest.

**Every row should pass through a live re-verification pass before publication.** URLs are given at domain or stable-path level only; deep links must be re-found.

---

## Section 1 — The inventory

### 1.1 Japan

| technology | series name | publisher | first year | last year (attestable) | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| dial-up | 通信利用動向調査 (Communications Usage Trend Survey) — ISP/dial-up contract counts | 総務省 (MIC), via e-Stat (e-stat.go.jp) | ~1996 | mid-2000s; line item discontinued, exact year unverified | annual | ISP subscription contracts via dial-up (契約数), business + household | `verified` (existence); end year `probable` |
| mobile telephony | Communications Usage Trend Survey (annual); 電気通信事業者協会 monthly contract statistics | MIC; TCA (tca.or.jp) | 1996 | 2024 | annual / monthly | 契約数 — active contracts, not SIMs or persons; corporate lines included; PHS reported as a separate category until service sunset | `verified` |
| PHS | same series, PHS category | MIC / TCA | 1996 | category removed as service phased out 2021–2023 (exact end year `probable`) | annual / monthly | PHS contracts | `verified` (existence) |
| fixed broadband | Broadband contract counts by technology (xDSL / cable / FTTH), 契約数等に関する調査 | MIC | xDSL ~1999; FTTH ~2001 | 2024 | monthly–quarterly | subscriptions by technology; apartment-type FTTH counted per dwelling after a counting change (~2010, `probable`) | `verified` |
| internet use (individuals) | Communications Usage Trend Survey, household/individual section; republished in 情報通信白書 (Information & Communications White Paper, soumu.go.jp/johotsusintokei/whitepaper/) | MIC | ~1997 | 2024 | annual | % of individuals (age band likely 6+, unverified) using the internet | `probable` |
| smartphones (individuals) | same household survey / white paper | MIC | ~2011 | 2024 | annual | % of individuals using a smartphone | `probable` |
| social web | 情報通信メディアの利用時間と情報行動に関する調査 (Survey on Media Use Time and Information Behaviour); SNS items also in the household survey | MIC | ~2011 (earlier antecedents possible) | 2024 | annual | % of individuals using SNS; platform list and wording vary by year | `probable` |
| generative AI | Communications Usage Trend Survey, 2023 round (R5), published 2024 — first generative-AI usage question | MIC | 2023 | unconfirmed continuation | annual | % of individuals using generative AI services | `probable` |

Licence: Japanese government statistics are released under the Government of Japan Standard Terms of Use (政府標準利用規約 2.0), compatible with CC BY 4.0 with attribution — `verified`.

### 1.2 Korea

| technology | series name | publisher | first year | last year (attestable) | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| internet use, incl. dial-up era | 인터넷 이용실태조사 (Survey on the Internet Usage) | KISA (kisa.or.kr); predecessor surveys by MIC/KRNIC/NIA before the 2009 merger | 1997/98 (exact start `probable`) | 2024 | annual | individuals aged 3+ (changed from 6/7+ around 2013 — see §3); usage rate, connection type, activities | `verified` (existence); start year and age-history `probable` |
| mobile telephony | mobile subscription statistics (월별 이동전화 가입자 현황), also carried in KOSIS (kosis.kr) | 과학기술정보통신부 (MSIT) | 1996 | 2024 | monthly / annual | 가입자 (subscriptions): includes second devices, data-only and IoT USIMs, MVNO from ~2011, 5G from 2019 — penetration exceeds 100% for this reason | `verified` (existence); exact series title `probable` |
| fixed broadband | broadband subscription counts by technology (xDSL / HFC / FTTx / satellite / WiBro) | MSIT (with NIA); via KOSIS; harmonised in OECD broadband statistics | 1998/99 | 2024 | monthly / annual | subscriptions by technology, OECD-consistent (≥256 kbps); FTTB (apartment building fibre) counted within FTTx | `verified` |
| smartphones | MSIT ICT statistics — smartphone subscription counts and penetration | MSIT | ~2010/11 | 2024 | monthly / annual | smartphone 가입자; penetration rate | `probable` |
| smartphones / messaging / SNS (individuals) | 스마트폰 이용실태조사 (Survey on Smartphone Usage), incl. messenger and SNS usage items (KakaoTalk measurable here) | KISA (with NIA) | ~2011 | 2024 | annual | usage rates among smartphone users / individuals | `probable` |
| generative AI | — | — | — | — | — | no national series I can attest; see §4 | `unknown` |

Licence: Korean public data under 공공누리 (KOGL) terms; statistics generally attribution-type — `probable`, verify per dataset.

### 1.3 United States

| technology | series name | publisher | first year | last year (attestable) | frequency | unit and definition | status |
|---|---|---|---|---|---|---|---|
| internet use (persons) | Computer and Internet Use Supplement to the Current Population Survey | US Census Bureau with NTIA (ntia.gov) | 1994 | 2021 (a 2023 supplement is possible; `unknown`) | **irregular** — roughly biennial with gaps (1994, 1997, 1998, 2000, 2001, 2003, 2007, 2009–2013, 2015, 2017, 2019, 2021; list approximate) | persons (3+) in households; internet use anywhere | `verified` |
| household internet subscriptions by type | American Community Survey (internet questions added 2013) | Census Bureau, data.census.gov | 2013 | 2023 (2020 1-year estimates **not released** — pandemic) | annual | households, by subscription type (broadband / cellular-only / satellite / dial-up / none); **home access only** | `verified` |
| fixed broadband connections | Form 477 filings, published as "Internet Access Services" reports | FCC (fcc.gov) | ~1999 (modern form ~2008) | ~2023; continuation under the Broadband Data Collection is `unknown` | semiannual / annual | end-user fixed connections ≥200 kbps (collection floor), residential + business, by speed tier | `verified` (existence); recent years `unknown` |
| mobile telephony | Semi-Annual Wireless Industry Survey | CTIA (industry association) | 1985 | 2024 | semiannual | retail connections (wholesale excluded); connected devices reported separately | `verified` |
| internet use, dial-up vs broadband, smartphones, social media, ChatGPT (adults) | Pew Research Center national surveys (pewresearch.org) | Pew (predecessor Times Mirror surveys from 1995; regular series from 2000) | 1995 | 2024 | irregular → periodic | US adults 18+; methodology break mid-2010s (American Trends Panel) — see §3 | `verified` |
| messaging apps | Pew app-specific questions | Pew | ~2015 | sporadic | irregular | % adults using named apps; no single dominant US platform, so no single-app series | `probable` |
| firm-level AI adoption | Annual Business Survey, AI/technology-use module | Census Bureau | 2023 (reference year 2022/23) | unconfirmed | annual/biennial | % firms using AI technologies — **includes non-generative AI** | `probable` |

Licence: US federal data public domain. Pew data free with attribution, non-commercial — `verified`.

### 1.4 International harmonised series (covering all three countries)

| series | publisher | first year | unit | status |
|---|---|---|---|---|
| ITU DataHub: individuals using the Internet (%); mobile-cellular subscriptions per 100; fixed broadband subscriptions; mobile-broadband subscriptions (from ~2007); household internet access | ITU (datahub.itu.int; legacy ICT Statistics portal migrated ~2023) | ~1996–1998 for these countries | ITU-harmonised definitions; values submitted by national administrations | `verified` (existence); licence terms `probable` |
| OECD Broadband Statistics / OECD Data Explorer | OECD (data-explorer.oecd.org) | ~1998 | fixed broadband subscriptions per 100 inhabitants, ≥256 kbps threshold | `verified` |
| OECD "ICT Access and Usage by Households and Individuals" | OECD | sparse ~1997; consistent from ~2006 | individuals **16–74** — note this differs from all three national headline series | `verified` (existence); coverage detail `probable` |
| World Development Indicators: IT.NET.USER.ZS, IT.CEL.SETS.P2, IT.NET.BBND.P2 | World Bank (databank.worldbank.org) | 1990s | mirrors ITU | `verified`; CC BY 4.0 |

---

## Section 2 — Definitions that do not match

This is the section that will generate errors if skipped.

**Internet use.** Japan: % of individuals, age band likely 6+. Korea: % of individuals 3+ since ~2013, 6/7+ before — the change adds young children at a period when their usage was rising, so the level jumps mechanically. US: three different units in circulation simultaneously — CPS persons 3+ (use anywhere), ACS **households** (subscription **at home only**), Pew **adults**. The ACS household-home series is not the same construct as any individual-use series; it excludes mobile-only use outside the home, which is common. ITU's harmonised indicator targets "individuals using the internet in the last 3 months"; national practice before the late-2010s harmonisation push varied in recall window (ever / monthly / 12-month), so pre-~2015 international values are weakly comparable. The OECD household database uses 16–74, so OECD Korea/Japan values will not match the national headlines for the same year.

**Mobile telephony.** Japan counts active contracts (契約数), not persons or SIMs; corporate lines included; PHS separate until sunset. Korea counts 가입자 including data-only and IoT USIMs and MVNO lines — penetration therefore exceeds 100%, and a "distinct persons" measure is not the headline (`probable` that MSIT publishes supplementary person-level figures). The US CTIA series counts retail connections and separates connected devices. ITU's "mobile-cellular subscriptions" inherits each country's submission practice, so Japanese contract counting and Korean M2M lines both enter the harmonised series. **Cross-country level comparisons of mobile penetration are invalid at any point in time; within-country trends are sound.**

**Fixed broadband.** Threshold: ITU/OECD ≥256 kbps downstream; FCC collection floor ≥200 kbps in one direction pre-2015, with policy benchmarks of 25/3 Mbps (2015) and 100/20 Mbps (2024) applied on top — benchmark changes move which *counted* connections are called "broadband" in FCC commentary without changing the 477 collection floor. Unit: subscriptions (JP/KR/FCC) vs households (ACS, no speed threshold at all). Japan's FTTH counts include apartment-type contracts counted per dwelling after a counting revision (~2010, `probable`) — a one-time level shift in FTTH. Korea's FTTx includes building-type fibre. FCC includes business connections; ACS is residential only.

**Smartphones.** All three series begin 2010–2011 (conveniently aligned), but denominators differ: Japan and Korea publish both subscription counts and individual usage rates; the US has **no official subscription series** — only Pew's adult-level ownership. Adult-based US values cannot be placed on the same base as population-based JP/KR subscription counts without conversion (§5).

**Social web.** US: % of adults using social networking sites (Pew, from 2005). Japan: % of individuals using SNS (MIC, from ~2011), platform list varies by year. Korea: % of individuals/users using SNS (KISA, from the 2010s). No ITU or OECD harmonised indicator exists for this. Question wording ("ever used" vs "use regularly") differs and is not documented consistently across the three.

**Messaging.** Japan: LINE's user figures are vendor announcements (monthly actives per LINE's own metric), not statistics; possibly also inside MIC's SNS platform table (`probable`). Korea: KakaoTalk usage rate appears inside KISA's smartphone survey (`probable`), plus vendor MAU announcements. US: no dominant platform; only occasional multi-app Pew questions. **There is no harmonised messaging series anywhere in the international system.**

**Generative AI.** Japan: MIC individual-usage question (recall window unverified). US: Pew asks about ChatGPT use by adults (ever/regularly); Census ABS asks firms about AI technology use — a broader, non-generative-inclusive, firm-level concept. These three constructs share nothing but the words. See §4.

---

## Section 3 — Breaks, revisions and discontinuities

| country/series | year | what changed | status |
|---|---|---|---|
| JP — subscription statistics | ~2003 | consolidation of several subscription surveys into the Communications Usage Trend Survey | `probable` |
| JP — dial-up | ~2006 | dial-up line item discontinued from the survey | `probable` |
| JP — FTTH | ~2010–12 | apartment-type FTTH counted per dwelling rather than per contract | `probable` |
| JP — individual survey | ~2011 | household/individual survey integrated or redesigned; pre/post individual series not directly comparable | `probable` |
| JP — mobile | 2021–23 | PHS category removed as service sunset | `probable` (end year) |
| KR — publisher | 2008–09 | Ministry of Information and Communication abolished; functions to MSIT/KCC; survey passed to KISA on the KRNIC–KISA merger | `verified` (institutional event); continuity of series `probable` |
| KR — internet survey | ~2013 | age coverage widened from 6/7+ to 3+ — mechanical level break | `probable` (year) |
| KR — mobile | 2011; 2019 | MVNO lines added; 5G category added | `probable` |
| KR — broadband | ~2006 | WiBro added as a broadband category | `probable` |
| KR — survey mode | 2010s | frame/mode changes as landline-only households vanished | `probable` |
| US — CPS supplement | 1994–2021 | schedule is irregular, gaps of 1–4 years; no annual series possible from CPS alone before 2013 | `verified` |
| US — ACS | 2013 | internet questions begin — new series; not splicable to CPS without assumptions | `verified` |
| US — ACS | 2020 | 1-year estimates not released (pandemic non-response); use 5-year or experimental weights | `verified` |
| US — FCC | 2015; 2024 | "advanced telecommunications capability" benchmark changed to 25/3, then 100/20 | `verified` (events); effect on published counts `probable` |
| US — FCC | ~2008–2014 | Form 477 moves from lines to end-user connections; end-user definition and speed tiers revised | `probable` |
| US — FCC | 2022–23 | Broadband Data Collection replaces Form 477 availability data; subscription-series continuation unverified | `unknown` |
| US — Pew | 2014–16 | migration to the American Trends Panel (probability online panel); Pew itself flags pre/post comparability limits | `verified` (event) |
| ITU | late 2010s–2022 | harmonisation of recall window for "individuals using the internet"; older country values not uniformly restated | `probable` |
| ITU | 2023 | DataHub migration; series names/IDs changed | `verified` (event) |
| OECD | ~2006–2010 | broadband definition/threshold restatements; historical figures revised | `probable` |

---

## Section 4 — The gap after the last measurement (generative AI)

**No continuous, industry-wide, country-level generative-AI usage series exists for Japan, Korea or the United States as of my knowledge cut-off (early 2025).** I state this plainly; it is a non-existence claim, not an access claim.

What is actually published, by form:

1. **Recurring national polls.** US: Pew asks about ChatGPT use among adults, first fielded July 2023, repeated several times per year — the closest thing to a series in any of the three countries, but ~2–4 point-in-time observations per year, adult-only, ever/regular-use wording. Japan: MIC's 2023 Communications Usage Trend Survey added a generative-AI usage item (`probable`); whether it continues annually is unverified. Korea: I cannot attest to any national generative-AI usage survey — `unknown`, possibly existing but unverifiable by me.
2. **Firm surveys.** US Census Annual Business Survey AI module (from 2023; includes non-generative AI; reference-year lag). Japan and Korea equivalents: `probable`/`unknown`.
3. **Vendor disclosures.** OpenAI weekly active users (global, announced at intervals — e.g., 100M November 2023, 200M mid/late 2024; further 2025 figures are at or beyond my boundary), Microsoft Copilot, Google Gemini, Meta AI, all point-in-time marketing metrics; definitions inconsistent (weekly vs monthly actives), unaudited, **no country breakdowns**; Anthropic publishes no usage figures. Kakao and LY Corp disclose messaging-platform MAUs periodically through earnings, which is the closest Korea/Japan analogue — vendor-defined, irregular.
4. **Commercial telemetry** (Similarweb, Sensor Tower, Comscore): continuous and country-split, but licensed, methodologically opaque, and fragile to app/web changes.

Consequence for the institution's "measured vs extrapolated" marker: for generative AI, "measurement" in 2023–2024 means scattered polls; anything from early 2025 onward is, for me, unattestable — and for the world, absent a continuous series, will consist of poll snapshots plus vendor claims until a statistical agency builds one.

---

## Section 5 — Normalisation proposal

**Rule: declared-ceiling normalisation with denominator harmonisation.** Mechanical throughout; two people applying it to the same tables get the same numbers.

1. **One population base.** Use UN World Population Prospects P(c,y) (total resident population), A(c,y) (15+), and age-band shares s(c,y) (share aged 3+, 6+) for all three countries and all years. Never use each country's own denominator for cross-country work.
2. **Series precedence.** For cross-country comparisons use the ITU/OECD harmonised series. For within-country continuity and back-history use the national series (Section 1 tables). Where both exist, publish both; discrepancies are logged, not reconciled silently.
3. **Unit conversion.**
   - Subscription series → per 100 inhabitants: `v' = v / P(c,y) × 100`.
   - Age-banded individual rates (Korea 3+, Japan 6+) → population rate: `v' = v × s(c,y)`. Declared assumption: usage among excluded ages is zero (defensible for 0–2; increasingly false for older bands — log the distortion).
   - Adult rates (Pew) → population rate: `v' = v × A(c,y)/P(c,y)`.
4. **Scaling.** `a = min(v'/S, 1)`, with declared per-technology ceilings: mobile S = 130 (permits multi-SIM/M2M), fixed broadband S = 100, internet use S = 100, smartphone S = 100. The ceilings are arbitrary but fixed; they rescale only, never reorder.
5. **Break handling.** At every break in Section 3: if the publisher supplies an overlap year under both definitions, splice with the ratio `r = new/old` in the overlap year, applied to all prior observations (chain-linking); if no overlap exists, insert a gap marker. **No interpolation without a flag; every splice recorded in metadata.**
6. **No imputation.** A missing year stays missing. The extrapolation flag attaches per series from its last measured year.

**What it assumes:** pure rescaling — no model fitting; saturation ceilings as declared; zero usage in excluded age bands.

**What it distorts:** late-period values compress against the ceiling differently by country (ageing populations cap internet/smartphone rates below 100 for years); mobile levels retain each country's M2M/SIM practices; the 3+/6+/adult zero-assumption flatters early smartphone numbers slightly.

**Invalid after application — do not use for:** cross-country mobile penetration levels at a point in time (M2M treatment differs); cross-country messaging and SNS levels (question wording differs, no harmonised indicator exists); internet-use cross-country comparisons before ~2015 (recall windows); any comparison mixing ACS (household, home-only) with individual-use series. **Valid after application:** within-country time paths for all subscription series and harmonised individual-use series; cross-country comparisons via ITU/OECD for mobile, broadband, and internet use in harmonised years.

---

## Section 6 — What cannot be sourced

- **Continuous generative-AI usage series, any of the three countries** — does not exist as a measured quantity as of early 2025 (§4).
- **Country-level vendor usage data** (OpenAI/Gemini/Meta AI by country) — not published; fragments in press only.
- **US dial-up 1996–1999 as an annual series** — does not exist at annual national frequency; only irregular CPS supplements (1994, 1997, 1998, 2000) and Pew predecessor polls. A 1996–2000 annual US dial-up line would be interpolation.
- **Korea generative-AI national survey** — status unknown to me: either published after my cut-off, published but not in my training data, or not yet fielded.
- **LINE / KakaoTalk in official statistics** — not isolated as official series (as far as I can attest); vendor earnings disclosures exist but are not statistics.
- **Harmonised social-web indicator (ITU/OECD)** — does not exist.
- **US ACS 2020 one-year estimates** — do not exist (pandemic; experimental weights only).
- **FCC subscription series after ~2023** — continuation under the Broadband Data Collection unknown to me.
- **Pre-2011 Japan individual internet-use methodology** — published but unverified by me; exists in MIC archives.
- **Korea distinct-person mobile penetration** — probable, details unknown.
- **ITU deep 1996–2000 household values** — likely in legacy publications, unverified by me; published but not confirmed accessible.

---

## Section 7 — Refusals and confidence

**Declined:** I gave no adoption values from memory (per the round's rules — an unsourced number is worse than a gap), made no post-early-2025 claims, and offered no view on the index's design or the underlying premise.

**Judgment on the one question:** **Yes, partially.** A defensible thirty-year, three-country diffusion series can be assembled for **four of the seven waves** — mobile telephony, fixed broadband, internet use, smartphones — at annual frequency from roughly 1996 to 2024, drawing on MIC (Japan), MSIT/KISA (Korea), Census/FCC/CTIA/Pew (US), harmonised through ITU/OECD, subject to these caveats: (1) every row needs live re-verification, since nothing here was checked against a live source; (2) roughly a dozen documented breaks (§3) must be spliced or flagged, never smoothed; (3) cross-country *level* comparisons are valid only for the ITU/OECD-harmonised indicators and only in harmonised years — the national series support cross-time, not cross-country, claims; (4) the US pre-2000 internet and dial-up record is genuinely sparse and cannot be made annual honestly. **Dial-up** is defensible for Japan and Korea but only as irregular points for the US before 2000. **Social web** is defensible as three national series from the mid-2000s (US) and early 2010s (JP/KR) but not as one comparable indicator. **Messaging** and **generative AI** cannot be sourced as continuous measured series at all: messaging rests on vendor announcements and one-off survey items, and generative AI on scattered polls beginning mid-2023 — for that wave, the institution's "no longer measured" line sits almost immediately after "first measured," and everything from early 2025 onward is beyond what any source can yet attest to in this document.