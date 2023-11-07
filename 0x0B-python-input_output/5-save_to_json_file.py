#!/usr/bin/python3
"""A function to write json obj to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Here is the function

    Args: The object
    The file
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
