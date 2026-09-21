**Training cut-off: late 2024.** Every "last year" below means "last year I can attest"; most series presumably continue. All 2025–2026 cells, and any release after my cut-off, are outside what I can attest and are marked as such where relevant. Conventions: markets JP/KR/US; "cells" = 90 year-market cells (30 × 3); ~ = approximate; statuses are verified / probable / speculative as defined in your §3.

---

## Section 1 — Sources for execution restored

| kind of data | source name | publisher or holder | markets | first year | last year | what it observes | inference to the exposure | status |
|---|---|---|---|---|---|---|---|---|
| Official ICT statistics | Falling Through the Net (report series) | NTIA, US Dept. of Commerce | US | 1996 | 2000 | PC, modem, internet, telephone penetration by income, race, age, disability | Penetration among groups barred by cost/literacy/disability ≈ restored access; assumes adoption → use for correspondence; group-level only | verified |
| Official ICT statistics | CPS Computer and Internet Use supplements | US Census Bureau | US | 1997 | 2021 (irregular) | Household device/internet use, with disability cross-tabs in several waves | Same two-step inference; question wording changes across redesigns | verified |
| Official ICT statistics | 通信利用動向調査 (Communications Usage Trend Survey) | MIC / Statistics Bureau, Japan | JP | ~1996 (current form; earlier under other names) | 2024 | Device ownership; internet and mobile-email use rates by age | Mobile-email use among elderly/immobile ≈ contact restored; adoption only; no disability split | verified (start year in current form: probable) |
| Official ICT statistics | 인터넷이용실태조사 (Internet Usage Survey) | KISA | KR | ~1998 | 2024 | Internet/smartphone use rates by age, region, income | Two-step adoption inference | probable |
| Official ICT statistics | 정보화실태조사 + 디지털정보지수 (Digital Divide Index) | MSIT / NIA | KR | ~2002 (index series earlier) | 2024 | Use rates; divide index by age, region, disability in some editions | The divide index is the nearest official thing to a *rate of gap closure* — still adoption-level; index methodology revised over time | probable |
| Official ICT statistics | World Telecommunication Indicators / DataHub / IDI | ITU | JP/KR/US | 1996 | 2024 | Subscriptions, internet users, mobile broadband per country-year | National aggregates; restoration only inferred as access gap closing; practice-blind | verified |
| Assistive / clinical | SIPP assistive-technology topical modules | US Census Bureau | US | 1990/92/94 (pre-span) | 1994 | Use of communication aids and devices among disabled persons | Device use ≈ doing restored; direct but falls outside the span — baseline only | verified |
| Assistive / clinical | Medicare DME claims for speech-generating devices (HCPCS E2500–02) | CMS / OIG | US | 2001 | 2024 | Devices reimbursed for speech loss (ALS and similar) | Reimbursement ≈ persons regaining speech output; counts devices, not use; single market; single mechanism | probable (public granularity limited) |
| Assistive / clinical | FDA 510(k)/PMA registrations for AAC and speech devices | FDA | US | 1996 | 2024 | Approvals by year (supply side) | Approval → availability → use → restoration: long chain, zero demand information | verified |
| Assistive / clinical | 장애인실태조사; 장애인정보화실태조사 | KRIPH / Korea Institute for Disability Development / MOHW | KR | ~2000 | ~2020 | Device use and ICT use among persons with disabilities | Device/ICT use → restoration; waves every 3–5 years, instruments change | probable |
| Assistive / clinical | 補装具費支給実績 (assistive-device subsidy payments) | MHLW / prefectures | JP | ~2006 | 2024 | Subsidy payments for assistive devices (hearing aids clear; communication aids uncertain) | Payments ≈ devices delivered; whether speech devices are covered is itself uncertain | speculative |
| Assistive / clinical | EHIMA hearing-aid unit sales; EuroTrak (JP/KR/US); MarkeTrak (US) | EHIMA / Hearing Industries Association | JP/KR/US, uneven entry years | ~1996 | 2024 | Unit sales; ownership/use rates | Restored hearing-mediated communication (practice: **calling**); sales ≠ use | probable |
| Telecom regulator records | Annual TRS reports: TRS/VRS/IP CTS minutes | FCC | US | ~1996 | 2024 | Relay-call minutes for Deaf, hard-of-hearing, speech-disabled users | Minutes ≈ calls made that otherwise could not be (practice: **calling**); nearest to a direct restoration count in the round | verified |
| Survey research | Pew Internet & American Life tracking surveys | Pew Research Center | US | 2000 | 2021 | Adoption and communication activity (email, texting) by age, income, disability in special reports | Activity rates among excluded groups → restoration; self-report; item wording varies | verified |
| Survey research | docomo Mobile Society Research Institute annual surveys | NTT docomo | JP | 2004 | 2024 | Mobile email/SNS behaviour, family contact frequency, elderly use | Mobile mail restored contact for distant/immobile persons; self-report | probable |
| Survey research | WebAIM Screen Reader User Surveys | WebAIM, Utah State University | US-leaning global | 2009 | 2024 (biennial) | Screen-reader adoption among blind/low-vision users | Written correspondence restored for blind users; self-selected online sample | verified |
| Assistive / clinical | National ALS Registry prevalence; ALS Association / MDA clinic data | CDC-ATSDR; advocacy bodies | US | 2010 | 2024 | ALS prevalence; device-use items irregular | Denominator for speech-loss restoration; the restoration series itself is absent | probable |
| Denominator | UNESCO UIS literacy series; national census items | UNESCO UIS | JP/KR/US | 1996 | 2024 | Adult literacy share | Sizes the "never had it" pool; not the exposure itself — a scale factor | verified |
| Denominator | Disability denominators: ACS (US), 生活基礎調査 (JP, triennial), 등록장애인 statistics (KR, annual) | Census / MHLW / MOHW | one each | 1996 | 2024 | Share of population with communicative or mobility disability | Denominator for restoration; definitions drift across the three systems | verified (US/KR), probable (JP) |
| Platform disclosure | Skype then Zoom user disclosures | Microsoft / Zoom | global, US-weighted | 2005 | 2024 | Registered users, peak-day DAU | Distance-restoration of **meeting/calling**; letter-adjacent only via asking-after someone | probable |

