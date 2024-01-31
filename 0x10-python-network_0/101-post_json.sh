#!/bin/bash
# A script to send JSON
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
