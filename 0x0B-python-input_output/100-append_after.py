#!/usr/bin/python3
"""defines search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of a text to a file, each line
    containing a specific string"""

    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
