# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
STATICDIR     = _static

# Put it first so that "make" without argument is like "make help".
.PHONY: help Makefile
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo "Home made rules:"
	@echo "  pandoc      to convert the README from markdown to ReST format"
	@echo "  doc         to make man, epub, latexpdf and html documentation (see their rules)"

# Compile all data and generate full documentation
.PHONY: doc
doc: apidoc pandoc html latexpdf epub man

# convert the README from markdown to ReST format"
.PHONY: pandoc
pandoc:
	pandoc --from=markdown --to=rst --output="$(SOURCEDIR)/readme.rst" ../README.md

# autodoc App modules
.PHONY: apidoc
apidoc:
	sphinx-apidoc -o "$(SOURCEDIR)/api" ..
	python ../manage.py graph_models --pydot -a -g -o "$(SOURCEDIR)/api/app_uml_class_diagram.png"

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
