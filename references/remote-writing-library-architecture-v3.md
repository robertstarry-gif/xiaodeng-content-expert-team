# Remote Writing Library Architecture V3

This package is public. The writing library can stay private.

The public skill contains workflow, safety rules, templates, and a small API helper. A private server stores domain cards, Chinese scene cards, bad/good sentence pairs, platform notes, and polishing methods. The server returns only a compact context pack for the current task.

## Recommended Flow

```text
User task
-> 小灯主编 creates a compact request
-> scripts/fetch_writing_context.py calls the private API
-> private library retrieves matching cards
-> API returns a context pack
-> 栗栗采风员 combines context pack with facts and boundaries
-> 小墨执笔人 drafts
-> 豆豆挑刺官 reviews for realism, claims, and AI-feel
-> 小剪修订员 revises
```

## Public Package Responsibilities

- Decide when a remote context pack is useful.
- Send only task-relevant metadata.
- Handle unavailable network or missing credentials gracefully.
- Never expose private corpus content in GitHub.
- Never require the remote library for basic use.

## Private Library Responsibilities

- Store cards by domain, platform, reader group, topic, and risk level.
- Return a small task-specific pack, not raw documents.
- Redact internal notes that should not be public.
- Log safely and avoid storing unnecessary user input.
- Version the API so public installers can stay stable.

## Environment Variables

- `CREATOR_CONTENT_LIBRARY_URL`: full API endpoint URL.
- `CREATOR_CONTENT_LIBRARY_TOKEN`: optional bearer token.
- `CREATOR_CONTENT_LIBRARY_TIMEOUT`: optional timeout in seconds, default `12`.

Example:

```bash
export CREATOR_CONTENT_LIBRARY_URL="https://example.com/v1/context-pack"
export CREATOR_CONTENT_LIBRARY_TOKEN="replace-with-your-token"
```

## Request Shape

The helper sends JSON like:

```json
{
  "skill": "creator-content-expert-team",
  "version": "4.0.0",
  "language": "zh-CN",
  "domain": "food",
  "topic": "after-work simple meals",
  "platform": "newsletter",
  "audience": "busy urban workers",
  "risk_level": "low",
  "voice": "warm, concrete, not preachy",
  "needs": [
    "reader scenes",
    "domain texture",
    "bad sentence warnings",
    "rewrite moves"
  ]
}
```

## Response Shape

Return JSON with these fields when possible:

```json
{
  "available": true,
  "pack_id": "context-pack-id",
  "library_version": "2026-05-11",
  "domain_cards": [],
  "reader_scenes": [],
  "knowledge_points": [],
  "bad_sentence_warnings": [],
  "rewrite_pairs": [],
  "platform_notes": [],
  "claim_boundaries": [],
  "source_notes": []
}
```

The response may include short examples, but it should not include raw private documents.

## Suggested Card Schema

Each private card can use:

- `card_id`
- `card_type`: `scene`, `knowledge`, `rewrite_pair`, `bad_sentence`, `platform_note`, `claim_boundary`, `title_pattern`, `opening_pattern`
- `domain`
- `topic_tags`
- `reader_group`
- `platform`
- `risk_level`
- `usable_when`
- `avoid_when`
- `sample`
- `notes`
- `source_label`
- `updated_at`

## Security Notes

- Put API keys in environment variables, never in `SKILL.md`, README, or templates.
- Keep the private library server-side.
- Prefer returning distilled context over searchable raw passages.
- Rate limit the endpoint if the public GitHub package becomes popular.
- Treat medical, legal, and financial cards as educational context, not professional advice.

## Failure Behavior

If the remote call fails, the skill should continue with local rules:

- use `references/chinese-real-context-guide-v3.md`;
- use source research when claims are factual or high-stakes;
- do not pretend a private context pack was used.
