<div align="center">

<pre>
   ____  ____  ___  ____    ___   ___  ____    _
  / __ \/ __ \/ _ \/ __ \  / _ \ / _ \|  _ \  / \
 / /_/ / /_/ /  __/ / / / | | | | | | | | | |/ _ \
/_____/ .___/\___/_/ /_/  | |_| | |_| | |_| / ___ \
      /_/                   \___/ \___/|____/_/   \_\
</pre>

### openOODA — Primary Systems Language & 5-Organization Ecosystem for the AI Era

[openooda.org](https://openooda.org) • [llms.txt](https://openooda.org/llms.txt) • [openOODA-kernel](https://github.com/openOODA-kernel) • [openOODA-OS](https://github.com/openOODA-OS) • [openOODA-tools](https://github.com/openOODA-tools) • [openOODA-DE](https://github.com/openOODA-DE)

</div>

Your process is born with no privileges. That is not an accident. That is the type system.

We assume the source is hostile, the tests are optimistic, and the agent will try the network. Then we make those attempts fail closed.

```sh
curl -fsSL https://openooda.org/install.sh | bash
```

Public home: [openooda.org](https://openooda.org). Copy: [`docs/HOME.oot`](../docs/HOME.oot).

## The 5-Organization Ecosystem (325 Repositories at v0.2.3)

| Layer & Org | Count | Focus |
| :--- | :---: | :--- |
| **Layer 0: [openOODA](https://github.com/openOODA)** | **14** | Self-hosting compiler (`oodac`), C host substrate (`oodar` with Landlock, `sys_spawn`/`sys_wait`, `OODA_LISTEN_FD`), `std`, `cli`, `opm`, `lsp`, `mcp`, `tui`, governance |
| **Layer 1: [openOODA-kernel](https://github.com/openOODA-kernel)** | **16** | Ring-0 NT/seL4 hybrid microkernel (`ookernel-ob`, `ookernel-mm`, `ookernel-sched`, `ookernel-ipc`) & Ring-3 drivers |
| **Layer 2: [openOODA-OS](https://github.com/openOODA-OS)** | **18** | Zero-root system daemons (`ooinit`, `oosvc-mgr`, `oovfs`, `oonetd`, `oosysbus`, `oohealthd`, `ooimage`, `ooaid --serve`, `oorealm`) |
| **Layer 3: [openOODA-tools](https://github.com/openOODA-tools)** | **257** | Userland CLI / TUI / MCP utilities across 12 functional categories (`oosh`, `oogrep`, `oofind`, `oojq`, `oollama`) |
| **Layer 4: [openOODA-DE](https://github.com/openOODA-DE)** | **20** | Capability Wayland Desktop Environment (`oocomp`, `oowm`, `oopanel`, `ooportal`, `oobazaar`, `oocockpit`, `ooagent-hud`) |

## Layer 0 Constellation (14 Repositories in `@openOODA`)

| Layer | Repo | Role |
|:---|:---|:---|
| **Governance** | [openOODA](https://github.com/openOODA/openOODA) | The laws and RFCs. They do not change. |
| **Compiler** | [oodac](https://github.com/openOODA/oodac) | Self-hosting compiler (`.oo` → LLVM IR → native). |
| **Substrate** | [oodar](https://github.com/openOODA/oodar) | C host substrate: Landlock sandbox (`PR_SET_NO_NEW_PRIVS`), non-blocking `sys_spawn`/`sys_wait`/`sys_kill`, `OODA_LISTEN_FD` socket activation, PQC, GPU. |
| **Library** | [std](https://github.com/openOODA/std) | 8-domain standard library: 188 modules, linear-arena memory, `tcp_bind` socket slot tables. |
| **Toolchain** | [cli](https://github.com/openOODA/cli) | Primary developer driver (build, test, fmt, qa). |
| | [ooda](https://github.com/openOODA/ooda) | Top-level workflow command runner. |
| | [opm](https://github.com/openOODA/opm) | Capability-aware deterministic package manager. |
| | [catalog](https://github.com/openOODA/catalog) | Public package registry for `opm`. |
| | [install](https://github.com/openOODA/install) | One-line toolchain bootstrap & package hooks. |
| **Agent / Editor** | [lsp](https://github.com/openOODA/lsp) | Language Server Protocol daemon for editor diagnostics. |
| | [mcp](https://github.com/openOODA/mcp) | Model Context Protocol server (26 capability-aware agent tools). |
| | [tui](https://github.com/openOODA/tui) | Terminal coding harness with prompt dock & live thought canvas. |
| **Web & Community** | [website](https://github.com/openOODA/website) | Source for [openooda.org](https://openooda.org). |
| | [.github](https://github.com/openOODA/.github) | Org profile, shared issue templates, and reusable CI workflows. |

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

---

License: Apache-2.0.
