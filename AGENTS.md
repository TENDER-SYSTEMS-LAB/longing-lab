# LONGING Wiki — Agent Instructions

This repository is LONGING's long-term memory. Agents working here read before they write. Before adding anything new, check what has already been recorded and build on it.

This repository follows the same operating convention as [other-goods-lab](https://github.com/TENDER-SYSTEMS-LAB/other-goods-lab). When the two diverge without reason, prefer the established convention there.

## What to Read First

Read these files in order:

1. `wiki/index.md`
2. `wiki/current-state.md`
3. `schema.md`
4. The concept, decision, or question pages relevant to the task

Do not begin by scanning the entire raw layer. Start with the synthesis already maintained in the Wiki, then consult only the raw sources that are necessary.

## Repository Language

- English is the canonical and default language for all maintained repository documentation, including `README.md`, `AGENTS.md`, `schema.md`, `wiki/**`, `raw/README.md`, and `raw/sources.md`.
- Write all new pages, edits, headings, summaries, metadata prose, and log entries in English, even when the user's working language is not English.
- Preserve proper names, source identifiers, file paths, code, and intentionally quoted source text when translating them would change their identity or evidentiary meaning.
- Registered files under `raw/documents/`, `raw/conversations/`, and `raw/surveys/` are immutable source records and retain their original language. Never rewrite a raw source to satisfy the English-default policy; synthesize or explain it in English in the Wiki instead.

## Document Roles

- `README.md` is the entry point through which readers understand the project and the repository. Do not put the complete file list or agent instructions there.
- `wiki/index.md` is the working catalog for finding every Wiki page and its editing destination. Excluding the index itself, register each page exactly once under its type with `link + one-line summary + updated date`; include status when the page has one.
- `wiki/current-state.md` is a snapshot of currently valid decisions, scope, priorities, and unresolved questions.
- `wiki/log.md` is an append-only chronological history of meaningful ingestion, queries, decisions, linting, and maintenance.
- `raw/sources.md` is the single registry for every original source's path, hash, and ingestion status. Do not duplicate the raw source list in the index.

## Query Workflow

When the user asks a question, find the answer in this order:

```text
index
  ↓
current-state
  ↓
relevant concept / decision / question
  ↓
raw source only when necessary
```

Consult raw sources only for consequential judgments or when the original evidence must be checked directly.

## Conversation Ingestion Workflow

When ingesting a new conversation or document, follow this sequence:

1. **Register the source** — Preserve the original unchanged under `raw/` and register it in `raw/sources.md` with its hash.
2. **Explore the existing Wiki** — Read the index, current state, and relevant pages first.
3. **Analyze the conversation** — Extract ideas, decisions, hypotheses, open questions, rejected or deferred ideas, rationale, tensions, and emerging concepts.
4. **Compare with existing knowledge** — Decide whether the information is new, reinforces existing material, conflicts with it, or supersedes an earlier decision.
5. **Decide whether to promote** — Keep the material only in raw or promote it into the Wiki.
6. **Prefer updating existing pages** — Before creating a page, check whether an existing page can be updated.
7. **Create a new page** — Do so only for a genuinely new, independent entity.
8. **Cross-link** — Link related concepts, decisions, and questions.
9. **Check current state** — Determine whether the project's current state changed and update it when needed.
10. **Synchronize the index** — In the same task, update the catalog entry when a page is created, moved, or deleted, or when its summary, status, or updated date changes.
11. **Append to `log.md`** — Add the work after all existing entries using `## [YYYY-MM-DD] <type> | <title>`. Prefer `ingest`, `query`, `decision`, `lint`, or `maintenance` as the type.

## Never Do These Things

- Delete or modify a raw source.
- Replace raw material with the Wiki.
- Promote every source automatically.
- Record an LLM proposal as a user decision.
- Present a rejected idea as current.
- Invent facts without a source.
- Hide uncertainty.
- Silently overwrite older knowledge.
- Modify past entries in `log.md` outside an explicitly authorized repository-wide migration.
- Create many empty placeholder pages.
- Add metadata fields that are not needed.
- Treat Wiki size, page count, or document length as a success metric.

## When to Create a New Page

Create a page only when a meaningful unit has emerged that cannot be captured by one line in `current-state.md` and is likely to develop independently over time.

## Verification

At the beginning and end of a task, verify that source originals have not changed since registration:

```bash
git hash-object raw/documents/*.md raw/conversations/*.md raw/surveys/*.md
```

Compare the results with the `Hash` column in `raw/sources.md`. If any value differs, the original changed. Do not update the Wiki automatically; mark the relevant page `REVIEW_REQUIRED`.
