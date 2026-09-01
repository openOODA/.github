---
name: Bug Report
about: Report a defect, capability violation, or unexpected behavior in openOODA
title: '[BUG]: '
labels: ['bug', 'triage']
assignees: ''
---

## 1. Defect Description
A clear and concise description of the bug or unexpected behavior.

## 2. Minimal Reproduction Code
Provide a minimal `.oo` source snippet that reproduces the issue:

```rust
// minimal_repro.oo
pub fn main() {
    // reproduction code
}
```

## 3. Execution Commands & Observed Output
```bash
./ooda/bin/ooda run minimal_repro.oo
```

**Observed Output:**
```
[paste error output or stack trace here]
```

## 4. Expected Behavior
A clear description of what should happen according to the openOODA specification.

## 5. Environment & System Details
- **openOODA Version**: run `./ooda/bin/ooda --version` and check `ooda/ooda.pkg` `version` / `git tag` (SSoT — do not pin)
- **Host OS**: Linux (x86_64 / aarch64)
- **Compiler / Toolchain**: GCC / Clang
- **Relevant Capability Tokens**: (e.g. `&FsReadCap`, `&ProcessCap`)

## 6. Additional Context / Red Team Analysis
Add any other context, SMT verification logs, or adversarial break-tests related to the problem.
