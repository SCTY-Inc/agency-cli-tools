# brand-os rename-readiness audit for future `agentcy-compass`

Date: 2026-04-12  
Scope: loop-7 repo-local audit of naming surfaces and boundary blockers in `brand-os` without changing names yet.

## Outcome

`brand-os` is aligned on the canonical family artifact-writer contract for `brief.v1`:

```json
{
  "repo": "brand-os",
  "module": "agentcy-compass"
}
```

That alignment is already encoded in `src/brand_os/plan/brief_v1.py` via `BriefWriter` and exercised in `tests/plan/test_brief_v1.py`.

Everything else in the repo is intentionally mixed and is exactly why this is the highest-risk rename-readiness audit in loop 7:

- repo directory still uses `brand-os`
- Python distribution name is still `brand-os`
- import path is still `brand_os`
- installed CLI binary is still `brandos`
- README and CLAUDE still present `brandOS` / `brandos` as the public product
- the repo still owns or exposes cross-boundary groups that are not fully compass-shaped: `persona`, `produce`, `eval`, `publish`, `queue`, `monitor`, `server`
- some planning concepts were selectively re-homed from `cli-agency`, but overlap with `cli-agency` is still a real boundary blocker

Loop 7 should classify those surfaces honestly, not rename them.

## Current canonical surfaces

### Canonical artifact writer alignment

Sources:

- `brand-os/src/brand_os/plan/brief_v1.py`
- `brand-os/tests/plan/test_brief_v1.py`
- `brand-os/README.md`

Current canonical writer:

```python
class BriefWriter(BaseModel):
    repo: Literal["brand-os"] = "brand-os"
    module: Literal["agentcy-compass"] = "agentcy-compass"
```

Interpretation:

- `writer.repo` correctly remains the current repo name `brand-os`
- `writer.module` correctly carries the future family module `agentcy-compass`
- this already matches the loop-7 family invariant and should stay stable until any literal repo rename lands

### Repo directory surface

- current canonical: `brand-os`
- this remains the current repo authority in family docs, task taxonomy, and writer fields
- any future repo rename must be treated separately from package, import-path, and CLI rename decisions

### Python distribution/package manifest surface

Source: `brand-os/pyproject.toml`

```toml
[project]
name = "brand-os"
```

Interpretation:

- install/distribution naming is still `brand-os`
- no `agentcy-compass` distribution alias exists yet
- package metadata still describes a broad standalone brand-operations tool, not a narrowed strategy/policy/brief module

### Python import-path surface

Sources:

- `brand-os/pyproject.toml` -> `packages = ["src/brand_os"]`
- repo imports and tests -> `from brand_os ...`
- package root -> `brand-os/src/brand_os/`

Interpretation:

- the internal module/import contract is still firmly `brand_os`
- this is a real implementation surface, not just branding
- import-path rename risk is much larger than repo/package/CLI branding changes because it touches code, tests, examples, and downstream consumers

### CLI binary and command surface

Sources:

- `brand-os/pyproject.toml`
- `brand-os/src/brand_os/cli.py`
- `brand-os/README.md`
- `brand-os/CLAUDE.md`

Current canonical CLI surface:

```toml
[project.scripts]
brandos = "brand_os.cli:app"
```

And in the Typer app:

```python
app = typer.Typer(
    name="brandos",
    help="CLI-first brand operations toolkit.",
    no_args_is_help=True,
)
```

Interpretation:

- installed command is `brandos`
- command examples across docs consistently use `brandos ...`
- CLI branding is public and user-facing, but still reflects the broad pre-family product surface

### README and install-branding surface

Sources:

- `brand-os/README.md`
- `brand-os/CLAUDE.md`

Current canonical branding patterns:

- repo title and prose heavily use `brandOS`, `brand-os`, and `brandos`
- docs now explicitly acknowledge that `brand-os` is the canonical writer for `brief.v1`
- docs still present the repo as an all-in-one brand operations toolkit spanning planning plus downstream execution-adjacent surfaces
- quick-start and command references still foreground `persona`, `produce`, `eval`, `publish`, `queue`, and `monitor` under the same tool banner

Interpretation:

- docs are family-aware at the artifact layer
- docs are not family-renamed at the product/package/CLI layer
- docs also expose the underlying boundary-readiness problem: this repo still presents itself as broader than future `agentcy-compass`

### Runtime path and key-prefix surface

