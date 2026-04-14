# cli-mirofish forecast.v1 deferral scorecard

Date: 2026-04-12
Scope: documentation-only breadth scan for future `agentcy-echo` / `forecast.v1`

## Why this pass exists

`cli-mirofish` already emits rich run, simulation, and report artifacts, but the current family plan keeps the first implementation slice smaller: `voice_pack.v1 -> brief.v1` first, then later pressure-test how `cli-mirofish` should map into `forecast.v1`.

This note inventories what exists now so later protocol work can reuse real outputs instead of inventing a schema in the abstract.

## Current output surfaces

### 1. Top-level CLI surfaces

Current commands:

```bash
mirofish run --files <files...> --requirement "..." --json
mirofish runs list --json
mirofish runs status <run_id> --json
mirofish runs export <run_id> --json
```

Observed contract:
- `run` creates one immutable run directory under `uploads/runs/<run_id>/`
- `runs list` returns stored run manifests, refreshed against live task/simulation/report state
- `runs status` returns one refreshed manifest
- `runs export` resolves artifact names to concrete filesystem paths

### 2. Run manifest

Primary file:
- `uploads/runs/<run_id>/manifest.json`

Current identifiers captured in the manifest:
- `run_id`
- `project_id`
- `graph_id`
- `simulation_id`
- `report_id`
- `graph_build_task_id`
- `prepare_task_id`
- `report_task_id`

Current lifecycle/status values seen in code:
- `created`
- `graph_building`
- `graph_ready`
- `simulation_preparing`
- `simulation_ready`
- `simulation_running`
- `simulation_completed`
- `report_generating`
- `completed`
- `failed`

Current timestamps / progress fields:
- `created_at`
- `updated_at`
- `task_progress`
- `task_message`
- `error`

### 3. Immutable run artifact set

Documented in `README.md` and written by `app/cli.py::_collect_run_outputs()` plus `app/run_artifacts.py`.

Current artifact inventory:

#### Inputs
- `input/requirement.txt`
- `input/source_files/`
- `input/ontology.json`
- `input/analysis_summary.txt`
- `input/simulation_config.json`
- `input/reddit_profiles.json`
- `input/twitter_profiles.csv`

#### Graph outputs
- `graph/graph.json`
- `graph/graph_summary.json`

#### Simulation outputs
- `simulation/timeline.json`
- `simulation/top_agents.json`
- `simulation/actions.jsonl`
- `simulation/config.json`
- `simulation/reddit_profiles.json`
- `simulation/twitter_profiles.csv`
- `logs/simulation.log`

#### Report outputs
- `report/meta.json`
- `report/report.md`
- `report/summary.json`

#### Visual outputs
- `visuals/swarm-overview.svg`
- `visuals/cluster-map.svg`
- `visuals/timeline.svg`
- `visuals/platform-split.svg`

## Current timeline and activity shapes

### Simulation timeline

Primary file:
- `uploads/runs/<run_id>/simulation/timeline.json`

Current round summary fields:
- `round_num`
- `twitter_actions`
- `reddit_actions`
- `total_actions`
- `active_agents_count`
- `active_agents`
- `action_types`
- `first_action_time`
- `last_action_time`

Related live runtime state from `uploads/simulations/<simulation_id>/run_state.json`:
- `runner_status`
- `current_round`
- `total_rounds`
- `simulated_hours`
- `total_simulation_hours`
- `progress_percent`
- per-platform round/hour counters
- per-platform completion booleans
- per-platform action counts
- `started_at`
- `updated_at`
- `completed_at`
- `recent_actions`

### Agent/action detail

Primary files:
- `uploads/runs/<run_id>/simulation/actions.jsonl`
- `uploads/runs/<run_id>/simulation/top_agents.json`

Action-level fields come from `AgentAction` in `app/services/simulation_runner.py`:
- `round_num`
- `timestamp`
- `platform`
- `agent_id`
- `agent_name`
- `action_type`
- `action_args`
- `result`
- `success`

Top-agent summary fields currently exposed:
- `agent_id`
- `agent_name`
- `total_actions`
- `twitter_actions`
- `reddit_actions`
- `action_types`
- `first_action_time`
- `last_action_time`

## Current report shape

Primary files:
- `uploads/reports/<report_id>/meta.json`
- `uploads/reports/<report_id>/full_report.md`
- copied into run bundle as:
  - `uploads/runs/<run_id>/report/meta.json`
  - `uploads/runs/<run_id>/report/report.md`
  - `uploads/runs/<run_id>/report/summary.json`

Current report object fields from `Report` in `app/services/report_agent.py`:
- `report_id`
- `simulation_id`
- `graph_id`
- `simulation_requirement`
- `status`
- `outline`
- `markdown_content`
- `created_at`
- `completed_at`
- `error`

Current outline shape:
- `title`
- `summary`
- `sections[]`
  - `title`
  - `content`

Supporting report-workbench files also exist under `uploads/reports/<report_id>/`:
- `outline.json`
- `progress.json`
- `section_XX.md`
- `agent_log.jsonl`
- `console_log.txt`

These are useful for diagnostics and authoring provenance, but they are not yet normalized into a stable family-level artifact contract.

## Example ID lineage observed in a real run

From the sample run already present in the repo:

