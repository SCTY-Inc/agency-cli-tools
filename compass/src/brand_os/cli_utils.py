from __future__ import annotations

import json
from typing import Any

import typer
import yaml
from pydantic import BaseModel
from rich.console import Console
from rich.pretty import Pretty

console = Console()


def emit(data: Any, format: str = "json") -> None:
    normalized = _normalize(data)
    if format == "json":
        console.print_json(json.dumps(normalized, indent=2))
        return
    if format == "yaml":
        typer.echo(yaml.safe_dump(normalized, sort_keys=False))
        return

    console.print(Pretty(normalized))


def _normalize(data: Any) -> Any:
    if isinstance(data, BaseModel):
        return data.model_dump()
    if isinstance(data, dict):
        return data
    if hasattr(data, "model_dump"):
        return data.model_dump()
    return data
