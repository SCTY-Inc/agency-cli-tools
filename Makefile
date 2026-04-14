.PHONY: install install-loom sync check test lint pipeline

# Install all Python workspace members
install:
	uv sync --all-extras

# Install loom (TypeScript)
install-loom:
	cd loom/runtime && pnpm install

# Sync without extras (fast)
sync:
	uv sync

# Typecheck + test all Python members
check:
	uv run pytest compass/tests echo/tests pulse/tests vox/tests -x
	cd loom/runtime && pnpm check

# Run tests for a single member: make test member=compass
test:
	uv run pytest $(member)/tests -x

# Lint all Python
lint:
	uv run ruff check compass/src echo/app pulse/src vox/src
	uv run ruff format --check compass/src echo/app pulse/src vox/src

# Run the canonical pipeline end-to-end (dry-run)
pipeline:
	@echo "==> vox: export voice pack"
	uv run agentcy-vox export $(persona) --to voice-pack.v1 --json > /tmp/voice_pack.json
	@echo "==> compass: generate brief"
	uv run agentcy-compass plan --brand $(brand) --json > /tmp/brief.json
	@echo "==> echo: forecast"
	uv run agentcy-echo run --files $(files) --requirement "$(req)" --brief /tmp/brief.json --json > /tmp/forecast.json
	@echo "==> loom: execute"
	cd loom/runtime && agentcy-loom run social.post --brand $(brand) --brief-file /tmp/brief.json --json > /tmp/run_result.json
	@echo "==> pulse: measure"
	uv run agentcy-pulse adapt --run-result /tmp/run_result.json --sidecar $(sidecar) --json > /tmp/performance.json
	@echo "==> pulse: calibrate"
	uv run agentcy-pulse calibrate --forecast /tmp/forecast.json --performance /tmp/performance.json
