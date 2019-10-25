#!/usr/bin/python3
"""
This method contains the function class_to_json
"""


def class_to_json(obj):
    """
    Use magic method __dict__ for return json representative
    """
    return obj.__dict__
