#!/usr/bin/python3
""" define  a class_to_json function"""


def class_to_json(obj):
    """
    Returns a dictionary representation of a simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: The dictionary representation of the object suitable for JSON serialization.
    """
    json_dict = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value
        elif hasattr(attr_value, '__dict__'):
            json_dict[attr_name] = class_to_json(attr_value)

    return json_dict
