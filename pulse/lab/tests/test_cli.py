from __future__ import annotations

import json
from pathlib import Path

from agentcy_lab.cli import main


def test_doctor_command_emits_ok_payload(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "agentcy_lab.cli.run_doctor_checks",
        lambda: [{"name": "protocols-directory", "ok": True, "path": "/tmp/protocols"}],
    )

    exit_code = main(["doctor"])

    assert exit_code == 0
    assert json.loads(capsys.readouterr().out) == {
        "status": "ok",
        "command": "doctor",
        "data": {"checks": [{"name": "protocols-directory", "ok": True, "path": "/tmp/protocols"}]},
    }


def test_calibration_command_writes_output_file(monkeypatch, tmp_path: Path, capsys) -> None:
    report = {"alignment": {"verdict": "aligned"}}
    output_path = tmp_path / "calibration.json"

    def fake_report(forecast: Path, performance: Path) -> dict:
        assert forecast == Path("forecast.json")
        assert performance == Path("performance.json")
        return report

    monkeypatch.setattr("agentcy_lab.cli.build_calibration_report", fake_report)

    exit_code = main(
        [
            "calibration",
            "--forecast",
            "forecast.json",
            "--performance",
            "performance.json",
            "--output",
            str(output_path),
        ]
    )

    assert exit_code == 0
    assert json.loads(output_path.read_text()) == report
    assert json.loads(capsys.readouterr().out) == {
        "status": "ok",
        "command": "calibration",
        "data": {"output_path": str(output_path), "report": report},
    }
