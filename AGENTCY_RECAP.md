# Agentcy recap

The monorepo has consolidated package and CLI naming around `agentcy-*`, but the protocol layer still uses mixed writer identities on purpose.

- `writer.repo` should stay on the current literal repo name until a literal repo rename lands
- `writer.module` should already carry the future family module name

That means:

- operators install and run `agentcy-vox`, `agentcy-compass`, `agentcy-echo`, `agentcy-loom`, and `agentcy-pulse`
- protocol artifacts still emit legacy `writer.repo` values for backward compatibility and lineage stability
- tests, examples, and root docs should describe that split explicitly instead of assuming a full rename already happened

The current repo focus is stabilization: make the monorepo testable, keep the pipeline commands accurate, and remove startup failures that block basic help or smoke checks.
