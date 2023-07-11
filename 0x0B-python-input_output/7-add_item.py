#!/usr/bin/python3
""" adds all arguments to a Python list and save them to a file """


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []


items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
