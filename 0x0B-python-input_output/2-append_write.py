#!/usr/python3
"""define a function called append_write"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
