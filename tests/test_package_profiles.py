from __future__ import annotations

import tomllib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PYPROJECT_PATH = REPO_ROOT / "pyproject.toml"


def _project_metadata() -> dict:
    with PYPROJECT_PATH.open("rb") as fh:
        return tomllib.load(fh)


def test_root_package_exposes_install_profile_extras() -> None:
    project = _project_metadata()["project"]
    extras = project["optional-dependencies"]

    assert extras["echo-simulation"] == ["agentcy-echo[simulation]"]
    assert extras["compass-all"] == ["agentcy-compass[all]"]
    assert extras["full-python"] == [
        "agentcy-compass[all]",
        "agentcy-echo[simulation]",
    ]


def test_root_package_has_readme_metadata() -> None:
    project = _project_metadata()["project"]

    assert project["readme"] == "README.md"
