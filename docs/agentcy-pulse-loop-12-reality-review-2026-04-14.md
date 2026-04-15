# agentcy-pulse loop-12 reality review — 2026-04-14

Date: 2026-04-14
Scope: bounded deep-review of the live `agentcy-pulse/` repo against `_agentcy-docs/family-loop-12-checkpoint-2026-04-12.md`, `_agentcy-docs/cli-metrics-birth-contract-2026-04-12.md`, and the canonical `performance.v1` seam
Mode: read-only repo and protocol review

## Verdict

The current mismatch is primarily **documentation drift**, not contract drift.

Why:
- the live repo directory in the workspace is now `agentcy-pulse/`, not `cli-metrics/`
- the live repo-local package/import/CLI surfaces are internally aligned as `agentcy-pulse` / `agentcy_pulse` / `agentcy-pulse`
- the canonical protocol contract still intentionally requires `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }`
- that mixed writer contract is still present in `protocols/performance.v1.schema.json`, `protocols/examples/performance.v1.minimal.json`, and `protocols/lineage-rules.md`
- the repo-local adapter stays thin and delegates to the parent canonical family adapter instead of inventing a second authority

So:
- **documentation drift:** yes, because loop-12 docs still narrate the birth slice as repo `cli-metrics` while literal workspace reality is `agentcy-pulse/`
- **repo-surface drift:** no meaningful current drift inside the repo’s package/import/bin surface; those surfaces are aligned with `agentcy-pulse`
- **contract drift:** no; the canonical `performance.v1` writer and privacy contract remain preserved

## Sources reviewed

Control plane:
- `_agentcy-docs/family-loop-12-checkpoint-2026-04-12.md`
- `_agentcy-docs/cli-metrics-birth-contract-2026-04-12.md`
- `_agentcy-docs/AGENTCY_STACK.md`
- `_agentcy-docs/AGENTCY_PROGRESS.md`
- `_agentcy-docs/AGENTCY_RECAP.md`
- `_agentcy-docs/family-workspace-reality-scan-2026-04-14.md`

Canonical protocol seam:
- `protocols/performance.v1.schema.json`
- `protocols/examples/run_result.v1.published.json`
- `protocols/examples/performance.v1.minimal.json`
- `protocols/lineage-rules.md`

Live repo:
- `agentcy-pulse/pyproject.toml`
- `agentcy-pulse/README.md`
- `agentcy-pulse/src/agentcy_pulse/__init__.py`
- `agentcy-pulse/src/agentcy_pulse/adapter.py`
- `agentcy-pulse/src/agentcy_pulse/cli.py`
- `agentcy-pulse/tests/test_seam.py`
- `agentcy-pulse/tests/test_cli.py`

## Literal repo reality now

Literal path:
- `/Users/amadad/projects/agentcy-pulse`

Git reality:
- branch: `main`
- upstream: none configured

Dirty working-tree facts observed during review:
- tracked modified:
  - `README.md`
  - `src/agentcy_pulse/cli.py`
  - `tests/test_seam.py`
- untracked:
  - `.github/workflows/smoke.yml`
  - `.gitignore`
  - `tests/test_cli.py`

Current tracked diffstat:
- `README.md` — 2 insertions
- `src/agentcy_pulse/cli.py` — 5 line changes
- `tests/test_seam.py` — 8 insertions

Interpretation:
- the repo is in-flight, matching the family workspace scan
- the local delta is still bounded to help/docs and seam-smoke coverage rather than a broadened analytics implementation wave

## Exact current install / help / import / test surface

### Install / environment sync

Verified command:
- `cd agentcy-pulse && uv sync`

Observed result:
- dependency resolution/check completed successfully
- no repo-local evidence suggests a heavier bootstrap than the bounded loop-12 birth slice

### Package / distribution surface

From `agentcy-pulse/pyproject.toml`:
- project name: `agentcy-pulse`
- version: `0.1.0`
- Python requirement: `>=3.11`

### CLI surface

From `agentcy-pulse/pyproject.toml`:
- script entrypoint: `agentcy-pulse = "agentcy_pulse.cli:main"`

Verified help command:
- `cd agentcy-pulse && uv run agentcy-pulse --help`

Observed help surface:
- command name: `agentcy-pulse`
- required argument: `--sidecar`
- optional arguments: `--run-result`, `--output`
- current help description: `Thin cli-metrics wrapper around the canonical family run_result.v1 -> performance.v1 adapter`

Interpretation:
- the installed operator-facing binary is already `agentcy-pulse`
- help text still references `cli-metrics` as the writer/birth lineage, which is consistent with the mixed writer contract and historical slice naming

### Import surface

