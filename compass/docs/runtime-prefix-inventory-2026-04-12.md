# brand-os runtime/env/data-path prefix inventory — 2026-04-12

## Scope

This is a compatibility/blocker inventory for loop 10. It documents the current `brand-os` runtime surface without migrating prefixes, moving local state, or claiming rename-readiness.

## Why this exists

`brand-os` currently exposes more than one naming family across config lookup, env vars, and runtime data paths:

- repo/package naming: `brand-os`
- import root: `brand_os`
- installed CLI: `brandos`
- config file: `brandos.yml`
- config/env namespace: `BRANDOPS_*`
- runtime data-dir override: `BRANDOS_DATA_DIR`
- config-model default data path: `~/.brandos`
- runtime storage default data path: `~/.brand-os`

That split is a blocker surface to inventory honestly before any future rename or migration story.

## Current compatibility surface

### 1. Config file resolution

Source: `src/brand_os/core/config.py`

Current order:

1. explicit `load_config(path=...)` argument
2. `BRANDOPS_CONFIG`
3. repo-local `./brandos.yml`
4. home config `~/.brandos/config.yml`
5. in-memory defaults from `BrandOpsConfig`

Current default model values when no config file is found:

- `brands_dir = Path("brands")`
- `data_dir = Path.home() / ".brandos"`
- `default_provider = "gemini"`
- `default_model = None`

Compatibility note: config lookup uses the `brandos` / `BRANDOPS` family, not the `brand-os` path family.

### 2. Generic env-prefix behavior

Source: `src/brand_os/core/config.py`

`get_env(key)` resolves environment variables as `BRANDOPS_{key.upper()}`.

Examples currently present in repo code:

- `BRANDOPS_CONFIG`
- `BRANDOPS_LLM_PROVIDER`
- `BRANDOPS_FROM_EMAIL`
- any future `get_env(...)`-style lookups under the same prefix

Compatibility note: this preserves an ops/config namespace shaped like `BRANDOPS_*` rather than `BRANDOS_*`.

### 3. Runtime data-dir resolution

Source: `src/brand_os/core/storage.py`

Current order:

1. `BRANDOS_DATA_DIR`
2. default runtime path `~/.brand-os`

Subdirectories created under that runtime root include:

- `outputs/`
- `identities/`
- `decisions/`
- `learning/`
- `signals/`
- `campaigns/`
- `personas/`
- `queues/`
- other feature-local directories built from `data_dir()`

Compatibility note: runtime storage uses the `BRANDOS` / `.brand-os` family, which does not match the config-model default `~/.brandos`.

### 4. Write action path behavior

Source: `src/brand_os/actions/write.py`

`WriteAction()` defaults to:

- `data_dir() / "outputs"`
- therefore the current runtime default path family is `~/.brand-os/outputs/...`

Compatibility note: write/audit outputs follow storage resolution, not `BrandOpsConfig.data_dir`.

## Deterministic compatibility checks added in this task

Targeted tests now verify the current behavior rather than a desired future cleanup:

- config candidate order remains `brandos.yml` then `~/.brandos/config.yml`
- `BRANDOPS_CONFIG` overrides default config candidates
- `get_env()` keeps the `BRANDOPS_*` prefix contract
- `BrandOpsConfig.data_dir` still defaults to `~/.brandos`
- runtime storage still defaults to `~/.brand-os`
- `BRANDOS_DATA_DIR` still overrides runtime storage
- `WriteAction` still writes under the storage/runtime path family

## Exact verification commands

Run from repo root:

```bash
cd brand-os && uv run pytest tests/core/test_runtime_prefix_compat.py
cd brand-os && uv run pytest tests/plan/test_brief_v1.py
```

The second command is unchanged repo-local regression coverage kept here as supporting proof that the new compatibility checks do not reopen the existing brief surface.

## Interpretation for loop 10

This is evidence of a mixed compatibility surface, not a migration plan.

What this doc proves:

- `brand-os` is not rename-ready across runtime/env/data-path surfaces
- `~/.brandos` and `~/.brand-os` are both live compatibility facts today
- `BRANDOPS_*` and `BRANDOS_DATA_DIR` are both live compatibility facts today
- the installed CLI/config filename family (`brandos`) is still distinct from part of the runtime storage family (`brand-os`)

What this doc does not do:

- no env-prefix rename
- no config-file rename
- no local-state move
- no import-path rewrite
- no claim that one namespace has been chosen as the future winner
