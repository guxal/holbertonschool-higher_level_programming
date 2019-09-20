#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for idx in sorted(a_dictionary.items()):
        print("{}: {}".format(idx[0], idx[1]))
