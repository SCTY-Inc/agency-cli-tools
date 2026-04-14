# cli-prsna rename-readiness audit for future `agentcy-vox`

Date: 2026-04-12  
Scope: loop-7 repo-local audit of naming surfaces in `cli-prsna` without changing names yet.

## Outcome

`cli-prsna` is already aligned on the canonical artifact-writer contract for the family voice layer:

```json
{
  "repo": "cli-prsna",
  "module": "agentcy-vox"
}
```

That writer alignment is already encoded in `src/prsna/exporters/__init__.py` inside `export_voice_pack()` and is the strongest rename-readiness fact in this repo.

The rest of the repo is intentionally mixed:

- repo directory still uses the legacy repo name `cli-prsna`
- Python distribution name is still `prsna`
- import path is still `src/prsna`
- installed CLI binary is still `persona`
- README and CLAUDE still brand the tool primarily as `prsna` / `persona`

Loop 7 should classify those surfaces, not rewrite them. The main readiness conclusion is:

- public branding/package/CLI surfaces can plausibly adopt future `agentcy-vox` naming later with compatibility aliases
- internal Python import-path surfaces are a separate, harder blocker and should not be implied by any future repo/package/CLI rename decision

## Current canonical surfaces

### Canonical artifact writer alignment

Source: `cli-prsna/src/prsna/exporters/__init__.py`

```python
"writer": {
    "repo": "cli-prsna",
    "module": "agentcy-vox",
}
```

Interpretation:

- `writer.repo` correctly remains the current repo name `cli-prsna`
- `writer.module` correctly carries the future family module `agentcy-vox`
- this already matches the loop-7 family invariant and should remain stable until any literal repo rename lands

### Repo directory surface

- current canonical: `cli-prsna`
- observed in family docs and task taxonomy as the current repo authority
- this is the canonical repo identifier for now and must remain the value used in writer fields

### Python distribution/package manifest surface

Source: `cli-prsna/pyproject.toml`

```toml
[project]
name = "prsna"
```

Interpretation:

- install/distribution naming is still legacy `prsna`
- no `agentcy-vox` distribution alias exists yet
- packaging currently describes a standalone persona tool, not the future family naming layer

### Python import-path surface

Sources:

- `cli-prsna/pyproject.toml` -> `packages = ["src/prsna"]`
- many imports across repo -> `from prsna ...`
- package root -> `cli-prsna/src/prsna/`

Interpretation:

- the internal module/import contract is still firmly `prsna`
- this is an implementation surface, not just branding
- it is materially harder to rename than repo/package/CLI display surfaces because it would touch code imports, tests, examples, and consumer code

### CLI binary and command surface

Sources:

- `cli-prsna/pyproject.toml`
- `cli-prsna/src/prsna/cli.py`
- `cli-prsna/README.md`
- `cli-prsna/CLAUDE.md`

Current canonical CLI surface:

```toml
[project.scripts]
persona = "prsna.cli:app"
```

And in the Typer app:

```python
app = typer.Typer(
    name="persona",
    help="Manage, compose, test, and export AI personas.",
    no_args_is_help=True,
)
```

Interpretation:

- installed command is `persona`
- command examples across docs consistently use `persona ...`
- CLI branding is public and user-facing, but separate from internal Python module naming

### README and install-branding surface

Sources:

- `cli-prsna/README.md`
- `cli-prsna/CLAUDE.md`

Current canonical branding patterns:

- repo title and prose heavily use `prsna`
- CLI examples heavily use `persona`
- library examples import from `prsna`
- README now explicitly says `persona export ... --to voice-pack` emits the canonical Agentcy `voice_pack.v1` JSON
- README also says `cli-prsna` owns writing the family voice artifact for downstream handoffs

Interpretation:

- docs are already family-aware at the artifact layer
- docs are not family-renamed at the product/package/CLI layer
- this mixed state is acceptable for loop 7 because artifact ownership and rename-readiness are intentionally decoupled

## Post-rename target surfaces

These are the likely future targets if a later wave authorizes naming changes. This section is directional only and does not authorize a rename now.

| Surface | Current canonical | Post-rename target |
| --- | --- | --- |
| artifact writer module | `agentcy-vox` | `agentcy-vox` |
| artifact writer repo | `cli-prsna` | `agentcy-vox` only after a literal repo rename |
| repo directory | `cli-prsna` | `agentcy-vox` |
| Python distribution name | `prsna` | likely `agentcy-vox` |
| import path | `prsna` | maybe `agentcy_vox` or another explicit import path, but not automatically implied |
| CLI binary | `persona` | likely `agentcy-vox` and/or `vox` |
| docs/install branding | `prsna` + `persona` | `agentcy-vox` with explicit legacy guidance |

Important distinction:

- `writer.module = agentcy-vox` is already on target
- `writer.repo = cli-prsna` must stay as-is until the repo is actually renamed
- import-path target is intentionally unresolved because public rename work must not accidentally imply immediate Python module churn

