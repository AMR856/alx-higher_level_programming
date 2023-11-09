#!/usr/bin/python3
"""Here is my square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """Here is my rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """The init function of my square

        Args: The size of the square
        x: The x value
        y: The y value
        id: The id
        """
        super().__init__(size, size, x, y, id)

    """A setter and getter for my square"""
    @property
    def size(self):
        return self._Rectangle__width

    @size.setter
    def size(self, myValue):
        if type(myValue) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if myValue <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self._Rectangle__width = myValue
        self._Rectangle__height = myValue

    def __str__(self):
        """A str method for my square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self._Rectangle__x, self._Rectangle__y,
                self._Rectangle__width))

    def update(self, *args, **kwargs):
        """My update function that takes args but with 5 arguments

        The first: The id
        The second: The size
        The fourth: The x
        The fifth: The y
        """
        if args is None or len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            counter = 0
            for i in ['id', 'size', 'x', 'y']:
                if counter < len(args):
                    setattr(self, i, args[counter])
                    counter = counter + 1
                else:
                    break

    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
