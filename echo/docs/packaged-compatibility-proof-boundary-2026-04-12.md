# cli-mirofish packaged compatibility proof boundary — 2026-04-12

## Scope

This is the bounded loop-11 proof note for `cli-mirofish` / future `agentcy-echo`.

It records exactly what is proven now across the currently shipped package/import/bin surfaces and the narrow family protocol seam, and it records the exact blocker that still prevents claiming a clean external proof of the full simulation runtime.

This note does not authorize:

- a literal repo rename
- a package/distribution rename
- an import-root rewrite away from `app`
- a CLI rename away from `mirofish`
- broad cross-repo churn

## Current surfaces under proof

The current public or semi-public compatibility surfaces remain:

- distribution: `mirofish-backend`
- import root: `app`
- console script: `mirofish`
- optional simulation runtime extra: `mirofish-backend[simulation]`
- canonical artifact writer: `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`

## Exact validation pass run

All commands below were run on 2026-04-12 from the current repo state.

### 1. Build the current package

```bash
cd cli-mirofish && uv build
```

Result:

- passed
- produced:
  - `dist/mirofish_backend-0.1.0.tar.gz`
  - `dist/mirofish_backend-0.1.0-py3-none-any.whl`

### 2. Repo-environment CLI help smoke

```bash
cd cli-mirofish && uv run mirofish --help
```

Result:

- passed
- current installed/repo-env operator surface is still `mirofish`
- help output confirms the current run-first CLI shape:
  - `usage: mirofish [-h] {run,runs} ...`
  - `Minimal run-first CLI for MiroFish`

### 3. Repo-environment import-root smoke

```bash
cd cli-mirofish && uv run python - <<'PY'
import app
from pathlib import Path
print(Path(app.__file__).resolve())
PY
```

Result:

- passed
- resolved import path:
  - `/Users/amadad/projects/cli-mirofish/app/__init__.py`
- this proves the current repo-env import surface is still `app`

### 4. Tiny current-surface compatibility proof

```bash
cd cli-mirofish && uv run python -m pytest tests/test_public_surface_contract.py -q
```

Result:

- passed
- summary: `5 passed in 0.17s`

What this tiny proof artifact locks:

- `[project].name == "mirofish-backend"`
- `[project.scripts] == { "mirofish": "app.cli:main" }`
- wheel packages remain `[`"app"`]`
- repo-local `import app` and `app.cli.main` remain valid
- pinned upstream OASIS/CAMEL deps now live in optional `[project.optional-dependencies].simulation`

### 5. Narrow parent-level protocol validation

```bash
cd cli-mirofish && uv run python -m pytest ../protocols/tests/test_brief_to_forecast_v1.py ../protocols/tests/test_forecast_v1_protocol.py -q
```

Result:

- passed
- summary: `4 passed in 0.18s`

What this still locks:

- the bounded family seam `brief.v1 -> forecast.v1` still works
- `cli-mirofish` remains the canonical writer repo for `forecast.v1`
- `agentcy-echo` remains the canonical writer module for `forecast.v1`

## Clean external base wheel-install attempt

A clean external base install was retried from a fresh virtualenv outside the repo root using the newly built wheel after moving the upstream OASIS/CAMEL runtime behind an optional `simulation` extra.

### Command shape used

```bash
cd cli-mirofish
uv build
WHEEL=$(ls -1t dist/*.whl | head -n 1)
TMPDIR=$(mktemp -d)
python3 -m venv "$TMPDIR/venv"
. "$TMPDIR/venv/bin/activate"
pip install --upgrade pip
pip install "$WHEEL"
mkdir "$TMPDIR/outside"
cd "$TMPDIR/outside"
mirofish --help
python - <<'PY'
import app
from pathlib import Path
print(Path(app.__file__).resolve())
PY
```

### Result

- passed for base package install
- passed for installed `mirofish --help`
- passed for external `import app`

### Installed-path proof

The external import resolved to installed site-packages rather than the repo checkout:

```text
/private/var/folders/.../venv/lib/python3.12/site-packages/app/__init__.py
```

## Clean external optional simulation-extra attempt

The full upstream simulation runtime is still intentionally available only via the optional `simulation` extra.
That extra was re-tested after pinning `camel-oasis` to its exact upstream PyPI wheel URL, because normal index resolution still could not discover it reliably.

### Command shape used

#### First retry from Python 3.12

```bash
cd cli-mirofish
uv build
WHEEL=$(ls -1t dist/*.whl | head -n 1)
TMPDIR=$(mktemp -d)
python3 -m venv "$TMPDIR/venv"
. "$TMPDIR/venv/bin/activate"
pip install --upgrade pip
pip install "$WHEEL[simulation]"
```

#### Follow-up retry from Python 3.11

```bash
cd cli-mirofish
uv build
WHEEL=$(ls -1t dist/*.whl | head -n 1)
TMPDIR=$(mktemp -d)
/Users/amadad/.local/share/uv/python/cpython-3.11.10-macos-aarch64-none/bin/python3.11 -m venv "$TMPDIR/venv"
. "$TMPDIR/venv/bin/activate"
pip install --upgrade pip
pip install "$WHEEL[simulation]"
mkdir "$TMPDIR/outside"
cd "$TMPDIR/outside"
mirofish --help
python - <<'PY'
import app
import oasis
from app.utils.oasis_llm import require_simulation_runtime
require_simulation_runtime()
print(app.__file__)
print(oasis.__file__)
PY
```

### Result

- Python 3.12 attempt: failed
- Python 3.11 attempt: passed

### Exact blocker reproduced on 3.12

After restoring a clean direct wheel reference for `camel-oasis`, the remaining failure is no longer package discovery.
It is upstream Python-version incompatibility:

