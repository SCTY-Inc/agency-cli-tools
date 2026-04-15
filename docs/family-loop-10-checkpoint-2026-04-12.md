# Agentcy family loop-10 checkpoint — bounded `brand-os` / `agentcy-compass` blocker-reduction slice

Date: 2026-04-12
Status: active checkpoint; bounded blocker-reduction proof merged

This checkpoint is the narrow successor to the completed loop-9 `cli-prsna` / `agentcy-vox` package and CLI alias-readiness proof.
Loop 9 remains complete and locked as the prior packaged install/help checkpoint.
Loop 10 does not reopen family-wide rename work.
It stays limited to the bounded single-repo `brand-os` / future `agentcy-compass` blocker-reduction slice.

## Prior slice completed, not reopened

The completed ninth bounded control-plane slice is:

`cli-prsna` / `agentcy-vox` package and CLI alias-readiness proof

Locked result:
- `family-loop-9-checkpoint-2026-04-12.md` remains the completed loop-9 checkpoint
- the loop-9 proof stays limited to the `prsna` package/distribution, the explicit `persona`-first CLI policy, and packaged install/help readiness
- loop 10 exists to record the next bounded single-repo slice in `brand-os`, not to relitigate the loop-9 evidence or reopen family-wide naming work

## Loop-10 scope

The active tenth bounded control-plane slice is:

`brand-os` / `agentcy-compass` blocker-reduction and rename-readiness decomposition

Loop 10 is limited to:
- the `brand-os` repo and the minimal family docs needed to record this slice boundary
- explicit separation of naming drift from boundary and ownership drift inside `brand-os`
- an unresolved-before-rename list that stays first-class and repo-local rather than implied by family prose alone
- bounded proof work around the current package/distribution, import-path, CLI, and runtime/env/data-path blocker inventory
- preserving canonical ownership in protocol artifacts and family docs

The landed loop-10 proof now hardens four things without widening scope:
- repo-local docs explicitly distinguish naming-only, boundary-only, and mixed blockers in `brand-os/docs/rename-blocker-profile-2026-04-12.md`
- packaged install/help evidence now exists for the exact current compatibility surfaces `brand-os` / `brand_os` / `brandos` in `brand-os/docs/packaged-install-help-proof-2026-04-12.md`
- runtime/env/data-path evidence now exists for the still-mixed `.brand-os`, `.brandos`, `BRANDOS_*`, and `BRANDOPS_*` compatibility surface in `brand-os/docs/runtime-prefix-inventory-2026-04-12.md`
- the family control plane can now summarize loop 10 as bounded current-surface proof plus blocker decomposition, not as rename readiness

Loop 10 is explicitly not:
- a literal repo rename for `brand-os`
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- import-path rewrites
- large boundary rewrites
- cosmetic churn outside the blocker-reduction proof surface

## Canonical ownership stays locked

Loop 10 does not change artifact authority.
The canonical ownership rule remains:

- `brief.v1.writer.repo = "brand-os"`
- `brief.v1.writer.module = "agentcy-compass"`

That mixed writer contract must remain intact unless a later bounded task intentionally changes it.
Loop 10 is about blocker reduction and decomposition, not writer-field migration.

## Why this slice exists

Loop 7 already established that `brand-os` has the hardest blocker profile in the family.
The rename-readiness matrix records mixed public surfaces across:
- package/distribution name: `brand-os`
- import root: `brand_os`
- CLI binary: `brandos`
- runtime and data-path surfaces such as `~/.brand-os/...`, `BRANDOS_DATA_DIR`, and related current-name-first prefixes
- broader repo boundary drift involving persona, produce, eval, publish, queue, monitor, server, and residual `cli-agency` lineage

The next honest question is narrower than a rename claim:
- which blockers are naming-only and which are real boundary/ownership blockers?
- what unresolved surfaces must be recorded before any rename story can be credible?
- what can be proven through docs, inventories, and bounded validation before any code-level rename or runtime migration is attempted?

