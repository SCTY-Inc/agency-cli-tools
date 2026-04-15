# agentcy-pulse

Measurement and calibration member of the agentcy monorepo.

## Subcommands

```bash
agentcy-pulse adapt      --sidecar <sidecar.json> [--run-result <run.json>] [--output <performance.json>] [--json]
agentcy-pulse calibrate  --forecast <f.json> --performance <p.json> [--output <report.json>] [--json]
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
  --sidecar protocols/tests/fixtures/run_result_to_performance_v1/sidecar.rich.json \
  --output /tmp/performance.json \
  --json

agentcy-pulse calibrate \
  --forecast protocols/examples/forecast.v1.completed-rich.json \
  --performance /tmp/performance.json \
  --json
```

Legacy compatibility is still supported for `adapt`, so bare invocations like `agentcy-pulse --sidecar sidecar.json` are treated as `agentcy-pulse adapt --sidecar sidecar.json`.
