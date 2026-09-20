# Raw Source Index

This document is the registry for every raw source. It tracks each source's ID, path, hash, and ingestion status. Any Wiki content followed back through its provenance must ultimately lead to an original through this table.

## Registration

When adding a source, append its row and record `git hash-object <path>` once in the `Hash` column. Preserve that hash as provenance.

For a lookup or suspected mismatch, search only the source ID/path and its capture note. Do not load this entire table or compare all hashes for routine tasks. Follow [AGENTS — Verification](../AGENTS.md#verification): inspect changed raw paths with Git; an explicitly requested provenance audit is a separate task.

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
| `SRC-2026-09-05-pricing-model-v2-factor-framework` | [raw/conversations/2026-09-05-pricing-model-v2-factor-framework.md](conversations/2026-09-05-pricing-model-v2-factor-framework.md) | conversation | 2026-09-05 | jointly-developed | `4f17627f095dcc1d9dee6b135b6c0be4744434e5` | 2026-09-05 | promoted |
| `SRC-2026-09-05-pricing-model-v2-factor-review-prompt` | [raw/documents/2026-09-05-pricing-model-v2-factor-review-prompt.md](documents/2026-09-05-pricing-model-v2-factor-review-prompt.md) | document | 2026-09-05 | jointly-developed | `b715d5a091eda3ff272114f81d9de3c204e57019` | 2026-09-05 | promoted |
| `SRC-2026-09-05-pricing-model-v2-factor-review-claude` | [raw/surveys/2026-09-05-pricing-model-v2-factor-review-claude.md](surveys/2026-09-05-pricing-model-v2-factor-review-claude.md) | survey | 2026-09-05 | llm-proposed | `1d2cfa544972c9cdcfab4b931399c9d31f160549` | 2026-09-05 | promoted |
| `SRC-2026-09-05-pricing-model-v2-factor-review-deepseek` | [raw/surveys/2026-09-05-pricing-model-v2-factor-review-deepseek.md](surveys/2026-09-05-pricing-model-v2-factor-review-deepseek.md) | survey | 2026-09-05 | llm-proposed | `1603db76927e2fc9d2bf980b92f05f6fe5de61c1` | 2026-09-05 | promoted |
| `SRC-2026-09-05-pricing-model-v2-factor-review-gemini` | [raw/surveys/2026-09-05-pricing-model-v2-factor-review-gemini.md](surveys/2026-09-05-pricing-model-v2-factor-review-gemini.md) | survey | 2026-09-05 | llm-proposed | `a1345d9596b9ddef2453f5afe94ac40a17b57ffc` | 2026-09-05 | promoted |
| `SRC-2026-09-05-pricing-model-v2-factor-review-glm` | [raw/surveys/2026-09-05-pricing-model-v2-factor-review-glm.md](surveys/2026-09-05-pricing-model-v2-factor-review-glm.md) | survey | 2026-09-05 | llm-proposed | `d7d5ed60ece2a72def25bf98357ab0e8f6e64e23` | 2026-09-05 | promoted |
| `SRC-2026-09-05-pricing-model-v2-factor-review-grok` | [raw/surveys/2026-09-05-pricing-model-v2-factor-review-grok.md](surveys/2026-09-05-pricing-model-v2-factor-review-grok.md) | survey | 2026-09-05 | llm-proposed | `98d25c865098b5844c2969f5b276a5416596d823` | 2026-09-05 | promoted |
| `SRC-2026-09-05-pricing-model-v2-factor-review-qwen` | [raw/surveys/2026-09-05-pricing-model-v2-factor-review-qwen.md](surveys/2026-09-05-pricing-model-v2-factor-review-qwen.md) | survey | 2026-09-05 | llm-proposed | `07c1fb597b79ee4cdb4dc3fce9d65e201d6911c3` | 2026-09-06 | promoted (re-captured; supersedes `59291ecd3ffdb1d45bbcc2ccc3d2403230242f15`) |
| `SRC-2026-09-06-factor-set-failure-profile-prompt-v1` | [raw/documents/2026-09-06-factor-set-failure-profile-prompt-v1.md](documents/2026-09-06-factor-set-failure-profile-prompt-v1.md) | document | 2026-09-06 | jointly-developed | `0adf9d64511716c3095d588673f3fedc4ce06e52` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-prompt-v2` | [raw/documents/2026-09-06-factor-set-failure-profile-prompt-v2.md](documents/2026-09-06-factor-set-failure-profile-prompt-v2.md) | document | 2026-09-06 | jointly-developed | `b9a7304cac60d123eaa79df6244e0068216aacbe` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-chatgpt` | [raw/surveys/2026-09-06-factor-set-failure-profile-chatgpt.md](surveys/2026-09-06-factor-set-failure-profile-chatgpt.md) | survey | 2026-09-06 | llm-proposed | `3eb4ac736a4528499eaf7fbfed705436d864177c` | 2026-09-06 | promoted |
| `SRC-2026-09-06-attribution-resolution-and-universe-scaling` | [raw/conversations/2026-09-06-attribution-resolution-and-universe-scaling.md](conversations/2026-09-06-attribution-resolution-and-universe-scaling.md) | conversation | 2026-09-06 | jointly-developed | `f369932d9135eeb1a15d22e256bc34748fd9cc28` | 2026-09-06 | promoted |
| `SRC-2026-09-06-arbitrage-news-quality-and-next-work-items` | [raw/conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md](conversations/2026-09-06-arbitrage-news-quality-and-next-work-items.md) | conversation | 2026-09-06 | user-originated | `9acabf63123daf4baec02cf627ab22c0ccd56c9f` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-claude` | [raw/surveys/2026-09-06-factor-set-failure-profile-claude.md](surveys/2026-09-06-factor-set-failure-profile-claude.md) | survey | 2026-09-06 | llm-proposed | `64865497a89355e4f22ff92100d0b71ed09fc415` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-deepseek` | [raw/surveys/2026-09-06-factor-set-failure-profile-deepseek.md](surveys/2026-09-06-factor-set-failure-profile-deepseek.md) | survey | 2026-09-06 | llm-proposed | `fb3ca556847aad43c5c2ba8c89e9b0378b40a172` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-gemini` | [raw/surveys/2026-09-06-factor-set-failure-profile-gemini.md](surveys/2026-09-06-factor-set-failure-profile-gemini.md) | survey | 2026-09-06 | llm-proposed | `92c3d53924aa6c37068417c537c6baaac13509bc` | — | raw-only (incomplete event coverage; superseded for synthesis by gemini-complete) |
| `SRC-2026-09-06-factor-set-failure-profile-grok` | [raw/surveys/2026-09-06-factor-set-failure-profile-grok.md](surveys/2026-09-06-factor-set-failure-profile-grok.md) | survey | 2026-09-06 | llm-proposed | `00f36ac71cfbb872b8157db5b4f9ffd91c7e5555` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-gemini-complete` | [raw/surveys/2026-09-06-factor-set-failure-profile-gemini-complete.md](surveys/2026-09-06-factor-set-failure-profile-gemini-complete.md) | survey | 2026-09-06 | llm-proposed | `b259b2f12b0edebc527c30e212e1bb9a7ece2c64` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-kimi` | [raw/surveys/2026-09-06-factor-set-failure-profile-kimi.md](surveys/2026-09-06-factor-set-failure-profile-kimi.md) | survey | 2026-09-06 | llm-proposed | `12cc3947d7172c141bc3d7af5345644d2e718b57` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-qwen` | [raw/surveys/2026-09-06-factor-set-failure-profile-qwen.md](surveys/2026-09-06-factor-set-failure-profile-qwen.md) | survey | 2026-09-06 | llm-proposed | `cf9c2968e125a6e5ecb979266f813489c4d973b8` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-completion-requests` | [raw/documents/2026-09-06-factor-set-failure-profile-completion-requests.md](documents/2026-09-06-factor-set-failure-profile-completion-requests.md) | document | 2026-09-06 | llm-proposed | `036e419f396f5b2810b46ce672a54d675acd3380` | 2026-09-06 | promoted |
| `SRC-2026-09-06-factor-set-failure-profile-glm` | [raw/surveys/2026-09-06-factor-set-failure-profile-glm.md](surveys/2026-09-06-factor-set-failure-profile-glm.md) | survey | 2026-09-06 | llm-proposed | `9903a4cab8ab65bee90763ee62d2675a9f966fbf` | 2026-09-06 | promoted |
| `SRC-2026-09-06-academic-model-research-brief` | [raw/documents/2026-09-06-academic-model-research-brief.md](documents/2026-09-06-academic-model-research-brief.md) | document | 2026-09-06 | llm-synthesis | `5d6ca7181b1f63c3d5d23ff5372ddca6aac32827` | 2026-09-06 | promoted |
| `SRC-2026-09-06-academic-model-research-notes` | [raw/surveys/2026-09-06-academic-model-research-notes.md](surveys/2026-09-06-academic-model-research-notes.md) | survey | 2026-09-06 | llm-synthesis | `c33fdae6a8469e87142f0ea836e09243332fad80` | 2026-09-06 | promoted |
| `SRC-2026-09-06-dataset-backtesting-research` | [raw/surveys/2026-09-06-dataset-backtesting-research.md](surveys/2026-09-06-dataset-backtesting-research.md) | survey | 2026-09-06 | llm-synthesis | `3f535e4c487027474bdec0c8506db96317d8b1b6` | 2026-09-06 | promoted |
| `SRC-2026-09-07-artwork-brainstorm-v2` | [raw/conversations/2026-09-07-artwork-brainstorm-v2.md](conversations/2026-09-07-artwork-brainstorm-v2.md) | conversation | 2026-09-07 | jointly-developed | `126afd7fc330f9d6367d9c34027d26723791ed80` | 2026-09-07 | promoted |

| `SRC-2026-09-06-cross-domain-model-survey-request` | [raw/documents/2026-09-06-cross-domain-model-survey-request.md](documents/2026-09-06-cross-domain-model-survey-request.md) | document | 2026-09-06 | user-originated | `35a71df127435019d292a4bc9a09337f97ad2577` | 2026-09-06 | promoted |
| `SRC-2026-09-06-cross-domain-model-survey` | [raw/surveys/2026-09-06-cross-domain-model-survey.md](surveys/2026-09-06-cross-domain-model-survey.md) | survey | 2026-09-06 | llm-synthesis | `47a6bf0307f8604f3eb94b4970e71df6c5bc3ee1` | 2026-09-06 | promoted |

| `SRC-2026-09-06-cross-domain-model-survey-korean` | [raw/surveys/2026-09-06-cross-domain-model-survey-korean.md](surveys/2026-09-06-cross-domain-model-survey-korean.md) | survey | 2026-09-06 | llm-synthesis | `d22087a2428a6373acda61dc1e3986476c07e166` | — | raw-only (Korean reader export; derivative, not independent evidence) |
| `SRC-2026-09-06-cross-domain-model-survey-korean-csv` | [raw/documents/2026-09-06-cross-domain-model-survey-korean.csv](documents/2026-09-06-cross-domain-model-survey-korean.csv) | document | 2026-09-06 | llm-synthesis | `cb969b28567cc6c01c94e71629d2563459b5a3c8` | — | raw-only (Korean reader export; derivative, not independent evidence) |
| `SRC-2026-09-06-academic-model-dialogue` | [raw/conversations/2026-09-06-academic-model-dialogue.md](conversations/2026-09-06-academic-model-dialogue.md) | conversation | 2026-09-06 | jointly-developed | `3209450b18ab30c63bb238798d506ce4163ed051` | 2026-09-06 | promoted (partial retrieval / compiled provenance disclosed) |
| `SRC-2026-09-06-academic-model-continuation` | [raw/conversations/2026-09-06-academic-model-continuation.md](conversations/2026-09-06-academic-model-continuation.md) | conversation | 2026-09-06 | jointly-developed | `cef6ff121d4aca4cdd563c2bc5299585c6c0e99d` | 2026-09-06 | promoted (partial retrieval / compiled provenance disclosed) |
| `SRC-2026-09-06-academic-model-recovered-excerpts` | [raw/conversations/2026-09-06-academic-model-recovered-excerpts.md](conversations/2026-09-06-academic-model-recovered-excerpts.md) | conversation | 2026-09-06 | jointly-developed | `faf7f71dd333cad4e58e472f862dd704c2a348b0` | 2026-09-06 | promoted (selected original message recovery) |
| `SRC-2026-09-06-worldbuilding-roadmap-request` | [raw/documents/2026-09-06-worldbuilding-roadmap-request.md](documents/2026-09-06-worldbuilding-roadmap-request.md) | document | 2026-09-06 | user-originated | `c2f36030c87896f2773fd34e75cba21ad867c366` | 2026-09-06 | promoted (request only; design depth and roadmap remain LLM proposals) |

| `SRC-2026-09-06-world-rules-letter-spec-request` | [raw/documents/2026-09-06-world-rules-letter-spec-request.md](documents/2026-09-06-world-rules-letter-spec-request.md) | document | 2026-09-06 | user-originated | `caafdfeb20586b467654a119ab9d5a55725bc371` | 2026-09-06 | promoted (exact request; world and LETTER design choices remain LLM proposals unless separately accepted) |
| `SRC-2026-09-06-worldbuilding-roadmap-and-handoff` | [raw/conversations/2026-09-06-worldbuilding-roadmap-and-handoff.md](conversations/2026-09-06-worldbuilding-roadmap-and-handoff.md) | conversation | 2026-09-06 | jointly-developed | `6a22a48044d40a7452563cd7448a29bbae6ad1c6` | 2026-09-06 | promoted (selected original messages; assistant-authored handoff distinct from later user-issued task request) |
| `SRC-2026-09-14-typographic-voice` | [raw/conversations/2026-09-14-typographic-voice.md](conversations/2026-09-14-typographic-voice.md) | conversation | 2026-09-14 | jointly-developed | `0201a6cb1bce1f171601f1cf11d0cff06b53dcd5` | 2026-09-15 | promoted as the inherited institutional typographic rule; LONGING surface assignments below it are `llm-proposed`, and Korean auxiliary typeface, version, weights, sizes, spacing, and per-system density remain unresolved |
| `SRC-2026-09-14-design-principles-draft` | [raw/conversations/2026-09-14-design-principles-draft.md](conversations/2026-09-14-design-principles-draft.md) | conversation | 2026-09-14 | llm-proposed | `ce5ad433d9ed496b120fd3c4e6a6ade813cdf523` | 2026-09-15 | partially promoted as an unconfirmed institutional design draft and the user's layering intent; the ten principles, the three-layer scheme, and the conflict ordering are not adopted rules |
| `SRC-2026-09-15-reserve-absorption-and-trust-instruments` | [raw/conversations/2026-09-15-reserve-absorption-and-trust-instruments.md](conversations/2026-09-15-reserve-absorption-and-trust-instruments.md) | conversation | 2026-09-15 | jointly-developed | `337bc0209634ddb3f6a9e2c01e40a0ea5689cae7` | 2026-09-15 | promoted as the absorption of the reserve function into LONGING, the BEARER BOND / BLIND TRUST instrument pair, and the no-advocacy decline mechanism; operator-captured transcript with user turns verbatim and assistant turns condensed |
| `SRC-2026-09-15-longing-research-rename` | [raw/conversations/2026-09-15-longing-research-rename.md](conversations/2026-09-15-longing-research-rename.md) | conversation | 2026-09-15 | user-originated | `d186ef253116a5dd44634ec20596a22eb79a1661` | 2026-09-15 | promoted as the rename of the work to LONGING RESEARCH, resolving the contradiction logged during the same day's earlier ingestion |
| `SRC-2026-09-15-numeraire-and-standard-return` | [raw/conversations/2026-09-15-numeraire-and-standard-return.md](conversations/2026-09-15-numeraire-and-standard-return.md) | conversation | 2026-09-15 | jointly-developed | `11c61a0be519aadeac9d92dd6434f614b57ddd21` | 2026-09-15 | promoted as DEC-007, the STANDARD RETURN numeraire, and as the answer closing Q-004 |
| `SRC-2026-09-15-ai-reinforcing-loop-diagram` | [raw/documents/2026-09-15-ai-reinforcing-loop-diagram.webp](documents/2026-09-15-ai-reinforcing-loop-diagram.webp) | document | 2026-09-15 | user-originated | `8db1d71c56a46bf3178f8da92af3f834a6413921` | 2026-09-15 | promoted only as the reinforcing structure behind the endogenous loop in DEC-007; its named actors are explicitly not adopted |
| `SRC-2026-09-16-loop-simulation-session` | [raw/conversations/2026-09-16-loop-simulation-session.md](conversations/2026-09-16-loop-simulation-session.md) | conversation | 2026-09-16 | jointly-developed | `55284e4985c09cf46798beac1414d4f6832b6359` | 2026-09-16 | promoted as the decision to simulate before selecting a factor set, and as the adoption of the redefined anxiety term |
| `SRC-2026-09-16-loop-simulation-findings` | [raw/documents/2026-09-16-loop-simulation-findings.md](documents/2026-09-16-loop-simulation-findings.md) | document | 2026-09-16 | llm-proposed | `76024d116f309fb6796c06ea28adc9c85d6947b6` | 2026-09-16 | promoted as loop-simulation; the seven findings are assistant-authored results from an assistant-authored model |
| `SRC-2026-09-16-loop-simulation-harness` | [raw/documents/2026-09-16-loop-simulation-harness.py](documents/2026-09-16-loop-simulation-harness.py) | document | 2026-09-16 | llm-proposed | `388783be4372f11fc8b3e141118cf5cd29ffdb2f` | 2026-09-16 | the instrument the findings come from, registered so they can be reproduced or refuted |
| `SRC-2026-09-19-market-texture-session` | [raw/conversations/2026-09-19-market-texture-session.md](conversations/2026-09-19-market-texture-session.md) | conversation | 2026-09-19 | jointly-developed | `421955e62da31b6897e4ee42a2898772583e53b0` | 2026-09-19 | promoted as the requirement that the market read as a real index inverted |
| `SRC-2026-09-19-market-texture-findings` | [raw/documents/2026-09-19-market-texture-findings.md](documents/2026-09-19-market-texture-findings.md) | document | 2026-09-19 | llm-proposed | `00a393f8c29d340d98232547e6130ce2adb7c80b` | 2026-09-19 | promoted into loop-simulation; six added mechanisms, three defects, and a stylistic-calibration boundary |
| `SRC-2026-09-19-loop-simulation-harness-v2` | [raw/documents/2026-09-19-loop-simulation-harness-v2.py](documents/2026-09-19-loop-simulation-harness-v2.py) | document | 2026-09-19 | llm-proposed | `34c5608e12f71c6bece43898ea3cd4091575b6a2` | 2026-09-19 | the harness after the texture round; supersedes the 2026-09-16 harness, which is retained unedited |
| `SRC-2026-09-20-bearer-bond-issuance` | [raw/conversations/2026-09-20-bearer-bond-issuance.md](conversations/2026-09-20-bearer-bond-issuance.md) | conversation | 2026-09-20 | user-originated | `c65b1d47b5cb7795357b2f889b85c47ae339be80` | 2026-09-20 | promoted as DEC-008, DEC-009 and technology-waves |
| `SRC-2026-09-20-simulation-rebuild` | [raw/conversations/2026-09-20-simulation-rebuild.md](conversations/2026-09-20-simulation-rebuild.md) | conversation | 2026-09-20 | jointly-developed | `2efda6c9420304ee7d1b9d02a600d0e917c37582` | 2026-09-20 | promoted as the third simulation round and the signed-positioning correction |
| `SRC-2026-09-20-rebuild-findings` | [raw/documents/2026-09-20-rebuild-findings.md](documents/2026-09-20-rebuild-findings.md) | document | 2026-09-20 | llm-proposed | `86e797688fa58159df1d08fc8a0c5d68ea3c023d` | 2026-09-20 | five defects, one of them a test that had been passing for the wrong reason |
| `SRC-2026-09-20-loop-simulation-harness-v3` | [raw/documents/2026-09-20-loop-simulation-harness-v3.py](documents/2026-09-20-loop-simulation-harness-v3.py) | document | 2026-09-20 | llm-proposed | `442c3e1b7b9c95a14ac7ba2282604334535bb234` | 2026-09-20 | the harness rebuilt on DEC-008 and DEC-009; supersedes v2, which is retained unedited |
| `SRC-2026-09-20-factor-identification-prompt` | [raw/documents/2026-09-20-factor-identification-prompt.md](documents/2026-09-20-factor-identification-prompt.md) | document | 2026-09-20 | jointly-developed | `59c082e4ad3699bba93ccd3f36cd3825fdcc4c91` | 2026-09-20 | promoted; seven responses synthesised in `wiki/concepts/factor-identification-review.md` |
| `SRC-2026-09-20-proxy-sourcing-prompt` | [raw/documents/2026-09-20-proxy-sourcing-prompt.md](documents/2026-09-20-proxy-sourcing-prompt.md) | document | 2026-09-20 | jointly-developed | `3bdd53cb7dc4c35cf68750123017ccde71ea0318` | 2026-09-20 | promoted; seven responses synthesised in `wiki/concepts/proxy-sourcing-review.md` |
| `SRC-2026-09-20-institution-naming-prompt` | [raw/documents/2026-09-20-institution-naming-prompt.md](documents/2026-09-20-institution-naming-prompt.md) | document | 2026-09-20 | jointly-developed | `a924dcb5b5c50779e451e451809dc92b627f3627` | 2026-09-20 | promoted; seven responses synthesised in `wiki/concepts/institution-naming-review.md` |
| `SRC-2026-09-20-requisition-cap-decision` | [raw/conversations/2026-09-20-requisition-cap-decision.md](conversations/2026-09-20-requisition-cap-decision.md) | conversation | 2026-09-20 | user-originated | `ce91289ea8e39fbb8134505b5a83169bd29de932` | 2026-09-20 | promoted as the `s(t)` cap decision in DEC-007; closes one of the four simulation gaps |
| `SRC-2026-09-20-factor-identification-chatgpt` | [raw/surveys/2026-09-20-factor-identification-chatgpt.md](surveys/2026-09-20-factor-identification-chatgpt.md) | survey | 2026-09-20 | llm-proposed | `a137b935fb9ad3615c4dac3f618cf6e03a05674c` | 2026-09-20 | promoted |
| `SRC-2026-09-20-factor-identification-claude` | [raw/surveys/2026-09-20-factor-identification-claude.md](surveys/2026-09-20-factor-identification-claude.md) | survey | 2026-09-20 | llm-proposed | `9c548f64c8e03233ec64d7e5b1071d6330f0b87d` | 2026-09-20 | promoted |
| `SRC-2026-09-20-factor-identification-deepseek` | [raw/surveys/2026-09-20-factor-identification-deepseek.md](surveys/2026-09-20-factor-identification-deepseek.md) | survey | 2026-09-20 | llm-proposed | `08feadf56a12e457a4f8d3b930c098e7d5116b31` | 2026-09-20 | promoted |
| `SRC-2026-09-20-factor-identification-gemini` | [raw/surveys/2026-09-20-factor-identification-gemini.md](surveys/2026-09-20-factor-identification-gemini.md) | survey | 2026-09-20 | llm-proposed | `fc07a869715ffb13950d2e381689ab524a1d60a1` | 2026-09-20 | promoted; response written in Korean, thresholds it invents recorded as flagged |
| `SRC-2026-09-20-factor-identification-glm` | [raw/surveys/2026-09-20-factor-identification-glm.md](surveys/2026-09-20-factor-identification-glm.md) | survey | 2026-09-20 | llm-proposed | `8260966aadd99c3619b3fdf0a93dba4295401afa` | 2026-09-20 | promoted |
| `SRC-2026-09-20-factor-identification-grok` | [raw/surveys/2026-09-20-factor-identification-grok.md](surveys/2026-09-20-factor-identification-grok.md) | survey | 2026-09-20 | llm-proposed | `758c7e8de06061f90daf9e367ac2b4d427cb8aeb` | 2026-09-20 | promoted |
| `SRC-2026-09-20-factor-identification-qwen` | [raw/surveys/2026-09-20-factor-identification-qwen.md](surveys/2026-09-20-factor-identification-qwen.md) | survey | 2026-09-20 | llm-proposed | `391f725dfbefc06d3e9ca20d34cdf4db25c0c03a` | 2026-09-20 | promoted |
| `SRC-2026-09-20-proxy-sourcing-chatgpt` | [raw/surveys/2026-09-20-proxy-sourcing-chatgpt.md](surveys/2026-09-20-proxy-sourcing-chatgpt.md) | survey | 2026-09-20 | llm-proposed | `c6edb2da9adc33c27d904931f592c5c0917a44b4` | 2026-09-20 | promoted |
| `SRC-2026-09-20-proxy-sourcing-claude` | [raw/surveys/2026-09-20-proxy-sourcing-claude.md](surveys/2026-09-20-proxy-sourcing-claude.md) | survey | 2026-09-20 | llm-proposed | `d6adb2453745e92e1a51873b5a6a7845392ce987` | 2026-09-20 | promoted; capture retains the leading chat message before the report |
| `SRC-2026-09-20-proxy-sourcing-deepseek` | [raw/surveys/2026-09-20-proxy-sourcing-deepseek.md](surveys/2026-09-20-proxy-sourcing-deepseek.md) | survey | 2026-09-20 | llm-proposed | `6fad8e5c3ca4d2177633cb19d64ca123868ba3e9` | 2026-09-20 | promoted; first delivered as a byte-identical pair with the Gemini slot, identified as DeepSeek by the user |
| `SRC-2026-09-20-proxy-sourcing-gemini` | [raw/surveys/2026-09-20-proxy-sourcing-gemini.md](surveys/2026-09-20-proxy-sourcing-gemini.md) | survey | 2026-09-20 | llm-proposed | `c0a4d1414c6116a3c23a87c6599afa5d616aeb84` | 2026-09-20 | promoted; re-collected after the first Gemini slot proved to be a duplicate of DeepSeek |
| `SRC-2026-09-20-proxy-sourcing-glm` | [raw/surveys/2026-09-20-proxy-sourcing-glm.md](surveys/2026-09-20-proxy-sourcing-glm.md) | survey | 2026-09-20 | llm-proposed | `f3f3dedf19f9a2253f4bade552702aa664785862` | 2026-09-20 | promoted; self-titled `Round 1`, attests no live lookup |
| `SRC-2026-09-20-proxy-sourcing-grok` | [raw/surveys/2026-09-20-proxy-sourcing-grok.md](surveys/2026-09-20-proxy-sourcing-grok.md) | survey | 2026-09-20 | llm-proposed | `7bacdd8fd530411d8487b8721b89a1befd23d2f5` | 2026-09-20 | promoted |
| `SRC-2026-09-20-proxy-sourcing-qwen` | [raw/surveys/2026-09-20-proxy-sourcing-qwen.md](surveys/2026-09-20-proxy-sourcing-qwen.md) | survey | 2026-09-20 | llm-proposed | `6d0a72a8e279d0a59a39b4987a020db81a1fb083` | 2026-09-20 | promoted |
| `SRC-2026-09-20-institution-naming-chatgpt` | [raw/surveys/2026-09-20-institution-naming-chatgpt.md](surveys/2026-09-20-institution-naming-chatgpt.md) | survey | 2026-09-20 | llm-proposed | `d203bb554e241493fd1f5e181c94abf61daf6df6` | 2026-09-20 | promoted |
| `SRC-2026-09-20-institution-naming-claude` | [raw/surveys/2026-09-20-institution-naming-claude.md](surveys/2026-09-20-institution-naming-claude.md) | survey | 2026-09-20 | llm-proposed | `35bee4f3e12651e343236adcfd22fe7c27b29acc` | 2026-09-20 | promoted; capture retains the leading chat message before the report |
| `SRC-2026-09-20-institution-naming-deepseek` | [raw/surveys/2026-09-20-institution-naming-deepseek.md](surveys/2026-09-20-institution-naming-deepseek.md) | survey | 2026-09-20 | llm-proposed | `f3cf27eb3d709b48c3dc22e2bab088089c684db1` | 2026-09-20 | promoted |
| `SRC-2026-09-20-institution-naming-gemini` | [raw/surveys/2026-09-20-institution-naming-gemini.md](surveys/2026-09-20-institution-naming-gemini.md) | survey | 2026-09-20 | llm-proposed | `08c8d9e8aa171192052504c16238525c0783ce93` | 2026-09-20 | promoted |
| `SRC-2026-09-20-institution-naming-glm` | [raw/surveys/2026-09-20-institution-naming-glm.md](surveys/2026-09-20-institution-naming-glm.md) | survey | 2026-09-20 | llm-proposed | `5721ca3948704db34671e9e517341e2fa5e9d29d` | 2026-09-20 | promoted |
| `SRC-2026-09-20-institution-naming-grok` | [raw/surveys/2026-09-20-institution-naming-grok.md](surveys/2026-09-20-institution-naming-grok.md) | survey | 2026-09-20 | llm-proposed | `9451f1bcc33cfce496bc799318164248bc3d9829` | 2026-09-20 | promoted |
| `SRC-2026-09-20-institution-naming-qwen` | [raw/surveys/2026-09-20-institution-naming-qwen.md](surveys/2026-09-20-institution-naming-qwen.md) | survey | 2026-09-20 | llm-proposed | `00964e9d77c2878daebe3e2ff44c70dcb15a42ee` | 2026-09-20 | promoted |

## Hash convention

Every hash in the table above is the source's Git blob hash, and `.gitattributes` keeps the working copy byte-identical to it: Markdown originals are stored and checked out with LF, and `*.csv` is marked `-text` so the Korean reader export keeps the CRLF bytes it was delivered with. Use plain `git hash-object <path>` for a newly registered source; the registry is the authority for the current source set.

The `--no-filters` exception recorded here previously is no longer needed. It existed because the working copies of the LF-stored Markdown originals carried CRLF while the CSV was stored as delivered, so the two required different commands. `ccb350ed9eb8377147a755ab2d5f7ad7e2795062` is the value line-ending normalization would produce for that CSV; it is kept here only so the earlier query and roadmap log entries stay readable. No original and no registered hash changed.

## Note on the survey sources

The seven `critic-of-model` surveys are independent reviews produced by seven different language models in response to one shared review prompt, `LONGING_market_pricing_model_review_prompt.md`. That prompt is **not registered in this repository**, so every survey's framing — the fifteen report sections and the numbered questions they answer — reaches the Wiki only through the surveys themselves. Treat statements about what was asked as secondary citations.

The Pricing Model v2 factor-review prompt is registered as `SRC-2026-09-05-pricing-model-v2-factor-review-prompt`, so the second review round's framing is directly available and statements about what the second round was asked are primary citations. All six review originals are now registered and promoted.

The Qwen original was re-captured. Its first registration on 2026-09-05 recorded hash `59291ecd3ffdb1d45bbcc2ccc3d2403230242f15`, which described an incomplete capture: the file ended mid-expression partway through the response. On 2026-09-06 the user replaced it with the complete response, giving the current hash `07c1fb597b79ee4cdb4dc3fce9d65e201d6911c3`. This is a capture correction rather than a change to the evidence, and no Wiki material had been promoted from the incomplete file. The superseded hash is retained in the table row and the correction is recorded in `wiki/log.md`.

## Note on the third review round

The third round asks a different question from the first two. It does not ask for a factor set. It presents the six sets proposed in the second round, stripped of model identity and labelled SET A through SET F, and asks only what each set fails to price, fails to attribute, or cannot express. Advocacy, ranking, and new proposals are prohibited by the prompt.

The prompt exists in two registered versions. Version 1 is what the ChatGPT response was produced against. Its SET B heading read `12 priced factors` while a note stated that two of those twelve run unpriced initially, and the ChatGPT response records its own resolution of that tension in its Refusals section. Version 2 clarifies the heading and states the execution rule explicitly. The other seven completed reviews were collected against version 2, so the round spans two prompt versions and the difference is registered rather than hidden. All eight accepted reviews and the prompt/follow-up provenance are now promoted into `wiki/concepts/factor-set-failure-profile-review.md`; no factor set or repair has been adopted.

The ChatGPT original was captured from the response as pasted into the working conversation rather than from a direct export. If a direct export becomes available and differs, register it as a separate revision source under the rule in `raw/README.md`. Preserve this capture and its registered hash, and document the relationship between the two sources.

### Third-round collection provenance

Collection completed on 2026-09-06 after the user authorized sending the registered v2 prompt to the seven services. New conversations were used. The accepted answers all reach Section 6, cover all six sets and subparts, and contain at least two event examples per set. Completeness is distinct from correctness: unsupported mathematical claims, missing assumptions, and remaining imprecision are qualified in the Wiki rather than edited in the originals.

Claude's raw file is the generated review artifact downloaded as `longing-round3-failure-profiles.md`, copied byte-for-byte; it does not include the short surrounding chat message. DeepSeek, Gemini, GLM, Grok, Kimi, and Qwen are verbatim rendered response text captured from their answer containers, without translation or summarization. These are not Markdown-source or full-conversation exports: presentation markup, list markers, and mathematical layout may differ from native exports. GLM's capture retains the leading collapsed UI label `Thought Process`; the expanded reasoning itself was not collected. Kimi's reasoning panel was excluded. File hashes attest to preservation of these captures, not to a provider-side export format.

| Service | Displayed model or mode during collection | Conversation |
|---|---|---|
| Claude | Opus 5, Medium | [Review conversation](https://claude.ai/chat/2bd938c4-4002-431f-bc0d-eb8a50ceb309) |
| DeepSeek | Fast; exact backend model not displayed | [Review conversation](https://chat.deepseek.com/a/chat/s/b0f42cec-646a-4c36-9f35-4b3d31970ea3) |
| Gemini | Pro Extended | [Review conversation](https://gemini.google.com/app/8df74a626c188b7e) |
| GLM | GLM-5.3, Deep Think Max; generic tab title advertised GLM-5.3-Flash | [Review conversation](https://chat.z.ai/c/9364a789-38b9-4bd5-b0f4-668d41989d5e) |
| Grok | Fast; exact backend model not displayed | [Review conversation](https://grok.com/c/316083e3-0898-4870-be79-39ca3a0e213a?rid=2da4df68-9933-4ec2-a031-6b614f4c6379) |
| Kimi | Instant, High; service notice reported an automatic switch to K2.6 Instant | [Review conversation](https://www.kimi.ai/chat/1a0759d7-8cf2-8a2f-8000-09acae8fb281?chat_enter_method=new_chat) |
| Qwen | Qwen3.8-Max, Thinking | [Review conversation](https://chat.qwen.ai/c/a89c4e85-ad93-4b05-a238-a852d9e82c5c) |

Qwen's first response stopped during SET D(c); Kimi's stopped during Section 3. Each was asked for a complete replacement in the same conversation with its selected mode unchanged. Those terminal fragments were not registered as accepted reviews. Kimi's automatic fallback means the service and selected mode are known, but exact backend-model continuity is not verified; do not label the saved response as K3. No manual model switch or paid upgrade was made.

Gemini's first answer ended normally but contained only one event per set. That already registered source remains unchanged and raw-only; the separate `gemini-complete` source supplies the complete replacement used in synthesis. It is one review lineage, not two votes. The exact follow-up messages for Qwen, Kimi, and Gemini are preserved in the registered completion-requests document. Retrying did not introduce a new substantive project brief.

## Note on the 2026-09-06 working-session record

`SRC-2026-09-06-attribution-resolution-and-universe-scaling` is a compiled record of a working session, not a byte-exact conversation export. Repository mechanics from the same session were omitted; the substantive exchange was written up afterwards. The user's own statements are reproduced verbatim in Korean and marked as such, and the record closes with an explicit split between what the user decided and what the assistant proposed without confirmation. Treat the assistant's reasoning in it as paraphrase and the quoted Korean as primary.

## Note on the 2026-09-06 arbitrage and news-quality record

`SRC-2026-09-06-arbitrage-news-quality-and-next-work-items` is a compiled working-session record on the same terms as the ledger-resolution record above: not a byte-exact export, with the user's own statements reproduced verbatim in Korean and everything attributed to the assistant marked as paraphrase. The session opened with a long plain-language explanation pass over material already in the Wiki; that pass is described but not reproduced, because it introduced no new claim. What is reproduced is the closing turn, in which the user proposed two new mechanisms and set three work items. The record closes with an explicit statement that none of the five positions is a specified mechanism and that the assistant proposed nothing in the session.

## Academic survey provenance

The academic research brief is a compiled task handoff, not a verbatim user conversation. The research notes are an original LLM survey of primary papers, not copies of those papers. Applications and tests remain proposals. Neither source constitutes an adopted factor set or a calibrated pricing model.

## Note on the 2026-09-14 institutional typography and design sources

`SRC-2026-09-14-typographic-voice` and `SRC-2026-09-14-design-principles-draft` are **derivative imports**, copied byte-for-byte on 2026-09-15 from the TENDER SYSTEMS institutional repository, where they are registered under the same source IDs. The Git blob hashes recorded above are identical to the institutional ones, so the two registrations describe the same bytes. The institutional checkout they were taken from was at commit `233b7658d5733e0c2a4daab09790226a4548692f` (2026-09-09); both originals and the institutional Wiki pages promoted from them were present in that working tree but not yet committed there at import time, so the linked GitHub blob URLs resolve only after the institution publishes them.

Both are full ChatGPT exports of conversations dated 2026-09-14, renamed upstream from `ChatGPT-글꼴 스타일 요청-20260915-1209.md` and `ChatGPT-좋은 디자인 원칙-20260915-1211.md` to the required `YYYY-MM-DD-slug` form with their bytes preserved. They are external sessions with no access to this repository; nothing in them was written against LONGING's records, and the LONGING examples they contain are the source assistant's inventions, not project decisions.

What the user actually accepted in the typography source is the speaker rule and its three typefaces: Inconsolata as the system's base voice, Departure Mono for terminals, dashboards, monitoring surfaces, logs, and live status, and Source Serif for text a person wrote. The Korean auxiliary typeface, the "Source Serif 4" version, weights, sizes, spacing, per-system density, and the English formulation "Typography identifies the speaker" are the source assistant's proposals. Glyph claims — including which families ship a slashed zero — and every licensing statement are that assistant's reports and were **not** verified during this ingestion. The earlier per-system Sans/Mono split in the same export is superseded and was never adopted. No font was installed, obtained, rendered, or implemented.

In the design-principles source only the request for an abstract institutional layer that each work specialises is the user's own. The ten principles, the three-layer table, and the conflict ordering are the assistant's draft and the conversation ends on them with no user reply. The two Korean auto-generated video transcripts inside that export are machine-transcribed and visibly damaged, carry no title, channel, date, or URL, and are not registered as sources here; attributions in them to Dieter Rams, Louis Sullivan, Mies van der Rohe, Braun, and Apple are the speakers' claims, not verified facts.

The canonical owners of the shared rule are the institutional pages, not this repository: [DEC-006 — Typeface Identifies the Speaker](https://github.com/TENDER-SYSTEMS-LAB/tender-systems/blob/main/wiki/decisions/DEC-006-typographic-voice.md) and [Design Principles](https://github.com/TENDER-SYSTEMS-LAB/tender-systems/blob/main/wiki/concepts/design-principles.md). LONGING's own application is held in [[design-application]].

## Note on the 2026-09-15 reserve-absorption record

`SRC-2026-09-15-reserve-absorption-and-trust-instruments` is an **operator-captured transcript, not an exporter-generated export**. The user turns are reproduced verbatim in Korean and are the evidence for every decision promoted from it. The assistant turns are condensed by the capturing assistant into their substantive claims; phrasing and formatting are not preserved, so the file is not a byte-faithful record of assistant output and must not be cited as one. No user turn is paraphrased, reordered, or omitted.

The same file is registered in [longing-lab](https://github.com/TENDER-SYSTEMS-LAB/longing-lab) and [the-reserve-lab](https://github.com/TENDER-SYSTEMS-LAB/the-reserve-lab) under one source ID and one blob hash, `337bc0209634ddb3f6a9e2c01e40a0ea5689cae7`, because a single conversation concluded one system and moved its function into another. The GitHub URLs resolve only after publication.

## Note on the 2026-09-15 numeraire record

`SRC-2026-09-15-numeraire-and-standard-return` is **machine-extracted from the Claude Code session transcript**, not an operator retyping and not a vendor export. Its own capture note states the boundary: every user and assistant message verbatim and both structured questions with the options offered and the answer selected, with 38 tool invocations and their outputs, session-level system reminders, and two invoked skill bodies excluded. None of those carry conversation substance that is not also visible in the repository's own Git state. The export was taken during the session it records, so the closing turns that register it are not in it; the log entry covers them.

`SRC-2026-09-15-ai-reinforcing-loop-diagram` is the image the user pasted in turn 21 of that conversation, preserved as the binary it arrived as. It is **third-party material**, not the user's own composition: the user identified its origin in turn 37 as <https://youtu.be/W_ChhnAM7GY>, whose page title returned as `AI 기업들이 숨기고있는 소름끼치는 것`. The channel and upload date could not be verified from the page and are not recorded. It is registered as `user-originated` because the five permitted attribution values have no term for material a user brings in from elsewhere; the distinction is carried here rather than by the column. Only its reinforcing structure is promoted. Its named actors — fear marketing, political lobbying, litigation — are explicitly not adopted, because an actor who intends the decline contradicts `DEC-004`.

## Note on the 2026-09-16 simulation records

Three sources, and the reason for three is that they carry different weights.

`SRC-2026-09-16-loop-simulation-session` is the conversation, extracted the same
way as its predecessor and registered separately because a registered original is
never edited. It begins at the turn after the first export was taken.

`SRC-2026-09-16-loop-simulation-harness` is the model itself — a stdlib Python
file, the first executable artifact in this project. It is registered so the
findings can be reproduced or refuted rather than believed. **It is not a
component of the artwork**, and no part of it is a specification: it is an
instrument built to test whether DEC-007's mechanism can produce the shape
DEC-004 asks for.

`SRC-2026-09-16-loop-simulation-findings` is the report. Its attribution is
`llm-proposed` and this matters more than usual: these are assistant-authored
results from an assistant-authored model, run on invented parameters that are
calibrated against nothing. The findings identify where DEC-007 is
underspecified, which is a claim about the document. They establish nothing about
the world. One of them corrects an earlier version of the same report, and that
reversal is kept in the file rather than edited out.

Only one thing in this group is `user-confirmed`, and it is in the conversation,
not the report: the redefinition of anxiety as trust that never returns.

## Note on the three 2026-09-20 prompts and their responses

Registered **before** dispatch, on purpose. `current-state` has carried a
provenance warning since the first review round — *the review prompt is not
registered, so everything the surveys say about what was asked is a secondary
citation.* Registering a prompt when it is written rather than when its answers
arrive removes that class of defect for these rounds.

The three were dispatched on 2026-09-20, one prompt per fresh session per model,
and the responses are registered as surveys with `Ingested` `—`: nothing has been
synthesised into the Wiki yet. Kimi was not consulted this round. ChatGPT files
use the `chatgpt` suffix as in the third round.

Capture conditions: verbatim rendered response text from each answer container,
reasoning panels excluded, no translation. Two Claude captures (naming, sourcing)
keep the one-line chat message that preceded the report; Gemini's factor response
is in Korean. Hashes attest to preservation of these captures.

**One re-collection.** The sourcing captures first delivered as DeepSeek and
Gemini were byte-identical (md5 `6582166967cb1b5bfc4893d0f1b7c3e6`). The user
identified the text as DeepSeek's; the Gemini response was collected again and
registered separately. The mis-pasted duplicate was never registered.

The three ask for different kinds of work and should not be treated as one round.
The factor prompt asks what the universe can identify, which is analytic. The
sourcing prompt asks what is published, which is verifiable and where an invented
figure is the failure mode. The naming prompt asks for candidates and, more
importantly, for an honest account of what its collision check could not check.

## Note on the 2026-09-20 records

`SRC-2026-09-20-bearer-bond-issuance` is attributed `user-originated` rather than
`jointly-developed`, which is unusual for a conversation source and deliberate.
Every framing the assistant offered for what one BEARER BOND is was rejected, and
the model that replaced it — attention as principal, a perpetual instrument, a
decline made of calls, a write-down that answers the counterparty — is the user's.
So are the thirty-year span, the three markets, and the correction that technology
raises before it takes. The assistant's contribution is the arithmetic and the
register.

`SRC-2026-09-20-loop-simulation-harness-v3` **supersedes** the v2 harness, which
is retained unedited as every registered original is. Keeping all three builds
side by side is the point: each round's defects live in the build that had them,
and a corrected copy would hide them.

`SRC-2026-09-20-rebuild-findings` is `llm-proposed`, and carries the same boundary
as its predecessors. One item in it is a correction to the project's own method
rather than to the world: a test had been passing for the wrong reason because it
measured a quote, which carries an event premium, instead of the fundamental the
claim was about.

## Note on the 2026-09-19 market-texture records

`SRC-2026-09-19-loop-simulation-harness-v2` **supersedes**
`SRC-2026-09-16-loop-simulation-harness` as the current instrument. The earlier
file is retained unedited, as every registered original is, and the two are worth
keeping side by side: the first round's build is where three defects were found,
and a corrected copy would hide them.

The reference the user set the texture against — a screenshot of a third-party
market-data terminal showing a real equity index — is **not registered**. It was
supplied to name a target, nothing in the wiki rests on its content, and
preserving a vendor screenshot serves no provenance purpose. The conversation
describes it in place.

`SRC-2026-09-19-market-texture-findings` is `llm-proposed` for the same reason as
its predecessor, and carries one boundary explicitly: matching a real index's
statistics is a stylistic calibration to the terminal register of `DEC-002`. It
answers whether the surface reads as traded rather than drawn. It is not evidence
about human practice, and no factor, coefficient, basket, or historical span
becomes selected by having produced a convincing chart.

## Note on the 2026-09-15 reserve-absorption record — naming survey

The naming survey prompt drafted in turn 18 was never dispatched and no external model was consulted. `JOINT CUSTODY`, `BEARER ASSURANCE`, `BLIND CUSTODY`, and the separate holding institution they belonged to are withdrawn proposals, superseded within the same conversation by the fold into LONGING. Nothing in the transcript establishes a market model, a coefficient, a date series, or an implementation.
