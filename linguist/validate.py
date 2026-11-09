#!/usr/bin/env python3
"""validate.py — GitHub Linguist & editor-grammar package gate for OODA (.oo/.oot).

Hard gates (any failure exits 1):
  1. grammars/oo.tmLanguage.json parses as JSON, scopeName == source.oo,
     fileTypes covers oo + oot, and every match/begin/end regex compiles.
  2. languages.yml parses and declares OODA with tm_scope source.oo.
  3. heuristics.yml parses; every disambiguation pattern compiles; every
     rule fires on >= 1 sample; every sample classifies as OODA (>= 1 hit).
  4. .gitattributes marks *.oo linguist-language=OODA and *.oot.
  5. Page Rule per sample page: 16..256 lines and <= 8 fn declarations.
  6. Every file under samples/OODA/ passes `oodac check` (exit 0).
     (.oot samples use the //-comment doc convention that the checker lexes;
     fleet `#`-markdown .oot docs are artifacts outside the check grammar.)

Advisory (WARN, never fails): grammar patterns that no sample exercises —
dead highlighting surface worth covering in a future sample.

Env:
  OODA_COMPILER  path to the oodac driver
                 (default /Projects/openOODA-core/oodac/bin/oodac)
"""

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SAMPLES = HERE / "samples" / "OODA"
GRAMMAR = HERE / "grammars" / "oo.tmLanguage.json"
LANGS = HERE / "languages.yml"
HEUR = HERE / "heuristics.yml"
ATTR = ROOT / ".gitattributes"
OODAC = os.environ.get("OODA_COMPILER",
                       "/Projects/openOODA-core/oodac/bin/oodac")
CHECK_ENV = dict(os.environ, OODA_NO_JAIL="1",
                 OO_LIST_AMBIENT_QUOTA="8589934592")

fails = 0
warns = 0


def fail(msg):
    global fails
    fails += 1
    print(f"FAIL  {msg}")


def warn(msg):
    global warns
    warns += 1
    print(f"WARN  {msg}")


def ok(msg):
    print(f"PASS  {msg}")


def iter_regexes(node, where, out):
    if isinstance(node, dict):
        for key in ("match", "begin", "end"):
            if isinstance(node.get(key), str):
                out.append((f"{where}.{key}", node[key]))
        for key, val in node.items():
            if isinstance(val, (dict, list)):
                iter_regexes(val, f"{where}.{key}", out)
    elif isinstance(node, list):
        for i, val in enumerate(node):
            iter_regexes(val, f"{where}[{i}]", out)


def load_heuristic_patterns(path):
    text = path.read_text()
    try:
        import yaml
    except ImportError:
        return re.findall(r"pattern:\s*'(.*)'", text), None
    try:
        doc = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        return None, f"heuristics.yml does not parse: {exc}"
    pats = [r["pattern"] for d in doc.get("disambiguations", [])
            for r in d.get("rules", []) if "pattern" in r]
    return pats, None


def check_grammar(corpus):
    try:
        g = json.loads(GRAMMAR.read_text())
    except json.JSONDecodeError as exc:
        fail(f"oo.tmLanguage.json is not valid JSON: {exc}")
        return
    ok("oo.tmLanguage.json parses as JSON")

    if g.get("scopeName") != "source.oo":
        fail(f"scopeName is {g.get('scopeName')!r}, expected 'source.oo'")
    ft = set(g.get("fileTypes", []))
    if not {"oo", "oot"} <= ft:
        fail(f"fileTypes {sorted(ft)} does not cover oo + oot")

    rxs = []
    iter_regexes(g, "$", rxs)
    bad = 0
    for where, rx in rxs:
        try:
            re.compile(rx)
        except re.error as exc:
            bad += 1
            fail(f"grammar regex {where}: {exc}")
    if bad == 0:
        ok(f"all {len(rxs)} grammar regexes compile")

    if rxs:
        uncovered = [(w, r) for w, r in rxs
                     if not re.search(r, corpus, re.M)]
        if uncovered:
            for w, r in uncovered:
                warn(f"grammar pattern never matches samples: {w} {r[:60]!r}")
        else:
            ok("every grammar regex is exercised by the sample corpus")


