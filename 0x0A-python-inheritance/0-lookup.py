#!/usr/bin/python3
"""defines Lookup"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""

    return [attr for attr in dir(obj)]