```text
ERROR: Package 'camel-oasis' requires a different Python: 3.12.12 not in '<3.12,>=3.10.0'
```

### Exact proof improved on 3.11

From a fresh external Python 3.11 environment outside the repo root:

- `pip install "$WHEEL[simulation]"` passed
- installed `mirofish --help` passed
- external `import app` passed from installed site-packages
- external `import oasis` passed from installed site-packages
- `require_simulation_runtime()` passed, proving the optional runtime imports are actually present

So the blocker has narrowed again: the optional simulation runtime is now externally installable and importable, but only on Python 3.11 because of the upstream `camel-oasis` interpreter constraint.

## Proof boundary

### Proven now

The following claims are now evidenced:

1. `cli-mirofish` builds successfully as the current distribution `mirofish-backend`.
2. In the repo environment, the current CLI binary `mirofish` is functional enough to render `--help`.
3. In the repo environment, the current packaged code root is still importable as `app`.
4. The additive tiny compatibility test artifact correctly locks the present distribution/import/bin contract, including the optional simulation-extra boundary.
5. In a fresh external environment, the base wheel installs successfully.
6. In a fresh external environment outside the repo root, the installed `mirofish` binary can render `--help`.
7. In a fresh external environment outside the repo root, `import app` resolves from installed site-packages.
8. In a fresh external Python 3.11 environment outside the repo root, the optional `mirofish-backend[simulation]` install succeeds.
9. In that same external Python 3.11 environment, `import oasis` succeeds and `require_simulation_runtime()` returns cleanly.
10. The current mixed canonical writer contract remains intact:
   - `writer.repo = "cli-mirofish"`
   - `writer.module = "agentcy-echo"`

### Not proven yet

The following claims are still not honest to make:

1. That the full `mirofish-backend[simulation]` install succeeds on Python 3.12.
2. That an externally installed end-to-end simulation run has been proven from that wheel.
3. That package/import/bin rename readiness is complete.
4. That any `agentcy-echo` package, import root, or installed binary exists today.

### Exact current blocker

The remaining blocking gap is no longer package discovery for the optional simulation runtime.
It is the upstream interpreter support boundary of `camel-oasis`, specifically:

- `camel-oasis 0.2.5` requires Python `<3.12`

Until that upstream Python-version boundary is changed or replaced in a later bounded task, the honest claim is:

- base package proof works on Python 3.11-3.12
- optional full simulation-runtime proof works on Python 3.11
- Python 3.12 remains a simulation-runtime blocker

## Interpretation for loop 11

This is the honest loop-11 boundary after the latest compatibility improvement:

- repo-local package/build/help/import proof exists
- the tiny compatibility regression test exists
- prior same-day narrow protocol proof still stands
- clean external base packaged install/help/import proof exists
- clean external optional simulation-runtime proof now exists on Python 3.11
- Python 3.12 still blocks the optional simulation runtime because of upstream `camel-oasis` metadata

So the current compatibility story should be stated narrowly as:

- current surfaces are still `mirofish-backend` / `app` / `mirofish`
- the family artifact contract is still `cli-mirofish` / `agentcy-echo`
- the base package proof is external and real
- the optional simulation install proof is now external and real on Python 3.11
- the remaining blocker is the upstream Python 3.12 incompatibility in `camel-oasis`, not generic package discovery and not the `app` import root

## Evidence summary

### Commands run

```bash
cd cli-mirofish && uv lock
cd cli-mirofish && uv run python -m pytest tests/test_public_surface_contract.py -q
cd cli-mirofish && uv build
cd cli-mirofish && pip install 'dist/mirofish_backend-0.1.0-py3-none-any.whl[simulation]'  # fresh Python 3.12 venv, expected failure
cd cli-mirofish && /Users/amadad/.local/share/uv/python/cpython-3.11.10-macos-aarch64-none/bin/python3.11 -m venv <tmp>/venv
cd <fresh-temp-outside-repo> && mirofish --help
cd <fresh-temp-outside-repo> && python - <<'PY'
import app
import oasis
from app.utils.oasis_llm import require_simulation_runtime
require_simulation_runtime()
print(app.__file__)
print(oasis.__file__)
PY
```

### Outcome summary

| Check | Outcome | Notes |
| --- | --- | --- |
| `uv lock` | passed | lockfile updated for direct reference metadata |
| `tests/test_public_surface_contract.py` | passed | 5 tests passed |
| `uv build` | passed | wheel and sdist built successfully |
| fresh external base wheel install | passed | installs without simulation deps |
| external installed `mirofish --help` | passed | run from outside repo root |
| external `import app` | passed | resolved from installed site-packages |
| fresh external `mirofish-backend[simulation]` install on Python 3.12 | failed | blocked on upstream `camel-oasis` Python `<3.12` requirement |
| fresh external `mirofish-backend[simulation]` install on Python 3.11 | passed | optional simulation runtime installed cleanly |
| external `import oasis` on Python 3.11 | passed | resolved from installed site-packages |
| `require_simulation_runtime()` on Python 3.11 | passed | optional runtime imports available |

## Bottom line

The current loop-11 proof boundary is still exact and narrow, but it is stronger than before:

- proven: current repo-local `mirofish-backend` / `app` / `mirofish` compatibility surfaces, external base wheel install/help/import proof, and external optional simulation-runtime install/import proof on Python 3.11
- blocked: Python 3.12 compatibility for the optional simulation runtime, due to the reproduced upstream `camel-oasis` interpreter constraint

That means the family can now honestly claim a bounded external full simulation-extra install proof on Python 3.11, while still refusing to overclaim Python 3.12 simulation support or any rename-ready package/import/bin story.
