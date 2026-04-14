# cli-mirofish rename-readiness scorecard for future `agentcy-echo`

Date: 2026-04-12
Repo under audit: `cli-mirofish`
Task: `task-3` (expanded from prior loop-7 audit baseline)
Scope: repo-local authority doc for alias policy and unresolved-before-rename blockers; no literal rename authorized
Summary readiness verdict: `forecast.v1` writer alignment is already canonical as `{ repo: "cli-mirofish", module: "agentcy-echo" }`, but `cli-mirofish` is not yet literal-rename-ready at the repo/package/import/CLI layer because the current shipped compatibility surfaces are still `cli-mirofish` / `mirofish-backend` / `app` / `mirofish`, while the repo also carries explicit upstream MiroFish fork lineage, AGPL obligations, and import-root/runtime identifiers that should not be rewritten casually.

## Source docs consulted

- `AGENTCY_RECAP.md`
- `AGENTCY_STACK.md`
- `AGENTCY_PROGRESS.md`
- `CONSOLIDATION.md`
- `family-loop-7-checkpoint-2026-04-12.md`
- `rename-readiness-matrix-2026-04-12.md`
- `cli-mirofish/README.md`
- `cli-mirofish/CLAUDE.md`
- `cli-mirofish/pyproject.toml`
- `cli-mirofish/app/forecast_v1.py`
- `cli-mirofish/app/brief_v1.py`
- `cli-mirofish/docs/forecast-v1-deferral-scorecard.md`

## Naming surface audit

| Surface | Current canonical | Post-rename target | Acceptable legacy alias | Hard blocker |
| --- | --- | --- | --- | --- |
| Repo directory name | `cli-mirofish` | `agentcy-echo` | `cli-mirofish` during any future transition | Repo path is still referenced across family docs/tests/tasks, and the repo intentionally preserves visible upstream `MiroFish` lineage rather than presenting as a fresh standalone family repo today. |
| Package/distribution name | Python distribution `mirofish-backend` in `pyproject.toml` | family-aligned distribution name to be chosen explicitly later; likely `agentcy-echo` or `agentcy-echo-backend` | `mirofish-backend` | Public install surface, metadata, and image naming are all MiroFish-branded today; AGPL/upstream lineage means the package rename needs an explicit compatibility and attribution policy rather than a cosmetic swap. |
| Import path | wheel exposes top-level package `app`; repo code imports through `app.*` | family-aligned import path to be chosen later; likely `agentcy_echo` or another non-generic top-level package | internal `app` and repo-local imports may persist temporarily if wrapped deliberately | `app` is generic and not rename-ready, but changing it is a deep code/package move that touches all imports and packaging. This is a hard blocker for claiming import-path readiness now. |
| CLI binary | console script `mirofish` | future canonical binary likely `agentcy-echo` or family-approved alias | `mirofish` | README, CLAUDE, examples, and automation all invoke `mirofish`; no alias/help/install compatibility policy exists yet for a new binary. |
| Docs/install branding | README/CLAUDE/PRD brand the product as `MiroFish`; fork lineage is called out explicitly | docs may later lead with `agentcy-echo` while preserving upstream attribution/reference notes | `MiroFish`, `cli-mirofish` | Upstream fork history is part of the honest public story, and AGPL attribution should remain explicit. Docs cannot simply erase MiroFish naming without a deliberate lineage section. |
| Artifact writer fields | canonical `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`; `brief.v1` import expects `{ repo: "brand-os", module: "agentcy-compass" }` | unchanged until a literal repo rename lands; only `writer.repo` would change later | none needed beyond the current mixed canonical pair | none for current loop-7 readiness accounting; this surface is already aligned with the locked family rule that `writer.module` may be future-facing while `writer.repo` stays literal/current. |
| Fixture/test references | parent and repo-local tests/docs still assert `cli-mirofish` writer, repo paths, `forecast_v1`, and `mirofish` command surfaces | family-aligned path/name updates only after a literal rename plan exists | existing `cli-mirofish` and `mirofish` references | Hidden path and command assumptions still exist across tests/docs; these need bounded inventory and migration planning before any literal rename claim. |
| Runtime path/key prefixes | `uploads/runs/...`, `uploads/simulations/...`, `uploads/reports/...`; graph IDs prefixed `mirofish_`; logger namespaces `mirofish.*`; default names like `MiroFish Run` and `MiroFish Graph` | leave repo-local/runtime prefixes mostly untouched unless a later migration proves value; only external canonical seams need family naming | `mirofish_*`, `mirofish.*`, `MiroFish Run`, `MiroFish Graph` | Many of these are safe internal legacy identifiers, but some are persisted into run artifacts/logs. A blanket rename would create churn and migration risk without improving the family protocol seam. |

## Canonical surfaces already aligned

- `forecast.v1` already uses the canonical mixed writer pair in `app/forecast_v1.py`:
  - `repo = "cli-mirofish"`
  - `module = "agentcy-echo"`
