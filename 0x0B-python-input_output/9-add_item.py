#!/usr/bin/python3
"""
This Script save the JSON and the file add_item.json
"""

import sys
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

name_file = "add_item.json"

if not os.path.exists(name_file):
    with open(name_file, "w", encoding='utf-8') as f:
        f.write("[]")

new_list = load_from_json_file(name_file)
argc = len(sys.argv)
for i in range(1, argc):
    new_list += [sys.argv[i]]

save_to_json_file(new_list, name_file)
