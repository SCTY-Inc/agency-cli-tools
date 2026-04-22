.PHONY: install install-loom sync install-python-suite install-echo-simulation install-full-operator doctor check check-python check-loom test lint lint-full pipeline pipeline-fixtures

# Install Python workspace members + repo-local dev tools
install:
	uv sync --all-extras --group dev

# Install the base Python suite only (root CLI + protocols + vox + compass + echo base CLI + pulse)
install-python-suite:
	uv sync --group dev

# Add the Echo simulation runtime (Python 3.11 only)
install-echo-simulation:
	uv sync --extra simulation

# Install loom (TypeScript)
install-loom:
	cd loom/runtime && pnpm install

# Install the full local operator stack
install-full-operator: install-python-suite install-echo-simulation install-loom

# Sync without optional extras, but keep repo-local dev tools available
sync:
	uv sync --group dev

# Lightweight readiness checks

doctor:
	uv run agentcy doctor --json
	uv run agentcy-pulse doctor --json
	uv run agentcy-echo doctor --json
	cd loom/runtime && node bin/loom.js help --json > /dev/null

# Typecheck + test the maintained monorepo surfaces
check: check-python check-loom

check-python:
	uv run pytest tests compass/tests echo/tests pulse/tests vox/tests protocols/tests -q

check-loom:
	cd loom/runtime && pnpm check

# Run tests for a single member: make test member=compass
# Special cases:
#   make test member=root
#   make test member=protocols
#   make test member=loom

test:
	@if [ "$(member)" = "root" ]; then \
		uv run pytest tests -q; \
	elif [ "$(member)" = "protocols" ]; then \
		uv run pytest protocols/tests -q; \
	elif [ "$(member)" = "loom" ]; then \
		cd loom/runtime && pnpm test; \
	else \
		uv run pytest $(member)/tests -q; \
	fi

# Green lint path for the actively maintained consolidation surfaces
lint:
	uv run ruff check src tests pulse/src protocols/src

# Full lint inventory across the repo (currently expected to report legacy debt)
lint-full:
	uv run --with ruff ruff check compass/src echo/app pulse/src vox/src protocols/src src tests

# Run the canonical pipeline end-to-end.
# Requirements:
# - agentcy-echo simulation needs Python 3.11 + `uv sync --extra simulation`
# - loom runtime needs `make install-loom`
pipeline:
	@echo "==> vox: export voice pack"
	uv run agentcy-vox --json export $(persona) --to voice-pack.v1 > /tmp/voice_pack.json
	@echo "==> compass: generate canonical brief.v1"
	uv run agentcy-compass plan run "$(req)" --brand $(brand) --voice-pack-input /tmp/voice_pack.json --brief-v1-output /tmp/brief.json -f json > /tmp/brief_plan.json
	@echo "==> echo: forecast (requires Python 3.11 simulation runtime)"
	uv run agentcy-echo run --files $(files) --brief /tmp/brief.json --json > /tmp/forecast.json
	@echo "==> loom: execute"
	cd loom/runtime && node bin/loom.js run social.post --brand $(brand) --brief-file /tmp/brief.json --json > /tmp/run_result.json
	@echo "==> pulse: measure"
	uv run agentcy-pulse adapt --run-result /tmp/run_result.json --sidecar $(sidecar) --output /tmp/performance.json --json > /tmp/performance.stdout.json
	@echo "==> pulse: calibrate"
	uv run agentcy-pulse calibrate --forecast /tmp/forecast.json --performance /tmp/performance.json --json > /tmp/calibration.json

# Fixture-backed smoke path that proves downstream protocol plumbing without
# requiring the optional echo simulation runtime.
pipeline-fixtures:
	cp protocols/examples/voice_pack.v1.rich.json /tmp/voice_pack.json
	cp protocols/examples/brief.v1.rich.json /tmp/brief.json
	cp protocols/examples/forecast.v1.completed-rich.json /tmp/forecast.json
	cp protocols/examples/run_result.v1.published.json /tmp/run_result.json
	uv run agentcy-pulse adapt --run-result /tmp/run_result.json --sidecar $(sidecar) --output /tmp/performance.json --json > /tmp/performance.stdout.json
	uv run agentcy-pulse calibrate --forecast /tmp/forecast.json --performance /tmp/performance.json --json > /tmp/calibration.json
