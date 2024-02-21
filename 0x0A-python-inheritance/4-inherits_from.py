#!/usr/bin/python3
"""defines Only sub class of"""


def inherits_from(obj, a_class):
    """checks for an object's instance of inherited class
    Args:
        obj (any): object to check
        a_class (type): class to be inherited
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
