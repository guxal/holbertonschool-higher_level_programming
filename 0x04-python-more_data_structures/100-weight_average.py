#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return 0
    (num, den) = 0, 0
    for value in my_list:
        (num, den) = (num + value[0] * value[1]), den + value[1]
    return num / den
