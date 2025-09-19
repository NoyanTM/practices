.PHONY: build diagrams

diagrams:
	java -jar plantuml.jar ./diagrams/1.puml -o 1.png
	java -jar plantuml.jar ./diagrams/2.puml -o 2.png
	java -jar plantuml.jar ./diagrams/3.puml -o 3.png

build:
	pdflatex --output-directory=build report.tex
	biber ./build/report
	pdflatex --output-directory=build report.tex
