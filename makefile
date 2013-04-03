THESIS=thesis

all: $(THESIS)

thesis: $(THESIS).tex references.bib $(wildcard sections/*.tex) $(wildcard figures/*)
	pdflatex $(THESIS).tex
	bibtex $(THESIS)
	pdflatex $(THESIS).tex
	pdflatex $(THESIS).tex

.PHONY: clear clean

clear: 
	rm -rf $(THESIS).{aux,dvi,log,out,toc,lof,lot,bbl,blg,tpt}
	rm -rf sections/*.aux
	rm -rf *~ sections/*~

clean: clear
	rm -rf $(THESIS).pdf
