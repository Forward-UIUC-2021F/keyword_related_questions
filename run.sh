#!/bin/bash
WD=$1
KEYWORD=$2

cd $WD/matt-ho-keyword-related-questions

source env/bin/activate
python3 src/main.py "$KEYWORD"