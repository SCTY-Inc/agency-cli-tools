from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .calibration import (
    CANONICAL_FORECAST_PATH,
    CANONICAL_PERFORMANCE_PATH,
    build_calibration_report,
    run_doctor_checks,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Minimal agentcy-lab CLI for forecast.v1 -> performance.v1 calibration"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("doctor", help="Check canonical family fixture availability")

    calibration = subparsers.add_parser(
        "calibration",
        help="Compare forecast intent with observed performance",
    )
    calibration.add_argument(
        "--forecast",
        type=Path,
        default=CANONICAL_FORECAST_PATH,
        help="Path to forecast.v1 JSON (defaults to the canonical family fixture)",
    )
    calibration.add_argument(
        "--performance",
        type=Path,
        default=CANONICAL_PERFORMANCE_PATH,
        help="Path to performance.v1 JSON (defaults to the canonical family fixture)",
    )
    calibration.add_argument("--output", type=Path, help="Optional output path")

    return parser


def _emit(payload: dict) -> None:
    print(json.dumps(payload, indent=2))


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "doctor":
        checks = run_doctor_checks()
        ok = all(check["ok"] for check in checks)
        _emit({"status": "ok" if ok else "error", "command": "doctor", "data": {"checks": checks}})
        return 0 if ok else 1

    if args.command == "calibration":
        report = build_calibration_report(args.forecast, args.performance)
        if args.output:
            args.output.write_text(json.dumps(report, indent=2) + "\n")
            data = {"output_path": str(args.output), "report": report}
        else:
            data = report
        _emit({"status": "ok", "command": "calibration", "data": data})
        return 0

    raise ValueError(f"Unknown command: {args.command}")
