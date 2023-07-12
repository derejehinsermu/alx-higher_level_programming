#!/usr/bin/python3
"""
an implementation of the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of a class that inherited from the class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
