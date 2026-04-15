# Agentcy family loop-6 checkpoint — bounded `agentcy-pulse` seam from canonical published `run_result.v1` to `performance.v1`

Date: 2026-04-12
Status: active checkpoint with landed seam evidence; loop 5 remains the locked protocol baseline

This checkpoint now records loop 6 as the bounded implementation follow-up to loop 5 with direct family-level seam evidence landed.
Loop 5 already proved the family control plane can lock the `run_result.v1 -> performance.v1` path without repo bootstrap.
Loop 6 adds the thinnest possible seam proof on top of that baseline: a family-owned fixture-only harness or tiny adapter that consumes canonical published `run_result.v1` and deterministically emits canonical `performance.v1`.

## Prior slice locked, not reopened

The prior fifth bounded slice is:

`cli-metrics` readiness -> future `agentcy-pulse` -> `performance.v1`

Locked result:
- `family-loop-5-checkpoint-2026-04-12.md` remains the protocol baseline for the first bounded `run_result.v1 -> performance.v1` slice
- docs, schema, examples, lineage rules, loom seam proof, and family validation are already landed and should not be reopened unless a concrete seam gap is found
- `cli-metrics` remains absent or not implementation-ready as a working family repo
- loop 5 stays the authority for scope, privacy guardrails, and what remains deferred

## Loop-6 scope

The active sixth bounded slice is:

`agentcy-pulse` thin family-owned seam for canonical published `run_result.v1 -> performance.v1`

Loop 6 is limited to:
- a family-owned fixture-only harness or tiny adapter seam
- consumption of the sole canonical source fixture `protocols/examples/run_result.v1.published.json`
- deterministic emission or mirroring of canonical `performance.v1`
- direct validation of success and rejection cases from canonical parent fixtures
- explicit proof that the seam stays measurement-only and does not widen ownership

Loop 6 is explicitly not:
- a `cli-metrics` repo bootstrap
- a search for a second canonical upstream fixture
- live analytics ingestion or platform API integration work
- umbrella CLI work or a new family runtime surface
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges

## Canonical source and authority

The sole canonical source fixture for the seam is:

`protocols/examples/run_result.v1.published.json`

Authority rules:
- this fixture is the only canonical published `run_result.v1` input the first pulse seam should read from
- any repo-local mirror fixture, including a possible future `cli-phantom` convenience copy, is optional, non-blocking, and non-authoritative
- canonical lineage and publish locators must come from the canonical published loom artifact, not from the adapter sidecar input

## Minimal deterministic seam contract

The loop-6 seam should stay narrow and deterministic.

Expected canonical input split:
1. canonical published `run_result.v1`
2. a tiny sidecar measurement envelope carrying only aggregate observation data that the loom artifact cannot invent itself

### Required sidecar fields

- `performance_id`
- `measured_at`
- `observations`

### Optional sidecar fields

- `window`
- `summary.notes`

### Observation minimums

Each observation should minimally provide:
- the intended `platform`
- a non-empty aggregate `metrics` object

### Locked derivation rule

The seam must copy, preserve, or derive from canonical published `run_result.v1`:
- `run_id`
- `brief_id`
- `brand_id`
- lineage fields such as `source_voice_pack_id`, `campaign_id`, and `signal_id` when present
- publish locators such as `platform`, `post_id`, and `url`

The seam must not invent publish locators from the sidecar input.

## Ownership restatement

Canonical writers remain unchanged:

| Artifact | Canonical writer repo | Family module |
| --- | --- | --- |
| `voice_pack.v1` | `cli-prsna` | `agentcy-vox` |
| `brief.v1` | `brand-os` | `agentcy-compass` |
| `forecast.v1` | `cli-mirofish` | `agentcy-echo` |
| `run_result.v1` | `cli-phantom` | `agentcy-loom` |
| `performance.v1` | `cli-metrics` / future repo | `agentcy-pulse` |

Loop 6 does not create a second writer for either artifact.
It only proves the thinnest bounded seam between the existing canonical upstream artifact and the future canonical downstream artifact.

## Validation gate for loop 6

Success now means, and is now evidenced by:
- the seam reads canonical published `run_result.v1` from the parent `protocols/examples/` surface
- canonical lineage and publish locators are preserved into `performance.v1`
- sidecar observations remain aggregate-only and measurement-only
- the tiny adapter can load deterministically from fixture paths without network access and match a golden expected `performance.v1` output
- rejection cases fail for dry-run, failed, non-`social.post`, missing-locator, and unmatched-platform inputs

The strongest honest implementation order remains:
1. re-anchor loop 6 in the control-plane docs
2. lock the deterministic seam contract
3. implement the tiny family-owned adapter or fixture harness
4. validate success and rejection cases directly from canonical parent fixtures
5. merge evidence back into the control plane

## Landed loop-6 evidence

The family now has direct loop-6 seam evidence via the parent-owned adapter and fixtures:
- `protocols/adapters/run_result_to_performance_v1.py`
- `protocols/tests/test_run_result_to_performance_adapter.py`
- `protocols/tests/fixtures/run_result_to_performance_v1/sidecar.rich.json`
- `protocols/tests/fixtures/run_result_to_performance_v1/performance.rich.expected.json`

What this evidence proves:
- canonical published `run_result.v1 -> performance.v1` is now proven by a deterministic family-owned adapter seam, not just by schema/examples/docs alone
- `protocols/examples/run_result.v1.published.json` remains the sole canonical source fixture for the seam
- loop-5 contract artifacts remain locked while loop 6 adds only a tiny adapter and canonical-fixture proof surface
- canonical lineage, publish locators, and privacy bounds survive the seam unchanged
- the seam remains narrow enough to avoid turning `agentcy-pulse` into publishing, strategy, persona, or runtime ownership

## Next bounded pulse boundary

The next acceptable pulse boundary remains narrower than a new repo wave:
- preserve the current family-owned adapter seam as the proof surface unless a concrete gap appears
- do not introduce a second canonical upstream fixture
- do not widen beyond published `social.post` aggregate measurements
- do not start live analytics integrations
- do not start heavy `cli-metrics` repo bootstrap

Any later follow-up should be a tiny maintenance or ingestion seam only, and only if it preserves the locked loop-5 contract plus the landed loop-6 seam evidence.

## Deferrals still in force

The following remain explicitly deferred during loop 6:
- giant family renames
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- heavy `cli-metrics` repo bootstrap
- live analytics platform integrations
- broad analytics abstractions beyond published `social.post`
- dry-run, failed, blog, outreach, reply, or non-`social.post` analytics for `performance.v1` v1

These deferrals remain in force because loop 6 is only a seam proof follow-up to the already-locked loop-5 protocol baseline.

## Bottom line

Loop 5 remains the locked protocol baseline.
Loop 6 is now the active bounded implementation follow-up.
The family may prove only a thin `agentcy-pulse` seam from canonical published `run_result.v1` to canonical `performance.v1`.
The seam must stay family-owned, deterministic, fixture-first, and narrow enough to avoid turning `agentcy-pulse` into a bootstrap, integration, or runtime-unification project.