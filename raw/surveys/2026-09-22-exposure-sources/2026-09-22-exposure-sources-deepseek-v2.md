**Training cut-off:** My knowledge extends to early 2025. Items marked after that date are outside what I can attest from training; where searches returned post-cut-off material, I note it but cannot independently confirm the source's continued existence or exact form.

---

## Section 1 — Sources for execution restored

This section collects sources that observe the *doing* of LETTER — the physical composition, handwriting, and release of a message — and the technological restoration of that doing to people who lost it or never had it. The reference case is a speech decoder for a person who lost speech to ALS, transposed to the handwritten letter: a person who cannot physically write but whose hand, via technology, produces the marks.

| kind of data | source name | publisher or holder | markets | first year | last year | what it observes | inference to the exposure | status |
|---|---|---|---|---|---|---|---|---|
| Assistive-technology product registries | ABLEDATA | AbleData / OK.gov (US) | US | 1990s (database era) | 2010s (archive) | Product listings for assistive technology, including voice output programs, communication boards, computer access devices | Product *existence* only; no adoption or use counts. Inference: if a handwriting-alternative input device exists in the registry for a given year, execution restoration was technologically *possible*. Very weak — existence ≠ access ≠ use. | verified |
| Assistive-technology product registries | Act-navi (情報アクセシビリティ支援ナビ) | MIC / NICT (Japan) | Japan | 2020 (constructed) | present | Database of ICT products/services for disability and aging, including communication support | Same as ABLEDATA: product existence. Japan-specific, so fills JP cells only from 2020 forward. | verified |
| Assistive-technology product registries | Korea National Assistive Technology Center (KNAT) DB | National Rehabilitation Center (Korea) | Korea | ~2010s | present | Domestic assistive-device database by activity, including communication devices | Product existence, with activity-based categorization. Inference to *restoration* requires knowing whether the device restores *handwriting* specifically, not just communication. | verified |
| Assistive-technology product registries | 意思疎通支援機器選択データベース (Communication Support Device Selection DB) | Chubu Gakuin University / MHLW grant | Japan | ~2010s | present | Searchable database of communication support devices, including writing alternatives | Product existence and institutional coverage (public funding eligibility). Inference: coverage in the public funding system suggests accessibility, not use. | probable |
| Assistive-technology service data | National Assistive Technology Act Data System (NATADS) | CATADA / US Dept. of Education | US | 1998 (AT Act) | present | Device demonstrations, device loans, and state-level AT program activity; speech communication devices are the most-demoed category | Demo and loan counts. Inference: a demo of a speech communication device indicates that a person *tried* restoration technology. Weak: demo ≠ adoption ≠ ongoing use. | verified |
| Assistive-technology service data | Korea NDS assistive technology module (2017 National Disability Survey) | Korea Institute for Health and Social Affairs / MOHW | Korea | 2017 | 2017 (survey wave) | Whether respondents *have*, *use*, and are *satisfied with* assistive products, including communication devices | Having/using an AP is closer to the exposure than mere product existence. Inference: "uses a communication AP" ≈ execution restored for that person's communication practice. Still one step away from *handwriting* specifically. | verified |
| Assistive-technology service data | Japan MHLW grants database (意思疎通支援機器) | MHLW / National Institute of Public Health | Japan | ~2010s | present | Devices covered under public funding for communication support; product lists with institutional relationships | Funding eligibility and device lists. Inference: if a handwriting-alternative is publicly funded, cost barrier is reduced, so restoration exposure rises. Weak on use. | probable |
| Clinical / disability surveys | Japan MHLW disability survey (communication equipment module) | MHLW (Japan) | Japan | Various waves (e.g., 2006, 2011, 2016) | Present (periodic) | Whether people with disabilities use communication devices, mobile phones, email, etc.; includes some handwriting/communication questions | Usage rates by disability type. Inference: if a person with a writing disability reports using a communication device, execution restoration may be inferred. But most items are *communication* generally, not *handwriting*. | verified |
| Clinical / disability surveys | Korea 2017 National Disability Survey (AT module) | MOHW / KIHASA (Korea) | Korea | 2017 | 2017 | Need, possession, use, and satisfaction with assistive products; 21 products are provided through NHIS | Use of a communication AP → execution restored for that practice. Definition of "communication AP" may include writing alternatives. | verified |
| Clinical / disability surveys | US National Survey of Children's Health / Disability supplements | US Census / HRSA | US | varies | varies | Assistive technology use among children with disabilities, including communication devices | General AT use. Inference to handwriting restoration is weak unless the survey item specifies writing. | probable |
| Handwriting recognition benchmarks | IAM Handwriting Database | University of Bern (Marti & Bunke) | Global (used in US/EU/Asia) | 1999 (first release) | present (v3.0) | Offline handwriting samples; error rates (CER/WER) of recognition systems on IAM test sets | CER is a *technological capability* measure, not a human restoration measure. Inference: if CER drops below a threshold, a person who cannot write could dictate and have their handwriting *synthesized* or *recognized*. Very weak: benchmark CER ≠ field performance for assistive use. | verified |
| Handwriting recognition benchmarks | ICDAR competitions (handwriting recognition) | ICDAR / academic community | Global | 2005 | present | Benchmark results on Arabic, Latin, and other handwriting datasets | Same as IAM: capability, not restoration. But year-by-year CER trends can proxy the *possible* restoration. | verified |
| Handwriting recognition benchmarks | ScaDS.AI German handwriting datasets | ScaDS.AI (Dresden/Leipzig) | Global | ~2020s | present | Line/word-level and full-page handwritten text data with ground truth | Capability measure. Weak inference to restoration. | probable |
| Voice synthesis / voice banking | ALS voice banking studies (e.g., Acapela, Team Gleason, ElevenLabs programs) | Various (ALS Schweiz, Team Gleason, academic groups) | US, EU, Japan (scattered) | 2010s | present | Whether ALS patients bank their voice; perceptual quality of synthetic voice; number of requests for voice-banking services | Requests or bankings → execution *restored for speech*, not for handwriting. Inference to LETTER requires transposing voice restoration to written composition: a person who cannot write could dictate and have their voice (or synthesized voice) converted to text. Additional step. | probable |
| Voice synthesis / voice banking | Team Gleason Foundation service requests | Team Gleason (US) | US | 2017 | 2022 (data points) | Number of requests for voice/AAC services (172 in 2017 → 1,200 in 2022) | Requests for service → demand for execution restoration. Inference: demand ≈ attempted restoration. Does not measure whether restoration succeeded or was used for *letters*. | probable |
| Speech recognition accuracy | DARPA / NIST speech recognition benchmarks (Switchboard, etc.) | DARPA / NIST (US) | US (global use) | 1990s | 2010s | Word error rate (WER) on conversational speech; milestones: 8% (IBM 2015), 6.3% (Microsoft 2016), 5.1% (Microsoft 2017) | WER is technological capability. Inference: lower WER → dictation-as-writing becomes more feasible → execution restoration for people who cannot write. But dictation is not *handwriting*; it is a different doing. One step away. | verified |
| Speech recognition accuracy | IPA (Japan) surveys of speech recognition accuracy | IPA (Japan) | Japan | 2015 | 2017 (data points) | Japanese-language speech recognition accuracy milestones | Same as NIST, but Japan-specific. | probable |
| Patent timelines | Google Patents / USPTO handwriting recognition patents | Google / USPTO | US (global filings) | 1995 | present | Filing and grant dates for handwriting recognition, synthesis, and integrated telephony-handwriting-speech systems | Patent existence → technological *possibility* of restoration. Extremely weak inference: patents ≠ products ≠ access. But useful for dating capability waves. | verified |
| Patent timelines | JPO / KIPRIS patent databases | JPO (Japan) / KIPRIS (Korea) | Japan, Korea | 1990s | present | Handwriting and communication-device patents in JP and KR | Same as above, market-specific. | probable |
| Postal volume data | Japan Post letter-mail volume statistics | Japan Post / MIC | Japan | 1956 (series) | present | Domestic letter-mail volume by year; peak ~26.2 billion in FY2001, declining ~45% by FY2022 | Volume of letters sent. Inference: *aggregate* letter volume declines as digital communication substitutes. Does NOT measure how many letters were *restored* to people who could not write. It measures the practice's total doing, not the restoration exposure. Very weak for this exposure. | verified |
| Postal volume data | Korea Post domestic mail volume statistics | Korea Post / KOSIS | Korea | 1994 (series) | present | Domestic mail volume by year; 1996: 3.78 billion items | Same as Japan Post: aggregate volume, not restoration. | verified |
| Postal volume data | USPS First-Class Mail volume | USPS | US | 1926 (series) | present | First-Class Mail pieces by year; 1996: 98.2 billion; declining to ~46 billion by FY2023 | Same as above: aggregate volume, not restoration. Useful as a denominator or context variable, not as a direct measure of restoration. | verified |
| Oral history / digitised corpora | War letters digitisation projects (e.g., NIOD "First-Hand Accounts of War," 2020–2023) | NIOD (Netherlands), various archives | Global (EU-centric) | 2020 | 2023 | Digitised handwritten wartime letters; metadata on writers, dates, content | Corpus of *past* handwritten letters. Inference: if a corpus exists, researchers *can* study handwriting, but this does not observe restoration in the 1996–2026 span. Only useful for baseline/historical context. | verified |
| Oral history / digitised corpora | Newberry Transcribe / Civil War in Letters | Newberry Library (US) | US | 2013 | present | Crowdsourced transcription of handwritten letters | Transcription activity → interest in handwriting, but not restoration exposure. | probable |

