#!/bin/sh

source venv/bin/activate

pyinstaller --icon=icon/AutoMouseClick.icns --windowed AutoMouseClick.py

