# Agentcy family loop-7 checkpoint — bounded rename-readiness and canonical naming alignment

Date: 2026-04-12
Status: active checkpoint; docs, audit, and validation only

This checkpoint opens loop 7 as a bounded family control-plane wave for rename-readiness and canonical naming alignment.
Loop 6 is complete and remains the locked seam-proof checkpoint for canonical published `run_result.v1 -> performance.v1`.
Loop 7 does not authorize literal repo renames. It exists to determine what must be true before the current repos can honestly adopt the family names `agentcy-vox`, `agentcy-compass`, `agentcy-echo`, `agentcy-loom`, and `agentcy-pulse`.

## Prior slice completed, not reopened

The completed sixth bounded slice is:

`agentcy-pulse` thin fixture or tiny adapter seam for canonical published `run_result.v1 -> performance.v1`

Locked result:
- `family-loop-6-checkpoint-2026-04-12.md` remains the completed seam-proof checkpoint
- loop 5 remains the locked protocol baseline for that seam
- canonical published `run_result.v1` and canonical `performance.v1` ownership remain unchanged
- loop 7 naming work must not reopen pulse seam scope, source-fixture authority, or privacy bounds

## Loop-7 scope

The active seventh bounded control-plane slice is:

`rename-readiness and canonical naming alignment audit`

Loop 7 is limited to:
- family docs that make the rename-readiness wave explicit
- a shared audit template that every repo-local naming scan can use
- validation of naming surfaces against the canonical family map
- classification of blockers, legacy aliases, and target names before any rename is proposed
- preserving the already-locked artifact ownership and protocol authority while names are audited

Loop 7 is explicitly not:
- literal repo directory renames
- package or distribution renames executed across the family by default
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- a justification for broad code churn just to cosmetically align names

## Canonical naming intent

Current family target names remain:
- `cli-prsna` -> `agentcy-vox`
- `brand-os` -> `agentcy-compass`
- `cli-mirofish` -> `agentcy-echo`
- `cli-phantom` -> `agentcy-loom`
- `cli-metrics` / future repo -> `agentcy-pulse`
- shared eval/autoresearch -> `agentcy-lab`

Loop 7 is about readiness for those names, not execution of those renames.

## Locked naming invariants

The following naming invariants remain in force during loop 7:
- canonical artifact ownership does not change
- `writer.module` may already use the future family module name where that was previously locked as canonical
- `writer.repo` must continue to reflect the current literal repo name until a real repo rename lands
- canonical fixtures, examples, and tests should not be rewritten broadly just to mimic a rename that has not happened
- install surfaces, binaries, import paths, and runtime keys must be classified honestly rather than prematurely normalized

## Shared loop-7 rename-readiness audit template

Every repo-local or family-level naming audit should use the same structure.

### Required audit metadata

- repo under audit
- date
- auditor or task id
- source docs consulted
- summary readiness verdict

### Required naming surfaces

For each of the following surfaces, record all four required classifications:
1. repo directory name
2. package/distribution name
3. import path
4. CLI binary
5. docs/install branding
6. artifact writer fields
7. fixture/test references
8. runtime path/key prefixes

### Required per-surface classifications

For each surface above, include:
- **Current canonical:** the authoritative name or value that should be treated as correct today
- **Post-rename target:** the future family-aligned name or value that would be correct after a literal rename lands
- **Acceptable legacy alias:** any old name that may continue to exist temporarily without violating control-plane correctness
- **Hard blocker:** the concrete reason this surface is not yet safely rename-ready, or `none` if no blocker is known

### Audit table template

| Surface | Current canonical | Post-rename target | Acceptable legacy alias | Hard blocker |
| --- | --- | --- | --- | --- |
| Repo directory name |  |  |  |  |
| Package/distribution name |  |  |  |  |
| Import path |  |  |  |  |
| CLI binary |  |  |  |  |
| Docs/install branding |  |  |  |  |
| Artifact writer fields |  |  |  |  |
| Fixture/test references |  |  |  |  |
| Runtime path/key prefixes |  |  |  |  |

### Required narrative sections after the table

1. **Canonical surfaces already aligned**
   - list surfaces that already match the future family intent or already follow the locked writer/module rule
2. **Safe legacy aliases**
   - list the aliases that may remain temporarily and why they do not create a second authority
3. **Hard blockers to literal rename**
   - list concrete blockers, with the smallest honest fix or validation still needed
4. **Bounded next actions**
   - docs, fixture, package-manifest, or validation tasks only
5. **Explicit non-goals**
   - restate that this audit is not authorizing runtime rewrites or broad rename churn

## Repo-specific expectations to test against

Loop 7 should expect different blocker profiles across the family:
- `brand-os` is likely the hardest blocker because naming drift and ownership drift both remain meaningful risks
- `cli-prsna` likely has legacy package/import/CLI surfaces that need explicit classification
- `cli-mirofish` adds upstream naming and AGPL-coupling constraints that must be called out rather than hand-waved
- `cli-phantom` likely has mixed repo/runtime naming that must be classified surface by surface
- `cli-metrics` is blocked first by missing birth-contract clarity, not by implementation polish

