# [cli-phantom] agentcy-loom runtime/package/bin drift review — 2026-04-14

Scope: bounded repo-local review of the live `agentcy-loom/` Node runtime surfaces around `run_result.v1`, package/bin naming, CLI entrypoints, packaged-help evidence, and local git-state reality.

## Result

`agentcy-loom/` is still the Loom runtime in practice, but it remains an intentionally mixed-surface repo:

- live repo directory: `agentcy-loom`
- preserved canonical writer repo for the artifact contract: `cli-phantom`
- canonical writer module: `agentcy-loom`
- current package/distribution surface: `loom-runtime`
- current installed CLI binary: `loom`
- current source CLI entrypoint: `runtime/src/cli.ts`
- current packaged bin shim: `runtime/bin/loom.js`

The bounded conclusion is the same one the family docs already point toward: the Node runtime/package/bin surface is mostly coherent, but repo-local docs still carry some pre-rename `cli-phantom` path narration and should be treated as compatibility/history language, not evidence of a completed repo/package normalization.

## Evidence reviewed

Files inspected:

- `agentcy-loom/README.md`
- `agentcy-loom/CLAUDE.md`
- `agentcy-loom/runtime/package.json`
- `agentcy-loom/runtime/src/cli.ts`
- `agentcy-loom/runtime/src/cli/index.ts`
- `agentcy-loom/runtime/bin/loom.js`
- `agentcy-loom/docs/packaged-install-help-proof-2026-04-12.md`
- `agentcy-loom/docs/package-cli-alias-readiness-2026-04-12.md`
- `agentcy-loom/runtime/src/domain/run-result-v1.ts`

Commands reviewed or run:

```bash
cd agentcy-loom && git status --short --branch
cd agentcy-loom && git diff --stat
cd agentcy-loom/runtime && node bin/loom.js --help
cd agentcy-loom/runtime && node bin/loom.js help --json
cd agentcy-loom/runtime && npm test
```

## Current branch and dirty-state facts

Observed local git state:

```text
## main...origin/main [ahead 9]
 M .gitignore
 M docs/packaged-install-help-proof-2026-04-12.md
 M runtime/src/cli/index.ts
```

Observed diff summary:

```text
 .gitignore                                     |  3 +++
 docs/packaged-install-help-proof-2026-04-12.md | 17 +++++++++++++++--
 runtime/src/cli/index.ts                       |  3 ++-
```

Interpretation:

- the repo is not clean during this review
- the active dirty files are narrow and local to ignore rules plus CLI/help text proof updates
- the dirty-state evidence is compatible with a bounded Node help-surface refresh, not a rename execution wave

## Package/bin/source-entrypoint truth

### Package metadata

`agentcy-loom/runtime/package.json` currently declares:

```json
{
  "name": "loom-runtime",
  "bin": {
    "loom": "./bin/loom.js"
  }
}
```

That means the live Node package/bin truth is:

- npm package name: `loom-runtime`
- installed executable name: `loom`
- packaged executable shim: `runtime/bin/loom.js`

### Source CLI path

The developer/source-first entrypoint remains:

```text
agentcy-loom/runtime/src/cli.ts
```

That file simply calls `runCli()` from:

```text
agentcy-loom/runtime/src/cli/index.ts
```

### Packaged shim behavior

`runtime/bin/loom.js` is a Node bin shim that resolves `../src/cli.ts` and launches it through:

```text
node --import tsx <resolved-cli-path>
```

So the current package/bin model is:

1. installed command `loom`
2. executes `bin/loom.js`
3. shim dispatches to `src/cli.ts`
4. `src/cli.ts` calls `runCli()` in `src/cli/index.ts`

This is a real Node-packaged CLI path, not just a Python-style or source-only assumption.

## Node-proof parity

This task explicitly required Node-proof parity rather than Python-only checking.

Observed local Node proof:

- `cd agentcy-loom/runtime && node bin/loom.js --help` succeeded
- `cd agentcy-loom/runtime && node bin/loom.js help --json` succeeded
- `cd agentcy-loom/runtime && npm test` passed (`31` tests)

This is the right proof shape for this repo because the runtime is TypeScript/Node-based. The review should therefore prefer:

- package metadata and bin shim inspection
- direct CLI help execution from the Node side
- runtime test execution via npm/vitest

and not treat Python-oriented import/help proof as the primary verification surface.

## `run_result.v1` writer contract

The canonical writer contract remains correctly locked in runtime code and repo docs:

```json
{
  "repo": "cli-phantom",
  "module": "agentcy-loom"
}
```

