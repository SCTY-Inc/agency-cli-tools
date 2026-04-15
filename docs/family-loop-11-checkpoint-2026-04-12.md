# Agentcy family loop-11 checkpoint — bounded `cli-mirofish` / `agentcy-echo` attribution-preserving compatibility slice

Date: 2026-04-12
Status: active checkpoint; bounded compatibility-planning slice

This checkpoint is the narrow successor to the completed loop-10 `brand-os` / `agentcy-compass` blocker-reduction proof.
Loop 10 remains complete and locked as the prior bounded `brand-os` evidence checkpoint.
Loop 11 does not reopen family-wide rename work.
It stays limited to the bounded single-repo `cli-mirofish` / future `agentcy-echo` compatibility-planning slice.

## Prior slice completed, not reopened

The completed tenth bounded control-plane slice is:

`brand-os` / `agentcy-compass` blocker-reduction and rename-readiness decomposition

Locked result:
- `family-loop-10-checkpoint-2026-04-12.md` remains the completed loop-10 checkpoint
- the loop-10 proof stays limited to current-surface `brand-os` / `brand_os` / `brandos` compatibility evidence, runtime/env/data-path inventory, and explicit separation of naming drift from boundary/ownership drift
- loop 11 exists to record the next bounded single-repo slice in `cli-mirofish`, not to relitigate the loop-10 evidence or reopen family-wide naming work

## Loop-11 scope

The active eleventh bounded control-plane slice is:

`cli-mirofish` / `agentcy-echo` attribution-preserving package/import/bin compatibility planning

Loop 11 is limited to:
- the `cli-mirofish` repo and the minimal family docs needed to record this slice boundary
- explicit preservation of upstream MiroFish lineage, attribution, and AGPL-aware compatibility constraints
- package/distribution, import-root, and CLI-binary inventory and planning only
- documenting the generic top-level `app` import-root problem as a compatibility blocker rather than silently treating it as a rename-ready surface
- recording the smallest honest current-surface proof targets and unresolved-before-rename blockers before any public-name migration claim is made
- preserving canonical ownership in protocol artifacts and family docs

Loop 11 is explicitly not:
- a literal repo rename for `cli-mirofish`
- package/distribution rename execution
- import-path rewrites
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- cosmetic churn outside the compatibility-planning proof surface

## Canonical ownership stays locked

Loop 11 does not change artifact authority.
The canonical ownership rule remains:

- `forecast.v1.writer.repo = "cli-mirofish"`
- `forecast.v1.writer.module = "agentcy-echo"`

That mixed writer contract must remain intact unless a later bounded task intentionally changes it.
Loop 11 is about attribution-preserving compatibility planning, not writer-field migration.

## Why this slice exists

Loop 7 already established that `cli-mirofish` is not rename-ready across package, import, CLI, and lineage surfaces together.
The family matrix records the concrete blocker profile across:
- package/distribution name: `mirofish-backend`
- import root: `app`
- CLI binary: `mirofish`
- repo/docs/product language that still explicitly reference upstream `MiroFish` lineage
- AGPL and fork-history constraints that make attribution-preserving compatibility more important than cosmetic family-name alignment

The next honest question is narrower than a rename claim:
- what current package/import/bin surfaces are actually public and must be preserved or explicitly aliased?
- what attribution and lineage language must remain first-class in any future compatibility policy?
- what is the smallest executable or documented proof surface that can be landed without rewriting imports, renaming packages, or flattening upstream history into family branding?
- which blockers must stay explicitly unresolved before any rename story can be credible?

## Required outputs for loop 11

Loop 11 should leave behind a bounded control-plane result with:

1. `family-loop-11-checkpoint-2026-04-12.md` naming loop 11 as the active slice
2. `AGENTCY_STACK.md` and `AGENTCY_PROGRESS.md` updated so loop 10 is preserved as completed evidence rather than active scope
3. repo-local `cli-mirofish` docs that inventory package/distribution, import-root, and CLI surfaces and publish an attribution-preserving compatibility policy
4. explicit preservation of the locked writer contract `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`
5. explicit deferrals for literal repo renames, package/import/bin rewrite execution, umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, and cosmetic churn

