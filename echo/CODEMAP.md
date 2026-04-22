# CODEMAP

Navigation map for the MiroFish codebase. 87 Python files.

## Entry point

- `app/cli.py` — CLI (`agentcy-echo run`, `agentcy-echo runs`). Orchestrates full pipeline via WorkbenchSession.

## Core orchestration (`app/core/`)

- `workbench_session.py` — Session wrapper, composes tools + resources
- `resource_loader.py` — Initializes all persistence stores
- `session_manager.py` — Tracks active project/graph/simulation/report IDs
- `task_manager.py` — Async task state machine (PENDING → RUNNING → COMPLETED/FAILED)

## Pipeline tools (`app/tools/`)

Composable steps called by WorkbenchSession in sequence:

1. `generate_ontology.py` — LLM entity/relationship extraction from documents
2. `build_graph.py` — Ontology → JSON graph
3. `prepare_simulation.py` — Generate agent profiles via LLM
4. `run_simulation.py` — Launch OASIS subprocess, track progress
5. `generate_report.py` — Single-pass report generation (calls `generate_report_fast`)
6. `simulation_support.py` — Shared utilities across tools

## Services (`app/services/`)

Heavy business logic:

- `graph_storage.py` — Abstract GraphStorage + JSON backend (~420 lines)
- `graph_db.py` — Query facade over graph storage
- `graph_builder.py` — Ontology → graph construction pipeline
- `entity_extractor.py` — Structured LLM extraction
- `entity_reader.py` — Entity filtering and enrichment
- `ontology_generator.py` — LLM prompts for extraction
- `oasis_profile_generator.py` — Agent persona generation
- `simulation_config_generator.py` — Simulation config assembly, including taxonomy-driven scenario buckets that seed initial posts and follow-up lanes
- `simulation_manager.py` — Simulation lifecycle state machine
- `simulation_runner.py` — Subprocess spawning, IPC, monitoring, and graph-memory updater lifecycle (~1500 lines); CLI automation now uses a `--no-wait` path so runs can exit cleanly without entering command mode
- `simulation_ipc.py` — File-based IPC with OASIS processes
- `simulation_platforms.py` — Twitter/Reddit data normalization
- `report_agent.py` — Report generation: `generate_report_fast()` (single-pass, default) + legacy ReACT loop (~2550 lines); failure persistence and default-outline helpers now live in the service
- `graph_models.py` — Search/interview result models shared across graph retrieval tools
- `graph_retrieval.py` — Base graph CRUD, summaries, and node/edge access
- `graph_search_tools.py` — Higher-level search helpers (`insight_forge`, `panorama_search`, `quick_search`)
- `graph_interview.py` — Agent interview helpers for report generation
- `graph_tools.py` — Public `GraphToolsService` assembly point over the split graph modules
- `graph_memory_updater.py` — Post-simulation graph updates
- `text_processor.py` — Encoding detection

## Resources (`app/resources/`)

Persistence adapters (thin wrappers over filesystem):

- `projects/` — Project metadata store
- `documents/` — Document file store
- `graph/` — Graph store adapter
- `simulations/` — Simulation state store
- `reports/` — Report store
- `llm/` — LLM provider config

## Utils (`app/utils/`)

- `llm_client.py` — CLI-only LLM client (claude-cli, codex-cli)
- `oasis_llm.py` — CAMEL/OASIS CLI bridge (fakes OpenAI ChatCompletion for simulation engine)
- `file_parser.py` — PDF/text extraction
- `logger.py` — Structured logging

## Artifacts

- `app/run_artifacts.py` — RunStore: immutable run directories with manifest
- `app/run_eval.py` — repo-local completed-run evaluation sidecar builder (`eval/run_eval.v1.json`)
- `app/smoke_mode.py` — deterministic smoke-mode timeline/report builder
- `app/visual_snapshots.py` — SVG generation (swarm, cluster, timeline, platform-split)

## Scripts (`scripts/`)

OASIS simulation runners (spawned as subprocesses by `simulation_runner.py`):

- `run_parallel_simulation.py` — Dual-platform (Twitter + Reddit)
- `run_twitter_simulation.py` — Twitter-only; now emits action logs via the SQLite trace helper
- `run_reddit_simulation.py` — Reddit-only; now emits action logs via the SQLite trace helper
- `action_logger.py` — Per-action recording for the parallel runner
- `action_trace.py` — SQLite trace reader used by the single-platform runners to rebuild action logs

## Config

- `app/config.py` — Environment loading, Config class
- `.env` / `.env.example` — LLM provider config
- `pyproject.toml` — Dependencies, `[project.scripts]` entry point
