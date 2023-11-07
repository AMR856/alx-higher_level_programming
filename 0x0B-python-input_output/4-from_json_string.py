#!/usr/bin/python3
"""A function to convert back to python"""
import json


def from_json_string(my_str):
    """Here is the function

    Args: The object"""
    return (json.loads(my_str))
