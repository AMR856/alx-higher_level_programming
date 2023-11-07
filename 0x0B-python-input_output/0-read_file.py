#!/usr/bin/python3
"""A program to read a file"""


def read_file(filename=""):
    """Here is the function for reading
        
    Args: The file name
    """
    with open(filename) as myFile:
        for line in myFile:
            print(line)
