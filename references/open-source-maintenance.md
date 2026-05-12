# Open Source Maintenance

Use this when updating the public skill package.

## Rules

1. Keep the active `SKILL.md` concise and domain-neutral.
2. Put domain details in references.
3. Keep private names, local paths, app-specific memories, and unpublished workflows out of the package.
4. Keep high-stakes medical, legal, and financial boundaries explicit.
5. Keep default output user-facing: artifact first, report only when requested or needed for risk.

## Validation

Run from the skill root:

```bash
python3 scripts/validate_creator_content_expert_team.py
```

Expected output:

```text
OK: Creator Content Expert Team public skill valid
```

Also run the platform's normal skill validator if available.

## Public Release Checklist

- [ ] No private names, paths, project names, memories, or local workflows.
- [ ] License metadata matches the repository license.
- [ ] Domain risk rules cover legal, medical, and financial content.
- [ ] Templates do not mention a private creator.
- [ ] Validator passes.
