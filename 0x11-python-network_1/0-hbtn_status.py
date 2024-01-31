#!/usr/bin/python3
"""A script that uses some things to do things"""
import urllib.request
if __name__ == "__main__":
    theUrl = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(theUrl) as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