- The loop-3/loop-7 family docs already treat `cli-mirofish` as the current canonical repo for future `agentcy-echo`.
- The stable downstream seam is already protocol-first rather than runtime-first:
  - `mirofish runs export <run_id> --artifact forecast_v1 --json`
  - emitted artifact type remains `forecast.v1`
- The `brief.v1` import adapter is family-aligned on upstream ownership and does not invent a second writer.

## Current shipped compatibility surfaces

The following remain the current shipped surfaces now. They are not already-shipped `agentcy-echo` replacements:

- repo: `cli-mirofish`
- Python distribution: `mirofish-backend`
- top-level import root: `app`
- installed CLI binary: `mirofish`
- primary docs/product/fork naming: `MiroFish`

Family naming is currently canonical only at the artifact-module layer:

- `forecast.v1.writer.repo = "cli-mirofish"`
- `forecast.v1.writer.module = "agentcy-echo"`

## Attribution-preserving alias policy

These old-name surfaces may remain as bounded compatibility aliases without creating a second family authority or erasing upstream lineage:

### Allowed compatibility aliases

- `cli-mirofish` as the literal repo name until a real repo rename is approved.
- `mirofish-backend` as the public distribution name until package/install migration is explicitly designed and verified.
- `app` as the current top-level import root until a deliberate package restructuring exists.
- `mirofish` as the installed CLI binary during any future transition window.
- `MiroFish` as upstream/fork branding in README, CLAUDE, acknowledgments, and attribution text.
- Internal runtime identifiers and namespaces such as:
  - `mirofish_*` graph IDs
  - `mirofish.*` logger namespaces
  - `MiroFish Run`
  - `MiroFish Graph`
- Repo-local filesystem buckets such as `uploads/runs/`, `uploads/simulations/`, and `uploads/reports/`.

### Alias policy rules

1. Old-name aliases may preserve install, import, execution, and lineage clarity; they must not be rewritten just for cosmetic family-name alignment.
2. Any future `agentcy-echo` naming should layer on top of these surfaces deliberately, not imply that the old surfaces never existed.
3. README/docs may introduce future family framing only if they continue to state clearly that this repo is a fork of upstream `MiroFish` and remains AGPL-licensed.
4. Compatibility aliases below the protocol seam are acceptable when they avoid churn in persisted artifacts, logs, run directories, or upstream-attribution language.
5. `writer.module = "agentcy-echo"` does not authorize changing `writer.repo`, package, import root, or CLI binary ahead of a literal migration.

Why these are safe for now:
- they do not alter the canonical family artifact writer contract
- they preserve explicit upstream fork and AGPL attribution instead of laundering lineage
- they are mostly internal, historical, or compatibility-facing
- changing them now would create churn in persisted state, logs, or public install surfaces with little protocol benefit

## Blocker profile by type

This task separates naming-only blockers from attribution/lineage blockers and from import-root blockers so future rename work cannot flatten them into one vague "naming cleanup" story.

### Naming-only blockers

These are user-visible naming surfaces that would need an explicit compatibility/deprecation plan, but they are not by themselves proof of deeper architectural coupling:

- repo directory `cli-mirofish`
- distribution/package name `mirofish-backend`
- console script `mirofish`
- docs/install/help text centered on `MiroFish`
- container/image naming under `ghcr.io/.../mirofish`
- fixture/test references to `cli-mirofish` and `mirofish`

Interpretation:
- these block any claim that a literal repo/package/CLI rename is already shipped
- they do not change canonical `forecast.v1` ownership by themselves
- most can remain as compatibility aliases until one migration plan is chosen and verified

### Attribution and lineage blockers

These are not cosmetic naming issues. They are obligations and public-history constraints that must remain visible through any future rename:

- the repo is documented as a fork of `666ghj/MiroFish`
- the repo remains AGPL-3.0 licensed
- the simulation/runtime layer remains OASIS-coupled
- README, CLAUDE, and acknowledgments presently tell the honest upstream story

Interpretation:
- future family naming must preserve explicit upstream attribution and AGPL notice
- docs cannot imply `agentcy-echo` is a clean-room replacement that superseded MiroFish already
- public rename work is blocked until the compatibility plan says how lineage remains operator-visible

### Import-root blockers

The package currently builds `packages = ["app"]`, and the console script points at `app.cli:main`.
That means the public Python import surface is still generic and repo-internal, not family-branded.
A literal package/import rename would require a deeper restructuring than loop 10 allows.

Why this blocker is distinct:
- `app` is not merely an old brand label; it is a generic import root embedded across repo code and packaging
- changing it would touch imports, wheel packaging, console entrypoints, and likely external examples/tests together
- unlike docs/bin aliases, import-root migration cannot honestly be claimed as a shallow compatibility shim

### Persisted runtime identifier blockers

Examples:
- `mirofish_...` graph IDs
- `mirofish.*` logger namespaces
- generated graph names/descriptions using `MiroFish`
- container/image naming under `ghcr.io/.../mirofish`

These should be classified individually. They are not all blockers to family protocol correctness, but they do block any claim that a full literal rename is just a docs-only change.

