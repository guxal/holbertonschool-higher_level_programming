#!/usr/bin/python3
"""
This module contains the Class Base.
"""
import json


class Base:
    """
    Class Base

    Args:
        @__nb_objects: number of instances Class

    Parameters:
        @id: number the id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def integer_validator(self, name, value):
        """The function contains integer_validator
        Args:
            @name: name of error.
            @value: integer validate.
        Raises:
            @TypeError: {name} must be an integer.
            @ValueError: {name} must be > 0.
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value <= 0 and name not in ["x", "y"]:
            raise ValueError(name + " must be > 0")
        elif value < 0:
            raise ValueError(name + " must be >= 0")

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file classmethod: Write the JSON string
        in a file.
        Args:
            cls: the class itself.
            list_objs: a list of instances who inherits of Base.
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding="utf-8") as f:
            (f.write("[]") if list_objs is None
             else f.write(cls.to_json_string([b.to_dictionary()
                                             for b in list_objs])))

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string method
        Return:
            returns the JSON string representation of list_dictionaries
        """
        ld = list_dictionaries
        return json.dumps(ld) if ld is not None else "[]"
