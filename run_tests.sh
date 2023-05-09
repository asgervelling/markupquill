#!/bin/bash

if [[ $1 == "-i" ]]; then
    pip install .
fi

python -m unittest discover -s app/markupquill/test -v
