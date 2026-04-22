# agentcy

Consolidated monorepo for the Agentcy CLI suite.

## Members

| Dir | Package / bin | Purpose |
| --- | --- | --- |
| `protocols/` | `agentcy-protocols` | Shared schemas, examples, and adapters |
| `vox/` | `agentcy-vox` | Persona creation and `voice_pack.v1` export |
| `compass/` | `agentcy-compass` | Brand planning and `brief.v1` generation |
| `echo/` | `agentcy-echo` | Forecast generation from documents + requirement |
| `loom/` | `agentcy-loom` | TypeScript execution runtime for drafts, review, publish |
| `pulse/` | `agentcy-pulse` | `run_result.v1` → `performance.v1` + calibration + study |

## Naming contract

This repo now uses `agentcy-*` package and CLI names, but the canonical protocol writer fields intentionally stay split for compatibility:

- `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`
- `brief.v1.writer = { repo: "brand-os", module: "agentcy-compass" }`
- `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`
- `run_result.v1.writer = { repo: "cli-phantom", module: "agentcy-loom" }`
- `performance.v1.writer = { repo: "cli-metrics", module: "agentcy-pulse" }`

The rule is simple: package/bin names are unified under Agentcy, while protocol lineage keeps the historical `writer.repo` values until an explicit artifact migration lands.

## Setup

```bash
# Python workspace + repo-local dev tools
uv sync --group dev

# Optional Python extras
uv sync --all-extras --group dev

# Loom runtime
cd loom/runtime && pnpm install
```

## Best fit

Agentcy is best when you need a protocol-first workflow stack rather than a single embedded SDK:

- persona → brief → forecast → execution → measurement pipelines
- human-and-agent collaboration over stable JSON/file handoffs
- resumable operator workflows with explicit artifacts and lineage

It is not yet the best fit for:

- non-technical one-click onboarding
- teams that only want a single import-and-go library

## Install profiles

The suite is consumable in layers:

```bash
# Base Python suite: root CLI + protocols + vox + compass + echo base CLI + pulse
uv sync --group dev
# or: make install-python-suite

# Full Echo simulation runtime (Python 3.11 only)
uv sync --extra simulation
# or: make install-echo-simulation

# Loom runtime (Node)
cd loom/runtime && pnpm install
# or: make install-loom

# Full local operator stack
make install-full-operator
```

Published package contours:

- `agentcy-protocols` — closest thing to a drop-in library layer
- `agentcy-*` member CLIs — stage-owned workflow tools
- `agentcy` — umbrella dispatcher and pipeline orchestrator

The umbrella package is therefore best understood as an operator CLI suite, not a single drop-in SDK.

Useful discovery commands:

```bash
agentcy catalog --json
agentcy quickstart --profile full-operator --json
agentcy doctor --json
agentcy member compass --json plan list
```

## Test it

```bash
make doctor
make check
make lint
```

### Direct test commands

```bash
# The protocol seam tests shell into loom, so install the runtime once in a clean checkout.
cd loom/runtime && pnpm install

uv run pytest tests compass/tests echo/tests pulse/tests vox/tests protocols/tests -q
cd loom/runtime && pnpm check
```

## Pipeline commands

### Root pipeline helpers

```bash
# Preview bundle: module-first output under artifacts/pipelines/<pipeline_id>/
uv run agentcy --provider claude-cli --model sonnet pipeline run \
  --pipeline-id givecare-launch-01 \
  --persona scientist \
  --persona-eval \
  --brand givecare \
  --brief "Before fall gets busy, make caregiving feel lighter" \
  --files docs/launch-memo.md \
  --loom-workflow social.post \
  --mode preview \
  --output-dir artifacts/pipelines \
  --json

# Preview mode auto-finishes loom as a dry run and writes one bundle with:
# vox/, compass/, echo/, loom/, pulse/, reports/, bundle_manifest.json
# Pulse is skipped honestly in preview mode unless you later attach canonical measurement.

# After loom publish + pulse adapt happen, backfill the bundle with canonical later-stage artifacts
uv run agentcy pipeline update \
  --manifest artifacts/pipelines/<pipeline_id>/manifest.json \
  --run-result /tmp/run_result.json \
  --performance /tmp/performance.json \
  --json

# Re-open the manifest later and run pulse study once performance exists
uv run agentcy pipeline study \
  --manifest artifacts/pipelines/<pipeline_id>/manifest.json \
  --json
```

