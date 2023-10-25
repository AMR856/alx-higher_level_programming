#!/usr/bin/python3
"""Making a new class called Square"""


class Square:
    """My square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Making the size attibute private and assigning its value

        Args:
            size :It's the size of the created object
            position: It's a tuple that idk
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """A getter for the size"""
        return self.__size

    @property
    def position(self):
        """A getter for the position"""
        return self.__position

    @position.setter
    def position(self, myPos):
        """A setter for the position

        Args:
            The tuple that is used to set the values

        """
        if isinstance(myPos, tuple) and len(myPos) == 2 \
            and isinstance(myPos[0], int) and isinstance(myPos[1], int) \
                and myPos[0] >= 0 and myPos[1] >= 0:
            self.__position = myPos
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        """A setter for the size

        Args:
            value of the size of the to be set

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Getting the area of the square

        """
        return self.__size * self.__size

    def my_print(self):
        """It's a method to print some hashtags on the screen

        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
    def __str__(self):
        """It's a method to print some hashtags on the screen

        """
        myList = ""
        if self.__size == 0:
            return myList
        for i in range (self.__position[1]):
            myList = myList + '\n'
        for i in range(self.__size):
            myList = myList + ((" " * self.__position[0] + "#" * self.__size))
            if (i != self.__size - 1):
                myList = myList + '\n'
        myList.strip()
        return myList
