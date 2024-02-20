#!/usr/bin/python3
"""defines save object to a file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using JSON representation
    Args:
        my_obj: object to be written
        filename: name of the file to be written to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
