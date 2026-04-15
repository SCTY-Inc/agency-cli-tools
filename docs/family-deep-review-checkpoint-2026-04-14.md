# Family deep-review checkpoint — 2026-04-14

Date: 2026-04-14
Scope: bounded family synthesis after the workspace scan, naming/writer/protocol drift audit, and repo-specific deep reviews
Mode: control-plane checkpoint only

## Purpose

This checkpoint publishes the smallest useful family-wide synthesis from the 2026-04-14 review wave. It does not reopen rename execution, broad repo rewiring, or artifact-owner changes.

It consolidates four things:

1. the current family set
2. the supporting/control-plane surfaces that should be narrated separately
3. the real drift profile now visible across the family
4. the next smallest queue of high-value follow-ups

## Current family vs supporting/control-plane surfaces

## Current six-repo family

Treat these as the current Agentcy family repos:

- `agentcy-compass`
- `agentcy-echo`
- `agentcy-lab`
- `agentcy-loom`
- `agentcy-pulse`
- `agentcy-vox`

These are the family modules under active review and should be counted as the family set for current control-plane narration.

## Supporting/control-plane surfaces

Treat these separately from the six-repo family:

- `cli-agency`
- `protocols`

### `cli-agency`

`cli-agency` is a supporting source-material/control-plane input repo. It is still useful for narrowed research/strategy concepts, but it is not a current family product module, not the family root, and not a canonical artifact writer.

### `protocols`

`protocols` is a supporting control-plane authority surface, not a family product repo. It owns canonical schemas, examples, lineage rules, family tests, and the thin adapters that lock writer contracts and handoffs.

## Review inputs merged into this checkpoint

This checkpoint synthesizes:

- `_agentcy-docs/family-workspace-reality-scan-2026-04-14.md`
- `_agentcy-docs/family-naming-writer-protocol-drift-2026-04-14.md`
- `_agentcy-docs/agentcy-compass-boundary-drift-review-2026-04-14.md`
- `_agentcy-docs/agentcy-echo-compatibility-drift-review-2026-04-14.md`
- `_agentcy-docs/agentcy-lab-reality-review-2026-04-14.md`
- `_agentcy-docs/agentcy-loom-runtime-drift-review-2026-04-14.md`
- `_agentcy-docs/agentcy-pulse-loop-12-reality-review-2026-04-14.md`
- `_agentcy-docs/agentcy-vox-surface-drift-review-2026-04-14.md`

## Executive summary

The family is currently in a mixed-but-bounded state:

- all six family repos exist on disk under `agentcy-*` directory names
- the family protocol layer still intentionally preserves mixed writer contracts for the five canonical artifacts
- four repos still expose meaningful legacy package/import/bin compatibility surfaces
- one repo (`agentcy-pulse`) is already family-aligned at package/import/CLI level but still narrated through a historical writer-repo contract
- one repo (`agentcy-lab`) is clean, aligned, and scan-sufficient
- the sharpest current confusion is not artifact ownership; it is the gap between current repo-directory truth and older present-tense control-plane narration

## What is intentional vs accidental drift

## Intentional drift that should stay classified as contract, not defect

The strongest intentional mixed surface in the family is the writer contract:

- `voice_pack.v1` -> `{ repo: "cli-prsna", module: "agentcy-vox" }`
- `brief.v1` -> `{ repo: "brand-os", module: "agentcy-compass" }`
- `forecast.v1` -> `{ repo: "cli-mirofish", module: "agentcy-echo" }`
- `run_result.v1` -> `{ repo: "cli-phantom", module: "agentcy-loom" }`
- `performance.v1` -> `{ repo: "cli-metrics", module: "agentcy-pulse" }`

This remains a deliberate family protocol contract locked by `protocols/lineage-rules.md`, protocol examples, and family validation tests. By itself, this should not be narrated as accidental drift.

## Accidental or stale drift that is real right now

The strongest accidental/stale drift classes are:

1. **family-doc narration drift**
   - control-plane docs still often speak in active present tense through `cli-prsna`, `brand-os`, `cli-mirofish`, `cli-phantom`, and `cli-metrics`
   - literal workspace repo directories are already `agentcy-*`

2. **repo-surface drift**
   - `agentcy-compass` still ships `brand-os` / `brand_os` / `brandos`
   - `agentcy-echo` still ships `mirofish-backend` / `app` / `mirofish`
   - `agentcy-loom` still ships `loom-runtime` / `loom`
   - `agentcy-vox` still ships `prsna` / `prsna` / `persona`

