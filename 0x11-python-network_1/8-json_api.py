#!/usr/bin/python3
"""A script that uses some things to do things"""
import requests
import sys

if __name__ == "__main__":
    theUrl = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    response = requests.post(theUrl, data = {"q" : letter})
    try:
        r = response.json()
        if r == {}:
            print("No result")
        else:
            print(f"[{r['id']}] {r['name']}")
    except ValueError:
        print("Not a valid JSON")
