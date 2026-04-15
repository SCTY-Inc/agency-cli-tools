# Agentcy family loop-8 checkpoint — bounded `cli-phantom` / `agentcy-loom` package and CLI alias-readiness slice

Date: 2026-04-12
Status: active checkpoint; single-repo proof slice

This checkpoint opens loop 8 as the narrow follow-up to the completed loop-7 rename-readiness audit.
Loop 7 remains the locked family-wide audit baseline.
Loop 8 does not reopen family-wide rename work. It opens only the bounded `cli-phantom` / `agentcy-loom` package and CLI alias-readiness slice.

## Prior slice completed, not reopened

The completed seventh bounded control-plane slice is:

`rename-readiness and canonical naming alignment audit`

Locked result:
- `family-loop-7-checkpoint-2026-04-12.md` remains the completed rename-readiness checkpoint
- the shared family audit template and `rename-readiness-matrix-2026-04-12.md` remain the authoritative loop-7 control-plane outputs
- loop 7 already established that `cli-phantom` is only partially aligned: Loom-shaped runtime surfaces exist, but packaged family binary readiness is still unproven
- loop 8 exists to prove or disprove that narrower package/bin surface honestly, not to relitigate the whole family naming matrix

## Loop-8 scope

The active eighth bounded control-plane slice is:

`cli-phantom` / `agentcy-loom` package metadata, CLI alias policy, and packaged install/help readiness

Loop 8 is limited to:
- the `cli-phantom` repo and the minimal family docs needed to record this slice boundary
- package metadata needed to support a packaged operator path
- the explicit `loom-runtime` / `loom` alias policy
- packaged install/help verification from outside the repo root
- the smallest entrypoint or packaging cleanup required to support that verification
- preserving canonical ownership in protocol artifacts and docs

Loop 8 is explicitly not:
- a literal repo rename for `cli-phantom`
- a package/import rename pass across the family
- umbrella CLI work
- MCP-first integration
- runtime-prefix migration
- broad runtime unification
- monolith moves or deep repo merges
- cosmetic churn outside the package/CLI proof surface

## Canonical ownership stays locked

Loop 8 does not change artifact authority.
The canonical ownership rule remains:

- `run_result.v1.writer.repo = "cli-phantom"`
- `run_result.v1.writer.module = "agentcy-loom"`

That mixed writer contract must remain intact unless a later bounded task intentionally changes it.
Loop 8 is about package/bin readiness, not writer-field migration.

## Why this slice exists

Loop 7 already showed that `cli-phantom` is ahead of the other repos on operator-facing Loom branding, but still not honest-to-claim as rename-ready.
The smallest remaining question is narrower than repo rename readiness:

- should `loom-runtime` be treated as the durable package/distribution alias?
- should `loom` be treated as the durable CLI alias?
- can an installed packaged binary be verified from outside the repo root?
- can help behavior be proven in packaged form rather than only through source-first `npx tsx src/cli.ts ...` flows?

Those answers are now proven in the bounded loop-8 sense through the repo-local proof record `cli-phantom/docs/packaged-install-help-proof-2026-04-12.md`.
That proof covers `npm pack`, local tarball install from `/tmp`, `loom --help`, and `loom help --json` from outside the repo root.
The family therefore gains one bounded package/bin readiness result without widening into rename theatre.

## Required proof target

Loop 8 should only be considered successful if it can record the smallest honest packaged proof, including:

1. an explicit alias policy for `loom-runtime` and `loom`
2. package metadata that supports the intended installed-binary path
3. verification from a directory outside `cli-phantom`
4. at least one packaged help check such as:
   - `loom --help`
   - `loom help --json`
5. updated control-plane notes that preserve the difference between:
   - repo identity (`cli-phantom`)
   - module identity (`agentcy-loom`)
   - package/distribution alias (`loom-runtime` if retained)
   - CLI alias (`loom` if retained)

## Bounded implementation guidance

Within loop 8, prefer:
- package-manifest changes over runtime rewiring
- installed-bin verification over speculative renaming
- exact docs that explain alias policy over broad branding edits
- one proof path over multiple parallel packaging strategies

Avoid:
- changing runtime prefixes or state-directory names
- broad README/marketing churn outside the install/help surface
- family-wide package or import naming proposals
- any change that would imply `writer.repo` should stop being `cli-phantom`

## Validation gate for loop 8

Loop 8 should be considered successful only if:
- loop 7 remains clearly recorded as completed rename-readiness evidence
- loop 8 is clearly framed as a single-repo proof slice
- the checkpoint preserves `writer.repo = "cli-phantom"` and `writer.module = "agentcy-loom"`
- literal repo renames remain explicitly deferred
- umbrella CLI work, MCP-first integration, runtime-prefix migration, broad runtime unification, monolith moves, and cosmetic churn remain explicitly deferred
- the proof target is packaged install/help readiness, not only in-repo source execution

Loop-8 status against that gate is now:
- passed via `cli-phantom/docs/packaged-install-help-proof-2026-04-12.md`
- exact recorded commands include `npm pack`, local tarball install, `loom --help`, and `loom help --json`
- the verified installed binary surface is `loom` from outside the repo root
- no repo rename and no `agentcy-loom` binary claim were made

## Deferrals still in force

The following remain explicitly deferred during loop 8:
- literal family repo renames
- umbrella CLI work
- MCP-first integration
- runtime-prefix migration
- broad runtime unification
- monolith moves or deep repo merges
- heavy `cli-metrics` repo bootstrap
- live analytics platform integrations
- broad metric abstractions beyond published `social.post`
- unnecessary code churn done only to cosmetically align names before readiness is proven

## Bottom line

Loop 7 stays complete and locked as the family rename-readiness audit wave.
Loop 8 has now landed its bounded `cli-phantom` / `agentcy-loom` package and CLI alias-readiness proof.
The verified result is narrow: `loom-runtime` remains a transitional package alias, installed `loom` help works from outside the repo root, canonical ownership stays `writer.repo = "cli-phantom"` and `writer.module = "agentcy-loom"`, and every broader rename/runtime migration remains explicitly deferred.
