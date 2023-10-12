#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object if it's possible."""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if possible, else raises a TypeError."""
    if hasattr(obj, attr_name):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute if the object can't have new attribute")