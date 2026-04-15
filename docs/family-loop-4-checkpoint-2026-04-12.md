# Agentcy family loop-4 checkpoint — bounded `cli-agency` narrowing and re-home scope

Date: 2026-04-12
Status: superseded historical checkpoint; replaced by `family-loop-5-checkpoint-2026-04-12.md`

This checkpoint moves the family control plane from the completed loop-3 seam into loop 4.

Loop 3 proved the canonical `brief.v1 -> forecast.v1` handoff.
Loop 4 is not a giant merge. It is a bounded narrowing pass over `cli-agency` so the family can decide what should be kept, re-homed into `brand-os` / future `agentcy-compass`, or explicitly archived.

## Prior slice closed

The completed third bounded slice is:

`brief.v1 -> forecast.v1`

Locked result:
- `brand-os` remains the canonical writer for `brief.v1`
- `cli-mirofish` / future `agentcy-echo` remains the canonical writer for `forecast.v1`
- parent family artifacts remain authoritative for schemas, lineage rules, examples, protocol tests, and ownership notes
- completed-only canonical `forecast.v1` exports remain the family contract; failed/partial forecast states stay repo-local unless a later slice says otherwise

## Loop-4 scope

The active fourth bounded slice is:

`cli-agency` narrowing -> `brand-os` / future `agentcy-compass`

Loop 4 is limited to:
- keep/re-home/archive decisions around `cli-agency` research surfaces
- keep/re-home/archive decisions around `cli-agency` strategy surfaces
- the smallest high-value concepts from `agency/schemas/research.py`, `agency/schemas/strategy.py`, and related research/strategy stage prompts that help strengthen `brand-os` as the strategy/policy/brief layer
- thin parent-level ownership notes, checkpoints, and bounded repo-local follow-up tasks

Loop 4 is explicitly not:
- a justification for making `cli-agency` the family root
- a broad merge of all `cli-agency` runtime surfaces into `brand-os`
- a family-wide runtime unification pass
- a monolith move disguised as “consolidation”

## Ownership restatement

### Canonical writers remain unchanged

| Artifact | Canonical writer repo | Family module |
| --- | --- | --- |
| `voice_pack.v1` | `cli-prsna` | `agentcy-vox` |
| `brief.v1` | `brand-os` | `agentcy-compass` |
| `forecast.v1` | `cli-mirofish` | `agentcy-echo` |
| `run_result.v1` | `cli-phantom` | `agentcy-loom` |
| `performance.v1` | `cli-metrics` / future repo | `agentcy-pulse` |

### `cli-agency` role in loop 4

`cli-agency` is source material for `agentcy-compass`, not the family root.

Allowed influence:
- research framing
- strategy field ideas
- stage/prompt concepts that strengthen brief creation or decision support inside `brand-os`

Not part of the canonical family center:
- shared root ownership
- protocol ownership
- canonical artifact writing
- cross-family runtime orchestration

## Keep / re-home / archive boundary

### Likely keep or re-home candidates

The bounded candidates under consideration are the smallest concepts that reinforce `brand-os` strategy ownership, such as:
- research-stage ideas
- strategy-stage ideas
- brief-shaping prompt structures
- decision-support schemas or field ideas that help produce better `brief.v1`

### Explicit leave-behind or archive candidates

These remain out of scope for loop 4 unless a later checkpoint says otherwise:
- `.agency/` store conventions
- plugin surfaces
- MCP surface
- interactive resume state machine
- umbrella CLI assumptions
- activation/runtime ownership that belongs downstream of `brief.v1`
- any attempt to make `cli-agency` a second `brief.v1` writer or a family protocol authority

## Deferrals still in force

The following remain explicitly deferred during loop 4:
- giant family renames
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- `cli-metrics` / `performance.v1`

These deferrals stay in force because loop 4 is about narrowing and re-home discipline, not expanding the family into one runtime.

## Implementation gate for loop 4

From this checkpoint forward:
- `brand-os` remains the canonical `brief.v1` writer
- `brand-os` is the sole canonical `brief.v1` writer; loop 4 does not create a second writer, alternate writer, or protocol authority for `cli-agency`
- `cli-agency` is reference/source material only and should not be treated as the family root
- any `cli-agency` follow-up should map to keep vs re-home vs archive, not generic merge language
- parent-level docs should stay authoritative for ownership and scope boundaries
- repo-local work should be the smallest concrete move that strengthens `brand-os` strategy ownership without absorbing plugins, stores, MCP, or unrelated runtime surfaces

## Immediate next-task shape implied by this checkpoint

1. restate the loop-4 control-plane language in the parent docs
2. confirm the smallest `cli-agency` research/strategy surfaces worth re-homing into `brand-os`
3. create one bounded `brand-os` implementation task for that first re-home seam
4. keep all giant-merge and umbrella-runtime ideas deferred until smaller seams are proven

## Bottom line

Loop 3 is complete.
Loop 4 is superseded and now historical.
`brand-os` stays the canonical `brief.v1` writer.
`cli-agency` is source material to narrow and selectively re-home, not the family root.
Active family control now lives in `family-loop-5-checkpoint-2026-04-12.md` for the bounded `cli-metrics` / `performance.v1` readiness wave.