## Old-name surfaces: blockers vs safe internal legacy identifiers

### Hard blockers for a literal repo/package/CLI rename

- repo directory `cli-mirofish`
- distribution/package name `mirofish-backend`
- console script `mirofish`
- top-level package/import surface `app`
- README/CLAUDE/install instructions centered on `MiroFish`
- container/image reference `ghcr.io/${owner}/mirofish`

These are user-visible or integration-visible surfaces and would need an explicit migration plan.

### Safe internal legacy identifiers for now

- `mirofish_*` graph IDs
- logger namespaces like `mirofish.report_agent`, `mirofish.graph_tools`, `mirofish.simulation_runner`
- default labels such as `MiroFish Run` and `MiroFish Graph`
- internal repo-local path buckets like `uploads/runs/`, `uploads/simulations/`, `uploads/reports/`
- repo-local explanatory docs that reference MiroFish as the upstream product/history

These can remain until there is a concrete migration reason because they do not change canonical artifact ownership and mostly live below the family protocol seam.

## Upstream coupling and lineage constraints

`cli-mirofish` has stronger upstream coupling than the other family repos:

- it is explicitly a translated/forked derivative of upstream `MiroFish`
- the simulation layer depends on OASIS runner scripts under `scripts/`
- the repo uses AGPL-3.0 licensing and should preserve honest attribution
- the current runtime/product vocabulary is part of that lineage

Implication for loop 7:
- `agentcy-echo` should be treated as the family module identity
- `cli-mirofish` / `MiroFish` should remain the current repo/package/CLI lineage until a deliberate migration plan proves that package/import/CLI changes can preserve attribution, compatibility, and operator clarity
- the family should keep protocol coupling thin and avoid forcing downstream repos to depend on MiroFish internals

## Unresolved-before-rename list

A credible rename proposal remains blocked until all of the following are answered explicitly:

1. Public package target: if `mirofish-backend` ever changes, what exact successor distribution name is canonical?
2. Import-root target: if `app` ever changes, what exact import root replaces it, and what compatibility story exists for current importers?
3. CLI plan: if `mirofish` ever changes, what alias/deprecation window and help/install proof will be provided?
4. Repo-name plan: when and how would `cli-mirofish` become `agentcy-echo` without rewriting current family docs/tests prematurely?
5. Attribution plan: where will upstream `MiroFish` fork acknowledgment and AGPL notice live in any future family-led README/install surface?
6. Persisted-runtime policy: which `mirofish_*`, `mirofish.*`, and `MiroFish ...` identifiers are intentionally permanent compatibility/history markers versus later migration candidates?
7. External verification plan: what exact clean-install, help, export, and import-smoke commands must pass before claiming any shipped rename surface?
8. Dependency blocker status: whether external packaged verification is still constrained by pinned simulation dependencies such as `camel-oasis==0.2.5`, and whether that limits any rename proof claim.

## Bounded next actions

1. Keep `forecast.v1` canonical writer fields unchanged unless and until a literal repo rename lands.
2. Keep the shipped compatibility surfaces explicit in docs: `cli-mirofish` / `mirofish-backend` / `app` / `mirofish` remain current.
3. If future rename work is proposed, decide the public package/import/bin contract once before editing manifests:
   - distribution target
   - import target
   - CLI alias/deprecation plan
4. Add a bounded install/help verification plan before any rename claim:
   - clean install
   - `--help`
   - one representative JSON workflow
   - import smoke test from outside the repo root
5. Preserve explicit upstream attribution and AGPL lineage language in README/docs during any future family-name transition.
6. Prefer family docs and compatibility shims over broad rewrites of persisted internal IDs, logger namespaces, or runtime directories.

## Explicit non-goals

This audit does not authorize:
- renaming the repo directory now
- renaming `mirofish-backend` now
- rewriting imports away from `app` now
- replacing the `mirofish` binary now
- mass-editing logger namespaces or persisted runtime IDs
- deep refactors to hide upstream MiroFish/OASIS lineage

## Validation commands

```bash
cd cli-mirofish && rg -n "mirofish|MiroFish|mirofish-backend|agentcy-echo|forecast\.v1|logger|app\.cli:main|packages = \[\"app\"\]" -S README.md CLAUDE.md pyproject.toml app docs tests .github
cd cli-mirofish && uv run python -m pytest tests/test_cli_artifacts_and_visuals.py -k 'forecast_v1 or import_brief_v1'
cd cli-mirofish && uv run python -m pytest ../protocols/tests/test_brief_to_forecast_v1.py ../protocols/tests/test_forecast_v1_protocol.py
```

## Bottom line

`cli-mirofish` is already canonically aligned at the artifact level for future `agentcy-echo`, but it is not honest to call the repo/package/import/CLI surfaces rename-ready yet. The repo should keep the mixed canonical contract (`cli-mirofish` repo, `agentcy-echo` module), preserve explicit MiroFish/AGPL lineage, and treat most remaining MiroFish-named internals as safe legacy identifiers unless and until a deliberate migration plan proves otherwise.
