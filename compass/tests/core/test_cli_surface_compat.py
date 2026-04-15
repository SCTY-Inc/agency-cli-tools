from __future__ import annotations

import tomllib
from pathlib import Path

from typer.testing import CliRunner

from brand_os.cli import app


ROOT = Path(__file__).resolve().parents[2]
PYPROJECT = ROOT / "pyproject.toml"
runner = CliRunner()


def _pyproject() -> dict:
    return tomllib.loads(PYPROJECT.read_text())


def test_pyproject_keeps_current_agentcy_compass_entrypoint() -> None:
    pyproject = _pyproject()

    assert pyproject["project"]["scripts"] == {"agentcy-compass": "brand_os.cli:app"}


def test_video_extra_keeps_solver_safe_replicate_floor() -> None:
    pyproject = _pyproject()

    assert pyproject["project"]["optional-dependencies"]["video"] == [
        "replicate>=1.0",
        "cartesia>=2.2",
    ]


def test_cli_app_keeps_current_agentcy_compass_name() -> None:
    assert app.info.name == "agentcy-compass"


def test_cli_help_keeps_current_operator_surface() -> None:
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Usage: agentcy-compass" in result.stdout
    assert "CLI-first brand operations toolkit." in result.stdout
    for command in [
        "persona",
        "intel",
        "signals",
        "plan",
        "produce",
        "eval",
        "publish",
        "queue",
        "monitor",
        "loop",
        "decision",
        "policy",
        "learn",
        "brand",
        "config",
        "version",
    ]:
        assert command in result.stdout


def test_version_command_matches_pyproject_version() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    expected = _pyproject()["project"]["version"]
    assert result.stdout.strip() == f"agentcy-compass v{expected}"


def test_plan_help_keeps_current_subcommand_group() -> None:
    result = runner.invoke(app, ["plan", "--help"])

    assert result.exit_code == 0
    assert "Usage: agentcy-compass plan" in result.stdout
    assert "Campaign planning commands." in result.stdout
    for command in ["research", "strategy", "creative", "activation", "run", "list", "resume"]:
        assert command in result.stdout
