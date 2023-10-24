class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, myPos):
        if myPos[0] >= 0 and myPos[1] >= 0 and myPos[0] <= self.size and \
            myPos[1] <= self.size \
                and isinstance(myPos, tuple) and len(myPos) == 2 and \
                    isinstance(myPos[0], int) and \
                        isinstance(myPos[1], int):
            self.__position = myPos
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__position[1] + self.__size):
            if i >= self.__position[1]:
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        myList = ""
        if self.__size == 0:
            myList += '\n'
            return myList
        for i in range(self.__position[1]):
            myList += '\n'
        for i in range(self.__size):
            myList += " " * self.__position[0] + "#" * self.__size + '\n'
        return myList.strip()
