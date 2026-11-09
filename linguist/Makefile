# OODA GitHub Linguist & editor-grammar package gate.
#
# `make check` runs the full validation: oo.tmLanguage.json parses and
# every regex compiles, languages.yml declares OODA, every heuristics.yml
# pattern compiles and classifies all samples as OODA, .gitattributes is
# wired, the Page Rule holds, and every sample in samples/OODA/ passes
# `oodac check` (OODA_COMPILER env overrides the compiler path).

.PHONY: check validate test
check validate test:
	python3 validate.py