Kinds used: six (official statistics; assistive/clinical; telecom regulator; survey research; denominators; platform).

---

## Section 2 — Sources for judgment substituted

| kind of data | source name | publisher or holder | markets | first year | last year | what it observes | inference to the exposure | status |
|---|---|---|---|---|---|---|---|---|
| Platform disclosure | Gmail Smart Reply / Smart Compose usage disclosures | Google | global, US-weighted | 2017 | 2024 | Share of replies machine-drafted (once cited ~10% of mobile replies); not maintained as a series | System-drafted, human-sent: the content decision is handed over; 1 inference step, but email replies only, no country split | probable |
| Platform disclosure | Grammarly user metrics and suggestion-acceptance figures | Grammarly | US-led global | 2013 | 2024 | Users, DAU; occasional "corrections accepted" counts | Wording decisions partially delegated; intensity unobserved | probable |
| Platform disclosure | Google Translate usage disclosures | Google | global | 2006 | 2024 | Milestone user/volume counts | Wording handed over for translated content; no country-year granularity | probable |
| Platform disclosure | Papago usage in Naver earnings/PR | Naver | KR (+JP corridors) | 2016 | 2024 | MAU / translation counts | MT use in KR–JP–EN corridors; DAU ≠ letter content | probable |
| Carrier press data | 年賀メール New Year traffic (docomo/au/SoftBank releases) | Mobile carriers | JP | ~2000 | ~2016 | Messages sent on 1 January | The composed greeting migrated to template/short-form channel; authorship unobserved; archived only in press releases | probable |
| Carrier press data | 설날·추석 문자 traffic (SKT/KT/LGU+ releases) | Mobile carriers | KR | ~2001 | ~2015 | Holiday message surges | Same as above | probable |
| Postal official | 年賀はがき受付・発行数 (New Year card volumes) | Japan Post | JP | 1996 | 2024 | Cards issued/delivered annually — peak and decline | Decline read as composition migrating to digital; mechanism and authorship unobserved | verified |
| Postal official | Letter-post volume series (郵便物数) | Japan Post | JP | 1996 | 2024 | Items posted | Practice volume only; several steps to substitution | verified |
| Postal official | 우편물 취급량 | Korea Post (우정사업본부) | KR | 1996 | 2024 | Items posted | Same | probable |
| Postal official | Household Diary Study | USPS | US | 1996 | ~2019 (later waves uncertain) | Household mail by type incl. personal correspondence; email-substitution questions | The round's best direct observation of the practice itself declining; authorship still unobserved | verified |
| International official | UPU postal statistics (letter post items) | Universal Postal Union | JP/KR/US | 1996 | 2024 | Letter-post items per country-year | Comparable practice volume; no content | verified |
| Commercial estimates | Email volume estimates | Radicati Group and similar | global | 1996 | 2024 | Emails sent per day | Substitute volume; method opaque; no market split | probable |
| Industry | SMS/MMS volumes | CTIA Wireless Industry Survey | US | ~2002 | 2024 | Texting volume | Substitute volume; content unobserved | verified |
| Platform disclosure | KakaoTalk daily message volume | Kakao | KR | ~2014 | 2024 | Messages per day on the dominant Korean channel | Includes greetings/asking-after; sticker-and-template share unsplit | probable (granularity) |
| Platform disclosure | LINE MAU and usage disclosures | LINE / LY Corp | JP | 2011 | 2024 | Adoption of the dominant Japanese messenger | Channel migration of composed messages | verified (existence of disclosures) |
| Survey research | Gallup and Pew letter-writing / email-substitution polls | Gallup / Pew | US | 1990s–2024, sporadic | 2024 | Self-reported letter frequency; substitution attitudes | One step if the item probes *why*; sporadic | probable |
| Survey research | 内閣府 older-persons surveys; 総務省 media-action surveys | Cabinet Office / MIC | JP | ~2000 | 2024 | Contact-method shares (letter / phone / email), media behaviour | Population-level substitution; item availability uneven | probable |
| Survey research | KISDI Media Panel Survey; 한국언론재단 미디어이용실태조사 | KISDI / Korea Press Foundation | KR | 2010 / ~2005 | 2024 | Messaging and SNS use, media time | Adoption of assembled-communication channels | probable |
| Industry association | Greeting-card digitisation: Greeting Card Association estimates, e-card services, wedding-invitation printers | Industry bodies / vendors | US/JP | 1996 | 2024 | Card sales trend; e-card launches; template printing share | Pre-written content bought = judgment outsourced at purchase (practices: **gifting, asking-after**); series fragmented | probable |
| Carrier / official | Telegram volumes (電報・祝電) | NTT / MIC | JP | 1996 | ~2008 | Telegrams sent | Menu-phrase telegrams = partial judgment hand-over long predating digital; dying series | probable |
| Platform disclosure | Voice-assistant adoption (Alexa, Hey Google, NUGU, Clova) | Vendor IR disclosures | US/JP/KR | ~2015 | 2024 | Device sales/subscribers (e.g., NUGU cumulative subscribers) | "Send a message" intent counts are not public; adoption only | probable (adoption); speculative (intents) |
| Telemetry (not public) | Input-method logs: autocorrect acceptance, suggestion uptake | Keyboard vendors | all | 1996 | 2024 | Would record assistance at decision/word level | The direct measure of judgment substitution; held privately, no series | speculative |
| Platform disclosure | LLM writing-assistant usage claims | OpenAI and others | global | 2022 | 2024 | Claimed users/messages; no country-year series | Maximal composition hand-over; measurement immature; within my window only 2022–24 | speculative |
| Corpora | Newspaper-archive term series (手紙→メール; 편지→문자; letter→email) | 聞蔵 / NAVER News Library / ProQuest | JP/KR/US | 1996 | 2024 | Mention-frequency shift | Discourse proxy; three-plus steps from behaviour | speculative (as measurement; archives verified) |
| Service industry | 代筆 / ghost-writing services (letter-writing shops, invitation houses) | none known | JP/KR/US | — | — | Would record whole-composition delegation | No series exists in any market | speculative |

