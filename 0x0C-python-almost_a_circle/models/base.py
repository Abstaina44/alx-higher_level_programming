#!/usr/bin/python3

"""Base Class"""

import json


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """Returns JSON string of parameter
            Args:
                list_dictionaries: Input parameter
            Returns:
                JSON string fo parameter
        """

        if (list_dictionaries == None or
                len(list_dictionaries) == 0):
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string"""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                obj_list = cls.from_json_string(json_data)
                return [cls.create(**obj_dict) for obj_dict in obj_list]
        except FileNotFoundError:
            return []
