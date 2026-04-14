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
agentcy-vox export <persona> --to voice-pack.v1 --json  → voice_pack.v1
agentcy-compass plan --brand <id> --json                → brief.v1
agentcy-echo run --files docs/ --brief brief.v1 --json  → forecast.v1
agentcy-loom run social.post --brand <id> --json        → run_result.v1
agentcy-pulse adapt --run-result ... --sidecar ... --json → performance.v1
agentcy-pulse calibrate --forecast ... --performance ... → calibration
```

Each tool reads a protocol artifact from the prior step and emits one for the next.

## Setup

```bash
# Python tools
uv sync --all-extras

# TypeScript (loom)
cd loom/runtime && pnpm install

# Full pipeline (dry-run)
make pipeline brand=givecare persona=my-persona files=docs/ req="predict adoption" sidecar=sidecar.json
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

Every tool must support:
- `--json` → `{"status": "ok"|"error", "command": str, "data": {...}}`
- `agentcy-* doctor --json` → readiness check
- Exit: `0` success, `1` user error, `2` runtime error

## Guardrails

- `trash` not `rm`
- `git add <files>` never `.`
- echo's `camel-oasis==0.2.5` / `camel-ai==0.2.78` stay pinned — do not upgrade
- Never delete `echo/uploads/runs/` — artifacts are immutable products
- compass persona subcommands are deprecated — use `agentcy-vox` instead
- pulse absorbs lab: `agentcy-pulse calibrate` replaces `agentcy-lab calibration`

## Module names (Python imports unchanged)

Bins renamed; Python import paths preserved until explicit refactor:
- compass imports: `brand_os`
- echo imports: `app`
- pulse imports: `agentcy_pulse`
- vox imports: `prsna`
