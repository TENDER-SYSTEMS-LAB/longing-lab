# Raw Source Index

This document is the registry for every raw source. It tracks each source's ID, path, hash, and ingestion status. Any Wiki content followed back through its provenance must ultimately lead to an original through this table.

## Registration

When adding a source, append one row to the table below and record the result of `git hash-object <path>` in the `Hash` column. If a later hash differs from the registered value, the original has changed. Do not update the Wiki automatically. Mark the pages that rely on the source `REVIEW_REQUIRED` so that a person can review them again.

## Source List

| Source ID | Path | Type | Date | Attribution | Hash | Ingested | Wiki Status |
|---|---|---|---|---|---|---|---|
| `SRC-2026-09-04-longing-concept-brainstorm` | [raw/conversations/2026-09-04-longing-concept-brainstorm.md](conversations/2026-09-04-longing-concept-brainstorm.md) | conversation | 2026-09-04 | jointly-developed | `d387cd37602638d884491cbea9291b3ef63ee7f2` | 2026-09-04 | promoted |
| `SRC-2026-09-05-price-formation-market-model` | [raw/conversations/2026-09-05-price-formation-market-model.md](conversations/2026-09-05-price-formation-market-model.md) | conversation | 2026-09-05 | jointly-developed | `bb15b180260e26f19a3447d808f8de07fe2c331d` | 2026-09-05 | promoted |
| `SRC-2026-09-05-claude-critic-of-model` | [raw/surveys/2026-09-05-claude-critic-of-model.md](surveys/2026-09-05-claude-critic-of-model.md) | survey | 2026-09-05 | llm-proposed | `68d0708d568a8f9dfe2cdfaffe4a50447024da2d` | 2026-09-05 | promoted |
| `SRC-2026-09-05-deepseek-critic-of-model` | [raw/surveys/2026-09-05-deepseek-critic-of-model.md](surveys/2026-09-05-deepseek-critic-of-model.md) | survey | 2026-09-05 | llm-proposed | `6685ee3ed45348df053d49aee0b913b3661343a0` | 2026-09-05 | promoted |
| `SRC-2026-09-05-gemini-critic-of-model` | [raw/surveys/2026-09-05-gemini-critic-of-model.md](surveys/2026-09-05-gemini-critic-of-model.md) | survey | 2026-09-05 | llm-proposed | `c77b4442480577cb7f739be25526fce7ddc1a1e5` | 2026-09-05 | promoted |
| `SRC-2026-09-05-glm-critic-of-model` | [raw/surveys/2026-09-05-glm-critic-of-model.md](surveys/2026-09-05-glm-critic-of-model.md) | survey | 2026-09-05 | llm-proposed | `63edf22960de0133b20f98e26ecf074c4a7a34e3` | 2026-09-05 | promoted |
| `SRC-2026-09-05-grok-critic-of-model` | [raw/surveys/2026-09-05-grok-critic-of-model.md](surveys/2026-09-05-grok-critic-of-model.md) | survey | 2026-09-05 | llm-proposed | `fd5945b2b3255f8a078f76acc59fba4fc87b5ac5` | 2026-09-05 | promoted |
| `SRC-2026-09-05-kimi-critic-of-model` | [raw/surveys/2026-09-05-kimi-critic-of-model.md](surveys/2026-09-05-kimi-critic-of-model.md) | survey | 2026-09-05 | llm-proposed | `50fef85b0ec9a9780d627260651d77280ffcc356` | 2026-09-05 | promoted |
| `SRC-2026-09-05-qwen-critic-of-model` | [raw/surveys/2026-09-05-qwen-critic-of-model.md](surveys/2026-09-05-qwen-critic-of-model.md) | survey | 2026-09-05 | llm-proposed | `8839d3047338ff3fa217cd789662f0043b1b279c` | 2026-09-05 | promoted |

## Note on the survey sources

The seven `critic-of-model` surveys are independent reviews produced by seven different language models in response to one shared review prompt, `LONGING_market_pricing_model_review_prompt.md`. That prompt is **not registered in this repository**, so every survey's framing — the fifteen report sections and the numbered questions they answer — reaches the Wiki only through the surveys themselves. Treat statements about what was asked as secondary citations.
