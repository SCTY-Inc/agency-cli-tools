# cli-prsna packaged install/help proof — 2026-04-12

Scope: bounded loop-9 proof for the exact shipped package/install surface of `cli-prsna` from outside the repo root.

## Outcome summary

This loop currently ships **only the `persona` installed CLI**.

Verified now:
- Python distribution/package name: `prsna`
- Python import path: `prsna`
- Installed operator-facing CLI: `persona`

Not claimed by this proof:
- no literal repo rename
- no Python import-path rename
- no future-facing installed alias such as `agentcy-vox` or `vox`

Per `docs/package-cli-alias-readiness-2026-04-12.md`, this proof therefore verifies the full packaged matrix for `persona` only and treats any future-facing installed alias as deferred.

## Verification environment

All install/run checks below were executed from a temp directory outside `/Users/amadad/projects/cli-prsna`.

- temp directory: `/tmp/cli-prsna-proof-zKUh94`
- installed binary path: `/tmp/cli-prsna-proof-zKUh94/venv/bin/persona`
- installed import path: `/tmp/cli-prsna-proof-zKUh94/venv/lib/python3.12/site-packages/prsna/__init__.py`

## Exact commands run

### 1) Build from the repo root

```bash
cd /Users/amadad/projects/cli-prsna
uv build
```

Observed build result:

```text
Building source distribution...
Building wheel from source distribution...
Successfully built dist/prsna-0.1.0.tar.gz
Successfully built dist/prsna-0.1.0-py3-none-any.whl
```

### 2) Create a temp environment outside the repo and install the built package

```bash
TMPDIR=$(mktemp -d /tmp/cli-prsna-proof-XXXXXX)
python3 -m venv "$TMPDIR/venv"
. "$TMPDIR/venv/bin/activate"
pip install --upgrade pip >/dev/null
pip install /Users/amadad/projects/cli-prsna/dist/prsna-0.1.0-py3-none-any.whl
cd "$TMPDIR"
```

This install path deliberately used the built wheel from outside the source tree rather than `uv run`, `python -m prsna`, or any repo-local invocation path.

### 3) Prove the shipped command surface from the external temp directory

#### 3a) Confirm current working directory is outside the repo

```bash
pwd
```

Output:

```text
/tmp/cli-prsna-proof-zKUh94
```

#### 3b) Confirm the installed `persona` binary is the one being executed

```bash
which persona
```

Output:

```text
/tmp/cli-prsna-proof-zKUh94/venv/bin/persona
```

#### 3c) `import prsna` smoke test

```bash
python -c 'import prsna; print(prsna.__file__)'
```

Output:

```text
/tmp/cli-prsna-proof-zKUh94/venv/lib/python3.12/site-packages/prsna/__init__.py
```

Interpretation:
- `import prsna` remains unchanged and works from the installed package
- this is a compatibility smoke test only, not an import-path rename

#### 3d) `persona --help`

```bash
persona --help
```

Output:

```text
Usage: persona [OPTIONS] COMMAND [ARGS]...

Manage, compose, test, and export AI personas.

Options:
  --version             -V
  --json                          Output as JSON
  --quiet               -q        Minimal output
  --install-completion            Install completion for the current shell.
  --show-completion               Show completion for the current shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

Commands:
  init      Create a new empty persona (manual editing required).
  create    Bootstrap a persona using AI.
  ls        List all personas.
  show      Show persona details.
  edit      Edit persona in $EDITOR.
  rm        Remove a persona.
  mix       Mix two personas into a new one.
  chat      Interactive chat with a persona.
  ask       Ask a persona a single question.
  export    Export persona to different formats, including canonical
            voice_pack.v1 JSON.
  enrich    Enrich persona with current info from Exa.
  test      Test persona consistency with DSPy.
  optimize  Optimize persona prompt using GEPA.
  learn     Analyze interactions and improve persona.
  critique  Self-critique persona and suggest improvements.
  drift     Check if a response drifts from persona.
```

#### 3e) `persona --version`

```bash
persona --version
```

Output:

```text
persona 0.1.0
```

Interpretation:
- version text matches the current persona-first CLI policy
- this proof does not claim a new alias or family-name binary

#### 3f) Safe command proof: `persona export --list`

```bash
persona export --list
```

Output:

```text
Available export formats:
  - prompt
  - eliza
  - v2
  - ollama
  - hub
  - voice-pack
  - voice_pack
  - voice_pack.v1
```

## Acceptance-matrix readout

| Surface | Result |
| --- | --- |
| build succeeds | yes — `uv build` produced sdist and wheel |
| local packaged install succeeds | yes — installed wheel into temp venv outside repo root |
| `persona --help` | yes |
| `persona --version` | yes |
| one safe command (`persona export --list`) | yes |
| `import prsna` compatibility smoke test | yes |
| future-facing installed alias proven | no — explicitly deferred |
| source-tree invocation required | no |

## Final interpretation

This proof shows that the currently shipped `cli-prsna` package can be built, installed, and exercised from outside the repo root with the exact public command surface that is actually present today:

- package/import surface: `prsna`
- installed CLI surface: `persona`

This document is evidence for packaged install/help readiness only. It does **not** imply:
- a literal rename from `cli-prsna` to `agentcy-vox`
- a Python import rename away from `prsna`
- a newly shipped `agentcy-vox` or `vox` installed command
