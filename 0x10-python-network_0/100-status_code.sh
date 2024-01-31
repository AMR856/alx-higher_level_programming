#!/bin/bash
# A script to get the status code
curl -s -o /dev/null --write-out "%{http_code}" "$1"
