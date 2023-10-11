#!/usr/bin/python3
"""This module defines a function to load an object from a JSON file"""

import json

def load_from_json_file(filename):
    """Loads an object from a JSON file"""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)