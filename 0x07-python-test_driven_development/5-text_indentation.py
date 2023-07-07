#!/usr/bin/python3
""" Define a function called text_indentation(text)"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in "\n.?:":  # Group the punctuation marks for readability
            print("\n")
        c += 1

        while c < len(text) and text[c] == ' ':
            c += 1

