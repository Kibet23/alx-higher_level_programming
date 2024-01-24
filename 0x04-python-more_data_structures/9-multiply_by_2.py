#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    returns a new dictionary with all values multiplied by 2
    Parameters:
    a_dictionary - dictionary to be checked
    """
    dict = {key: value * 2 for key, value in a_dictionary.items()}
    return (dict)
