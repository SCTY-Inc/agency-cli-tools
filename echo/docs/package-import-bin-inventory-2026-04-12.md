# cli-mirofish package / import / bin inventory — 2026-04-12

## Scope

This is a bounded inventory for the current `cli-mirofish` public compatibility surfaces and their reference blast radius.

It inventories, without rewriting:

- distribution name: `mirofish-backend`
- import root: `app`
- CLI binary: `mirofish`

It also separates these public/operator-facing surfaces from safe internal legacy identifiers that are not themselves the current package/import/bin contract.

## Current public compatibility surfaces

| Surface type | Current surface | Source of truth | Notes |
| --- | --- | --- | --- |
| Python distribution | `mirofish-backend` | `cli-mirofish/pyproject.toml` | Current install/build metadata surface. |
| Top-level import root | `app` | `cli-mirofish/pyproject.toml`, repo imports under `cli-mirofish/app/` | Current package/import surface exposed by the wheel because `packages = ["app"]`. |
| Console script / CLI binary | `mirofish` | `cli-mirofish/pyproject.toml`, `cli-mirofish/app/cli.py` | Current operator-facing installed command. |
| Canonical family writer fields | `writer = { repo: "cli-mirofish", module: "agentcy-echo" }` | `protocols/forecast.v1.schema.json`, `protocols/tests/test_brief_to_forecast_v1.py`, `cli-mirofish/app/forecast_v1.py` | Family artifact contract is already mixed/canonical and is intentionally separate from package/import/bin naming. |

## Exact defining references

### 1. Distribution: `mirofish-backend`

Defined in `cli-mirofish/pyproject.toml`:

```toml
[project]
name = "mirofish-backend"
```

Additional packaging evidence:

```toml
[tool.hatch.build.targets.wheel]
packages = ["app"]
```

This means the shipped distribution name and the import root are currently different surfaces:

- install/build surface: `mirofish-backend`
- import surface: `app`

### 2. Import root: `app`

Defined in `cli-mirofish/pyproject.toml` via:

```toml
[tool.hatch.build.targets.wheel]
packages = ["app"]
```

The console entry point also resolves through that import root:

```toml
[project.scripts]
mirofish = "app.cli:main"
```

Repo-local test imports confirm the current import surface is still `app.*`:

- `cli-mirofish/tests/test_cli_artifacts_and_visuals.py`
  - `from app.brief_v1 import import_brief_v1`
  - `from app.cli import ...`
  - `from app.forecast_v1 import ...`
  - `from app.config import Config`
  - `from app.run_artifacts import RunStore`
  - `from app.services.simulation_runner import ...`
  - `from app.visual_snapshots import ...`
- `protocols/tests/test_brief_to_forecast_v1.py`
  - `from app.brief_v1 import import_brief_v1`
  - `from app.cli import main`
  - `from app.config import Config`
  - `from app.run_artifacts import RunStore`

### 3. CLI binary: `mirofish`

Defined in `cli-mirofish/pyproject.toml`:

```toml
[project.scripts]
mirofish = "app.cli:main"
```

Confirmed in `cli-mirofish/app/cli.py`:

```python
parser = argparse.ArgumentParser(prog="mirofish", description="Minimal run-first CLI for MiroFish")
```

Documented operator-facing usage:

- `cli-mirofish/README.md`
  - `mirofish run ...`
  - `mirofish runs list --json`
  - `mirofish runs status <run_id> --json`
  - `mirofish runs export <run_id> --json`
  - `mirofish runs export <run_id> --artifact forecast_v1 --json`
- `cli-mirofish/CLAUDE.md`
  - `mirofish run --files ...`
  - `mirofish runs list --json`
  - `mirofish runs status <id> --json`
  - `mirofish runs export <id> --json`
- `cli-mirofish/tests/test_cli_artifacts_and_visuals.py`
  - parser assertions are built around the current run/runs CLI shape
- `cli-mirofish/docs/prd-agent-first-cli.md`
  - explicitly states `A single CLI executable, mirofish.`

## Reference blast radius

### Repo-local references

#### Public/package metadata and docs

| File | Surface(s) referenced | Why it matters |
| --- | --- | --- |
| `cli-mirofish/pyproject.toml` | `mirofish-backend`, `mirofish`, `app` | Primary source of truth for distribution, installed binary, and packaged import root. |
| `cli-mirofish/README.md` | `mirofish` | Public operator docs and examples. |
| `cli-mirofish/CLAUDE.md` | `mirofish`, `app` | Repo operating docs and layout contract. |
| `cli-mirofish/app/cli.py` | `mirofish` | CLI parser declares the current binary/program name. |
| `cli-mirofish/docs/prd-agent-first-cli.md` | `mirofish` | Product/CLI contract doc still names the executable directly. |
| `cli-mirofish/docs/rename-readiness-scorecard-2026-04-12.md` | `mirofish-backend`, `mirofish`, `app` | Prior control-plane audit already records these as blockers/readiness surfaces. |

#### Repo-local tests and code imports

| File | Surface(s) referenced | Why it matters |
| --- | --- | --- |
| `cli-mirofish/tests/test_cli_artifacts_and_visuals.py` | `app` | Direct imports from `app.*`; verifies parser/export behavior tied to current package layout. |
| `cli-mirofish/scripts/run_parallel_simulation.py` | `app` | Internal script imports `app.utils.oasis_llm`. |
| `cli-mirofish/scripts/run_reddit_simulation.py` | `app` | Internal script imports `app.utils.oasis_llm`. |
| `cli-mirofish/scripts/run_twitter_simulation.py` | `app` | Internal script imports `app.utils.oasis_llm`. |
| `cli-mirofish/scripts/test_profile_format.py` | `app` | Internal script imports `app.services.oasis_profile_generator`. |

