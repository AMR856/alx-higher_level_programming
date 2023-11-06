#!/usr/bin/python3
"""A class that inherits from the list"""


class MyList(list):
    """Here is the class"""
    def print_sorted(self):
        """A method to print the list sorted"""
        newList = sorted(self)
        print(newList)
