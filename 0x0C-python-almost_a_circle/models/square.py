#!/usr/bin/python3
"""
This module contains the Class Square.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square inherits Rectangle.
    """
    def update(self, *args, **kwargs):
        """update method
        Args:
            @args: is the list of arguments - no-keyworded arguments
            @kwargs: double pointer to a dictionary: key/value
        """
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    super(Rectangle, self).__init__(arg)
                if idx == 1:
                    self.size = arg
                if idx == 2:
                    self.x = arg
                if idx == 3:
                    self.y = arg
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    super(Rectangle, self).__init__(value)
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def __init__(self, size, x=0, y=0, id=None):
        """init methods: use super for init square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        """magic method __str__
        Return [Square] (<id>) <x>/<y> - <size>
        """
        _print = "[Square] ({}) {}/{} - {}"
        return _print.format(self.id, self.x, self.y, self.width)
