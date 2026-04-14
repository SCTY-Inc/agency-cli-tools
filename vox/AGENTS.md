# Agent Architecture

How prsna's intelligent features work under the hood.

## Overview

prsna uses LLMs as agents for several tasks:

1. **Bootstrapping** — Generate personas from descriptions
2. **Enrichment** — Synthesize personas from real-world data
3. **Testing** — Evaluate persona consistency
4. **Optimization** — Evolve prompts for better performance
5. **Drift Detection** — Monitor responses for consistency
6. **Self-Learning** — Improve from interaction patterns

## Agent: Bootstrap

**Module:** `src/prsna/bootstrap.py`

### From Description

```
User Input: "skeptical investigative journalist"
     │
     ▼
┌─────────────────────────────────────┐
│  BOOTSTRAP_SYSTEM_PROMPT            │
│  - Generate name, traits, voice     │
│  - Create boundaries, examples      │
│  - Output structured JSON           │
└─────────────────────────────────────┘
     │
     ▼
Complete Persona YAML
```

### From Real Person

```
User Input: "Marc Andreessen"
     │
     ▼
┌─────────────────────────────────────┐
│  Exa People Search                  │
│  - Query: "Marc Andreessen VC"      │
│  - Get top 3-5 results              │
│  - Extract text + highlights        │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│  PERSON_SYNTHESIS_PROMPT            │
│  - Analyze communication style      │
│  - Extract thinking patterns        │
│  - Create INSPIRED persona          │
│  - NOT impersonation                │
└─────────────────────────────────────┘
     │
     ▼
Persona with source attribution
```

## Agent: Test (DSPy)

**Module:** `src/prsna/optimization/dspy_modules.py`

Uses DSPy signatures for structured evaluation:

```python
class PersonaSignature(dspy.Signature):
    """Respond as a given persona."""
    persona: str = dspy.InputField()
    message: str = dspy.InputField()
    response: str = dspy.OutputField()

class PersonaConsistency(dspy.Signature):
    """Evaluate if response matches persona."""
    persona: str = dspy.InputField()
    response: str = dspy.InputField()
    consistent: bool = dspy.OutputField()
    reasoning: str = dspy.OutputField()
```

**Flow:**

```
Test Messages (10 samples)
     │
     ▼
┌─────────────────────────────────────┐
│  PersonaChat Module                 │
│  - Generate response for each       │
│  - Chain of Thought reasoning       │
└─────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────┐
│  PersonaConsistency Evaluator       │
│  - Score each response              │
│  - Check trait alignment            │
│  - Check voice match                │
└─────────────────────────────────────┘
     │
     ▼
Fidelity Score: 73%
```

## Agent: Optimize (GEPA)

**Module:** `src/prsna/optimization/optimize.py`

GEPA (Genetic-Pareto) optimization flow:

```
Seed: Current persona prompt
     │
     ▼
┌─────────────────────────────────────┐
│  GEPA Optimization Loop             │
│                                     │
│  1. Mutate prompt variants          │
│  2. Evaluate on trainset            │
│  3. Reflect on failures             │
│  4. Select Pareto-optimal           │
│  5. Repeat until budget exhausted   │
└─────────────────────────────────────┘
     │
     ▼
Optimized persona description
(often 2-3x longer with specific guidance)
```

**Key insight:** GEPA uses LLM reflection to understand *why* prompts fail, not just brute-force search.

## Agent: Drift Detection

**Module:** `src/prsna/drift.py`

Monitors responses for consistency:

```
Response to check
     │
     ▼
┌─────────────────────────────────────┐
│  DRIFT_DETECTION_PROMPT             │
│                                     │
│  Evaluate on 4 dimensions:          │
│  - TRAIT_ALIGNMENT                  │
│  - VOICE_CONSISTENCY                │
│  - BOUNDARY_RESPECT                 │
│  - FACTUAL_GROUNDING                │
└─────────────────────────────────────┘
     │
     ▼
DriftScore {
  consistent: bool,
  drift_score: 0.0-1.0,
  issues: [...],
  dimension_scores: {...}
}
```

**Conversation monitoring:**

```python
drift = monitor_conversation(persona, messages)

if drift.needs_refresh:  # avg > 0.3 or increasing trend
    refresh_prompt = suggest_refresh_prompt(persona, drift)
    # Inject refresh into conversation
```

## Agent: Self-Learning

**Module:** `src/prsna/learning.py`

### Interaction Analysis

```
Logged Interactions (last 10)
     │
     ▼
┌─────────────────────────────────────┐
│  FEEDBACK_ANALYSIS_PROMPT           │
│                                     │
│  Extract:                           │
│  - Effective patterns               │
│  - Ineffective patterns             │
│  - Suggested traits                 │
│  - Suggested boundaries             │
│  - Voice adjustments                │
│  - Example to add                   │
└─────────────────────────────────────┘
     │
     ▼
Learnings with confidence score
```

### Self-Critique

Uses stronger model (gpt-4o) for deeper analysis:

```
Persona + Interaction History
     │
     ▼
┌─────────────────────────────────────┐
│  SELF_CRITIQUE_PROMPT               │
│                                     │
│  Analyze:                           │
│  - Total conversations              │
│  - Average drift score              │
│  - Common issues                    │
│                                     │
│  Suggest:                           │
│  - Trait changes (add/remove)       │
│  - Voice changes                    │
│  - Boundary changes                 │
│  - Description rewrite              │
│  - Priority (high/medium/low)       │
└─────────────────────────────────────┘
     │
     ▼
Prioritized improvement plan
```

