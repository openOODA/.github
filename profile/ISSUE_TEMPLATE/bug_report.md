---
name: Bug Report (AI JSON Diagnostic)
about: Report a compiler error, contract violation, or runtime bug
title: '[BUG]: '
labels: 'bug, AI-diagnostic'
assignees: ''

---

## 🐛 Bug Description
Clear, concise description of what failed.

## 🤖 AI JSON Compiler Diagnostic Payload
Paste output from `ooda run --json-errors <file.oo>`:

```json
{
  "error_type": "...",
  "file": "...",
  "line": 1,
  "column": 1,
  "message": "..."
}
```

## 📜 Reproducible `.oo` Code Snippet
```ooda
pub fn example() {
    // Code to reproduce bug
}
```