Verified import command:
- `cd agentcy-pulse && uv run python -c "import agentcy_pulse; print(agentcy_pulse.__file__)"`

Observed import root:
- `agentcy_pulse`

Exported package surface:
- `adapt_canonical_run_result_to_performance`
- `__version__ = "0.1.0"`

### Test surface

Verified commands:
- `cd agentcy-pulse && uv run pytest -q`
- `cd agentcy-pulse && uv run pytest -q tests/test_seam.py tests/test_cli.py`

Observed result:
- `3 passed`

Current repo-local test coverage is still bounded:
- `tests/test_seam.py` checks parity with the canonical family expected fixture when sibling `../protocols/` fixtures are available
- `tests/test_cli.py` checks CLI file-output and stdout behavior without widening scope

## Repo-birth reality against loop-12 claims

## 1. Repo directory claim

Loop-12 checkpoint language still records the birth repo as `cli-metrics`.
Literal workspace reality is now `agentcy-pulse/`.

Assessment:
- this is the clearest **documentation drift** in the loop-12 narration
- it is not evidence of repo-local implementation drift because the repo itself is coherent
- it is also not by itself contract drift, because the protocol still intentionally preserves `writer.repo = "cli-metrics"`

## 2. Package / import / CLI claim

Loop-12 expected birth surfaces:
- package/distribution `agentcy-pulse`
- import root `agentcy_pulse`
- CLI binary `agentcy-pulse`

Live repo reality matches those exactly.

Assessment:
- no meaningful repo-surface drift here
- the repo-local public surface is already aligned with the family module name

## 3. Thin seam delegation claim

The repo-local adapter in `src/agentcy_pulse/adapter.py` dynamically loads the parent canonical adapter at:
- `protocols/adapters/run_result_to_performance_v1.py`

The repo-local seam test compares output against:
- `protocols/tests/fixtures/run_result_to_performance_v1/performance.rich.expected.json`

Assessment:
- this preserves the parent family protocol layer as authority
- no second schema/fixture authority is being created in the repo
- this is aligned with the loop-12 and birth-contract requirement to stay thin

## performance.v1 ownership and privacy review

### Ownership remains preserved

Canonical `performance.v1` ownership remains locked and consistent across reviewed artifacts:
- schema: `writer.repo = "cli-metrics"`, `writer.module = "agentcy-pulse"`
- example: same mixed writer contract
- lineage rules: same mixed writer contract

The live repo does not override that contract.
Its CLI and adapter merely produce canonical output through the family-owned adapter path.

### Privacy bounds remain preserved

The canonical privacy rule remains intact in reviewed protocol artifacts:
- aggregate published `social.post` observations only
- no tokens
- no secrets
- no auth material
- no audience-level data
- no user-level PII
- publish locators such as `post_id` and public `url` remain allowed

The live repo review found no widening beyond that boundary.
The repo still operates on:
- canonical published `run_result.v1`
- deterministic sidecar metrics
- canonical `performance.v1` output

## Smallest honest classification

### What is real today
- repo directory: `agentcy-pulse`
- package: `agentcy-pulse`
- import root: `agentcy_pulse`
- CLI binary: `agentcy-pulse`
- canonical writer contract: still `cli-metrics` / `agentcy-pulse`

### Therefore
- the repo birth is real as a minimal pulse repo
- the family protocol contract is still intentionally mixed
- the main inconsistency is that some loop-12 docs still describe literal repo birth using the historical `cli-metrics` repo name after the family directory rename landed

## Next smallest bounded follow-up

Only one bounded follow-up is justified from this review:

**Update loop-12 control-plane docs so they distinguish literal repo reality from preserved writer-contract history.**

That follow-up should:
- record that the literal workspace repo is now `agentcy-pulse/`
- preserve canonical `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }` unless a separate bounded contract-change task is opened
- avoid changing repo-local package/import/bin surfaces, which already align
- avoid broad analytics expansion, rename normalization, or ownership rewrites

Not justified from this review:
- changing the `performance.v1` writer contract
- widening `performance.v1` scope
- adding live analytics integrations
- introducing broader metrics abstractions
- reworking the repo’s public surface

## Bottom line

`agentcy-pulse/` is real and internally coherent as a thin repo-birth slice.
The current mismatch against loop 12 is mainly **documentation drift about literal repo naming**, not repo-surface drift and not contract drift.
The canonical `performance.v1` seam remains thin, parent-authoritative, ownership-preserving, and privacy-bounded.
The next smallest bounded action is a control-plane doc correction that acknowledges the live `agentcy-pulse/` directory while leaving the mixed `writer.repo = "cli-metrics"` contract untouched until an explicit later task changes it.