---

## Section 2 — Sources for judgment substituted

This section collects sources that observe the *deciding* of LETTER — the deliberation over what to say, how to phrase it, the consequential choice of content — and the technological substitution of that deliberation. A system that translates "how are you" hands over the deliberation whole. A system that suggests the next word may or may not.

| kind of data | source name | publisher or holder | markets | first year | last year | what it observes | inference to the exposure | status |
|---|---|---|---|---|---|---|---|---|
| Autocomplete / predictive text | Chrome autocomplete field statistics | Google (Chrome DevRel) | Global (US, JP, KR included) | ~2015 (data published) | present | Form abandonment reduction (75%), time reduction (35%) when autocomplete is used | Autocomplete use → the system completes the *doing* of typing. Inference to *judgment* substitution: if the system suggests the word/phrase and the user accepts, the choice of wording is partially handed over. Strength depends on whether the user *deliberates* over the suggestion. Source does not distinguish. Weak for judgment substitution alone. | probable |
| Autocomplete / predictive text | Google autocomplete savings statistics (200 years of typing per day; 25% input reduction) | Google (blog/announcements) | Global | 2010s | present | Estimated time/keystrokes saved by autocomplete | Same as above: doing saved. Inference to judgment requires knowing whether the user *would have* chosen a different word without the suggestion. Source does not capture this. | probable |
| Autocomplete / predictive text | Academic studies on word-prediction adoption (e.g., ETH Zurich research on typing strategy trade-offs) | Academic (various) | Global (EU/US) | 2010s | present | Whether users use suggestions despite decreased performance; cognitive cost of prediction | Use of suggestions → the user *chooses* to accept the system's word. Inference: if acceptance is habitual, deliberation over that word is reduced. Closer to judgment substitution, but still requires an interpretive step. | probable |
| Machine translation | DeepL / Google Translate usage surveys (Japan) | Various (DeepL, academic surveys) | Japan | 2020s | present | 42.9% use free MT for work; 37.6% use generative AI for translation; 36% of university students submit AI translations directly | Use of MT → the system produces the translated content. Inference: if the user submits the MT output without correction, the *judgment* over how to phrase the foreign-language letter is handed over. The survey distinguishes "used directly" vs. "checked and corrected" in some items — this is the key separator. | probable |
| Machine translation | Korean university student MT perception survey (2024) | KCI journal | Korea | 2024 | 2024 | Perception and use patterns of MT among university students | Use + perception. Inference: if students use MT for coursework and accept output, judgment substitution is present. The survey includes attitude items, which may help distinguish deliberation from blind acceptance. | probable |
| Machine translation | Machine translation adoption dynamics (global, 2020–2025) | Various (hispadoc.es synthesis) | US, Asia (JP/KR/CN) | 2020 | 2025 | Market share of MT in translation services: USA 42%→50%; Asia 36%→41%→52% | Market-level adoption → aggregate judgment substitution. Inference: if a larger share of translation is machine-performed, more consequential choices about wording are handed to the system. But this is *market* data, not individual practice data. One step away. | speculative |
| Summarisation | Enterprise AI summarisation adoption (Gartner 2025) | Gartner | Global (US-heavy) | 2023 | 2025 | 41% enterprise adoption of AI summarisation, up from 18% in 2023 | Adoption → the system produces the summary. Inference: if a person uses summarisation to *understand* a letter or to *compose* one, the deliberation over what matters is handed over. But the source measures enterprise adoption, not personal letter-writing. Two steps away. | probable |
| Summarisation | NTT Docomo Mobile Society Research Institute survey (Japan, 2025) | NTT Docomo | Japan | 2025 | 2025 | 37% of generative-AI users use it for "text generation, summarisation"; 46% for search/information gathering | Use category. Inference: "text generation" use → the system may produce content the user would otherwise deliberate over. Does not separate *composition* of a personal letter from other text generation. | probable |
| Summarisation | AI meeting-notes usage surveys (Korea, 2026) | Buzzni / ZDNet Korea | Korea | 2026 | 2026 | Industry breakdown of AI meeting-note usage; IT/AI/SaaS 16.4%, commerce 12.9%, etc. | Meeting summarisation → the system decides what was important in the meeting. Inference to LETTER: analogous to summarising a conversation into a message, but not the same practice. One step away. | probable |
| Content generation / writing assistants | GitHub Copilot adoption statistics (NTT Docomo, Japan) | NTT Docomo / IT Leaders | Japan | 2023 | 2025 | 3,647 developers using GitHub Copilot (Nov 2025) | Code generation → the system writes code. Inference to LETTER: very weak. Different practice. Included only as a boundary case. | probable |
| Content generation / writing assistants | Generative AI usage surveys (Japan, 2025) | Glocom / NTT Docomo | Japan | 2025 | 2025 | 65.1% use generative AI for research/search; 45.5% for summarisation; 31.9% for translation | Use categories. Inference: "summarisation" and "translation" are closer to judgment substitution than "search." But the survey does not ask whether the output is used *as* the final message. | probable |
| Voice synthesis from learned voice | ALS voice-banking perceptual studies | Academic (various) | US, EU, Japan (scattered) | 2010s | present | Whether listeners perceive synthetic voice as close to original (e.g., "75% close"); intelligibility and naturalness ratings | Perceptual quality → the *doing* of speech is restored. Inference to judgment: a voice clone that speaks in the person's voice does not decide *what* to say; it only restores the *how*. This is execution restoration, not judgment substitution, unless the system generates content autonomously. | verified |
| Voice synthesis from learned voice | ElevenLabs voice-cloning programs (ALS, trauma) | ElevenLabs | US, global | 2023 | present | Free AI voice cloning for people who lost voice | Same as above: voice restoration is execution, not judgment. Included here to mark the boundary. | probable |

