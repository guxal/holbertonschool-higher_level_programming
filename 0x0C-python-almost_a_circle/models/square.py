#!/usr/bin/python3
"""
This module contains the Class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """init methods: use super for init square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """magic method __str__
        Return [Square] (<id>) <x>/<y> - <size>
        """
        _print = "[Square] ({}) {}/{} - {}"
        return _print.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value
