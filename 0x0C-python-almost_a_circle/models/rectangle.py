#!/usr/bin/python3
"""
This module contains the Class Rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    This Class Rectangle inherit from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        Args:
            @width: width rectangle.
            @height: height rectangle.
            @x: x position
            @y: y position
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width
        Attributes:
            @__width: rectangle width
        Args:
            @value: rectangle width value
        """
        self.integer_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height
        Attributes:
            @__height: rectangle height
        Args:
            @value: rectangle height value
        """
        self.integer_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter x
        Attributes:
            @__x: x position
        Args:
            @value: x position value
        """
        self.integer_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter y
        Attributes:
            @__y: y position
        Args:
            @value: y position value
        """
        self.integer_validator("y", value)
        self.__y = value
