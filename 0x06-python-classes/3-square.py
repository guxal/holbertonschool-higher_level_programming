#!/usr/bin/python3
class Square:
    """
    Class definition: Square

    Attributes:
        __size (int): square size private

    """
    def area(self):
        """ Function area

        Returns:
            int : area the square
        """
        return self.__size ** 2

    def __init__(self, size=0):
        """
        Args:
            size: square size

        Raises:
            TypeError: if size is not type int
            ValueError: if size is negative
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif int(size) >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
