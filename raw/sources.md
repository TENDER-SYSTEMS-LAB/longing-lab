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
