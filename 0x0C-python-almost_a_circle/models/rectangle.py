#!/usr/bin/python3
"""Here is my rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Here is my rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Here is init function

        Args:
            width: The width of my rec
            height: The height of my rec
            x: The x value of my rec
            y: The y value of my rec
        """
        self.width = width
        self. height = height
        self.x = x
        self.y = y
        super().__init__(id)

    
    @property
    def width(self):
        """The getter and setter for my width"""
        return self.__width

    @width.setter
    def width(self, myValue):
        if type(myValue) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if myValue <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = myValue

    @property
    def height(self):
        """The getter and setter for my height"""
        return self.__height

    @height.setter
    def height(self, myValue):
        if type(myValue) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if myValue <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = myValue


    @property
    def x(self):
        """The getter and setter for my x"""
        return self.__x

    @x.setter
    def x(self, myValue):
        if type(myValue) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if myValue < 0:
            raise ValueError("{} must be > 0".format("x"))
        self.__x = myValue

    @property
    def y(self):
        """The getter and setter for my y"""
        return self.__y

    @y.setter
    def y(self, myValue):
        if type(myValue) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if myValue < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = myValue

    def area(self):
        """A method to get the area"""
        return self.__width * self.__height

    def display(self):
        """A method to print # on the screen"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """My str method for printing"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """My update function that takes args but with 5 arguments

        The first: The id
        The second: The width
        The third: The height
        The fourth: The x
        The fifth: The y
        """
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            counter = 0
            for i in ['id', 'width', 'height', 'x', 'y']:
                if counter < len(args):
                    setattr(self, i, args[counter])
                    counter = counter + 1
                else:
                    break

    def to_dictionary(self):
        """A function to get a dic that represents the object"""
        return {"id": self.id, "width": self.__width,
                "height": self.__height, "x": self.__x, "y": self.__y}
