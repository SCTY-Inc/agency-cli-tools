# `cli-metrics` absence map and loop-5 `performance.v1` readiness scan

Date: 2026-04-12
Status: family readiness artifact for loop 5
Scope: parent-owned readiness and protocol framing only; no `cli-metrics` bootstrap

## Executive read

`cli-metrics` is currently absent as a working family repo.
That means loop 5 is not ready for implementation-heavy analytics work.
The bounded family-ready move is narrower:

- treat future `agentcy-pulse` as measurement-only
- use canonical published `run_result.v1` from `cli-phantom` / `agentcy-loom` as the only upstream seam for v1
- limit first-wave `performance.v1` to published `social.post` outcomes only
- keep the work at the parent family layer: schema, examples, lineage rules, and docs/test-only seam proof

## 1. Current absence map

### Repo state

Current practical state in `/Users/amadad/projects`:

- `cli-metrics/` is missing from the family workspace
- there is no repo-local runtime, CLI, fixture set, or tests that currently emit canonical `performance.v1`
- there is no proven analytics adapter seam yet for platform reads, metric normalization, or backfill flows
- there is no family-approved storage/runtime boundary yet for measurement collection

### What this means

`cli-metrics` is still a future writer target, not a present implementation surface.
So loop 5 should not start with:

- repo bootstrap
- live platform integrations
- dashboards or warehouse work
- broad attribution abstractions
- retraining infrastructure

Instead, loop 5 should prove the family contract first.

## 2. Upstream seam already available now

The strongest usable upstream seam is the canonical published `run_result.v1` artifact already owned by `cli-phantom` / `agentcy-loom`.

### Why this seam is sufficient for a first pulse slice

Current family protocol artifacts already show that published `run_result.v1` can carry:

- `run_id`
- `brief_id`
- `brand_id`
- `workflow`
- `started_at`
- `completed_at`
- writer ownership: `{ repo: "cli-phantom", module: "agentcy-loom" }`
- carried lineage:
  - `source_voice_pack_id`
  - `campaign_id`
  - `signal_id`
- per-platform delivery locators in published runs:
  - `platform`
  - `post_id`
  - `url`

### Evidence already present in family artifacts

From `protocols/run_result.v1.schema.json` and `protocols/examples/run_result.v1.published.json`:

- delivery platform items allow `post_id` and `url`
- canonical published examples already model platform-level locator data
- lineage is already normalized into family field names rather than repo-local internals

From `cli-phantom/runtime/src/domain/run-result-v1.ts`:

- published delivery results map repo-local publish output into canonical delivery items
- `postId` becomes canonical `post_id`
- `postUrl` becomes canonical `url`
- canonical export only happens once the run is in an exportable state

## 3. First-wave source boundary for `performance.v1`

The first-wave source boundary should be explicit:

### In scope for `performance.v1` v1

Only canonical published `social.post` outcomes.

Required shape of the upstream source:

- `run_result.v1.status = "published"`
- `run_result.v1.workflow = "social.post"`
- at least one delivery platform record with:
  - `platform`
  - and a publish locator via `post_id` and/or `url`

### Out of scope for `performance.v1` v1

These are explicitly excluded from the first wave:

- dry-run analytics
- failed-run analytics
- blog analytics
- outreach analytics
- reply analytics
- non-`social.post` workflows
- audience-level or user-level records
- secret-bearing export shapes

This keeps the first pulse slice measurement-only and prevents it from becoming a generic execution-history mirror.

## 4. Downstream readers worth naming now

The purpose of naming downstream readers is not to move ownership.
It is to show why a narrow `performance.v1` is useful once it exists.

### `brand-os` learning and calibration surfaces

Likely downstream readers:

- `brand-os/src/brand_os/core/learning.py`
  - already computes aggregate learning metrics and recommendations
  - is a natural reader of outcome summaries keyed by brand / decision type / success-like measures
- `brand-os/src/brand_os/loop_cli.py`
  - already exposes learning metrics and recommendation surfaces
  - is the most obvious future place to display pulse-fed performance summaries without moving measurement ownership into `brand-os`

Interpretation:
`brand-os` should consume aggregated performance snapshots as learning input.
It should not become the canonical writer of those measurement artifacts.

### `cli-prsna` drift and feedback surfaces

Likely downstream readers:

- `cli-prsna/src/prsna/drift.py`
  - currently evaluates consistency and drift against persona definitions
- `cli-prsna/src/prsna/learning.py`
  - already stores interaction logs and extracts learnings / suggested improvements

Interpretation:
future pulse outputs can become one source of aggregate feedback about what published voice variants performed better or worse.
But `cli-prsna` should remain a reader of those drift-feedback signals, not the owner of analytics collection.

## 5. Ownership guardrail: what `agentcy-pulse` is and is not

### `agentcy-pulse` is measurement-only

Allowed ownership for the future module:

- performance snapshots
- attribution records
- aggregate performance summaries
- drift feedback signals derived from aggregate outcomes

### `agentcy-pulse` is not

It is not the owner of:

- strategy authoring
- brief generation
- publishing runtime
- persona authoring
- secrets or auth-token protocol artifacts
- audience-level or user-level PII in canonical examples/tests

This matters because the family already has clearer owners:

- `brand-os` / `agentcy-compass` owns strategy and briefs
- `cli-phantom` / `agentcy-loom` owns publish/runtime outcomes
- `cli-prsna` / `agentcy-vox` owns persona and drift logic

Pulse should measure those outputs, not absorb them.

## 6. First-wave exclusions and why they stay excluded

### Dry-run outcomes

Exclude from v1 because they prove the seam but do not represent real audience exposure.
They are useful for loom validation, not for pulse measurement.

### Failed outcomes

Exclude from v1 because they are runtime/error states, not canonical performance observations.
They may matter later for ops analytics, but not for the first measurement slice.

### Blog, outreach, and reply analytics

Exclude from v1 because they would widen the surface too early:

- different locator semantics
- different metric semantics
- likely different platform/API contracts
- higher risk of sprawling into a broad analytics abstraction before the social-post seam is proven

### Audience/user-level analytics

Exclude from v1 because loop 5 must keep canonical artifacts free of:

- tokens
- auth material
- account secrets
- audience-level PII
- user-level PII

The first family artifact should carry only lineage, publish locators, timestamps, and aggregate metrics.

## 7. Readiness conclusion

Current readiness is sufficient for protocol work, but not for implementation-heavy runtime work.

### Ready now

- parent-owned readiness documentation
- family-owned `performance.v1` schema
- canonical examples
- lineage rule extension for `performance.v1`
- docs/test-only loom seam proof using published `run_result.v1`
- family validation that examples stay aggregate-only and secret-free

### Not ready now

- `cli-metrics` repo bootstrap
- live platform analytics reads
- adapters for every publish workflow
- broad storage/runtime design
- analytics collection daemons or scheduling
- strategy or persona ownership changes

## 8. Smallest next actionable slice

The smallest next actionable slice is:

1. family-owned `performance.v1` schema/examples/lineage for published `social.post` outcomes only
2. a docs/test-only loom seam proof that canonical published `run_result.v1` exposes the locators pulse needs
3. no `cli-metrics` repo bootstrap yet
4. no live analytics integrations yet

## Bottom line

`cli-metrics` is absent, so loop 5 should stay protocol-first.
The family already has enough upstream signal in canonical published `run_result.v1` to define a minimal `performance.v1` contract.
That first contract should cover published `social.post` outcomes only, keep `agentcy-pulse` measurement-only, exclude dry-run/failed/blog/outreach/reply analytics, and stop before any runtime bootstrap.