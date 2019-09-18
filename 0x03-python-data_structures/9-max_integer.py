#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return (None)
    _max = my_list[0]
    for i in my_list[:]:
        if (_max < i):
            _max = i
    return (_max)
