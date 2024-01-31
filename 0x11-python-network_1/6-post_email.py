#!/usr/bin/python3
"""A script that uses some things to do things"""
import requests
import sys

if __name__ == "__main__":
    theUrl = sys.argv[1]
    theEmail = sys.argv[2]
    r = requests.post(theUrl, data={"email": theEmail})
    print(r.text)
