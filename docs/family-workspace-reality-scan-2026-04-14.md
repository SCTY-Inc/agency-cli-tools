# Family workspace reality scan — 2026-04-14

Date: 2026-04-14
Scope: literal workspace state under `/Users/amadad/projects`
Mode: read-only inventory

## Purpose

This document records filesystem truth for the current six-repo Agentcy family as it exists in the workspace today. It does not re-argue the intended architecture. It separates:

- literal workspace reality: directory names, git state, dirty/untracked state, and package/import/bin surfaces
- control-plane narration: the family-module framing recorded in `_agentcy-docs/AGENTCY_RECAP.md`, `_agentcy-docs/AGENTCY_STACK.md`, and related docs

## Filesystem truth vs control-plane narration

Current control-plane docs describe the active family as:

- `agentcy-compass`
- `agentcy-echo`
- `agentcy-lab`
- `agentcy-loom`
- `agentcy-pulse`
- `agentcy-vox`

Literal workspace truth is mixed:

- all six family repo directories do exist under those `agentcy-*` names
- several repos still expose legacy package/import/bin surfaces internally
- supporting surfaces `cli-agency/` and `protocols/` are present in the same workspace but are not part of the six-repo family count for this scan

## Status-label rubric used here

- `clean`: repo exists, no dirty/untracked files, and surface naming is internally coherent enough for this snapshot
- `in-flight`: repo exists but has active local tracked or untracked changes
- `drift-prone`: repo exists, but literal public/package/import/bin surfaces still materially diverge from its directory/module-family name, even if the repo is otherwise usable

## Family repos: literal workspace inventory

| Family repo | Literal path | Git branch / upstream | Ahead / behind | Dirty / untracked summary | Package / import / bin surface observed now | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `agentcy-compass` | `/Users/amadad/projects/agentcy-compass` | `main` tracking `origin/main` | ahead 11 / behind 0 | 3 tracked changes, 3 untracked | Python package `brand-os`; import root `brand_os`; CLI script `brandos` | drift-prone | Directory is renamed to family form, but package/import/bin surfaces remain legacy `brand-*`. Dirty local state is present. |
| `agentcy-echo` | `/Users/amadad/projects/agentcy-echo` | `main` tracking `origin/main` | ahead 9 / behind 0 | 14 tracked changes, 1 untracked | Python package `mirofish-backend`; import root `app`; CLI script `mirofish` | drift-prone | Directory is family-form, but public/code surfaces still reflect MiroFish lineage and generic `app` import root. Active local work is present. |
| `agentcy-lab` | `/Users/amadad/projects/agentcy-lab` | `main` with no upstream configured | n/a | clean working tree | Python package `agentcy-lab`; import root `agentcy_lab`; CLI script `agentcy-lab` | clean | This repo is the most internally aligned with its directory/module name in the current workspace snapshot. |
| `agentcy-loom` | `/Users/amadad/projects/agentcy-loom` | `main` tracking `origin/main` | ahead 9 / behind 0 | 3 tracked changes, 0 untracked | Node package `loom-runtime`; installed bin `loom`; no separate import-root claim captured in package manifest | drift-prone | Directory is family-form, but package surface remains `loom-runtime` and operator bin remains `loom`. Active local edits are present. |
| `agentcy-pulse` | `/Users/amadad/projects/agentcy-pulse` | `main` with no upstream configured | n/a | 3 tracked changes, 3 untracked | Python package `agentcy-pulse`; import root `agentcy_pulse`; CLI script `agentcy-pulse` | in-flight | Family naming is internally aligned, but the repo has active local tracked and untracked changes. |
| `agentcy-vox` | `/Users/amadad/projects/agentcy-vox` | `main` tracking `origin/main` | ahead 6 / behind 0 | 2 tracked changes, 2 untracked | Python package `prsna`; import root `prsna`; CLI script `persona` | drift-prone | Directory is family-form, but package/import/bin surfaces still expose legacy Persona naming. Active local work is present. |

## Supporting/control-plane repos and directories

These are present in the same workspace and matter to the family, but they are not counted as family product modules for this scan.

| Support surface | Literal path | Git branch / upstream | Ahead / behind | Dirty / untracked summary | Surface observed now | Family status | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `cli-agency` | `/Users/amadad/projects/cli-agency` | `main` tracking `origin/main` | ahead 4 / behind 0 | 2 tracked changes, 1 untracked | Python package `agency`; CLI script `agency` | non-family support surface | Legacy/supporting control-plane input repo; current docs treat it as source logic to narrow or re-home, not as one of the six active family repos. |
| `protocols` | `/Users/amadad/projects/protocols` | not a git repo in this workspace snapshot | n/a | not summarized via git because no repo metadata is present at this path | Family schemas, examples, tests, lineage docs, and adapters under a plain workspace directory | non-family support surface | Important control-plane/protocol authority, but not a counted family product repo. In this snapshot it is a directory surface rather than a standalone git repo. |

## Supporting-surface detail

### `cli-agency`

Literal manifest surface:

- package/distribution: `agency`
- CLI: `agency`
- Python requirement: `>=3.12`

Observed role in current control-plane docs:

- supporting source/control-plane input
- not the long-term family root
- not part of the six-repo family inventory

### `protocols`

Literal filesystem contents observed now include:

- canonical schemas such as `voice_pack.v1.schema.json`, `brief.v1.schema.json`, `forecast.v1.schema.json`, `run_result.v1.schema.json`, `performance.v1.schema.json`
- canonical examples under `protocols/examples/`
- family validation tests under `protocols/tests/`
- lineage and adapter docs

Observed role in current control-plane docs:

- parent-level protocol authority
- control-plane input and validation surface
- not a counted family product repo

## Quick readout

### Repos that are literally present and internally aligned enough today

- `agentcy-lab`
- `agentcy-pulse` is naming-aligned at package/import/bin level, but not clean because local work is in progress

### Repos where directory rename is ahead of public/package/import/bin reality

- `agentcy-compass` -> still `brand-os` / `brand_os` / `brandos`
- `agentcy-echo` -> still `mirofish-backend` / `app` / `mirofish`
- `agentcy-loom` -> still `loom-runtime` / `loom`
- `agentcy-vox` -> still `prsna` / `prsna` / `persona`

### Repos with active local work right now

- `agentcy-compass`
- `agentcy-echo`
- `agentcy-loom`
- `agentcy-pulse`
- `agentcy-vox`
- `cli-agency`

### Repos that are clean right now

- `agentcy-lab`

## Bottom line

Literal workspace reality on 2026-04-14 is not a fully normalized six-repo family with matching package/import/bin surfaces. It is a mixed state where:

- the six family directories are present under the `agentcy-*` names
- `agentcy-lab` is the cleanest fully aligned repo in this snapshot
- `agentcy-pulse` is naming-aligned but actively being worked on
- `agentcy-compass`, `agentcy-echo`, `agentcy-loom`, and `agentcy-vox` still show meaningful directory-versus-surface drift
- `cli-agency` and `protocols` remain important support/control-plane surfaces, but should be narrated separately from the six family repos