---

## Section 3 — Sources that observe both, or the boundary between them

Sources in this section can be read as restoration or substitution depending on intensity. The key separator is whether the system *produces content the person would have deliberated over* or merely *executes a decision the person has already made*.

| source | what it observes | what would let the two be told apart | status |
|---|---|---|---|
| Google autocomplete field statistics | Form completion behaviour; time saved | Whether the user *reads and accepts* a suggested phrase vs. *types the phrase themselves*. The source does not record this. If the suggestion is accepted without review, it is closer to substitution; if reviewed and rejected/edited, closer to restoration. | probable |
| Machine translation surveys (Japan, Korea) | Whether users check and correct MT output vs. submit directly | The item "used directly" vs. "checked and compared" is the separator. Direct submission → judgment substituted (the system chose the wording). Checked and corrected → the system restored the *doing* while the user retained the *deciding*. | probable |
| Voice banking / voice synthesis | Perceptual quality of synthetic voice; use in AAC | Whether the system *generates* content (e.g., predictive phrases) or only *speaks* content the user composed. If the user composes the letter and the system speaks it in their voice, it is execution restored. If the system suggests what to write, it crosses into judgment substitution. | probable |
| Summarisation tools | Adoption and use categories | Whether the user uses the summary as a *draft* they then revise (restoration of doing) or as the *final* understanding/message (substitution of judgment). Enterprise adoption data cannot tell this apart. | probable |
| Predictive text academic studies | Whether users accept suggestions despite performance cost | Acceptance rate alone is ambiguous. If the user accepts suggestions *because* they trust the system's choice, judgment is substituted. If they accept because it saves keystrokes while they already knew the word, it is execution restored. The source does not distinguish motivation. | probable |
| Handwriting recognition benchmarks (IAM, ICDAR) | CER/WER on benchmark sets | Low CER means the system can *read* handwriting. This is restoration if the person *wrote* the marks (even via an alternative input) and the system transcribes. It is substitution if the system *generates* the marks from a prompt. The benchmark does not separate these. | verified |
| Speech recognition accuracy benchmarks (NIST, IPA) | WER on conversational speech | Low WER means dictation becomes feasible. If the person dictates a letter they composed, the system executes the transcription (restoration of doing). If the system composes the letter from a prompt, judgment is substituted. The benchmark only measures transcription accuracy, not composition. | verified |