- `run_id`: `run_6fd9fdc872a1`
- `project_id`: `proj_5082a06a3af7`
- `graph_id`: `mirofish_2aa457dae7c64a37`
- `simulation_id`: `sim_ef82695e9d60`
- `report_id`: `report_425a1b14de23`
- `graph_build_task_id`: `81dc7eff-8c44-48fb-9819-5e597a8f6e98`
- `prepare_task_id`: `426ecbf6-c1d0-4fff-a5a1-2b066d3d4970`
- `report_task_id`: `a87f279c-662d-4225-a66c-3666fdfb2bb7`

This is enough to see a likely future lineage spine:

`run_id -> project_id -> graph_id -> simulation_id -> report_id`

But that lineage is still MiroFish-local rather than family-canonical.

## How current outputs could later map to forecast.v1

### Best candidate sources

A future `forecast.v1` likely should draw from these existing sources rather than from raw internal stores:

- `report/meta.json`
  - narrative forecast
  - scenario framing
  - completed timestamps
- `report/summary.json`
  - compact machine-facing summary
  - useful IDs and aggregate counts
- `simulation/timeline.json`
  - temporal structure
  - round-by-round activity
- `simulation/top_agents.json`
  - most active actors
- `simulation/actions.jsonl`
  - full trace when deeper provenance is needed
- `manifest.json`
  - lineage and artifact pointers

### Likely future forecast.v1 fields

Not a schema proposal yet, but the repo strongly suggests these future categories:
- lineage IDs: `forecast_id`, `run_id`, maybe `scenario_id`, `brief_id`
- provenance: source docs, graph/simulation/report references
- time horizon: derived from `simulation_requirement` plus simulation config
- forecast summary: concise machine-readable prediction
- narrative/body: current markdown report content or normalized section blocks
- actor/activity summary: top agents, platform split, total actions
- timeline summary: rounds, major spikes, first/last action windows
- confidence / caveats: not explicitly modeled yet, so would need later schema work

## Why forecast.v1 is deferred from the first slice

### 1. First slice should stay small

The current family checkpoint says the first real implementation slice should remain:

`voice_pack.v1 -> brief.v1`

Pulling `forecast.v1` into that first slice would expand scope into:
- scenario simulation
- heavy report generation
- extra lineage decisions
- additional protocol ownership questions

That violates the current protocol-first, bounded-depth plan.

### 2. cli-mirofish is heavy and architecturally distinct

Per `AGENTCY_RECAP.md`, `cli-mirofish` is:
- a real foresight/simulation module
- heavy
- separate architecture
- better treated with loose coupling than deep merging

The repo confirms that:
- simulation runtime is OASIS subprocess-driven
- report generation is large and bespoke
- outputs are richer than the minimal first shared contracts need

### 3. Current outputs are useful but not yet family-stable

Today the repo exposes several layers at once:
- project metadata
- graph state
- simulation prep state
- live run state
- report artifacts
- copied run-bundle artifacts

That is valuable, but it means `forecast.v1` should be defined after the family is ready to choose:
- canonical forecast owner fields
- which internal IDs become cross-family lineage IDs
- which report details are product surface vs debug surface

### 4. forecast.v1 should not become a backdoor monolith

If defined too early, `forecast.v1` could accidentally absorb:
- graph internals
- simulation internals
- report-workbench logs
- repo-specific storage assumptions

The better move is to defer until a thin family protocol can be extracted from real usage.

## Loose-coupling and AGPL constraints

### Loose-coupling guidance

`cli-mirofish` should integrate by file/protocol handoff, not by deep runtime embedding.

Recommended boundary for later work:
- read exported run/report artifacts
- define a thin `forecast.v1` projection over those artifacts
- avoid making other family repos depend directly on MiroFish internals, OASIS state files, or report-agent implementation details

### AGPL implications

The repo is explicitly `AGPL-3.0` licensed.

Practical implication for the family plan:
- keep `agentcy-echo` loosely coupled as its own module
- prefer artifact exchange over code copy/paste into non-echo repos
- avoid early deep merges that blur license boundaries or force unnecessary architectural entanglement

This aligns with the recap's recommendation to treat MiroFish as a separate, loosely coupled foresight layer.

## Likely files for later forecast.v1 follow-up

Highest-value files to revisit later:
- `app/cli.py`
- `app/run_artifacts.py`
- `app/services/simulation_runner.py`
- `app/services/simulation_manager.py`
- `app/services/report_agent.py`
- `app/visual_snapshots.py`
- `tests/test_cli_artifacts_and_visuals.py`
- `README.md`
- sample runtime data under `uploads/runs/`, `uploads/simulations/`, and `uploads/reports/`

## Verification commands for this documentation pass

Read-only repo scan:

```bash
cd cli-mirofish
find docs -maxdepth 2 -type f | sort
rg -n "run_id|report_id|simulation_id|timeline|artifact|forecast|report" app tests README.md CODEMAP.md
```

Artifact verification:

```bash
cd cli-mirofish
mirofish runs list --json
mirofish runs status <run_id> --json
mirofish runs export <run_id> --json
```

Test verification used in this pass:

```bash
cd cli-mirofish
uv run python -m pytest tests/test_cli_artifacts_and_visuals.py -q
```

## Bottom line

`cli-mirofish` already produces enough concrete run, simulation, and report outputs to support a later `forecast.v1` contract. But the right near-term move is deferral, not implementation:
- keep the first family slice focused on `voice_pack.v1 -> brief.v1`
- preserve `cli-mirofish` as a loosely coupled AGPL foresight module
- return later to project a thin, canonical `forecast.v1` from the existing artifact bundle
