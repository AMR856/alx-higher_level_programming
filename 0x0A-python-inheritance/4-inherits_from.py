#!/usr/bin/python3
"""A function to check inheritence"""


def inherits_from(obj, a_class):
    """Here is the function

    Args: The object
    The class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
