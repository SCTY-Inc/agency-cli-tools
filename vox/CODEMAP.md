# Codemap

Generated: 2026-01-25

## Architecture

CLI tool and Python library for managing AI personas. Core persona lifecycle: create → enrich → test → optimize → chat → learn. Centralized LLM calls via `src/prsna/llm.py`.

## Directory Structure

| Path | Purpose | Key Files |
| --- | --- | --- |
| src/prsna/ | Main package | cli.py, persona.py, llm.py |
| src/prsna/bootstrap.py | Persona generation | bootstrap_from_description, bootstrap_from_person |
| src/prsna/enrichment/ | External data | exa.py |
| src/prsna/optimization/ | DSPy + GEPA | dspy_modules.py, optimize.py |
| src/prsna/eval_cases.py | Structured eval tiers + custom case loading | generate_eval_cases, load_eval_cases |
| src/prsna/eval_store.py | Saved eval-report persistence | save_eval_report, list_eval_reports, latest_eval_report |
| src/prsna/exporters/ | Export formats | __init__.py |
| tests/ | Test suite | test_*.py |
| personas/ | Sample personas | *.yaml |

## Entry Points

| Entry | File | Description |
| --- | --- | --- |
| CLI | src/prsna/cli.py | `persona` command |
| Library | src/prsna/persona.py | Persona class API |

## Data Flow

Persona YAML → load via `Persona.load()` → chat/test/optimize workflows → interaction logs in `~/.prsna/learning/` + optional eval reports in `~/.prsna/evals/` → optional export formats.

## Key Patterns

- **Centralized LLM**: `complete()`, `complete_json()`, `complete_chat()` in `llm.py`.
- **Persona as config**: YAML files stored under `~/.prsna/personas/`.
- **Agent modules**: bootstrap + repair, drift detection, learning, optimization, eval-case generation, eval-report persistence.

## Dependencies (non-obvious)

| Package | Why |
| --- | --- |
| dspy | Consistency testing + optimization |
| litellm | Multi-provider LLM calls |
| exa-py | People search enrichment |
| typer | CLI |
| pydantic | Data models |

## Common Tasks

| Task | Steps |
| --- | --- |
| Create persona | `persona create "description"` |
| Enrich persona | `persona enrich name --query "..."` |
| Test consistency | `persona test name --difficulty stress --save-report` |
| Compare eval drift over time | `persona evals name --compare` |
| Optimize prompt | `persona optimize name` |
| Add export format | Add function in `src/prsna/exporters/__init__.py` and register in `_EXPORTERS` |