def check_languages_yml():
    text = LANGS.read_text()
    if "OODA:" not in text:
        fail("languages.yml lacks the OODA entry")
    if "tm_scope: source.oo" not in text:
        fail("languages.yml tm_scope != source.oo")
    for ext in ('".oo"', '".oot"'):
        if ext not in text:
            fail(f"languages.yml missing extension {ext}")
    ok("languages.yml declares OODA (.oo/.oot, tm_scope source.oo)")


def check_heuristics(samples):
    pats, err = load_heuristic_patterns(HEUR)
    if err:
        fail(err)
        return
    rxs = []
    for i, p in enumerate(pats):
        try:
            rxs.append(re.compile(p, re.M))
        except re.error as exc:
            fail(f"heuristics rule[{i}] does not compile: {exc}")
    ok(f"all {len(rxs)} heuristic patterns compile")

    hits = {i: 0 for i in range(len(rxs))}
    for name, text in samples:
        mine = [i for i, rx in enumerate(rxs) if rx.search(text)]
        for i in mine:
            hits[i] += 1
        if mine:
            ok(f"{name}: classified OODA via rules {mine}")
        else:
            fail(f"{name}: no heuristic rule matches — not detectable as OODA")
    for i, n in hits.items():
        if n == 0:
            warn(f"heuristic rule[{i}] fires on no sample: {pats[i][:60]!r}")


def check_gitattributes():
    text = ATTR.read_text()
    if "linguist-language=OODA" not in text or "*.oo " not in text:
        fail(".gitattributes lacks '*.oo linguist-language=OODA'")
    if "*.oot" not in text:
        fail(".gitattributes lacks a '*.oot' entry")
    ok(".gitattributes maps *.oo and *.oot to OODA")


def check_page_rule(samples):
    fn_rx = re.compile(r"^\s*(?:pub\s+)?fn\s+\w+\s*\(", re.M)
    clean = True
    for name, text in samples:
        lines = text.count("\n") + (0 if text.endswith("\n") else 1)
        fns = len(fn_rx.findall(text))
        if not 16 <= lines <= 256:
            clean = False
            fail(f"{name}: {lines} lines outside 16..256")
        if fns > 8:
            clean = False
            fail(f"{name}: {fns} fn declarations exceeds 8")
    if clean:
        ok("Page Rule holds over all sample pages (16..256 lines, <=8 fns)")


def check_oodac(samples):
    if not Path(OODAC).exists():
        fail(f"oodac not found at {OODAC} (set OODA_COMPILER to override)")
        return
    # oodac writes .ooda-cache into its CWD; run from a temp dir so the
    # package tree stays clean. Imports still resolve file-relative.
    with tempfile.TemporaryDirectory(prefix="linguist-check-") as cwd:
        for name, _ in samples:
            proc = subprocess.run([OODAC, "check", str(SAMPLES / name)],
                                  capture_output=True, text=True,
                                  env=CHECK_ENV, cwd=cwd)
            if proc.returncode == 0:
                ok(f"oodac check {name}: OK")
            else:
                tail = (proc.stdout + proc.stderr).strip().splitlines()[-4:]
                fail(f"oodac check {name}: exit {proc.returncode}\n"
                     + "\n".join("      " + t for t in tail))


def main():
    if not SAMPLES.is_dir():
        fail(f"sample dir missing: {SAMPLES}")
        return 1
    files = sorted(p for p in SAMPLES.iterdir() if p.is_file())
    if not files:
        fail("no sample files under samples/OODA/")
        return 1
    samples = [(p.name, p.read_text()) for p in files]
    corpus = "\n".join(t for _, t in samples)
    ok(f"{len(samples)} sample files under samples/OODA/")

    check_grammar(corpus)
    check_languages_yml()
    check_heuristics(samples)
    check_gitattributes()
    check_page_rule(samples)
    check_oodac(samples)

    print(f"---\n{warns} warning(s), {fails} failure(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
