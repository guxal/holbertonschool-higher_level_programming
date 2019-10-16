#!/usr/bin/python3
""" My List Class Module """


class MyList(list):
    """
    Class MyList
    Inherits:
        @list: listing
    """
    def print_sorted(self):
        """function print sorted"""
        try:
            print(sorted(self))
        except:
            raise TypeError("unorderable types: int() < list()")
