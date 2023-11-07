#!/usr/bin/python3
"""A function  to return a dic that represents the obj"""


def class_to_json(obj):
    """Here is the function

    Args: The obj"""
    theDic = obj.__dict__
    return theDic
