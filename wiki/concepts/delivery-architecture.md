---
status: hypothesis
attribution: llm-proposed
updated: 2026-10-04
sources:
  - SRC-2026-10-04-public-delivery-architecture-request
  - SRC-2026-09-04-longing-concept-brainstorm
---

# Delivery Architecture

How LONGING RESEARCH could be served to an unspecified public without going down when traffic arrives all at once. The requirement is the user's ([[SRC-2026-10-04-public-delivery-architecture-request]], `user-originated`): show the work to anyone, and stay up under a sudden surge. **Everything below that requirement is the assistant's proposal, `llm-proposed`, and nothing in it is adopted.** No platform, domain, account or code exists. The current-state entry *Medium and delivery* — no platform, technology or exhibition context decided — still holds.

Original: [raw/conversations/2026-10-04-public-delivery-architecture-request.md](../../raw/conversations/2026-10-04-public-delivery-architecture-request.md).

## What the recorded decisions already imply

The design follows from decisions already made, not from a preference for a stack:

| Recorded decision | Consequence for delivery |
|---|---|
| Weekly market, monthly research; real-time pricing rejected ([[DEC-003-weekly-market-monthly-research]]) | Data changes at most once a week. Nothing needs computing per visitor. |
| Fictional history modelled ahead of time ([[data-sources]]) | Prices and reports exist before anyone looks at them. |
| Aggregate Market; investor stories and exchange operation are not content ([[current-state]]) | Visitors read; they do not trade, post or log in. There is no write path. |
| Research-house terminal, dense, no onboarding ([[DEC-002-research-house-form]]) | Interaction is browsing, charting and switching securities — all doable in the browser. |
| Mobile-first was the starting assumption ([[overview]]) | Page weight matters to the visitor; it does not change the server design. |

So the work is a **read-only publication that changes on a schedule**. The proposal rests on that one fact.

## Principle

**Put no server in the read path that a crowd can exhaust.** Every page and every data file is a static file, built before publication and served from a CDN's edge. A surge is then a surge of cache hits, which is the load a CDN is built for. Nothing the visitor does reaches a process that can run out of memory, connections or database capacity.

## Components

1. **Source repository.** A separate implementation repository under `TENDER-SYSTEMS-LAB` holding the model code and authored data, as the institution's confirmed convention requires: `{project-slug}-web`, created only when implementation actually begins ([DEC-001 — Repository Conventions](https://github.com/TENDER-SYSTEMS-LAB/tender-systems/blob/main/wiki/decisions/DEC-001-repository-conventions.md)). Whether its slug is `longing` or `longing-research` depends on the open rename question. This Wiki stays the project memory and is not the site.
2. **Build.** A scheduled CI job (GitHub Actions) runs the model and writes the whole site as files: HTML pages, one JSON series per security and index, report pages, and self-hosted fonts. It runs on push and at the weekly strike, `FRIDAY 17:00 UTC`.
3. **Gate.** Before deploy the build checks its own output — schema of the data files, no missing security, page-weight budget. A failure stops the deploy. **The previous week stays online**, so a broken build never becomes a broken site.
4. **Hosting.** A static host on a global CDN with atomic deploys and instant rollback. The proposed default is Cloudflare (Pages or Workers static assets). Two reasons: static requests and bandwidth were unmetered on its free tier when last checked, so a surge cannot become a bill (*denial of wallet*); and DDoS mitigation is on by default. **Verify the current plan terms before adopting.**
5. **Cache policy.** Fingerprinted assets (`app.3f9a.js`, fonts, past weeks' data) are `Cache-Control: public, max-age=31536000, immutable`. HTML and the current-week index file are short-lived — about `max-age=60, stale-while-revalidate=86400` — so the strike reaches visitors within a minute, and a stale copy is served rather than an error.
6. **Client.** Charts, security switching, archive browsing and report reading run in the browser from the static JSON. No API, no cookies, no login, no form.
7. **Mirror (when the stakes rise).** The same build output pushed to a second static host (for example GitHub Pages). If the primary CDN fails, switch DNS by hand. Not needed for a first release; add it before an exhibition opening or a planned press moment.

```
 authored data + model ──► CI build (push / Fri 17:00 UTC) ──► gate ──► static files
                                                                │  fail: last week stays
                                                                ▼
 visitors ◄── CDN edge (cache) ◄── static host (atomic deploy, rollback)
                                    └─► optional mirror (manual DNS switch)
```

## Why a surge does not take it down

| Failure | What happens |
|---|---|
| Sudden traffic (press, social sharing, the strike moment) | Served from edge cache; no origin process to exhaust. |
| Everyone refreshes at the strike | All visitors receive the same new file; it is cached after the first request per edge location. |
| The build or the model fails | The gate stops the deploy; the previous week stays online. |
| A bad week is published | Roll back to the previous deploy in one action. |
| Bots or scraping | Static files; same as ordinary traffic. |
| The primary CDN is down | Optional mirror and a manual DNS switch. |
| A surge would cost money | Avoided by choosing a host whose static traffic is not metered. |

## Choices made deliberately

- **No future weeks are published ahead of time.** Pre-building every week and revealing it by the visitor's clock would remove the weekly build, but the files are public and anyone could read next week's prices. The strike is built at the strike.
- **No backend, database, container cluster or autoscaling.** Each would add something that can fail under load, and the work has nothing for them to do.
- **Fonts self-hosted.** Inconsolata, Departure Mono and Source Serif are served from the same host, so no third-party service sits in the page's critical path ([[design-application]]). The Korean auxiliary typeface is undecided upstream; a Korean webfont is large and would need subsetting.
- **The same build runs offline.** If the work is shown in a gallery, the static output plays from a local machine with no network dependence.

## Open — needing the user

- **Domain.** Which name the work is served under. The repository-rename question ([[DEC-001-project-name-longing]]) bears on it.
- **Does the market keep running past its present?** If yes, the weekly build continues; if the history is a frozen archive, the build runs only on change. Both use the same design. See the open timeline question on [[technology-waves]].
- **Any audience input.** If the work later lets visitors act (for example issue something), that is a separate write path — a queue in front of a small store — kept apart so that its failure cannot take the read path down. Not designed, because nothing calls for it.
- **Exhibition context.** None decided; it decides whether the mirror and the offline build are needed.

## How to check it, once built

Confirm `cf-cache-status: HIT` (or the host's equivalent) on pages and data after the first request. Then run a short load test against the published URL from one machine — for example `oha -z 60s -c 200 <url>` — and watch for errors and the cache-hit ratio, not the server, since there is none.
