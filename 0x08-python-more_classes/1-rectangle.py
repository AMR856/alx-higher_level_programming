#!/usr/bin/python3
"""This is my class of the rectangle"""


class Rectangle:
    """Here is the class"""
    def __init__(self, width=0, height=0):
        """My init function of the rectangle

        Args:
            width: It's the width of my rectangle
            height: It's the height of my rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter for my width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter for my width

        Args: The value of the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The getter for my height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter for my height

        Args: The value of the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
