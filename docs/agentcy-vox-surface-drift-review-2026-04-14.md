# agentcy-vox surface drift review — 2026-04-14

Scope: bounded deep review of the actual `agentcy-vox/` repo reality versus the still-live public compatibility surfaces around `voice_pack.v1`.

## Bottom line

`agentcy-vox/` is already the literal repo directory, but the repo's operator-facing and import-facing surfaces are still intentionally the older `cli-prsna` lineage:

- Python distribution/package: `prsna`
- Python import path: `prsna`
- installed CLI: `persona`
- canonical artifact writer: `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`

That split is not accidental drift inside the runtime surface. It is the currently documented compatibility policy. The biggest next blocker is **broader control-plane narration drift**, not implementation drift in the package/import/CLI surfaces themselves.

## What was inspected

Repo-local reality checked from `agentcy-vox/`:

- `agentcy-vox/pyproject.toml`
- `agentcy-vox/README.md`
- `agentcy-vox/CLAUDE.md`
- `agentcy-vox/docs/package-cli-alias-readiness-2026-04-12.md`
- `agentcy-vox/docs/packaged-install-help-proof-2026-04-12.md`
- `agentcy-vox/docs/voice-pack-v1-scorecard.md`
- `agentcy-vox/src/prsna/cli.py`
- `agentcy-vox/src/prsna/exporters/__init__.py`
- git branch / dirty-state commands from inside `agentcy-vox/`
- bounded verification commands for exporter and CLI surface

## Literal repo truth vs compatibility-surface truth

### Literal repo truth now

The directory on disk is already:

- repo directory: `agentcy-vox`

This means the family-level repo rename has landed at the filesystem level.

### Still-live public compatibility surfaces now

The repo itself still ships and documents these public surfaces:

| Surface | Current live value | Evidence |
| --- | --- | --- |
| Python distribution/package | `prsna` | `pyproject.toml` -> `[project] name = "prsna"` |
| Python import path | `prsna` | `src/prsna/`, internal imports, packaged proof doc |
| installed CLI | `persona` | `pyproject.toml` -> `[project.scripts] persona = "prsna.cli:app"`; `src/prsna/cli.py` |
| CLI help identity | `persona` | `Typer(name="persona", help="Manage, compose, test, and export AI personas.")` |
| canonical writer contract | `repo = "cli-prsna"`, `module = "agentcy-vox"` | `src/prsna/exporters/__init__.py` |

### Interpretation

The repo directory and the public package/import/CLI surfaces are now deliberately split. The code and docs do **not** currently claim that the public install/import/CLI surfaces were renamed to `agentcy-vox`. Instead they repeatedly preserve the mixed contract.

## `voice_pack.v1` writer contract status

The canonical writer remains correctly locked in the exporter:

```json
{
  "writer": {
    "repo": "cli-prsna",
    "module": "agentcy-vox"
  }
}
```

Observed in:

- `agentcy-vox/src/prsna/exporters/__init__.py`

Interpretation:

- `writer.module = "agentcy-vox"` matches current family naming
- `writer.repo = "cli-prsna"` intentionally preserves the historical writer contract
- this task should not rewrite that mixed contract

## Repo-local doc posture

The repo-local docs are mostly internally consistent about the compatibility story:

- `README.md` explicitly says install/package remains `prsna`, CLI remains `persona`, and `agentcy-vox` is future family naming only
- `CLAUDE.md` repeats the same naming policy and explicitly warns against implying an import-path rename
- `docs/package-cli-alias-readiness-2026-04-12.md` locks the loop-9 policy: no repo rename claim, no import rename, `persona` remains required compatibility CLI
- `docs/packaged-install-help-proof-2026-04-12.md` proves only the externally installed `persona` path and `import prsna`
- `docs/voice-pack-v1-scorecard.md` records the same mixed-surface analysis

The docs therefore still tell one coherent repo-local story, even though that story now diverges from the literal on-disk directory name.

## Package / import / CLI surface reality

### Package and install surface

Observed:

- `pyproject.toml` still publishes `name = "prsna"`
- no `agentcy-vox` package/distribution alias is present
- packaged proof doc records external wheel install for `prsna`

Assessment:

- no package/install implementation drift was found inside the repo
- the package surface is still intentionally old-name compatible

### Import path surface

Observed:

- package root remains `src/prsna/`
- internal imports are still `from prsna ...`
- packaged proof doc explicitly proves `import prsna`

Assessment:

- import-path readiness for any future rename is still unresolved
- but this is not accidental drift; it is a consciously preserved compatibility surface

### CLI surface

Observed:

- `pyproject.toml` exports only `persona = "prsna.cli:app"`
- `src/prsna/cli.py` sets Typer app name to `persona`
- `uv run persona export --list` still works
- packaged proof doc records external `persona --help`, `persona --version`, and `persona export --list`

Assessment:

- the CLI surface is coherent and proven for `persona`
- there is no evidence of a half-completed `agentcy-vox` or `vox` CLI rollout

## Current git-state evidence

Observed from inside `agentcy-vox/` on 2026-04-14:

```text
branch: main
status: main...origin/main [ahead 6]
modified: .gitignore
modified: README.md
untracked: CODEMAP.md
untracked: cli-prsna-wave.md
```

`git diff --stat` showed only:

```text
 .gitignore | 8 ++++++++
 README.md  | 2 +-
 2 files changed, 9 insertions(+), 1 deletion(-)
```

Interpretation:

- the repo is not clean
- the dirty state appears unrelated to a broad package/import/CLI migration
- there is active local documentation/chore drift, so any future proof claims should keep distinguishing repo-local dirty state from canonical shipped surface claims

## Bounded verification run for this review

Commands run:

```bash
cd agentcy-vox && uv run python -m pytest tests/test_exporters.py -q
cd agentcy-vox && uv run persona export --list
```

Observed:

- `tests/test_exporters.py`: 3 passed
- `persona export --list` still exposes `voice-pack`, `voice_pack`, and `voice_pack.v1`

Interpretation:

- canonical `voice_pack.v1` export surface is still functioning
- repo-local proof for the voice artifact remains healthy under the current compatibility naming

## Drift classification

### What is already aligned enough

- `voice_pack.v1` writer contract is preserved correctly
- repo-local docs consistently describe `prsna` / `persona` as the live public surfaces
- exported voice-pack surface still works
- packaged install/help proof for the current compatibility surfaces already exists

### What is actually drifting

The main drift is narrative mismatch between:

1. literal repo reality: `agentcy-vox/`
2. public compatibility surfaces: `prsna` package/import and `persona` CLI
3. older family docs that still frame this repo primarily as `cli-prsna`

That is mostly a control-plane narration issue, not a repo-local runtime-surface issue.

## Next blocker call

### Primary blocker: broader control-plane narration

This review classifies the next blocker as:

- **primary:** broader control-plane narration
- **secondary:** import-path readiness
- **not primary right now:** package/install proof drift
- **not primary right now:** repo-local docs drift

Why:

1. Repo-local docs are already fairly explicit and internally coherent.
2. Package/install proof is already present for the currently shipped `prsna` / `persona` surfaces.
3. Import-path readiness is still unresolved, but there is no evidence this repo is trying to solve it yet.
4. The most confusing live mismatch is that the repo directory is now `agentcy-vox/` while canonical writer docs and public surfaces intentionally still say `cli-prsna` / `prsna` / `persona`.

## Recommended smallest next action

Do not change runtime/package/import/CLI code from this review alone.

Instead, the smallest next control-plane action is:

1. update family-level review/checkpoint narration so it explicitly distinguishes:
   - literal repo directory truth: `agentcy-vox/`
   - public compatibility surfaces: `prsna` package/import and `persona` CLI
   - locked artifact writer contract: `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`
2. keep any future import-path or package-alias work as a separate bounded task
3. avoid implying that the repo rename completed public rename readiness

## Final assessment

`agentcy-vox/` is currently a renamed repo directory wrapped around a still-intentional `cli-prsna` compatibility surface.

That means the important fact is not "the repo is drifting badly." The more accurate statement is:

- the repo-local implementation is stable on `prsna` / `persona`
- the canonical voice artifact still correctly points at `cli-prsna` / `agentcy-vox`
- the remaining confusion mostly lives in family-level narration about what changed at the repo layer versus what has **not** changed in the package/import/CLI layer
