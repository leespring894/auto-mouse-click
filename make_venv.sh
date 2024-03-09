#!/bin/sh

set -x

python3 -m venv venv || exit 1

source venv/bin/activate || exit 1

venv/bin/pip install pyside6 pynput pyinstaller
