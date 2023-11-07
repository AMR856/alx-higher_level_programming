#!/usr/bin/python3
"""A function to get an object from the file"""
import json


def load_from_json_file(filename):
    """Here is the function

    Args: The file name
    """
    with open(filename, 'r', encoding='utf-8') as myFile:
        myData = json.load(myFile)
        return (myData)
