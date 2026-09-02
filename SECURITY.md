# Security Policy

The openOODA project enforces capability security, zero ambient authority, and continuous adversarial validation across all compiler, runtime, and ecosystem components.

---

## 1. Supported Versions

Security patches and vulnerability remediation are actively maintained for the following versions:

| Version | Status | Security Support | Architectures |
|---|---|---|---|
| Current (`ooda/ooda.pkg` + `git tag v*` SSoT) | **Active** | Full Capability & Adversarial Updates | `x86_64`, `aarch64`, `wasm32` |
| Previous tag (`git tag --sort=-v:refname`) | **Maintenance** | Critical Security Fixes Only | `x86_64` |
| `< previous` | **End of Life** | Unsupported — Upgrade Immediately | N/A |

---

## 2. Reporting a Vulnerability

We treat all potential security vulnerabilities with the highest priority. If you discover a security vulnerability or capability bypass in openOODA:

1. **Do NOT open a public GitHub issue.**
2. **Email the Security Swarm**: Send encrypted vulnerability reports to `security@openooda.org`.
3. **Report Contents**:
   - Detailed description of the vulnerability and security impact.
   - Minimal reproduction script (`.oo` source file exercising the defect).
   - Identification of violated capability boundaries or runtime gates.
   - Any proposed patch or mitigation.
4. **Coordinated Disclosure SLA**:
   - **Triage & Acknowledgment**: Within 24 hours.
   - **Adversarial Assessment & Reproduction**: Within 72 hours.
   - **Signed Patch Release & Advisory**: Within 7 days.

---

## 3. Capability Security Boundary Doctrine

openOODA enforces **Pillar 5 (Capability Security & Zero Ambient Authority)**. Software operates without ambient privileges to the host filesystem, network, system clocks, or OS processes.

### The 14 Unforgeable Capability Tokens

Every privileged operation requires an unforgeable capability token passed as an explicit first parameter:

| Capability Token | Scope & Lowered Operations | Security Boundary |
|---|---|---|
| `&FsReadCap` | `read_file`, `path_exists`, `file_size`, `fs_read_dir` | Confined to `OODA_FS_READDIR` sandbox |
| `&FsWriteCap` | `write_file`, `fs_mkdir`, `remove_file`, `rmdir` | Confined to `OODA_FS_WRITEDIR` sandbox |
| `&FsCap` | Combined filesystem read and write operations | Sandbox path containment |
| `&ProcessCap` | `sys_exec`, `sys_spawn`, `sys_wait`, `sys_kill` | Sanitized environment variable scrub |
| `&SysCap` | `landlock_restrict`, `rlimit_set_*`, OS syscalls | Kernel Landlock sandbox boundary |
| `&NetCap` | Low-level raw network socket dispatch | Strict packet bounds |
| `&HttpCap` | Outbound HTTP/1.0 `fetch` client operations | URL and network boundary |
| `&TcpCap` | `tcp_connect`, `tcp_read`, `tcp_write`, `tls_connect` | Host and port socket boundary |
| `&UdpCap` | `bind_udp`, `udp_recv`, `resolve_ipv4` (DNS queries) | Datagram endpoint boundary |
| `&BindCap` | Server listening ports (`tcp_bind`) | Local port binding authority |
| `&EnvCap` | Environment variable inspection (`env_get`) | Restricted to `OODA_*` / `OO_*` keys |
| `&TimeCap` | Monotonic clock and timer (`now_ms`, `sleep_ms`) | Timer resolution containment |
| `&RandCap` | Cryptographic entropy generation (`random`, `seed`) | Entropy pool protection |
| `&AllocCap` | Linear arena memory allocations (`arena_create`, `alloc`) | Memory quota and zero-leak boundary |

---

## 4. Zero Ambient Authority Rules

1. **Explicit Parameter Passing**: Helper functions cannot mint or manufacture capabilities. Tokens must be passed explicitly from caller to callee.
2. **DINNER CAPs Specification**: Every privileged function declares its exact capability tokens in a `// ## CAPs` header block.
3. **Compile-Time SMT Check Elision**: `oodac/check_caps.oo` verifies capability tokens at compile time. Validated calls eliminate runtime branch overhead while preserving mathematical safety.
4. **Runtime Token Sealing**: 64-bit unforgeable handles in `ooda/runtime/chs_rt_caps.c` validate caller grants before any privileged syscall.

---

## 5. Fail-Closed Incident Response Protocol

1. **Immediate Execution Termination**: Any missing, invalid, null, or forged capability token immediately terminates execution via `process_exit(1)` with standard capability diagnostics (`ERR\tcap\t...`).
2. **Deterministic Sandboxing**: Subprocesses execute with scrubbed environment variables and Landlock filesystem restrictions.
3. **Continuous Red Team Validation**: Every security remediation requires an adversarial falsification probe added to `openOODA/scripts/redteam_orchestrate.oo` and `qa/`.
4. **Minisign Cryptographic Verification**: All official releases are signed with Ed25519 public key:
   `RWTrl0z1EzuELsS9SzufTcBTXLV5kUWiO7Yu+WyJqN4wgoKLblKv5NkA`.
