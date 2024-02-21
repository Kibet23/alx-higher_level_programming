#!/usr/bin/python3
"""defines class or inherit from"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance or if the object is
    an instance of a class that inherited from
    Args:
        obj (str): object in question
        a_class (type): The class to match thr type of object to.
    Returns:
        True if obj is an instance of of a class that is inherited from
        Otherwise false
    """
    if isinstance(obj, a_class):
        return True
    return False