**Sources that separate who wrote from who sent, or record assistance at decision level** (per your §4 request): Gmail Smart Reply share (system-drafted, human-sent — the closest); Grammarly accepted-suggestion figures (suggestion level, not keystroke level); input-method telemetry (decision level, not public); AAC clinical session notes (spontaneous sentence vs. banked phrase — exists clinically, never aggregated); 代筆 services (whole-composition delegation — no series anywhere).

---

## Section 3 — Sources that observe both, or the boundary between them

| source | markets | years | what it observes | reads as execution-restored when… | reads as judgment-substituted when… | what in the source would tell the two apart | status |
|---|---|---|---|---|---|---|---|
| Predictive text / T9 / autocorrect | all | 1996–2024 | Word and phrase completion in every text-entry device | Word completion, spelling repair (motor, literacy) | Phrase and emoji suggestion, auto-greetings | Accept-rate telemetry by suggestion type — private to keyboard vendors | probable (tech exists); speculative (series) |
| Smart Reply / Smart Compose | global | 2017– | Share of replies machine-drafted | Typing effort saved | Content chosen by system | Google's own suggest-vs-draft framing hints at the split; no per-message public data | probable |
| Machine translation (Translate, Papago) | JP/KR/US | 2006– / 2016– | Translation volume | Restores the doing across language distance (diaspora, deaf-interpretation of text) | Auto-suggested phrases hand over "how are you" whole | Would need a split of user-typed source text vs. app-suggested templates — not public | probable (use); speculative (split) |
| Speech-to-text dictation | all | ~2008– | Voice-typed messages | Restores writing for motor-impaired and low-literacy users | Auto-punctuation and rewrite co-author the phrasing | Edit-distance logs (spoken text vs. final text) — not public | probable (adoption); speculative (split) |
| AAC / speech-generating devices with phrase prediction | US (JP/KR sparse) | 1996– | Device claims, approvals | Restores speech output itself | Phrase banks pre-shape content at device setup | Spontaneous-vs-banked split exists in clinical notes; never aggregated into a series | verified (devices); speculative (split) |
| Voice synthesis from a learned voice (Project Revoice, VocaliD class) | US; JP/KR unknown | ~2015– | Case studies, vendor claims | Restores the speaker's own voice — the doing | If the system also composes the message | Nothing public; case documentation only | speculative |
| Email templates / canned responses | all | 2000s– | Feature presence | Formatting effort removed | Content taken from templates | No usage series at all | speculative |
| Summarisation (mail digests, message summaries) | all | ~2018– | Feature launches | Time restored | What to attend to / reply decided by system | No usage series | speculative |
| Channel-migration volume pairs (letters vs. email / SMS / LINE / KakaoTalk) | all | 1996– | Volume on both sides of the swap | Adopters barred from mail by cost, distance, illness → restoration | Adopters delegating composition to short-form templates → substitution | Only adopter-motivation data would split them; asked only in scattered one-off surveys | verified (volumes); speculative (split) |
| Holiday greeting pair: 年賀状 decline vs. 年賀メール counts; 설날 문자 | JP/KR | 1996–2016 | Both sides of the greeting's migration | Sending at all from sickbed or distance | Templates and copy-paste = composition delegated | Nothing in the sources distinguishes; press releases count messages only | probable |
| Voice assistants executing "send a message" | all | ~2015– | Device adoption; intents private | Speech UI restores sending for visually/motor-impaired | Assistant drafts or asks clarifying questions = shared judgment | Vendor intent logs would split dictated content from assistant-drafted — not public | probable / speculative |
| Handwriting-recognition input (Graffiti → Apple Scribble; 手書きIME) | all | 1996– | Product launches only | Restores pen-like input for those who cannot type | Kills the handwritten artifact LETTER is defined on | Usage series absent; device-shipment data as weak proxy | probable (launches); speculative (use) |

