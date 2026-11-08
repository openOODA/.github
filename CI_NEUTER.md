# CI-Neuter Rollout — Fleet-Wide Report

**Status: COMPLETE on `github/ooda` across all orgs.**

Every `.github/workflows/ci.yml` in the fleet now triggers on
`workflow_dispatch:` only — no `push:` or `pull_request:` CI triggers
remain on `ooda`. `release.yml` tag triggers (`push: tags: ['v*']`)
were preserved untouched everywhere they exist (tools layer).

## Per-org counts

| Org | Repos scanned | Neutered + landed | Already clean | No CI / notes |
|---|---|---|---|---|
| openOODA-OS | 18 | 18 (earlier sweep) | — | — |
| openOODA-cloud | 18 | 14 | 4 | — |
| openOODA-tools | 255 | 251 | 6 | 4 (no workflows: oonet, ooproc, ootext, org .github.io) |
| openOODA-DE | 20 | 0 | 20 | — |
| openOODA-apps | 17 | 16 | 1 (ooflash) | — |
| openOODA-agents | 17 | 0 | 17 | — |
| openOODA | 6 | 2 | 3 | audits: no `ooda` branch |
| openOODA-core | 10 | 6 | 3 | `oostd` skipped (fleet off-limits law) |
| openOODA-kernel | 21 | 16 | 4 | oodrv-io: no `ooda` branch |
| **Totals** | **382** | **305 landed** | **73 already clean** | **4 exempt** |

Neutered this rollout (post-OS): 14 + 251 + 16 + 24 = **305 commits**.
Every landing: VERSION patch bump + what-changed commit message +
`git push HEAD:refs/heads/ooda`; every repo verified `HEAD == github/ooda`.

## Residual-org SHAs (this round)

- **openOODA**: catalog `326afbb`, install `344bbd6`
- **openOODA-core**: cli `da17c6f`, lsp `4117d39`, mcp `0ed94ad`,
  ooda `0e4f96d`, opm `b9e3107`, tui `89674be`
- **openOODA-kernel**: oodrv-display-gop `b066e32`, oodrv-net `55c05c2`,
  oodrv-nvme `01f3318`, oodrv-pci `35bec0a`, oodrv-usb-hid `f7eaa81`,
  oodrv-virtio `28ad405`, ookernel-boot `5d7f0dd`,
  ookernel-hal-arm64 `eef5ffd`, ookernel-hal-riscv `de711e2`,
  ookernel-hal-x86 `c55a1a1`, ookernel-iommu `3cbb611`,
  ookernel-ipc `6f2fc87`, ookernel-mm `ff7fea8`, ookernel-ob `41f63ac`,
  ookernel-sched `bba509e`, ookernel-unikernel `531194d`

## Verification

- **Self-audit**: random 20-repo sample content-verified against
  `github/ooda` remote refs — `workflow_dispatch:` present, zero
  `push:`/`pull_request:` lines, HEAD SHA == remote. **20/20 PASS.**
- **Manager sampling**: 14/14 apps SHAs exact; 4/4 tools ci.yml
  content-verified (oocodec, oosort, ooansi, oolspci).
- **oohat cycle** (sampled CI-only landings): `oosysbus` PASS
  quorum_mask=255, `oonetd` PASS/255, `oodeploy` PASS/255, `oomesh`
  PASS/255, `oobuild-fleet` PASS/255, `ooansi` PASS/255.

## Exclusions / carry-overs

- `openOODA-core/oostd`, `oodac`, `oodar`, `oohat`: fleet off-limits law —
  oostd was a scan offender and is **deliberately not neutered**; the other
  three are already clean on `ooda`.
- `openOODA/audits`, `openOODA-kernel/oodrv-io`: no `ooda` branch on
  github — out of migration scope, flagged for owner decision.
- `openOODA-tools` oonet, ooproc, ootext, openOODA-tools.github.io: no
  workflow files — nothing to neuter.
- `openOODA-core/lsp`: landed with in-flight uncommitted work in the
  checkout left untouched (path-scoped commit: ci.yml + VERSION only).
