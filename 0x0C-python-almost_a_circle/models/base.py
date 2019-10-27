#!/usr/bin/python3
"""
This module contains the Class Base.
"""


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
            raise ValueError(name + " must be => 0")
