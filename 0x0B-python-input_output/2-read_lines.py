#!/usr/bin/python3
"""
This module contains the function read_lines
"""


def read_lines(filename="", nb_lines=0):
    """
    Function that returns the read of lines on a file
    """
    lines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            lines += 1

    if nb_lines <= 0 or nb_lines >= lines:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f.read(), end="")

    else:
        with open(filename, 'r', encoding='utf-8') as f:
            for i in range(nb_lines):
                print(f.readline(), end="")
