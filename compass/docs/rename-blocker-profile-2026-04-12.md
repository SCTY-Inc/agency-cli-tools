# `brand-os` loop-10 rename blocker profile

Date: 2026-04-12  
Scope: authoritative repo-local blocker profile for the active loop-10 `brand-os` / future `agentcy-compass` slice.

## Purpose

This document replaces any fuzzy “rename readiness” story with a narrower and more honest one:

- `brand-os` is already the canonical writer for `brief.v1`
- the repo is **not** rename-ready overall
- the blockers split across three distinct buckets:
  - **naming-only**
  - **boundary-only**
  - **mixed**
- the unresolved-before-rename list must stay first-class until the blockers are reduced with bounded follow-up work

Loop 10 is therefore about blocker decomposition and evidence, not about performing a repo rename, package rename, import rewrite, CLI migration, or runtime-prefix migration.

## Executive summary

`brand-os` remains the canonical writer for `brief.v1` with:

```json
{
  "repo": "brand-os",
  "module": "agentcy-compass"
}
```

That part is already correct and should not be reopened.

What is still blocked is the rest of the repo surface. The hardest part is that `brand-os` is not blocked by naming alone. It is blocked by a mix of:

1. broad public naming surfaces still using `brand-os` / `brand_os` / `brandos`
2. inconsistent runtime/env/data-path prefixes
3. boundary drift across `persona`, `produce`, `eval`, `publish`, `queue`, `monitor`, and `server`
4. residual `cli-agency` lineage and selective re-home history

The critical loop-10 distinction is:

- `brief.v1` writer ownership is already settled
- broader repo ownership is not yet compass-shaped
- residual `cli-agency` entanglement is a **boundary/ownership drift** problem, not a naming drift problem

## Canonical artifact ownership vs broader repo surface

### Canonical ownership that is already locked

`brief.v1` is the only family-critical writer surface that this repo currently owns canonically.

Evidence:

- `src/brand_os/plan/brief_v1.py`
- `tests/plan/test_brief_v1.py`
- `tests/fixtures/brief.v1.rich.mirror.json`
- parent family docs in `AGENTCY_STACK.md` and `AGENTCY_RECAP.md`

Canonical state:

- `writer.repo = "brand-os"`
- `writer.module = "agentcy-compass"`

Interpretation:

- this is already aligned with the family control plane
- this should remain stable until a literal repo rename is authorized and actually lands
- loop 10 must not blur this stable artifact ownership with the messier repo-wide surface inventory below

### Broader repo surfaces that are not canonical `agentcy-compass` proof

These surfaces exist in the repo today, but they should be treated as broader repo scope rather than proof that the repo is already narrowed to future `agentcy-compass` ownership:

- `persona`
- `produce`
- `eval`
- `publish`
- `queue`
- `monitor`
- `server`

Representative evidence:

- `src/brand_os/persona/`
- `src/brand_os/produce/`
- `src/brand_os/eval/`
- `src/brand_os/publish/`
- `src/brand_os/monitor/`
- `src/brand_os/server/api.py`
- `src/brand_os/cli.py`
- `README.md`
- `CLAUDE.md`

These do **not** invalidate canonical `brief.v1` ownership. They do block any honest claim that the full repo is already shaped like `agentcy-compass`.

## Surface-by-surface blocker profile

| Surface | Current state | Class | Why it blocks rename honesty |
| --- | --- | --- | --- |
| Repo directory | `brand-os` | naming-only | Literal repo identity is still `brand-os`; must stay separate from other migrations |
| Python distribution/package | `brand-os` | naming-only | `pyproject.toml` still publishes `brand-os`; install surface is unchanged |
| Import root | `brand_os` | naming-only | Real Python compatibility surface used across code, tests, and packaging |
| CLI binary | `brandos` | mixed | Public command name is old-brand shaped and the command tree still exposes broad non-compass groups |
| Runtime path prefixes | `.brand-os` and `.brandos` | mixed | Prefixes are inconsistent and tied to live filesystem behavior |
| Env/config prefixes | `BRANDOS_*` and `BRANDOPS_*` | mixed | Naming inconsistency overlaps active config/runtime compatibility |
| Data-path defaults | `~/.brandos`, `~/.brand-os`, `brandos.yml` | mixed | Persisted path conventions exist already and need compatibility policy |
| Repo boundary ownership | `persona`, `produce`, `eval`, `publish`, `queue`, `monitor`, `server` | boundary-only | Broader than future `agentcy-compass` ownership |
| Residual `cli-agency` entanglement | selective re-home history inside planning stages | boundary-only | Historical narrowing is incomplete; this is ownership drift, not naming drift |

## Detailed blocker classification

### 1. Repo directory surface

Current canonical surface:

- repo directory: `brand-os`

Primary evidence:

- repository name and URLs in `pyproject.toml`
- family control-plane docs

Classification: **naming-only**

Why:

- the repo can keep shipping canonical `brief.v1` without changing the directory name
- a literal repo rename is a separate decision from package, import, CLI, runtime, or boundary changes
- no repo-level rename should be implied by the already-correct `writer.module = "agentcy-compass"`

