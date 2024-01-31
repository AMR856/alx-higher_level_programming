#!/usr/bin/python3
"""A script that uses some things to do things"""
import requests
import sys
if __name__ == "__main__":
    theUrl = sys.argv[1]
    response = requests.get(theUrl)
    print(response.headers.get("X-Request-Id"))
