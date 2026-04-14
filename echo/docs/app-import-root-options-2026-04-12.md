# cli-mirofish app import-root options — 2026-04-12

## Scope

This is a bounded decision note for the current generic import-root blocker in `cli-mirofish`.

It explains why the current packaging contract:

- `packages = ["app"]`
- `mirofish = "app.cli:main"`

is a real rename-readiness blocker, compares the smallest honest options, chooses one next step, and explicitly forbids broad `app` import rewrites in this loop.

This note does not authorize any package, import-root, or CLI migration.

## Current facts

From `cli-mirofish/pyproject.toml`:

```toml
[project.scripts]
mirofish = "app.cli:main"

[tool.hatch.build.targets.wheel]
packages = ["app"]
```

That means the shipped wheel currently exposes top-level Python package `app`, and the installed CLI entry point resolves through `app.cli:main`.

## Why this is a real blocker

`app` is not just an internal folder name.

It is currently all of the following at once:

1. The wheel-packaged top-level import root.
2. The console-script target for the installed `mirofish` binary.
3. The repo-local import surface used by tests and scripts.
4. A parent-level family-test import surface used outside the repo.

So `app` is not merely cosmetic naming drift. It is a public and semi-public compatibility surface.

## Classified blast radius of `app`

### 1. Packaging and installed command surface

Direct defining references:

- `cli-mirofish/pyproject.toml`
  - `packages = ["app"]`
  - `mirofish = "app.cli:main"`

Impact:

- the built wheel exports `app`
- the installed binary depends on `app.cli:main`
- any future import-root change must account for both packaging and entrypoint resolution together

### 2. Repo-local code and test surface

Direct references include:

- `cli-mirofish/tests/test_cli_artifacts_and_visuals.py`
  - `from app.brief_v1 import import_brief_v1`
  - `from app.cli import ...`
  - `from app.forecast_v1 import ...`
  - `from app.config import Config`
  - `from app.run_artifacts import RunStore`
  - `from app.services.simulation_runner import ...`
  - `from app.visual_snapshots import generate_visual_snapshots`
- `cli-mirofish/scripts/run_parallel_simulation.py`
- `cli-mirofish/scripts/run_reddit_simulation.py`
- `cli-mirofish/scripts/run_twitter_simulation.py`
- `cli-mirofish/scripts/test_profile_format.py`

Impact:

- the import root is embedded across active repo-local test and script surfaces
- a rename would touch working local verification paths, not just packaging metadata

### 3. Family / parent-level seam surface

Direct references include:

- `protocols/tests/test_brief_to_forecast_v1.py`
  - `from app.brief_v1 import import_brief_v1`
  - `from app.cli import main`
  - `from app.config import Config`
  - `from app.run_artifacts import RunStore`

Impact:

- `app` already leaks beyond repo-local code into the parent family validation layer
- changing it would widen scope into a cross-repo test migration, even if runtime behavior stayed the same

### 4. Repo layout and operator-doc surface

Direct references include:

- `cli-mirofish/CLAUDE.md`
- `cli-mirofish/README.md`
- `cli-mirofish/CODEMAP.md`

Impact:

- `app/` is part of the documented layout contract for the repo
- even a no-behavior rename would create doc churn and risk overstating readiness

## Option comparison

### Option A — documented defer / no change now

Description:

- keep `packages = ["app"]`
- keep `mirofish = "app.cli:main"`
- document clearly that `app` is a real blocker to later rename-readiness
- do not introduce a new public import root in this loop

Pros:

- honest about the current shipped compatibility surface
- no risk of half-migrated package behavior
- no cross-repo import churn
- preserves the currently proven repo-local and parent-level tests
- matches the loop rule to avoid broad import-path rewrites

Cons:

- does not reduce the blocker yet
- future rename work still needs an explicit target import root and migration plan

Honesty level:

- highest for this loop

### Option B — additive alias / shim now

Description:

- keep `app` as the packaged root
- add a second family-shaped import surface later, such as `agentcy_echo`, as a wrapper or alias
- leave the installed CLI on `mirofish` or add only a narrow parallel shim

What would have to be true for this to be credible:

- exact target import root is chosen first
- packaging can ship both roots intentionally
- tests prove both import roots work from outside the repo root
- docs explain which root is canonical versus compatibility-only

Pros:

- could reduce future migration risk if done carefully
- allows a later deprecation path instead of a flag-day cutover

Cons:

- still requires packaging changes, not just docs
- risks creating two ambiguous authorities
- easy to over-claim progress without actually proving external install/import behavior
- not bounded enough for this loop unless accompanied by a very small, explicitly verified shim task

Honesty level:

- potentially valid later, but premature in this loop

### Option C — later real migration

Description:

- choose a new import root explicitly
- move code from `app` to the new package layout
- update console entrypoints, repo-local imports, parent-level tests, scripts, and docs together
- prove external install/help/import behavior before claiming readiness

Pros:

- actually resolves the blocker
- ends the generic import-root problem cleanly

Cons:

- broad, structural migration
- touches packaging, code imports, tests, docs, and likely external assumptions together
- incompatible with the current bounded planning loop

Honesty level:

- honest only as a later dedicated migration wave, not as a small follow-up inside this loop

## Decision

The smallest honest next step is **Option A: documented defer / no change now**.

Reasoning:

1. `app` is a structural compatibility surface, not a label-only problem.
2. An additive shim is only honest after the family chooses an exact successor import root and proves external packaging behavior.
3. A real migration is too broad for the current loop.
4. The current loop is specifically supposed to separate blocker recording from rename theatre.

So the correct move here is to record `app` as the heaviest import-root blocker, keep the shipped surface unchanged, and defer any alias or migration work to a later, explicitly scoped task.

## Smallest honest next step

The next step after this note, if the family chooses to reduce the blocker later, should be:

1. Choose one exact successor import root first.
   - likely something family-aligned such as `agentcy_echo`
   - do not start by rewriting imports before this is decided
2. Design a bounded additive packaging proof task, if still desired.
   - prove whether both `app` and the new root can coexist cleanly
   - verify from outside the repo root
3. Only after that proof succeeds, decide whether a real migration is worth the churn.

This sequencing keeps the family from pretending that a generic `app` import-root problem can be solved with a casual search-and-replace.

## Explicitly forbidden in this loop

This loop does **not** authorize:

- broad `from app ...` to `from <new_root> ...` rewrites
- moving the `app/` tree to a new package root
- changing `mirofish = "app.cli:main"` in `pyproject.toml`
- changing `packages = ["app"]` in `pyproject.toml`
- updating parent-level protocol tests to a new import root
- mass-editing repo docs to imply import readiness that has not been proven

Why:

- those changes would turn a blocker-analysis task into a migration task
- they would widen scope beyond the bounded loop-11 planning surface
- they would create rename-readiness theater without external compatibility proof

## Verification evidence

Search command used:

```bash
cd /Users/amadad/projects && rg -n --hidden --glob '!**/.venv/**' --glob '!**/dist/**' --glob '!**/build/**' '\bpackages = \["app"\]|app\.cli:main|from app\.|import app\b|\bapp/' cli-mirofish protocols
```

Verification commands used:

```bash
cd cli-mirofish && uv run python -m pytest tests/test_cli_artifacts_and_visuals.py -k 'cli_parser_is_run_first or runs_export_emits_forecast_v1'
cd cli-mirofish && uv run python -m pytest ../protocols/tests/test_brief_to_forecast_v1.py
```

## Bottom line

`packages = ["app"]` plus `app.cli:main` is a real rename-readiness blocker because `app` is simultaneously the packaged import root, CLI entrypoint target, repo-local import surface, and a parent-level family-test dependency.

The smallest honest path is to document and defer the blocker now, forbid broad `app` import rewrites in this loop, and reserve any additive alias or real migration work for a later explicitly scoped task with external packaging proof.