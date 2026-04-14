from __future__ import annotations

import pytest

from agentcy_lab import build_calibration_report, run_doctor_checks
from agentcy_lab.calibration import CANONICAL_FORECAST_PATH, CANONICAL_PERFORMANCE_PATH

requires_family_workspace = pytest.mark.skipif(
    not CANONICAL_FORECAST_PATH.is_file() or not CANONICAL_PERFORMANCE_PATH.is_file(),
    reason="canonical family protocols fixtures are not available in this checkout",
)


@requires_family_workspace
def test_doctor_checks_pass_for_family_workspace() -> None:
    checks = run_doctor_checks()
    assert checks
    assert all(check["ok"] for check in checks)


@requires_family_workspace
def test_calibration_report_matches_canonical_examples() -> None:
    report = build_calibration_report()

    assert report["top_scenario"] == {
        "scenario_id": "givecare.scenario.fall-checkin.base.v1",
        "label": "practical-relief-resonates",
        "probability": 0.58,
    }
    assert report["forecast_focus"] == {
        "platform_mentions": ["linkedin", "instagram"],
        "metric_mentions": ["comments", "saves"],
    }
    assert report["metric_leaders"]["comments"] == {"platform": "linkedin", "value": 29}
    assert report["metric_leaders"]["saves"] == {"platform": "instagram", "value": 65}
    assert report["alignment"] == {
        "verdict": "aligned",
        "matched_metrics": ["comments", "saves"],
        "missed_metrics": [],
    }
    assert "Promote the forecast thesis" in report["recommendation"]
