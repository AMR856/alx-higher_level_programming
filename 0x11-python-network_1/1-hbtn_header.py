#!/usr/bin/python3
"""A script that uses some things to do things"""
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    theHeader = response.getheader("X-Request-Id")
    print(theHeader)
