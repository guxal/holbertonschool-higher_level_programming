#!/usr/bin/python3
""" lookup module """


def lookup(obj):
    """
    Returns:
        available attributes and methods of the object
    Parameters:
        obj: object analize
    """
    return list(dir(obj))
