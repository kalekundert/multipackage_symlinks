#!/usr/bin/env bash
set -x

venv=venv_pip
rm -rf $venv

python -m venv $venv
. $venv/bin/activate

pip install ./foo_pkg
pip install ./bar_pkg

python -c 'import foo; print(foo.name)'
python -c 'import foo.shared; print(foo.shared.name)'
python -c 'import bar; print(bar.name)'
python -c 'import bar.shared; print(bar.shared.name)'
