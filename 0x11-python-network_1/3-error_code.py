#!/usr/bin/python3
"""A script that uses some things to do things"""
import urllib.request
import urllib.error
import sys
if __name__ == "__main__":
    theUrl = sys.argv[1]
    req = urllib.request.Request(theUrl)
    try:
        with urllib.request.urlopen(req) as response:
            thePage = response.read()
            print(thePage.decode('utf-8'))
    except urllib.error.HTTPEerror as e:
        print(f"Error code: {e.code}")