## Required outputs for loop 10

Loop 10 should leave behind a bounded control-plane result with:

1. `family-loop-10-checkpoint-2026-04-12.md` naming loop 10 as the active slice
2. `AGENTCY_STACK.md` and `AGENTCY_PROGRESS.md` updated so loop 9 is preserved as completed evidence rather than active scope
3. a first-class unresolved-before-rename artifact for `brand-os` that separates:
   - naming drift
   - boundary/ownership drift
   - current-surface proof
   - future rename claims
4. explicit repo-local validation commands for any package/help/import/runtime inventory work
5. conditional guidance for any future CLI/help edits rather than assuming code changes are required

Those outputs are now present in bounded form:
- the unresolved-before-rename artifact is `brand-os/docs/rename-blocker-profile-2026-04-12.md`
- the current shipped package/import/CLI proof is `brand-os/docs/packaged-install-help-proof-2026-04-12.md`
- the current runtime/env/data-path inventory is `brand-os/docs/runtime-prefix-inventory-2026-04-12.md`
- the verification commands remain repo-local and current-surface-first rather than assuming any future `agentcy-compass` rename path

## Parallel bounded work expected after re-anchor

After this re-anchor, the next bounded follow-ups may proceed in parallel as separate `brand-os` tasks:
- packaging and public-surface inventory (`brand-os`, `brand_os`, `brandos`, install metadata, help surfaces)
- runtime/env/data-path inventory (`~/.brand-os`, env vars, persisted state, side effects)

Those follow-ups must remain evidence-first.
They should not widen into import-path rewrites, broad runtime unification, or repo-boundary surgery.

## Validation gate for loop 10

Loop 10 is now considered correctly opened and partially evidenced because:
- loop 9 remains clearly recorded as completed proof rather than active scope
- loop 10 is clearly framed as a single-repo `brand-os` blocker-reduction slice
- the checkpoint preserves `writer.repo = "brand-os"` and `writer.module = "agentcy-compass"`
- the active problem is stated as blocker decomposition and evidence gathering, not rename execution
- landed proof is explicitly limited to current `brand-os` / `brand_os` / `brandos` compatibility surfaces plus runtime/env/data-path inventory
- naming drift is now recorded separately from boundary/ownership drift instead of being collapsed into a single rename-readiness claim
- literal repo renames remain explicitly deferred
- umbrella CLI work, MCP-first integration, import-path rewrites, broad runtime unification, monolith moves, large boundary rewrites, and cosmetic churn remain explicitly deferred

## Deferrals still in force

The following remain explicitly deferred during loop 10:
- literal family repo renames
- umbrella CLI work
- MCP-first integration
- import-path rewrites
- broad runtime unification
- runtime-prefix migrations as implementation work rather than inventory work
- monolith moves or deep repo merges
- large boundary rewrites
- unnecessary code churn done only to cosmetically align names before readiness is proven

## Control-plane limit for this task

This checkpoint now records the active loop-10 slice and should stay aligned with:
- `AGENTCY_PROGRESS.md`
- `AGENTCY_STACK.md`
- `rename-readiness-matrix-2026-04-12.md`

Those family control-plane docs should move only far enough to make loop 10 explicitly active and keep the bounded blocker-reduction scope honest.

## Bottom line

Loop 9 stays complete and locked as the bounded `cli-prsna` package/help proof.
Loop 10 remains the active narrow single-repo slice for `brand-os` / `agentcy-compass`, and the family now has bounded evidence for that slice: current packaged install/help proof on `brand-os` / `brand_os` / `brandos`, runtime/env/data-path inventory for mixed current prefixes, and an explicit unresolved-before-rename blocker profile that separates naming drift from true boundary/ownership drift.
The writer contract stays `brief.v1.writer = { repo: "brand-os", module: "agentcy-compass" }`, and every broader rename, umbrella CLI, MCP-first, import-path, runtime-unification, runtime-prefix migration, monolith, and large-boundary rewrite remains explicitly deferred.
