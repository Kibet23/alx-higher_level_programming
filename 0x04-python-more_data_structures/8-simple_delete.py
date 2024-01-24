#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """"
    Deletes a key in a dictionary
    Parameters:
    a_dictionary - the dictionary to have the keys deleted from
    key - key to be deleted
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
