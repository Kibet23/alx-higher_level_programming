#!/usr/bin/python3
"""defines a write function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8).

    Args:
        filename (str): name of the file to be written
        text (str): text to be written to the file
    Return:
        number of characters written"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
