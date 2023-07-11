#!/usr/bin/python3
""" define a function called save_to_json_file """


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The path and filename of the text file.

    Returns:
        None
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
