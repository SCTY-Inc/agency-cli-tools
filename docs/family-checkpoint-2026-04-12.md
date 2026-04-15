# Agentcy family checkpoint — ownership matrix, first slice, and deferrals

Date: 2026-04-12
Task: `task-6`
Status: approved checkpoint for the next implementation wave

This checkpoint consolidates the current repo-local breadth scans into one explicit family decision artifact.

It is the gate for the next implementation work.

Implementation should proceed from this checkpoint and the referenced scorecards, not from informal planning prose alone.

## Inputs consolidated

This checkpoint is based on:

- `brand-os/docs/ownership-scorecard-2026-04-12.md`
- `cli-prsna/docs/voice-pack-v1-scorecard.md`
- `cli-mirofish/docs/forecast-v1-deferral-scorecard.md`
- `cli-phantom/docs/agentcy-loom-breadth-scan-2026-04-12.md`
- `cli-agency/docs/re-home-candidate-scorecard-2026-04-12.md`
- `AGENTCY_RECAP.md`
- `AGENTCY_STACK.md`
- `CONSOLIDATION.md`

## Decision summary

### 1. One writer per artifact

The family will treat these artifact owners as explicit, not provisional planner shorthand.

| Artifact | Canonical writer | Current repo | Notes |
| --- | --- | --- | --- |
| `voice_pack.v1` | `agentcy-vox` | `cli-prsna` | Canonical machine-readable export should come from the `Persona` authoring model, not from downstream adapter formats. |
| `brief.v1` | `agentcy-compass` | `brand-os` | Canonical brief should be emitted from the planning pipeline, not from persona, publish, or downstream execution surfaces. |
| `scenario_pack.v1` | `agentcy-compass` or thin family orchestration layer | parent/future | Not part of the first implementation slice; keep ownership narrow until a real scenario handoff is needed. |
| `forecast.v1` | `agentcy-echo` | `cli-mirofish` | Deferred; define later as a thin projection over exported run/report artifacts. |
| `run_result.v1` | `agentcy-loom` | `cli-phantom` | Deferred; define later around delivery artifact plus final run state. |
| `performance.v1` | `agentcy-pulse` | `cli-metrics` / not yet built | Deferred; no current writer exists because the module is not yet built. |

## Ownership matrix by repo

| Repo | Family module | Owns canonically | Consumes canonically | Explicit non-ownership / leave-behind |
| --- | --- | --- | --- | --- |
| `cli-prsna` | `agentcy-vox` | `voice_pack.v1` | future performance/drift feedback | strategy, publishing, analytics |
| `brand-os` | `agentcy-compass` | `brief.v1` | `voice_pack.v1`, signals, brand context | canonical persona authoring, publishing runtime, analytics |
| `cli-mirofish` | `agentcy-echo` | future `forecast.v1` | future `brief.v1` or scenario inputs | canonical strategy, publishing runtime, analytics |
| `cli-phantom` | `agentcy-loom` | future `run_result.v1` | future `brief.v1` | strategy ownership, voice ownership, analytics |
| `cli-metrics` | `agentcy-pulse` | future `performance.v1` | future `run_result.v1` and lineage references | strategy authoring, publishing runtime |
| `cli-agency` | source material for `agentcy-compass` | no canonical shared artifact | n/a | family root, shared store/plugin/MCP ownership |
| parent family docs | family protocol layer | canonical schemas, lineage rules, example payloads, ownership notes | inputs from repo-local scans | runtime ownership inside product repos |

## First implementation slice

### Selected slice

The first implementation slice is:

`voice_pack.v1 -> brief.v1`

That means:

1. `cli-prsna` becomes the canonical writer for `voice_pack.v1`
2. `brand-os` becomes the canonical writer for `brief.v1`
3. the parent family layer should define the schema/examples/lineage notes that both repos follow
4. implementation tasks should stay mostly one-repo-at-a-time, with only thin family-level schema/docs tasks crossing repo boundaries

### Why this slice won

This is the smallest slice that is both real and compounding:

- `cli-prsna` already has the strongest authoring model for voice constraints
- `brand-os` already has the strongest planning seam for brief emission
- it validates the recap rule of protocol-first integration
- it avoids dragging heavy runtime, forecast, publish, or analytics concerns into the first move
- it keeps the first execution tasks testable and non-monolithic

## Repo-local implications of the slice

### `cli-prsna` / `agentcy-vox`

Expected near-term writer task:
- add a canonical `voice_pack.v1` exporter from `Persona`
- keep payload thin: id, version, summary, traits, voice, constraints, examples
- avoid strategy/publish/performance fields

### `brand-os` / `agentcy-compass`

Expected near-term writer task:
- emit `brief.v1` from the plan pipeline and saved campaign seam
- treat `voice_pack.v1` as an input contract, not as locally authored state
- keep the brief centered on planning outputs, policy/strategy context, and lineage

### Parent family layer

Expected near-term family task:
- publish canonical schema/examples/ownership notes for `voice_pack.v1` and `brief.v1`
- keep repo-local fixtures mirrored from family-owned examples rather than redefining the contracts inside each repo

## Deferral checkpoint

### Deferred now: `cli-mirofish` / `forecast.v1`

Decision:
- defer from the first implementation slice

Reason:
- `cli-mirofish` is heavy, architecturally distinct, and AGPL-licensed
- its outputs are already rich enough to inform a later protocol pass
- the right later move is a thin `forecast.v1` projection over exported run/report artifacts, not deep merging or early schema sprawl

Boundary note:
- keep coupling file/protocol-based
- do not make other repos depend on MiroFish internals as part of the first slice

### Deferred now: `cli-phantom` / `run_result.v1`

Decision:
- defer from the first implementation slice

Reason:
- the runtime already has a clear future seam: internal brief ingestion on the way in, delivery + final run state on the way out
- pulling loom into the first slice would expand scope into execution, review, publish behavior, and extra lineage rules too early

Boundary note:
- later protocol work should focus on imported `brief.v1` compatibility and exported `run_result.v1`, not on broad runtime rewiring

### Deferred now: `cli-metrics` / `performance.v1`

Decision:
- defer from the first implementation slice

Reason:
- `cli-metrics` does not yet exist as a built module
- there is no current writer implementation to narrow or validate
- performance/attribution should be defined only after `run_result.v1` and lineage are real enough to map publish outcomes back to briefs and voices

Boundary note:
- `agentcy-pulse` remains a planned feedback module, but not a prerequisite for the first handoff slice

## Narrow extraction rule for `cli-agency`

`cli-agency` remains source material, not protocol center.

Allowed influence:
- research/strategy field ideas
- prompt/stage concepts that help shape `brief.v1`

Explicitly deferred or left behind:
- `.agency/` store conventions
- plugin surfaces
- MCP surface
- interactive resume state machine
- activation/runtime planning as first-slice canonical protocol

## Implementation gate

From this checkpoint forward:

- family-level schema/examples/ownership artifacts should cite this checkpoint
- repo-local implementation tasks should align to the writer matrix above
- no implementation should claim a shared artifact contract based only on planner prose or repo-local convenience
- if a repo wants to emit or consume a family artifact, that move should map back to this checkpoint and the family-owned schema/examples

## Immediate next-task shape implied by this checkpoint

1. family docs/schema task for canonical `voice_pack.v1` and `brief.v1` examples/lineage
2. `cli-prsna` task for canonical `voice_pack.v1` export
3. `brand-os` task for canonical `brief.v1` emit path
4. thin integration validation between those two artifacts
5. later follow-up checkpoints for `forecast.v1`, `run_result.v1`, and `performance.v1`

## Bottom line

This checkpoint makes the next wave explicit:

- `cli-prsna` writes `voice_pack.v1`
- `brand-os` writes `brief.v1`
- that handoff is the first real slice
- `cli-mirofish`, `cli-phantom`, and `cli-metrics` are recorded as deliberate deferrals
- `cli-agency` informs the strategy layer but does not own the family protocol