## Landed loop-11 evidence now merged into this checkpoint

The bounded repo-local follow-ups for loop 11 have now landed and should be treated as evidence, not as authorization to widen scope:
- `cli-mirofish/docs/rename-readiness-scorecard-2026-04-12.md` now serves as the repo-local authority doc for the attribution-preserving alias policy, blocker-type separation, and unresolved-before-rename checklist
- `cli-mirofish/docs/packaged-compatibility-proof-boundary-2026-04-12.md` now records the exact current-surface proof boundary for `mirofish-backend` / `app` / `mirofish`

What that landed evidence now means at the family layer:
- current shipped compatibility surfaces remain `cli-mirofish` / `mirofish-backend` / `app` / `mirofish`
- upstream `MiroFish` lineage and AGPL-aware attribution remain first-class and must stay visible in any future family framing
- the generic top-level import root `app` is a distinct blocker that cannot be hand-waved as a shallow alias or cosmetic rename
- the current proof boundary applies only to present compatibility surfaces: repo-local build/help/import proof exists, the tiny public-surface regression test exists, and the narrow `brief.v1 -> forecast.v1` protocol seam remains proven
- clean external wheel-install proof, external installed-CLI proof, and external import proof remain unproven because dependency resolution still fails on reproduced `camel-oasis==0.2.5`

This merged checkpoint still does not authorize import-path rewrites, package renames, repo renames, or broad runtime unification work.

## Validation gate for loop 11

Loop 11 is considered correctly opened and now correctly merged only if:
- loop 10 remains clearly recorded as completed bounded `brand-os` evidence rather than active scope
- loop 11 is clearly framed as a single-repo `cli-mirofish` compatibility-planning slice
- the checkpoint preserves `writer.repo = "cli-mirofish"` and `writer.module = "agentcy-echo"`
- the active problem is stated as attribution-preserving package/import/bin compatibility planning, not rename execution
- the generic `app` import root is recorded as a blocker to be planned around, not hand-waved away
- upstream MiroFish lineage and AGPL-aware attribution constraints stay explicit
- the current proof boundary is stated narrowly as present-compatibility-surface evidence only, not as a completed rename-ready or external packaged-proof claim
- the unresolved external dependency/install blocker `camel-oasis==0.2.5` remains explicit wherever external packaged proof is summarized
- literal repo renames remain explicitly deferred
- umbrella CLI work, MCP-first integration, import-path rewrites, broad runtime unification, monolith moves, and cosmetic churn remain explicitly deferred

## Deferrals still in force

The following remain explicitly deferred during loop 11:
- literal family repo renames
- package/distribution rename execution
- import-path rewrites
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- runtime-wide cleanup outside the package/import/bin planning surface
- unnecessary code churn done only to cosmetically align names before compatibility readiness is proven

## Control-plane limit for this task

This checkpoint now records the active loop-11 slice and should stay aligned with:
- `AGENTCY_PROGRESS.md`
- `AGENTCY_STACK.md`
- `rename-readiness-matrix-2026-04-12.md`

Those family control-plane docs should move only far enough to make loop 11 explicitly active and keep the bounded compatibility-planning scope honest.

## Bottom line

Loop 10 stays complete and locked as the bounded `brand-os` blocker-reduction proof.
Loop 11 is now the active narrow single-repo slice for `cli-mirofish` / `agentcy-echo`, focused on attribution-preserving package/distribution, import-root, and CLI compatibility planning around the current `mirofish-backend`, `app`, and `mirofish` surfaces.
The writer contract stays `forecast.v1.writer = { repo: "cli-mirofish", module: "agentcy-echo" }`.
The merged family evidence now says only this: the alias policy is attribution-preserving, the generic `app` import root remains a real blocker, and the exact proof boundary covers current repo-local compatibility surfaces plus the narrow protocol seam only.
It does not justify a repo/package/import/bin rename claim, and it does not justify claiming external packaged proof while `camel-oasis==0.2.5` still blocks clean wheel installation.
Every broader repo rename, package rename, import rewrite, umbrella CLI, MCP-first, runtime-unification, monolith, and cosmetic-churn path remains explicitly deferred.