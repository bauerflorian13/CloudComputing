#!/bin/bash

pdflatex --halt-on-error cw1-97059-97133.tex && bibtex cw1-97059-97133 && pdflatex --halt-on-error cw1-97059-97133.tex && pdflatex --halt-on-error cw1-97059-97133.tex
