#!/usr/bin/python3
""" 
unction that returns True if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the class; otherwise False.
    """
    return type(obj) is a_class