Evidence:

- `agentcy-loom/README.md`
- `agentcy-loom/CLAUDE.md`
- `agentcy-loom/docs/package-cli-alias-readiness-2026-04-12.md`
- `agentcy-loom/docs/packaged-install-help-proof-2026-04-12.md`
- `agentcy-loom/runtime/src/domain/run-result-v1.ts`

In `runtime/src/domain/run-result-v1.ts`, the exported canonical payload still hard-codes:

- `writer.repo = 'cli-phantom'`
- `writer.module = 'agentcy-loom'`

That is correct for the current bounded family contract and should not be changed as part of package/bin/doc drift cleanup.

## Repo-local documentation drift

### Aligned surfaces

`README.md` and `CLAUDE.md` are broadly aligned on the key mixed-surface policy:

- repo identity preserved as `cli-phantom` in writer fields
- package surface documented as `loom-runtime`
- installed CLI documented as `loom`
- loop-8 scope kept as packaged-help proof rather than rename execution

### Drift still visible

The main repo-local drift is historical path narration versus the literal renamed repo directory:

1. `agentcy-loom/docs/packaged-install-help-proof-2026-04-12.md` still describes the proof as:
   - "cli-phantom packaged install/help proof"
   - run from `/Users/amadad/projects/cli-phantom/runtime`
   - outside `/Users/amadad/projects/cli-phantom`

2. That wording is historically understandable, but it no longer matches the literal current directory name `agentcy-loom/`.

3. The same proof doc is also currently dirty in git, which suggests the help-text record is being refreshed but the broader path narration has not yet been fully normalized.

### Interpretation of that drift

This is documentation/path drift, not a runtime ownership drift:

- package/bin/runtime behavior still points at Loom surfaces
- the artifact writer contract is still correctly preserved
- the remaining mismatch is mostly how the proof doc narrates the repo path and historical repo label

## Current CLI/help surface reality

The live help surface in `runtime/src/cli/index.ts` currently presents:

- usage line: `loom <command> [options]`
- command families: `auto`, `brand`, `run`, `review`, `publish`, `inspect`, `retry`, `lab`, `ops`
- workflow list: `social.post`, `blog.post`, `outreach.touch`, `respond.reply`
- examples including `loom lab render ...`

The currently dirty diff in `runtime/src/cli/index.ts` is small and meaningful:

- `lab card ...` summary text was broadened to `lab <card|render> ...`
- a `loom lab render ...` example was added

That is a bounded Node CLI/help correction and is consistent with the updated proof doc.

## Acceptance-criteria checklist

- recorded current branch and dirty facts: yes
- documented package name `loom-runtime`: yes
- documented installed bin `loom`: yes
- documented source CLI path: yes (`runtime/src/cli.ts`)
- inspected packaged-help proof doc: yes
- preserved `run_result.v1.writer = { repo: "cli-phantom", module: "agentcy-loom" }`: yes
- applied Node-proof parity instead of Python-only checks: yes
- identified bounded repo-local documentation drift: yes
- avoided rename execution: yes

## Smallest next bounded follow-up

The next smallest honest follow-up is:

### Follow-up candidate

Refresh `agentcy-loom/docs/packaged-install-help-proof-2026-04-12.md` so its historical explanation distinguishes clearly between:

- the current literal repo directory `agentcy-loom/`
- the preserved canonical writer repo value `cli-phantom`
- the bounded package/bin surfaces `loom-runtime` and `loom`

### Why this is the smallest good next step

- it stays repo-local
- it clarifies real path/package/bin truth for operators and future reviewers
- it does not change package names, bin names, runtime prefixes, or writer fields
- it does not expand into repo rename execution or family-wide normalization work

### Explicit non-follow-ups

Do not expand the next step into:

- changing `writer.repo` to `agentcy-loom`
- renaming `loom-runtime` to `agentcy-loom`
- replacing `loom` with a new installed binary name
- broad runtime-prefix migration
- cross-repo rename cleanup

## Bottom line

`agentcy-loom` currently has a credible Node runtime surface with a real packaged CLI path:

- package: `loom-runtime`
- installed bin: `loom`
- source CLI: `runtime/src/cli.ts`
- packaged shim: `runtime/bin/loom.js`

The live drift is mostly documentation/path narration around the old `cli-phantom` repo name, while the canonical artifact contract correctly remains:

```json
{
  "repo": "cli-phantom",
  "module": "agentcy-loom"
}
```

That means the repo should be treated as package/bin-help aligned enough for bounded compatibility review, but not as evidence that repo/package normalization is complete.