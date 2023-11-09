#!/usr/bin/python3
import json
import csv
"""My base module"""


class Base:
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
        with open (f"{cls.__name__}.json", 'w', encoding='utf-8') as myFile:
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
        with open (f"{cls.__name__}.csv", 'w', encoding='utf-8') as myFile:
            if list_objs is None:
                myFile.write("")
            myList = []
            for i in list_objs:
                myList.append(i.to_dictionary())
            csv_writer = csv.writer(myFile)
            csv_writer.writerows(myList)

    def load_from_file_csv(cls):
        pass