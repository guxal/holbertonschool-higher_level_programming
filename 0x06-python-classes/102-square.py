#!/usr/bin/python3
class Square:

    def area(self):
        return self.__size ** 2

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

    def __lt__(self, other):
        '''
        special method
        '''
        return (self.size < other.size)

    def __gt__(self, other):
        '''
        special method
        '''
        return (self.area() > other.area())

    def __le__(self, other):
        '''
        special method
        '''
        return (self.area() <= other.area())

    def __ge__(self, other):
        '''
        special method
        '''
        return (self.area() >= other.area())

    def __eq__(self, other):
        '''
        special method
        '''
        return (self.size == other.size)

    def __eq__(self, other):
        '''
        special method
        '''
        return (self.area() == other.area())
