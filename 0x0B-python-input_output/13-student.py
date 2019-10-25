#!/usr/bin/python3
"""
This module contains the Class Student.
"""


class Student:
    """
    Class Student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializer new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Use magic method __dict__ return representation of class in json
        """
        if attrs is None:
            return self.__dict__
        else:
            ditc = self.__dict__
            return{z: ditc[z] for ot in attrs for z in ditc if z == ot}

    def reload_from_json(self, json):
        """
        Function replace JSON
        """
        for key in json:
            if key in self.__dict__.keys():
                self.__dict__[key] = json[key]
