# Agentcy progress

## Current phase

Post-consolidation stabilization.

## Completed in this pass

- aligned root docs and commands around the current `agentcy-*` package/bin names
- kept canonical writer fixtures on their existing mixed repo/module pairs
- added a root CI workflow and repo-local dispatcher tests
- fixed root doctor so it checks reachability, not just binary presence
- updated pulse to support legacy bare adapt invocation and `--json` envelopes
- fixed Loom help/runtime startup by lazy-loading command modules and falling back when native canvas is unavailable
- corrected stale protocol test paths to the monorepo layout

## Ongoing rules

- `writer.module` may remain on the future family-name track
- `writer.repo` must still reflect the current repo name until any literal rename actually lands

## Remaining work

- reduce the larger lint backlog, especially under `echo/app`
- deepen coverage in the biggest forecast/runtime files
- finish the unfinished autonomous execution handlers in Compass
- decide whether to migrate the protocol writer repos in a future, explicit lineage-breaking task