Dispatcher commands also accept root-level LLM overrides that are forwarded to members which honor them. The root pipeline also supports `--pipeline-id` so stable bundles can land at paths like `artifacts/pipelines/givecare-launch-01/`:

```bash
uv run agentcy --provider claude-cli --model haiku echo run --files docs/memo.md --requirement "Predict reaction" --smoke --json
```

### Live pipeline

```bash
uv run agentcy-vox --json export scientist --to voice-pack.v1 > /tmp/voice_pack.json
uv run agentcy-compass plan run "Before fall gets busy, make caregiving feel lighter" \
  --brand givecare \
  --voice-pack-input /tmp/voice_pack.json \
  --brief-v1-output /tmp/brief.json \
  -f json > /tmp/brief_plan.json
uv run agentcy-echo run --files docs/ --brief /tmp/brief.json --json > /tmp/forecast.json
cd loom/runtime && node bin/loom.js run social.post --brand givecare --brief-file /tmp/brief.json --json > /tmp/run_result.json
uv run agentcy-pulse adapt --run-result /tmp/run_result.json --sidecar sidecar.json --output /tmp/performance.json --json > /tmp/performance.stdout.json
uv run agentcy-pulse calibrate --forecast /tmp/forecast.json --performance /tmp/performance.json --json > /tmp/calibration.json
```

### Runtime constraints

- `agentcy-echo` full simulation requires **Python 3.11** plus `uv sync --extra simulation`
- `agentcy-echo run --smoke` keeps ontology/graph/profile preparation live but skips the long-running OASIS subprocess and emits deterministic run artifacts instead
- `loom/runtime` needs `pnpm install`
- `make pipeline-fixtures` is the fixture-backed smoke path when you only want to validate downstream protocol plumbing

## Current status

- Root dispatcher: healthy, now probes member reachability instead of only binary presence; ships `pipeline run` / `pipeline update` / `pipeline study` helpers, supports stable named bundles via `--pipeline-id`, writes module-first preview bundles (`vox/`, `compass/`, `echo/`, `loom/`, `pulse/`, `reports/`), forwards root-level `--provider` / `--model` overrides to members, including Compass via `BRANDOPS_LLM_PROVIDER` when applicable, and now exposes `agentcy member <member> --json ...` as a normalized wrapper over member-local JSON differences
- Vox: healthy; structured eval tiers and saved eval-report review flow now ship in the CLI
- Compass: healthy for package/CLI + planning surfaces; stage outputs are normalized before validation, activation coercion now tolerates numeric week/budget fields, local operator runs can use `claude-cli` / `sonnet` instead of falling back to mock on Gemini rate limits, and compatible data-producing commands now support both `--json` preference and `--json-envelope` normalized success envelopes
- Echo: base CLI healthy; completed runs now emit a repo-local `run_eval` sidecar alongside canonical forecast export, the simulation-config stage now seeds taxonomy-driven `scenario_buckets` into aligned initial reaction lanes, CLI automation forces the simulation subprocess to exit instead of lingering in command-waiting mode, and the single-platform scripts emit action logs for downstream timeline/report assembly
- Loom: help and runtime tests no longer hard-fail when native `canvas` is unavailable; social rendering falls back to SVG/resvg
- Pulse: supports legacy bare adapt invocation, standardized `--json` envelopes, and a `study` command that ingests optional echo/vox eval sidecars, including echo synthetic-signal metrics such as coverage, local diversity, complexity, and heuristic critic rejection rate