3. **boundary drift**
   - strongest in `agentcy-compass`, where repo scope still exceeds the future strategy/policy/briefing boundary

4. **path-reference drift in family validation/docs**
   - at least one family protocol test path still referenced `brand-os/...` after the repo-directory rename to `agentcy-compass/...`

## Uncommitted local-repo reality

The 2026-04-14 review wave confirmed that local repo reality is still important context. The family is not operating from six uniformly clean repos.

### Clean now

- `agentcy-lab`

### In-flight or dirty now

- `agentcy-compass`
- `agentcy-echo`
- `agentcy-loom`
- `agentcy-pulse`
- `agentcy-vox`
- supporting repo `cli-agency`

### Interpretation

The meaningful family readout is not “everything is rename-ready.” It is:

- the repo-directory rename wave has landed
- several repos are still actively being narrowed, documented, or compatibility-proofed
- current checkpoint language must distinguish dirty local repo truth from locked protocol truth

## Family classification by repo

| Repo | Family role now | Repo/package/bin alignment | Dirty-state reality | Main risk class | Checkpoint call |
| --- | --- | --- | --- | --- | --- |
| `agentcy-compass` | strategy / policy / brief layer | repo renamed, package/import/bin still `brand-*` | in-flight | boundary drift first, naming drift second | highest family boundary-risk hotspot |
| `agentcy-echo` | foresight / forecast layer | repo renamed, package/import/bin still MiroFish-shaped | in-flight | compatibility + attribution + dependency boundary | preserve compatibility and attribution; do not widen |
| `agentcy-lab` | shared eval/autoresearch plane | aligned | clean | low | scan-sufficient, no immediate follow-up |
| `agentcy-loom` | execution / publish runtime | repo renamed, package/bin still `loom-runtime` / `loom` | in-flight | docs/path narration drift around otherwise coherent Node runtime surfaces | small docs-only follow-up is enough |
| `agentcy-pulse` | analytics / attribution / feedback layer | aligned as `agentcy-pulse` / `agentcy_pulse` / `agentcy-pulse` | in-flight | family-doc narration drift, not repo-surface drift | distinguish live repo reality from preserved writer history |
| `agentcy-vox` | voice/persona/drift layer | repo renamed, package/import/bin still `prsna` / `persona` | in-flight | family-doc narration drift around intentional compatibility surfaces | keep runtime surfaces stable; clarify control-plane narration |

## Boundary-risk hotspots

## 1. `agentcy-compass` is the highest boundary-risk hotspot

Why:

- it is not just a naming mismatch
- its repo still exposes persona, produce, eval, publish, queue, monitor, and server/API surfaces beyond a narrow strategy/policy/briefing role
- `cli-agency` overlap remains a conceptual gravity source if not explicitly classified as support-only

Checkpoint call:
- treat `agentcy-compass` as the main family boundary hotspot
- prefer scorecards and scope-clarification docs over implementation rewiring

## 2. `agentcy-echo` is the highest compatibility/attribution hotspot

Why:

- current public surfaces remain `mirofish-backend`, `app`, and `mirofish`
- explicit MiroFish fork lineage and AGPL-aware attribution must stay visible
- optional simulation/runtime proof remains bounded by upstream dependency support
- one parent-level family verification surface still showed renamed-path narration drift

Checkpoint call:
- preserve current writer contract and attribution posture
- treat dependency/install boundary plus control-plane narration as the next blockers, not ownership changes

## 3. `agentcy-vox` and `agentcy-pulse` are mainly narration hotspots

### `agentcy-vox`

The repo-local compatibility story is coherent:

- package/import remain `prsna`
- CLI remains `persona`
- writer stays `cli-prsna` / `agentcy-vox`

The main confusion is family-level narration around what changed at the repo-directory layer versus what did not change in public surfaces.

### `agentcy-pulse`

The repo-local public surface is already aligned:

- package `agentcy-pulse`
- import `agentcy_pulse`
- CLI `agentcy-pulse`

The main mismatch is family docs still narrating the live repo through `cli-metrics` even though that is now mostly preserved writer-history, not repo-surface truth.

## 4. `agentcy-loom` is mostly a docs/path hotspot

