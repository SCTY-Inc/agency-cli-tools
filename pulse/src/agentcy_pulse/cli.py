from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from .adapter import CANONICAL_RUN_RESULT_PATH, adapt_canonical_run_result_to_performance

_PROTOCOLS_ROOT = Path(__file__).resolve().parents[3] / "protocols"
_CANONICAL_FORECAST = _PROTOCOLS_ROOT / "examples" / "forecast.v1.completed-rich.json"
_CANONICAL_PERFORMANCE = _PROTOCOLS_ROOT / "examples" / "performance.v1.rich.json"
_COMMANDS = {"adapt", "calibrate", "doctor"}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agentcy-pulse",
        description="Measurement and calibration for the agentcy pipeline",
    )
    sub = parser.add_subparsers(dest="command")

    adapt = sub.add_parser("adapt", help="run_result.v1 + sidecar → performance.v1")
    adapt.add_argument("--sidecar", type=Path, required=True)
    adapt.add_argument("--run-result", type=Path, default=CANONICAL_RUN_RESULT_PATH)
    adapt.add_argument("--output", type=Path)

    calibrate = sub.add_parser(
        "calibrate",
        help="forecast.v1 + performance.v1 → calibration report",
    )
    calibrate.add_argument("--forecast", type=Path, default=_CANONICAL_FORECAST)
    calibrate.add_argument("--performance", type=Path, default=_CANONICAL_PERFORMANCE)
    calibrate.add_argument("--output", type=Path)

    doctor = sub.add_parser("doctor", help="Check fixture availability")
    doctor.add_argument("--output", type=Path)

    return parser


def _normalize_argv(argv: Sequence[str] | None) -> tuple[list[str], bool]:
    args = list(sys.argv[1:] if argv is None else argv)
    json_out = False

    normalized: list[str] = []
    for arg in args:
        if arg == "--json":
            json_out = True
            continue
        normalized.append(arg)

    if normalized and normalized[0] not in _COMMANDS:
        return ["adapt", *normalized], json_out

    return normalized, json_out


def main(argv: Sequence[str] | None = None) -> int:
    normalized_argv, json_out = _normalize_argv(argv)
    parser = build_parser()

    if not normalized_argv:
        parser.print_help()
        return 1

    args = parser.parse_args(normalized_argv)

    if args.command == "adapt":
        performance = adapt_canonical_run_result_to_performance(
            args.sidecar,
            run_result_path=args.run_result,
        )
        _emit(
            performance,
            args.output,
            command="adapt",
            json_out=json_out,
        )
        return 0

    if args.command == "calibrate":
        from .calibration import build_calibration_report

        report = build_calibration_report(args.forecast, args.performance)
        _emit(
            report,
            args.output,
            command="calibrate",
            json_out=json_out,
        )
        return 0

    if args.command == "doctor":
        from .calibration import run_doctor_checks

        checks = run_doctor_checks()
        ok = all(check["ok"] for check in checks)
        _emit(
            {"checks": checks},
            args.output,
            command="doctor",
            json_out=json_out,
            status="ok" if ok else "error",
        )
        return 0 if ok else 1

    parser.print_help()
    return 1


def _emit(
    data: dict[str, Any],
    path: Path | None = None,
    *,
    command: str,
    json_out: bool,
    status: str = "ok",
) -> None:
    raw_payload = json.dumps(data, indent=2) + "\n"
    if path is not None:
        path.write_text(raw_payload)
        if not json_out:
            return
        envelope = {
            "status": status,
            "command": command,
            "data": {"output": str(path)},
        }
        print(json.dumps(envelope, indent=2))
        return

    if json_out:
        print(json.dumps({"status": status, "command": command, "data": data}, indent=2))
        return

    print(raw_payload, end="")