Observed runtime/storage naming:

- `~/.brand-os/...` in `src/brand_os/actions/write.py`
- `~/.brandos/...` and `BRANDOS_DATA_DIR` / `brandos.yml` in `src/brand_os/core/config.py` and `src/brand_os/core/storage.py`

Interpretation:

- runtime naming is not yet even internally uniform across `brand-os` vs `brandos`
- this is an additional blocker for a clean future rename because filesystem/config prefixes would need an explicit compatibility policy

## Boundary blockers that make the repo not fully compass-shaped

The naming audit is inseparable from ownership drift in this repo. These groups are real and documented, but they exceed the intended `agentcy-compass` boundary:

- `persona`
- `produce`
- `eval`
- `publish`
- `queue`
- `monitor`
- `server`

### Why these matter

Per `AGENTCY_RECAP.md`, future `agentcy-compass` should own:

- signals
- policy decisions
- briefs
- approvals/escalations
- strategy/policy learning

But `brand-os` still exposes:

- persona authoring/export/drift/optimization under `src/brand_os/persona/`
- content production under `src/brand_os/produce/`
- evaluation under `src/brand_os/eval/`
- social publishing and queue ownership under `src/brand_os/publish/`
- reporting/monitoring under `src/brand_os/monitor/`
- API/MCP surfaces under `src/brand_os/server/`

These groups do not block the existing `brief.v1` writer contract, but they do block an honest claim that the repo as a whole is already shaped like `agentcy-compass`.

## Unresolved overlap with `cli-agency`

The repo has selective, bounded re-home evidence, but not clean isolation yet.

Sources:

- `src/brand_os/plan/stages/research.py`
- `src/brand_os/plan/stages/strategy.py`
- parent-level loop-4 notes in `AGENTCY_PROGRESS.md`
- `cli-agency/docs/re-home-candidate-scorecard-2026-04-12.md`

Current state:

- `brand-os` planning stages explicitly mention selective re-homing of durable `cli-agency` research and strategy concepts
- the family has already decided `cli-agency` is source material to narrow/re-home, not a second `brief.v1` authority
- that decision helps the canonical writer contract, but it also proves the repo is still boundary-sensitive and historically entangled with `cli-agency`

Conclusion:

- `cli-agency` no longer blocks canonical `brief.v1` writer alignment
- it does still block repo-level rename honesty, because `brand-os` is not yet cleanly perceived as a standalone strategy/policy/brief layer divorced from broader legacy agency logic

## Post-rename target surfaces

These are likely future targets if a later wave authorizes naming changes. This section is directional only and does not authorize a rename now.

| Surface | Current canonical | Post-rename target |
| --- | --- | --- |
| artifact writer module | `agentcy-compass` | `agentcy-compass` |
| artifact writer repo | `brand-os` | `agentcy-compass` only after a literal repo rename |
| repo directory | `brand-os` | `agentcy-compass` |
| Python distribution name | `brand-os` | likely `agentcy-compass` |
| import path | `brand_os` | maybe `agentcy_compass` or another explicit import path, but not automatically implied |
| CLI binary | `brandos` | likely `agentcy-compass` and/or `compass` |
| docs/install branding | `brandOS` / `brand-os` / `brandos` | `agentcy-compass` with explicit legacy guidance |
| runtime paths and env prefixes | `.brand-os`, `.brandos`, `BRANDOS_*` | explicit future compass-prefixed policy only after compatibility planning |

Important distinction:

- `writer.module = agentcy-compass` is already on target
- `writer.repo = brand-os` must stay as-is until the repo is actually renamed
- import-path and runtime-prefix targets are intentionally unresolved because public rename work must not smuggle in deeper migration churn

## Acceptable legacy aliases

Loop 7 should preserve room for compatibility layers. The following legacy names are acceptable aliases after any future public rename, subject to later implementation work.

### Repo and docs aliases

- `brand-os` as the historical repo name in migration notes and lineage docs
- `brandOS` as a historical product/style reference in docs and release notes

### Package/distribution aliases

- `brand-os` as a compatibility install surface for some transition period if an `agentcy-compass` package is later introduced

### CLI aliases

- `brandos` is the strongest legacy CLI alias candidate because all current docs and workflows depend on it
- a future `agentcy-compass` or `compass` command should not require immediate removal of `brandos`

### Import-path aliases

