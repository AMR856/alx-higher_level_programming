#!/usr/bin/python3
"""A script that uses some things to do things"""
import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    theUrl = sys.argv[1]
    values = {"email": sys.argv[2]}
    theFinalData = urllib.parse.urlencode(values)
    theFinalData = theFinalData.encode('ascii')
    theRequest = urllib.request.Request(theUrl, theFinalData)
    with urllib.request.urlopen(theRequest) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
