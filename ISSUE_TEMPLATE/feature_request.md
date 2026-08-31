---
name: Feature Request
about: Propose a new feature, compiler optimization pass, or capability extension for openOODA
title: '[FEATURE]: '
labels: ['enhancement', 'proposal']
assignees: ''
---

## 1. Problem Statement / Motivation
Is your feature request related to a problem or performance bottleneck?
A clear and concise description of the motivation (e.g. "I am encountering high rebuild latency when compiling generic AST chunks...").

## 2. Proposed Solution & E-M Impact
A detailed description of the proposed feature or compiler optimization.
- **Thrust ($T$)**: How does this increase semantic throughput or emission speed?
- **Drag ($D$)**: How does this eliminate allocation, search, or rebuild latency?
- **Weight ($W$)**: What is the impact on AST/binary size?
- **Velocity ($V$)**: How does this accelerate the OODA turnaround cycle?

## 3. Capability Security & Boundary Alignment
- Which of the 14 unforgeable capability tokens (`&CapName`) are required?
- How does the feature maintain zero ambient authority and fail-closed safety?

## 4. Alternative Approaches Considered
A description of any alternative designs, workarounds, or prior art considered.

## 5. RFC Backlog / Specification Seams
- Proposed RFC name (e.g. `openOODA/rfcs/0023-feature-name.oot`)
- Affected canonical boards (e.g. `NORTHSTAR.oot`, `ROADMAP.oot`, `SECURITY.oot`)
