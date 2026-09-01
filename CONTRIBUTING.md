# Contributing to openOODA

Welcome to the openOODA ecosystem. openOODA is engineered for high-performance, deterministic systems programming and autonomous AI agent swarms governed by Colonel John Boyd's Energy-Maneuverability (E-M) principles and capability security.

---

## 1. Development Philosophy

All contributions to openOODA adhere to three foundational philosophies:

1. **First Principles & Hardware Grounding**: Algorithms, type representations, and instruction sets derive directly from silicon physics, IEEE 754, NIST Known Answer Tests, and IETF RFCs.
2. **Subtractive Optimization Law**: Software improves by systematic subtraction. We remove garbage collection pauses, ambient authority, null pointers, dynamic dispatch, and unnecessary intermediate files.
3. **Boyd's Energy-Maneuverability Formula**:
   $$P_{s,\text{info}} = \left( \frac{T - D}{W} \right) \cdot V$$
   - **Thrust ($T$)**: Maximize instruction throughput, SIMD execution, and direct machine code emission.
   - **Drag ($D$)**: Eliminate heap allocation locks, rebuild latency, and unneeded context ingestion.
   - **Weight ($W$)**: Minimize binary size, AST memory footprint, and external dependencies.
   - **Velocity ($V$)**: Maximize incremental compilation turnaround and agent loop frequency.

---

## 2. The 10 Governance Pillars

Every commit, pull request, and architecture change must align with the 10 Governance Pillars:

1. **Pillar 1 — First Principles & Specification Derivation**: Root-cause defects and build real AST pipelines. Prohibit regex heuristics and canned mocks.
2. **Pillar 2 — Boyd's E-M Engine & Subtractive Design**: Elevate the OODA loop from raw CPU cycles to typed AST analysis and SMT contract orientation.
3. **Pillar 3 — Negative Trust & Adversarial Falsification**: Assume unverified code contains defects until proven. Multi-agent teams deploy the 4 Adversarial Red Team roles (`REDTEAM.oot`).
4. **Pillar 4 — Power Law 80/20 Leverage**: Focus development on high-leverage primitives: SSA mem2reg, flat closures, SIMD vectorization, direct ELF64/WASM emission, and linear arenas.
5. **Pillar 5 — Capability Security & Zero Ambient Authority**: All privileged operations require one of the 14 unforgeable capability tokens (`&CapName`).
6. **Pillar 6 — Multi-Agent Swarm Safety & Layer Stratification**: Stratify architectures into Generational tiers (Gen 1 silicon through Gen 6 autonomous synthesis).
7. **Pillar 7 — Deterministic Bit-Identical Reproducibility**: Builds produce bit-identical binaries with zero-timestamp SHA-256 Merkle digests.
8. **Pillar 8 — Sparing Ingress & Token Economy**: Query architectures via `ooda outline` and AST reflection to eliminate context token waste.
9. **Pillar 9 — Boundary Physics & SMT Decidability**: Bound verification to decidable SMT logics (QF_LIA, QF_BV) under Rice's Theorem and Landauer's thermodynamic limit.
10. **Pillar 10 — Generational Evolution & Fail-Closed Invariants**: Releases follow Generational Semantic Versioning (`v<Floor>.<Thrust>.<Patch>`) with zero unhandled panics.

---

## 3. Strict Invariants & Coding Standards

### 3.1 Strict 256-Line Limit
Every `.oo` source file and `.oot` documentation file must strictly contain **$\le 256$ lines**. Large files must be modularized across clean domain seams.

### 3.2 Academy Header Standards

#### A. Source Code (`.oo` files)
Every `.oo` file begins with a 4-element Academy header in ASD-STE100 technical English:
```rust
// # <Title>
//
// Logline: <One sentence in present tense, active voice, ending with a period.>
//
// Setup: <Preconditions, required capability tokens, or runtime assumptions.>
//
// Beats:
//   1. <First action or responsibility>
//   2. <Second action or responsibility>
//   3. <Third action or responsibility>
```

#### B. Documentation (`.oot` files)
Every `.oot` file begins with a 4-element document header:
```markdown
# <NAME> — <Domain or Purpose Title>
Floor: 2
Thrust: 9
Patch: 2
File: <path/to/file.oot>
```

### 3.3 Zero Ambient Authority & OCap Rules
- Privilege operations require an explicit capability token (`&FsReadCap`, `&FsWriteCap`, `&ProcessCap`, etc.).
- Never mint capability tokens ambiently in helper functions; accept them as caller arguments.

---

## 4. Testing & Verification Requirements

### 4.1 Double-Run Test Law
All test suites and verification scripts must be executed twice sequentially in clean, independent processes:
```bash
./ooda/bin/ooda run <path/to/test.oo>
./ooda/bin/ooda run <path/to/test.oo>
```

### 4.2 Master Governance Linters
Before submitting a PR, verify that all master linters pass with `0` errors:
```bash
./ooda/bin/ooda run openOODA/scripts/enforcer.oo
./ooda/bin/ooda run openOODA/scripts/check_board.oo
./ooda/bin/ooda run openOODA/scripts/verify_all.oo
./ooda/bin/ooda run openOODA/scripts/redteam_hook.oo
```

---

## 5. Commit & Version Conventions

1. **Conventional Commit Prefixes**:
   - `feat:` — New compiler/runtime feature or capability.
   - `fix:` — Bug fix or defect remediation.
   - `sec:` — Capability security boundary or token remediation.
   - `audit:` — Audit logs and compliance certifications.
   - `perf:` — Boyd E-M performance or SIMD optimization.
   - `docs:` — Process board or specification updates.
2. **Generational Semantic Versioning**:
   - Syntax: `v<Floor>.<Thrust>.<Patch>` (Current: see `ooda/ooda.pkg` `version` and `git tag --sort=-v:refname | head -1` — SSoT, no duplicate pins).
   - Floor ($F$): Increments on breaking changes to core memory or capability ABI.
   - Thrust ($T$): Increments on performance gains and non-breaking features.
   - Patch ($P$): Increments on bug repairs and security remediation.