---

## Section 4 — A first sort by quantity and quality

Not a selection. Two marks per row: **Quantity** = how many year-market cells of the 90 (30 years × 3 markets) the source fills. **Quality** = number of inference steps between what it counts and the exposure, and whether the definition holds steady.

### Assistive-technology product registries

| source | Quantity (of 90) | Quality (inference steps; definition stability) |
|---|---|---|
| ABLEDATA | ~30–40 (US only, 1990s–2010s; JP/KR not covered) | 3–4 steps: existence → availability → access → use → restoration. Definition (product listing) holds steady. |
| Act-navi (Japan) | ~6 (JP only, 2020–2026) | 3–4 steps: same as ABLEDATA. Definition holds. |
| KNAT DB (Korea) | ~15–20 (KR only, ~2010s–present) | 3–4 steps. Definition holds. |
| Communication Support Device DB (Japan) | ~15–20 (JP only) | 3–4 steps. Definition holds. |
| NATADS (US) | ~25 (US only, 1998–present) | 2–3 steps: demo/loan → adoption → use. Demo ≠ use is the biggest gap. Definition holds. |
| Korea NDS AT module | 1 (KR, 2017 only) | 1–2 steps: use of AP → restoration. Definition holds but single wave. |

### Clinical / disability surveys

| source | Quantity (of 90) | Quality |
|---|---|---|
| Japan MHLW disability survey | ~10 (JP only, periodic waves) | 2–3 steps: device use → communication restoration → handwriting restoration. Most items are general communication, not handwriting-specific. |
| Korea 2017 NDS AT module | 1 (KR, 2017) | 1–2 steps: AP use → restoration. Strong but single-year. |
| US National Survey of Children's Health | ~10 (US only) | 3–4 steps: AT use → communication → handwriting. Weak. |

