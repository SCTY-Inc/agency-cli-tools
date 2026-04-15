# CLAUDE.md — agentcy monorepo

Agent CLI suite. Six tools that chain sequentially through a shared protocol layer.

## Members

| Dir | Bin | Role |
|-----|-----|------|
| `protocols/` | (lib) | Shared schemas + adapters — `agentcy-protocols` pip package |
| `vox/` | `agentcy-vox` | Persona management — create, test, optimize, export |
| `compass/` | `agentcy-compass` | Brand ops — signals → plan → produce → publish |
| `echo/` | `agentcy-echo` | Swarm prediction — docs + requirement → social forecast |
| `loom/` | `agentcy-loom` | Comms runtime — brief → draft → render → publish (TypeScript) |
| `pulse/` | `agentcy-pulse` | Measurement + calibration — run_result.v1 → performance.v1 |

## Pipeline

```
agentcy-vox --json export <persona> --to voice-pack.v1                                → voice_pack.v1
agentcy-compass plan run "<brief>" --brand <id> --voice-pack-input <voice_pack> \
  --brief-v1-output <brief.v1.json> -f json                                           → brief.v1
agentcy-echo run --files docs/ --brief brief.v1.json --json                           → forecast.v1
agentcy-loom run social.post --brand <id> --brief-file brief.v1.json --json           → run_result.v1
agentcy-pulse adapt --run-result ... --sidecar ... --output performance.v1.json --json → performance.v1
agentcy-pulse calibrate --forecast ... --performance ... --json                        → calibration
```

Each tool reads a protocol artifact from the prior step and emits one for the next.

## Setup

```bash
# Python tools + repo-local dev commands
uv sync --group dev

# Optional extras
uv sync --all-extras --group dev

# TypeScript (loom)
cd loom/runtime && pnpm install

# Full live pipeline (echo simulation requires Python 3.11 + simulation extra)
make pipeline brand=givecare persona=my-persona files=docs/ req="predict adoption" sidecar=sidecar.json

# Fixture-backed downstream smoke path
make pipeline-fixtures sidecar=protocols/tests/fixtures/run_result_to_performance_v1/sidecar.rich.json
```

## Toolchain

- Python: uv workspace (`pyproject.toml` at root)
- TypeScript: pnpm (standalone in `loom/runtime/`)
- Lint: ruff (Python), tsc + vitest (TypeScript)

## Protocol contracts

All inter-tool contracts live in `protocols/`:
- `brief.v1.schema.json` — compass → echo, loom
- `forecast.v1.schema.json` — echo → pulse calibrate
- `run_result.v1.schema.json` — loom → pulse adapt
- `performance.v1.schema.json` — pulse adapt output; pulse calibrate input
- `voice_pack.v1.schema.json` — vox → compass, loom

## Standard interface

Current operator contract:
- `agentcy doctor --json` returns the normalized suite-wide readiness envelope
- `agentcy-pulse --json` now emits `{"status": "ok"|"error", "command": str, "data": {...}}`
- `agentcy-vox` uses a global `--json` flag
- `agentcy-echo` and `agentcy-loom` expose subcommand-level `--json`
- `agentcy-compass` currently prefers `-f json` on data-producing subcommands
- Exit: `0` success, `1` user error, `2` runtime error

Do not assume every member subcommand has the same JSON envelope yet; use the documented command form for each tool.

## Guardrails

- `trash` not `rm`
- `git add <files>` never `.`
- echo's `camel-oasis==0.2.5` / `camel-ai==0.2.78` stay pinned — do not upgrade
- Never delete `echo/uploads/runs/` — artifacts are immutable products
- compass persona subcommands are deprecated — use `agentcy-vox` instead
- pulse absorbs lab: `agentcy-pulse calibrate` replaces `agentcy-lab calibration`

## Writer contract split

Canonical artifact lineage intentionally keeps legacy `writer.repo` values while package/bin names use `agentcy-*`:
- `voice_pack.v1` → `{ repo: "cli-prsna", module: "agentcy-vox" }`
- `brief.v1` → `{ repo: "brand-os", module: "agentcy-compass" }`
- `forecast.v1` → `{ repo: "cli-mirofish", module: "agentcy-echo" }`
- `run_result.v1` → `{ repo: "cli-phantom", module: "agentcy-loom" }`
- `performance.v1` → `{ repo: "cli-metrics", module: "agentcy-pulse" }`

## Module names (Python imports unchanged)

Bins renamed; Python import paths preserved until explicit refactor:
- compass imports: `brand_os`
- echo imports: `app`
- pulse imports: `agentcy_pulse`
- vox imports: `prsna`
