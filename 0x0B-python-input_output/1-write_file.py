#!/usr/bin/python3
"""A program to write to a file"""


def write_file(filename="", text=""):
    """My function

    Args: The file we want to write to
    the Text to be written
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return (myFile.write(text))
