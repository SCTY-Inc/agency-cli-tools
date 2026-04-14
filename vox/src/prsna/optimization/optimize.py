"""Persona optimization and testing."""

from __future__ import annotations

from typing import TYPE_CHECKING

import dspy

if TYPE_CHECKING:
    from prsna.persona import Persona


def persona_fidelity_metric(example: dspy.Example, prediction: dspy.Prediction) -> float:
    """Measure how well a response matches persona expectations.

    Returns a score between 0 and 1.
    """
    from prsna.optimization.dspy_modules import PersonaConsistency

    evaluator = dspy.ChainOfThought(PersonaConsistency)

    result = evaluator(
        persona=example.persona,
        response=prediction.response,
    )

    return 1.0 if result.consistent else 0.0


def test_persona(
    persona: Persona,
    test_messages: list[str] | None = None,
    num_samples: int = 10,
) -> dict:
    """Test persona consistency across sample interactions.

    Args:
        persona: The persona to test
        test_messages: Custom test messages (optional)
        num_samples: Number of samples if no custom messages

    Returns:
        Dict with score, passed/failed counts, and details
    """
    from prsna.optimization.dspy_modules import PersonaChat

    # Default test messages
    if not test_messages:
        test_messages = [
            "Hello, who are you?",
            "What do you think about this topic?",
            "Can you help me with something?",
            "Tell me more about yourself.",
            "What's your opinion on current events?",
            "How would you approach this problem?",
            "What are your strengths?",
            "Describe your background.",
            "What do you value most?",
            "How do you handle disagreements?",
        ][:num_samples]

    chat = PersonaChat(persona.to_prompt())
    results = []

    for msg in test_messages:
        example = dspy.Example(persona=persona.to_prompt(), message=msg).with_inputs(
            "persona", "message"
        )
        prediction = chat(message=msg)
        score = persona_fidelity_metric(example, prediction)
        results.append({"message": msg, "response": prediction.response, "score": score})

    scores = [r["score"] for r in results]
    avg_score = sum(scores) / len(scores) if scores else 0

    return {
        "persona": persona.name,
        "score": avg_score,
        "passed": sum(1 for s in scores if s > 0.5),
        "failed": sum(1 for s in scores if s <= 0.5),
        "total": len(scores),
        "details": results,
    }


def optimize_persona(
    persona: Persona,
    trainset: list[dspy.Example],
    valset: list[dspy.Example] | None = None,
    max_iterations: int = 50,
) -> Persona:
    """Optimize persona prompt using GEPA.

    Args:
        persona: The persona to optimize
        trainset: Training examples
        valset: Validation examples (optional)
        max_iterations: Maximum optimization iterations

    Returns:
        Persona with optimized description/traits
    """
    try:
        import gepa
    except ImportError:
        raise ImportError("gepa required: pip install gepa")

    seed_candidate = {"persona_prompt": persona.to_prompt()}

    result = gepa.optimize(
        seed_candidate=seed_candidate,
        trainset=trainset,
        valset=valset or trainset,
        task_lm="openai/gpt-4o-mini",
        reflection_lm="openai/gpt-4o",
        max_metric_calls=max_iterations,
    )

    # Update persona description with optimized prompt
    optimized_prompt = result.best_candidate["persona_prompt"]
    persona.description = optimized_prompt

    return persona
