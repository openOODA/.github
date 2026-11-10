# .github (openOODA) — Organization Profile & Governance Metadata

Canonical organization-profile host of the openOODA capability-secured computing stack
(`L0`–`L7`, zero ambient authority, single-cycle 64-bit `CapReg64` hardware/software
capabilities). This repository is the public face of [`@openOODA`](https://github.com/openOODA):
it holds the org profile page (`profile/README.md`), the 9-organization brand icon
gallery (`brand/`), the GitHub Linguist package (`linguist/`), and a native `.oo`
self-verification surface (`bin/oogithub`) that proves every metadata invariant without stubs.

## Repo Root (11 Entries)

`AGENTS.md` `README.md` `Makefile` `ooda.pkg` `anchor.oo` `cli/` `core/` `tests/`
= the canonical 8-entry product blueprint **plus** `profile/` (org profile page),
`brand/` (icon gallery), `linguist/` (grammar + samples + `validate.py` gate).

## Metadata Surfaces

- `profile/README.md` — public org profile: Root repos, `L0`–`L7` org table with exact
  repo counts, fleet census, and the 4-tier system-requirements matrix.
- `brand/` — org avatar (`avatar.png`/`avatar.svg`) + `option-{a,b,c}/` icon sets:
  all 9 organizations (`@openOODA` Root + `L0`–`L7`) in `1024×1024` PNG and SVG.
- `linguist/` — `languages.yml` OODA entry, `heuristics.yml` disambiguation rules,
  `grammars/oo.tmLanguage.json` TextMate grammar, `.gitattributes` mapping, and 9
  compilable samples (`samples/OODA/`); `make -C linguist check` runs `validate.py`.
  `verify_contracts.oo` carries the check-time `verify`/`assert_eq!` surface — a
  check-only leaf never linked into binaries.
- `tests/` — lean 2-file suite over the linguist samples AND the metadata checkers.

## The Exact Consolidated L0–L7 Ecosystem (110 Repos)

| Layer | Organization | Repos | Members |
| :--- | :--- | :---: | :--- |
| **Root** | `@openOODA` | `5` | `openOODA`, `catalog`, `install`, `website`, `.github` |
| **L0** | `@openOODA-core` | `8` | `ooda`, `oodac`, `oodar`, `oostd`, `oopm`, `oolsp`, `oomcp`, `oohat` |
| **L1** | `@openOODA-kernel` | `8` | `ooboot`, `oohal`, `ookernel`, `oodrv-storage`, `oodrv-net`, `oodrv-io`, `oodrv-virt`, `oodrv-accel` |
| **L2** | `@openOODA-OS` | `9` | `ooinit`, `oovfs`, `oonetd`, `oosysbus`, `ooauthd`, `oohealthd`, `oocontainer`, `oollama`, `oomodemd` |
| **L3** | `@openOODA-tools` | `39` | `ooarchive`, `ooawk`, `oocat`, `oocodec`, `oocron`, `oocurl`, `oodefense`, `oodiff`, `ooengine`, `oofind`, `oofirewall`, `oofs`, `oofzf`, `oogrep`, `ooh`, `oohash`, `oohw`, `oojq`, `ooless`, `ools`, `oomount`, `oonet`, `oopath`, `ooperm`, `oopower`, `ooproc`, `ooprovenance`, `ooredact`, `oorgb`, `oosandbox`, `oosed`, `oosh`, `oosign`, `oosort`, `ootext`, `ootheme`, `ootty`, `ooui`, `oovault` |
| **L4** | `@openOODA-DE` | `8` | `oocomp`, `oopanel` (`+ooagent-hud`), `ooportal`, `ooterm`, `oofiles`, `oosettings`, `oobazaar`, `oosaver` |
| **L5** | `@openOODA-apps` | `16` | `oobrowser`, `oostudio`, `oooffice`, `oocanvas`, `oomedia`, `ooflash`, `oodaw`, `oochat`, `oopass`, `ookvm`, `oocamera`, `ooemu`, `ooarcade`, `oocommand`, `oostrike`, `oovoxel` |
| **L6** | `@openOODA-cloud` | `8` | `oomesh`, `oostore`, `oodeploy`, `oogateway`, `ooidentity`, `oodb`, `ootelemetry`, `oobilling` |
| **L7** | `@openOODA-agents` | `9` | `ooloop`, `ooswarm`, `oobench`, `oodream`, `oofalsify`, `ooconsensus`, `oocode`, `oomemory`, `oogovern` (`+ooquota`) |

**Fleet Census**: `97` product binaries across `L1`–`L7` (`105` across `L0`–`L7`) +
`5` `@openOODA` governance repos = `110` total repos. Folded repos
(`ooagent-hud` -> `oopanel`, `ooquota` -> `oogovern`) count inside their host, never
as separate rows.

## Power-of-2 Shape Ladder (`1/2/4/8/16/32/64/128/256`)

- `1`: Link count == 1 (0 symlinks/hardlinks) & max 1 statement/line.
- `2`: Lean 2-file `tests/` suite (`test_functional.oo` + `test_refusal.oo`, 0 source-grepping).
- `4`: Max 4 nesting depth & 4-Axis Code Review (`oohat` + `Semantic & Spec` + `Native Binary & Systems` + `Ecosystem & Registry`).
- `8`: Max 8 `.oo` pages/dir, 8 fns/file, 8 params/fn, 8-entry product repo root.
- `16`: Min 16 lines/file. `32`: 32 explicit capabilities (`0..31`), max 32 chars/name, <=32 `.oo` pages/repo.
- `64`: Max 64 code lines/fn. `128`: Max 128 chars/line. `256`: Max 256 lines/file.

## CLI Laws & Self-Verification Surface

- `bin/oogithub` verbs: `check`/`audit`/`status`/`verify` (census + orgs + members +
  root + brand + linguist + docs verdicts), `census`, `about`, `theme <name>`,
  `--self-test`, `--help`, `--version`, additive `--json`.
- Subcommand dispatch only; `--persona`, `--mode`, `--personas` flags are forbidden and
  every unknown argument or `..` traversal operand refuses with exit `2`.
- `core/meta_check.oo` proves: `profile/README.md` carries the exact census
  (`97`/`105`/`110` + `5`/`8`/`9`/`39`/`16` counts), all 9 org links, and one canonical
  member per layer (`oodac`..`ooloop`); `meta_ver_num` folds the component semver.
- `core/meta_law.oo` proves: the 11-entry repo root exists, `AGENTS.md` opens with the
  canonical title, `README.md` links `profile/README.md` + `brand/`, all 56 brand icons
  exist (9 orgs x 3 options x png+svg + avatar pair), and the linguist package is complete.

## Syntax, Mandatory `oostd` Reuse & Workflow

- Relative string imports only (`import "core/engine.oo";` or `import "oostd/fs/os/fs.oo";`, never `::`).
  No parens on `if cond { }` / `while cond { }`. No struct trailing commas. Academy headers on every page.
- **Always import `oostd` (`L0`)** for math (`oostd/core/math/exact/...`, `geometry/...`), 2D/3D physics &
  collision (`oostd/core/science/phys/classical/...`, `gnc/...`, `relativistic/...`,
  `oostd/core/app/ui/game_engine/...`), frontier AI-for-science & graphs (`oostd/core/app/ai/...`),
  collections (`oostd/core/collection/...`), and crypto/hashing (`oostd/sec/hash/...`,
  `capability/...`)—never re-implement duplicate local helpers!
- Build & Verify: `make build && make test` (or `ooda build && ooda test`), then
  `make verify`, `ooda check && ooda audit`, and `oohat cycle` (`quorum_mask=255`).
