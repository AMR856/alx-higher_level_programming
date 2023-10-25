#!/usr/bin/python3
import math
import dis
"""Making my own MagicClass"""


class MagicClass:
    "Here you can find my own class"

    def __init__(self, raduis):
        """The init of my class

        Args:
            The value of the raduis to be put

        """
        self.raduis = raduis
        if type(raduis) is not int and type(raduis) is not float:
            raise TypeError('radius must be a number')

    def area(self):
        """A method to the circumference of the circle"""
        return (math.pi * self.raduis ** 2)

    def circumference(self):
        """A method to the circumference of the circle"""
        return (2 * math.pi * self.raduis)
