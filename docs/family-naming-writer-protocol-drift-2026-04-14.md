# Family naming, writer, and protocol drift ledger — 2026-04-14

Purpose: compare the six current family modules across literal repo directory, shipped package/import/CLI surfaces, canonical writer contract, and current control-plane narration.

Scope and method:
- Family modules only: `agentcy-vox`, `agentcy-compass`, `agentcy-echo`, `agentcy-loom`, `agentcy-pulse`, `agentcy-lab`
- Inputs: `_agentcy-docs/AGENTCY_RECAP.md`, `_agentcy-docs/AGENTCY_STACK.md`, `_agentcy-docs/AGENTCY_PROGRESS.md`, `protocols/`, and each repo README/manifest
- This is an audit ledger, not a rename plan
- Supporting repos such as `protocols/` and `cli-agency` are cited as control-plane evidence only, not counted as family modules

## Decision rule used in this ledger

Intentional mixed writer contract:
- `writer.repo` stays on the canonical current repo identity locked in family protocol artifacts
- `writer.module` stays on the family module identity
- this is intentional when confirmed by `protocols/tests/test_canonical_writer_module_references.py` and `protocols/lineage-rules.md`

Stale present-tense naming drift:
- a doc speaks as if former repo names are still the live directories now
- or a family doc narrates a current repo primarily through historical names even though the workspace directory already uses `agentcy-*`
- or a repo surface still ships older package/import/CLI names that are real public compatibility surfaces

Drift classes used below:
- `intentional mixed writer contract`
- `family-doc-only drift`
- `repo-surface drift`
- `both`

## Ledger

| Family module | Literal repo directory now | Shipped package / distribution | Import / module path | CLI binary | Canonical `writer.repo` | Canonical `writer.module` | Control-plane current narration | Drift class | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `agentcy-vox` | `agentcy-vox` | `prsna` (`agentcy-vox/pyproject.toml`) | `prsna` (`packages = ["src/prsna"]`) | `persona` (`[project.scripts]`) | `cli-prsna` | `agentcy-vox` | `AGENTCY_RECAP.md` and `AGENTCY_STACK.md` both still narrate this module as `agentcy-vox` formerly `cli-prsna`, while loop docs still cite the canonical writer as `cli-prsna` | both | Writer locked by `protocols/lineage-rules.md`, `protocols/tests/test_canonical_writer_module_references.py`, `protocols/tests/test_voice_pack_to_brief_v1.py`; repo surfaces from `agentcy-vox/pyproject.toml`, `agentcy-vox/README.md` |
| `agentcy-compass` | `agentcy-compass` | `brand-os` (`agentcy-compass/pyproject.toml`) | `brand_os` (`packages = ["src/brand_os"]`) | `brandos` | `brand-os` | `agentcy-compass` | control plane correctly locks the mixed writer pair, but still narrates active bounded work in present tense as `brand-os` / future `agentcy-compass` | both | Writer locked by `protocols/lineage-rules.md`, `protocols/tests/test_canonical_writer_module_references.py`, `protocols/tests/test_voice_pack_to_brief_v1.py`, `agentcy-compass/tests/plan/test_brief_v1.py`; repo surfaces from `agentcy-compass/pyproject.toml`, `agentcy-compass/README.md` |
| `agentcy-echo` | `agentcy-echo` | `mirofish-backend` (`agentcy-echo/pyproject.toml`) | `app` (`packages = ["app"]`) | `mirofish` | `cli-mirofish` | `agentcy-echo` | control plane still narrates this module through attribution-preserving `cli-mirofish` / MiroFish compatibility language, with former naming still front-and-center | both | Writer locked by `protocols/lineage-rules.md`, `protocols/tests/test_canonical_writer_module_references.py`, `protocols/tests/test_brief_to_forecast_v1.py`, `protocols/tests/test_forecast_v1_protocol.py`; repo surfaces from `agentcy-echo/pyproject.toml`, `agentcy-echo/README.md`, `agentcy-echo/app/forecast_v1.py` |
| `agentcy-loom` | `agentcy-loom` | `loom-runtime` (`agentcy-loom/runtime/package.json`) | runtime source modules under `runtime/src/*` | `loom` (`bin.loom`) | `cli-phantom` | `agentcy-loom` | control plane still narrates loop 8 as `cli-phantom` / `agentcy-loom`; repo README still states `repo: cli-phantom` even though directory is now `agentcy-loom` | both | Writer locked by `protocols/lineage-rules.md`, `protocols/tests/test_canonical_writer_module_references.py`, `protocols/tests/test_brief_to_run_result_v1.py`, `protocols/tests/test_run_result_v1_protocol.py`; repo surfaces from `agentcy-loom/runtime/package.json`, `agentcy-loom/README.md`, `agentcy-loom/runtime/fixtures/run_result.v1.published.mirror.json` |
| `agentcy-pulse` | `agentcy-pulse` | `agentcy-pulse` (`agentcy-pulse/pyproject.toml`) | `agentcy_pulse` | `agentcy-pulse` | `cli-metrics` | `agentcy-pulse` | control plane still narrates the canonical writer and active loop as `cli-metrics` / `agentcy-pulse`, even though the repo directory now exists as `agentcy-pulse` | family-doc-only drift | Writer locked by `protocols/lineage-rules.md`, `protocols/tests/test_canonical_writer_module_references.py`, `protocols/tests/test_performance_v1_protocol.py`, `protocols/adapters/run_result_to_performance_v1.py`; repo surfaces from `agentcy-pulse/pyproject.toml`, `agentcy-pulse/README.md` |
| `agentcy-lab` | `agentcy-lab` | `agentcy-lab` (`agentcy-lab/pyproject.toml`) | `agentcy_lab` | `agentcy-lab` | none locked at family protocol layer | none locked at family protocol layer | control plane narrates `agentcy-lab` consistently as a shared eval/autoresearch plane and records no canonical writer contract yet | none material | No family writer artifact exists in `protocols/lineage-rules.md` or `protocols/tests/test_canonical_writer_module_references.py`; repo surfaces from `agentcy-lab/pyproject.toml`, `agentcy-lab/README.md` |

