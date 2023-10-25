#!/usr/bin/python3
"""Making my own MagicClass that is unknown until now"""
import math


class MagicClass:
    "my MagicClass"

    def __init__(self, raduis=0):
        """The init of my class

        Args:
            raduis: The value of the raduis
        """

        if type(raduis) is not int and type(raduis) is not float:
            raise TypeError('radius must be a number')
        self.__raduis = raduis

    def area(self):
        """A method to the circumference of the circle"""
        return (math.pi * (self.__raduis ** 2))

    def circumference(self):
        """A method to the circumference of the circle"""
        return (2 * math.pi * self.__raduis)