### 2. Python distribution/package surface

Current canonical surface:

```toml
[project]
name = "brand-os"
```

Primary evidence:

- `pyproject.toml`

Classification: **naming-only**

Why:

- this is mainly an install/distribution identity question
- package naming can only be changed honestly after explicit operator-path proof and migration guidance
- it does not itself prove or solve repo boundary narrowing

### 3. Import-root surface

Current canonical surface:

- package root: `src/brand_os`
- imports across repo: `from brand_os ...`
- wheel packaging: `packages = ["src/brand_os"]`

Primary evidence:

- `pyproject.toml`
- `src/brand_os/...`
- `tests/...`

Classification: **naming-only**

Why:

- this is still fundamentally a naming surface
- but it is the heaviest naming surface because it touches actual Python compatibility
- it must remain separate from repo/package/CLI storytelling and cannot be smuggled into a cosmetic rename claim

### 4. CLI binary surface

Current canonical surface:

```toml
[project.scripts]
brandos = "brand_os.cli:app"
```

```python
app = typer.Typer(
    name="brandos",
    help="CLI-first brand operations toolkit.",
    no_args_is_help=True,
)
```

And the current top-level command tree includes:

- `persona`
- `intel`
- `signals`
- `plan`
- `produce`
- `eval`
- `publish`
- `queue`
- `monitor`
- `loop`
- `decision`
- `policy`
- `learn`
- `brand`
- `config`

Primary evidence:

- `pyproject.toml`
- `src/brand_os/cli.py`
- `README.md`
- `CLAUDE.md`

Classification: **mixed**

Why:

- the binary name `brandos` is a naming surface
- but the currently exposed command tree also reflects a broader-than-compass repo boundary
- therefore the blocker is not only “rename the binary”; it is also “stop overstating the binary as already compass-shaped”

### 5. Runtime path surface

Current observed surfaces:

- `~/.brand-os` via `BRANDOS_DATA_DIR` fallback in `src/brand_os/core/storage.py`
- `~/.brandos` default config/data path in `src/brand_os/core/config.py`

Primary evidence:

- `src/brand_os/core/storage.py`
- `src/brand_os/core/config.py`

Classification: **mixed**

Why:

- the prefixes are naming surfaces
- but they are also active runtime and persistence surfaces with compatibility consequences
- the repo is not even internally uniform yet, which makes future rename claims less credible without a compatibility plan

### 6. Env/config prefix surface

Current observed surfaces:

- `BRANDOS_DATA_DIR`
- `BRANDOPS_CONFIG`
- `BRANDOPS_<KEY>`

Primary evidence:

- `src/brand_os/core/storage.py`
- `src/brand_os/core/config.py`

Classification: **mixed**

Why:

- the inconsistent prefixes are naming drift
- but env vars are part of the active runtime contract, so changing them would be migration work, not just branding cleanup
- loop 10 should inventory these, not normalize them yet

### 7. Data-path and config-file surface

Current observed surfaces:

- `~/.brandos/config.yml`
- `brandos.yml`
- `~/.brandos`
- `~/.brand-os`
- repo-local brand data directories under `brands/`

Primary evidence:

- `src/brand_os/core/config.py`
- `src/brand_os/core/storage.py`
- repo docs and CLI behavior

Classification: **mixed**

Why:

- these are visible naming surfaces
- they also define where operators already keep state and configuration
- any future rename would need deterministic compatibility rules and migration tests before it becomes credible

### 8. Boundary ownership surface

Current broader repo-owned groups:

- `persona`
- `produce`
- `eval`
- `publish`
- `queue`
- `monitor`
- `server`

Primary evidence:

- `src/brand_os/cli.py`
- `src/brand_os/persona/`
- `src/brand_os/produce/`
- `src/brand_os/eval/`
- `src/brand_os/publish/`
- `src/brand_os/monitor/`
- `src/brand_os/server/`
- `README.md`
- `CLAUDE.md`

Classification: **boundary-only**

Why:

- this is not mainly a naming problem
- this is the repo still exposing surfaces that extend beyond future `agentcy-compass` scope
- loop 10 should keep these visible as ownership drift rather than pretending a rename would solve them

### 9. Residual `cli-agency` entanglement

Current evidence:

- `src/brand_os/plan/stages/strategy.py` explicitly says it selectively re-homes durable strategy concepts from `cli-agency`
- planning stages still frame the work as a selective re-home rather than a cleanly isolated new boundary
- family docs already lock `cli-agency` as source material, not a second `brief.v1` writer

Primary evidence:

- `src/brand_os/plan/stages/strategy.py`
- `AGENTCY_RECAP.md`
- `AGENTCY_STACK.md`
- `AGENTCY_PROGRESS.md`
- historical `cli-agency` scorecard references in family docs

Classification: **boundary-only**

Why:

- the problem is not the string `cli-agency`
- the problem is lingering ownership/history drift and incomplete narrowing
- this must be recorded as a boundary/ownership issue, not misfiled as a naming issue