---

## Section 4 — A first sort by quantity and quality

Grouped by kind. Quantity = cells of 90 filled. Quality = inference steps between what is counted and the exposure, plus definitional stability.

**Official ICT statistics**
- ITU indicators / IDI — Quantity 90/90. Quality: 2 steps; definitions harmonised and stable; practice-blind, weakest substantive link.
- 通信利用動向調査 (MIC) — Quantity ~29/30 (JP). Quality: 2 steps; stable instrument with mid-2000s redesign.
- 인터넷이용실태조사 (KISA) — Quantity ~27/30 (KR, from ~1998). Quality: 2 steps; stable.
- 정보화실태조사 / 디지털정보지수 — Quantity ~20/30 (KR). Quality: 2 steps, but the divide-index is the nearest to measuring restoration directly; index revisions cause drift.
- CPS Computer & Internet Use — Quantity ~14/30 (US, irregular waves). Quality: 2 steps; item drift at each redesign.
- NTIA Falling Through the Net — Quantity 4/30 (US, 1996–2000). Quality: 2 steps but with direct disability/income splits; series dies in 2000.

**Assistive-technology and clinical**
- Medicare SGD claims — Quantity ~24/30 (US, 2001–). Quality: 1 step to "speech restored," the shortest chain in the round; counts devices not use; narrow practice.
- FCC TRS/VRS minutes — Quantity ~29/30 (US). Quality: 1 step for calling-restoration; stable definition; single practice.
- FDA approvals — Quantity: event-level, ~30 entry markers, not a series. Quality: 3 steps (approval → availability → use → restoration).
- 장애인실태조사 — Quantity ~7/30 (KR, periodic). Quality: 2 steps; instruments change between waves.
- 補装具支給実績 — Quantity ~19/30 (JP). Quality: 2 steps; coverage of communication aids uncertain — definitional fragility. speculative.
- EHIMA / EuroTrak / MarkeTrak — Quantity ~15/90 (uneven country entry). Quality: 2 steps (sales → use); sales ≠ fit.
- SIPP AT panels — Quantity 0/90 (pre-span). Quality: 1 step; snapshot baseline only.
- ALS Registry — Quantity ~15/30 (US). Quality: denominator only — 0 steps to the exposure, needed as a scale factor.

