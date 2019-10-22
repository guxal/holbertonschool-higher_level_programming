#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        intval = self.integer_validator
        intval("height", height)
        intval("width", width)

        self.__width = width
        self.__height = height
