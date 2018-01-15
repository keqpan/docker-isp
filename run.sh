#!/bin/bash

cd code && python code.py;
cd ../latex && pdflatex paper.tex;
biber paper && pdflatex paper.tex && pdflatex paper.tex;
cp paper.pdf ../results/;

#docker tag handson blaabl/isp

#docker push blaabl/isp