### Handwriting recognition benchmarks

| source | Quantity (of 90) | Quality |
|---|---|---|
| IAM Handwriting Database | ~27 (global, 1999–present; applies to all three markets as capability) | 2–3 steps: CER → capability → feasible restoration. Definition (CER on benchmark) holds. |
| ICDAR competitions | ~21 (global, 2005–present) | 2–3 steps. Holds. |
| ScaDS.AI datasets | ~5 (global, ~2020s–present) | 2–3 steps. Holds. |

### Speech recognition accuracy

| source | Quantity (of 90) | Quality |
|---|---|---|
| DARPA/NIST benchmarks | ~25 (US-led, 1990s–2010s) | 2–3 steps: WER → dictation feasibility → restoration. Holds. |
| IPA (Japan) accuracy data | ~3 (JP, 2015–2017) | 2–3 steps. Holds. |

### Voice synthesis / voice banking

| source | Quantity (of 90) | Quality |
|---|---|---|
| ALS voice banking studies | ~10 (US/EU/JP scattered, 2010s–present) | 2–3 steps: banking → voice restoration → (transposed) writing restoration. Additional transposition step from speech to writing. |
| Team Gleason service requests | ~5 (US, 2017–2022) | 1–2 steps: request → attempted restoration. Strong on demand, weak on success. |

### Postal volume data

| source | Quantity (of 90) | Quality |
|---|---|---|
| Japan Post letter volume | 30 (JP, 1996–2026) | 2–3 steps: volume → aggregate doing → restoration? The leap from aggregate volume to *restoration* is very weak. Volume measures total practice, not how much was restored to people who could not otherwise do it. |
| Korea Post mail volume | 30 (KR, 1996–2026) | Same as above. |
| USPS First-Class Mail volume | 30 (US, 1996–2026) | Same as above. |

### Autocomplete / predictive text

| source | Quantity (of 90) | Quality |
|---|---|---|
| Chrome autocomplete statistics | ~15 (global, ~2015–present; applies to all markets) | 2–3 steps: use → doing saved → judgment substituted? The last step is the weak one. |
| Google autocomplete savings | ~10 (global) | 2–3 steps. Same weakness. |
| ETH Zurich / academic studies | ~10 (global, 2010s–present) | 2–3 steps. Some studies may separate motivation, but most do not. |

### Machine translation

