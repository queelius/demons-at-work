# Makefile for "Demons at Work"
# Satirical horror novella. First-person demon narrator.

PDFLATEX = pdflatex -interaction=nonstopmode
MAIN     = demons_at_work
TEX      = $(MAIN).tex
PDF      = $(MAIN).pdf
EPUB     = $(MAIN).epub
PB_PDF   = $(MAIN)_paperback.pdf
PB_TEX   = $(MAIN)_paperback.tex

CHAPTERS = $(wildcard chapters/*.tex)
DEPS     = $(TEX) $(CHAPTERS)

# KDP / EPUB
EPUB_META   = kdp/metadata.yaml
EPUB_CSS    = kdp/kindle.css
EPUB_LUA    = kdp/epub-filter.lua
EPUB_DEPS   = $(DEPS) $(EPUB_META) $(EPUB_CSS) $(EPUB_LUA)

# HTML output
HTML_DIR = docs

# KDP paperback trim (5.5 x 8.5 for thin novella)
TRIM_W   = 5.5in
TRIM_H   = 8.5in
PB_MARGIN = 0.75in

AUX_EXTS = aux log out toc bbl blg lof lot fls fdb_latexmk synctex.gz latexml.log

.DEFAULT_GOAL := pdf

.PHONY: all pdf epub html paperback check wordcount clean distclean help

all: pdf epub  ## Build PDF and EPUB

# --- PDF (two-pass, letterpaper reading copy) ---
pdf: $(PDF)  ## Build PDF (default)

$(PDF): $(DEPS)
	$(PDFLATEX) $(TEX)
	$(PDFLATEX) $(TEX)
	@echo "Built: $@ ($$(pdfinfo $@ 2>/dev/null | grep Pages | awk '{print $$2}') pages)"

# --- Quick compile ---
check: $(DEPS)  ## Quick single-pass compile check
	$(PDFLATEX) $(TEX)
	@echo "Quick compile done (run 'make pdf' for full build)"

# --- EPUB (via pandoc, for Kindle / ebook) ---
epub: $(EPUB)  ## Build EPUB for Kindle

$(EPUB): $(EPUB_DEPS)
	pandoc $(TEX) \
		--from=latex \
		--to=epub3 \
		--mathml \
		--metadata-file=$(EPUB_META) \
		--css=$(EPUB_CSS) \
		--lua-filter=$(EPUB_LUA) \
		--epub-cover-image=kdp/cover-ebook.jpg \
		--epub-title-page=true \
		--toc \
		--toc-depth=1 \
		--split-level=1 \
		-o $(EPUB)
	python3 kdp/fix-epub.py
	@echo "Built: $@"

# --- HTML (via tex2html / LaTeXML) ---
html: $(DEPS)  ## Build HTML via tex2html
	tex2html $(TEX) -t modern -c floating-toc,dark-mode -o $(HTML_DIR)/
	@echo "Built: $(HTML_DIR)/"

# --- KDP paperback interior PDF (custom trim) ---
paperback: $(PB_PDF)  ## Build KDP paperback PDF (5.5 x 8.5)

$(PB_PDF): $(DEPS)
	@echo '\\PassOptionsToPackage{papersize={$(TRIM_W),$(TRIM_H)},margin=$(PB_MARGIN),inner=0.875in}{geometry}' > $(PB_TEX)
	@echo '\\input{$(TEX)}' >> $(PB_TEX)
	$(PDFLATEX) $(PB_TEX)
	$(PDFLATEX) $(PB_TEX)
	@echo "Built: $@ (trim $(TRIM_W) x $(TRIM_H), $$(pdfinfo $@ 2>/dev/null | grep Pages | awk '{print $$2}') pages)"

# --- Word count ---
wordcount:  ## Word counts per chapter
	@echo "Chapter word counts:"
	@for f in $(CHAPTERS); do \
		words=$$(detex "$$f" 2>/dev/null | wc -w); \
		printf "  %-40s %s\n" "$$f" "$$words"; \
	done
	@echo "---"
	@total=$$(cat $(CHAPTERS) 2>/dev/null | detex 2>/dev/null | wc -w); \
	printf "  %-40s %s\n" "TOTAL" "$$total"

# --- Cleanup ---
clean:  ## Remove aux files (preserve outputs)
	@for ext in $(AUX_EXTS); do \
		rm -f $(MAIN).$$ext $(MAIN)_paperback.$$ext; \
	done
	@rm -f $(PB_TEX)
	@rm -f chapters/*.aux
	@echo "Cleaned aux files."

distclean: clean  ## Remove all generated files
	rm -f $(PDF) $(EPUB) $(PB_PDF)
	rm -rf $(HTML_DIR)/
	@echo "Cleaned all output."

# --- Help ---
help:  ## Show targets
	@echo "Demons at Work -- Build System"
	@echo ""
	@echo "  make pdf         Build PDF, letterpaper reading copy (default)"
	@echo "  make check       Quick single-pass compile"
	@echo "  make epub        Build EPUB for Kindle/KDP"
	@echo "  make html        Build HTML via tex2html (LaTeXML + modern theme)"
	@echo "  make paperback   Build KDP paperback interior PDF (5.5 x 8.5 trim)"
	@echo "  make all         Build PDF + EPUB"
	@echo "  make wordcount   Word counts per chapter"
	@echo "  make clean       Remove auxiliary files"
	@echo "  make distclean   Remove all generated output"
	@echo "  make help        Show this message"
