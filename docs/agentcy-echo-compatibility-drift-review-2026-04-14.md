# agentcy-echo compatibility, attribution, and dependency-boundary drift review — 2026-04-14

Task: `task-5`
Scope: bounded reality review for current `agentcy-echo/` repo truth and still-live public surfaces around `forecast.v1`

## Bottom line

`forecast.v1` ownership should stay locked as:

```json
{ "repo": "cli-mirofish", "module": "agentcy-echo" }
```

The current repo still ships and tests the legacy compatibility surfaces:

- distribution: `mirofish-backend`
- import root: `app`
- CLI binary: `mirofish`
- upstream/open-source product naming: `MiroFish`

The strongest current blocker is still the dependency/install boundary, not artifact ownership drift. More specifically:

- base packaging/help/import proof is still in place
- `app` remains a real import-root blocker for any future rename claim, but it is not the next thing to rewrite in this task
- attribution must keep explicit upstream MiroFish fork + AGPL lineage visible
- the optional simulation runtime is still constrained by upstream `camel-oasis` support boundaries
- one family protocol test now also exposes control-plane narration drift because it still looks for `brand-os/...` after the literal repo rename to `agentcy-compass/...`

## Sources reviewed

- `_agentcy-docs/AGENTCY_STACK.md`
- `_agentcy-docs/AGENTCY_PROGRESS.md`
- `_agentcy-docs/CONSOLIDATION.md`
- `_agentcy-docs/AGENTCY_RECAP.md`
- `agentcy-echo/CLAUDE.md`
- `agentcy-echo/README.md`
- `agentcy-echo/pyproject.toml`
- `agentcy-echo/app/forecast_v1.py`
- `agentcy-echo/tests/test_public_surface_contract.py`
- `agentcy-echo/tests/test_simulation_runtime_preflight.py`
- `agentcy-echo/docs/packaged-compatibility-proof-boundary-2026-04-12.md`
- `agentcy-echo/docs/rename-readiness-scorecard-2026-04-12.md`

## Current repo truth

### Git/dirty-state snapshot

From `cd agentcy-echo && git status --short --branch`:

- branch: `main`
- tracking: `origin/main`
- ahead: `9`
- dirty tracked files include:
  - `.gitignore`
  - `CLAUDE.md`
  - `README.md`
  - `app/cli.py`
  - `app/tools/run_simulation.py`
  - `app/utils/oasis_llm.py`
  - `docs/packaged-compatibility-proof-boundary-2026-04-12.md`
  - `pyproject.toml`
  - `scripts/run_parallel_simulation.py`
  - `scripts/run_reddit_simulation.py`
  - `scripts/run_twitter_simulation.py`
  - `tests/test_cli_artifacts_and_visuals.py`
  - `tests/test_public_surface_contract.py`
  - `uv.lock`
- untracked:
  - `tests/test_simulation_runtime_preflight.py`

This review treats that dirty state as active repo reality, not noise.

### Current public/semi-public package surfaces

From `agentcy-echo/pyproject.toml` and repo tests:

- `[project].name = "mirofish-backend"`
- `[project.scripts] = { "mirofish": "app.cli:main" }`
- wheel packages remain `[`"app"`]`
- optional simulation extra remains separate from base install:
  - `camel-oasis @ <direct wheel url>`
  - `camel-ai==0.2.78`

### Current canonical artifact seam

From `agentcy-echo/app/forecast_v1.py`:

- artifact type remains `forecast.v1`
- writer remains:
  - `repo = "cli-mirofish"`
  - `module = "agentcy-echo"`

This is still aligned with the family mixed writer contract. No evidence in this review justifies changing `writer.repo` yet.

## Compatibility reality vs family framing

### Literal repo truth

The literal repo directory is now `agentcy-echo/`.

### Still-live shipped/operator truth

The shipped runtime and packaging surfaces are still:

- package/distribution: `mirofish-backend`
- import root: `app`
- binary: `mirofish`
- docs/product lineage: `MiroFish`

### What that means

The repo rename and family framing did not produce a clean public-surface migration. Instead, the current state is:

- repo directory already family-named
- artifact module already family-named
- public package/import/CLI surfaces still legacy/upstream-shaped

That is compatibility drift, but it is currently intentional and bounded. It is not yet ownership drift.

## Attribution and lineage constraints

Attribution remains a hard boundary, not optional polish.

Evidence:

- `agentcy-echo/README.md` still explicitly says this is a fork of upstream `666ghj/MiroFish`
- `agentcy-echo/CLAUDE.md` says the repo is a fork of upstream MiroFish and translated to English
- `agentcy-echo/pyproject.toml` keeps:
  - author: `MiroFish Team`
  - license: `AGPL-3.0`
- README acknowledgments still name both upstream MiroFish and OASIS

Interpretation:

- any future `agentcy-echo` package/import/bin story must preserve visible upstream attribution
- family docs should not narrate this repo as if it were a clean-room family-native runtime
- AGPL-aware lineage is a real boundary on rename theater and dependency laundering

## Dependency-boundary findings

### Base package path

The repo-local compatibility tests still pass for the current contract:

```bash
cd agentcy-echo && uv run python -m pytest tests/test_public_surface_contract.py tests/test_simulation_runtime_preflight.py -q
```

Observed result:

- `8 passed`

This supports the still-live contract that:

- base package/import/bin surfaces are intentional
- simulation dependencies remain optional
- Python 3.12 is explicitly rejected for the optional simulation runtime before import checks

### Simulation/runtime boundary

The current docs and tests agree on the main dependency seam:

- base package works on Python 3.11-3.12
- optional simulation runtime depends on upstream `camel-oasis`
- `camel-oasis 0.2.5` remains the controlling upstream constraint
- the package keeps a direct wheel URL pin to preserve installability

This means the repo is not blocked first by package naming. It is blocked first by honest simulation-runtime install proof boundaries.

## Import-root findings

`app` is still a real blocker, but not the newest one.

Evidence:

- wheel packages are still `app`
- console script still resolves via `app.cli:main`
- tests still import `app` directly
- README setup still describes external `import app` proof

Interpretation:

- `app` remains the heaviest rename-readiness/import-root blocker
- but current evidence does not say “rewrite imports now”
- current evidence says “keep documenting `app` as a real compatibility surface until a separate bounded migration task exists”

## Verification findings from this task

### Passing check

```bash
cd agentcy-echo && uv run python -m pytest tests/test_public_surface_contract.py tests/test_simulation_runtime_preflight.py -q
```

Result:

- passed

### Family seam check with live failure

```bash
cd agentcy-echo && uv run python -m pytest ../protocols/tests/test_brief_to_forecast_v1.py ../protocols/tests/test_forecast_v1_protocol.py -q
```

Result:

- failed: `1 failed, 3 passed`

Failure observed:

- `test_brand_os_mirror_brief_also_round_trips_through_forecast_export`
- looked for:
  - `/Users/amadad/projects/brand-os/tests/fixtures/brief.v1.rich.mirror.json`
- current workspace reality has the renamed repo path `agentcy-compass/`, not `brand-os/`

Interpretation:

- this failure does **not** show `forecast.v1` writer drift
- it does **not** show packaging failure inside `agentcy-echo`
- it does show a live control-plane narration / path-reference drift in family protocol tests after repo renames

## Classification

### Ownership / writer seam

Status: aligned

- keep `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`
- no bounded evidence here supports changing canonical writer ownership

### Package/distribution surface

Status: intentionally legacy-compatible

- `mirofish-backend` remains live
- still proven enough for current bounded compatibility story
- not family-renamed

### Import-root surface

Status: real blocker, unchanged

- `app` remains public/semi-public
- rename-readiness still blocked here
- no rewrite justified by this task

### CLI surface

Status: intentionally legacy-compatible

- `mirofish` remains live and documented
- no family-name installed alias is proven here

### Attribution

Status: must preserve

- explicit MiroFish fork story and AGPL lineage remain required
- cannot be collapsed into generic family branding

### Dependency/install proof

Status: strongest active blocker class inside repo-local compatibility

- base install/help/import story is okay
- optional simulation runtime still depends on upstream `camel-oasis` boundary
- this remains more concrete than any package-name choice question

### Control-plane narration

Status: live family drift outside the repo-local writer seam

- at least one family protocol test still hardcodes `brand-os/...`
- this is the clearest newly observed drift from today’s verification pass

## Best next blocker call

If forced to name the single next blocker category, it is:

**control-plane narration**, with a close second of **dependency/install proof**.

Why control-plane narration wins in today’s live run:

- the repo-local compatibility tests passed
- the writer seam is still aligned
- the protocol-family verification failure came from stale renamed-path narration (`brand-os` vs `agentcy-compass`)

Why dependency/install proof is still the next repo-local blocker behind that:

- the optional simulation runtime remains bounded by upstream `camel-oasis`
- that is still the main honest blocker before any stronger public compatibility claim

Why package/import-root do **not** win as the next blocker here:

- package surface is already intentionally locked to `mirofish-backend`
- import root `app` is a known blocker, but not the one that failed this task’s live verification

## Recommended bounded follow-ups

1. Fix family protocol/path narration so renamed repos are referenced consistently in parent-level tests and docs.
2. Keep `forecast.v1.writer` unchanged until a deliberate writer-contract task says otherwise.
3. Keep explicit MiroFish + AGPL attribution in any family-facing docs about `agentcy-echo`.
4. Treat any future import-root work (`app` replacement or aliasing) as a separate bounded migration task with external package proof.
5. Keep dependency/install proof focused on the optional simulation runtime boundary rather than broad package renaming.

## Evidence

Commands run:

```bash
cd agentcy-echo && git status --short --branch
cd agentcy-echo && git branch --show-current
cd agentcy-echo && git diff --stat
cd agentcy-echo && uv run python -m pytest tests/test_public_surface_contract.py tests/test_simulation_runtime_preflight.py -q
cd agentcy-echo && uv run python -m pytest ../protocols/tests/test_brief_to_forecast_v1.py ../protocols/tests/test_forecast_v1_protocol.py -q
```