These expectations are prompts for honest audits, not pre-approved conclusions.

## Family naming matrix

The family-owned current-vs-target naming matrix for loop 7 now lives in `rename-readiness-matrix-2026-04-12.md`.

That matrix adds three control-plane outputs beyond the generic audit template:
- one current-vs-target inventory row for each future module
- an explicit family-wide statement that `writer.module` already follows future family naming while `writer.repo` must stay on the current literal repo name until a real repo rename lands
- the minimum verification evidence required before repo-directory, package/distribution, import-path, or CLI-binary rename readiness may be claimed

Repo-local loop-7 audits should use the shared template in this checkpoint and cite the family matrix when classifying their own surfaces.

## Merged findings and smallest next actions

### Family-wide result after the repo-local audits

Loop 7 now has enough evidence to summarize the family without reopening validation:

- every active family artifact is already aligned on the mixed canonical writer rule (`writer.repo` = current repo name, `writer.module` = future family module name)
- no current repo is honest-to-rename at every naming surface together
- repo-directory rename readiness remains deferred everywhere because literal repo renames would force `writer.repo`, path, docs, and operator migration decisions that are not yet proven
- package/import/CLI readiness must be treated as separate questions rather than collapsed into a single “rename-ready” label
- the smallest next actions are still docs, compatibility-policy, and bounded verification tasks rather than runtime rewrites

### By-repo synthesis

1. `cli-prsna` / `agentcy-vox`
   - artifact-writer surface is already aligned
   - repo/package/import/CLI surfaces are still legacy-first (`cli-prsna`, `prsna`, `prsna`, `persona`)
   - the key blocker is that import-path migration is deeper than a branding change
   - smallest next action: choose a future package/bin target and alias policy before any rename claim

2. `brand-os` / `agentcy-compass`
   - artifact-writer surface is already aligned
   - this remains the hardest repo-level blocker because naming drift overlaps real boundary/ownership drift
   - package/import/CLI/runtime-prefix surfaces all still point at `brand-os` / `brand_os` / `brandos`
   - smallest next action: narrow the repo boundary and keep runtime/env-prefix migration separate from any public rename discussion

3. `cli-mirofish` / `agentcy-echo`
   - artifact-writer surface is already aligned
   - repo/package/import/CLI are blocked by explicit upstream MiroFish/AGPL lineage plus the generic import root `app`
   - smallest next action: define attribution-preserving compatibility policy before touching package/import/bin surfaces

4. `cli-phantom` / `agentcy-loom`
   - artifact-writer surface is already aligned
   - runtime package/docs/CLI are already Loom-shaped, but repo identity remains Phantom-shaped on purpose
   - smallest next action: decide whether `loom-runtime` and `loom` are durable aliases and prove a packaged install/help path before any family-name claim

5. future `cli-metrics` / `agentcy-pulse`
   - protocol-layer writer surface is already aligned
   - all repo/package/import/CLI readiness questions remain pre-implementation
   - smallest next action: treat `cli-metrics-birth-contract-2026-04-12.md` as the required gate for repo birth

### Control-plane decisions locked by this merge

- literal repo renames remain deferred everywhere
- package/distribution rename readiness is not the same as import-path readiness
- import-path migrations in Python repos are separate compatibility projects, not “free” byproducts of branding changes
- CLI rename readiness requires explicit alias behavior and command verification, not just a target name
- runtime/env/data-path prefix changes remain separate migrations and should not be bundled into rename-readiness claims unless their compatibility story is documented first
- `brand-os` / `cli-agency` historical overlap remains a repo-boundary blocker, not a reason to reopen broad merge work

## Validation gate for loop 7

Loop 7 should be considered successful only if:
- loop 6 remains clearly recorded as complete
- loop 7 is clearly framed as docs, audit, and validation only
- the shared audit template is published once at the control-plane level
- the family naming matrix is published once at the control-plane level
- the template covers every required naming surface
- the template requires all four per-surface classifications
- the matrix makes the `writer.module` vs `writer.repo` split explicit
- the matrix defines minimum readiness evidence for repo, package, import, and CLI rename claims
- explicit deferrals remain in force for literal repo renames, umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, and unnecessary code churn
- repo-local work can now report rename-readiness in a uniform shape without changing canonical ownership or triggering broad implementation churn

## Deferrals still in force

The following remain explicitly deferred during loop 7:
- literal family repo renames
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- heavy `cli-metrics` repo bootstrap
- live analytics platform integrations
- broad analytics abstractions beyond published `social.post`
- unnecessary code churn done only to cosmetically align names before readiness is proven

These deferrals remain in force because loop 7 is a control-plane readiness wave, not a rename execution wave.

## Bottom line

Loop 6 is complete and stays locked.
Loop 7 is now active as the bounded family rename-readiness and canonical naming alignment wave.
The family should audit names honestly, classify blockers explicitly, and publish uniform readiness evidence before any literal repo rename is considered.