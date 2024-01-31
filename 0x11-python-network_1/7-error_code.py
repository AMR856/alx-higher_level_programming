#!/usr/bin/python3
"""A script that uses some things to do things"""
import requests
import sys

if __name__ == "__main__":
    theUrl = sys.argv[1]
    response = requests.get(theUrl)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.content.decode('utf-8'))