The Node runtime is coherent enough for its bounded proof surface:

- package `loom-runtime`
- installed bin `loom`
- source CLI `runtime/src/cli.ts`
- packaged shim `runtime/bin/loom.js`

The drift is mostly historical path narration in repo-local proof docs, not a broken runtime contract.

## Scan-sufficient / no-immediate-follow-up repo

## `agentcy-lab`

`agentcy-lab` is the current repo with the strongest internal alignment:

- clean git state
- aligned repo/package/import/CLI naming
- bounded CLI claim
- bounded test surface
- no family protocol writer contract that needs normalization today

Checkpoint call:
- scan-level coverage is sufficient
- no immediate bounded follow-up is needed

## Next smallest high-value queue

The queue below is intentionally narrow. It prefers repo-local docs/spec clarifications or parent control-plane fixes over broad code changes.

## Queue A — highest-value family/control-plane tasks

1. **[family] Normalize present-tense repo-directory narration across control-plane docs**
   - goal: make current docs consistently say the live repo directories are `agentcy-*`
   - preserve mixed writer contracts in protocol artifacts
   - especially clarify `agentcy-pulse`, `agentcy-vox`, `agentcy-loom`, `agentcy-echo`, and `agentcy-compass`

2. **[family] Fix stale renamed-path references in parent-level tests/docs**
   - goal: remove path assumptions like `brand-os/...` where the live repo path is now `agentcy-compass/...`
   - keep writer contracts untouched
   - this is the smallest family verification-hardening task surfaced by the `agentcy-echo` review

3. **[family] Publish one support-surface authority note for `cli-agency` and `protocols`**
   - goal: make it explicit in one place that `cli-agency` is source material only and `protocols` is parent protocol authority, not a seventh product repo
   - prevent future review waves from re-centering `cli-agency`

## Queue B — highest-value repo-local follow-ups

4. **[brand-os] refresh a boundary scorecard / CLI-scope map in `agentcy-compass`**
   - classify current command groups and top-level source areas as:
     - compass-core
     - over-boundary but tolerated for now
     - likely future handoff/reference-only
   - keep command behavior unchanged

5. **[cli-phantom] refresh `agentcy-loom` packaged-help proof wording**
   - distinguish clearly between:
     - current literal repo directory `agentcy-loom/`
     - preserved writer repo `cli-phantom`
     - live package/bin surfaces `loom-runtime` and `loom`

6. **[cli-mirofish] keep `agentcy-echo` dependency/install proof bounded**
   - if further repo-local work is needed, focus only on the optional simulation runtime proof boundary
   - do not widen into import rewrites or rename execution

7. **[cli-prsna] no code-surface rename task yet; only clarify family-level narration**
   - `agentcy-vox` runtime/package/import/CLI surfaces are coherent under current compatibility policy
   - the next smallest task is doc/control-plane clarification, not a runtime rename pass

8. **[cli-metrics] record live `agentcy-pulse/` repo reality explicitly in loop-12 family docs**
   - keep `performance.v1.writer.repo = "cli-metrics"`
   - do not widen into analytics scope or ownership rewrites

## Explicit non-queue items

Do not promote any of these from this checkpoint alone:

- literal repo rename normalization across writer contracts
- umbrella CLI work
- MCP-first integration
- import-path rewrites
- broad runtime unification
- monolith merges
- package renames for `agentcy-vox`, `agentcy-compass`, `agentcy-echo`, or `agentcy-loom`
- broad analytics expansion in `agentcy-pulse`
- a canonical lab-owned protocol artifact for `agentcy-lab`

## Checkpoint bottom line

The bounded 2026-04-14 deep-review wave shows a family that is more coherent than the old docs alone suggest, but less normalized than the repo-directory rename might imply.

The practical family truth is:

- the current family is exactly six repos: `agentcy-compass`, `agentcy-echo`, `agentcy-lab`, `agentcy-loom`, `agentcy-pulse`, and `agentcy-vox`
- `cli-agency` and `protocols` matter, but as supporting/control-plane surfaces, not extra family modules
- mixed writer contracts are still intentionally locked and should not be confused with accidental drift
- the highest real hotspot is `agentcy-compass` boundary breadth
- the cleanest repo is `agentcy-lab`
- the highest-value next work is mostly doc/protocol-local clarification and very small repo-local scope maps, not broad implementation rewiring
