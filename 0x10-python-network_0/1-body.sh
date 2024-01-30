#!/bin/bash
# A script to curlllllll
http_status=$(curl -s -L  -o /dev/null -w "%{http_code}" "$1")
response_body=$(curl -s -L "$1")
if [ $http_status -eq 200 ]; then
    echo -n "$response_body"
fi
