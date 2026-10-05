<div align="center">

<pre>
   ____  ____  ___  ____    ___   ___  ____    _
  / __ \/ __ \/ _ \/ __ \  / _ \ / _ \|  _ \  / \
 / /_/ / /_/ /  __/ / / / | | | | | | | | | |/ _ \
/_____/ .___/\___/_/ /_/  | |_| | |_| | |_| / ___ \
      /_/                   \___/ \___/|____/_/   \_\
</pre>

### openOODA — Sovereign Systems Language for the AI Era

[openooda.org](https://openooda.org) • [llms.txt](https://openooda.org/llms.txt) • [openOODA-tools](https://github.com/openOODA-tools)

</div>

Your process is born with no privileges. That is not an accident. That is the type system.

We assume the source is hostile, the tests are optimistic, and the agent will try the network. Then we make those attempts fail closed.

```sh
curl -fsSL https://openooda.org/install.sh | bash
```

Public home: [openooda.org](https://openooda.org). Copy: [`docs/HOME.oot`](../docs/HOME.oot).

## The Constellation (14 Repositories)

| Layer | Repo | Role |
|:---|:---|:---|
| **Governance** | [openOODA](https://github.com/openOODA/openOODA) | The laws and RFCs. They do not change. |
| **Compiler** | [oodac](https://github.com/openOODA/oodac) | Sovereign self-hosting compiler (`.oo` → LLVM IR → native). |
| **Substrate** | [oodar](https://github.com/openOODA/oodar) | Gen 1 C host substrate: Landlock sandbox, PQC, ROCm GPU. |
| **Library** | [std](https://github.com/openOODA/std) | 8-domain standard library: 188 modules, linear-arena memory. |
| **Toolchain** | [cli](https://github.com/openOODA/cli) | Sovereign developer driver (build, test, fmt, qa). |
| | [ooda](https://github.com/openOODA/ooda) | Top-level workflow command runner. |
| | [opm](https://github.com/openOODA/opm) | Capability-aware deterministic package manager. |
| | [catalog](https://github.com/openOODA/catalog) | Public package registry for `opm`. |
| | [install](https://github.com/openOODA/install) | One-line toolchain bootstrap & package hooks. |
| **Agent / Editor** | [lsp](https://github.com/openOODA/lsp) | Language Server Protocol daemon for editor diagnostics. |
| | [mcp](https://github.com/openOODA/mcp) | Model Context Protocol server (26 capability-aware agent tools). |
| | [tui](https://github.com/openOODA/tui) | Terminal coding harness with prompt dock & live thought canvas. |
| **Web & Community** | [website](https://github.com/openOODA/website) | Source for [openooda.org](https://openooda.org). |
| | [.github](https://github.com/openOODA/.github) | Org profile, shared issue templates, and reusable CI workflows. |

> Note: [bb](https://github.com/openOODA/bb) (blackbox execution flight recorder) is preserved for historical post-mortem autopsy reference.

---

## 🛠️ The Userland Suite: openOODA-tools

Looking for everyday command-line utilities written in pure openOODA? Visit our sister organization:  
👉 **[openOODA-tools](https://github.com/openOODA-tools)** — Modern replacements for Unix coreutils (`oosh`, `oogrep`, `oodiff`, `oofind`, `oojq`, `ootail`) featuring dual-plane execution: human CLI speed + agent-native MCP.

---

License: Apache-2.0.
