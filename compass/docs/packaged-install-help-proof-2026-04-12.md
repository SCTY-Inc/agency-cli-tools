# brand-os packaged install/help proof — 2026-04-12

Scope: bounded loop-10 proof for the exact shipped package/install surface of `brand-os` from outside the repo root.

## Outcome summary

This loop currently ships the following public Python/package surface:

- Python distribution/package name: `brand-os`
- Python import path: `brand_os`
- Installed operator-facing CLI: `brandos`

Verified now:
- `cd brand-os && uv build` succeeds after narrowing sdist contents to repo-local files only
- the build no longer attempts to package external absolute symlink targets from shared config directories
- an external wheel install works from a temp directory outside `/Users/amadad/projects/brand-os`
- the installed command and import surface behave honestly as `brandos` and `brand_os`
- the canonical family writer claim remains `brief.v1.writer = { repo: "brand-os", module: "agentcy-compass" }`; this packaging proof does not alter that mixed contract

Not claimed by this proof:
- no literal repo rename
- no package rename away from `brand-os`
- no import-path rename away from `brand_os`
- no installed alias such as `agentcy-compass` or `compass`
- no claim that broader repo scope is already narrowed to future `agentcy-compass`
- no claim that runtime/env/data-path compatibility work is complete

## Packaging blocker removed

Before this change, `uv build` failed while constructing the source distribution because Hatch tried to include repo dot-directories containing absolute symlinks to shared files outside the repo.

Observed failure before the fix:

```text
Building source distribution...
  × Failed to build `/Users/amadad/projects/brand-os`
  ├─▶ Invalid tar file
  ├─▶ failed to unpack
  │   `/Users/amadad/.cache/uv/sdists-v9/.../brand_os-0.1.0/.claude/commands/de-slop.md`
  ╰─▶ symlink path `/Users/amadad/projects/agents/_commands/de-slop.md` is absolute, but external symlinks are not allowed
```

Minimum fix applied:
- added `[tool.hatch.build.targets.sdist]` exclusions in `brand-os/pyproject.toml` for repo-local tool/config/cache directories that should not ship in the package artifact

## Exact commands run

### 1) Repo-local blocker reproduction before the fix

```bash
cd /Users/amadad/projects/brand-os
uv build
```

This failed with the external-symlink packaging error quoted above.

### 2) Repo-local verification after the fix

```bash
cd /Users/amadad/projects/brand-os
uv build
```

Observed result:

```text
Building source distribution...
Building wheel from source distribution...
Successfully built dist/brand_os-0.1.0.tar.gz
Successfully built dist/brand_os-0.1.0-py3-none-any.whl
```

## External verification environment

All install/run checks below were executed from a temp directory outside `/Users/amadad/projects/brand-os`.

- temp directory: `/tmp/brand-os-proof-p5RUy1`
- installed binary path: `/tmp/brand-os-proof-p5RUy1/venv/bin/brandos`
- installed import path: `/tmp/brand-os-proof-p5RUy1/venv/lib/python3.12/site-packages/brand_os/__init__.py`

### 3) Create a temp environment outside the repo and install the built wheel

```bash
cd /Users/amadad/projects/brand-os
PROOF_ROOT=$(mktemp -d /tmp/brand-os-proof-XXXXXX)
python3 -m venv "$PROOF_ROOT/venv"
. "$PROOF_ROOT/venv/bin/activate"
pip install --upgrade pip >/dev/null
pip install /Users/amadad/projects/brand-os/dist/brand_os-0.1.0-py3-none-any.whl
cd "$PROOF_ROOT"
```

This install path deliberately used the built wheel from outside the source tree rather than `uv run`, `python -m brand_os`, or any repo-local invocation path.

### 4) Prove the shipped command surface from the external temp directory

#### 4a) Confirm current working directory is outside the repo

```bash
pwd
```

Output:

```text
/tmp/brand-os-proof-p5RUy1
```

#### 4b) Confirm the installed `brandos` binary is the one being executed

```bash
which brandos
```

Output:

```text
/tmp/brand-os-proof-p5RUy1/venv/bin/brandos
```

#### 4c) `python -c "import brand_os"` smoke test

```bash
python -c 'import brand_os; print(brand_os.__file__)'
```

Output:

```text
/tmp/brand-os-proof-p5RUy1/venv/lib/python3.12/site-packages/brand_os/__init__.py
```

Interpretation:
- `import brand_os` remains unchanged and works from the installed package
- this is a compatibility smoke test only, not an import-path rename

#### 4d) `brandos --help`

```bash
brandos --help
```

Output:

```text
Usage: brandos [OPTIONS] COMMAND [ARGS]...

CLI-first brand operations toolkit.
```

Observed command groups included `version`, `persona`, `intel`, `signals`, `plan`, `produce`, `eval`, `publish`, `queue`, `monitor`, `loop`, `decision`, `policy`, `learn`, `brand`, and `config`.

#### 4e) `brandos version`

```bash
brandos version
```

Output:

```text
brandos v0.1.0
```

Interpretation:
- the installed CLI remains `brandos`
- the current proof does not claim a future family-name binary

#### 4f) `brandos plan --help`

```bash
brandos plan --help
```

Output:

```text
Usage: brandos plan [OPTIONS] COMMAND [ARGS]...

Campaign planning commands.
```

Observed subcommands included `research`, `strategy`, `creative`, `activation`, `run`, `list`, and `resume`.

## Acceptance-matrix readout

| Surface | Result |
| --- | --- |
| repo-local `uv build` succeeds | yes |
| build avoids packaging external symlinked config dirs | yes |
| local packaged install succeeds outside repo root | yes |
| `brandos --help` | yes |
| `brandos version` | yes |
| `brandos plan --help` | yes |
| `python -c "import brand_os"` | yes |
| repo/package/import/bin rename introduced | no |
| source-tree invocation required | no |

## Relationship to the other loop-10 proof notes

This document is intentionally narrow.

Use it together with:

- `docs/rename-blocker-profile-2026-04-12.md` for the naming-only vs boundary-only vs mixed blocker split and the unresolved-before-rename list
- `docs/runtime-prefix-inventory-2026-04-12.md` for the still-mixed `.brand-os` / `.brandos` and `BRANDOS_*` / `BRANDOPS_*` runtime compatibility surface
- `docs/cli-surface-proof-2026-04-12.md` for deterministic repo-local checks that lock the current `brandos` help/version/command-tree truth without claiming a rename

Taken together, the loop-10 proof set says:

- packaged install/help readiness is proven for the current shipped names
- canonical `brief.v1` ownership is already settled
- rename-readiness is still blocked for broader package/import/CLI/runtime/boundary reasons

## Final interpretation

This proof shows that the currently shipped `brand-os` package can be built, installed, and exercised from outside the repo root with the exact public surface that is actually present today:

- package surface: `brand-os`
- import surface: `brand_os`
- installed CLI surface: `brandos`

This document is evidence for packaged build/install/help readiness only. It does **not** imply:
- a literal rename from `brand-os` to `agentcy-compass`
- a Python import rename away from `brand_os`
- a newly shipped installed command such as `agentcy-compass` or `compass`
