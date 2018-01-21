#!/bin/bash

cd code && python3 code.py;
cd ../latex && pdflatex -interaction=batchmode paper.tex;
biber paper && pdflatex -interaction=batchmode paper.tex && pdflatex -interaction=batchmode paper.tex;
cp paper.pdf ../results/;
cp textrank_example.png ../results/;

#docker tag handson blaabl/isp

#docker push blaabl/isp
