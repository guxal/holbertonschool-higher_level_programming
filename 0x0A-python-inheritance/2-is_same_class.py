#!/usr/bin/python3
""" Is_Same_Class Module """


def is_same_class(obj, a_class):
    """
    Returns:
        True is obj equal an a_class;
        otherwise False.

    Parameters:
        obj: object
        a_class: class

    """
    return type(obj) is a_class
