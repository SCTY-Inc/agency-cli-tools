"""Thin re-export of the canonical adapter so workspace members can import it."""

import sys
from pathlib import Path

# Add the protocols/adapters directory to path so we can import the canonical adapter
_adapters_dir = Path(__file__).parent.parent.parent / "adapters"
if str(_adapters_dir) not in sys.path:
    sys.path.insert(0, str(_adapters_dir))

from run_result_to_performance_v1 import adapt_canonical_run_result_to_performance as adapt_run_result_to_performance  # noqa: E402

__all__ = ["adapt_run_result_to_performance"]
