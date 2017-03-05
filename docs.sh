#!/usr/bin/env bash

virtualenv --python=python3.5 .venv
source .venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)
pip3 install -r doc-requirements.txt
cd docs
make html