# agentcy-lab

Minimal birth slice for the shared `agentcy-lab` eval/autoresearch plane.

This repo is intentionally tiny and only proves one cross-family seam:

- input authorities:
  - `../protocols/examples/forecast.v1.completed-rich.json`
  - `../protocols/examples/performance.v1.rich.json`
- repo-local output: a calibration report that compares forecast intent with observed performance
- non-goal: claiming a canonical `lab` protocol before the family needs one

## Install

```bash
uv sync
```

## Smoke checks

```bash
uv run agentcy-lab --help
uv run agentcy-lab doctor
uv run agentcy-lab calibration
uv run python -c "import agentcy_lab"
uv run pytest
```

The repo-local test suite keeps the canonical family-fixture calibration check when sibling `../protocols/` fixtures are available and still runs standalone CLI smoke tests when they are not.

## Example

```bash
uv run agentcy-lab calibration \
  --forecast ../protocols/examples/forecast.v1.completed-rich.json \
  --performance ../protocols/examples/performance.v1.rich.json
```
