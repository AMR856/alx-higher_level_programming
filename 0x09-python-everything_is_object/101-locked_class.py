#!/usr/bin/python3
"""Creating a locked class here"""


class LockedClass:
    """Here is my class and nothing speical about it"""
    __slots__ = ["first_name"]

    def __init__(self, first_name):
        self.first_name = first_name
