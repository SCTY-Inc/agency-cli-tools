# Agentcy family loop-9 checkpoint — bounded `cli-prsna` / `agentcy-vox` package and CLI alias-readiness slice

Date: 2026-04-12
Status: active checkpoint; bounded proof recorded

This checkpoint is the narrow successor to the completed loop-8 `cli-phantom` / `agentcy-loom` package and CLI alias-readiness proof.
Loop 8 remains complete and locked as the prior packaged install/help checkpoint.
Loop 9 does not reopen family-wide rename work.
It stays limited to the bounded `cli-prsna` / `agentcy-vox` package and CLI alias-readiness slice.

## Prior slice completed, not reopened

The completed eighth bounded control-plane slice is:

`cli-phantom` / `agentcy-loom` package and CLI alias-readiness proof

Locked result:
- `family-loop-8-checkpoint-2026-04-12.md` remains the completed loop-8 checkpoint
- the loop-8 proof stays limited to the `cli-phantom` package metadata, explicit `loom-runtime` / `loom` alias policy, and packaged install/help readiness
- loop 9 exists to record the next bounded single-repo proof in `cli-prsna`, not to relitigate the loop-8 evidence or reopen family-wide naming work

## Loop-9 scope

The active ninth bounded control-plane slice is:

`cli-prsna` / `agentcy-vox` package target and CLI alias-readiness proof

Loop 9 is limited to:
- the `cli-prsna` repo and the minimal family docs needed to record this slice boundary
- the explicit package-target and CLI-alias policy for the current `prsna` / `persona` surfaces and future `agentcy-vox` direction
- the smallest package-manifest, installed-binary, or help-surface proof needed to establish honest alias readiness
- preserving canonical ownership in protocol artifacts and family docs

Loop 9 is explicitly not:
- a literal repo rename for `cli-prsna`
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- import-path rewrites
- cosmetic churn outside the package/CLI proof surface

## Canonical ownership stays locked

Loop 9 does not change artifact authority.
The canonical ownership rule remains:

- `voice_pack.v1.writer.repo = "cli-prsna"`
- `voice_pack.v1.writer.module = "agentcy-vox"`

That mixed writer contract must remain intact unless a later bounded task intentionally changes it.
Loop 9 is about package/bin alias readiness, not writer-field migration.

## Landed bounded proof

The loop-9 bounded proof is now recorded in:

- `cli-prsna/docs/packaged-install-help-proof-2026-04-12.md`

What that proof establishes:
- the currently shipped Python distribution/package remains `prsna`
- the currently shipped import path remains `prsna`
- the currently shipped installed operator-facing CLI remains `persona`
- from outside the repo root, the family now has bounded evidence for `uv build`, external wheel install, `persona --help`, `persona --version`, `persona export --list`, and unchanged `import prsna`

What that proof does not establish:
- no literal repo rename
- no import-path rewrite away from `prsna`
- no newly shipped installed alias such as `agentcy-vox` or `vox`
- no family-wide package or CLI normalization

## Why this slice exists

Loop 7 already established that `cli-prsna` is not rename-ready across repo, package, import, and CLI surfaces together.
The rename-readiness matrix records the live public surfaces as `prsna` for package/import and `persona` for CLI invocation.
The smallest next question was narrower than a repo rename:

- what package/distribution target should this repo prove first?
- what CLI alias policy should govern `persona` and any future additional alias?
- what installed-binary or help behavior can be honestly verified without widening into import migration or repo rename work?

This checkpoint opened that bounded question only.
The proof has now landed, but only for the currently shipped `persona` packaging surface.

## Required proof target

Loop 9 is considered successful because the bounded task recorded the smallest honest single-repo proof, including:

1. an explicit package-target and CLI-alias policy for `cli-prsna`
2. package metadata and command surfaces that match that policy exactly
3. verification from an operator path narrow enough to prove alias readiness honestly
4. at least one installed-binary or help-surface check
5. updated notes that preserve the difference between:
   - repo identity (`cli-prsna`)
   - module identity (`agentcy-vox`)
   - package/distribution identity
   - CLI binary identity

## Bounded implementation guidance

Within loop 9, prefer:
- explicit package/bin policy over speculative rename language
- package-manifest or entrypoint alignment over broad refactors
- installed-bin and help verification over source-first assumptions alone
- exact docs that explain the alias policy over broad branding edits

Avoid:
- import-path churn framed as package readiness work
- family-wide package or CLI normalization proposals
- changes that imply `writer.repo` should stop being `cli-prsna`
- broad README or marketing edits outside the bounded proof surface

## Validation gate for loop 9

Loop 9 is considered successful because:
- loop 8 remains clearly recorded as completed proof rather than active scope
- loop 9 is clearly framed as a single-repo `cli-prsna` proof slice
- the checkpoint preserves `writer.repo = "cli-prsna"` and `writer.module = "agentcy-vox"`
- the landed proof is stated precisely as `persona`-only packaged readiness plus unchanged `prsna` import compatibility
- literal repo renames remain explicitly deferred
- umbrella CLI work, MCP-first integration, broad runtime unification, monolith moves, import-path rewrites, and cosmetic churn remain explicitly deferred
- the proof target stays package and CLI alias-readiness rather than widening into a family rename campaign

## Deferrals still in force

The following remain explicitly deferred during loop 9:
- literal family repo renames
- umbrella CLI work
- MCP-first integration
- broad runtime unification
- monolith moves or deep repo merges
- import-path rewrites
- unnecessary code churn done only to cosmetically align names before readiness is proven

## Control-plane limit for this task

This checkpoint now records the landed proof and should stay aligned with:
- `AGENTCY_PROGRESS.md`
- `AGENTCY_STACK.md`
- `rename-readiness-matrix-2026-04-12.md`

Those family control-plane docs now move only to record the bounded evidence that actually landed, not to widen the scope.

## Bottom line

Loop 8 stays complete and locked as the bounded `cli-phantom` package/help proof.
Loop 9 is now the active narrow single-repo slice for `cli-prsna` / `agentcy-vox`, with bounded packaged proof recorded for the currently shipped `persona` CLI and unchanged `prsna` import surface only.
The writer contract stays `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`, and every broader rename, import, runtime, and monolith move remains explicitly deferred.
