# CLAUDE.md

## What this is

MiroFish — CLI-only swarm intelligence prediction engine. Feed documents + requirement, get a simulated social media prediction with report and visual snapshots.

Fork of [666ghj/MiroFish](https://github.com/666ghj/MiroFish), fully translated to English.

## Commands

```bash
uv sync                                    # base CLI/help/import install
uv sync --extra simulation                 # full simulation runtime
agentcy echo run --files f.pdf --requirement "..." --json   # run pipeline
agentcy echo runs list --json              # list runs
agentcy echo runs status <id> --json       # check status
agentcy echo runs export <id> --json       # export artifacts
# or directly:
agentcy-echo run --files f.pdf --requirement "..." --json
uv run python -m pytest -x                 # tests
```

## Layout

```
app/
  cli.py              Entry point (console_scripts: agentcy-echo)
  config.py            Env + validation (.env loaded automatically)
  cli_display.py       Rich visual pipeline display
  run_artifacts.py     Immutable run storage (RunStore)
  visual_snapshots.py  SVG generation (no browser needed)
  core/                WorkbenchSession, TaskManager, ResourceLoader
  tools/               Composable pipeline steps (ontology, graph, prepare, run, report)
  services/            Business logic (graph_storage, simulation_runner, report_agent, llm)
  resources/           Persistence adapters (projects, documents, graph, simulations, reports)
  models/              Data models
  utils/
    llm_client.py      CLI-only LLM client (claude-cli, codex-cli)
    logger.py          Structured logging
scripts/               OASIS simulation runner scripts (subprocess)
tests/                 pytest
uploads/               Runtime data (gitignored)
data/                  Graph JSON storage (gitignored)
```

## Architecture

CLI (`cli.py`) orchestrates via `WorkbenchSession` which composes tools:
1. `GenerateOntologyTool` — LLM entity/relationship extraction
2. `BuildGraphTool` — ontology → JSON graph
3. `PrepareSimulationTool` — agent profile generation
4. `RunSimulationTool` — OASIS subprocess (Twitter + Reddit)
5. `GenerateReportTool` — single-pass report generation (ReACT loop available but not default)

Each run produces an immutable directory under `uploads/runs/<run_id>/` with manifest, frozen inputs, graph, simulation data, report, SVG visuals, and logs.

## Config

`.env` file at repo root. Key vars:
- `LLM_PROVIDER` — `claude-cli` (default) or `codex-cli`

## Gotchas
- Simulation runs OASIS in a subprocess via `scripts/`. The scripts add the project root to `sys.path` to import from `app.utils.oasis_llm`.
- `camel-oasis==0.2.5` and `camel-ai==0.2.78` stay pinned in the optional `simulation` extra — upgrading either can break the simulation pipeline.
- `report_agent.py` has two generation paths: `generate_report_fast()` (single-pass, default) and `generate_report()` (ReACT loop, legacy). The ReACT path is 2500+ lines and much slower.
- CLI display (`cli_display.py`) uses `rich.Live` on stderr. Suppresses service-layer logs to WARNING during display. `--json` mode bypasses rich entirely.
- Never trash `uploads/runs/` — run artifacts are the product. Each run is immutable and self-contained.