| source | Quantity (of 90) | Quality |
|---|---|---|
| DeepL / Google Translate surveys (Japan) | ~6 (JP, 2020s) | 1–2 steps if the survey separates "used directly" from "checked and corrected." Otherwise 2–3. |
| Korean university student survey | 1 (KR, 2024) | 1–2 steps. Includes attitude items that may help. |
| Global MT adoption dynamics | ~6 (US, Asia, 2020–2025) | 2–3 steps: market share → aggregate substitution. Weak on individual practice. |

### Summarisation

| source | Quantity (of 90) | Quality |
|---|---|---|
| Gartner enterprise adoption | ~3 (US-led, 2023–2025) | 2–3 steps: adoption → use → substitution. Enterprise ≠ personal letter-writing. |
| NTT Docomo survey (Japan) | 1 (JP, 2025) | 2 steps: use category → possible substitution. Does not separate letter-writing. |
| Buzzni AI meeting-notes (Korea) | 1 (KR, 2026) | 2–3 steps. Different practice (meetings), but boundary-relevant. |

---

## Section 5 — What no source covers

**Years and markets with no direct restoration data:**

- **Japan, 1996–2010:** No systematic, year-by-year measure of execution restoration for *handwriting* specifically. ABLEDATA is US-only; Act-navi begins 2020; the MHLW communication-device DB begins in the 2010s. For the first 15 years of the span, Japan has no source that observes how many people who could not write were enabled to write by technology.
- **Korea, 1996–2010:** The Korea NDS AT module is a single 2017 wave. The KNAT database begins in the 2010s. There is no year-by-year series for the first 15 years.
- **US, 1996–1998:** NATADS begins with the AT Act of 1998. The first two years of the span have no systematic AT data.
- **All three markets, 1996–2005:** Handwriting recognition benchmarks (IAM begins 1999) measure *capability*, not *restoration*. No source observes whether any person actually used a handwriting-restoration technology in a personal letter during this decade.

**Exposures with no direct measurement:**

- **Execution restored for *handwriting* specifically (as opposed to communication generally):** No source in any market counts "people who could not write and now can write letters via technology." All AT sources count communication devices broadly. The inference from "uses a communication device" to "can handwrite a letter" is never directly supported.
- **Judgment substituted at the level of the *letter's content*:** No source separates "the system chose the words" from "the system executed the words the person chose." Autocomplete and MT surveys come closest, but the "used directly" vs. "checked and corrected" distinction is only explicit in a few Japanese MT surveys from the 2020s.
- **Who wrote the content vs. who sent it:** No source I found records the *authorship* of the letter's content separately from the *transmission* of the letter. Postal volume data counts sent items but not who composed them. Platform data (LINE, KakaoTalk) counts messages but not whether the sender composed the text or accepted a suggestion.
- **Assistance at the decision level:** No source records when a human aide *decided* what to write on behalf of a person with a disability, versus when the person decided and the aide only wrote. The "Bliss communication with an aide who translated this into writing" case (from the academic survey literature) is qualitative and not systematically counted.

**Kinds of data that would cover these:**

1. **A disability-specific handwriting-restoration registry:** A year-by-year count, by market, of people who have a writing disability and who have been supplied with a technology that enables them to produce handwritten or handwritten-equivalent marks. No such registry exists in any of the three markets.
2. **A composition-authorship survey:** A survey that asks, for a recent personal message, "Who decided what to say?" and "Who decided how to say it?" separately from "Who physically produced the marks?" No such survey exists.
3. **A platform-level suggestion-acceptance log:** Messaging platforms could, in principle, log whether a sent message was typed character-by-character or accepted from a suggestion. No platform publishes this data. LINE, KakaoTalk, and US carriers do not disclose it.
4. **An aide-assisted communication census:** A count of paid or unpaid human assistants who write *on behalf of* people with disabilities, with a distinction between those who transcribe dictated content (execution assistance) and those who compose content (judgment assistance). No census of this kind exists in JP, KR, or US.
5. **A longitudinal handwriting-capability index:** A repeated measure of "can this person, with available technology, produce a handwritten letter to a particular person?" administered to a representative disability sample. No such index exists; existing surveys ask about device *use*, not *capability with technology*.

---

**Note on post-cut-off material:** Search results dated 2026 (e.g., the 2026 AI summarisation statistics, the 2026 Korean meeting-notes survey, the 2026 Japanese browser-AI summarisation study) are outside my training window. I cannot attest to their existence or content from training; they appear in search results but should be verified independently before use.