## Unresolved-before-rename list

This section is the first-class loop-10 gate. No credible rename story should bypass it.

### Must remain unresolved until explicitly addressed

1. **Repo boundary remains broader than future `agentcy-compass`.**  
   `brand-os` still exposes `persona`, `produce`, `eval`, `publish`, `queue`, `monitor`, and `server` surfaces beyond the canonical `brief.v1` strategy/policy/brief seam.

2. **`cli-agency` narrowing is incomplete at the boundary layer.**  
   Selective re-home evidence exists, but the repo still carries legacy lineage and ownership ambiguity in planning-stage concepts.

3. **Package, import, and CLI surfaces are still current-brand shaped.**  
   `brand-os`, `brand_os`, and `brandos` remain the real public/operator/developer surfaces.

4. **Runtime/env/data-path prefixes are inconsistent today.**  
   The repo already mixes `.brand-os`, `.brandos`, `BRANDOS_*`, and `BRANDOPS_*`, so future migration policy cannot be inferred from a doc rename.

5. **CLI scope is broader than future module scope.**  
   Even if a future alias were added, the command tree still exposes broader repo responsibilities rather than a narrowly compass-shaped interface.

6. **No compatibility policy has been proven yet for rename-adjacent runtime surfaces.**  
   There is not yet a deterministic policy for config-file lookup, env fallback order, persisted data lookup, or CLI alias behavior across legacy names.

7. **No public rename claim should be made from `writer.module` alone.**  
   `writer.module = "agentcy-compass"` is already correct, but it does not imply repo/package/import/CLI/runtime readiness.

## Bounded proof already landed in loop 10

The blocker profile should be read together with the two bounded proof notes that now exist for this repo:

- `docs/packaged-install-help-proof-2026-04-12.md` proves the current shipped package/install/help surface from outside the repo root and confirms the honest current names are still package `brand-os`, import `brand_os`, and CLI `brandos`
- `docs/runtime-prefix-inventory-2026-04-12.md` inventories the current runtime/env/data-path compatibility surface and confirms the still-mixed `.brand-os`, `.brandos`, `BRANDOS_*`, and `BRANDOPS_*` reality

Together with the canonical `brief.v1` tests and fixtures, the bounded loop-10 evidence now says:

- current surfaces are documented as they actually ship today
- canonical `brief.v1.writer = { repo: "brand-os", module: "agentcy-compass" }` remains locked
- unresolved-before-rename blockers remain first-class and are not erased by packaged help proof or runtime inventory work

## Smallest honest follow-ups after this profile

These are acceptable next steps only if kept narrow and evidence-first:

1. **Package/import/CLI current-surface proof**  
   Capture exact current package metadata, import root, installed script, and help output without claiming a rename or forcing code churn.

2. **Runtime/env/data-path compatibility inventory**  
   Capture exact prefixes, path defaults, env lookup order, and persisted-state implications without performing migration work.

3. **Boundary scorecard tightening**  
   Keep `brief.v1` writer ownership explicit while documenting which broader repo groups are still outside future `agentcy-compass` scope.

Not acceptable in loop 10:

- literal repo rename
- import-path rewrite
- runtime-prefix migration
- umbrella CLI redesign
- broad boundary rewrite
- monolith move
- MCP-first integration

## Validation commands

Read-only validation commands for this blocker profile:

```bash
cd brand-os && rg -n 'name = "brand-os"|brandos = "brand_os\.cli:app"|packages = \["src/brand_os"\]' pyproject.toml
cd brand-os && rg -n 'name="brandos"|app.add_typer\(|persona|produce|eval|publish|queue|monitor|server' src/brand_os/cli.py
cd brand-os && rg -n 'repo: Literal\["brand-os"\]|module: Literal\["agentcy-compass"\]|brief\.v1' src/brand_os/plan/brief_v1.py tests/plan/test_brief_v1.py tests/fixtures/brief.v1.rich.mirror.json
cd brand-os && rg -n '\.brand-os|\.brandos|BRANDOS_|BRANDOPS_|brandos\.yml' src/brand_os/core/config.py src/brand_os/core/storage.py
cd brand-os && rg -n 'cli-agency|re-home|brief\.v1 writer|agentcy-compass' src/brand_os/plan/stages/strategy.py docs/ownership-scorecard-2026-04-12.md
```

Optional repo-local verification command for the canonical writer seam:

```bash
cd brand-os && PYTHONPATH=src ../cli-prsna/.venv/bin/python -m pytest tests/plan/test_brief_v1.py
```

## Bottom line

The authoritative loop-10 position is:

- `brand-os` already has the right canonical `brief.v1` writer contract
- the repo is not rename-ready overall
- the blockers span naming-only, boundary-only, and mixed surfaces
- `cli-agency` residue is a boundary/ownership issue, not a naming issue
- the unresolved-before-rename list must stay first-class until bounded follow-up evidence reduces it

Any future rename proposal that collapses these surfaces into a single “rename readiness” claim would be overstating the current state.