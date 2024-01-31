#!/usr/bin/python3
"""A script that uses some things to do things"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: ", html.__class__)
    print("\t- content: ", html)
    print("\t- utf8 content", html.decode('utf-8'))
