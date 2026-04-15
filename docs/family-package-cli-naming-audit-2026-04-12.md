# Family package and CLI naming audit — 2026-04-12

Scope: bounded loop-7 rename-readiness check for public package/distribution names, import paths, CLI binaries, and install/documentation surfaces across the active family repos.

Canonical future family targets from `AGENTCY_RECAP.md`:

- `cli-prsna` -> `agentcy-vox`
- `brand-os` -> `agentcy-compass`
- `cli-mirofish` -> `agentcy-echo`
- `cli-phantom` -> `agentcy-loom`
- future `cli-metrics` -> `agentcy-pulse`

Loop-7 invariant: this is an audit only. It does **not** authorize literal repo renames or broad runtime churn.

## Summary

Current public naming is still mixed across the family:

- `cli-prsna` ships package `prsna`, import path `prsna`, and CLI binary `persona`, so a future repo rename to `agentcy-vox` would still leave three separate public surfaces on the old brand.
- `brand-os` is the cleanest of the Python repos on import/module alignment (`brand_os` + `brandos`), but its package/distribution name remains `brand-os`, so future `agentcy-compass` would still need an explicit package + CLI migration story.
- `cli-mirofish` is the hardest public-package mismatch: repo target is `agentcy-echo`, but the package is `mirofish-backend` while the CLI binary and docs present `mirofish`.
- `cli-phantom` has not exposed a packaged install binary yet; docs still teach `npx tsx src/cli.ts ...` from `runtime/`, while the runtime package itself is named `loom-runtime`. A future repo rename alone would not define the public command surface.
- `agentcy-pulse` is blocked at the birth-contract stage because there is no repo or package yet, so no public naming surface is locked.

## Cross-repo matrix

| Repo | Future target | Current package/distribution | Current import/module path | Current CLI/binary surface | Current install/doc surface | Rename-readiness blocker |
| --- | --- | --- | --- | --- | --- | --- |
| `cli-prsna` | `agentcy-vox` | `prsna` | `prsna` | `persona` | `uv pip install -e .`; `uv run persona --help`; README/CLAUDE use `persona ...` | Repo rename alone would leave package, import, and binary on legacy names; binary is especially ambiguous versus target `vox`. |
| `brand-os` | `agentcy-compass` | `brand-os` | `brand_os` | `brandos` | `uv sync`; `uv run brandos --help`; README/CLAUDE use `brandos ...` | Cleaner than others, but package, import, and CLI all still encode current repo branding rather than `compass`. |
| `cli-mirofish` | `agentcy-echo` | `mirofish-backend` | `app` | `mirofish` | `uv sync`; docs use `mirofish ...` directly | Package/binary split is already inconsistent today; target rename would still leave backend + CLI on old/upstream naming. |
| `cli-phantom` | `agentcy-loom` | `loom-runtime` (runtime package only) | runtime TS sources under `src/` | no installed binary documented; command is `npx tsx src/cli.ts ...` | docs require `cd runtime` and direct TS execution | No durable public install/binary contract yet; repo rename would not settle whether users install `agentcy-loom`, `loom-runtime`, or invoke `loom`. |
| future `cli-metrics` | `agentcy-pulse` | none yet | none yet | none yet | none yet | Missing birth contract; package/import/CLI naming cannot be evaluated until a minimal public contract exists. |

## Repo-by-repo findings

### 1) `cli-prsna` -> future `agentcy-vox`

Sources checked:
- `cli-prsna/pyproject.toml`
- `cli-prsna/src/prsna/cli.py`
- `cli-prsna/README.md`
- `cli-prsna/CLAUDE.md`

#### Naming surfaces

| Surface | Current canonical | Post-rename target | Acceptable legacy alias | Hard blocker |
| --- | --- | --- | --- | --- |
| Repo directory | `cli-prsna` | `agentcy-vox` repo | `cli-prsna` during transition | yes — repo rename alone does not change public package/binary surfaces |
| Package/distribution | `prsna` | likely `agentcy-vox` | `prsna` | yes — package name remains fully legacy-brand if repo changes first |
| Import path | `prsna` | likely `agentcy_vox` or a consciously retained `prsna` compatibility module | `prsna` | yes — no migration decision exists |
| CLI binary | `persona` | likely `agentcy-vox` or `vox` | `persona` | yes — current binary describes function, not family module |
| Docs/install branding | install editable package, run `persona ...` | docs should state target package + binary policy explicitly | current `persona` examples | yes — current docs never explain how future family naming relates to package/binary naming |

#### Evidence

- `pyproject.toml`: `name = "prsna"`
- `pyproject.toml`: `[project.scripts] persona = "prsna.cli:app"`
- `src/prsna/cli.py`: `app = typer.Typer(name="persona", ...)`
- README install: `uv pip install -e .`
- README development: `uv run persona --help`
- README/CLAUDE command surface consistently uses `persona ...`