### Family-test / parent-level references

| File | Surface(s) referenced | Why it matters |
| --- | --- | --- |
| `protocols/tests/test_brief_to_forecast_v1.py` | `app`, `cli-mirofish` | Parent-level seam test imports `app.*`, sets `CLI_MIROFISH_DIR = ROOT / "cli-mirofish"`, and asserts canonical writer fields. |
| `protocols/tests/test_forecast_v1_protocol.py` | `cli-mirofish` | Parent-level protocol test asserts `writer = { repo: "cli-mirofish", module: "agentcy-echo" }`. |
| `protocols/tests/test_canonical_writer_module_references.py` | `cli-mirofish` | Family-level mixed writer contract regression. |
| `protocols/forecast.v1.schema.json` | `cli-mirofish` | Canonical schema locks `writer.repo = "cli-mirofish"`. |
| `protocols/examples/forecast.v1.completed-minimal.json` | `cli-mirofish` | Canonical example fixture uses the current repo name in writer metadata. |
| `protocols/examples/forecast.v1.completed-rich.json` | `cli-mirofish` | Canonical example fixture uses the current repo name in writer metadata. |

## Public compatibility surfaces vs safe internal legacy identifiers

### Public compatibility surfaces to treat as externally meaningful right now

These are the active surfaces an operator, installer, or downstream test can reasonably depend on today:

- distribution name: `mirofish-backend`
- import root: `app`
- console script: `mirofish`
- canonical family artifact writer repo: `cli-mirofish`
- canonical family artifact writer module: `agentcy-echo`

### Safe internal legacy identifiers to record, not rewrite in this task

These appear throughout the repo, but they are not the same thing as the current package/import/bin contract:

- logger namespaces such as `mirofish.graph_storage`, `mirofish.report_agent`, `mirofish.simulation_runner`
- default display/product strings such as `MiroFish Run`
- historical/upstream references in docs such as `MiroFish` fork attribution and AGPL lineage notes
- internal file/layout paths under `app/services`, `app/tools`, `app/resources`, etc.
- internal image/container references such as `ghcr.io/${owner}/mirofish`
- persisted MiroFish-local provenance IDs already separated from family lineage in forecast export work

Why they are classified as safe internal legacy identifiers here:

1. They are mostly internal implementation, provenance, or attribution surfaces.
2. They do not by themselves redefine the install/import/CLI contract.
3. Rewriting them would widen scope into runtime/logging/migration churn, which this inventory task does not authorize.

## Blast-radius summary by named surface

### `mirofish-backend`

Current blast radius is relatively narrow but external:

- package metadata in `cli-mirofish/pyproject.toml`
- lock/build metadata such as `cli-mirofish/uv.lock`
- prior rename-readiness docs that already record the distribution name

Interpretation: this is a real public packaging surface, but its references are much narrower than `app` imports or `mirofish` operator docs.

### `app`

Current blast radius is broad and structural:

- wheel packaging via `packages = ["app"]`
- console script target `app.cli:main`
- repo-local test imports
- parent-level family test imports
- internal scripts importing `app.*`
- repo layout/docs describing `app/` as the main code root

Interpretation: `app` is the heaviest rename-readiness blocker of the three surfaces because it is both a packaged import root and a widely used internal code path.

### `mirofish`

Current blast radius is medium-to-broad and operator-facing:

- installed console script definition in `pyproject.toml`
- CLI parser `prog="mirofish"`
- README usage examples
- CLAUDE usage examples
- agent-first CLI PRD
- rich CLI display text and other repo-local docs

Interpretation: `mirofish` is a public/operator contract, but changing it would be less structurally invasive than changing the `app` import root.

## Exact evidence gathered

### Read artifacts

- `cli-mirofish/pyproject.toml`
- `cli-mirofish/README.md`
- `cli-mirofish/CLAUDE.md`
- `cli-mirofish/app/cli.py`
- `cli-mirofish/tests/test_cli_artifacts_and_visuals.py`
- `protocols/tests/test_brief_to_forecast_v1.py`
- `AGENTCY_STACK.md`
- `AGENTCY_PROGRESS.md`
- `CONSOLIDATION.md`
- `AGENTCY_RECAP.md`

### Search command used

```bash
rg -n --hidden --glob '!**/.venv/**' --glob '!**/dist/**' --glob '!**/build/**' '\bmirofish-backend\b|\bmirofish\b|\bapp\b' cli-mirofish protocols
```

### Verification commands used

```bash
cd cli-mirofish && uv run python -m pytest tests/test_cli_artifacts_and_visuals.py -k 'cli_parser_is_run_first or runs_export_emits_forecast_v1'
cd cli-mirofish && uv run python -m pytest ../protocols/tests/test_brief_to_forecast_v1.py
```

### Verification results

- `tests/test_cli_artifacts_and_visuals.py`: 2 selected tests passed
- `protocols/tests/test_brief_to_forecast_v1.py`: 2 tests passed

## Bottom line

The current public compatibility surfaces are still exactly:

- distribution: `mirofish-backend`
- import root: `app`
- CLI binary: `mirofish`

The family artifact contract stays intentionally separate and already canonical as:

- `writer.repo = "cli-mirofish"`
- `writer.module = "agentcy-echo"`

This inventory shows:

- `mirofish-backend` is a bounded packaging/install surface
- `mirofish` is a public operator/docs surface
- `app` is the broadest structural surface and the largest rename-readiness blocker
- many `mirofish.*` internal identifiers are better treated as safe legacy/internal surfaces unless a later bounded migration explicitly targets them

No package/import/bin names were changed by this task.
