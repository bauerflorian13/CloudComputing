#!/bin/bash


# I have NEVER tested the script below



# LAST always contains last commands output
BASEFILE="cw1-97059-97133"

# Compile .tex to latex
if [ ! -f $BASEFILE.pdf ]; then
  killall Preview
fi
latex --halt-on-error $BASEFILE.tex && bibtex $BASEFILE && latex --halt-on-error $BASEFILE.tex && pdflatex --halt-on-error $BASEFILE.tex

if [ $? -eq 0 ]; then
  if [ $(lsappinfo info -only name `lsappinfo front` | sed 's/"//g') == "LSDisplayName=Preview" ]; then
    killall Preview
  fi

  open -a preview $BASEFILE.pdf
  exit 0
else
  rm -rf $BASEFILE.acn
  rm -rf $BASEFILE.acr
  rm -rf $BASEFILE.alg
  rm -rf $BASEFILE.aux
  rm -rf $BASEFILE.dvi
  rm -rf $BASEFILE.glg
  rm -rf $BASEFILE.glo
  rm -rf $BASEFILE.gls
  rm -rf $BASEFILE.idx
  rm -rf $BASEFILE.ist
  rm -rf $BASEFILE.log
  rm -rf $BASEFILE.out
  rm -rf $BASEFILE.pdf
  rm -rf $BASEFILE.toc
  rm -rf $BASEFILE.xdy0

  exit 1
fi