#### Assessment

`cli-prsna` is **not** package/CLI rename-ready. Public naming today is coherent internally, but it is coherent around `prsna`/`persona`, not around the future family target `agentcy-vox`. The biggest unresolved question is whether family naming wants:

1. a family-branded package and binary (`agentcy-vox`, maybe `vox`), or
2. a family-branded package with a retained functional binary alias (`persona`), or
3. a family-branded repo only, with `prsna` intentionally kept as package/import identity.

Until that decision is made, repo rename readiness is incomplete.

### 2) `brand-os` -> future `agentcy-compass`

Sources checked:
- `brand-os/pyproject.toml`
- `brand-os/src/brand_os/cli.py`
- `brand-os/README.md`
- `brand-os/CLAUDE.md`

#### Naming surfaces

| Surface | Current canonical | Post-rename target | Acceptable legacy alias | Hard blocker |
| --- | --- | --- | --- | --- |
| Repo directory | `brand-os` | `agentcy-compass` repo | `brand-os` during transition | partial |
| Package/distribution | `brand-os` | likely `agentcy-compass` | `brand-os` | yes |
| Import path | `brand_os` | likely `agentcy_compass` or retained compatibility import | `brand_os` | yes |
| CLI binary | `brandos` | likely `agentcy-compass` or `compass` | `brandos` | yes |
| Docs/install branding | `uv sync`; `uv run brandos --help`; broad `brandOS` branding | docs should define the family-facing package/CLI story | `brandos` | yes |

#### Evidence

- `pyproject.toml`: `name = "brand-os"`
- `pyproject.toml`: `[project.scripts] brandos = "brand_os.cli:app"`
- `src/brand_os/cli.py`: `app = typer.Typer(name="brandos", ...)`
- wheel package path: `packages = ["src/brand_os"]`
- README install uses `uv sync`, then all examples call `brandos ...`
- README already aligns protocol ownership via `writer.module = "agentcy-compass"`, so artifact naming is farther ahead than package/CLI naming

#### Assessment

`brand-os` has the clearest internal public surface today, but it still does **not** match future family naming. It is a good example of the loop-7 rule that `writer.module` can be future-facing while package/import/CLI surfaces remain current-repo-branded. A literal repo rename to `agentcy-compass` would still leave users installing `brand-os`, importing `brand_os`, and invoking `brandos` unless an explicit migration plan is added.

### 3) `cli-mirofish` -> future `agentcy-echo`

Sources checked:
- `cli-mirofish/pyproject.toml`
- `cli-mirofish/app/cli.py`
- `cli-mirofish/README.md`
- `cli-mirofish/CLAUDE.md`

#### Naming surfaces

| Surface | Current canonical | Post-rename target | Acceptable legacy alias | Hard blocker |
| --- | --- | --- | --- | --- |
| Repo directory | `cli-mirofish` | `agentcy-echo` repo | `cli-mirofish` | yes |
| Package/distribution | `mirofish-backend` | likely `agentcy-echo` | `mirofish-backend` | yes |
| Import path | `app` | likely explicit package namespace for echo | `app` only as internal layout | yes |
| CLI binary | `mirofish` | likely `agentcy-echo` or `echo` | `mirofish` | yes |
| Docs/install branding | `uv sync`; docs use `mirofish ...` | docs should define whether upstream/fork naming remains public | `mirofish` | yes |

#### Evidence

- `pyproject.toml`: `name = "mirofish-backend"`
- `pyproject.toml`: `[project.scripts] mirofish = "app.cli:main"`
- `app/cli.py`: argparse `prog="mirofish"`
- README and CLAUDE consistently teach `mirofish run ...`, `mirofish runs list ...`, `mirofish runs export ...`
- README explicitly frames the repo as a fork of MiroFish

#### Assessment

`cli-mirofish` is the least rename-ready on public package surfaces. It already has a split identity:

- repo: `cli-mirofish`
- package: `mirofish-backend`
- CLI: `mirofish`
- future target: `agentcy-echo`

That means even without a repo rename, package and binary naming are already divergent. The audit result is not "rename now" but "decide whether upstream MiroFish branding remains a public compatibility layer or becomes a deprecated alias." Without that decision, `agentcy-echo` cannot present a clean public install story.

### 4) `cli-phantom` -> future `agentcy-loom`

Sources checked:
- `cli-phantom/runtime/package.json`
- `cli-phantom/runtime/src/cli.ts`
- `cli-phantom/README.md`
- `cli-phantom/CLAUDE.md`

#### Naming surfaces

