#!/usr/bin/env bash

if [ ! -f "res/db/sets2cards.json" ]; then
    echo "Must first download and build db. Run 'make'"
    exit 1
fi

python3 scripts/get_images.py "$1"
