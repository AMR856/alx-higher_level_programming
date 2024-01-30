#!/bin/bash
# A script to get the size of something
curl -s "$1" | wc -c
