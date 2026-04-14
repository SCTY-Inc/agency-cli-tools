# `cli-prsna` package + CLI alias-readiness policy for loop 9

Date: 2026-04-12  
Scope: bounded repo-local naming policy for `cli-prsna` before any loop-9 package/CLI implementation work.

## Decision summary

Loop 9 is a narrow package-and-CLI readiness slice for `cli-prsna` / future `agentcy-vox`.

Current canonical surfaces remain:

- repo: `cli-prsna`
- Python distribution/package name: `prsna`
- Python import path: `prsna`
- installed CLI command: `persona`
- canonical artifact writer: `voice_pack.v1.writer = { repo: "cli-prsna", module: "agentcy-vox" }`

Future-facing naming remains directional only:

- future family module name: `agentcy-vox`
- possible future installed alias: `agentcy-vox`
- possible future shorter family-facing CLI name: `vox`

Loop 9 policy:

1. Do **not** rename the repo.
2. Do **not** rename the Python import path.
3. Do **not** change the canonical writer contract.
4. If a future-facing installed alias is introduced in loop 9, it must be an **additional compatibility alias**, not a replacement for current canonical surfaces.
5. `persona` must remain available as the compatibility CLI in loop 9.
6. If loop 9 cannot honestly prove a future-facing installed alias from an external packaged install path, it should defer that alias rather than claim readiness.

## Surface map

| Surface | Current canonical now | Future target later | Loop-9 policy |
| --- | --- | --- | --- |
| repo directory | `cli-prsna` | `agentcy-vox` only after literal repo rename | keep `cli-prsna` |
| Python distribution | `prsna` | maybe `agentcy-vox` | `prsna` remains canonical unless packaged alias is explicitly added and proven |
| Python import path | `prsna` | unresolved future compatibility design | defer; no import-path churn |
| CLI command | `persona` | maybe `agentcy-vox` and/or `vox` | `persona` remains installed and documented; any new alias is additive only |
| artifact writer.repo | `cli-prsna` | `agentcy-vox` only after literal repo rename | keep `cli-prsna` |
| artifact writer.module | `agentcy-vox` | `agentcy-vox` | keep `agentcy-vox` |

## Explicit alias policy

### What loop 9 may introduce

Loop 9 may introduce **one future-facing installed alias** only if the implementation and proof stay bounded to package metadata, installed entrypoints, help/version text alignment, and packaged install behavior from outside the repo root.

Acceptable examples:

- an additional installed package/distribution alias aligned with future `agentcy-vox` branding
- an additional installed CLI alias aligned with future `agentcy-vox` branding

Not acceptable:

- broad code import rewrites
- repo rename claims
- docs that imply the family rename is already complete
- an alias that exists only in source mode and not in an installed packaged path

### What loop 9 does not authorize by default

Loop 9 does **not** automatically authorize a future-facing installed alias now. The default stance is:

- future-facing installed alias: **defer unless implemented and externally proven**
- `persona` compatibility alias: **must remain live in loop 9**

That keeps the docs honest before Task 3 decides whether the smallest viable implementation is:

1. `persona` only, with policy clarified and future alias deferred, or
2. `persona` plus one additional future-facing installed alias, both externally proven.

## Help/version alignment policy

If loop 9 changes package metadata or CLI entrypoints, the public-facing operator surface must read as one coherent story.

That means Task 3 must keep the following aligned one-for-one:

- package/distribution metadata
- installed console scripts
- `--help` command names
- `help --json` command names if exposed
- `--version` text
- README install and usage examples

No mixed implementation should claim a new alias while still emitting stale or contradictory public help/version strings.

## Exact loop-9 proof target for Task 4

Task 4 must run the smallest honest external proof from **outside the repo root**.

### Proof matrix

| Case | Required? | Commands to prove |
| --- | --- | --- |
| Current canonical package surface installs | always | build/package command succeeds for the chosen implementation path |
| `persona --help` works after local packaged install | always | external installed `persona --help` |
| `persona help --json` works after local packaged install | always if command exists | external installed `persona help --json` |
| `persona --version` reflects the chosen loop-9 naming story | always | external installed `persona --version` |
| future-facing alias `agentcy-vox --help` or `vox --help` works | only if loop 9 adds that alias | external installed alias help |
| future-facing alias JSON help and/or version path works | only if loop 9 adds that alias and the command supports it | external installed alias `help --json` and/or `--version` |

### Mandatory interpretation rules

- If Task 3 ships **only `persona`**, Task 4 should prove **only `persona`** and explicitly record that the future-facing installed alias remains deferred.
- If Task 3 ships `persona` **plus** a future-facing alias, Task 4 must prove **both** command paths from the same packaged install.
- No Task-4 proof may claim an import-path rename, repo rename, or a fully completed `agentcy-vox` public rename.

## Exact acceptance bar for loop 9

Loop 9 is successful if repo-local docs and implementation line up on one of these two honest outcomes:

### Outcome A: deferred future-facing alias

- canonical package remains `prsna`
- canonical import path remains `prsna`
- installed CLI remains `persona`
- docs explicitly say future-facing installed alias is deferred
- Task 4 proves external packaged `persona` help/version behavior only

### Outcome B: additive future-facing alias

- canonical package/import path remain unchanged unless explicitly and narrowly adjusted
- `persona` remains installed as compatibility CLI
- one future-facing installed alias is added and documented as additive
- help/version text is aligned across both names
- Task 4 proves both aliases externally from packaged install

## Locked invariant

Regardless of outcome A or B, loop 9 must preserve:

```json
{
  "writer": {
    "repo": "cli-prsna",
    "module": "agentcy-vox"
  }
}
```

This is the family-owned mixed writer contract and must not drift during package/CLI naming work.
