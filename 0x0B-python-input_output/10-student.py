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

    def to_json(self, attrs=None):
        myFlag = 1
        if attrs is None:
            return {'first_name': self.first_name,
                    "last_name": self.last_name, "age": self.age}
        for i in attrs:
            if type(i) is not str:
                myFlag = 0
                break
        if (myFlag == 1):
            myNewDic = {}
            for i in attrs:
                if i in self.__dict__:
                    myNewDic[i] = self.__dict__[i]
            return myNewDic
        else:
            return {'first_name': self.first_name,
                    "last_name": self.last_name, "age": self.age}
