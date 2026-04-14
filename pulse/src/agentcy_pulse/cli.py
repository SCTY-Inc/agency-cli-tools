from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Sequence

from .adapter import CANONICAL_RUN_RESULT_PATH, adapt_canonical_run_result_to_performance

# Calibration logic inlined from agentcy-lab
_PROTOCOLS_ROOT = Path(__file__).resolve().parents[3] / "protocols"
_CANONICAL_FORECAST = _PROTOCOLS_ROOT / "examples" / "forecast.v1.completed-rich.json"
_CANONICAL_PERFORMANCE = _PROTOCOLS_ROOT / "examples" / "performance.v1.rich.json"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agentcy-pulse",
        description="Measurement and calibration for the agentcy pipeline",
    )
    sub = parser.add_subparsers(dest="command")

    # adapt: run_result.v1 + sidecar → performance.v1
    adapt = sub.add_parser("adapt", help="run_result.v1 + sidecar → performance.v1")
    adapt.add_argument("--sidecar", type=Path, required=True)
    adapt.add_argument("--run-result", type=Path, default=CANONICAL_RUN_RESULT_PATH)
    adapt.add_argument("--output", type=Path)

    # calibrate: forecast.v1 + performance.v1 → calibration report
    cal = sub.add_parser("calibrate", help="forecast.v1 + performance.v1 → calibration report")
    cal.add_argument("--forecast", type=Path, default=_CANONICAL_FORECAST)
    cal.add_argument("--performance", type=Path, default=_CANONICAL_PERFORMANCE)
    cal.add_argument("--output", type=Path)

    # doctor
    sub.add_parser("doctor", help="Check fixture availability")

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "adapt" or args.command is None:
        # Bare invocation: legacy compat — treat flags as adapt
        if args.command is None:
            build_parser().print_help()
            return 1
        performance = adapt_canonical_run_result_to_performance(
            args.sidecar,
            run_result_path=args.run_result,
        )
        _emit(performance, args.output)

    elif args.command == "calibrate":
        from .calibration import build_calibration_report
        report = build_calibration_report(args.forecast, args.performance)
        _emit({"status": "ok", "command": "calibrate", "data": report}, args.output)

    elif args.command == "doctor":
        from .calibration import run_doctor_checks
        checks = run_doctor_checks()
        ok = all(c["ok"] for c in checks)
        _emit({"status": "ok" if ok else "error", "command": "doctor", "data": {"checks": checks}})
        return 0 if ok else 1

    return 0


def _emit(data: object, path: Path | None = None) -> None:
    payload = json.dumps(data, indent=2) + "\n"
    if path:
        path.write_text(payload)
    print(payload, end="")
