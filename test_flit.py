#!/usr/bin/env bash
set -x

venv=venv_flit
rm -rf $venv

python -m venv $venv
. $venv/bin/activate
pip install flit

(cd foo_pkg; python -m flit build)
(cd bar_pkg; python -m flit build)
(cd bar_pkg; python -m flit build --format sdist)
(cd bar_pkg; python -m flit build --format wheel)
