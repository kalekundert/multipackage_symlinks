#!/usr/bin/env bash
set -x

venv=venv_build
rm -rf $venv

python -m venv $venv
. $venv/bin/activate
pip install build

python -m build foo_pkg
python -m build bar_pkg
