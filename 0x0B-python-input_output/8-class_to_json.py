#!/usr/bin/python3
"""This module defines a function to convert an object's serializable attributes to a dictionary"""

def class_to_json(obj):
    """Returns a dictionary description with simple data structure attributes for JSON serialization"""
    if not hasattr(obj, '__dict__'):
        raise ValueError("Input object is not an instance of a class.")

    serializable_data = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_data[attr] = value

    return serializable_data