**Postal statistics**
- USPS Household Diary Study — Quantity ~24/30 (US). Quality: 1–2 steps; the most stable instrument aimed at the practice itself.
- Japan Post 年賀状 series — Quantity ~29/30 (JP). Quality: 0 steps to practice volume, 2–3 to substitution; single-practice and crisp.
- UPU letter-post statistics — Quantity 90/90. Quality: 0 steps to volume, 3+ to either exposure; stable.
- Japan Post / Korea Post volume series — Quantity ~29/30 each. Quality: same profile.

**Survey research**
- Pew tracking — Quantity ~22/30 (US). Quality: 2 steps; item wording drifts study to study.
- docomo Mobile Society Research Institute — Quantity ~21/30 (JP). Quality: 2 steps; instrument evolves annually.
- KISDI panel / 언론재단 실태조사 — Quantity ~15–20/30 (KR). Quality: 2 steps.
- 内閣府 / 総務省 older-persons and media surveys — Quantity ~15–20/30 (JP). Quality: 2 steps; relevant items unevenly present.
- WebAIM surveys — Quantity ~8 waves (≈8/90). Quality: 2 steps; self-selected sample; biennial.
- Gallup/Pew letters polls — Quantity ~5/30 (US). Quality: 2 steps; sporadic.

**Platform and commercial disclosures**
- Gmail Smart Reply share — Quantity ~8/90 (2017–24, global-as-three). Quality: 1 step — the nearest to decision-level authorship anywhere; not a maintained series; no country split.
- Papago — Quantity ~9/30 (KR, 2016–). Quality: 2 steps.
- KakaoTalk message volume — Quantity ~11/30 (KR). Quality: 2 steps.
- LINE — Quantity ~14/30 (JP). Quality: 2 steps.
- Grammarly — Quantity ~12/90 (global-as-three). Quality: 2 steps.
- CTIA SMS volumes — Quantity ~23/30 (US). Quality: 2 steps.
- Google Translate disclosures — Quantity ~19/90 (global-as-three, milestone only). Quality: 2 steps; not annual.
- Carrier holiday-traffic releases — Quantity ~10/30 JP + ~10/30 KR. Quality: 2 steps; press-release methodology, unstable.
- Voice-assistant adoption — Quantity ~10/90. Quality: 3 steps; the decisive intent data are missing.
- LLM usage claims — Quantity ~3/90 (2022–24). Quality: 3 steps; speculative.
- Radicati email estimates — Quantity: global only, no country cells. Quality: 3 steps; opaque method.
- Skype/Zoom — Quantity ~10/90. Quality: 2 steps; adjacent practices only.

