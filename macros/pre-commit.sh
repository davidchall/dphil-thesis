#!/bin/bash

./macros/texcount.pl -opt=macros/texcount_options.txt thesis.tex > macros/texcount_output.txt
./macros/drawCharts.py
git add macros/texcount_output.txt
git add macros/wordcount.txt
git add macros/stats.html

