# openOODA

A systems language for AI-assisted work. Effects take capability tokens.
The product path is: typecheck, emit C, compile with gcc, run.

Public site: https://openooda.github.io
Field guide: https://github.com/openOODA/wiki
Proof stays on the private boards (`openOODA/SHIPPED.oot`).

## What is product

- Compiler and CLI live in `ooda`. Commands: `check`, `build`, `run`, `test`, `fix`, `patch`, `lsp`.
- Native backend is C plus `runtime/chs_rt.c`, then host gcc.
- Product standard library is the small tracked set in `ooda/std` (53 files on the honesty pin).
- LLVM hello and Result `match` are smoke (`emit-llvm` + clang + run). LLVM self-host is residual.
- vscode uses a Node language server: hover, document symbols, `oodac check` diagnostics.

## What is not product

- `cargo` / Rust. That toolchain is gone.
- JIT, 0ms GC, and bit-identical rebuilds.
- Org `std/` file count (thousands of modules, 93 domains). That is volume, not emit+gcc+run.
- HITL. The human loop is `ooda fix`.
- A working public `curl | sh` install. The compiler repo is private. The script pins an old tag and does not check a hash.

## Repositories

| Repo | Role | Notes |
| --- | --- | --- |
| `wiki` | Public field guide | Public. Not product proof |
| `registry` | File-backed vendor | Public. https://registry.openooda.org |
| `openOODA.github.io` | Public site + install endpoint | Public. Not a docs site |
| `ooda` | Compiler, CLI, runtime | Private |
| `openOODA` | Nine process boards | Private. Source of truth for what shipped |
| `std` | Org standard library | Private. Not certified product |
| `docs` | Guides and research papers | Private. Papers are design, not proof |
| `qa` | External tests | Private. e2e still has leftover `.sh` |
| `vscode` | Editor extension | Private. Node LSP, not native `ooda lsp` |
| `tree-sitter` | Editor grammar | Private |
| `helloworld` | Starter | Private |
| `brand` | Logos | Private |

## Build from a checkout

From an `ooda` tree that already has a seed compiler:

```
cd ooda
OODAC_BIN=./bootstrap/seed/oodac bash bootstrap/oodac_pure_build oodac/main.oo oodac/oodac
./oodac/oodac check oodac/main.oo
./bin/ooda run fixtures/hello.oo
```

Do not run `cargo`.
