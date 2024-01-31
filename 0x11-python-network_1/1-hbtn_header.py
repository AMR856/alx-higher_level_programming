#!/usr/bin/python3
"""A script that uses some things to do things"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        theHeader = response.getheader("X-Request-Id")
        print(theHeader)
