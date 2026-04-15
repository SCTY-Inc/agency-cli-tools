# agentcy-lab reality review — 2026-04-14

## Scope

Bounded deep review of `agentcy-lab/` as the current family calibration-plane repo. This review stays limited to current repo truth:

- repo status and cleanliness
- README / manifest / import / CLI surfaces
- test coverage and current verification results
- whether scan-level coverage is sufficient right now

`agentcy-lab` is a current Agentcy family repo, not a background note. Per the control-plane docs, it is the shared eval/autoresearch plane that sits across `agentcy-vox`, `agentcy-compass`, `agentcy-echo`, `agentcy-loom`, and `agentcy-pulse` without taking ownership of their production state.

## Repo-state truth

- Repo path: `agentcy-lab/`
- Git state: clean on `main`
- Working tree evidence: `cd agentcy-lab && git status --short --branch` returned only `## main`
- Diff evidence: `cd agentcy-lab && git diff --stat` returned no pending changes

Interpretation: unlike some larger family repos, `agentcy-lab` currently presents as a minimal, clean, bounded repo rather than an in-progress migration surface.

## Surface inventory

### README

`agentcy-lab/README.md` accurately describes the repo as a minimal birth slice for the shared `agentcy-lab` eval/autoresearch plane.

Documented scope is narrow and consistent with current code:

- canonical inputs from `../protocols/examples/forecast.v1.completed-rich.json`
- canonical inputs from `../protocols/examples/performance.v1.rich.json`
- repo-local output: calibration report comparing forecast intent with observed performance
- explicit non-goal: no canonical `lab` protocol claim yet

The README also documents the exact smoke checks that matter right now:

- `uv run agentcy-lab --help`
- `uv run agentcy-lab doctor`
- `uv run agentcy-lab calibration`
- `uv run python -c "import agentcy_lab"`
- `uv run pytest`

### Manifest / package / import surface

`agentcy-lab/pyproject.toml` matches the README and the recap docs:

- package/distribution: `agentcy-lab`
- import root: `agentcy_lab`
- installed CLI binary: `agentcy-lab`
- Python floor: `>=3.11`
- wheel package target: `src/agentcy_lab`

This is unusually clean compared with the family repos that still carry older package/import/bin drift. There is no competing legacy package name or alternate installed CLI documented in the repo.

### CLI entrypoint

The repo exposes one script entrypoint:

- `[project.scripts] agentcy-lab = "agentcy_lab.cli:main"`

`src/agentcy_lab/cli.py` is intentionally small and only exposes two subcommands:

- `doctor`
- `calibration`

Observed CLI behavior from live verification:

- `agentcy-lab --help` prints the expected two-command surface
- `agentcy-lab doctor` verifies the sibling `protocols/` directory plus canonical `forecast.v1` and `performance.v1` fixtures
- `agentcy-lab calibration` is a thin wrapper around report generation and optional JSON output

Interpretation: the CLI is honest about being a thin calibration seam. It does not pretend to be a broader eval framework, orchestration plane, or family umbrella runtime.

### Code/import surface

Current source files are minimal:

- `src/agentcy_lab/__init__.py`
- `src/agentcy_lab/__main__.py`
- `src/agentcy_lab/cli.py`
- `src/agentcy_lab/calibration.py`

Current import surface is also narrow:

- public exports are `build_calibration_report` and `run_doctor_checks`
- calibration logic reads canonical family fixtures from `../protocols/`
- lineage validation only checks `brief_id` and `brand_id`
- output is a repo-local calibration report, not a new family-owned protocol artifact

This matches the role described in `AGENTCY_RECAP.md`: `agentcy-lab` is a cross-family eval/autoresearch plane and does not own production module state.

## Test surface

Repo-local tests are present and aligned with the current bounded scope:

- `tests/test_cli.py`
  - verifies `doctor` JSON output shape
  - verifies `calibration` output-file behavior
- `tests/test_calibration.py`
  - verifies doctor checks pass when canonical family fixtures exist
  - verifies the canonical calibration report against live sibling family fixtures

CI surface is also present via `.github/workflows/smoke.yml`:

- `uv sync`
- `uv run agentcy-lab --help`
- `uv run python -c "import agentcy_lab"`
- `uv run pytest`

Interpretation: for a repo this small, the test surface is proportionate and directly tied to the only seam the repo currently claims.

## Verification run on 2026-04-14

Executed from `agentcy-lab/`:

```bash
uv run agentcy-lab --help
uv run agentcy-lab doctor
uv run pytest
```

Observed results:

- help output exposed only `doctor` and `calibration`
- doctor returned `status: ok` and found:
  - `/Users/amadad/projects/protocols`
  - `protocols/examples/forecast.v1.completed-rich.json`
  - `protocols/examples/performance.v1.rich.json`
- pytest passed: `4 passed`

## Classification

## Decision: `agentcy-lab` is currently scan-sufficient

It does **not** need its own immediate bounded follow-up task right now.

### Why this is sufficient

1. **Repo-state truth is stable and clean.**
   The repo is clean on `main` with no active dirty-state ambiguity.

2. **Package / import / CLI surfaces are already aligned.**
   The repo name, package name, import root, and installed CLI binary all point to the same current family identity:
   - repo: `agentcy-lab`
   - package: `agentcy-lab`
   - import: `agentcy_lab`
   - CLI: `agentcy-lab`

3. **The CLI claim is bounded and truthful.**
   The repo exposes only a `doctor` check and one `forecast.v1 -> performance.v1` calibration report path. There is no evidence of hidden broader ownership or drift between docs and executable surface.

4. **Tests cover the exact seam the repo claims to own.**
   The tests verify both local CLI behavior and the live family-fixture-backed calibration seam. For a minimal calibration-plane repo, this is enough scan depth to classify current reality.

5. **The repo is already explicitly represented in the family control plane.**
   `AGENTCY_STACK.md`, `AGENTCY_PROGRESS.md`, and `AGENTCY_RECAP.md` all treat `agentcy-lab` as a current family repo with the shared eval/autoresearch role, not as a side note.

## Smallest next task, if one is later needed

No immediate follow-up is required.

If the family later wants deeper `agentcy-lab` work, the smallest honest bounded follow-up would be:

- **document one additional calibration/eval seam only after another module exposes a stable protocol-backed input worth scoring**

That future task should still avoid:

- inventing a canonical `lab` protocol early
- turning `agentcy-lab` into a family umbrella CLI
- broad framework work untied to a real family seam

## Bottom line

`agentcy-lab` is a real current family repo and, at present, a notably clean one. Its README, manifest, import surface, CLI entrypoint, tests, and git state all agree on the same narrow truth: it is a minimal cross-family calibration-plane repo proving one bounded `forecast.v1 -> performance.v1` seam. That makes scan-level coverage sufficient for now.