### Applying Learnings

```python
persona = apply_learnings(persona, learnings, auto_apply=True)
# - Adds suggested traits (if confidence > threshold)
# - Adds boundaries
# - Adjusts voice
# - Adds good examples
# - Rewrites description if suggested
# - Increments version
```

## Data Flow: Complete Lifecycle

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│  CREATE ─────────────────────────────────────────────────────┐   │
│    │                                                         │   │
│    ▼                                                         │   │
│  persona.yaml                                                │   │
│    │                                                         │   │
│    ├──▶ ENRICH (Exa) ──▶ Add context                        │   │
│    │                                                         │   │
│    ├──▶ TEST (DSPy) ──▶ Fidelity score                      │   │
│    │         │                                               │   │
│    │         ▼                                               │   │
│    │    OPTIMIZE (GEPA) ──▶ Better prompt                    │   │
│    │                                                         │   │
│    ├──▶ CHAT ──▶ Log interactions ──┐                       │   │
│    │                                 │                       │   │
│    │    ┌────────────────────────────┘                       │   │
│    │    │                                                    │   │
│    │    ▼                                                    │   │
│    │  LEARN ──▶ Analyze patterns ──▶ Apply improvements ────┘   │
│    │                                                             │
│    └──▶ EXPORT ──▶ eliza / v2 / ollama / hub                    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

## Model Selection

| Task | Default Model | Why |
|------|---------------|-----|
| Bootstrap | gpt-4o-mini | Good enough, fast |
| Enrich synthesis | gpt-4o-mini | Structured extraction |
| Test evaluation | gpt-4o-mini | Many calls, cost-sensitive |
| Optimize | gpt-4o-mini (task) + gpt-4o (reflect) | GEPA uses stronger model for reflection |
| Drift detection | gpt-4o-mini | Per-response, needs speed |
| Self-critique | gpt-4o | Deeper analysis benefits from capability |
| Chat | configurable | User choice via providers.default |

## Extending Agents

### Add a new agent capability

1. Create module in `src/prsna/`
2. Define prompt template as constant
3. Create dataclass for results
4. Use centralized LLM module (NOT direct litellm calls):
   ```python
   from prsna.llm import complete_json, DEFAULT_MODEL

   def my_agent(persona: Persona, model: str = DEFAULT_MODEL) -> dict:
       prompt = MY_PROMPT.format(persona=persona.to_prompt())
       return complete_json(prompt, model=model, default={"error": "failed"})
   ```
5. Add CLI command in `cli.py`
6. Update this doc

### Prompt engineering tips

- Use `complete_json()` for structured responses (handles parsing + defaults)
- Include specific dimensions to evaluate
- Provide examples in prompt when possible
- Use centralized `prsna.llm` module for consistent error handling

## Library Usage: Synthetic Testing

prsna can be used as a library for synthetic data generation and chatbot testing.

### Basic Chat

```python
from prsna import Persona, LLMError

# Load and chat
vc = Persona.load("~/.prsna/personas/tech-investor.yaml")
response = vc.chat("Should I raise a seed round now?")

# Streaming
for chunk in vc.stream("Tell me about market timing"):
    print(chunk, end="", flush=True)

# Error handling
try:
    response = vc.chat("What about market conditions?")
except LLMError as e:
    print(f"LLM call failed: {e}")
```

### Multi-turn Conversation

```python
with vc.conversation() as conv:
    print(conv.send("I have a B2B SaaS startup"))
    print(conv.send("Revenue is $50k MRR"))
    print(conv.send("Should I raise?"))
```

### Synthetic User Generation

Test your chatbot with diverse synthetic users:

```python
from prsna import Persona, bootstrap_from_description

# Create test personas
angry = Persona(**bootstrap_from_description("frustrated customer who wants refund"))
confused = Persona(**bootstrap_from_description("elderly user unfamiliar with technology"))
power = Persona(**bootstrap_from_description("demanding power user who knows the product deeply"))

# Generate test inputs
test_cases = [
    angry.as_user("asking about refund policy"),
    confused.as_user("trying to reset password"),
    power.as_user("requesting advanced API feature"),
]

# Test your bot
for user_message in test_cases:
    bot_response = my_chatbot(user_message)
    # Assert, evaluate, log...
```

### Batch Generation

```python
# Generate many responses for training data
scenarios = [
    "Explain our pricing to a skeptic",
    "Handle a feature request we can't implement",
    "Respond to praise from a happy customer",
]

support = Persona.load("support-agent.yaml")
responses = support.generate(scenarios)
```

### Integration with Testing Frameworks

```python
import pytest
from prsna import Persona, bootstrap_from_description

@pytest.fixture
def angry_customer():
    return Persona(**bootstrap_from_description("angry customer demanding refund"))

def test_bot_handles_angry_customer(angry_customer, my_chatbot):
    user_msg = angry_customer.as_user("product arrived broken")
    response = my_chatbot(user_msg)

    assert "sorry" in response.lower() or "apologize" in response.lower()
    assert "refund" in response.lower() or "replace" in response.lower()
```

### Model Selection

Override models per-call or via persona config:

```python
# Per-call override
response = persona.chat("Hello", model="claude-3-sonnet-20240229")

# Via persona YAML
# providers:
#   default: "gpt-4o-mini"
#   roleplay: "minimax/m2-her"  # if/when supported
```
