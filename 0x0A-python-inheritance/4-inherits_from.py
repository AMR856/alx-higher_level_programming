#!/usr/bin/python3
"""A function to check inheritence"""


def inherits_from(obj, a_class):
    """Here is the function

    Args: The object
    The class"""
    if (a_class == object):
        return False
    return (isinstance(obj, a_class))
