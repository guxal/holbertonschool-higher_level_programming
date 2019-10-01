#!/usr/bin/python3
class Square:

    def area(self):
        return self.__size ** 2

    def my_print(self):
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
        return self.__size

    @size.setter
    def size(self, size):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif int(size) >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
