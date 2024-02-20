#!/usr/bin/python3
"""defines class to JSON"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure for
    JSON serialization
    Args:
        obj: instance of a class
    """
    serialized_obj = {}
    """dictionary of attributes from the object"""
    attributes = obj.__dict__

    """iterate through the attributes"""
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            """Add key-value pair to the serialized object"""
            serialized_obj[key] = value

    return serialized_obj
