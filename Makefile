# Minimal makefile for Latex meeting protocol template
#

# You can set these variables from the command line, and also
# from the environment.
OUTDIR      	?= ./build
DOC						?= %ENTRYPOINT%

# Put it first so that "make" without argument is like "make help".
help:


.PHONY: help Makefile

# create PDF with xelatex
pdf: prebuild
	@xelatex -synctex=1 -interaction=nonstopmode -file-line-error -output-directory=$(OUTDIR) $(DOC)

prebuild:
	@/usr/bin/env python3 ./scripts/build.py

# clean buildfolder and create pdf
clean:
	@rm -R ./build
	@make pdf

push:
	@git push
	@git push "git@github.com:lufixSch/meeting-protocol-template.git"

# run setup script
init:
	@/usr/bin/env python3 ./scripts/setup.py