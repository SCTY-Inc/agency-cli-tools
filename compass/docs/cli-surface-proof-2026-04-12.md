# brand-os CLI surface proof — 2026-04-12

Scope: bounded loop-10 proof for the current repo-local CLI surface without introducing any package rename, import-path rewrite, runtime-prefix migration, or repo rename.

## Outcome summary

This proof locks the current operator-facing CLI surface as it actually exists today:

- installed script name: `brandos`
- Typer app name: `brandos`
- help banner: `CLI-first brand operations toolkit.`
- current top-level command tree still includes broader-than-compass groups such as `persona`, `produce`, `eval`, `publish`, `queue`, and `monitor`
- `brandos version` should match the installed `brand-os` distribution version
- `brandos plan --help` should continue exposing the current planning subgroup surface

This is evidence for current CLI truthfulness only. It does **not** claim:

- a future `agentcy-compass` or `compass` binary
- a narrowed command tree already aligned to future `agentcy-compass` ownership
- any import rename away from `brand_os`
- any runtime/env/data-path cleanup

## Deterministic repo-local coverage added

New repo-local compatibility checks live in:

- `tests/core/test_cli_surface_compat.py`

They verify:

1. `pyproject.toml` still exposes `[project.scripts].brandos = "brand_os.cli:app"`
2. the Typer app name remains `brandos`
3. `brandos --help` still presents the current operator-facing banner and command groups
4. `brandos version` stays aligned with installed distribution metadata for `brand-os`
5. `brandos plan --help` keeps the current planning subcommand surface

## Exact verification commands

Run from repo root with the existing local virtualenv:

```bash
cd /Users/amadad/projects/brand-os
./.venv/bin/python -m py_compile tests/core/test_cli_surface_compat.py
./.venv/bin/python - <<'PY'
import importlib.metadata
from typer.testing import CliRunner
from brand_os.cli import app

runner = CliRunner()
help_result = runner.invoke(app, ["--help"])
version_result = runner.invoke(app, ["version"])
plan_help_result = runner.invoke(app, ["plan", "--help"])

assert help_result.exit_code == 0
assert "Usage: brandos" in help_result.stdout
assert "CLI-first brand operations toolkit." in help_result.stdout
for command in [
    "persona", "intel", "signals", "plan", "produce", "eval", "publish",
    "queue", "monitor", "loop", "decision", "policy", "learn", "brand",
    "config", "version",
]:
    assert command in help_result.stdout

assert version_result.exit_code == 0
assert version_result.stdout.strip() == f"brandos v{importlib.metadata.version('brand-os')}"

assert plan_help_result.exit_code == 0
assert "Usage: brandos plan" in plan_help_result.stdout
assert "Campaign planning commands." in plan_help_result.stdout
for command in ["research", "strategy", "creative", "activation", "run", "list", "resume"]:
    assert command in plan_help_result.stdout
PY
```

## Interpretation for loop-10 readiness

This narrows one proof gap: the repo now has deterministic coverage for the current CLI/package identity instead of relying only on manual external install notes.

It does **not** remove the larger blockers:

- repo/package/import names are still `brand-os` / `brand_os`
- runtime and env prefixes remain mixed across `.brandos`, `.brand-os`, `BRANDOPS_*`, and `BRANDOS_DATA_DIR`
- the top-level CLI still exposes broader repo scope than future `agentcy-compass`
- external packaged verification via `uv run` remains environment-sensitive when dependency resolution is unhealthy
