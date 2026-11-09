# <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/avatar.png" width="36" align="top"> openOODA

Capability-secured computing stack (`L0`–`L7`) built in native `.oo` with zero ambient authority and single-cycle 64-bit hardware/software capabilities (`CapReg64`).

- **Website**: [https://openOODA.org](https://openOODA.org)
- **Binary & ISO Release Hub**: [`openOODA/install@hub`](https://github.com/openOODA/install/releases/tag/hub)
- **Package Registry**: [`openOODA/catalog`](https://github.com/openOODA/catalog)
- **Brand & Icon Gallery**: [`openOODA/.github/brand`](https://github.com/openOODA/.github/tree/master/brand)

## Quick Install

```sh
curl -fsSL https://openOODA.org/install.sh | bash
```

Manage layers and packages with `oopm`:

```sh
oopm group list            # List @core, @kernel, @os, @tools, @de, @apps, @cloud, @agents, @workstation, @all
oopm install @core         # L0 toolchain: ooda, oodac, oodar, oostd, oopm, oolsp, oomcp, oohat
oopm install @tools        # 39 capability-sandboxed L3 utilities
oopm install @workstation  # Full workstation stack (@core + @tools + @de + @apps)
oopm install @all          # Complete L0–L7 stack
```

## Root Repositories (`@openOODA`)

| Repository | Role |
| :--- | :--- |
| [`openOODA`](https://github.com/openOODA/openOODA) | Governance charter (`AGENTS.md`) and the 8 Quick Cards (`cards/`) |
| [`install`](https://github.com/openOODA/install) | Universal bootstrap installer, bootable Live ISO (`ooda-os-x86_64.iso`), Buildbox, and binary release hub |
| [`catalog`](https://github.com/openOODA/catalog) | Signed `L0`–`L7` package registry queried by `oopm` |
| [`website`](https://github.com/openOODA/website) | Static source for [https://openOODA.org](https://openOODA.org) (`docs/`) |

## L0–L7 Organizations

| Icon | Layer | Organization | Scope |
| :---: | :--- | :--- | :--- |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA.png" width="28"> | **Root** | [`@openOODA`](https://github.com/openOODA) | Governance & Quick Cards (`openOODA`), Binary & ISO Hub (`install`), Package Catalog (`catalog`), Website (`website`) |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA-core.png" width="28"> | **L0** | [`@openOODA-core`](https://github.com/openOODA-core) | Master CLI (`ooda`), Native Compiler (`oodac`), Runtime (`oodar`), Standard Library (`oostd`), Package Manager (`oopm`), `oolsp`, `oomcp`, 8-Hat Verifier & Debugger (`oohat`) |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA-kernel.png" width="28"> | **L1** | [`@openOODA-kernel`](https://github.com/openOODA-kernel) | UEFI Bootloader (`ooboot`), HAL (`oohal`), Capability Microkernel (`ookernel`), Ring-3 Drivers (`oodrv-io`, `oodrv-storage`, `oodrv-virt`) |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA-OS.png" width="28"> | **L2** | [`@openOODA-OS`](https://github.com/openOODA-OS) | Zero-Root Daemons (`ooinit`, `oovfs`, `oonetd`, `oosysbus`, `ooauthd`, `oohealthd`, `oocontainer`, `oollama`, `oomodemd`) |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA-tools.png" width="28"> | **L3** | [`@openOODA-tools`](https://github.com/openOODA-tools) | 39 Capability-Sandboxed Unix, System, Security (`oodefense`, `oosandbox`), UI (`ootheme`, `ooui`), & Engine (`ooengine`) Utilities |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA-DE.png" width="28"> | **L4** | [`@openOODA-DE`](https://github.com/openOODA-DE) | Wayland Compositor (`oocomp`), Panel (`oopanel`), Privacy Portals (`ooportal`), Terminal (`ooterm`), Files, Settings, Bazaar, HUD |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA-apps.png" width="28"> | **L5** | [`@openOODA-apps`](https://github.com/openOODA-apps) | 16 Native Applications (`oobrowser`, `oostudio`, `oooffice`, `oocanvas`, `oomedia`, `ooflash`, `oodaw`, `ooarcade`, `oostrike`, `oovoxel`) |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA-cloud.png" width="28"> | **L6** | [`@openOODA-cloud`](https://github.com/openOODA-cloud) | Mesh (`oomesh`), Object Store (`oostore`), Bare-Metal Deploy (`oodeploy`), Gateway (`oogateway`), Identity, DB (`oodb`), Telemetry, Billing |
| <img src="https://raw.githubusercontent.com/openOODA/.github/master/brand/option-b/openOODA-agents.png" width="28"> | **L7** | [`@openOODA-agents`](https://github.com/openOODA-agents) | Autonomous OODA Loops (`ooloop`, `ooswarm`), Falsification (`oofalsify`), Consensus (`ooconsensus`), Code (`oocode`), Memory, Quota, Govern |
