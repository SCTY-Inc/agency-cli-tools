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
| `pulse/` | `agentcy-pulse` | `run_result.v1` → `performance.v1` + calibration |

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

## Test it

```bash
make doctor
make check
make lint
```

### Direct test commands

```bash
uv run pytest tests compass/tests echo/tests pulse/tests vox/tests protocols/tests -q
cd loom/runtime && pnpm check
```

## Pipeline commands

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
- `loom/runtime` needs `pnpm install`
- `make pipeline-fixtures` is the fixture-backed smoke path when you only want to validate downstream protocol plumbing

## Current status

- Root dispatcher: healthy, now probes member reachability instead of only binary presence
- Vox: healthy
- Compass: healthy for package/CLI + planning surfaces; advanced autonomous features remain partial
- Echo: base CLI healthy; full simulation remains Python 3.11 only
- Loom: help and runtime tests no longer hard-fail when native `canvas` is unavailable; social rendering falls back to SVG/resvg
- Pulse: supports legacy bare adapt invocation and standardized `--json` envelopes
