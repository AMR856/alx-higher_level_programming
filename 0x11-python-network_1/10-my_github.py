#!/usr/bin/python3
"""A script that uses some things to do things"""
import requests
import sys
from requests.auth import HTTPBasicAuth
if __name__ == "__main__":
    theAuth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=theAuth)
    print(response.json().get('id'))