## Acceptable legacy aliases

Loop 7 should preserve room for compatibility layers. The following legacy names are acceptable aliases after any future public rename, subject to later implementation work.

### Repo and docs aliases

- `cli-prsna` as the historical repo name in migration notes and lineage docs
- `prsna` as the historical product/library name in upgrade instructions

### Package/distribution aliases

- `prsna` as a compatibility install surface for some transition period if a future `agentcy-vox` distribution is introduced
- explicit docs may need to say that `prsna` remains installable while `agentcy-vox` becomes the preferred public name

### CLI aliases

- `persona` is the strongest legacy CLI alias candidate because current docs and user flows depend on it
- a future `agentcy-vox` or `vox` command should not require immediate removal of `persona`

### Import-path aliases

- `prsna` import path should be treated as a long-lived compatibility surface if import renaming ever happens at all
- unlike repo/package/CLI naming, import aliases are not just convenience; they protect existing Python consumers and tests

## Hard blockers

### Internal import-path blockers

These are the most important blockers to distinguish clearly from public-facing rename work.

1. `src/prsna` is the current package root.
2. `pyproject.toml` wheel packaging explicitly points at `src/prsna`.
3. repo code imports `prsna` broadly across CLI, core modules, tests, and package exports.
4. README and CLAUDE library examples instruct users to `from prsna import ...`.
5. any import-path rename would need a deliberate Python compatibility story, not a cosmetic rename.

Conclusion:

- internal import-path churn is a real engineering blocker
- it should be treated separately from repo/package/CLI rename readiness
- future repo rename work must not imply that `from prsna import Persona` immediately disappears

### Public package/CLI blockers

These are lighter than the import-path blockers, but still real.

1. PyPI/distribution name is currently `prsna`, not `agentcy-vox`.
2. the only installed command is `persona`.
3. README quick start, commands, and development instructions are all written around `persona` and `prsna`.
4. CLAUDE developer guidance assumes the project is `prsna` and the command is `persona`.

Conclusion:

- public rename work is feasible but would require install/docs/entrypoint migration planning
- these blockers are less invasive than import-path blockers because compatibility aliases can absorb much of the transition

### Artifact-layer blockers

There is no blocker on the canonical writer alignment itself.

Current status:

- canonical `voice_pack.v1` export exists
- canonical writer field already reports `{ repo: "cli-prsna", module: "agentcy-vox" }`
- family artifact ownership is therefore aligned even while public product naming remains legacy

## Validation commands

Read-only validation commands for this audit:

```bash
cd cli-prsna && rg -n "name = \"prsna\"|\[project.scripts\]|persona = \"prsna\.cli:app\"|packages = \[\"src/prsna\"\]" pyproject.toml
cd cli-prsna && rg -n 'name="persona"|writer|agentcy-vox|cli-prsna|voice_pack' src/prsna/cli.py src/prsna/exporters/__init__.py
cd cli-prsna && rg -n "prsna|persona|agentcy-vox|voice_pack" README.md CLAUDE.md docs/voice-pack-v1-scorecard.md
cd cli-prsna && uv run python -m pytest tests/test_exporters.py
```

Optional spot checks for later rename planning:

```bash
cd cli-prsna && uv run persona export --list
cd cli-prsna && uv run persona export scientist --to voice-pack
```

## Loop-9 package/CLI policy handoff

Loop 7 established the readiness separation. Loop 9 narrows it further to a bounded package/CLI alias policy for this repo.

The explicit loop-9 policy is:

- keep `cli-prsna` as the canonical repo name
- keep `prsna` as the canonical Python package/distribution name unless a future-facing installed alias is additively introduced and proven
- keep `prsna` as the Python import path with no loop-9 import churn
- keep `persona` as the required compatibility CLI in loop 9
- preserve `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`
- allow a future-facing installed alias only if Task 3 implements it narrowly and Task 4 proves it from outside the repo root

The exact proof target is now documented in `docs/package-cli-alias-readiness-2026-04-12.md`.

## Bottom line

`cli-prsna` is already rename-ready at the family artifact-writer layer because canonical voice exports identify the module as `agentcy-vox` while correctly keeping the repo field on `cli-prsna`.

It is not yet rename-ready for a no-drama full public rename across every surface, because four separate naming layers are still legacy and should be handled independently:

1. repo directory: `cli-prsna`
2. package/distribution: `prsna`
3. import path: `prsna`
4. CLI binary: `persona`

The key loop-7 and loop-9 conclusion is the separation of concerns:

- public repo/package/CLI naming can be audited and later migrated with aliases
- internal Python import-path renaming is a distinct blocker and should remain explicitly deferred unless a future task authorizes compatibility work
- any future-facing installed alias must remain additive and externally proven rather than merely implied by docs

That separation keeps future `agentcy-vox` rename work honest and prevents accidental Python-module churn from being smuggled in under a simple branding change.