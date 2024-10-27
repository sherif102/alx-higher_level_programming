#!/usr/bin/python3
"""
Module: 7-add_item.py
Author: Sheriff Abdulfatai
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    file = load_from_json_file(filename)
except FileNotFoundError:
    file = []
file.extend(sys.argv[1:])
save_to_json_file(file, filename)