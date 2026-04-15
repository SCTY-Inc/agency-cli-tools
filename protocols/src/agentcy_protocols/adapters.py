"""Thin re-export of the canonical adapter so workspace members can import it."""

from __future__ import annotations

import importlib.util
from pathlib import Path


def _load_adapter():
    adapter_path = (
        Path(__file__).resolve().parents[3] / "adapters" / "run_result_to_performance_v1.py"
    )
    spec = importlib.util.spec_from_file_location(
        "agentcy_protocols_run_result_to_performance",
        adapter_path,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load canonical adapter from {adapter_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


adapt_run_result_to_performance = _load_adapter().adapt_canonical_run_result_to_performance

__all__ = ["adapt_run_result_to_performance"]
