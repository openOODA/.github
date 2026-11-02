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

## The 5-Organization Ecosystem

| Layer & Org | Count | Focus |
| :--- | :---: | :--- |
| **Layer 0: [openOODA](https://github.com/openOODA)** | **14** | Self-hosting compiler (`oodac`), C host substrate (`oodar`), `std`, `cli`, `opm`, `lsp`, `mcp`, `tui`, governance |
| **Layer 1: [openOODA-kernel](https://github.com/openOODA-kernel)** | **16** | Ring-0 NT/seL4 hybrid microkernel (`ookernel-ob`, `ookernel-mm`, `ookernel-sched`, `ookernel-ipc`) & Ring-3 drivers |
| **Layer 2: [openOODA-OS](https://github.com/openOODA-OS)** | **16** | Zero-root system daemons (`ooinit`, `oovfs`, `oonetd`, `oosysbus`, `oohealthd`, `ooimage`) |
| **Layer 3: [openOODA-tools](https://github.com/openOODA-tools)** | **256** | Userland CLI / TUI / MCP utilities across 12 functional categories (`oosh`, `oogrep`, `oofind`, `oojq`) |
| **Layer 4: [openOODA-DE](https://github.com/openOODA-DE)** | **18** | Capability Wayland Desktop Environment (`oocomp`, `oowm`, `oopanel`, `ooportal`, `ooterm`, `ooagent-hud`) |

## Layer 0 Constellation (14 Repositories in `@openOODA`)

| Layer | Repo | Role |
|:---|:---|:---|
| **Governance** | [openOODA](https://github.com/openOODA/openOODA) | The laws and RFCs. They do not change. |
| **Compiler** | [oodac](https://github.com/openOODA/oodac) | Self-hosting compiler (`.oo` → LLVM IR → native). |
| **Substrate** | [oodar](https://github.com/openOODA/oodar) | C host substrate: Landlock sandbox, PQC, ROCm GPU. |
| **Library** | [std](https://github.com/openOODA/std) | 8-domain standard library: 188 modules, linear-arena memory. |
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

---

License: Apache-2.0.
