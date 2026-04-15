# Agentcy family loop-5 checkpoint — bounded `cli-metrics` readiness and `performance.v1` path

Date: 2026-04-12
Status: active checkpoint with loop-5 evidence merged; next follow-up remains bounded

This checkpoint moves the family control plane from the superseded loop-4 `cli-agency` narrowing branch into loop 5.

Loop 4 established that `brand-os` remains the canonical `brief.v1` writer and that `cli-agency` is source material rather than the family root.
Loop 5 is not a repo bootstrap. It is a bounded readiness and protocol pass for `cli-metrics` / future `agentcy-pulse` and the smallest viable path to canonical `performance.v1`.

## Prior slice superseded

The superseded fourth bounded slice is:

`cli-agency` narrowing -> `brand-os` / future `agentcy-compass`

Locked result:
- `brand-os` remains the canonical writer for `brief.v1`
- `cli-agency` remains source material for selective re-home work, not the family root and not a canonical shared-artifact writer
- loop 4 decisions remain valid historical context, but loop 4 is no longer the active family branch

## Loop-5 scope

The active fifth bounded slice is:

`cli-metrics` readiness -> future `agentcy-pulse` -> `performance.v1`

Loop 5 is limited to:
- a parent-level readiness scan documenting the current absence or unreadiness of `cli-metrics`
- a minimal family-owned `performance.v1` protocol definition
- a thin seam proof that canonical published `run_result.v1` contains the lineage and publish locators needed for measurement
- a thin family validation pass for canonical `run_result.v1 -> performance.v1`

Loop 5 is explicitly not:
- a `cli-metrics` repo bootstrap
- live analytics ingestion or platform API integration work
- a broad metric abstraction for every workflow
- a justification for moving strategy, publishing, persona, or generic runtime ownership into `agentcy-pulse`
- a family-wide runtime unification pass
- a monolith move disguised as “analytics readiness”

## Current readiness statement

Current practical state:
- `cli-metrics` is not yet present as a working family repo with a proven implementation seam for this wave
- `performance.v1` is not yet a live runtime-owned artifact
- the strongest upstream seam already available to the family is canonical published `run_result.v1` from `cli-phantom` / `agentcy-loom`
- loop 5 has now proven the bounded family path with docs, schema, examples, lineage rules, loom seam evidence, and validation before any runtime bootstrap

## Ownership restatement

### Canonical writers remain unchanged

| Artifact | Canonical writer repo | Family module |
| --- | --- | --- |
| `voice_pack.v1` | `cli-prsna` | `agentcy-vox` |
| `brief.v1` | `brand-os` | `agentcy-compass` |
| `forecast.v1` | `cli-mirofish` | `agentcy-echo` |
| `run_result.v1` | `cli-phantom` | `agentcy-loom` |
| `performance.v1` | `cli-metrics` / future repo | `agentcy-pulse` |

### `agentcy-pulse` role in loop 5

`agentcy-pulse` is the future measurement and attribution layer only.

Allowed ownership:
- performance snapshots
- attribution records
- performance summaries
- drift feedback signals derived from aggregate outcomes

Not part of pulse ownership:
- strategy authoring
- publishing runtime ownership
- persona authoring
- auth/token storage in family-owned protocol artifacts
- audience-level or user-level PII in canonical artifacts, examples, or tests

## Minimal first `performance.v1` shape implied by this checkpoint

The smallest viable first `performance.v1` is a narrow measurement snapshot for published `social.post` outcomes only.

It should:
- reference canonical loom output through `run_id`
- preserve upstream lineage through `brief_id`, `brand_id`, and carried lineage like `source_voice_pack_id`, `campaign_id`, and `signal_id`
- capture per-platform publish locators such as `post_id` and `url` when available
- keep metric fields narrow, aggregate, and optional
- exclude secrets, tokens, auth material, and audience-level or user-level PII

It should not yet include:
- dry-run outcomes
- failed outcomes
- blog, outreach, reply, or non-`social.post` analytics
- per-user audience records
- broad warehouse, dashboard, or retraining infrastructure

## Deferrals still in force

The following remain explicitly deferred during loop 5:
- giant family renames
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- heavy `cli-metrics` repo bootstrap
- live analytics platform integrations
- broad analytics abstractions beyond published `social.post`

These deferrals stay in force because loop 5 is about proving the narrow family protocol seam first, not building the full analytics product surface.

## Implementation gate for loop 5

From this checkpoint forward:
- `family-loop-5-checkpoint-2026-04-12.md` is the only active family control-plane checkpoint
- `family-loop-4-checkpoint-2026-04-12.md` remains historical context and must not be treated as an active parallel branch
- loop 5 is evidenced in this order: readiness scan, protocol definition, loom seam proof, and thin validation
- any future `cli-metrics` follow-up should remain thin and seam-driven; the protocol artifacts are already proven and should not be expanded into repo bootstrap by default
- parent-level docs remain authoritative for ownership, scope, exclusions, and privacy guardrails

## Immediate next-task shape implied by this checkpoint

1. treat the loop-5 readiness scan, `performance.v1` schema/examples/lineage, loom seam proof, and family validation as landed evidence for the bounded `run_result.v1 -> performance.v1` slice
2. if implementation work continues, limit it to a future thin `cli-metrics` fixture or adapter seam that consumes canonical published `run_result.v1` and emits or mirrors canonical `performance.v1`
3. keep docs/schema/examples/tests as the already-locked contract surface unless a specific seam gap is discovered
4. keep repo bootstrap, live integrations, and runtime unification deferred

## Bottom line

Loop 4 is superseded and now historical.
Loop 5 is active and now evidenced as complete at the readiness/protocol/seam/validation layer.
`cli-metrics` / future `agentcy-pulse` is still not implementation-ready as a working repo, so the next step is not a bootstrap.
The only named next implementation candidate is a future thin `cli-metrics` fixture or adapter seam for published `social.post` `run_result.v1 -> performance.v1` outcomes.
