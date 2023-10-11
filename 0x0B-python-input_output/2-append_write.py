#!/usr/bin/python3
"""This module defines a text file-appending function"""

def append_write(filename="", text=""):
    """Appends a string to the end of a text file (UTF8) and returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_added = file.write(text)
    return num_chars_added