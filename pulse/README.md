# agentcy-pulse

Measurement and calibration member of the agentcy monorepo.

## Subcommands

```bash
agentcy-pulse adapt      --sidecar <sidecar.json> [--run-result <run.json>]   # → performance.v1
agentcy-pulse calibrate  --forecast <f.json> --performance <p.json>           # → calibration report
agentcy-pulse doctor                                                           # fixture check
```

Or via the dispatcher: `agentcy pulse adapt ...`

## Install

```bash
uv sync  # from monorepo root
```

## Example

```bash
agentcy-pulse adapt \
  --sidecar protocols/tests/fixtures/run_result_to_performance_v1/sidecar.rich.json

agentcy-pulse calibrate \
  --forecast protocols/examples/forecast.v1.completed-rich.json \
  --performance protocols/examples/performance.v1.rich.json
```
