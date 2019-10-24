#!/usr/bin/python3
import json
"""
This module contains the function save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """
    Save json in file
    Return nothing
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
