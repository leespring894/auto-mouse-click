#!/bin/sh

source venv/bin/activate

set -x

pyside6-uic -g python MainDlg.ui -o MainDlg.py
