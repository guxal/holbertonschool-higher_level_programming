#!/usr/bin/python3

def add_attribute(cls, name, value):

    if hasattr(cls, "__dict__"):
        cls.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
