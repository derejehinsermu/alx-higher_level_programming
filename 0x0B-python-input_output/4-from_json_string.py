#!/usr/bin/python3
"""This module defines a function to parse a JSON string and return a Python object"""

import json

def from_json_string(my_str):
    """Parses a JSON string and returns the corresponding Python data structure"""
    return json.loads(my_str)