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
            int: area the square
        """
        return self.__size ** 2

    def my_print(self):
        """Function my_print print the square

        Returns:
            str: string square with #
        """
        if self.size is 0:
            print("")
        else:
            for x in range(self.size):
                for t in range(self.size):
                    print("#", end="")
                print("")

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        int: __size getter method
        """
        return self.__size

    @size.setter
    def size(self, size):
        """int: setter method in the __size
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
