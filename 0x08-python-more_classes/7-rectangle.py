#!/usr/bin/python3
"""This is my class of the rectangle"""


class Rectangle:
    """Here is the class"""
    number_of_instances = 0
    print_symbol = '#'
    
    def __init__(self, width=0, height=0):
        """My init function of the rectangle

        Args:
            width: It's the width of my rectangle
            height: It's the height of my rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

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

    def area(self):
        """A method to get my area"""
        return self.__height * self.__width

    def perimeter(self):
        """A method to get the perimeter"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """It's a method to print some hashtags on the screen

        """
        myList = ""
        if self.__height == 0 or self.__width == 0:
            return myList
        for i in range(self.__height):
            myList = myList + (self.__width * str(self.print_symbol))
            if (i != self.__height - 1):
                myList = myList + '\n'
        myList.strip()
        return myList

    def __repr__(self):
        """A repr method that is used to create new instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """My deconstructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
