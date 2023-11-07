#!/usr/bin/python3
"""A module to append text"""


def append_write(filename="", text=""):
    """A function to append

    Args: The file
    The text
    """
    with open(filename, 'a', encoding='utf-8') as myFile:
        return (myFile.write(text))
