all:	Kryptographie-Folien.pdf Kryptographie-Handout.pdf Kryptographie-Aufgaben.pdf

%.pdf: %.md
	@pandoc $(OPTIONS) $< -o $@

Kryptographie-Folien.pdf: OPTIONS += -t beamer --highlight-style kate

Kryptographie-Handout.pdf: OPTIONS += --toc

Kryptographie-Aufgaben.pdf: 

clean:
	@echo "cleaning..."
	@rm -f *~ *.pdf
	@echo "done."
