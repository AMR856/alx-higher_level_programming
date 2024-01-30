#!/bin/bash
# A script to see options
curl -sI -X OPTIONS "$1" | sed -n '6p' | cut -d ':' -f 2 | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//'