| Surface | Current canonical | Post-rename target | Acceptable legacy alias | Hard blocker |
| --- | --- | --- | --- | --- |
| Repo directory | `cli-phantom` | `agentcy-loom` repo | `cli-phantom` | partial |
| Package/distribution | `loom-runtime` | likely `agentcy-loom` or intentionally retained `loom-runtime` | `loom-runtime` | yes |
| Import/module path | none exposed as public install/import surface | TBD | TS internal `src/*` layout | yes |
| CLI binary | no installed binary declared in `package.json`; docs invoke `npx tsx src/cli.ts` directly | likely `agentcy-loom` or `loom` | current direct-tsx dev command | yes |
| Docs/install branding | README/CLAUDE teach `cd runtime` + `npx tsx src/cli.ts ...` | docs should define stable install and invoke contract | dev-only `tsx` invocation | yes |

#### Evidence

- `runtime/package.json`: `name = "loom-runtime"`
- `runtime/package.json`: no `bin` field
- `runtime/package.json`: scripts include `"cli": "tsx src/cli.ts"`
- README and CLAUDE use direct commands like `npx tsx src/cli.ts help`

#### Assessment

`cli-phantom` has good future-module alignment in prose (`Loom Runtime`, `agentcy-loom`), but its public install surface is still underdefined. The current docs expose a development invocation pattern, not a durable package/binary contract. So a future repo rename to `agentcy-loom` would still leave open all of these questions:

- Is the npm package `agentcy-loom` or `loom-runtime`?
- Is the CLI binary `loom`, `agentcy-loom`, or still an undocumented `tsx` entrypoint?
- Is there any public binary at all, or is direct source execution the intended operator surface?

### 5) future `cli-metrics` -> `agentcy-pulse`

Sources checked:
- family control-plane docs only (`AGENTCY_STACK.md`, `AGENTCY_PROGRESS.md`)
- note from loop-7 instructions referencing `cli-metrics-birth-contract-2026-04-12.md`

#### Naming surfaces

| Surface | Current canonical | Post-rename target | Acceptable legacy alias | Hard blocker |
| --- | --- | --- | --- | --- |
| Repo directory | none yet | future `cli-metrics` or direct family-name repo decision | `cli-metrics` if introduced | yes |
| Package/distribution | none yet | likely `agentcy-pulse` | none yet | yes |
| Import path | none yet | TBD | none yet | yes |
| CLI binary | none yet | likely `agentcy-pulse` or `pulse` | none yet | yes |
| Docs/install branding | none yet | must be locked before repo creation | none yet | yes |

#### Assessment

`agentcy-pulse` is blocked not by cleanup work but by missing first-contract decisions. The family should avoid repeating the same ambiguity seen in other repos by deciding package name, import path, and binary name **before** a repo is created.

## Cross-repo blocker list

1. **No family-wide package/binary migration policy exists yet.**
   The repos have future family-module targets, but no shared rule says whether public package names and CLI binaries should also move to family names, or whether repo-local legacy binaries remain first-class aliases.

2. **Repo rename readiness is ahead of package/binary readiness.**
   `writer.module` alignment is already future-facing in several places, but public install/import/CLI surfaces remain current-brand or upstream-brand oriented.

3. **`cli-mirofish` has the highest current public-name ambiguity.**
   `cli-mirofish` / `mirofish-backend` / `mirofish` / `agentcy-echo` are four separate names for one module boundary.

4. **`cli-prsna` lacks a target binary decision.**
   The current binary `persona` is functionally descriptive, but no policy says whether that should remain an enduring alias under future `agentcy-vox` branding.

5. **`cli-phantom` lacks a stable packaged CLI surface.**
   Without a `bin` entry or an install command in docs, public naming cannot be considered settled even though `loom` branding is emerging.

6. **`agentcy-pulse` needs a birth contract before implementation.**
   Package name, import path, and CLI binary should be locked before any repo bootstrap to avoid another mixed-surface migration later.

## Recommended next bounded actions

1. Add a short family naming policy doc or control-plane appendix that answers two questions once for all repos:
   - Are family names required for package/distribution names, or only for module identity and docs?
   - Should each repo expose a short operator binary (`vox`, `compass`, `echo`, `loom`, `pulse`) plus legacy aliases, or retain current binaries indefinitely?

2. For each repo-local future audit, keep the current four-way table but add one explicit field: **public migration strategy** (`rename`, `alias`, or `retain`).

3. For `cli-phantom`, lock a minimal public binary contract before any rename proposal advances.

4. For future `cli-metrics`, use the birth-contract doc to decide package/import/CLI surfaces first, then build.

## Verification notes

This task was a docs/audit pass. Evidence came from direct inspection of:

- `cli-prsna/pyproject.toml`
- `brand-os/pyproject.toml`
- `cli-mirofish/pyproject.toml`
- `cli-phantom/runtime/package.json`
- `cli-prsna/src/prsna/cli.py`
- `brand-os/src/brand_os/cli.py`
- `cli-mirofish/app/cli.py`
- `cli-phantom/runtime/src/cli.ts`
- repo `README.md` and `CLAUDE.md` install/usage surfaces for each repo
