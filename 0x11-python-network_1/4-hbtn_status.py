#!/usr/bin/python3
"""A script that uses some things to do things"""
import requests 
if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.content.decode('utf-8'))}")
    print(f"\t- content: {response.content.decode('utf-8')}")
