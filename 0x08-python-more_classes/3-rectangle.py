#!/usr/bin/python3
class Rectangle:
    """
    The Rectangle class create a new object

    Args:
        width (int): integer value of the width
        height (int): integer value of the height

    Attributes:
        width (int): integer value of the width
        height (int): integer value of the height

    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """
        Function area the rectangle

        Formule: width * height = area

        Returns:
            area

        """
        return self.width * self.height

    def perimeter(self):
        """
        Function petimeter the rectangle

        Formule: 2*(width + height)

        Returns:
            perimeter

        """
        w, h = self.width, self.height
        return 0 if (w or h) == 0 else 2*(w + h)

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set heigth"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __str__(self):
        __list = ""
        w, h = self.width, self.height
        if w == 0 or h == 0:
            _list = ""
        else:
            for x in range(h):
                for y in range(w):
                    __list += "#"
                if x != h - 1:
                    __list += '\n'

        return __list
