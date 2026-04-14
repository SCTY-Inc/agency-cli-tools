# brief.v1 echo handoff proof

This repo stays bounded to the `brief.v1` writer role for loop 3.

## Scope

`brand-os` proves only that `brandos plan run --brief-v1-output ...` can emit a canonical, echo-consumable `brief.v1` artifact.

It does **not** add ownership for:
- `forecast.v1`
- simulation runtime behavior
- cross-repo orchestration
- any new echo-side logic

## Canonical authority

Parent-level protocol artifacts remain authoritative:
- `../protocols/brief.v1.schema.json`
- `../protocols/examples/brief.v1.rich.json`
- `../protocols/lineage-rules.md`

The repo-local fixture mirror at `tests/fixtures/brief.v1.rich.mirror.json` is intentionally a mirror of the parent canonical rich example. If the parent example changes, update the mirror to match exactly.

## Repo-local proof surfaces

1. `tests/plan/test_brief_v1.py` validates that the mirror fixture matches the parent canonical example exactly.
2. `tests/plan/test_brief_v1.py` smoke-tests `brandos plan run --brief-v1-output ...` with a canonical `voice_pack.v1` input fixture.
3. The smoke test validates the emitted payload through the local `BriefV1` model, confirming the output stays canonical and consumable by downstream repo adapters without requiring a live cross-repo invocation.

## Expected emitted contract

The emitted artifact keeps the family-owned `brief.v1` shape:
- `artifact_type = "brief.v1"`
- `schema_version = "v1"`
- canonical writer = `{ "repo": "brand-os", "module": "agentcy-compass" }`
- stable lineage keys including `brief_id`, `brand_id`, `voice_pack_id`, and `lineage.source_voice_pack_id`

That is the only handoff proof this repo owns for loop 3.
