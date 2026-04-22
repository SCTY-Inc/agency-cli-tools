# CLAUDE.md — agentcy-vox

CLI tool **and Python library** for managing AI personas. Create, test, optimize, and use personas programmatically. Member of the agentcy monorepo.

## Current surfaces (monorepo)

- Python distribution: `agentcy-vox`
- Python import path: `prsna` (unchanged until explicit refactor)
- installed CLI: `agentcy-vox`
- dispatcher alias: `agentcy vox ...`
- writer contract: `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`

The package and CLI are Agentcy-branded, but canonical protocol lineage still keeps the historical `writer.repo` value for compatibility.

**Core concept:** Personas are the new prompts. As AI gets more capable, consistent behavior becomes the bottleneck.

## Library Usage

```python
from prsna import Persona, bootstrap_from_description, LLMError

# Load and chat
vc = Persona.load("~/.prsna/personas/tech-investor.yaml")
response = vc.chat("Should I raise now?")

# Multi-turn
with vc.conversation() as conv:
    print(conv.send("I have $50k MRR"))
    print(conv.send("Should I raise?"))

# Synthetic user generation (for testing chatbots)
angry = Persona(**bootstrap_from_description("angry customer"))
test_input = angry.as_user("asking about refund policy")
bot_response = my_chatbot(test_input)

# Batch generation
responses = persona.generate(["prompt1", "prompt2", "prompt3"])

# Error handling
try:
    response = persona.chat("Hello")
except LLMError as e:
    print(f"LLM failed: {e}")
```

## Commands

```bash
agentcy-vox create "description"        # AI-bootstrap from description
agentcy-vox create --like "Person"      # Base on real person (Exa)
agentcy-vox init name                   # Empty template
agentcy-vox ls / show / edit / rm       # CRUD
agentcy-vox mix A B --as C              # Compose personas
agentcy-vox enrich name --query "..."   # Add real-world context (Exa)
agentcy-vox test name --difficulty stress --save-report   # structured eval tiers + saved report
agentcy-vox evals name --latest                           # inspect latest saved eval report
agentcy-vox evals name --compare                          # compare latest vs previous eval report
agentcy-vox optimize name                                 # GEPA prompt evolution
agentcy-vox drift name "response"                         # Check single response
agentcy-vox learn name --apply          # Learn from interactions
agentcy-vox critique name --apply       # Self-critique
agentcy-vox chat name                   # Interactive REPL
agentcy-vox ask name "question"         # One-shot
agentcy-vox export name --to FORMAT     # Export (eliza, v2, ollama, hub)
```

## Architecture

```
src/prsna/
├── cli.py              # Typer commands (entry point)
├── persona.py          # Persona class + chat methods
├── llm.py              # Centralized LLM interface
├── clients.py          # Shared API clients (Exa)
├── bootstrap.py        # LLM-powered persona generation + repair pass
├── drift.py            # Consistency monitoring
├── learning.py         # Self-improvement from interactions
├── eval_cases.py       # Generated and custom eval-case loading
├── eval_store.py       # Saved eval-report persistence under ~/.prsna/evals/
├── utils.py            # JSON parsing helpers
├── enrichment/
│   └── exa.py          # Exa people search integration
├── optimization/
│   ├── dspy_modules.py # PersonaChat, PersonaSignature
│   └── optimize.py     # test_persona, optimize_persona
└── exporters/
    └── __init__.py     # eliza, v2, ollama, hub formats
```

## Key Files

| File | Purpose |
|------|---------|
| `persona.py` | Core `Persona` class with `.chat()`, `.stream()`, `.conversation()`, `.as_user()`, `.generate()` |
| `llm.py` | Centralized LLM calls: `complete()`, `complete_json()`, `complete_chat()` with error handling |
| `clients.py` | Shared API clients: `get_exa_client()` singleton |
| `bootstrap.py` | `bootstrap_from_description()`, `bootstrap_from_person()`, `bootstrap_from_role()` with a repair pass before save/export |
| `drift.py` | `detect_drift()`, `monitor_conversation()`, `ConversationDrift` |
| `learning.py` | `log_interaction()`, `analyze_interactions()`, `self_critique()`, `apply_learnings()` |

## Data Storage

```
~/.prsna/
├── personas/           # Persona YAML files
│   └── scientist.yaml
├── learning/           # Interaction logs for learning
│   └── scientist.json
└── evals/              # Saved persona eval reports
    └── scientist/
        └── 20260418T000000000000Z.json
```

## Dependencies

- **typer** — CLI framework
- **dspy** — LLM signatures and modules
- **gepa** — Genetic-Pareto optimization (via DSPy)
- **litellm** — Multi-provider LLM calls
- **exa-py** — People search
- **pydantic** — Data validation
- **rich** — Terminal formatting

## Environment Variables

```bash
OPENAI_API_KEY    # Required for most features
EXA_API_KEY       # Required for enrich, create --like
```

## Development

```bash
uv sync --dev
uv run agentcy-vox --help
uv run pytest
ruff check src/
```

Loop-9 proof work should keep help/version/install examples honest. Historical packaged-install proof may still mention the old `persona` binary, but current operator-facing docs in this repo should use `agentcy-vox` for the CLI and `prsna` for the package/import surface.

## Common Tasks

### Add a new export format

1. Add function in `src/prsna/exporters/__init__.py`:
   ```python
   def export_newformat(persona: Persona) -> str:
       ...
   ```
2. Register in `_EXPORTERS` dict
3. Update CLI help text in `export_persona()`

### Add a new CLI command

1. Add function in `src/prsna/cli.py` with `@app.command()` decorator
2. Use `load_persona()` helper to get persona by name
3. Use `console.status()` for long operations
4. Use `rprint()` with rich markup for output
5. If the command emits durable evaluation state, persist it via `src/prsna/eval_store.py` instead of inventing a second storage path

### Modify persona schema

1. Update `Persona` class in `src/prsna/persona.py`
2. Update `to_prompt()` if new fields affect prompt generation
3. Update bootstrap prompts in `bootstrap.py` if needed
4. Update exporters if new fields should be exported

### Make LLM calls

Always use the centralized `llm.py` module instead of calling litellm directly:

```python
from prsna.llm import complete, complete_json, complete_chat

# Simple completion
response = complete("Hello", model="gpt-4o-mini")

# JSON response with safe parsing
data = complete_json(prompt, default={"error": "failed"})

# Chat with message history
content = complete_chat(messages, model="gpt-4o")
```

Benefits: error handling, logging, timeouts, consistent defaults.

### Add external API client

Add to `src/prsna/clients.py` with lazy initialization:

```python
@lru_cache(maxsize=1)
def get_new_client():
    api_key = os.getenv("NEW_API_KEY")
    if not api_key:
        raise ClientError("NEW_API_KEY required")
    return NewClient(api_key=api_key)
```

## Research References

| Paper | Used For |
|-------|----------|
| [arXiv:2406.20094](https://arxiv.org/abs/2406.20094) | Persona Hub methodology |
| [arXiv:2402.10962](https://arxiv.org/abs/2402.10962) | Drift detection |
| [arXiv:2507.21509](https://arxiv.org/abs/2507.21509) | Persona vectors concept |
| [arXiv:2510.07841](https://arxiv.org/abs/2510.07841) | Self-improvement |
| [arXiv:2407.18416](https://arxiv.org/abs/2407.18416) | PersonaGym evaluation |

## Code Style

- Type hints required
- Use `from __future__ import annotations` for forward refs
- Pydantic models for data classes
- Rich for terminal output
- Keep functions focused; split large modules
