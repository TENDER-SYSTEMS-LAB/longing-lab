# Raw

This directory is the Source of Truth. It preserves originals unchanged: conversation exports, documents, surveys, and unclassified material.

## Directories

- `conversations/` — exported conversation transcripts
- `documents/` — standalone documents
- `surveys/` — survey or evaluation outputs collected from multiple models
- `inbox/` — material that has arrived but has not been classified yet

## Adding a Source

1. Place the original, unchanged, under the directory matching its type. Use the filename form `YYYY-MM-DD-short-slug.md`.
2. Compute its hash:

   ```bash
   git hash-object raw/<type>/YYYY-MM-DD-short-slug.md
   ```

3. Append one row to [`sources.md`](sources.md) with the source ID `SRC-YYYY-MM-DD-short-slug`, the path, the type, the date, the attribution, the hash, and the ingestion status.

## Rules

- Never edit or delete a registered source. If a correction is needed, register the corrected version as a separate source.
- A registered file that turns out to be an incomplete or corrupted capture of its original is a capture failure, not a revision of the evidence. Replace the file with a correct capture under the same source ID, update the hash, and record the superseded hash and the reason in `wiki/log.md`. This exception applies only when no Wiki material has been promoted from the defective capture. If any has, register the corrected capture as a separate revision source instead so the earlier basis stays traceable.
- Registered sources keep their original language. The repository's English-default policy applies to the Wiki, not to evidence.
- Registration is not promotion. A source enters the Wiki only when the promotion rules in [`../schema.md`](../schema.md) are satisfied.