## Per-module findings

### 1. `agentcy-vox`
- Intentional mixed contract is real: canonical family artifacts still require `writer = { repo: "cli-prsna", module: "agentcy-vox" }`.
- Repo-surface drift is also real: actual shipped surfaces are still `prsna` package, `prsna` import, and `persona` CLI.
- Family-doc-only drift is present because current family docs narrate the live repo as `formerly cli-prsna` while loop-era notes still speak in active present tense about `cli-prsna` as if it were the live repo root.

### 2. `agentcy-compass`
- Intentional mixed contract is real: canonical `brief.v1` ownership remains `brand-os` + `agentcy-compass`.
- Repo-surface drift is real and wider than naming alone: `brand-os` package, `brand_os` import, `brandos` CLI, plus broader repo-scope surfaces still exceed the future compass boundary.
- This is the clearest case where naming drift and ownership/boundary drift must stay separated.

### 3. `agentcy-echo`
- Intentional mixed contract is real: canonical `forecast.v1` ownership remains `cli-mirofish` + `agentcy-echo`.
- Repo-surface drift is real and includes upstream-attribution surfaces: `mirofish-backend` distribution, `app` import root, `mirofish` CLI, and MiroFish branding.
- Family docs are intentionally conservative here, but they still narrate the module primarily through the former repo identity and compatibility framing.

### 4. `agentcy-loom`
- Intentional mixed contract is real: canonical `run_result.v1` ownership remains `cli-phantom` + `agentcy-loom`.
- Repo-surface drift is real: package is `loom-runtime`, CLI is `loom`, and README still says `repo: cli-phantom` in present tense.
- This is not just protocol drift; it is also a real public-surface mix across repo, package, and CLI layers.

### 5. `agentcy-pulse`
- The writer split is still intentionally mixed in canonical family protocol artifacts: `writer.repo = "cli-metrics"`, `writer.module = "agentcy-pulse"`.
- Unlike the other modules, repo-surface drift is minimal now because package/import/CLI already match `agentcy-pulse` naming.
- The main drift is family-doc-only: control-plane docs still narrate the writer and active slice through `cli-metrics` even though the live repo directory is `agentcy-pulse`.
- This looks intentional at the protocol layer and stale only at the repo-directory narration layer.

### 6. `agentcy-lab`
- No canonical family writer contract is presently locked for a `lab` artifact.
- Repo/package/import/CLI naming is internally consistent.
- Current docs treat it as a shared plane rather than a protocol writer, which matches the available evidence.

## Explicit separation: intentional mixed contracts vs stale drift

