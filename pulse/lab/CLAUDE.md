# CLAUDE.md

## Repo purpose

`agentcy-lab` is the minimal eval/autoresearch seed repo for the Agentcy family.

Current bounded scope:
- read canonical family fixtures from `../protocols/`
- compare `forecast.v1` against `performance.v1`
- emit a small calibration report

## Commands

```bash
uv sync
uv run agentcy-lab --help
uv run agentcy-lab doctor
uv run agentcy-lab calibration
uv run pytest
```

## Guardrails

- Keep this repo thin and cross-family
- Do not invent a canonical `lab` protocol unless the family actually needs one
- Prefer seams and reports over broad framework work
