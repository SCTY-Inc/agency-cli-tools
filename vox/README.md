# agentcy-vox

Part of the agentcy monorepo — invoke via `agentcy vox` or `agentcy-vox`.

Manage, compose, test, and evolve AI personas.

## Current surfaces (monorepo)

- repo: `agentcy`
- Python distribution/package: `agentcy-vox`
- Python import path: `prsna` (unchanged until explicit refactor)
- installed CLI: `agentcy-vox`
- dispatcher alias: `agentcy vox ...`
- writer contract: `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`

The package and CLI are Agentcy-branded, but canonical protocol lineage still keeps the historical `writer.repo` value for compatibility.

## Install

```bash
uv pip install -e .
```

## What It Does

**Turn AI personas from throwaway prompt strings into managed, testable, self-improving assets.**

| Without prsna | With prsna |
|---------------|------------|
| Prompts scattered across files | `agentcy-vox ls` — versioned library |
| Made-up traits | Real person data via Exa |
| "Seems right?" | Consistency score: 73% |
| Manual prompt tweaking | GEPA auto-optimizes |
| Persona degrades over chat | Drift detection + refresh |
| Static forever | Self-learning from interactions |

## Quick Start

### CLI

```bash
# Bootstrap a persona with AI
agentcy-vox create "skeptical investigative journalist"

# Or base on a real person
agentcy-vox create --like "Marc Andreessen" "tech investor"

# Chat with it
agentcy-vox chat journalist

# Check consistency
agentcy-vox test journalist

# Let it learn from interactions
agentcy-vox learn journalist --apply
```

### Library

```python
from prsna import Persona, bootstrap_from_description, LLMError

# Load and chat
vc = Persona.load("~/.prsna/personas/tech-investor.yaml")
response = vc.chat("Should I raise now?")

# Multi-turn conversation
with vc.conversation() as conv:
    print(conv.send("I have $50k MRR"))
    print(conv.send("Should I raise?"))

# Streaming
for chunk in vc.stream("Tell me about market timing"):
    print(chunk, end="", flush=True)

# Synthetic user generation (for testing chatbots)
angry = Persona(**bootstrap_from_description("frustrated customer"))
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
# GLOBAL FLAGS
agentcy-vox --version                   # Show version
agentcy-vox --json ls                   # Output as JSON (for scripting)
agentcy-vox --quiet ls                  # Minimal output (names only)

# CREATE
agentcy-vox init scientist              # Empty template (manual edit)
agentcy-vox create "description"        # AI-generated from description
agentcy-vox create --like "Person"      # Based on real person (Exa)
agentcy-vox create --role "Job Title"   # Based on job role

# MANAGE
agentcy-vox ls                          # List all personas
agentcy-vox show scientist              # Show details
agentcy-vox edit scientist              # Open in $EDITOR
agentcy-vox rm scientist                # Delete

# COMPOSE
agentcy-vox mix scientist comedian --as science-comedian

# ENRICH
agentcy-vox enrich scientist --query "MIT AI researcher"

# TEST & OPTIMIZE
agentcy-vox test scientist --samples 10      # DSPy consistency check
agentcy-vox optimize scientist --iterations 50  # GEPA prompt evolution
agentcy-vox drift scientist "response text"  # Check single response

# LEARN & IMPROVE
agentcy-vox learn scientist --apply     # Learn from logged interactions
agentcy-vox critique scientist --apply  # Self-critique and improve

# USE
agentcy-vox chat scientist              # Interactive REPL
agentcy-vox ask scientist "question"    # One-shot
echo "question" | agentcy-vox ask scientist -  # Pipe from stdin

# EXPORT
agentcy-vox export scientist --to voice-pack.v1  # Canonical Agentcy voice_pack.v1 JSON
agentcy-vox export scientist --to eliza       # PersonaKit/Eliza
agentcy-vox export scientist --to v2          # Character Card V2
agentcy-vox export scientist --to ollama      # Ollama Modelfile
agentcy-vox export scientist --to hub         # PERSONA HUB format
```

The canonical family protocol for downstream Agentcy handoffs lives in `../protocols/voice_pack.v1.schema.json` and `../protocols/examples/voice_pack.v1.*.json`. `agentcy-vox` owns writing that artifact; strategy, briefs, and publishing stay in sibling repos.


## Persona Format

```yaml
name: scientist
version: 1
description: A curious research scientist who values evidence

traits:
  - curious
  - methodical
  - precise
  - humble about uncertainty

voice:
  tone: academic
  vocabulary: technical
  patterns:
    - "The evidence suggests..."
    - "It's worth noting that..."

boundaries:
  - Never claim certainty without data
  - Acknowledge limitations

examples:
  - user: "Is this true?"
    assistant: "The current evidence suggests..."

dynamic:
  source: exa
  query: "Dr. Jane Smith MIT"
  refresh: weekly

providers:
  default: gpt-4o-mini
```

## How It Works

```
┌──────────────────────────────────────────────────────────────────┐
│                         LIFECYCLE                                │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CREATE ──▶ ENRICH ──▶ TEST ──▶ OPTIMIZE ──▶ USE ──▶ LEARN      │
│     │         │         │          │         │         │        │
│     ▼         ▼         ▼          ▼         ▼         ▼        │
│  Bootstrap  Exa      DSPy       GEPA     Chat/Ask  Analyze      │
│  from desc  people   fidelity   evolve   with      interactions │
│  or person  search   scoring    prompt   drift     & improve    │
│                                          detect                  │
│                                                                  │
│                    ◀──── CONTINUOUS IMPROVEMENT ────▶           │
└──────────────────────────────────────────────────────────────────┘
```

## Research Foundation

Built on techniques from recent persona research:

| Paper | Technique Used |
|-------|----------------|
| [Scaling Synthetic Data with 1B Personas](https://arxiv.org/abs/2406.20094) | Persona Hub integration |
| [Measuring Persona Drift](https://arxiv.org/abs/2402.10962) | Drift detection |
| [Persona Vectors](https://arxiv.org/abs/2507.21509) | Consistency monitoring |
| [Self-Improving Agents](https://arxiv.org/abs/2510.07841) | Learning from interactions |
| [PersonaGym](https://arxiv.org/abs/2407.18416) | Fidelity evaluation |
| [RoleLLM](https://arxiv.org/abs/2310.00746) | Role-conditioned tuning |

## Stack

- **typer** — CLI framework
- **dspy** — LLM programming & signatures
- **gepa** — Genetic-Pareto prompt optimization
- **litellm** — Multi-provider LLM calls (via centralized `llm.py`)
- **exa-py** — People search enrichment
- **pydantic** — Data validation
- **rich** — Terminal formatting

## Environment Variables

```bash
OPENAI_API_KEY=sk-...      # Required for most features
EXA_API_KEY=...            # Required for enrich, create --like
```

## Development

```bash
cd ~/projects/agentcy/vox
uv sync --dev
uv run agentcy-vox --help
uv run pytest
ruff check src/
```

## Why prsna?

**Personas are the new prompts.** As AI systems get more capable, the bottleneck shifts from "can it do X?" to "does it behave consistently as Y?"

prsna treats personas as first-class software artifacts:
- **Versioned** — Track changes, roll back
- **Testable** — Measure consistency, catch regressions
- **Composable** — Mix traits, extend bases
- **Evolvable** — Learn from use, self-improve
- **Portable** — Export to any format/platform, including canonical `voice_pack.v1`

---

**prsna** = Git + npm + CI for AI personas
