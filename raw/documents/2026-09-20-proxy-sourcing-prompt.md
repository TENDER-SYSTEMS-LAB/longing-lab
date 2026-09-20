# LONGING — Technology Diffusion Proxy Sourcing

Purpose: establish whether a continuous, comparable measure of technology adoption in Japan, Korea and the United States from 1996 to 2026 can actually be assembled from published statistics, and on what terms.

This is a **sourcing and documentation task, not a design task.** Nothing you write here will be used to argue anything about the subject matter.

---

# 1. What this round is for

A fictional research institution publishes an index whose movement is driven by a single measured series: how far a set of communication technologies had spread, each year, in three countries. The institution intends to publish that series, say where it came from, and mark the week after which it is no longer measured but extrapolated.

For that to be honest, the series has to exist. This round finds out whether it does.

The waves of interest, in rough order of arrival:

- dial-up and bulletin-board services
- mobile telephony (subscriptions, then penetration)
- fixed broadband
- the social web
- smartphones
- messaging platforms
- generative AI usage

---

# 2. What this round is NOT for

Do not estimate a number you cannot source. An invented figure that looks like a measurement is worse than a gap.

Do not smooth, interpolate or backfill silently. If you propose interpolation, mark it as such and say which points are real.

Do not propose what the index should do with the series. That is decided elsewhere.

Do not assess whether the underlying artistic premise is sound.

---

# 3. Rules of engagement

**Cite.** For every series: the publishing body, the exact series name, the URL or publication where it lives, the licence or reuse terms if you can determine them, and the date you believe the figures were last revised.

**Separate what you know from what you infer.** Mark each row as `verified` (you are confident the series exists with that name and coverage), `probable` (you are confident something of this kind exists but not of its exact form), or `unknown`.

**Say when you cannot check.** If you cannot reach a source, say that plainly rather than reconstructing it from memory. A row marked `probable — could not verify` is more useful than a confident invention.

**Currency of your knowledge.** State your training cut-off, and mark any figure after it as outside what you can attest.

---

# 4. Required output

## Section 1 — The inventory

One table per country — Japan, Korea, the United States — with one row per candidate series:

| technology | series name | publisher | first year | last year | frequency | unit and definition | status |

Prefer the longest continuous series over the most precise one. Note where a national statistical office and an international body (ITU, OECD, World Bank) publish different figures for the same thing, and give both.

## Section 2 — Definitions that do not match

For each technology, state how the three countries' definitions differ. Examples of the kind of thing wanted: whether mobile penetration counts subscriptions or individuals, how multiple SIMs are treated, what counts as broadband and at what speed threshold, whether household or individual is the unit, and how the base year is set.

This section is the point of the exercise. Two series with the same title and different definitions are the failure mode.

## Section 3 — Breaks, revisions and discontinuities

List every known break in series continuity: definitional changes, survey redesigns, changes of publisher, revisions that moved history. Give the year and what changed.

## Section 4 — The gap after the last measurement

For generative AI specifically: state what is actually published about usage volumes, by whom, and in what form. Distinguish vendor disclosures at a point in time from continuous series. If no continuous industry-wide series exists, say so, and list the closest available proxies with their limitations.

## Section 5 — A normalisation proposal

Propose a rule for putting three countries' series onto one comparable scale, given the definitional differences in Section 2.

State what the rule assumes, what it distorts, and which comparisons remain invalid after it is applied. A rule that works for cross-time comparison within a country but not for cross-country comparison at a point in time should be described that way.

Give the rule precisely enough that someone else could apply it and get the same numbers.

## Section 6 — What cannot be sourced

List what this exercise could not find, and say whether you believe it is unpublished, published but not accessible to you, or does not exist as a measured quantity at all.

## Section 7 — Refusals and confidence

State anything you declined to answer. Then give an overall judgement on one question only: **can a defensible thirty-year, three-country diffusion series be assembled, and if so, with what caveats?**

---

Accuracy here matters more than completeness. A short inventory of verified series with honest gaps is worth more than a full table in which some rows are guesses.
