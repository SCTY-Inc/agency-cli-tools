from __future__ import annotations

import asyncio
import json
import os
import re
from dataclasses import dataclass
from typing import Any, Protocol


class ProviderError(RuntimeError):
    pass


class LLMProvider(Protocol):
    def complete(self, prompt: str, system: str | None = None, model: str | None = None) -> str: ...

    def complete_json(
        self,
        prompt: str,
        system: str | None = None,
        model: str | None = None,
        default: dict[str, Any] | None = None,
    ) -> dict[str, Any]: ...


@dataclass
class LLMConfig:
    provider: str = "mock"
    model: str | None = None


class MockProvider:
    def complete(self, prompt: str, system: str | None = None, model: str | None = None) -> str:
        return ""

    def complete_json(
        self,
        prompt: str,
        system: str | None = None,
        model: str | None = None,
        default: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        return default or {}


class GeminiProvider:
    """Google Gemini provider - best free tier for autonomous loops."""

    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ProviderError("GOOGLE_API_KEY not set")

    def complete(self, prompt: str, system: str | None = None, model: str | None = None) -> str:
        import httpx

        model = model or "gemini-2.0-flash"
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

        messages = []
        if system:
            messages.append({"role": "user", "parts": [{"text": f"System: {system}"}]})
            messages.append({"role": "model", "parts": [{"text": "Understood."}]})
        messages.append({"role": "user", "parts": [{"text": prompt}]})

        response = httpx.post(
            url,
            params={"key": self.api_key},
            json={"contents": messages},
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()

        return data["candidates"][0]["content"]["parts"][0]["text"]

    def complete_json(
        self,
        prompt: str,
        system: str | None = None,
        model: str | None = None,
        default: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        full_prompt = f"{prompt}\n\nRespond with valid JSON only, no markdown."
        text = self.complete(full_prompt, system, model)
        return _parse_json(text, default)


class AnthropicProvider:
    """Anthropic Claude provider - Haiku is cheap for high-volume."""

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ProviderError("ANTHROPIC_API_KEY not set")

    def complete(self, prompt: str, system: str | None = None, model: str | None = None) -> str:
        import httpx

        model = model or "claude-3-5-haiku-20241022"

        response = httpx.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": model,
                "max_tokens": 4096,
                "system": system or "You are a helpful assistant.",
                "messages": [{"role": "user", "content": prompt}],
            },
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()

        return data["content"][0]["text"]

    def complete_json(
        self,
        prompt: str,
        system: str | None = None,
        model: str | None = None,
        default: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        full_prompt = f"{prompt}\n\nRespond with valid JSON only, no markdown."
        text = self.complete(full_prompt, system, model)
        return _parse_json(text, default)


def _parse_json(text: str, default: dict[str, Any] | None = None) -> dict[str, Any]:
    """Extract JSON from LLM response, handling markdown code blocks."""
    # Try to find JSON in code blocks
    json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text)
    if json_match:
        text = json_match.group(1)

    # Try to find raw JSON object
    obj_match = re.search(r'\{[\s\S]*\}', text)
    if obj_match:
        text = obj_match.group(0)

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return default or {}


def get_provider(name: str | None = None) -> LLMProvider:
    provider = name or os.getenv("BRANDOPS_LLM_PROVIDER", "gemini")

    if provider == "mock":
        return MockProvider()
    elif provider == "gemini":
        return GeminiProvider()
    elif provider == "anthropic":
        return AnthropicProvider()

    raise ProviderError(f"Unknown LLM provider: {provider}")


def complete(prompt: str, system: str | None = None, model: str | None = None) -> str:
    provider = get_provider()
    return provider.complete(prompt=prompt, system=system, model=model)


def complete_json(
    prompt: str,
    system: str | None = None,
    model: str | None = None,
    default: dict[str, Any] | None = None,
) -> dict[str, Any]:
    provider = get_provider()
    return provider.complete_json(prompt=prompt, system=system, model=model, default=default)


async def acomplete(prompt: str, system: str | None = None, model: str | None = None) -> str:
    """Async version of complete - runs sync provider in thread pool."""
    return await asyncio.to_thread(complete, prompt, system, model)


async def acomplete_json(
    prompt: str,
    system: str | None = None,
    model: str | None = None,
    default: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Async version of complete_json - runs sync provider in thread pool."""
    return await asyncio.to_thread(complete_json, prompt, system, model, default)
