#!/usr/bin/python3
import json
"""
This module contains the function load_from_json_file
"""


def load_from_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
