<div align="center">

# openOODA
### Sovereign Systems Programming Language & Autonomic AI Substrate

[![Version](https://img.shields.io/github/v/tag/openOODA/ooda?label=version&style=flat-square&labelColor=0b0e14&color=00f2fe)](https://github.com/openOODA/ooda/releases)<!-- SSoT: ooda/ooda.pkg + git tag v* — no manual pin -->
[![10-Pillar Enforcer](https://img.shields.io/badge/10--Pillar%20Enforcer-PASS%20(__FAILS__%3D0)-00e676.svg?style=flat-square)](https://github.com/openOODA/openOODA)
[![8D Red Team](https://img.shields.io/badge/8D%20Red%20Team-PASS%20(9%20Gates)-brightgreen.svg?style=flat-square)](https://github.com/openOODA/ooda)
[![13 Process Boards](https://img.shields.io/badge/13%20Process%20Boards-13%2F13%20VERIFIED-7928ca.svg?style=flat-square)](https://github.com/openOODA/openOODA)
[![Zero Ambient Authority](https://img.shields.io/badge/Zero%20Ambient%20Authority-14%20OCap%20Tokens-ff0055.svg?style=flat-square)](https://github.com/openOODA/openOODA/blob/main/SECURITY.oot)
[![Coordination Drag](https://img.shields.io/badge/Coordination%20Drag--95.5%25%20(3--Tier)-blue.svg?style=flat-square)](https://openooda.org)
[![License](https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-ffd700.svg?style=flat-square)](LICENSE)

```text
   ____  ____  ___  ____    ___   ___  ____    _   
  / __ \/ __ \/ _ \/ __ \  / _ \ / _ \|  _ \  / \  
 / /_/ / /_/ /  __/ / / / | | | | | | | | | |/ _ \ 
 \____/ .___/\___/_/ /_/  | |_| | |_| | |_| / ___ \
     /_/                   \___/ \___/|____/_/   \_\
   Observe · Orient · Decide · Act — Sovereign Development Substrate
```

**Zero Ambient Authority · Energy-Maneuverability · Landlock LSM Sandboxing · AI Swarm Locality**

[Portal & Documentation](https://openooda.org) • [Standard Library](https://github.com/openOODA/ooda) • [Governance Boards](https://github.com/openOODA/openOODA) • [Package Registry](https://registry.openooda.org) • [Playground](https://openooda.org/play.html)

---

</div>

## Overview

**openOODA** is a sovereign systems programming language, deterministic compiler toolchain, and autonomic runtime substrate designed from first principles for capability-safe systems and autonomous AI agent swarms.

Engineered around **Col. John Boyd's Energy-Maneuverability ($P_s$) theory**, openOODA replaces runtime indeterminism, garbage collection drag, and ambient authority vulnerabilities with an unforgeable 14-token Object Capability (OCap) security lattice, linear bump-arena memory management, 256-bit SIMD vector codegen, and native multi-backend compilation (direct x86_64, AArch64, standalone WebAssembly, and C99 + Linux Landlock LSM).

```bash
# Universal Zero-Dependency Bootstrap
curl -fsSL https://openooda.org/install.sh | bash
```

---

## 3-Tier Sovereign Topology Lattice

The openOODA ecosystem is partitioned into a strict 3-Tier DAG architecture. This minimal closed topology collapses $N=12$ fragmented repositories into $N=3$ sovereign domains, eliminating **95.5% of inter-agent coordination drag**:

$$C(N) = \frac{N(N - 1)}{2} \implies C(12) = 66 \text{ channels} \longrightarrow C(3) = 3 \text{ channels} \quad \left(\Delta = -95.5\%\right)$$

```text
═════════════════════════════════════════════════════════════════════════════════════════════
                              openOODA 3-TIER SOVEREIGN TOPOLOGY LATTICE
═════════════════════════════════════════════════════════════════════════════════════════════

  ┌─────────────────────────────────────────────────────────────────────────────────────────┐
  │ TIER 1: GOVERNANCE & META-SPECIFICATION (openOODA)                                      │
  │ ├─ 13 Canonical Process Boards (START, RULES, NORTHSTAR, SECURITY, ROADMAP, FORMAT...)  │
  │ ├─ Formal RFC Specifications (openOODA/rfcs/*.oot)                                      │
  │ ├─ Academic Research Archive (openOODA/research/RP-*.oot)                               │
  │ └─ Deterministic Rule Enforcers (enforcer.oo, check_board.oo, verify_all.oo)            │
  └────────────────────────────────────────────┬────────────────────────────────────────────┘
                                               │ Directs Architecture Contracts
                                               ▼
  ┌─────────────────────────────────────────────────────────────────────────────────────────┐
  │ TIER 2: DETERMINISTIC ENGINE & TOOLCHAIN (ooda)                                         │
  │ ├─ Compiler Core (oodac: x86_64, AArch64, standalone WASM, C99, GPU Backends)          │
  │ ├─ Runtime Substrate & Landlock LSM Sandbox (runtime/chs_rt_cap.c, chs_rt_alloc.c)      │
  │ ├─ Standard Library (std/) & 18-Tool Cognitive Discovery Matrix (cli/cmd_mcp.oo)        │
  │ ├─ Unified 8-Gate Red Team Engine (qa/ + redteam_hook.oo)                               │
  │ └─ Language Tools (ooda.ebnf, tree-sitter, vscode, stdio JSON-RPC LSP, MCP Server)      │
  └────────────────────────────────────────────┬────────────────────────────────────────────┘
                                               │ Delivers Certified Artifacts
                                               ▼
  ┌─────────────────────────────────────────────────────────────────────────────────────────┐
  │ TIER 3: DISTRIBUTION & PUBLIC PORTAL (openOODA.github.io)                               │
  │ ├─ Public Documentation Static Site (SSG Docs & Research Renderings)                   │
  │ ├─ Cryptographic Package Index (registry/index, index.minisig)                          │
  │ ├─ Secure Bootstrap Installers (install.sh, install.ps1 with Minisign Ed25519)          │
  │ └─ WebAssembly Interactive Portal & Visual Dogfight Simulation Engine                   │
  └─────────────────────────────────────────────────────────────────────────────────────────┘
═════════════════════════════════════════════════════════════════════════════════════════════
```

<div align="center">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="auto">
  <defs>
    <linearGradient id="gradCyan" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#4facfe" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="gradBlue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#243949" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#517fa4" stop-opacity="0.9"/>
    </linearGradient>
    <linearGradient id="gradAmber" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#f6d365" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#fda085" stop-opacity="0.9"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <rect width="900" height="480" fill="#0b0e14" rx="12"/>
  
  <!-- Tier 1 -->
  <rect x="50" y="30" width="800" height="100" rx="8" fill="#151b23" stroke="#00f2fe" stroke-width="2"/>
  <text x="70" y="60" fill="#00f2fe" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">TIER 1: GOVERNANCE &amp; META-SSoT (openOODA)</text>
  <text x="70" y="85" fill="#8b949e" font-family="JetBrains Mono, monospace" font-size="13">13 Process Boards · RFC Specifications · Research Archive · Deterministic Enforcers</text>
  <text x="70" y="105" fill="#58a6ff" font-family="JetBrains Mono, monospace" font-size="12">10-Pillar Enforcer (__FAILS__=0) · 13/13 Boards Verified · Zero Ambient Authority</text>

  <!-- Arrow 1->2 -->
  <line x1="450" y1="130" x2="450" y2="170" stroke="#00f2fe" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="445,165 450,175 455,165" fill="#00f2fe"/>

  <!-- Tier 2 -->
  <rect x="50" y="175" width="800" height="120" rx="8" fill="#151b23" stroke="#58a6ff" stroke-width="2"/>
  <text x="70" y="205" fill="#58a6ff" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">TIER 2: SOVEREIGN COMPILER &amp; RUNTIME ENGINE (ooda)</text>
  <text x="70" y="230" fill="#8b949e" font-family="JetBrains Mono, monospace" font-size="13">Self-Hosted Compiler (oodac) · 14 OCap Tokens · Linux Landlock LSM · Pure stdio LSP &amp; MCP</text>
  <text x="70" y="255" fill="#8b949e" font-family="JetBrains Mono, monospace" font-size="13">Standard Library (std/) · 8-Gate Red Team Engine · 8-Lane SIMD (f32x8) Boyd E-M Engine</text>
  <text x="70" y="275" fill="#7ee787" font-family="JetBrains Mono, monospace" font-size="12">8D Red Team Certified · 2,500 Hz OODA Loop · 0ms GC Pauses · 28 KB ELF Footprint</text>

  <!-- Arrow 2->3 -->
  <line x1="450" y1="295" x2="450" y2="335" stroke="#58a6ff" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="445,330 450,340 455,330" fill="#58a6ff"/>

  <!-- Tier 3 -->
  <rect x="50" y="340" width="800" height="105" rx="8" fill="#151b23" stroke="#f6d365" stroke-width="2"/>
  <text x="70" y="370" fill="#f6d365" font-family="JetBrains Mono, monospace" font-size="16" font-weight="bold">TIER 3: DISTRIBUTION &amp; PUBLIC PORTAL (openOODA.github.io)</text>
  <text x="70" y="395" fill="#8b949e" font-family="JetBrains Mono, monospace" font-size="13">Single-Page Application Portal · SSG Documentation Hub · Interactive WASM Playground</text>
  <text x="70" y="415" fill="#8b949e" font-family="JetBrains Mono, monospace" font-size="13">Ed25519-Signed Package Registry · Universal Bootstrap (install.sh / install.ps1)</text>
  <text x="70" y="435" fill="#ffa657" font-family="JetBrains Mono, monospace" font-size="12">Minisign Ed25519 Verified · 95.5% Coordination Drag Reduction · Fail-Closed Ingestion</text>
</svg>

</div>

---

## Energy-Maneuverability ($P_s$) & SIMD Benchmarks

In classical aeronautics, Col. John Boyd defined Specific Excess Power ($P_s$) as the instantaneous climb and acceleration rate:

$$P_s = V \cdot \frac{T - D}{W}$$

In openOODA, software execution is governed by the **Informational Energy-Maneuverability Formulation**:

$$P_{s,\text{info}} = \left(\frac{T_{\text{semantic}} - D_{\text{systemic}}}{W_{\text{entropy}}}\right) \cdot V_{\text{ooda}}$$

Where:
- $T_{\text{semantic}}$ = Meaningful computation, typed SSA transformations, and direct machine code emission.
- $D_{\text{systemic}} = D_{\text{rebuild}} + D_{\text{token\_burn}} + D_{\text{alloc}} + D_{\text{search}} + D_{\text{verify}} \longrightarrow 0$.
- $W_{\text{entropy}}$ = AST weight, stack frame footprint ($28\,\text{KB}$ binary), and memory overhead ($0\,\text{ms}$ GC pauses).
- $V_{\text{ooda}}$ = Cycle frequency ($2,500\,\text{Hz}$ / $0.4\,\text{ms}$ turn rate).

### SIMD & Performance Telemetry

| Metric | openOODA Substrate | Legacy VM / Runtime | Advantage |
|---|---|---|---|
| **OODA Cycle Rate** | **2,500 Hz** ($0.4\,\text{ms}$) | 0.02 Hz ($50\,\text{s}$) | **125,000× faster turnover** |
| **Specific Excess Power ($P_s$)** | **+510,000.00 ft/s** ($850\times$) | -450.00 ft/s (drag-limited) | **Unbounded energy gain** |
| **SIMD Vectorization** | **8-Lane `f32x8` AVX2 / AVX-512** | Scalar / Auto-vectorized | **8× hardware parallelism** |
| **AST Cache Turnaround** | **< 100 μs** (Merkle AST Hash) | 2.5 s - 15.0 s (re-parse) | **25,000× latency reduction** |
| **GC / Allocation Pause** | **0 ms** (Linear Arena $O(1)$ reset) | 15 ms - 250 ms stop-the-world | **Deterministic real-time** |
| **Standalone Binary Size** | **28 KB** (Stripped ELF64) | 45 MB - 120 MB | **99.9% weight reduction** |
| **Token Ingress Compression** | **$\rho \ge 98.7\%$** ($50\text{k} \to 600$ lines) | 0% (raw ingest) | **76× context efficiency** |

---

## Zero Ambient Authority: The 14 Capability Tokens

openOODA enforces pure Object Capability security (OCap). **Functions possess zero ambient authority**: code cannot read disk, access network, spawn processes, or allocate memory unless an unforgeable capability token reference is explicitly passed as a parameter.

| # | Capability Token | Domain | Operations Granted | Fail-Closed Error Code |
|---|---|---|---|---|
| 1 | `&FsReadCap` | Filesystem Read | `read_file`, `path_exists`, `file_size`, `fs_read_dir`, `fs_is_dir` | `ERR_CAP_FS_READ` |
| 2 | `&FsWriteCap` | Filesystem Write | `write_file`, `fs_mkdir`, `remove_file`, `rmdir`, `hardlink`, `symlink` | `ERR_CAP_FS_WRITE` |
| 3 | `&FsCap` | Broad Filesystem | Unified superset token covering read, write, and directory management | `ERR_CAP_FS` |
| 4 | `&ProcessCap` | Process Control | `sys_exec`, `process_exec`, `sys_spawn`, `sys_wait`, `sys_kill` | `ERR_CAP_PROCESS` |
| 5 | `&SysCap` | OS & Sandboxing | `landlock_restrict`, `sys_epoll_create`, `sys_inotify_init`, `rlimit_set_*` | `ERR_CAP_SYS` |
| 6 | `&NetCap` | Broad Network | Raw socket operations (`sock_raw`), interface bindings | `ERR_CAP_NET` |
| 7 | `&HttpCap` | HTTP Client | Confined HTTP/1.0 GET client operations (`fetch`) | `ERR_CAP_HTTP` |
| 8 | `&TcpCap` | TCP Networking | `tcp_connect`, `tcp_read`, `tcp_write`, `tcp_close`, `tls_connect` | `ERR_CAP_TCP` |
| 9 | `&UdpCap` | UDP Networking | `bind_udp`, `udp_recv`, `resolve_ipv4` (DNS queries) | `ERR_CAP_UDP` |
| 10 | `&BindCap` | Server Listening | `tcp_bind` (listening port creation) | `ERR_CAP_BIND` |
| 11 | `&EnvCap` | Environment | `env_get` (strictly confined to `OODA_*` and `OO_*` keys) | `ERR_CAP_ENV` |
| 12 | `&TimeCap` | Monotonic Clock | `now_ms`, `sleep_ms` (`CLOCK_MONOTONIC`, `CLOCK_REALTIME`) | `ERR_CAP_TIME` |
| 13 | `&RandCap` | Cryptographic PRNG| `random`, `seed` (hardware entropy harvesting) | `ERR_CAP_RAND` |
| 14 | `&AllocCap` | Linear Bump Arena | `arena_create`, `alloc`, `alloc_bytes`, `reset` ($O(1)$ bulk resets) | `ERR_CAP_ALLOC` |

---

## 18-Tool MCP Cognitive Discovery Matrix

The openOODA toolchain includes a zero-configuration Model Context Protocol (MCP) server and stdio JSON-RPC LSP that automatically connects to 18 modern developer environments and AI coding agents:

```text
┌───────────────────────────────────────────────────────────────────────────────────────────┐
│                        18-TOOL COGNITIVE DISCOVERY MATRIX (cmd_mcp.oo)                    │
├───────────────────────────────────────────────────────────────────────────────────────────┤
│  [1] Aider             [6] Continue          [11] Helix            [16] Pi                │
│  [2] Antigravity       [7] Cursor            [12] Muse             [17] VS Code           │
│  [3] Charm             [8] Devin             [13] Neovim           [18] Zed               │
│  [4] Claude Code       [9] Goose             [14] OpenCode CLI                            │
│  [5] Claude Desktop   [10] Grok              [15] OpenCode TUI                            │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

Auto-detect and wire all tools with a single command:
```bash
ooda mcp setup --all
```

---

## Quickstart

### 1. Universal Installer
```bash
# macOS & Linux (x86_64 / AArch64)
curl -fsSL https://openooda.org/install.sh | bash

# Windows (PowerShell)
irm https://openooda.org/install.ps1 | iex
```

### 2. Verify Cryptographic Integrity
All official distribution archives are signed with Minisign Ed25519 (version from `ooda/ooda.pkg` SSoT):
```bash
VER=$(grep 'version = ' ooda/ooda.pkg | cut -d'"' -f2)
minisign -Vm "ooda-v${VER}-x86_64-linux.tar.gz" \
  -P RWTrl0z1EzuELsS9SzufTcBTXLV5kUWiO7Yu+WyJqN4wgoKLblKv5NkA
```

### 3. Build & Run
```bash
# Initialize a new openOODA project
ooda init my_agent

# Check, test, and execute
ooda check main.oo
ooda test
ooda run main.oo
```

---

## Ecosystem Navigation

- **[openOODA/openOODA](https://github.com/openOODA/openOODA)**: Tier 1 Governance Single Source of Truth (SSoT), 13 Process Boards, RFC specifications, research archive, and rule enforcers.
- **[openOODA/ooda](https://github.com/openOODA/ooda)**: Tier 2 Self-hosted compiler (`oodac`), capability runtime, standard library (`std/`), LSP, MCP server, and 8-gate Red Team suite.
- **[openOODA/openOODA.github.io](https://github.com/openOODA/openOODA.github.io)**: Tier 3 Documentation portal, interactive WASM playground, signed package index, and distribution staging.

---

## License

Dual-licensed under either of:
- **MIT License** ([LICENSE-MIT](LICENSE-MIT) or https://opensource.org/licenses/MIT)
- **Apache License, Version 2.0** ([LICENSE-APACHE](LICENSE-APACHE) or https://www.apache.org/licenses/LICENSE-2.0)

at your option.
