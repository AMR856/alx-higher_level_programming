#!/usr/bin/python3
"""That is my base module"""
import json
import csv


class Base:
    """Here is my class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This is my init function

        Args:
            The value of the id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A method to return the json string represenatation

        Args: The dic to be converted
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """This is a method that can write my json files to a file

        Args: The list of objects
        """
        with open(f"{cls.__name__}.json", 'w', encoding='utf-8') as myFile:
            if list_objs is None:
                myFile.write("[]")
            myList = []
            for i in list_objs:
                myList.append(i.to_dictionary())
            myFile.write(Base.to_json_string(myList))

    @staticmethod
    def from_json_string(json_string):
        """A method to get the list back from json

        Args: The json string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A method to convert to csv

        Args: The list of objects
        """
        with open(f"{cls.__name__}.csv", 'w', encoding='utf-8') as myFile:
            if list_objs is None or len(list_objs) == 0:
                myFile.write("")
            else:
                if cls.__name__ == "Rectangle":
                    myFields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    myFields = ["id", "size", "x", "y"]
                myWriter = csv.DictWriter(myFile, myFields)
                for obj in list_objs:
                    myWriter.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """A method to load from a csv file

        Args: Nothing
        """
        try:
            with open(f"{cls.__name__}.csv", "r", encoding="utf-8") as myFile:
                if cls.__name__ == "Rectangle":
                    myFields = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    myFields = ["id", "size", "x", "y"]
                myReturnedList = []
                myListOfDic = csv.DictReader(myFile, myFields)
                myListOfDic = [dict([(myKey, int(myValue)) for myKey, myValue
                                    in miniD.items()])
                               for miniD in myListOfDic]
                for item in myListOfDic:
                    myReturnedList.append(cls.create(**item))
                return myReturnedList
        except FileNotFoundError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """A method to create the object

        Args: The kwargs for my update function
        """
        if cls.__name__ == "Rectangle":
            myDummyR = cls(1, 1, 0, 0, None)
            myDummyR.update(**dictionary)
            return myDummyR
        elif cls.__name__ == "Square":
            myDummyS = cls(1, 0, 0, None)
            myDummyS.update(**dictionary)
            return myDummyS

    @classmethod
    def load_from_file(cls):
        """A method to load an object from json file

        Args: Nothing
        """
        try:
            with open(f"{cls.__name__}.json", "r", encoding="utf-8") as myFile:
                myList = []
                theJsonString = myFile.read()
                mylistAfterJson = Base.from_json_string(theJsonString)
                for item in mylistAfterJson:
                    myList.append(cls.create(**item))
                return myList
        except FileNotFoundError:
            return []
