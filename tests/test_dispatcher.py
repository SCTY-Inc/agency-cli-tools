from __future__ import annotations

import json
from pathlib import Path

from typer.testing import CliRunner

import agentcy.cli as cli
from agentcy import __version__

runner = CliRunner()


def test_version_command_uses_package_version() -> None:
    result = runner.invoke(cli.app, ["version"])

    assert result.exit_code == 0
    assert result.stdout.strip() == f"agentcy {__version__}"


def test_doctor_reports_member_probe_failures(monkeypatch) -> None:
    fake_bins = {
        "agentcy-vox": "/tmp/agentcy-vox",
        "agentcy-compass": "/tmp/agentcy-compass",
        "agentcy-echo": "/tmp/agentcy-echo",
        "agentcy-pulse": "/tmp/agentcy-pulse",
        "node": "/tmp/node",
    }

    def fake_which(name: str) -> str | None:
        return fake_bins.get(name)

    def fake_probe(command: list[str]) -> bool:
        joined = " ".join(command)
        return "agentcy-echo" not in joined and " help " not in f" {joined} "

    monkeypatch.setattr(cli.shutil, "which", fake_which)
    monkeypatch.setattr(cli, "_loom_bin", lambda: "/tmp/agentcy-loom")
    monkeypatch.setattr(cli, "_probe_member", fake_probe)

    result = runner.invoke(cli.app, ["doctor", "--json"])

    assert result.exit_code == 1
    payload = json.loads(result.stdout)
    assert payload["status"] == "error"
    assert payload["data"]["echo"]["reachable"] is False
    assert payload["data"]["loom"]["reachable"] is False


def test_doctor_reports_ok_when_members_are_present_and_reachable(monkeypatch) -> None:
    fake_bins = {
        "agentcy-vox": "/tmp/agentcy-vox",
        "agentcy-compass": "/tmp/agentcy-compass",
        "agentcy-echo": "/tmp/agentcy-echo",
        "agentcy-pulse": "/tmp/agentcy-pulse",
        "node": "/tmp/node",
    }

    monkeypatch.setattr(cli.shutil, "which", lambda name: fake_bins.get(name))
    monkeypatch.setattr(cli, "_loom_bin", lambda: "/tmp/agentcy-loom")
    monkeypatch.setattr(cli, "_probe_member", lambda command: True)

    result = runner.invoke(cli.app, ["doctor", "--json"])

    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert payload["status"] == "ok"
    assert all(info["reachable"] for info in payload["data"].values())


def test_local_loom_bin_resolves_repo_runtime_bin() -> None:
    expected = Path(__file__).resolve().parents[1] / "loom" / "runtime" / "bin" / "loom.js"
    resolved = cli._loom_bin()

    assert resolved is not None
    assert Path(resolved) == expected
