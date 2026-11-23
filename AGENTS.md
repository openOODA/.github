# .github (openOODA) — Organization Profile & Governance Metadata

Canonical organization-profile host of the openOODA capability-secured computing stack
(zero ambient authority, single-cycle 64-bit `CapReg64` hardware/software
capabilities). This repository is the public face of [`@openOODA`](https://github.com/openOODA):
it holds the org profile page (`profile/README.md`), the 5-organization brand icon
gallery (`brand/`), the GitHub Linguist package (`linguist/`), and a native `.oo`
self-verification surface (`bin/oogithub`) that proves every metadata invariant without stubs.

## Repo Root (11 Entries)

`AGENTS.md` `README.md` `Makefile` `ooda.pkg` `anchor.oo` `cli/` `core/` `tests/`
= the canonical 8-entry product blueprint **plus** `profile/` (org profile page),
`brand/` (icon gallery), `linguist/` (grammar + samples + `validate.oo` gate).

## Metadata Surfaces

- `profile/README.md` — public org profile: Root repos, 5-org table with exact
  repo and package counts, and the 4-tier system-requirements matrix.
- `brand/` — org avatar (`avatar.png`/`avatar.svg`) + `option-{a,b,c}/` icon sets:
  all 5 canonical organizations (`@openOODA` Umbrella + `@openOODA-core` + `@openOODA-system` + `@openOODA-apps` + `@openOODA-games`) in `1024×1024` PNG and SVG.
- `linguist/` — `languages.yml` OODA entry, `heuristics.yml` disambiguation rules,
  `grammars/oo.tmLanguage.json` TextMate grammar, `.gitattributes` mapping, and 9
  compilable samples (`samples/OODA/`); `make -C linguist check` runs `validate.oo`.
  `verify_contracts.oo` carries the check-time `verify`/`assert_eq!` surface — a
  check-only leaf never linked into binaries.
- `tests/` — lean 2-file suite over the linguist samples AND the metadata checkers.

## The Exact Consolidated 5-Organization Ecosystem (74 Repos)

| Organization | Repos | Members |
| :--- | :---: | :--- |
| **`@openOODA`** | `5` | `openOODA`, `catalog`, `install`, `website`, `.github` |
| **`@openOODA-core`** | `12` | `ooda`, `ooda-bridge`, `ooda-compiler`, `ooda-interface`, `ooda-language`, `ooda-package`, `ooda-runtime`, `ooda-sign`, `ooda-standard`, `ooda-verify`, `ooda-version`, `.github` |
| **`@openOODA-system`** | `27` | `ooda-archive`, `ooda-authority`, `ooda-boot`, `ooda-bus`, `ooda-compositor`, `ooda-connect`, `ooda-container`, `ooda-data`, `ooda-database`, `ooda-drivers`, `ooda-filesystem`, `ooda-firewall`, `ooda-hardware`, `ooda-health`, `ooda-inference`, `ooda-kernel`, `ooda-network`, `ooda-panel`, `ooda-portal`, `ooda-screensaver`, `ooda-settings`, `ooda-shell`, `ooda-start`, `ooda-theme`, `ooda-vault`, `ooda-web`, `.github` |
| **`@openOODA-apps`** | `20` | `ooda-browser`, `ooda-calculator`, `ooda-calendar`, `ooda-camera`, `ooda-chat`, `ooda-clock`, `ooda-code`, `ooda-files`, `ooda-flasher`, `ooda-media`, `ooda-notepad`, `ooda-office`, `ooda-passwords`, `ooda-photos`, `ooda-remote`, `ooda-screenshot`, `ooda-software`, `ooda-studio`, `ooda-terminal`, `.github` |
| **`@openOODA-games`** | `10` | `ooda-arcade`, `ooda-capella`, `ooda-commander`, `ooda-engine`, `ooda-island`, `ooda-retro`, `ooda-ski`, `ooda-strike`, `ooda-voxel`, `.github` |

**Fleet Census**: `65` product packages (`11` core + `26` system + `19` apps + `9` games) +
`4` `@openOODA` umbrella repos = `69` product+platform repos + `5` `.github` org-profile repos = `74` total repos. The `11` core packages are `ooda`, `ooda-bridge`, `ooda-compiler`, `ooda-interface`, `ooda-language`, `ooda-package`, `ooda-runtime`, `ooda-sign`, `ooda-standard`, `ooda-verify`, `ooda-version`. The `26` system packages are `ooda-archive`, `ooda-authority`, `ooda-boot`, `ooda-bus`, `ooda-compositor`, `ooda-connect`, `ooda-container`, `ooda-data`, `ooda-database`, `ooda-drivers`, `ooda-filesystem`, `ooda-firewall`, `ooda-hardware`, `ooda-health`, `ooda-inference`, `ooda-kernel`, `ooda-network`, `ooda-panel`, `ooda-portal`, `ooda-screensaver`, `ooda-settings`, `ooda-shell`, `ooda-start`, `ooda-theme`, `ooda-vault`, `ooda-web`. The `19` apps packages are `ooda-browser`, `ooda-calculator`, `ooda-calendar`, `ooda-camera`, `ooda-chat`, `ooda-clock`, `ooda-code`, `ooda-files`, `ooda-flasher`, `ooda-media`, `ooda-notepad`, `ooda-office`, `ooda-passwords`, `ooda-photos`, `ooda-remote`, `ooda-screenshot`, `ooda-software`, `ooda-studio`, `ooda-terminal`. The `9` games packages are `ooda-arcade`, `ooda-capella`, `ooda-commander`, `ooda-engine`, `ooda-island`, `ooda-retro`, `ooda-ski`, `ooda-strike`, `ooda-voxel`.

## Power-of-2 Shape Ladder (`1/2/4/8/16/32/64/128/256`)

- `1`: Link count == 1 (0 symlinks/hardlinks) & max 1 statement/line.
- `2`: Lean 2-file `tests/` suite (`test_functional.oo` + `test_refusal.oo`, 0 source-grepping).
- `4`: Max 4 nesting depth & 4-Axis Code Review (`ooda-verify` + `Semantic & Spec` + `Native Binary & Systems` + `Ecosystem & Registry`).
- `8`: Max 8 `.oo` pages/dir, 8 fns/file, 8 params/fn, 8-entry product repo root.
- `16`: Min 16 lines/file. `32`: 32 explicit capabilities (`0..31`), max 32 chars/name, <=32 `.oo` pages/repo.
- `64`: Max 64 code lines/fn. `128`: Max 128 chars/line. `256`: Max 256 lines/file.

## CLI Laws & Self-Verification Surface

- `bin/oogithub` verbs: `check`/`audit`/`status`/`verify` (`profile` + `charter` +
  `root` + `brand` + `linguist` + `docs` verdicts), `census`, `about`, `theme <name>`,
  `--self-test`, `--help`, `--version`, additive `--json`.
- Subcommand dispatch only; `--persona`, `--mode`, `--personas` flags are forbidden and
  every unknown argument or `..` traversal operand refuses with exit `2`.
- `core/meta_check.oo` proves: `meta_profile_ok` verifies `profile/README.md`'s 5-org repo and package counts plus all 5 org links, while `meta_charter_ok` verifies the Ecosystem & Fleet Census section of `AGENTS.md` (scoped prior to subsequent `##` headings so prose below cannot self-certify it); `meta_ver_num` folds the component semver.
- `core/meta_law.oo` proves: the 11-entry repo root exists, `AGENTS.md` opens with the
  canonical title, `README.md` links `profile/README.md` + `brand/`, all 30 brand icons
  exist (5 orgs x 3 options x png+svg + avatar pair), and the linguist package is complete.

## Syntax, Mandatory `ooda-standard` Reuse & Workflow

- Relative string imports only (`import "core/engine.oo";` or `import "ooda-standard/fs/os/fs.oo";`, never `::`).
  No parens on `if cond { }` / `while cond { }`. No struct trailing commas. Academy headers on every page.
- **Always import `ooda-standard`** for math & proofs (`ooda-standard/core/math/{exact,geometry,blas,fft,algebra,graph_topology}/...`, `ooda-standard/core/proofs/...`), science & 2D/3D engine physics (`ooda-standard/core/science/{phys,chem,bio,comm,econ}/...`, `ooda-standard/core/app/ui/game_engine/...`), frontier AI-for-science (`ooda-standard/core/app/ai/...`), collections (`ooda-standard/core/collection/...`), and crypto/security (`ooda-standard/sec/{hash,capability,pqc,symmetric}/...`)—never re-implement duplicate local helpers!
- Build & Verify: `make build && make test` (or `ooda build && ooda test`), then
  `make verify`, `ooda check && ooda audit`, and `ooda-verify cycle` (`quorum_mask=255`).
