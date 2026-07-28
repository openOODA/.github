# Welcome to openOODA Organization ⚡

<p align="center">
  <b>The AI-Native, Capability-Secure, Self-Testing Systems Programming Language</b>

🌐 **Official Public Website**: **[`https://openOODA.github.io`](https://openOODA.github.io)**</b>
</p>

---

## ⚡ What is OODA?

**OODA** (*Observe, Orient, Decide, Act*) is a modern programming language designed specifically for the era of high-velocity AI co-authoring ("vibe coding"), capability sandboxing, zero-day defense, and zero-overhead performance.

### 🌟 Key Architectural Pillars

* 🔒 **Capability-Based Sandboxing**: Default-deny security. Functions doing I/O must take explicit `&NetCap` or `&FsCap` tokens.
* 🧪 **Self-Testing Code**: Executable contracts (`requires`/`ensures`) and co-located `verify` test blocks.
* 🤖 **AI-Native Toolchain**: `--json-errors` emits machine-readable AST diff patches for 1-turn AI auto-fixing.
* ⚡ **Dual Engine Velocity**: Instant JIT mode for sub-second edit loops + Native LLVM IR compiler (`ooda build --release`) with 0ms GC pauses via RAII & Region Arenas.

---

## 🏛️ Ecosystem Repositories

| Repository | Purpose |
| :--- | :--- |
| ⚙️ **[openOODA/ooda](https://github.com/openOODA/ooda)** | Core Compiler, JIT Evaluator, LLVM Backend, & CLI Toolchain |
| 📜 **[openOODA/spec](https://github.com/openOODA/spec)** | Formal `ooda.ebnf` Grammar (< 2k tokens) & Architecture Specification |
| 📦 **[openOODA/std](https://github.com/openOODA/std)** | Standard Library Modules (`std::net`, `std::fs`, `std::json`, `std::crypto`) |
| 📚 **[openOODA/docs](https://github.com/openOODA/docs)** | Official Documentation Site & Developer Tutorials |
| 🧪 **[openOODA/qa](https://github.com/openOODA/qa)** | External Quality Assurance (QA) & E2E Integration Test Suite |
| 🚀 **[openOODA/helloworld](https://github.com/openOODA/helloworld)** | Starter Application Template |
| 🧩 **[openOODA/vscode](https://github.com/openOODA/vscode)** | VSCode & Cursor IDE Syntax Highlighting Extension |
| 🌳 **[openOODA/tree-sitter](https://github.com/openOODA/tree-sitter)** | Tree-Sitter Parser Grammar for Zed, Neovim, and GitHub |

---

## ⚡ Quickstart

```bash
# Clone and build the compiler
git clone https://github.com/openOODA/ooda.git
cd ooda
cargo build --release

# Run a hello world script
./target/release/ooda run examples/hello.oo
```
