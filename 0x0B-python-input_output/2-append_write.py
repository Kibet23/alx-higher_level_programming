#!/usr/bin/python3
"""defines a function that appends a string"""


def append_write(filename="", text=""):
    """
    appends a string at the end of UTF8
    Args:
        filename: name of the file to be appended
        text: text to be appended

    Return:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