- `brand_os` import path should be treated as a long-lived compatibility surface if import renaming ever happens at all
- unlike repo/package/CLI naming, import aliases protect existing Python consumers and test fixtures

### Runtime/storage aliases

- `.brand-os`, `.brandos`, and `BRANDOS_*` should be treated as compatibility surfaces if runtime prefixes are ever normalized
- no future rename should assume existing local data/config directories can be broken without a migration plan

## Hard blockers by rename surface

### 1. Repo rename blockers

A literal repo rename from `brand-os` to `agentcy-compass` is blocked by more than branding:

1. the repo still presents a broad product boundary spanning strategy plus persona, production, evaluation, publishing, monitoring, and server surfaces
2. README and CLAUDE still market the repo as a full-stack brand operations toolkit rather than a narrowed strategy/policy/brief module
3. unresolved historical overlap with `cli-agency` still makes ownership perception messy even though canonical `brief.v1` writer authority is locked

Conclusion:

- repo rename is blocked mainly by boundary honesty, not by the `brief.v1` contract

### 2. Package/distribution rename blockers

1. `pyproject.toml` still publishes `name = "brand-os"`
2. optional dependency groups and package metadata are still framed around the broader tool surface
3. install/docs examples all assume `brand-os` as the package identity

Conclusion:

- package rename is plausible later, but it needs install-surface migration planning and should not happen before the repo boundary is narrower

### 3. Import-path rename blockers

1. `src/brand_os` is the current package root
2. wheel packaging explicitly points at `src/brand_os`
3. repo code, tests, docs, and examples import `brand_os` broadly
4. import-path rename would require Python compatibility shims or a deliberate breaking-change strategy

Conclusion:

- import-path churn is the heaviest technical blocker and must stay separate from public-facing rename readiness

### 4. CLI rename blockers

1. `[project.scripts]` exposes only `brandos = "brand_os.cli:app"`
2. README and CLAUDE command references overwhelmingly use `brandos ...`
3. CLI help and command hierarchy still expose cross-boundary groups (`persona`, `produce`, `eval`, `publish`, `queue`, `monitor`) under the same binary

Conclusion:

- CLI rename is blocked both by migration cost and by the fact that the current command surface is broader than future `agentcy-compass`

## Validation commands

Read-only validation commands for this audit:

```bash
cd brand-os && rg -n 'name = "brand-os"|brandos = "brand_os\.cli:app"|packages = \["src/brand_os"\]' pyproject.toml
cd brand-os && rg -n 'BriefWriter|agentcy-compass|repo: Literal\["brand-os"\]|module: Literal\["agentcy-compass"\]' src/brand_os/plan/brief_v1.py tests/plan/test_brief_v1.py
cd brand-os && rg -n 'brandOS|brand-os|brandos|agentcy-compass|brief\.v1|persona|produce|eval|publish|queue|monitor|server' README.md CLAUDE.md src/brand_os/cli.py src/brand_os/core/config.py src/brand_os/core/storage.py
cd brand-os && PYTHONPATH=src ../cli-prsna/.venv/bin/python -m pytest tests/plan/test_brief_v1.py
```

Optional spot checks for later rename planning:

```bash
cd brand-os && uv run brandos plan --help
cd brand-os && uv run brandos plan run "Increase caregiver response to a fall planning checklist." --brand GiveCare --voice-pack-input ../protocols/examples/voice_pack.v1.minimal.json --brief-v1-output ./tmp/brief.v1.json --policy-verdict approved --policy-confidence 0.91
```

## Bottom line

`brand-os` is already aligned where loop 7 most needs it to be: canonical `brief.v1` output keeps `writer = { repo: "brand-os", module: "agentcy-compass" }`.

It is not yet honestly rename-ready across the rest of the repo because four distinct naming layers and one deeper boundary problem are still unresolved:

1. repo directory: `brand-os`
2. package/distribution: `brand-os`
3. import path: `brand_os`
4. CLI binary: `brandos`
5. repo boundary: still broader than future `agentcy-compass`, with active overlap across `persona`, `produce`, `eval`, `publish`, `queue`, `monitor`, `server`, plus residual `cli-agency` entanglement

The key loop-7 conclusion is therefore:

- artifact-writer alignment is already correct
- public rename readiness is blocked mostly by boundary narrowing and migration planning
- import-path and runtime-prefix renames are separate technical migrations that should remain explicitly deferred until a future task authorizes compatibility work
