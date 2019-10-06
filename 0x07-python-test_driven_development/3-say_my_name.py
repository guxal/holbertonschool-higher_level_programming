#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    Error = "{} must be a string"
    if isinstance(first_name, str) is False:
        raise TypeError(Error.format("first_name"))
    if isinstance(last_name, str) is False:
        raise TypeError(Error.format("last_name"))
    if first_name is "" and last_name is "":
        print("My name is ")
    else:
        print("My name is {} {}".format(first_name, last_name))
