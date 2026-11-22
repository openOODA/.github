# OODA GitHub Linguist & editor-grammar package gate (pure .oo).
#
# `make check` compiles and runs validate.oo over oo.tmLanguage.json,
# languages.yml, heuristics.yml, .gitattributes, the Page Rule, and
# `ooda-compiler check` over every sample in samples/OODA/ (OODA_COMPILER overrides).

OODA_COMPILER ?= $(HOME)/.openooda/bin/ooda-compiler
RESOLVED_COMP := $(if $(wildcard $(OODA_COMPILER)),$(OODA_COMPILER),$(HOME)/.openooda/bin/ooda-compiler)
OODA_STANDARD_ROOT ?= $(HOME)/.openooda/ooda-standard
OODA_RUNTIME_ROOT ?= $(HOME)/.openooda/bin
OO_LIST_AMBIENT_QUOTA ?= 8589934592

.PHONY: check validate test clean
check validate test:
	@mkdir -p .ooda-cache
	@cd .. && env -u OODA_OODAR_ROOT -u OODA_OOSTD_ROOT OO_LIST_AMBIENT_QUOTA=$(OO_LIST_AMBIENT_QUOTA) OODA_NO_JAIL=1 \
		OODA_COMPILER="$(RESOLVED_COMP)" \
		OODA_STANDARD_ROOT="$(OODA_STANDARD_ROOT)" OODA_RUNTIME_ROOT="$(OODA_RUNTIME_ROOT)" \
		"$(RESOLVED_COMP)" build linguist/validate.oo -o linguist/.ooda-cache/validate
	@cd .. && env -u OODA_OODAR_ROOT -u OODA_OOSTD_ROOT OO_LIST_AMBIENT_QUOTA=$(OO_LIST_AMBIENT_QUOTA) OODA_NO_JAIL=1 \
		OODA_COMPILER="$(RESOLVED_COMP)" \
		OODA_STANDARD_ROOT="$(OODA_STANDARD_ROOT)" OODA_RUNTIME_ROOT="$(OODA_RUNTIME_ROOT)" \
		./linguist/.ooda-cache/validate .

clean:
	@rm -rf .ooda-cache
