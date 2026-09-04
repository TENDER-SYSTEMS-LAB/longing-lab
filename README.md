# LONGING Lab

This repository is LONGING's long-term memory. It does not contain the project's application code. It preserves primary materials such as conversations, documents, and surveys, then maintains a connected Wiki of concepts, decisions, and open questions.

## Status

Initialized 2026-09-04. No project material has been ingested yet. The structure exists; the content does not. Nothing about LONGING has been decided or recorded.

## How This Repository Builds Memory

The repository has three layers, matching the convention used by [other-goods-lab](https://github.com/TENDER-SYSTEMS-LAB/other-goods-lab):

- [`raw/`](raw/) — the Source of Truth, preserving original conversations, documents, and surveys without alteration.
- [`wiki/`](wiki/) — the synthesis layer, comparing and connecting multiple sources to maintain the best current understanding.
- [`schema.md`](schema.md) and [`AGENTS.md`](AGENTS.md) — the operating layer, defining Wiki structure, provenance, ingestion, language, and maintenance rules.

Each new source prompts updates to the relevant Wiki pages and their relationships, so the Wiki becomes a persistent body of knowledge rather than a search result reconstructed for each question.

## What Goes Here

Ideas, research, references, concepts, decisions about the work itself, rejected directions, and the context needed to understand the project.

## What Does Not Go Here

Implementation decisions — framework, database, deployment, authentication, runtime — belong in the implementation repository, once one exists. Conventions and principles that apply across every TENDER SYSTEMS project belong in [tender-systems](https://github.com/TENDER-SYSTEMS-LAB/tender-systems).

## Where to Start

- [Current State](wiki/current-state.md) — what is confirmed, in progress, and unknown.
- [Project Overview](wiki/overview.md) — the project's definition and central question.
- [Wiki Index](wiki/index.md) — the working catalog of every Wiki page by type.

## Language

English is the canonical language of the repository. Registered raw sources remain in their original language because they are immutable evidence; their promoted summaries and interpretations are written in English.

## Working in This Repository

Human readers should begin with [Current State](wiki/current-state.md). Follow [`raw/README.md`](raw/README.md) when adding source material. Agents must read [`AGENTS.md`](AGENTS.md) and [`schema.md`](schema.md) first.
