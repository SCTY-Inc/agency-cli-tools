# Agentcy stack

## Runtime layers

- Python workspace at the repo root via `uv`
- TypeScript runtime for Loom under `loom/runtime/` via `pnpm`
- Protocol schemas and examples under `protocols/`
- Thin root dispatcher in `src/agentcy/cli.py`

## Naming policy

The family stack intentionally separates package/bin naming from protocol lineage.

- `writer.module` tracks future family naming
- `writer.repo` must continue to reflect the current repo name until any literal repo rename actually lands

That split lets the monorepo expose unified `agentcy-*` CLIs without rewriting canonical lineage IDs or historical fixtures.

## CI path

The green path is:

1. Python + protocol tests from the root workspace
2. Loom `vitest` + `tsc --noEmit`
3. Maintained-surface Ruff checks for the consolidation layer

Repo-wide lint debt still exists, especially in `echo/app`, so the root CI path currently prefers passing contract tests over enforcing every historical style warning at once.
