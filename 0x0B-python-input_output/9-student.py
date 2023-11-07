#!/usr/bin/python3
"""My student class"""


class Student:
    """Here is the class"""
    def __init__(self, first_name, last_name, age):
        """The init function of my class

        Args: The first name
        the last name
        the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """A function to return a dic that represents the obj"""
        return {'first_name': self.first_name,
                "last_name": self.last_name, "age": self.age}
