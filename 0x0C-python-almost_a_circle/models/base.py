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
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
