#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for idx, value in new_dict.items():
        new_dict[idx] = value * 2
    return new_dict
