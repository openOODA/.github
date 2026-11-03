<div align="center">

<pre>
   ____  ____  ___  ____    ___   ___  ____    _
  / __ \/ __ \/ _ \/ __ \  / _ \ / _ \|  _ \  / \
 / /_/ / /_/ /  __/ / / / | | | | | | | | | |/ _ \
/_____/ .___/\___/_/ /_/  | |_| | |_| | |_| / ___ \
      /_/                   \___/ \___/|____/_/   \_\
</pre>

### openOODA — Primary Systems Language & 9-Organization Ecosystem (Root + L0-L7) for the AI Era

[openooda.org](https://openooda.org) • [llms.txt](https://openooda.org/llms.txt) • [openOODA-core](https://github.com/openOODA-core) • [openOODA-kernel](https://github.com/openOODA-kernel) • [openOODA-OS](https://github.com/openOODA-OS) • [openOODA-tools](https://github.com/openOODA-tools) • [openOODA-DE](https://github.com/openOODA-DE) • [openOODA-apps](https://github.com/openOODA-apps) • [openOODA-cloud](https://github.com/openOODA-cloud) • [openOODA-agents](https://github.com/openOODA-agents)

</div>

Your process is born with no privileges. That is not an accident. That is the type system.

We assume the source is hostile, the tests are optimistic, and the agent will try the network. Then we make those attempts fail closed.

```sh
curl -fsSL https://openooda.org/install.sh | bash
```

Public home: [openooda.org](https://openooda.org). Copy: [`docs/HOME.oot`](../docs/HOME.oot).

## The 9-Organization Ecosystem (Root `@openOODA` + L0–L7)

| Layer & Org | Count | Focus |
| :--- | :---: | :--- |
| **Root Umbrella: [openOODA](https://github.com/openOODA)** | **5** | Governance, 24 laws & RFCs (`openOODA`), fleet buildbox (`buildbox`), website (`website`), one-line installer (`install`), public package registry (`catalog`), and `.github` |
| **Layer 0: [openOODA-core](https://github.com/openOODA-core)** | **10** | Sublayers L0.1-L0.4: host/silicon ABI (`oodar`: Landlock, `sys_spawn`/`sys_wait`, `OODA_LISTEN_FD`), deterministic runtime & memory (`std` linear arenas), self-hosting compiler (`oodac`: `.oo` -> LLVM IR -> native), language/stdlib/tools (`cli`, `ooda`, `opm`, `lsp`, `mcp`, `tui`) |
| **Layer 1: [openOODA-kernel](https://github.com/openOODA-kernel)** | **16** | Ring-0 NT/seL4 hybrid microkernel (`ookernel-ob`, `ookernel-mm`, `ookernel-sched`, `ookernel-ipc`) & Ring-3 drivers |
| **Layer 2: [openOODA-OS](https://github.com/openOODA-OS)** | **18** | Zero-root system daemons (`ooinit`, `oosvc-mgr`, `oovfs`, `oonetd`, `oosysbus`, `oohealthd`, `ooimage`, `ooaid --serve`, `oorealm`) |
| **Layer 3: [openOODA-tools](https://github.com/openOODA-tools)** | **257** | Userland CLI / TUI / MCP utilities across 12 functional categories (`oosh`, `oogrep`, `oofind`, `oojq`, `oollama`) |
| **Layer 4: [openOODA-DE](https://github.com/openOODA-DE)** | **20** | Capability Wayland Desktop Environment (`oocomp`, `oowm`, `oopanel`, `ooportal`, `oobazaar`, `oocockpit`, `ooagent-hud`) |
| **Layer 5: [openOODA-apps](https://github.com/openOODA-apps)** | **16** | Flagship GUI Applications & Creator Suite (`oobrowser`, `oostudio`, `oodocs`, `oosheet`, `oodeck`, `oonotes`, `oocanvas`, `oopaint`, `oomedia`, `oodaw`, `oopdf`, `oomail`, `oochat`, `oopass`, `oovm-ui`, `oogit-ui`) |
| **Layer 6: [openOODA-cloud](https://github.com/openOODA-cloud)** | **16** | Distributed Cluster, Mesh & GPU Compute Grid (`oomesh`, `oogrid-sched`, `oostore-cas`, `oocontainer`, `ooinfer-grid`, `oobuild-grid`, `ookv-raft`, `oolb`, `ooci-runner`, `ooobserv`, `oosecrets`, `ooregistry`, `oodns-grid`, `oobackup`, `oogateway`, `oochron`) |
| **Layer 7: [openOODA-agents](https://github.com/openOODA-agents)** | **16** | Autonomous OODA Loops, Swarm & Governance (`oooda-engine`, `ooherdr`, `ooquota`, `ooredteam`, `oofalsify`, `ooconsensus`, `ooreviewer`, `ooarchitect`, `oocoder`, `oorelease`, `oomemory`, `ooplanner`, `oorouter`, `ooeval`, `oogovern`, `ooevolve`) |

## Root Umbrella (`@openOODA`) & Layer 0 Constellation (`@openOODA-core`)

| Layer | Repo | Role |
|:---|:---|:---|
| **Root Governance & Buildbox** | [openOODA/openOODA](https://github.com/openOODA/openOODA) | The laws, RFCs, and `buildbox/` watchdog. |
| **Root Website & Installer** | [openOODA/website](https://github.com/openOODA/website) | Source for [openooda.org](https://openooda.org). |
| | [openOODA/install](https://github.com/openOODA/install) | One-line toolchain bootstrap & package hooks. |
| | [openOODA/catalog](https://github.com/openOODA/catalog) | Public package registry for `opm`. |
| | [openOODA/.github](https://github.com/openOODA/.github) | Org profile, shared issue templates, and reusable CI workflows. |
| **L0.3 Self-Hosted Compiler** | [openOODA-core/oodac](https://github.com/openOODA-core/oodac) | Self-hosting compiler (`.oo` → LLVM IR → native). |
| **L0.1 Host/Silicon ABI** | [openOODA-core/oodar](https://github.com/openOODA-core/oodar) | C host substrate: Landlock sandbox (`PR_SET_NO_NEW_PRIVS`), non-blocking `sys_spawn`/`sys_wait`/`sys_kill`, `OODA_LISTEN_FD` socket activation, PQC, GPU. |
| **L0.2 Deterministic Runtime & Memory** | [openOODA-core/std](https://github.com/openOODA-core/std) | 8-domain standard library: 188 modules, linear-arena memory, `tcp_bind` socket slot tables. |
| **L0.4 Language/Stdlib/Tools** | [openOODA-core/cli](https://github.com/openOODA-core/cli) | Primary developer driver (build, test, fmt, qa). |
| | [openOODA-core/ooda](https://github.com/openOODA-core/ooda) | Top-level workflow command runner. |
| | [openOODA-core/opm](https://github.com/openOODA-core/opm) | Capability-aware deterministic package manager. |
| | [openOODA-core/lsp](https://github.com/openOODA-core/lsp) | Language Server Protocol daemon for editor diagnostics. |
| | [openOODA-core/mcp](https://github.com/openOODA-core/mcp) | Model Context Protocol server (26 capability-aware agent tools). |
| | [openOODA-core/tui](https://github.com/openOODA-core/tui) | Terminal coding harness with prompt dock & live thought canvas. |

## 3-Tier Canonical OODA Containers & Multimodal Inference Fleet

| Tier | Image & Components | Capabilities & Fleet Topology |
| :--- | :--- | :--- |
| **Tier 1: `localhost/ooda-core:latest`** | `ooinit` (PID 1), `oosvc-mgr`, `oologd`, `oohealthd`, `oopolicyd`, `ooaid`, `oorealm`, `ooimage` + `.oo` userland tools | Ultra-minimal immutable OODA base runtime (`zero .py/.sh`), non-blocking `sys_spawn`/`sys_wait`, `OODA_LISTEN_FD` zero-downtime socket activation, and kernel `Landlock` + `PR_SET_NO_NEW_PRIVS` sandboxing. |
| **Tier 2: `localhost/ooda-buildbox:latest`** | `oodac` seed + `oodar` + `std` + `ooda-loop` + `ooda-fanout` | 24/7 `.oo`-native compiler & fleet audit container across `zebes` (control plane), `ringmaster` (62 GiB RAM, 2x RTX 4060 Ti 16GB), and `spotlight` (31 GiB RAM, 2x RTX 4060 Ti 16GB). |
| **Tier 3: `localhost/ooda-inference:latest`** | `ooaid --serve` (`:11434`) + `oollama` + CUDA `llama-server` (`ooda-inference.container` Quadlet) | Dual-GPU MTP speculative decoding (`draft_num_predict 3` on `qwen36-35b-uncensored-1m`), active-active routing across `spotlight` & `ringmaster`, KV prefix pinning (`cache_prompt: true`), `<think>` budget gating, `.ooda-cache/ai` semantic cache, GBNF grammar enforcement, mandatory secret redaction, and 8 multimodal endpoints. |

## 3-Tier Universal App Compatibility & Store Architecture

| Tier | Bridge & Subsystems | Capability Enforcement |
| :--- | :--- | :--- |
| **Tier 1: Flathub / Bazaar Desktop Store Bridge** | `ooportal` + `ooimage` + `oopolicyd` | `ooimage` ingests Flathub OSTree Merkle commits into the immutable content-addressed store; `oopolicyd` translates Flatpak metadata permissions (`sockets=wayland;pulseaudio;network`, `filesystems=...`) 1-to-1 into attenuated `WindowCap`, `FrameCap`, `AudioCap`, `NetConnectCap`, and scoped `FsReadCap` mediated by `ooportal`. |
| **Tier 2: Podman-Style Rootless Server Containers** | `oocage` + `ooimage` + `oosvc-mgr` | Daemonless, rootless OCI container execution (Bazarr, Sonarr, Plex, Postgres) where each container runs in an isolated `CSpace` over read-only `ooimage` Merkle layers and explicit volume/port capabilities (`FsReadCap`/`FsWriteCap`/`NetBindCap`). |
| **Tier 3: Steam/Proton Cell + IOMMU Anti-Cheat (`WinRealm`)** | `ookernel-iommu` + `ookernel-unikernel` + `oocomp` | Linux Steam + Proton (`DXVK`/`VKD3D`) runs inside a GPU capability cell (`GpuCap` + `FrameCap` + `AudioCap` + `HidCap`). For kernel anti-cheat Windows games (Destiny 2 / BattlEye `BEDaisy.sys`), `ookernel-iommu` + `oodrv-pci` binds the GPU/NVMe partition to an IOMMU-fenced Windows NT Gaming Realm (`WinRealm`) with vTPM/SMBIOS passthrough from `ookernel-boot`, streaming frames at 144Hz/240Hz via zero-copy shared-memory `FrameCap` (LookingGlass/IVSHMEM ring) into a native `oocomp` window while mixing audio via `ooaudiod` and forwarding raw input via `oodrv-usb-hid`. |

## Unified L0-L7 Layer Model & Fleet Verification at v0.2.3

The ecosystem is structured into the root umbrella (`@openOODA`) plus 8 layer organizations (**L0–L7**). **L0 (`@openOODA-core`)** is subdivided into **L0.1 Host/Silicon ABI** (`oodar`), **L0.2 Deterministic Runtime & Memory** (`std` linear arenas, bulk resets), **L0.3 Self-Hosted Compiler** (`oodac`), and **L0.4 Language/Stdlib/Tools** (`cli`, `ooda`, `opm`, `lsp`, `mcp`, `tui`). Above it: **L1 `openOODA-kernel`** (16), **L2 `openOODA-OS`** (18), **L3 `openOODA-tools`** (257), **L4 `openOODA-DE`** (20), **L5 `openOODA-apps`** (16), **L6 `openOODA-cloud`** (16), **L7 `openOODA-agents`** (16).

**54/54 KVM microVM boot verification at v0.2.3:** `eco-vm-test` stages all 54 core subsystem binaries (16 kernel + 18 OS + 20 DE), sha256 Merkle-hashes them, gates each on `--self-test`, and boots the initramfs in a QEMU/KVM microVM on a Landlock-enforced kernel; PID 1 runs `status` + `--self-test` on every `/bin/<repo>` and the serial log must read `RESULT: 54/54 subsystems verified in hardware VM (fail=0)`.

---

License: Apache-2.0.