### Intentional mixed writer contracts
These are supported by family protocol artifacts and should not be called stale drift by themselves:
- `voice_pack.v1` -> `{ repo: "cli-prsna", module: "agentcy-vox" }`
- `brief.v1` -> `{ repo: "brand-os", module: "agentcy-compass" }`
- `forecast.v1` -> `{ repo: "cli-mirofish", module: "agentcy-echo" }`
- `run_result.v1` -> `{ repo: "cli-phantom", module: "agentcy-loom" }`
- `performance.v1` -> `{ repo: "cli-metrics", module: "agentcy-pulse" }`

Primary proof:
- `protocols/lineage-rules.md`
- `protocols/tests/test_canonical_writer_module_references.py`
- protocol-specific tests: `test_voice_pack_to_brief_v1.py`, `test_brief_to_forecast_v1.py`, `test_brief_to_run_result_v1.py`, `test_performance_v1_protocol.py`

### Family-doc-only drift
These are places where the live workspace reality is `agentcy-*` directories, but control-plane narration still speaks in present tense through former repo identities:
- `AGENTCY_STACK.md` loop summaries for `cli-prsna`, `brand-os`, `cli-mirofish`, `cli-phantom`, `cli-metrics`
- `AGENTCY_PROGRESS.md` active loop narration, especially for pulse
- `AGENTCY_RECAP.md` still says older protocol artifacts and historical notes may carry pre-rename identifiers, which is fair historically but leaves present-tense ambiguity for current repo directories

### Repo-surface drift
These are real public/operator/developer surfaces that still ship older or mixed names:
- `agentcy-vox`: `prsna` / `persona`
- `agentcy-compass`: `brand-os` / `brand_os` / `brandos`
- `agentcy-echo`: `mirofish-backend` / `app` / `mirofish`
- `agentcy-loom`: `loom-runtime` / `loom` with README still narrating `cli-phantom`
- `agentcy-pulse`: little repo-surface drift; naming is already family-aligned at package/import/CLI level
- `agentcy-lab`: no meaningful repo-surface drift found

## Bottom line

1. The canonical writer split is not the drift problem; it is an intentionally locked family protocol contract.
2. The strongest true drift now is the gap between:
   - live repo directories already named `agentcy-*`, and
   - family control-plane narration that still speaks as if former repo identities are the operative present-tense repo roots.
3. Public repo-surface drift remains real for `vox`, `compass`, `echo`, and `loom` because package/import/CLI surfaces are still mixed or legacy-facing.
4. `agentcy-pulse` is the clearest case where the repo surface is already family-aligned but the family protocol docs intentionally keep an older `writer.repo` contract.
5. `agentcy-lab` should stay explicitly outside the writer-contract matrix until the family actually defines a canonical lab-owned protocol artifact.

## Citation index
- Control plane: `_agentcy-docs/AGENTCY_RECAP.md`, `_agentcy-docs/AGENTCY_STACK.md`, `_agentcy-docs/AGENTCY_PROGRESS.md`
- Canonical writer rules: `protocols/lineage-rules.md`, `protocols/tests/test_canonical_writer_module_references.py`
- `agentcy-vox` writer proofs: `protocols/tests/test_voice_pack_to_brief_v1.py`, `protocols/examples/voice_pack.v1.minimal.json`, `protocols/examples/voice_pack.v1.rich.json`
- `agentcy-compass` writer proofs: `protocols/tests/test_voice_pack_to_brief_v1.py`, `agentcy-compass/tests/plan/test_brief_v1.py`, `protocols/examples/brief.v1.rich.json`
- `agentcy-echo` writer proofs: `protocols/tests/test_brief_to_forecast_v1.py`, `protocols/tests/test_forecast_v1_protocol.py`, `protocols/examples/forecast.v1.completed-rich.json`
- `agentcy-loom` writer proofs: `protocols/tests/test_brief_to_run_result_v1.py`, `protocols/tests/test_run_result_v1_protocol.py`, `protocols/examples/run_result.v1.published.json`
- `agentcy-pulse` writer proofs: `protocols/tests/test_performance_v1_protocol.py`, `protocols/tests/test_run_result_to_performance_v1_adapter.py`, `protocols/examples/performance.v1.rich.json`
- Repo manifests and READMEs: `agentcy-vox/pyproject.toml`, `agentcy-compass/pyproject.toml`, `agentcy-echo/pyproject.toml`, `agentcy-loom/runtime/package.json`, `agentcy-pulse/pyproject.toml`, `agentcy-lab/pyproject.toml`, plus each repo `README.md`
