# CODEMAP

Navigation map for the MiroFish codebase. 62 Python files.

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
- `simulation_config_generator.py` — Simulation config assembly
- `simulation_manager.py` — Simulation lifecycle state machine
- `simulation_runner.py` — Subprocess spawning, IPC, monitoring (~1480 lines)
- `simulation_ipc.py` — File-based IPC with OASIS processes
- `simulation_platforms.py` — Twitter/Reddit data normalization
- `report_agent.py` — Report generation: `generate_report_fast()` (single-pass, default) + legacy ReACT loop (~2800 lines, largest file)
- `graph_tools.py` — Search, interview, analysis helpers (~2100 lines)
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
- `app/visual_snapshots.py` — SVG generation (swarm, cluster, timeline, platform-split)

## Scripts (`scripts/`)

OASIS simulation runners (spawned as subprocesses by `simulation_runner.py`):

- `run_parallel_simulation.py` — Dual-platform (Twitter + Reddit)
- `run_twitter_simulation.py` — Twitter-only
- `run_reddit_simulation.py` — Reddit-only
- `action_logger.py` — Per-action recording during simulation

## Config

- `app/config.py` — Environment loading, Config class
- `.env` / `.env.example` — LLM provider config
- `pyproject.toml` — Dependencies, `[project.scripts]` entry point