**Patents and product timelines**
- Patent counts (USPTO/JPO/KIPRIS) — Quantity 90/90. Quality: 3–4 steps; classification drift; fills cells cheaply and emptily.
- Product-launch timelines — Quantity: markers only. Quality: 3 steps.

**Corpora and archives**
- Newspaper corpora — Quantity ~90/90 (archives exist for all three markets). Quality: 3 steps; discourse is not behaviour.
- Google Books Ngram — Quantity ~37/90 (JP corpus ends ~2008–2012; KR weak). Quality: 3 steps.
- Oral histories (StoryCorps, postal museums) — Quantity ~0 cells. Quality: qualitative mechanism evidence; no quantitative fill.

---

## Section 5 — What no source covers

1. **Authorship, all markets, all years.** No source anywhere in the ninety cells observes who wrote the content versus who sent it. The nearest approximations are Gmail Smart Reply share (2017 onward, global, email replies only) and private keyboard telemetry (not public). The needed instrument is a per-message authorship record — a diary or telemetry item asking "did the system draft this, how much of it."
2. **Judgment substituted before ~2004.** Except for greeting-card/template industries and telegram stock-phrase menus, nothing measures who decided the content of a greeting, letter, or message in 1996–2004 in any of the three markets. The T9-era assistance left no public trace.
3. **The restoration counterfactual.** No repeated series asks adopters *why* they adopted — whether the technology restored something they had lost (illness, distance, cost, literacy) or merely sped up what they could already do. This distinction underlies the whole exposure, and only scattered one-off surveys (Pew specials; SIPP snapshots before the span) touch it. A yearly barrier-attributed adoption survey would cover it; none exists.
4. **Disability-disaggregated ICT use, Japan, all years.** Japan has no yearly series on internet/communication-technology use among persons with disabilities. Korea is sporadic from ~2000; the US is best but irregular.
5. **Speech restoration outside the US.** The reference case — a speech decoder for someone with ALS — has a usable paper trail only in the US (Medicare SGD claims from 2001, FDA approvals). Japan's 補装具 data on communication aids is uncertain to nonexistent; Korea's AAC device coverage is not publicly compiled. JP/KR cells for this exposure are speculative only.
6. **Voice synthesis from a learned voice.** Usage counts exist nowhere; only case studies (Project Revoice ~2018, VocaliD). JP/KR: nothing at all.
7. **2025–2026, every exposure, every market.** Entirely outside my attestation; even publishers' releases after late 2024 are unknown to me. Thirty of the ninety cells cannot be filled from this round at all.
8. **Assistance intensity at the decision level.** No source, any year, records how much of a message was system-proposed versus person-written. Vendors hold this; it has never been published as a series.
9. **Korea 1996–1997.** Internet-era Korean statistics begin ~1998; the first two Korean years are thin for both exposures.

The common weakness, stated once: nearly every source counts adoption or use of a *channel or device*; both exposures sit behind it — behind (a) practice-level use of that channel, (b) the adopter's counterfactual ability, and (c) decision-level authorship. No public source observes (b) or (c) annually in all three markets.